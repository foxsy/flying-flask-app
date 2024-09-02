from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello, World!"

@app.route("/sayhello")
def sayhello():
    # Get the args from URL called 'name'
    args_name = request.args.get('name')

    # Set an empty string that we can use as a return
    hello_string = ""

    # If there is no name arg in the url we just give a generic hello
    if not args_name:
        hello_string = "Hello there, stranger!"

    else:
        hello_string = f'Howdy {args_name}!'
    return hello_string

@app.route("/submit-contact", methods=['POST'])
def submit_contact():
    # Get the json body and store it in the data var
    data = request.get_json()

    # If the body is empty, return a 400 with error
    if not data:
        return jsonify({"error": "Invalid or missing JSON data"}), 400

    # Get the individual fields in the JSON passed
    name = data.get('name')
    email = data.get('email')

    # If either are empty, it's not valid for parsing so return a 400 with error
    if not name or not email:
            return jsonify({"error": "Missing required fields"}), 400

    # We made it this far, so this is where we would process and store the data to a database or do some
    # action with a third-party API, since that's not the goal now, we will just return a 200 with some details
    return jsonify({"message": "Contact submitted successfully", "name": name, "email": email}), 200

@app.route("/combined-data", methods=['PATCH'])
def combined_data():
    # Set the endpoint for the third-party api
    api_url = "https://jsonplaceholder.org/users/1"
    data = {
        "name": "John Doe",
        "email": "johndoe@example.com"
    }

    # Call the API in a try/except block to handle errors
    try:
        response = requests.get(api_url)

        # Check if the request was successful
        response.raise_for_status()

        # Parse the JSON response from the external API
        external_data = response.json()

        # Get the birthDate field in the response
        birth_date = external_data.get('birthDate')

        # Add the birth date field to our user dict
        data["birth_date"] = birth_date

        # Return the dict as json
        return jsonify(data), 200

    except requests.exceptions.HTTPError as http_err:
        # Handle HTTP errors (4xx and 5xx responses)
        return jsonify({"error": f"HTTP error occurred: {http_err}"}), response.status_code

    except requests.exceptions.RequestException as err:
        # Handle all other types of errors
        return jsonify({"error": f"An error occurred: {err}"}), 500
