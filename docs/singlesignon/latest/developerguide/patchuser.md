# PatchUser

The `/Users` endpoint allows a `PATCH` request to be made for
partial changes to an existing user. In the body of the request, the target attribute
and its new value must be specified as shown in the Examples
section.

## Not supported

The IAM Identity Center SCIM implementation does not support the following aspects of this API
operation.

- Multiple `PATCH` operations on `userName` or
  `active` attribute
- `ims`, `photos`, `x509Certificates`,
  `entitlements`, and `password` field
- `displayName` subattribute for manager
- `display` subattribute for `emails`,
  `addresses`, and `phoneNumbers`

## Constraints

The IAM Identity Center SCIM implementation has the following constraints for this API
operation.

- The supported operations are `add`, `replace`, and
  `remove`.
- The operation must be specified.
- The path is required for a `remove` operation.
- A value is required for `add` and `replace`.
- Modification is only allowed for the `userName`,
  `active`, `externalId`, `displayName`,
  `nickName`, `profileUrl`, `title`,
  `userType`, `preferredLanguage`,
  `locale`, `timezone`, `name`,
  `enterprise`, `emails`, `addresses`,
  and `phoneNumbers` attributes.
- Only the `eq` operator is supported in filters.
- The `remove` patch operation is not supported for
  `userName` or active attributes.
- We do not support having multi-valued attributes (such as
  `emails`, `addresses`, `phoneNumbers`.
  Only one value is permitted for each of those attributes.

## Errors

The following IAM Identity Center SCIM implementation errors are common for this API
operation.

| Error                       | Condition                                                                                                                               | HTTP Status Code |
| --------------------------- | --------------------------------------------------------------------------------------------------------------------------------------- | ---------------- |
| `ValidationException`       | Request cannot be parsed, is syntactically incorrect, or violates<br>schema. This error also occurs if the operation is<br>unsupported. | 400              |
| `UnauthorizedException`     | Authorization header is invalid or missing. This error also<br>occurs if the tenant ID is incorrect.                                    | 401              |
| `AccessDeniedException`     | Operation is not permitted based on the supplied<br>authorization.                                                                      | 403              |
| `ResourceNotFoundException` | Specified user does not exist.                                                                                                          | 404              |
| `ConflictException`         | User already exists.                                                                                                                    | 409              |
| `ThrottlingException`       | Too many requests exceeded the limits.                                                                                                  | 429              |
| `InternalServerException`   | Service failed to process the request.                                                                                                  | 500              |

## Examples

Following are example requests and responses for this API operation.

###### Example Request

```
PATCH https://scim.us-east-1.amazonaws.com/{tenant_id}/scim/v2/Users/9067729b3d-94f1e0b3-c394-48d5-8ab1-2c122a167074
User-Agent: Mozilla/5.0
Authorization: Bearer <bearer_token>

{
    "schemas": [
        "urn:ietf:params:scim:api:messages:2.0:PatchOp"
    ],
    "Operations": [
        {
            "op": "replace",
            "path": "active",
            "value": "false"
        }
    ]
}
```

###### Example Response

```
HTTP/1.1 200
Date: Tue, 31 Mar 2020 02:36:15 GMT
Content-Type: application/json
x-amzn-RequestId: abbf9e53-9ecc-46d2-8efe-104a66ff128f
{
    "id": "9067729b3d-94f1e0b3-c394-48d5-8ab1-2c122a167074",
    "externalId": "701984",
    "meta": {
        "resourceType": "User",
        "created": "2020-03-31T02:36:15Z",
        "lastModified": "2020-04-03T06:02:47Z"
    },
    "schemas": [
        "urn:ietf:params:scim:schemas:core:2.0:User",
        "urn:ietf:params:scim:schemas:extension:enterprise:2.0:User"
    ],
    "userName": "bjensen",
    "name": {
        "formatted": "Ms. Barbara J Jensen, III",
        "familyName": "Jensen",
        "givenName": "Barbara",
        "middleName": "Jane",
        "honorificPrefix": "Ms.",
        "honorificSuffix": "III"
    },
    "displayName": "Babs Jensen",
    "nickName": "Bas",
    "title": "Tour Guide",
    "userType": "Employee",
    "preferredLanguage": "en-US",
    "locale": "en-US",
    "timezone": "America/Los_Angeles",
    "active": false,
    "emails": [
        {
            "value": "bjensen@example.com",
            "type": "work",
            "primary": true
        }
    ],
    "addresses": [
        {
            "formatted": "100 Universal City Plaza Hollywood, CA 91608 USA",
            "streetAddress": "100 Universal City Plaza",
            "locality": "Hollywood",
            "region": "CA",
            "postalCode": "91608",
            "country": "USA",
            "type": "work",
            "primary": true
        }
    ],
    "phoneNumbers": [
        {
            "value": "555-555-5555",
            "type": "work"
        }
    ],
    "urn:ietf:params:scim:schemas:extension:enterprise:2.0:User": {
        "employeeNumber": "701984",
        "costCenter": "4130",
        "organization": "Universal Studios",
        "division": "Theme Park",
        "department": "Tour Operations",
        "manager": {
            "value": "9067729b3d-ee533c18-538a-4cd3-a572-63fb863ed734"
        }
    }
}
```
