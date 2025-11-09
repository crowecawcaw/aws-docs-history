# Authorize

|                                                                                    |
| ---------------------------------------------------------------------------------- |
| The AWS AppFabric for productivity feature is in preview and is subject to change. |

Authorizes an AppClient.

###### Topics

- [Request body](#API_Authorize_request "#API_Authorize_request")

## Request body

The request accepts the following data in JSON format.

| Parameter         | Description                                                               |
| ----------------- | ------------------------------------------------------------------------- |
| **app_client_id** | The ID of the AppClient to authorize.                                     |
| **redirect_uri**  | The URI to redirect end users to after<br>authorization.                  |
| **state**         | A unique value to maintain the state between the request<br>and callback. |
