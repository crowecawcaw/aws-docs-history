# Getting started with Session Manager API

The Amazon DCV Session Manager API provides an automated interface for managing remote desktop sessions. Through this
API, developers can create, list, start, stop, and otherwise control DCV sessions programmatically.
This allows for the integration of Amazon DCV functionality into custom applications and workflows. By
leveraging this API, organizations can streamline the management of remote visualization workloads, automating many common tasks.

Before you can start making calls to the Amazon DCV API, you'll need to obtain an access token that authenticates your application
and authorizes it to access the necessary resources. The Amazon DCV API uses OAuth 2.0 for authentication,
so you'll need to register your application and retrieve the necessary credentials. Once you have your access token,
you can start sending requests to the Amazon DCV API endpoints to begin processing data.

###### Topics

- [Step 1: Generate your API client](client-sdk.md "client-sdk.md")
- [Step 2: Register your client API](credentials.md "credentials.md")
- [Step 3: Get an access token and make an API request](request.md "request.md")
