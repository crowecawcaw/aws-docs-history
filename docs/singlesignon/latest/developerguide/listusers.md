# ListUsers

This endpoint provides the ability to perform filter queries on an existing list of
users through a `GET` request to `/Users` by inserting additional
filters. Only a maximum of 50 results can be returned. See the **Constraints** section for more
information.

## Not supported

The IAM Identity Center SCIM implementation does not support the following aspects of this API
operation.

- `startIndex`, `attributes`, and
  `excludedAttributes` (despite being listed in the SCIM
  protocol)

## Constraints

The IAM Identity Center SCIM implementation has the following constraints for this API
operation.

- At this time, the `ListUsers` API is only capable of returning up to 50 results.
- Supported filter combinations: (`userName`),
  (`externalId`), (`id` and `manager`),
  (`manager` and `id`). Note that the use of
  `id` as an individual filter, though valid, should be avoided
  as a `getUser` endpoint is already available.
- Supported comparison operator in filters: `eq`
- Filter must be specified as follows: `<filterAttribute> eq
"<filterValue>"`

## Errors

The following IAM Identity Center SCIM implementation errors are common for this API
operation.

| Error                     | Condition                                                                                                                               | HTTP Status Code |
| ------------------------- | --------------------------------------------------------------------------------------------------------------------------------------- | ---------------- |
| `ValidationException`     | Request cannot be parsed, is syntactically incorrect, or violates<br>schema. This error also occurs if the operation is<br>unsupported. | 400              |
| `UnauthorizedException`   | Authorization header is invalid or missing. This error also<br>occurs if the tenant ID is incorrect.                                    | 401              |
| `AccessDeniedException`   | Operation is not permitted based on the supplied<br>authorization.                                                                      | 403              |
| `ThrottlingException`     | Too many requests exceeded the limits.                                                                                                  | 429              |
| `InternalServerException` | Service failed to process the request.                                                                                                  | 500              |

## Examples

Following are example requests and responses for this API operation.

###### Example Request

```
GET https://scim.us-east-1.amazonaws.com/{tenant_id}/scim/v2/Users
User-Agent: Mozilla/5.0
Authorization: Bearer <bearer_token>
```

###### Example Response

