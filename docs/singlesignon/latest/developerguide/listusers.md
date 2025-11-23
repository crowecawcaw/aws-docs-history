# ListUsers

This endpoint provides the ability to perform filter queries on an existing list of
users through a `GET` request to `/Users` by inserting additional
filters. A maximum of 100 results can be returned per page. See the **Constraints** section for more
information.

## Not supported

The IAM Identity Center SCIM implementation does not support the following aspects of this API
operation.

- `startIndex`, `attributes`, and
  `excludedAttributes` (despite being listed in the SCIM
  protocol)

## Query Parameters

ListUsers currently supports the following optional query parameters:

- `cursor` used to specify the next page for paginated calls
  - Pattern: [-a-zA-Z0-9+=/:\_]\*
  - Response format: Including the cursor parameter changes the default response format from non-paginated (with totalResults, startIndex, and itemsPerPage fields) to cursor-based paginated results (with itemsPerPage and nextCursor fields)

- `count` used to specify the maximum number of results per page
  - Valid Range: Minimum value of 1. Maximum value of 100.
  - Default: 100

- `filter` used to filter out specific users

## Constraints

The IAM Identity Center SCIM implementation has the following constraints for this API
operation.

- The `ListUsers` API is capable of returning up to a maximum of 100 results per page.
- Supported filter combinations: (`userName`),
  (`externalId`), (`groups.value`), (`id` and `manager`),
  (`manager` and `id`). Note that the use of
  `id` as an individual filter, though valid, should be avoided
  as a `getUser` endpoint is already available.
- Pagination requests must include `cursor` in the query parameters
  - The first request made with cursor must be empty (eg. https://.../Users?cursor)
  - If the response includes a nextCursor field, its value can be used as the cursor value to retrieve the next page of results

- Paginated calls may return less results than count but as long as nextCursor is present in the response, additional pages are available.
- Supported comparison operator in filters: `eq`
- Filter must be specified as follows: `<filterAttribute> eq
"<filterValue>"`

## Errors

The following IAM Identity Center SCIM implementation errors are common for this API
operation.

| Error                     | Condition                                                                                                                                                                                                | HTTP Status Code |
| ------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------- |
| `ValidationException`     | Request cannot be parsed, is syntactically incorrect, or violates<br>schema. This error also occurs if the operation is<br>unsupported, or if filter parameters are changed between pagination requests. | 400              |
| `UnauthorizedException`   | Authorization header is invalid or missing. This error also<br>occurs if the tenant ID is incorrect.                                                                                                     | 401              |
| `AccessDeniedException`   | Operation is not permitted based on the supplied<br>authorization.                                                                                                                                       | 403              |
| `ThrottlingException`     | Too many requests exceeded the limits.                                                                                                                                                                   | 429              |
| `InternalServerException` | Service failed to process the request.                                                                                                                                                                   | 500              |

## Pagination Examples

### Example Request For First Page

###### Example Request

```
GET https://scim.us-east-1.amazonaws.com/{tenant_id}/scim/v2/Users?cursor
Authorization: Bearer <bearer_token>
```

###### Example Response

```
{
  "itemsPerPage": 100,
  "nextCursor": "VGVzdFVzZXJDdXJzb3I",
  "schemas": [
    "urn:ietf:params:scim:api:messages:2.0:ListResponse"
  ],
  "Resources": [
    ...
  ]
}
```

### Example Request For Getting the Next Page

_Note: the example does not include a `nextCursor` field since the current page is the last page of results_

###### Example Request

```
GET https://scim.us-east-1.amazonaws.com/{tenant_id}/scim/v2/Users?cursor=VGVzdFVzZXJDdXJzb3I
Authorization: Bearer <bearer_token>
```

###### Example Response

```
{
  "itemsPerPage": 100,
  "schemas": [
    "urn:ietf:params:scim:api:messages:2.0:ListResponse"
  ],
  "Resources": [
    ...
  ]
}
```

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
- `groups.value`
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

### groups.value

#### Example Request Without Pagination

###### Example Request

```
GET https://scim.us-east-1.amazonaws.com/{tenant_id}/scim/v2/Users?filter=groups.value eq "0458a488-2081-70c8-4b0b-3e4b2b10ddb5"
Authorization: Bearer <bearer_token>
```

###### Example Response

```
{
  "totalResults": 100,
  "itemsPerPage": 100,
  "startIndex": 1,
  "schemas": [
    "urn:ietf:params:scim:api:messages:2.0:ListResponse"
  ],
  "Resources": [
    {
      "id": "5418a458-c0a1-7066-bdd4-9ea543c0cf6d",
      "externalId": "eid_XftxVGp61hDs6Dugey2R",
      "meta": {
        "resourceType": "User",
        "created": "2025-07-30T17:13:10Z",
        "lastModified": "2025-07-30T17:13:10Z"
      },
      "schemas": [
        "urn:ietf:params:scim:schemas:core:2.0:User",
        "urn:ietf:params:scim:schemas:extension:enterprise:2.0:User"
      ],
      "userName": "username_XftxVGp61hDs6Dugey2R",
      "name": {
        "formatted": "formatted_XftxVGp61hDs6Dugey2R",
        "familyName": "familyname_XftxVGp61hDs6Dugey2R",
        "givenName": "givenname_XftxVGp61hDs6Dugey2R",
        "middleName": "middlename_XftxVGp61hDs6Dugey2R",
        "honorificPrefix": "Ms.",
        "honorificSuffix": "III"
      },
      "displayName": "displayname_XftxVGp61hDs6Dugey2R",
      "nickName": "nickName_XftxVGp61hDs6Dugey2R",
      "title": "Tour Guide",
      "userType": "Employee",
      "preferredLanguage": "en-US",
      "locale": "en-US",
      "timezone": "America/Los_Angeles",
      "active": true,
      "emails": [
        {
          "value": "XftxVGp61hDs6Dugey2R@example.com",
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
          "type": "work",
          "primary": true
        }
      ],
      "urn:ietf:params:scim:schemas:extension:enterprise:2.0:User": {
        "employeeNumber": "employeeNumber_XftxVGp61hDs6Dugey2R",
        "costCenter": "4130",
        "organization": "Universal Studios",
        "division": "Theme Park",
        "department": "Tour Operations"
      }
    },
    ...
  ]
}
```

#### Example Request With Pagination

###### Example Request

```
GET https://scim.us-east-1.amazonaws.com/{tenant_id}/scim/v2/Users?cursor&filter=groups.value eq "0458a488-2081-70c8-4b0b-3e4b2b10ddb5"
Authorization: Bearer <bearer_token>
```

###### Example Response

```
{
  "itemsPerPage": 100,
  "nextCursor": "Q3Vyc29yVXNlckZpbHRlcg",
  "schemas": [
    "urn:ietf:params:scim:api:messages:2.0:ListResponse"
  ],
  "Resources": [
    ...
  ]
}
```

#### Example Request For Getting the Next Page

###### Example Request

```
GET https://scim.us-east-1.amazonaws.com/{tenant_id}/scim/v2/Users?cursor=Q3Vyc29yVXNlckZpbHRlcg&filter=groups.value eq "0458a488-2081-70c8-4b0b-3e4b2b10ddb5"
Authorization: Bearer <bearer_token>
```

###### Example Response

```
{
  "itemsPerPage": 10,
  "schemas": [
    "urn:ietf:params:scim:api:messages:2.0:ListResponse"
  ],
  "Resources": [
    ...
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
