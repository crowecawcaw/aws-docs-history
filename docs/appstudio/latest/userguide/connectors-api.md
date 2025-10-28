# Connect to third-party services and APIs (generic)

Use the following procedure to create a generic **API Connector** in App Studio. The **API Connector** is used to
provide App Studio apps with access to third-party services, resources, or operations.

###### To connect to third-party services with the **API Connector**

1.  In the left-side navigation pane, choose **connectors** in the **Manage** section.
    You will be taken to a page displaying a list of existing connectors with some details about each.
2.  Choose **+ Create connector**.
3.  Choose **API Connector**. Now, configure your connector by filling out the following fields.
4.  **Connector name:** Provide a name for your connector.
5.  **Connector description:** Provide a description for your connector.
6.  **Base URL:** The website or host of the third-party connection. For example, `www.slack.com`.
7.  **Authentication method:** Choose the method for authenticating with the target service.
    - **None:** Access the target service with no authentication.
    - **Basic:** Access the target service using a **Username** and **Password** obtained from the service being
      connected to.
    - **Bearer Token:** Access the target service using the **Token value** of an authentication token obtained from the service's user
      account or API settings.
    - **OAuth 2.0:** Access the target service using the OAuth 2.0 protocol, which grants App Studio access to the service and resources without sharing any
      credentials or identity. To use the OAuth 2.0 authentication method, you must first create an application from the service being connected to that represents
      App Studio to obtain the necessary information. With that information, fill out the following fields:
      1.  **Client credentials flow:** Ideal for system-to-system interactions where the application acts on its own behalf without user interaction. For example, a CRM app
          that updates Salesforce records automatically based on new records added by users, or an app that retrieves and displays transaction data in reports.

              1. In **Client ID**, enter the ID obtained from the OAuth app created in the target service.
              2. In **Client secret**, enter the secret obtained from the OAuth app created in the target service.
              3. In **Access token URL**, enter the token URL obtained from the OAuth app created in the target service.
              4. Optionally, in **Scopes**, enter the scopes for the application.
               Scopes are permissions or access levels required by the application. Refer to the target service's API documentation to understand
               their scopes, and configure only those that your App Studio app needs.

          Choose **Verify connection** to test the authentication and connection.

      2.  **Authorization code flow:** Ideal for applications that require acting on behalf of a user. For example, a customer support app where users log in and
          view and update support tickets, or a sales app where each team members logs in to view and manage their sales data.
          1. In **Client ID**, enter the ID obtained from the OAuth app created in the target service.
          2. In **Client secret**, enter the secret obtained from the OAuth app created in the target service.
          3. In **Authorization URL**, enter the authorization URL from the target service.
          4. In **Access token URL**, enter the token URL obtained from the OAuth app created in the target service.
          5. Optionally, in **Scopes**, enter the scopes for the application.
             Scopes are permissions or access levels required by the application. Refer to the target service's API documentation to understand
             their scopes, and configure only those that your App Studio app needs.

8.  **Headers:** Add HTTP headers that are used to provide metadata about the request or response. You can add both
    keys and values, or only provide a key to which the builder can provide a value in the application.
9.  **Query parameters:** Add query parameters that are used to pass options, filters, or data as part of the request URL. Like headers,
    you can provide both a key and value, or only provide a key to which the builder can provide a value in the application.
10. Choose **Create**. The newly created connector will appear in the **Connectors** list.
    Now that the connector is created, builders can use it in their apps.
