# Connect to services with OpenAPI

To connect App Studio with services using OpenAPI to enable builders to build applications that send requests and receive responses from the services,
perform the following steps:

1. [Get the OpenAPI Specification file and gather service information](#connectors-openapi-create-resources "#connectors-openapi-create-resources")
2. [Create OpenAPI connector](#connectors-openapi-create-connector "#connectors-openapi-create-connector")

## Get the OpenAPI Specification file and gather service information

To connect a service to App Studio with OpenAPI, perform the following steps:

1. Go to the service that you want to connect to App Studio and find an OpenAPI Specification JSON file.

###### Note

App Studio supports OpenAPI Specification files that conform to version OpenAPI Specification Version 3.0.0 or higher. 2. Gather the necessary data to configure the OpenAPI connector, including the following:

    * The base URL for connecting to the service.
    * Authentication credentials, such as a token or username/password.
    * If applicable, any headers.
    * If applicable, any query parameters.

## Create OpenAPI connector

###### To create a connector for OpenAPI

1.  Navigate to App Studio.
2.  In the left-side navigation pane, choose **Connectors** in the **Manage** section.
    You will be taken to a page displaying a list of existing connectors with some details about each.
3.  Choose **+ Create connector**.
4.  Choose **OpenAPI Connector** from the list of connector types. Now, configure your connector by filling out the following fields.
5.  **Name:** Enter a name for your OpenAPI connector.
6.  **Description:** Enter a description for your OpenAPI connector.
7.  **Base URL:** Enter the base URL for connecting to the service.
8.  **Authentication method:** Choose the method for authenticating with the target service.
    - **None:** Access the target service with no authentication.
    - **Basic:** Access the target service using a **Username** and **Password** obtained from the service being
      connected to.
    - **Bearer Token:** Access the target service using the **Token value** of an authentication token obtained from the service's user
      account or API settings.
    - **OAuth 2.0:** Access the target service using the OAuth 2.0 protocol, which grants App Studio access to the service and resources without sharing any
      credentials or identity. To use the OAuth 2.0 authentication method, you must first create an application from the service being connected to that represents
      App Studio to obtain the necessary information. With that information, fill out the following fields:
      1.  **Client credentials flow:**

              1. In **Client ID**, enter the ID from the target service.
              2. In **Client secret**, enter the secret from the target service.
              3. In **Access token URL**, enter the token URL from the target service.
              4. Optionally, in **Scopes**, enter the scopes for the application.
               Scopes are permissions or access levels required by the application. Refer to the target service's API documentation to understand
               their scopes, and configure only those that your App Studio app needs.

          Add any **Variables** to be sent with the service with each call, and choose **Verify connection** to test the authentication and connection.

      2.  **Authorization code flow:**
          1. In **Client ID**, enter the ID from the target service.
          2. In **Client secret**, enter the secret from the target service.
          3. In **Authorization URL**, enter the authorization URL from the target service.
          4. In **Access token URL**, enter the token URL from the target service.
          5. Optionally, in **Scopes**, enter the scopes for the application.
             Scopes are permissions or access levels required by the application. Refer to the target service's API documentation to understand
             their scopes, and configure only those that your App Studio app needs.

9.  **Variables:** Add variables to be sent to the service with each call. Variables added during configuration are
    securely stored and only accessed during runtime of applications that use the connection.
10. **Headers:** Add HTTP headers that are used to provide metadata about the request or response. You can add both
    keys and values, or only provide a key to which the builder can provide a value in the application.
11. **Query parameters:** Add query parameters that are used to pass options, filters, or data as part of the request URL. Like headers,
    you can provide both a key and value, or only provide a key to which the builder can provide a value in the application.
12. **OpenAPI Spec File:** Upload an OpenAPI Specification JSON file by dragging and dropping, or choosing
    **Select a file** to navigate your local file system and choose the file to be uploaded.

Once added, the file is
processed and a list of available options are displayed. Select the necessary operations for your connector. 13. Choose **Create**. The newly created connector will appear in the **Connectors** list.

Now that the connector is created, builders can use it in their apps.
