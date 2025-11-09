# UpdateAppClient

|                                                                                    |
| ---------------------------------------------------------------------------------- |
| The AWS AppFabric for productivity feature is in preview and is subject to change. |

Updates an AppClient.

###### Topics

- [Request body](#API_UpdateAppClient_request "#API_UpdateAppClient_request")
- [Response elements](#API_UpdateAppClient_response "#API_UpdateAppClient_response")

## Request body

The request accepts the following data in JSON format.

| Parameter               | Description                                                                                                                                                                                                                                                                                                                           |
| ----------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------- |
| **appClientIdentifier** | The Amazon Resource Name (ARN) or Universal Unique<br>Identifier (UUID) of the AppClient to use for the<br>request.<br>Length Constraints: Minimum length of 1. Maximum length of<br>1011.<br>Pattern:<br>`arn:.+$                                                                                                                    | ^[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`<br>Required: Yes |
| **redirectUrls**        | The URI to redirect end users to after authorization. You<br>can add up to 5 redirectUrls. For example,<br>`https://localhost:8080`.<br>Type: Array of strings<br>Array Members: Minimum number of 1 item. Maximum number of<br>5 items.<br>Length Constraints: Minimum length of 1. Maximum length of<br>2048.<br>Pattern:<br>`(http | https):\/\/[-a-zA-Z0-9_:.\/]+`                                                  |

## Response elements

If the action is successful, the service sends back an HTTP 200
response.

The following data is returned in JSON format by the service.

| Parameter     | Description                                                                                                  |
| ------------- | ------------------------------------------------------------------------------------------------------------ |
| **appClient** | Contains information about an AppClient.<br>Type: [AppClient](API_AppClient.md "API_AppClient.md")<br>object |
