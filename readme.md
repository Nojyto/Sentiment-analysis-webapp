# Foobar

footext

## Project Structure

The project is organized as follows:

- **ml_model/**: holds model training contents
- **webapp/**: Contains the main Flask application, including routes, models, and templates.
  - **static/**: Stores static assets like CSS, JavaScript, and images.
  - **templates/**: Holds HTML templates for different views.
  - **models.py**: Defines the SQLAlchemy model for logging predictions.
  - **model.py**: Loads the trained machine learning model.
  - **routes.py**: Contains the route definitions and application logic.
  - ****init**.py**: Initializes and configures the Flask app and database.

## Installation

1. Clone the repository:
2. Set up a virtual environment and activate it:

    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
    ```

3. Install the dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Run main.ipynb to setup model.

## Usage

For debug and development to start the application, run:

```bash
python app.py
```

For production on the server run:

```bash
sudo git clone <repository_url> /var/www/flaskwebapp
sudo chmod +x /var/www/flaskwebapp/setup_flask_app.sh
sudo /var/www/flaskwebapp/setup_flask_app.sh
```
