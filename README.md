# Car Management Application (car-assessmentObjective)

This is a Car Management Application where users can create, view, edit, and delete cars. Each car can contain up to 10 images (specifically of a car), a title, a description, and tags such as `car_type`, `company`, `dealer`, etc. The application includes user authentication, allowing users to manage only their own cars, and provides search functionality across all cars.

## Features

### User Authentication
1. **Sign Up / Login**: Users can create an account or log in with existing credentials to access the application.
2. **Car Management**: Users can add, edit, view, and delete their cars.

### Car Management
1. **Add Car**: Users can add a car with up to 10 images, a title, a description, and tags (such as `car_type`, `company`, `dealer`, etc.).
2. **View Cars**: Users can view a list of all the cars they have added.
3. **Edit Car**: Users can update the title, description, tags, and images of any of their cars.
4. **Delete Car**: Users can delete any car they have added.
5. **Global Search**: Users can search through their cars based on the title, description, or tags. The application will list cars whose attributes match the keyword.

### Frontend Requirements
1. **Sign Up / Login Page**: A page that allows users to register and log in to access their cars.
2. **Product List Page**: Displays a list of all the cars created by the logged-in user, with a search bar to filter results.
3. **Product Creation Page**: A form for uploading an image, setting a title, and writing a description for a new car.
4. **Product Detail Page**: Displays a car’s details with options to edit or delete it.

## API Endpoints

The following API endpoints are available to interact with the backend service:

1. **Create User**
   - **POST** `/api/users/signup`: Create a new user with a username and password.
   - **POST** `/api/users/login`: Log in to an existing account.

2. **Car Management**
   - **POST** `/api/cars`: Create a new car with images, title, description, and tags.
   - **GET** `/api/cars`: List all cars added by the logged-in user.
   - **GET** `/api/cars/{id}`: Retrieve details of a specific car by its ID.
   - **PUT** `/api/cars/{id}`: Update the title, description, tags, or images of a car.
   - **DELETE** `/api/cars/{id}`: Delete a specific car by its ID.

3. **Search**
   - **GET** `/api/cars/search`: Search through cars based on the title, description, or tags.

### Documentation
- An API documentation route `/api/docs` will be available that provides detailed information about all the available APIs, request parameters, authentication requirements, and response structure. Tools like **Swagger** or **Postman** can be used for documentation.

## Tech Stack

- **Frontend**: Choose any frontend framework (e.g., React, Angular, Vue.js, etc.) that makes API calls to the backend.
- **Backend**: You can use any backend framework (e.g., Flask, Django, Express.js, etc.) to serve the APIs.
- **Database**: Any database can be used (e.g., SQLite, PostgreSQL, MongoDB, etc.) to store user and car data.
- **Image Storage**: The application can store images locally or use cloud storage (e.g., AWS S3, Cloudinary).
- **Cloud Hosting**: Deploy the application on a cloud provider such as **Heroku**, **Vercel**, **AWS**, etc.

## Instructions

### 1. Clone the Repository

Clone this repository to your local machine:

```bash
git clone https://github.com/your-username/car-assessment.git
cd car-assessment
