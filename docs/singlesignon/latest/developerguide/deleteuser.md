# DeleteUser

A user can be deleted by making a `DELETE` request to the
`/Users` endpoint with an existing user ID.

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

| Error                       | Condition                                                                                                                               | HTTP Status Code |
| --------------------------- | --------------------------------------------------------------------------------------------------------------------------------------- | ---------------- |
| `ValidationException`       | Request cannot be parsed, is syntactically incorrect, or violates<br>schema. This error also occurs if the operation is<br>unsupported. | 400              |
| `UnauthorizedException`     | Authorization header is invalid or missing. This error also<br>occurs if the tenant ID is incorrect.                                    | 401              |
| `AccessDeniedException`     | Operation is not permitted based on the supplied<br>authorization.                                                                      | 403              |
| `ResourceNotFoundException` | Specified user does not exist.                                                                                                          | 404              |
| `ThrottlingException`       | Too many requests exceeded the limits.                                                                                                  | 429              |
| `InternalServerException`   | Service failed to process the request.                                                                                                  | 500              |

## Examples

Following are example requests and responses for this API operation.

###### Example Request

```
DELETE https://scim.us-east-1.amazonaws.com/{tenant_id}/scim/v2/Users/9067729b3d-ee533c18-538a-4cd3-a572-63fb863ed734
User-Agent: Mozilla/5.0
Authorization: Bearer <bearer_token>
```

###### Example Response

```
HTTP/1.1 204
Date: Tue, 31 Mar 2020 02:36:15 GMT
Content-Type: application/json
x-amzn-RequestId: abbf9e53-9ecc-46d2-8efe-104a66ff128f
```
