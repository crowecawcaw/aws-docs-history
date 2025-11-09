# DeleteAppClient

|                                                                                    |
| ---------------------------------------------------------------------------------- |
| The AWS AppFabric for productivity feature is in preview and is subject to change. |

Deletes an application client.

###### Topics

- [Request body](#API_DeleteAppClient_request "#API_DeleteAppClient_request")
- [Response elements](#API_DeleteAppClient_response "#API_DeleteAppClient_response")

## Request body

The request accepts the following data in JSON format.

| Parameter               | Description                                                                                                                                                                                                        |
| ----------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ | ------------------------------------------------------------------------------- |
| **appClientIdentifier** | The Amazon Resource Name (ARN) or Universal Unique<br>Identifier (UUID) of the AppClient to use for the<br>request.<br>Length Constraints: Minimum length of 1. Maximum length of<br>1011.<br>Pattern:<br>`arn:.+$ | ^[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`<br>Required: Yes |

## Response elements

If the action is successful, the service sends back an HTTP 204 response with
an empty HTTP body.
