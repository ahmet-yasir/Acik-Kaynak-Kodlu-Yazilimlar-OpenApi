# Flask User Management API
This Flask application provides a simple REST API for managing user data, including creating, reading, updating, and deleting user information stored in a JSON file. The API supports basic validations for user inputs such as name, phone, and email.

# Features  
List all users  
Add a new user  
Get a specific user's details  
Update existing user data  
Delete a user  
# Prerequisites  
Docker installed on your machine. Download from Docker's website if needed.  

## Installation and Setup
### Clone the repository
```bash
git clone https://github.com/ahmet-yasir/Acik-Kaynak-Kodlu-Yazilimlar-OpenApi.git
```
```bash
cd Acik-Kaynak-Kodlu-Yazilimlar-OpenApi
```
### Building the Docker Container
Build the Docker image:  
```bash
docker build -t flask-user-management .
```
### Running the Application
Run your Flask application inside a Docker container:  
```bash
docker run -dp 5000:5000 flask-user-management
```

# API Endpoints
The application provides the following endpoints:  

GET /users - Retrieve a list of all users.  
POST /users - Add a new user. Requires JSON input specifying name, phone, and email.  
GET /users/<int:user_index> - Retrieve details of a specific user.  
PUT /users/<int:user_index> - Update an existing user. Requires JSON input specifying name, phone, and email.  
DELETE /users/<int:user_index> - Delete a specific user.  
# Example Usage
## 1. GET /users - Retrieve a list of all users
To fetch all users from the API:

```bash
curl -X GET http://localhost:5000/users
```
## 2. POST /users - Add a new user
To add a new user by sending JSON data:

```bash
curl -X POST http://localhost:5000/users \
-H "Content-Type: application/json" \
-d '{"name": "John Doe", "phone": "1234567890", "email": "john.doe@example.com"}'
```
## 3. GET /users/int:user_index - Retrieve details of a specific user
To get details of a specific user (replace <user_index> with the actual user index):

```bash
curl -X GET http://localhost:5000/users/0
```
## 4. PUT /users/int:user_index - Update an existing user
To update an existing user's details (replace <user_index> with the actual user index):

```bash
curl -X PUT http://localhost:5000/users/0 \
-H "Content-Type: application/json" \
-d '{"name": "Jane Doe", "phone": "0987654321", "email": "jane.doe@example.com"}'
```
## 5. DELETE /users/int:user_index - Delete a specific user
To delete a specific user (replace <user_index> with the actual user index):

```bash
curl -X DELETE http://localhost:5000/users/0
```
## Notes:
URL: In all these examples, the base URL http://localhost:5000 assumes that your Flask application is running locally on port 5000. If you are accessing the API deployed on a different server or port, adjust the URL accordingly.

Data Formats: Make sure that the JSON data you send is properly formatted. Also, update field values like name, phone, and email as per your API's validation rules.

User Index: In your API, it appears that user data is accessed via an index (user_index). Ensure that this index is valid, i.e., there is a user at that position in your data array. For new deployments, you may initially not have any data, so attempts to access or update a user at a non-existent index will result in an error.  

These curl commands provide a basic CLI-based method to test and interact with your Flask API. For more advanced usage, including error handling and dynamic data processing, consider using API testing tools like Postman or writing scripts in a programming language such as Python using libraries like requests.  
 
# Contributing  
Contributions are what make the open-source community such an amazing place to learn, inspire, and create. Any contributions you make are greatly appreciated.  

If you have a suggestion that would make this better, please fork the repo and create a pull request. You can also simply open an issue with the tag "enhancement".
Don't forget to give the project a star! Thanks again!  

# Fork the Project
Create your Feature Branch (git checkout -b feature/AmazingFeature)  
Commit your Changes (git commit -m 'Add some AmazingFeature')  
Push to the Branch (git push origin feature/AmazingFeature)  
Open a Pull Request  
# License
Distributed under the MIT License. See LICENSE for more information.
