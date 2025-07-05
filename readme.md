# Mini Event Management System

The **Mini Event Management System** is a lightweight, containerized web application built with Django and Django REST Framework. It provides a clean API for creating events and managing attendee registrations, with built-in validation, caching, and auto-generated API documentation via Swagger.

## Features

### Event Management

- Create events with name, location, start time, end time, and maximum capacity.
- Retrieve a list of all upcoming events via a RESTful API.

### Attendee Registration

- Register users to specific events using their name and email.
- Prevent duplicate registrations for the same event based on email.
- Automatically block new registrations once an event reaches full capacity.

### Performance Optimization

- Utilizes Redis to cache registered emails for each event.
- Speeds up duplicate registration checks by avoiding redundant database queries.

### Deployment

- Fully Dockerized using Docker and Docker Compose.
- Includes isolated containers for Django, PostgreSQL, and Redis.
- Simple to set up, deploy, and scale in any environment.

### API Documentation

- Interactive Swagger.
- Access live API docs.
- Clean and OpenAPI-compliant documentation for easy integration and testing.

## Technologies Used

- **Backend**: Python, Django, Django REST Framework
- **API Docs**: drf-spectacular (Swagger UI)
- **Database**: PostgreSQL, SQLite (for development)
- **Caching**: Redis
- **DevOps**: Docker, Docker Compose


## Installation

### Prerequisites

- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)

### Setup

1. **Clone the repository:**

   ```bash
   git clone https://github.com/codewithmanuu/event-management-system.git


2. **Build and start the services using Docker Compose:**

   ```bash
   sudo docker-compose up --build

   ```windows
   docker-compose up --build

3. **Make migrations and migrate**

   ```bash
   - sudo docker-compose exec django python manage.py makemigratios event_app
   - sudo docker-compose exec django python manage.py migrate

   ```windows
   - docker-compose exec django python manage.py makemigratios event_app
   - docker-compose exec django python manage.py migrate

3. **Create a superuser for accessing the Django admin panel:**

   ```bash
   sudo docker-compose exec django python manage.py createsuperuser

   ```windows
   docker-compose exec django python manage.py createsuperuser

## 🚀 Usage

- Access the Swagger API documentation at [http://localhost:8000/api/v1/docs/](http://localhost:8000/api/v1/docs/)
- Use the **`POST /events`** endpoint to create a new event by providing:
  - `name`, `location`, `start_time`, `end_time`, and `max_capacity`.
- Use the **`GET /events`** endpoint to list all upcoming events.
- Use the **`POST /events/{event_id}/register`** endpoint to register a user for a specific event by submitting:
  - `name` and `email` in the request body.
  - Automatically checks for duplicates and prevents overbooking.
- Use the **`GET /events/{event_id}/attendees`** endpoint to retrieve a list of all registered attendees for a specific event.
- Access the Django admin panel at [http://localhost:8000/admin/](http://localhost:8000/admin/) to manage events and attendees directly.


## Development
 
1. **Use the following command to stop and remove containers:**

   ```bash
   sudo docker-compose down

   ```windows
   docker-compose down

2. **Use the following command to rebuild images and start services:**

   ```bash
   sudo docker-compose up --build

   ```windows
   docker-compose up --build

