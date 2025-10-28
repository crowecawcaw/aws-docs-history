# Set up the JWT bearer OAuth flow for Salesforce

Refer to Salesforce public documentation for enabling server-to-server integration with [OAuth 2.0 JSON Web Tokens](https://help.salesforce.com/s/articleView?id=sf.remoteaccess_oauth_jwt_flow.htm "https://help.salesforce.com/s/articleView?id=sf.remoteaccess_oauth_jwt_flow.htm").

Once you have created a JWT and configured the connected app appropriately in Salesforce, you can create a new Salesforce connection with the `JWT_TOKEN` key set in your Secrets Manager Secret. Set the OAuth grant type to **JWT Bearer Token** when creating the connection.
