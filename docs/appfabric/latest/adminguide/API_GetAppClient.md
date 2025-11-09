# GetAppClient

|                                                                                    |
| ---------------------------------------------------------------------------------- |
| The AWS AppFabric for productivity feature is in preview and is subject to change. |

Returns information about an AppClient.

###### Topics

- [Request body](#API_GetAppClient_request "#API_GetAppClient_request")
- [Response elements](#API_GetAppClient_response "#API_GetAppClient_response")

## Request body

The request accepts the following data in JSON format.

| Parameter               | Description                                                                                                                                                                                                        |
| ----------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------- |
| **appClientIdentifier** | The Amazon Resource Name (ARN) or Universal Unique<br>Identifier (UUID) of the AppClient to use for the<br>request.<br>Length Constraints: Minimum length of 1. Maximum length of<br>1011.<br>Pattern:<br>`arn:.+$ | ^[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`<br>Required: Yes |

## Response elements

If the action is successful, the service sends back an HTTP 200
response.

The following data is returned in JSON format by the service.

| Parameter     | Description                                                                                                  |
| ------------- | ------------------------------------------------------------------------------------------------------------ |
| **appClient** | Contains information about an AppClient.<br>Type: [AppClient](API_AppClient.md "API_AppClient.md")<br>object |
