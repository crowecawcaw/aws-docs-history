

# Troubleshoot AgentCore Web Search

## Errors
<a name="web-search-api-errors"></a>

The following table lists the errors that the `InvokeWebSearch` API returns and what you can do about each one. Error responses include a `message` field. A `ValidationException` also includes a `reason` field.


| Error | HTTP status | Cause | What to do | 
| --- | --- | --- | --- | 
|  `ValidationException`  | 400 | The request doesn’t meet the rules in [Request fields](web-search-api-reference.md#web-search-api-request). For example, `searchQuery` is empty or longer than 200 characters, `maxResults` is outside 1–25, a domain list is empty or holds more than 100 names, a publication time isn’t a valid timestamp, `publishedAfter` is later than `publishedBefore`, the body contains an unknown field, or the body is larger than 32 KiB. | Correct the request, and then send it again. | 
|  `AccessDeniedException`  | 403 | The caller doesn’t have the `bedrock-agentcore:InvokeWebSearch` permission on the web search tool Amazon Resource Name (ARN), or a policy denies the request. For requests through an interface virtual private cloud (VPC) endpoint, the endpoint policy can also deny the request. | Grant the `bedrock-agentcore:InvokeWebSearch` permission. For instructions on granting the permission, see [Grant permission to call the API](web-search-api-get-started.md#web-search-api-permissions). Check any policies that deny the action, including the VPC endpoint policy. | 
|  `MissingAuthenticationTokenException`, `UnrecognizedClientException`, or `InvalidSignatureException`  | 403 | The request isn’t signed, the credentials aren’t valid or have expired, or the request is signed for a different Region or service. | Call the API with an AWS SDK or the AWS Command Line Interface (AWS CLI) and current credentials. If you sign requests yourself, sign them with AWS Signature Version 4 (SigV4) for the service name `bedrock-agentcore` and the Region of the endpoint that you call. | 
|  `ResourceNotFoundException`  | 404 | The `webSearchId` in the request isn’t the identifier of a web search tool. For example, the value has a typo or names a version that doesn’t exist. | Set `webSearchId` to `web-search.v1`, the identifier of the AWS managed web search tool, and then send the request again. | 
|  `ThrottlingException`  | 429 | Your account sent requests faster than its quota for the API allows, or the service is temporarily limiting requests. | Retry the request with exponential backoff. If you need a higher rate, request a quota increase. For more information about the quota, see [Quotas](web-search-api.md#web-search-api-quotas). | 
|  `InternalServerException`  | 500 | The service had an internal error. | Retry the request with exponential backoff. | 
|  `ServiceUnavailableException`  | 503 | The service can’t handle the request right now. | Retry the request. If the response includes `retryAfterSeconds`, wait that many seconds before you retry. | 