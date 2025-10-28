# ServiceProviderConfig

You can use the `/ServiceProviderConfig` endpoint for `GET`
requests to view additional information about the IAM Identity Center SCIM implementation. The
`/ServiceProviderConfig` endpoint is read only.

## Not supported

The IAM Identity Center SCIM implementation does not support the following aspects of this API
operation.

- None

## Constraints

The IAM Identity Center SCIM implementation has the following constraints for this API
operation.

- None

## Errors

The following IAM Identity Center SCIM implementation errors are common for this API
operation.

| Error                     | Condition                                                                                         | HTTP Status Code |
| ------------------------- | ------------------------------------------------------------------------------------------------- | ---------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `UnauthorizedException`   | Authorization header is invalid or missing. This error also occurs if the tenant ID is incorrect. | 401              |
| `AccessDeniedException`   | Operation is not permitted based on the supplied authorization.                                   | 403              |
| `ThrottlingException`     | Too many requests were made that exceed the limits.                                               | 429              |
| `InternalServerException` | Service failed to process the request.                                                            | 500              | ## Examples Following are example requests and responses for this API operation. ###### Example Request `GET https://scim.us-east-1.amazonaws.com/{tenant_id}/scim/v2/ServiceProviderConfig User-Agent: Mozilla/5.0 Authorization: Bearer <bearer_token>` ###### Example Response `HTTP/1.1 200 Date: Thu, 13 Aug 2020 21:11:26 GMT Content-Type: application/json x-amzn-RequestId: d0f671f1-3217-4b0f-b310-82a0b6861967 { "schemas": [ "urn:ietf:params:scim:schemas:core:2.0:ServiceProviderConfig" ], "documentationUri": "https://docs.aws.amazon.com/singlesignon/latest/userguide/manage-your-identity-source-idp.html", "authenticationSchemes": [ { "type": "oauthbearertoken", "name": "OAuth Bearer Token", "description": "Authentication scheme using the OAuth Bearer Token Standard", "specUri": "https://www.rfc-editor.org/info/rfc6750", "documentationUri": "https://docs.aws.amazon.com/singlesignon/latest/userguide/provision-automatically.html", "primary": true } ], "patch": { "supported": true }, "bulk": { "supported": false, "maxOperations": 1, "maxPayloadSize": 1048576 }, "filter": { "supported": true, "maxResults": 50 }, "changePassword": { "supported": false }, "sort": { "supported": false }, "etag": { "supported": false } }` |
