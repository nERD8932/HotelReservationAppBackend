# Reserver Backend

Reserver is an app that lets you find and reserve hotel rooms. This repository contains the Django-based backend for the same.

## Installation

- Clone the repository with

```bash
git clone https://github.com/nERD8932/HotelReservationAppBackend.git
```

- Use [pip](https://pip.pypa.io/en/stable/) to install requirements.

```bash
pip install -r requirements.txt
```

- Run the Django server

```bash
cd HotelReservationAppBackend
python manage.py startserver
```

## Usage

To access the deployed version of the website, go to [nerd8932.pythonanywhere.com](https://nerd8932.pythonanywhere.com/)

The website URL structure is as follows:

---

- /media - Used to get background images used in the app
  - Method: **GET**
  
---
- /location - Used to retrieve all accessible locations in the app, along with image data
  - Method: **GET**
  
---
- /search - Used to search for available hotels based on the URL Query Parameters:
  - Method: **GET**
  - Format: ?startDate=`[YYYY-MM-DD]`&endDate=`[YYYY-MM-DD]`&location=`[location name, or empty for no filtering]`
  - **Note:** All fields need to be included for the request to be conidered valid.
  
---
- /add-hotel/ - Used to add a hotel entry to the database.
  - Method: **POST**
  - Format: A `form-data` (Fields: hotel_name - Text, location - Text, image - File) POST request with an Authentication: Bearer `TOKEN` header. The default admin auth token is `Y4T6MDxj33`. This can (and should) be changed through the Django Admin page.
  - Example cURL Request:
    ```bash
    curl --location '127.0.0.1:8000/add-hotel/'
    --header 'Authorization: Bearer ••••••'
    --form 'hotel_name="Sunrise Lodge"'
    --form 'location="Toronto"'
    --form 'image=@"bE82DPhW7/hilton-grand-vacations.jpg"'
    ```
---
- /pull: Used to pull the latest GitHub commit.
  - Method: **POST**
  - Format: A POST request with an Authentication: Bearer `TOKEN` header. The token must match with the username `admin` (as added in the `api_tokens` table)

## Contributing

The project isn't maintained actively, on account of being made primarily for a college assignment, but feel free to clone it.

