

# GetAppClient
<a name="API_GetAppClient"></a>


|  | 
| --- |
| The AWS AppFabric for productivity feature is in preview and is subject to change. | 

Returns information about an AppClient.

**Topics**
+ [Request body](#API_GetAppClient_request)
+ [Response elements](#API_GetAppClient_response)

## Request body
<a name="API_GetAppClient_request"></a>

The request accepts the following data in JSON format.


| Parameter | Description | 
| --- | --- | 
| **appClientIdentifier** | The Amazon Resource Name (ARN) or Universal Unique Identifier (UUID) of the AppClient to use for the request.<br />Length Constraints: Minimum length of 1. Maximum length of 1011.<br />Pattern: `arn:.+$\|^[a-f0-9]{8}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{4}-[a-f0-9]{12}`<br />Required: Yes | 

## Response elements
<a name="API_GetAppClient_response"></a>

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.


| Parameter | Description | 
| --- | --- | 
| **appClient** | Contains information about an AppClient.<br />Type: [AppClient](API_AppClient.md) object | 