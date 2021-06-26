import json
import requests
from django.core.management.base import BaseCommand, CommandError
from csv import reader, writer
from api.models import Customer


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('csv_name')
        parser.add_argument('--input_csv_path', default= r"C:\Users\felli\Desktop\test\django-api-exercise\insert_csv_here" , help="Please, inform the location where your csv file is located")
        parser.add_argument('--output_csv_path', default= r"C:\Users\felli\Desktop\test\django-api-exercise\output_csv\output.csv" , help="Please, inform the location where the output csv will be located")
        parser.add_argument('--key_path', default= r"C:\Users\felli\Desktop\test\django-api-exercise\insert_api_key_here\api-key.txt" , help="Please, inform the location where your Google API key is located")

    def handle(self, *args, **options):
        print('Starting the function...')
        # API key
        print('Getting your Google API key...')
        api_file = open(options["key_path"],"r")
        api_key = api_file.read()
        api_file.close()

        # base Google API url
        url = "https://maps.googleapis.com/maps/api/geocode/json?"

        if ".csv" not in options['csv_name']:
            raise CommandError("Please, provide a valid .csv archive.")
            return

        with open(f"{options['input_csv_path']}\{options['csv_name']}", 'r', newline = '') as read_obj, \
             open(options["output_csv_path"], 'w', newline='') as write_obj:

            print(f'Reading the csv file : {options["csv_name"]}')
            csv_reader = reader(read_obj)
            csv_writer = writer(write_obj)

            count_header = 1

            for row in csv_reader:
                if count_header == 1:
                    print('Validating the archive')
                    if row[6] != "city":
                        print(f"Sorry, the 7th column should contain the 'city' tag to keep going with the importation. The currently value is : '{row[6]}'.")
                        break
                    else:
                        print('Validation succeed!')
                    count_header += 1

                else:
                    city = row[6]

                    # get response
                    response = requests.get(url+"address=" + city + "&key=" + api_key)
                    response = response.json()

                    print(f"\ncsv_row : {row[0]}, City : '{city}', Request status : {response['status']}")

                    if response["status"] == "OK":
                        lat = response["results"][0]["geometry"]["location"]["lat"]
                        lng = response["results"][0]["geometry"]["location"]["lng"]
                        print(f"Coordinates(latitude, longitude) : {lat}, {lng}")

                        # Inserting the values into the csv file:
                        row.append(lat)
                        row.append(lng)

                        csv_writer.writerow(row)

                        #Inserting the values into the database:
                        try:
                            obj = Customer.objects.get(req_status = response["status"], 
                                                        first_name = row[1],
                                                        last_name = row[2],
                                                        email = row[3],
                                                        gender = row[4],
                                                        company = row[5],
                                                        city = row[6],
                                                        title = row[7],
                                                        lat = row[8],
                                                        lgn = row[9])
                        except Customer.DoesNotExist:
                            obj = Customer(req_status = response["status"], 
                                            first_name = row[1],
                                            last_name = row[2],
                                            email = row[3],
                                            gender = row[4],
                                            company = row[5],
                                            city = row[6],
                                            title = row[7],
                                            lat = row[8],
                                            lgn = row[9])
                            obj.save()
                            print('Saved to the database!\n')
                    else:
                        print("Coordinate not found.")

                        try:
                            obj = Customer.objects.get(req_status = response["status"], 
                                                        first_name = row[1],
                                                        last_name = row[2],
                                                        email = row[3],
                                                        gender = row[4],
                                                        company = row[5],
                                                        city = row[6],
                                                        title = row[7],
                                                        lat = "Not found.",
                                                        lgn = "Not found.")
                        except Customer.DoesNotExist:
                            obj = Customer(req_status = response["status"], 
                                            first_name = row[1],
                                            last_name = row[2],
                                            email = row[3],
                                            gender = row[4],
                                            company = row[5],
                                            city = row[6],
                                            title = row[7],
                                            lat = "Not found.",
                                            lgn = "Not found.")
                            obj.save()
                            print('Saved to the database!')
                            row.append("Coordinate not found.")
                        csv_writer.writerow(row)
                        pass
        
        self.stdout.write(self.style.SUCCESS(f"\n{options['csv_name']} importation succeed!\n\nYou can also see the csv_output at:\n\t{options['output_csv_path']}"))


