# Country Dialing Code API Documentation

This FastAPI project provides information about countries, including their names, dialing codes, and country codes. It reads this information from a JSON file and exposes an endpoint to retrieve these data.

## Installation and Setup

Before running the API, you'll need to install the required dependencies. You can do this using pip:

```bash
pip install fastapi uvicorn pydantic
```

## Running the API

To start the FastAPI server, run the following command:

```bash
uvicorn your_script_name:app --host 0.0.0.0 --port 8080
```

Replace `your_script_name` with the name of the Python script where your FastAPI app is defined. If your script is named `main.py`, the command would be:

```bash
uvicorn main:app --host 0.0.0.0 --port 8080
```

This will start the server on the specified port or on the default port 8080 if the `PORT` environment variable is not set.

## Endpoint

The API has a single endpoint for retrieving information about countries with dialing codes:

- **GET /countries-with-dialing-code**

  This endpoint returns a JSON response containing a list of countries with their names, dialing codes, and country codes.

  Example response:

  ```json
  [
    {
      "name": "Brazil",
      "dial_code": "+55",
      "code": "BR"
    },
    {
      "name": "United States",
      "dial_code": "+1",
      "code": "US"
    },
    ...
  ]
  ```

## API Response

The response JSON format is defined by the `Country` Pydantic model, which includes the following fields:

- `name`: The name of the country.
- `dial_code`: The dialing code of the country.
- `code`: The country code.

## Configuration

You can configure the port on which the server runs by setting the `PORT` environment variable. If the `PORT` environment variable is not set, the server will use the default port 8080.

## Error Handling

If any errors occur while reading the JSON file or processing the request, the API will return a JSON response with an `"error"` field containing an error message.

## Contribution

If you wish to contribute to this project or make improvements, feel free to fork the repository, make the necessary changes, and submit a pull request.

## License

This project is licensed under the MIT License. Please refer to the [LICENSE](LICENSE) file for more details.

We hope this documentation helps you set up and use the Country Dialing Code API. If you have any questions or need further information, please don't hesitate to get in touch.

## Create by:
**[Francisco Inoque](https://www.franciscoinoque.tech/)**
