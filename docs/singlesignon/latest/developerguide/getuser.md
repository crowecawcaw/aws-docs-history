# GetUser

Existing users can be retrieved by making a `GET` request to the IAM Identity Center SCIM
implementation `/Users` endpoint with a user ID.

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

| Error                       | Condition                                                                                                                         | HTTP Status Code |
| --------------------------- | --------------------------------------------------------------------------------------------------------------------------------- | ---------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `ValidationException`       | Request cannot be parsed, is syntactically incorrect, or violates schema. This error also occurs if the operation is unsupported. | 400              |
| `UnauthorizedException`     | Authorization header is invalid or missing. This error also occurs if the tenant ID is incorrect.                                 | 401              |
| `AccessDeniedException`     | The operation is not permitted based on the supplied authorization.                                                               | 403              |
| `ResourceNotFoundException` | Specified user or endpoint does not exist.                                                                                        | 404              |
| `ThrottlingException`       | Too many requests exceeded the limits.                                                                                            | 429              |
| `InternalServerException`   | Service failed to process the request.                                                                                            | 500              | ## Examples Following are example requests and responses for this API operation. ###### Example Request `GET https://scim.us-east-1.amazonaws.com/{tenant_id}/scim/v2/Users/9067729b3d-ee533c18-538a-4cd3-a572-63fb863ed734 User-Agent: Mozilla/5.0 Authorization: Bearer <bearer_token>` ###### Example Response `HTTP/1.1 200 Date: Tue, 31 Mar 2020 02:36:15 GMT Content-Type: application/json x-amzn-RequestId: abbf9e53-9ecc-46d2-8efe-104a66ff128f { "id": "9067729b3d-ee533c18-538a-4cd3-a572-63fb863ed734", "externalId": "1", "meta": { "resourceType": "User", "created": "2020-03-30T16:55:15Z", "lastModified": "2020-03-30T16:55:15Z" }, "schemas": [ "urn:ietf:params:scim:schemas:core:2.0:User" ], "userName": "johndoe", "name": { "familyName": "Doe", "givenName": "John" }, "displayName": "John Doe", "active": false, "emails": [ { "value": "johndoe@example.com", "type": "work", "primary": true } ] }` |
