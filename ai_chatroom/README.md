# AI Chatroom

## Description

AI Chatroom is a web application that allows users to create and join chatrooms with AI bots and other users. It provides a platform for dynamic and engaging conversations, enhanced by the presence of customizable AI personalities.

## Main Features

*   **User Registration and Login:** Securely create accounts and log in to access the application.
*   **Chatroom Creation:** Create new chatrooms with custom names and descriptions.
*   **Bot Integration:** Add AI bots with unique personalities to your chatrooms.
*   **Real-time Chat:** Engage in real-time conversations with other users and bots.
*   **Chatroom Settings:** Customize chatroom settings such as theme, maximum number of users, and public/private visibility.

## Technologies Used

*   **Backend:**
    *   FastAPI: A modern, fast (high-performance), web framework for building APIs with Python.
    *   SQLAlchemy: A powerful SQL toolkit and Object-Relational Mapping (ORM) system.
    *   Psycopg2: The most popular PostgreSQL database adapter for Python.
    *   Passlib: For password hashing and security.
    *   Pydantic: For data validation and settings management.
*   **Database:**
    *   PostgreSQL: A robust, open-source relational database management system.
*   **Server:**
    *   Uvicorn: An ASGI server for running FastAPI applications.
*   **Others:**
    * pip: For package management
    * curl: For testing endpoints.

## Prerequisites

*   Python 3.8+
*   PostgreSQL installed and running
*   `pip` package manager

## Setup and Installation

1.  **Clone the Repository:**
```
bash
    git clone <repository_url>
    cd ai_chatroom
    
```
2.  **Create and Activate a Virtual Environment:**
```
bash
    python3 -m venv venv
    source venv/bin/activate  # On Linux/macOS
    venv\Scripts\activate  # On Windows
    
```
3.  **Install Dependencies:**
```
bash
    pip install -r requirements.txt
    pip install pydantic[email]
    pip install passlib
    
```
4.  **Database Setup:**
    *   Create a PostgreSQL database.
    *   Create a user and grant access to the database.
    *   Update the `DATABASE_URL` in `app/database/database.py` or set it as an environment variable:
```
bash
    export DATABASE_URL="postgresql://<user>:<password>@localhost/<database_name>"
    
```
5. Create the tables in the database:
```
bash
    python -m app.database.create_tables
    
```
## How to Run the App

1.  **Activate the Virtual Environment:**
```
bash
    source venv/bin/activate  # On Linux/macOS
    venv\Scripts\activate  # On Windows
    
```
2.  **Start the Uvicorn Server:**
```
bash
    uvicorn app.main:app --reload
    
```
3.  **Access the App:**
    *   Open your web browser and go to the url provided in the terminal or go to http://127.0.0.1:8000/.

## How to Run the Tests

*   **Coming Soon:** We don't have tests at this time.

## How to Add New Features

1.  **Create a New Route:**
    *   In the `app/routers` directory, create a new `.py` file for your feature or add to an existing file.
    *   Define your route using FastAPI's `@router` decorator.

2.  **Create a New Schema:**
    *   If needed, create a new schema in the `app/schemas` directory to define the data structure.

3.  **Update the database:**
    * If you need to add a new database table, you will need to add a new model to app/models.

4.  **Include the Router:**
    *   Import your new router into `app/main.py` and include it in the `app` using `app.include_router()`.

5.  **Restart Uvicorn:**
    *   Restart the Uvicorn server to load the changes.

## Licensing

*   This project is licensed under the MIT License.

## Contact

*   \[Your Name] - \[Your Email]

## Contributors

*   \[Your Name]

## Future Improvements

*   **Complete Chatroom Functionality:** Implement full CRUD operations for chatrooms.
*   **Bot Customization:** Allow users to fully customize bot personalities and behaviors.
*   **WebSockets for Real-Time Chat:** Implement WebSockets for real-time chat functionality.
*   **User Authentication:** Add more advanced user authentication and authorization features (JWT).
*   **OAuth Integration:** Allow users to login using google and facebook.
*   **Error Handling:** Implement more robust error handling and validation.
*   **Testing:** Implement unit and integration tests.
* **UI/UX:** Design a more complete frontend.
* **Deployment:** Create a full deployment pipeline.
* **Logging:** Implement improved logging and monitoring.