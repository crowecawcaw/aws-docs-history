# ListResourceTypes

Information about supported resource types can be retrieved by making a request to the `/ResourceTypes` endpoint.

## Not supported

The IAM Identity Center SCIM implementation does not support the following aspects of this API
operation.

- None

## Constraints

The IAM Identity Center SCIM implementation has the following constraints for this API
operation.

- None.

## Errors

The following IAM Identity Center SCIM implementation errors are common for this API
operation.

| Error                     | Condition                                                                                                                         | HTTP Status Code |
| ------------------------- | --------------------------------------------------------------------------------------------------------------------------------- | ---------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| `ValidationException`     | Request cannot be parsed, is syntactically incorrect, or violates schema. This error also occurs if the operation is unsupported. | 400              |
| `UnauthorizedException`   | Authorization header is invalid or missing. This error also occurs if the tenant ID is incorrect.                                 | 401              |
| `AccessDeniedException`   | Operation is not permitted based on the supplied authorization.                                                                   | 403              |
| `ThrottlingException`     | Too many requests exceeded the limits.                                                                                            | 429              |
| `InternalServerException` | Service failed to process the request.                                                                                            | 500              | ## Examples Following are example requests and responses for this API operation. ###### Example Request `GET /{tenant_id}/scim/v2/ResourceTypes HTTP/2 User-Agent: Mozilla/5.0 Authorization: Bearer <bearer_token>` ###### Example Response `HTTP/2 200 OK Date: Fri, 12 May 2023 16:59:31 GMT Content-Type: application/json Content-Length: 2 X-Amzn-Requestid: 5b6de8b5-36a3-4179-8afa-71e918d85516 { "schemas": [ "urn:ietf:params:scim:api:messages:2.0:ListResponse" ], "totalResults": 2, "itemsPerPage": 2, "startIndex": 1, "Resources": [ { "schemas": ["urn:ietf:params:scim:schemas:core:2.0:ResourceType"], "id": "User", "name": "User", "endpoint": "/Users", "description": "User Account", "schema": "urn:ietf:params:scim:schemas:core:2.0:User", "schemaExtensions": [ { "schema": "urn:ietf:params:scim:schemas:extension:enterprise:2.0:User", "required": true } ], "meta": { "resourceType": "ResourceType" "\"location\":\"https://scim.us-east-1.amazonaws.com/{tenant_id}/scim/v2/ResourceTypes/User\"" } }, { "schemas": ["urn:ietf:params:scim:schemas:core:2.0:ResourceType"], "id": "Group", "name": "Group", "endpoint": "/Groups", "description": "Group", "schema": "urn:ietf:params:scim:schemas:core:2.0:Group", "meta": { "resourceType": "ResourceType" "\"location\":\"https://scim.us-east-1.amazonaws.com/{tenant_id}/scim/v2/ResourceTypes/Group\"" } } ] }` |