```
HTTP/1.1 200
Date: Thu, 23 Jul 2020 00:15:28 GMT
Content-Type: application/json
x-amzn-RequestId: 88204ccc-30cd-4010-b3ac-b4a12cc31e8b

{
    "totalResults": 5,
    "itemsPerPage": 5,
    "startIndex": 1,
    "schemas": [
        "urn:ietf:params:scim:api:messages:2.0:ListResponse"
    ],
    "Resources": [
        {
            "id": "90677c608a-7afcdc23-0bd4-4fb7-b2ff-10ccffdff447",
            "externalId": "702135",
            "meta": {
                "resourceType": "User",
                "created": "2020-07-22T22:32:58Z",
                "lastModified": "2020-07-22T22:32:58Z"
            },
            "schemas": [
                "urn:ietf:params:scim:schemas:core:2.0:User",
                "urn:ietf:params:scim:schemas:extension:enterprise:2.0:User"
            ],
            "userName": "mjack",
            "name": {
                "familyName": "Mark",
                "givenName": "Jackson",
                "honorificPrefix": "Mr.",
                "honorificSuffix": "I"
            },
            "displayName": "mjack",
            "nickName": "Mark",
            "active": false,
            "emails": [
                {
                    "value": "mjack@example.com",
                    "type": "work",
                    "primary": true
                }
            ],
            "urn:ietf:params:scim:schemas:extension:enterprise:2.0:User": {
                "manager": {
                    "value": "9067729b3d-ee533c18-538a-4cd3-a572-63fb863ed734"
                }
            }
        },
        {
            "id": "90677c608a-787142a0-3f27-4cd3-afb6-8aed7ce87094",
            "externalId": "705167",
            "meta": {
                "resourceType": "User",
                "created": "2020-07-22T22:34:55Z",
                "lastModified": "2020-07-22T22:34:55Z"
            },
            "schemas": [
                "urn:ietf:params:scim:schemas:core:2.0:User",
                "urn:ietf:params:scim:schemas:extension:enterprise:2.0:User"
            ],
            "userName": "druss",
            "name": {
                "familyName": "Daniel",
                "givenName": "Russell",
                "honorificPrefix": "Mr.",
                "honorificSuffix": "I"
            },
            "displayName": "danrussell",
            "nickName": "Dan",
            "active": false,
            "emails": [
                {
                    "value": "druss@example.com",
                    "type": "work",
                    "primary": true
                }
            ],
            "urn:ietf:params:scim:schemas:extension:enterprise:2.0:User": {
                "manager": {
                    "value": "9067729b3d-ee533c18-538a-4cd3-a572-63fb863ed734"
                }
            }
        },
        {
            "id": "90677c608a-229f7eb1-c07d-4c21-a5fd-769bf2e8c5c9",
            "externalId": "2",
            "meta": {
                "resourceType": "User",
                "created": "2020-07-22T23:51:45Z",
                "lastModified": "2020-07-22T23:51:45Z"
            },
            "schemas": [
                "urn:ietf:params:scim:schemas:core:2.0:User"
            ],
            "userName": "tzhang",
            "name": {
                "familyName": "Terry",
                "givenName": "Zhang"
            },
            "displayName": "Terry Zhang",
            "active": false,
            "emails": [
                {
                    "value": "tzhang@example.com",
                    "type": "work",
                    "primary": true
                }
            ]
        },
        {
            "id": "90677c608a-685d5bf3-efab-48c8-b3b1-648fc5c5d980",
            "externalId": "701985",
            "meta": {
                "resourceType": "User",
                "created": "2020-07-22T22:17:47Z",
                "lastModified": "2020-07-22T22:17:47Z"
            },
            "schemas": [
                "urn:ietf:params:scim:schemas:core:2.0:User",
                "urn:ietf:params:scim:schemas:extension:enterprise:2.0:User"
            ],
            "userName": "jdoe",
            "name": {
                "familyName": "John",
                "givenName": "Doe",
                "honorificPrefix": "Mr.",
                "honorificSuffix": "III"
            },
            "displayName": "jdoe",
            "nickName": "Johnny",
            "active": false,
            "emails": [
                {
                    "value": "johndoe@example.com",
                    "type": "work",
                    "primary": true
                }
            ],
            "urn:ietf:params:scim:schemas:extension:enterprise:2.0:User": {
                "manager": {
                    "value": "9067729b3d-ee533c18-538a-4cd3-a572-63fb863ed734"
                }
            }
        },
        {
            "id": "90677c608a-9683e752-a6fd-4935-b6b8-3fe26a202f21",
            "externalId": "702138",
            "meta": {
                "resourceType": "User",
                "created": "2020-07-22T22:38:11Z",
                "lastModified": "2020-07-22T22:38:11Z"
            },
            "schemas": [
                "urn:ietf:params:scim:schemas:core:2.0:User",
                "urn:ietf:params:scim:schemas:extension:enterprise:2.0:User"
            ],
            "userName": "hmack",
            "name": {
                "familyName": "Henry",
                "givenName": "Mackenzie",
                "honorificPrefix": "Mr.",
                "honorificSuffix": "I"
            },
            "displayName": "hmack",
            "nickName": "Henry",
            "active": false,
            "emails": [
                {
                    "value": "hmack@example.com",
                    "type": "work",
                    "primary": true
                }
            ],
            "urn:ietf:params:scim:schemas:extension:enterprise:2.0:User": {
                "manager": {
                    "value": "9067729b3d-ee533c18-538a-4cd3-a572-63fb863jd956"
                }
            }
        }
    ]
}
```

## Filter examples

The following four different filter combinations are supported.

- `externalId`
- `userName`
- `id` and `manager`
- `manager` and `id`

The filters can be applied in the formats as shown.

**Single filter**

```
filter=<filterAttribute> eq "<filterValue>"
```

**Two filters**

```
filter=<filterAttribute1> eq "<filterValue1>" and <filterAttribute2> eq "<filterValue2>"
```

### externalId

###### Example Request

```
GET https://scim.us-east-1.amazonaws.com/{tenant_id}/scim/v2/Users?filter=externalId eq "705167"
User-Agent: Mozilla/5.0
Authorization: Bearer <bearer_token>
```

###### Example Response

```
HTTP/1.1 200
Date: Wed, 22 Jul 2020 22:57:01 GMT
Content-Type: application/json
x-amzn-RequestId: c482800a-f6ba-4979-91d0-72d3a7b496cb

{
    "totalResults": 1,
    "itemsPerPage": 1,
    "startIndex": 1,
    "schemas": [
        "urn:ietf:params:scim:api:messages:2.0:ListResponse"
    ],
    "Resources": [
        {
            "id": "90677c608a-787142a0-3f27-4cd3-afb6-8aed7ce87094",
            "externalId": "705167",
            "meta": {
                "resourceType": "User",
                "created": "2020-07-22T22:34:55Z",
                "lastModified": "2020-07-22T22:34:55Z"
            },
            "schemas": [
                "urn:ietf:params:scim:schemas:core:2.0:User",
                "urn:ietf:params:scim:schemas:extension:enterprise:2.0:User"
            ],
            "userName": "druss",
            "name": {
                "familyName": "Daniel",
                "givenName": "Russell",
                "honorificPrefix": "Mr.",
                "honorificSuffix": "I"
            },
            "displayName": "danrussell",
            "nickName": "Dan",
            "active": false,
            "emails": [
                {
                    "value": "druss@example.com",
                    "type": "work",
                    "primary": true
                }
            ],
            "urn:ietf:params:scim:schemas:extension:enterprise:2.0:User": {
                "manager": {
                    "value": "9067729b3d-ee533c18-538a-4cd3-a572-63fb863ed734"
                }
            }
        }
    ]
}
```

