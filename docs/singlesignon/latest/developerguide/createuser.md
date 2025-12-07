# CreateUser

You can create new users from a POST request using the IAM Identity Center SCIM implementation
`/Users` endpoint. See the Examples section.

## Not supported

The IAM Identity Center SCIM implementation does not support the following aspects of this API
operation.

- `ims`, `photos`, `x509Certificates`,
  `entitlements`, and `password` attributes
- `displayName` subattribute for manager
- `display` subattribute for `emails`,
  `addresses`, and `phoneNumbers`

## Constraints

The IAM Identity Center SCIM implementation has the following constraints for this API
operation.

- The `givenName`, `familyName`,
  `userName`, and `displayName` fields are
  required.
- The `addresses` field can contain letters, accented characters,
  symbols, numbers, punctuation, space (normal and nonbreaking).
- We do not support multiple values in multi-value attributes (such as
  `emails`, `addresses`, `phoneNumbers`, `roles`).
  Only single values are permitted.
- The `emails` attribute value must be marked as primary.
- The `groups` field cannot be specified with the
  `createUser` request.
- The `userName` field can contain letters, accented characters,
  symbols, numbers, punctuation.
- The `roles` attribute value cannot contain display field,
  only `value`, `type`, and `primary` are supported.

## Errors

The following IAM Identity Center SCIM implementation errors are common for this API
operation.

| Error                     | Condition                                                                                                                               | HTTP Status Code |
| ------------------------- | --------------------------------------------------------------------------------------------------------------------------------------- | ---------------- |
| `ValidationException`     | Request cannot be parsed, is syntactically incorrect, or violates<br>schema. This error also occurs if the operation is<br>unsupported. | 400              |
| `UnauthorizedException`   | Authorization header is invalid or missing. This error also<br>occurs if the tenant ID is incorrect.                                    | 401              |
| `AccessDeniedException`   | Operation is not permitted based on the supplied<br>authorization.                                                                      | 403              |
| `ConflictException`       | User already exists.                                                                                                                    | 409              |
| `ThrottlingException`     | Too many requests exceeded the limits.                                                                                                  | 429              |
| `InternalServerException` | Service failed to process the request.                                                                                                  | 500              |

## Examples

Following are example requests and responses for this API operation.

###### Example Request

```
POST https://scim.us-east-1.amazonaws.com/{tenant_id}/scim/v2/Users
User-Agent: Mozilla/5.0
Authorization: Bearer <bearer_token>

{
  "externalId": "701984",
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
  "nickName": "Babs",
  "profileUrl": "https://login.example.com/bjensen",
  "emails": [
    {
      "value": "bjensen@example.com",
      "type": "work",
      "primary": true
    }
  ],
  "addresses": [
    {
      "type": "work",
      "streetAddress": "100 Universal City Plaza",
      "locality": "Hollywood",
      "region": "CA",
      "postalCode": "91608",
      "country": "USA",
      "formatted": "100 Universal City Plaza Hollywood, CA 91608 USA",
      "primary": true
    }
  ],
  "phoneNumbers": [
    {
      "value": "555-555-5555",
      "type": "work"
    }
  ],
  "roles": [
    {
        "value": "Researcher",
        "type": "work",
        "primary": true
    }
  ],
  "userType": "Employee",
  "title": "Tour Guide",
  "preferredLanguage": "en-US",
  "locale": "en-US",
  "timezone": "America/Los_Angeles",
  "active": true,
  "urn:ietf:params:scim:schemas:extension:enterprise:2.0:User": {
    "employeeNumber": "701984",
    "costCenter": "4130",
    "organization": "Universal Studios",
    "division": "Theme Park",
    "department": "Tour Operations",
    "manager": {
      "value": "9067729b3d-ee533c18-538a-4cd3-a572-63fb863ed734",
      "$ref": "../Users/9067729b3d-ee533c18-538a-4cd3-a572-63fb863ed734"
    }
  }
}
```

###### Example Response

```
HTTP/1.1 201
Date: Tue, 31 Mar 2020 02:36:15 GMT
Content-Type: application/json
x-amzn-RequestId: abbf9e53-9ecc-46d2-8efe-104a66ff128f
{
    "id": "9067729b3d-94f1e0b3-c394-48d5-8ab1-2c122a167074",
    "externalId": "701984",
    "meta": {
        "resourceType": "User",
        "created": "2020-03-31T02:36:15Z",
        "lastModified": "2020-03-31T02:36:15Z"
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
    "nickName": "Babs",
    "title": "Tour Guide",
    "userType": "Employee",
    "preferredLanguage": "en-US",
    "locale": "en-US",
    "timezone": "America/Los_Angeles",
    "active": true,
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
    "roles": [
        {
            "value": "Researcher",
            "type": "work",
            "primary": true
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
