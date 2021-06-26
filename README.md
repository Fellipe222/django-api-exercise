# django-api-exercise
<h2>Overall :</h2>
That's a brief django-rest application, whom has two endpoints. Those endpoints provide information that was fetched through a .csv archive. 

<h2>Project specifications :</h2>

Basically, this project can be segregated in the steps below:
- Read the csv file provided by the user
- With the values contained in the "city" column, retrieve the cordinates (latitude and longitude) trhough Google Geolocation API
- Update the database (in this case, sqlite) with the data 
- Make an csv output file from the processed data, just to be redundant
- Build an api with those data, with an overall endpoint, and another one, just retrieving the information of a specific 'id'
- Make a api documentation, expliciting witch and what the existing endpoint returns

<h2>How to use?</h2>
- Open up CMD and type the path, where the code is located and press ENTER:
<img src="https://user-images.githubusercontent.com/56563965/123497803-e2039c00-d605-11eb-93bd-964e502c7330.png">

- Type: python manage.py <b>importcsv</b> (the file with will be inserted into the database) and press ENTER:<br>
  <b>Note:</b> if the 7th row data won't be "city", an error will be raised.
 <img src="https://user-images.githubusercontent.com/56563965/123497806-e62fb980-d605-11eb-8aa5-d227e84ef05a.png">
 
 - Now, you need to provide you Google API key:
 <img src="https://user-images.githubusercontent.com/56563965/123498468-71a94a80-d606-11eb-8bfe-e33b998d9896.png">
 
 - Inform the path where the csv file is located:
 <img src="https://user-images.githubusercontent.com/56563965/114295037-f7424300-9a78-11eb-896b-d77e8673662c.png">
 
 - Inform the path where the output file is located (in my case, it'll be located at the same folder):
 <img src="https://user-images.githubusercontent.com/56563965/114295066-44261980-9a79-11eb-80b7-84f13d47ded0.png">
 
 - Once finished the importation, you are going to see this message:
 <img src="https://user-images.githubusercontent.com/56563965/123498625-905c1100-d607-11eb-83d0-24d0a907b0b4.png">
 
 - Done that, you're ready to run the server. Now, just type "python manage.py runserver" and press ENTER once more:
 <img src="https://user-images.githubusercontent.com/56563965/123498649-b386c080-d607-11eb-90af-8dadab8e421c.png">
 
 - Go to your web browser and paste the IP adress shown at CMD and... ENTER again:
 <img src="https://user-images.githubusercontent.com/56563965/114295642-e5629f00-9a7c-11eb-9801-84846eec98ee.png">
 
 - To get access to the entire registers storaged into the database, just go to <a href="http://127.0.0.1:8000/customer/">The customer's tab</a>
 
 - To get a specific piece of information about some customer, just specify its 'id' at the end:
 <img src="https://user-images.githubusercontent.com/56563965/114295829-0d063700-9a7e-11eb-88a3-d370844809d9.png">
 
 <h2>API documentation</h2>
 - The API documentation is availabe at "http://127.0.0.1:8000/doc/"
 <img src="https://user-images.githubusercontent.com/56563965/123498669-ca2d1780-d607-11eb-9d46-b9b0c499df63.png">
 