### userName

###### Example Request

```
GET https://scim.us-east-1.amazonaws.com/{tenant_id}/scim/v2/Users?filter=userName eq "jdoe"
User-Agent: Mozilla/5.0
Authorization: Bearer <bearer_token>
```

###### Example Response

```
HTTP/1.1 200
Date: Wed, 22 Jul 2020 22:53:33 GMT
Content-Type: application/json
x-amzn-RequestId: a8764ca2-899f-4362-871d-3f255671ca1f

{
    "totalResults": 1,
    "itemsPerPage": 1,
    "startIndex": 1,
    "schemas": [
        "urn:ietf:params:scim:api:messages:2.0:ListResponse"
    ],
    "Resources": [
        {
            "id": "90677c608a-685d5bf3-efab-48c8-b3b1-648fc5c5d980",
            "externalId": "701985",
            "meta": {
                "resourceType": "User",
                "created": "2020-07-22T22:17:47Z",
                "lastModified": "2020-07-22T22:17:47Z"
            },
            "schemas": [
                "urn:ietf:params:scim:schemas:core:2.0:User",
                "urn:ietf:params:scim:schemas:extension:enterprise:2.0:User"
            ],
            "userName": "jdoe",
            "name": {
                "familyName": "John",
                "givenName": "Doe",
                "honorificPrefix": "Mr.",
                "honorificSuffix": "III"
            },
            "displayName": "jdoe",
            "nickName": "Johnny",
            "active": false,
            "emails": [
                {
                    "value": "johndoe@example.com",
                    "type": "work",
                    "primary": true
                }
            ],
            "urn:ietf:params:scim:schemas:extension:enterprise:2.0:User": {
                "manager": {
                    "value": "9067729b3d-ee533c18-538a-4cd3-a572-63fb863ed734"
                }
            }
        }
    ]
}
```

### User id and

manager

Both `id` and `manager` can be used together, and their
order can be interchanged.

###### Example Request

```
GET https://scim.us-east-1.amazonaws.com/{tenant_id}/scim/v2/Users?filter=id eq "90677c608a-7afcdc23-0bd4-4fb7-b2ff-10ccffdff447" and manager eq "9067729b3d-ee533c18-538a-4cd3-a572-63fb863ed734"
User-Agent: Mozilla/5.0
Authorization: Bearer <bearer_token>
```

###### Example Response

```
HTTP/1.1 200
Date: Wed, 22 Jul 2020 22:42:29 GMT
Content-Type: application/json
x-amzn-RequestId: 23178777-466c-44fb-b5b4-7efc12a766aa
{
    "totalResults": 1,
    "itemsPerPage": 1,
    "startIndex": 1,
    "schemas": [
        "urn:ietf:params:scim:api:messages:2.0:ListResponse"
    ],
    "Resources": [
        {
            "id": "90677c608a-7afcdc23-0bd4-4fb7-b2ff-10ccffdff447",
            "externalId": "702135",
            "meta": {
                "resourceType": "User",
                "created": "2020-07-22T22:32:58Z",
                "lastModified": "2020-07-22T22:32:58Z"
            },
            "schemas": [
                "urn:ietf:params:scim:schemas:core:2.0:User",
                "urn:ietf:params:scim:schemas:extension:enterprise:2.0:User"
            ],
            "userName": "mjack",
            "name": {
                "familyName": "Mark",
                "givenName": "Jackson",
                "honorificPrefix": "Mr.",
                "honorificSuffix": "I"
            },
            "displayName": "mjack",
            "nickName": "Mark",
            "active": false,
            "emails": [
                {
                    "value": "mjack@example.com",
                    "type": "work",
                    "primary": true
                }
            ],
            "urn:ietf:params:scim:schemas:extension:enterprise:2.0:User": {
                "manager": {
                    "value": "9067729b3d-ee533c18-538a-4cd3-a572-63fb863ed734"
                }
            }
        }
    ]
}
```
