# DeleteGroup

The `DELETE` request is also available for the `/Groups`
endpoint to delete existing groups using the value of the `id`.

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
| `ResourceNotFoundException` | Specified group does not exist.                                                                                                         | 404              |
| `ThrottlingException`       | Too many requests exceeded the limits.                                                                                                  | 429              |
| `InternalServerException`   | Service failed to process the request.                                                                                                  | 500              |

## Examples

Following are example requests and responses for this API operation.

###### Example Request

```
DELETE https://scim.us-east-1.amazonaws.com/{tenant_id}/scim/v2/Groups/9067729b3d-f987ac4d-a175-44f0-a528-6d23c5d2ec4d
User-Agent: Mozilla/5.0
Authorization: Bearer <bearer_token>
```

###### Example Response

```
HTTP/1.1 204
Date: Mon, 06 Apr 2020 22:21:24 GMT
Content-Type: application/json
x-amzn-RequestId: abbf9e53-9ecc-46d2-8efe-104a66ff128
```
