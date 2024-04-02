# Workout-tracking-programme
This is a simple workout tracking programme with pixela API
This Python code interacts with the Pixela API, which is a service for creating customizable graphs to track various activities over time. Let's break down what each part of the code does:

Import Statements: The code imports the necessary modules, requests for making HTTP requests, and datetime for working with dates and times.

Constants:

USER_NAME: Your Pixela username.
TOKEN: Your Pixela token.
GRAPH_ID: Unique identifier for the graph.
Endpoints:

pixela_endpoint: Base URL for Pixela API.
User Registration:

The code prepares parameters for user registration with Pixela API. It includes your username, token, and agreement to terms of service.
requests.post() is used to send a POST request to register the user. This part is currently commented out.
Graph Creation:

The code prepares parameters for creating a graph. It includes details like graph ID, name, unit, type, and color.
requests.post() is used to send a POST request to create the graph. This part is currently commented out.
Pixel Creation:

The code prepares data for creating a pixel on the graph, representing today's date and the quantity (in kilometers cycled) obtained from user input.
requests.post() is used to send a POST request to add a pixel to the graph.
Pixel Update:

The code prepares data for updating a pixel on the graph. In this case, it's updating today's pixel with a new quantity.
requests.put() is used to send a PUT request to update the pixel. This part is currently commented out.
Pixel Deletion:

The code prepares the endpoint for deleting today's pixel on the graph.
requests.delete() is used to send a DELETE request to remove the pixel. This part is currently commented out.
Overall, this code demonstrates how to interact with the Pixela API to create, update, and delete pixels on a graph tracking cycling activity.






