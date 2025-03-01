## Deployment 
- **Deployment URL (Frontend)**: https://cze4yzrdmbnlspydvig9ki.streamlit.app/
- **Deployment URL (Backend)**: https://api-298313983231.us-central1.run.app/
- The frontend has been deployed in streamlit, and the backend has been deployed in GCP artifact registry using Gloud Run.
- Reference (Backend): https://blog.devgenius.io/deploy-a-flask-app-with-docker-google-cloud-run-and-cloud-sql-for-postgresql-6dc9e7f4c434

## GraphQL
- **Link**: https://api-298313983231.us-central1.run.app/graphql
  
## Overview
This project is a Django-based API with the following key features:
- **SQLite database**: The database for storing user and location data.
- **Search Location API**: Uses Google Maps **Places API** for searching and saving locations.
- **Save Location API**: Allows users to save locations to their profiles.
- **JWT Authentication**: Uses JSON Web Tokens for secure user authentication.

---

## API Endpoints

### 1. **Authentication**

#### a) **Register User**
- **Endpoint**: `/api/register/`
- **Method**: `POST`
- **Description**: Register a new user and authenticate with JWT.
- **Payload**:
    ```json
    {
      "username": "testuser",
      "email": "testuser@example.com",
      "password": "testpassword"
    }
    ```
- **Response Example**:
    ```json
    {
      "username": "testuser",
      "email": "testuser@example.com"
    }
    ```

#### b) **Login User**
- **Endpoint**: `/api/login/`
- **Method**: `POST`
- **Description**: Authenticate an existing user and receive JWT tokens.
- **Payload**:
    ```json
    {
      "username": "testuser",
      "password": "testpassword"
    }
    ```
- **Response Example**:
    ```json
    {
      "access": "YOUR_ACCESS_TOKEN",
      "refresh": "YOUR_REFRESH_TOKEN"
    }
    ```

---

### 2. **Search Location API**
- **Endpoint**: `/api/search-location/`
- **Method**: `GET`
- **Description**: Search for locations using Google Maps Places API.
- **Payload**:
    - `query`: The search term (e.g., a place name or address).
    - `location`: Optional. Latitude and longitude for proximity-based search.
    - `radius`: Optional. Search radius in meters.
- **Example Request**:  
  `http://127.0.0.1:8000/api/search-location/?query=restaurant`

- **Response Example**:
    ```json
    {
      "results": [
        {
          "name": "Sample Location",
          "address": "123 Example Street",
          "latitude": 40.7128,
          "longitude": -74.0060
        }
      ]
    }
    ```
![WhatsApp Image 2025-01-25 at 8 57 13 PM](https://github.com/user-attachments/assets/6466dff1-4193-4fec-a64b-525730eb2831)

---

### 3. **Save Location API**
- **Endpoint**: `/api/save-location/`
- **Method**: `POST`
- **Description**: Save a location to the user's profile.
- **Payload**:
    ```json
    {
      "latitude": 40.7128,
      "longitude": -74.0060,
      "name": "Sample Location",
      "address": "123 Example Street"
    }
    ```
- **Response Example**:
    ```json
    {
      "status": "success",
      "message": "Location saved successfully"
    }
    ```

---

### 4. **GraphQL Endpoint**
- **Endpoint**: `/graphql/`
- **Method**: `POST`
- **Description**: Use GraphQL for querying and mutating data.
- **Sample Query**:
    ```graphql
    query {
      searchLocation(query: "New York") {
        name
        address
        latitude
        longitude
      }
    }
    ```
- **Response Example**:
    ```json
    {
      "data": {
        "searchLocation": [
          {
            "name": "New York",
            "address": "New York, NY, USA",
            "latitude": 40.7128,
            "longitude": -74.0060
          }
        ]
      }
    }
    ```

![image](https://github.com/user-attachments/assets/907476ee-4bda-4809-a219-f6a54b15c246)

---

## Setup Instructions (Local environment)

1. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

2. Migrate the database:
    ```bash
    python manage.py migrate
    ```

3. Run the development server:
    ```bash
    python manage.py runserver
    ```

4. Access the GraphQL API at:
    ```plaintext
    http://127.0.0.1:8000/graphql/
    ```

5. Use Google Maps API for location-related features.

---
