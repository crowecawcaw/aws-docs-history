# CreateGroup

Groups can be created through a `POST` request to the `/Groups`
endpoint with the body containing the information of the group.

## Not supported

The IAM Identity Center SCIM implementation does not support the following aspects of this API
operation.

- None

## Constraints

The IAM Identity Center SCIM implementation has the following constraints for this API
operation.

- `displayName` is required.
- A maximum of 100 members can be added in a single request.

## Errors

The following IAM Identity Center SCIM implementation errors are common for this API
operation.

| Error                     | Condition                                                                                                                              | HTTP Status Code |
| ------------------------- | -------------------------------------------------------------------------------------------------------------------------------------- | ---------------- |
| `ValidationException`     | Request can't be parsed, is syntactically incorrect, or violates<br>schema. This error also occurs if the operation is<br>unsupported. | 400              |
| `UnauthorizedException`   | Authorization header is invalid or missing. This error also<br>occurs if the tenant ID is incorrect.                                   | 401              |
| `AccessDeniedException`   | Operation isn't permitted based on the supplied<br>authorization.                                                                      | 403              |
| `ConflictException`       | Group already exists.                                                                                                                  | 409              |
| `ThrottlingException`     | Too many requests exceeded the limits.                                                                                                 | 429              |
| `InternalServerException` | Service failed to process the request.                                                                                                 | 500              |

## Examples

Following are example requests and responses for this API operation.

###### Example Request

```
POST https://scim.us-east-1.amazonaws.com/{tenant_id}/scim/v2/Groups
User-Agent: Mozilla/5.0
Authorization: Bearer <bearer_token>

{
    "externalId": "701984",
    "displayName": "Group Bar",
    "members": [
        {
            "value": "9067729b3d-94f1e0b3-c394-48d5-8ab1-2c122a167074",
            "$ref": "../Users/9067729b3d-94f1e0b3-c394-48d5-8ab1-2c122a167074",
            "type": "User"
        }
    ]
}
```

###### Example Response

```
HTTP/1.1 201
Date: Mon, 06 Apr 2020 16:48:19 GMT
Content-Type: application/json
x-amzn-RequestId: abbf9e53-9ecc-46d2-8efe-104a66ff128f

{
    "id": "9067729b3d-a2cfc8a5-f4ab-4443-9d7d-b32a9013c554",
    "externalId": "701984",
    "meta": {
        "resourceType": "Group",
        "created": "2020-04-06T16:48:19Z",
        "lastModified": "2020-04-06T16:48:19Z"
    },
    "schemas": [
        "urn:ietf:params:scim:schemas:core:2.0:Group"
    ],
    "displayName": "Group Bar"
}
```
