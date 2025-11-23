# ListGroups

You can use the `/Groups` endpoint to filter queries on a list of existing
groups by making a `GET` request with additional filter information. A maximum of 100 results can be returned per page. See the
**Constraints** section for a list of available
filters.

## Not supported

The IAM Identity Center SCIM implementation does not support the following aspects of this API
operation.

- `GetGroup` and `ListGroups` return an empty member
  list. To see group info for a certain member, call `ListGroups`
  with a member filter. (See the examples that follow.)

## Query Parameters

ListGroups currently supports the following optional query parameters:

- `cursor` used to specify which page to retrieve in paginated API calls.
  - Pattern: [-a-zA-Z0-9+=/:\_]\*
  - Response format: Including the cursor parameter changes the default response format from non-paginated (with totalResults, startIndex, and itemsPerPage fields) to cursor-based paginated results (with itemsPerPage and nextCursor fields)

- `count` used to specify the maximum number of results per page
  - Valid Range: Minimum value of 1. Maximum value of 100.
  - Default: 100

- `filter` used to filter out specific groups

## Constraints

The IAM Identity Center SCIM implementation has the following constraints for this API
operation.

- The `ListGroups` API is capable of returning up to a maximum of 100 results per page.
- Supported filter combinations: (`displayName`), (`externalId`), (`members.value`),
  (`id` and `member`), and (`member` and
  `id`). Note that the use of id as an individual filter, while
  valid, should be avoided as there is already a getGroup endpoint
  available.
- Pagination requests must include `cursor` in the query parameters
  - The first request made with cursor must be empty (eg. https://.../Groups?cursor)
  - If the response includes a nextCursor field, its value can be used as the cursor value to retrieve the next page of results

- Paginated calls may return less results than count but as long as nextCursor is present in the response, additional pages are available.
- Supported comparison operator in filters: `eq`
- Filter must be specified as: `<filterAttribute> eq
"<filterValue>"`

## Errors

The following IAM Identity Center SCIM implementation errors are common for this API
operation.

| Error                       | Condition                                                                                                                                                                                                | HTTP Status Code |
| --------------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------- |
| `ValidationException`       | Request cannot be parsed, is syntactically incorrect, or violates<br>schema. This error also occurs if the operation is<br>unsupported, or if filter parameters are changed between pagination requests. | 400              |
| `UnauthorizedException`     | Authorization header is invalid or missing. This error also<br>occurs if the tenant ID is incorrect.                                                                                                     | 401              |
| `AccessDeniedException`     | Operation is not permitted based on the supplied<br>authorization.                                                                                                                                       | 403              |
| `ResourceNotFoundException` | When filter querying with a nonexisting member.                                                                                                                                                          | 404              |
| `ThrottlingException`       | Too many requests exceeded the limits.                                                                                                                                                                   | 429              |
| `InternalServerException`   | Service failed to process the request.                                                                                                                                                                   | 500              |

## Pagination Examples

### Example Request For Getting the First Page

###### Example Request

```
GET https://scim.us-east-1.amazonaws.com/{tenant_id}/scim/v2/Groups?cursor
Authorization: Bearer <bearer_token>
```

###### Example Response

```
{
  "itemsPerPage": 100,
  "nextCursor": "VGVzdEdyb3VwQ3Vyc29y",
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
GET https://scim.us-east-1.amazonaws.com/{tenant_id}/scim/v2/Groups?cursor=VGVzdEdyb3VwQ3Vyc29y
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
GET https://scim.us-east-1.amazonaws.com/{tenant_id}/scim/v2/Groups
User-Agent: Mozilla/5.0
Authorization: Bearer <bearer_token>
```

###### Example Response

```
HTTP/1.1 200
 Date: Thu, 23 Jul 2020 00:37:15 GMT
 Content-Type: application/json
 x-amzn-RequestId: e01400a1-0f10-4e90-ba58-ea1766a009d7

 {
    "totalResults": 6,
    "itemsPerPage": 6,
    "startIndex": 1,
    "schemas": [
        "urn:ietf:params:scim:api:messages:2.0:ListResponse"
    ],
    "Resources": [
        {
            "id": "90677c608a-ef9cb2da-d480-422b-9901-451b1bf9e607",
            "externalId": "702135",
            "meta": {
                "resourceType": "Group",
                "created": "2020-07-22T23:10:21Z",
                "lastModified": "2020-07-22T23:10:21Z"
            },
            "schemas": [
                "urn:ietf:params:scim:schemas:core:2.0:Group"
            ],
            "displayName": "Group Foo",
            "members": []
        },
        {
            "id": "90677c608a-95aca21b-4bb7-4161-94cb-d885e2920414",
            "meta": {
                "resourceType": "Group",
                "created": "2020-07-23T00:16:49Z",
                "lastModified": "2020-07-23T00:16:49Z"
            },
            "schemas": [
                "urn:ietf:params:scim:schemas:core:2.0:Group"
            ],
            "displayName": "Group Beta",
            "members": []
        },
        {
            "id": "90677c608a-00dbcb72-e0b2-49a0-86a2-c259369fc6a7",
            "meta": {
                "resourceType": "Group",
                "created": "2020-07-23T00:18:08Z",
                "lastModified": "2020-07-23T00:18:08Z"
            },
            "schemas": [
                "urn:ietf:params:scim:schemas:core:2.0:Group"
            ],
            "displayName": "Group Omega",
            "members": []
        },
        {
            "id": "90677c608a-10d47528-1e68-4730-910e-c8a102121f47",
            "meta": {
                "resourceType": "Group",
                "created": "2020-07-22T22:58:48Z",
                "lastModified": "2020-07-22T22:58:48Z"
            },
            "schemas": [
                "urn:ietf:params:scim:schemas:core:2.0:Group"
            ],
            "displayName": "Group Bar",
            "members": []
        },
        {
            "id": "90677c608a-6ba7b52f-67e5-4849-b64c-15464fe7893b",
            "meta": {
                "resourceType": "Group",
                "created": "2020-07-23T00:14:19Z",
                "lastModified": "2020-07-23T00:14:19Z"
            },
            "schemas": [
                "urn:ietf:params:scim:schemas:core:2.0:Group"
            ],
            "displayName": "Group Delta",
            "members": []
        },
        {
            "id": "90677c608a-a9f17294-7931-41a5-9c00-6e7ace3c2c11",
            "meta": {
                "resourceType": "Group",
                "created": "2020-07-23T00:20:08Z",
                "lastModified": "2020-07-23T00:20:08Z"
            },
            "schemas": [
                "urn:ietf:params:scim:schemas:core:2.0:Group"
            ],
            "displayName": "Group Gamma",
            "members": []
        }
    ]
}
```

## Filter examples

For the ListGroup endpoint we support three different combinations of filters as
follows:

- `displayName`
- `externalId`
- `members.value`
- `id` and `member`
- `member` and `id`

The filters can be applied in the formats as shown.

**Single filter**

```
filter=<filterAttribute> eq "<filterValue>"
```

**Two filters**

```
filter=<filterAttribute1> eq "<filterValue1>" and <filterAttribute2> eq "<filterValue2>"
```

See the following examples.

### displayName

###### Example Request

```
GET https://scim.us-east-1.amazonaws.com/{tenant_id}/scim/v2/Groups?filter=displayName eq "Group Bar"
User-Agent: Mozilla/5.0
Authorization: Bearer <bearer_token>
```

###### Example Response

```
HTTP/1.1 200
Date: Wed, 22 Jul 2020 23:06:38 GMT
Content-Type: application/json
x-amzn-RequestId: 45995b44-02cd-419f-87f4-ff8fa323448d

{
    "totalResults": 1,
    "itemsPerPage": 1,
    "startIndex": 1,
    "schemas": [
        "urn:ietf:params:scim:api:messages:2.0:ListResponse"
    ],
    "Resources": [
        {
            "id": "90677c608a-10d47528-1e68-4730-910e-c8a102121f47",
            "meta": {
                "resourceType": "Group",
                "created": "2020-07-22T22:58:48Z",
                "lastModified": "2020-07-22T22:58:48Z"
            },
            "schemas": [
                "urn:ietf:params:scim:schemas:core:2.0:Group"
            ],
            "displayName": "Group Bar",
            "members": []
        }
    ]
}
```

### externalId

###### Example Request

```
GET https://scim.us-east-1.amazonaws.com/{tenant_id}/scim/v2/Groups?filter=externalId eq "705167"
User-Agent: Mozilla/5.0
Authorization: Bearer <bearer_token>
```

###### Example Response

```
HTTP/1.1 200
Date: Wed, 22 Jul 2020 23:06:38 GMT
Content-Type: application/json
x-amzn-RequestId: 45995b44-02cd-419f-87f4-ff8fa323448d

{
 "totalResults": 1,
 "itemsPerPage": 1,
 "startIndex": 1,
 "schemas": [
 "urn:ietf:params:scim:api:messages:2.0:ListResponse"
 ],
 "Resources": [
    {
        "id": "90677c608a-ef9cb2da-d480-422b-9901-451b1bf9e607",
        "externalId": "702135",
        "meta": {
             "resourceType": "Group",
             "created": "2020-07-22T23:10:21Z",
             "lastModified": "2020-07-22T23:10:21Z"
        },
        "schemas": [
            "urn:ietf:params:scim:schemas:core:2.0:Group"
        ],
        "displayName": "Group Foo",
        "members": []
    }
  ]
}
```

### members.value

#### Example Request Without Pagination

###### Example Request

```
GET https://scim.us-east-1.amazonaws.com/{tenant_id}/scim/v2/Groups?filter=members.value eq "04285428-40b1-7000-1624-dbde7efebbbf"
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
      "id": "d468e4d8-c051-703d-dd84-28caf445f15e",
      "externalId": "eid_RuvdCnwuJD4KNi2zyiRe",
      "meta": {
        "resourceType": "Group",
        "created": "2025-08-08T17:28:12Z",
        "lastModified": "2025-08-08T17:28:12Z"
      },
      "schemas": [
        "urn:ietf:params:scim:schemas:core:2.0:Group"
      ],
      "displayName": "display_name_eid_RuvdCnwuJD4KNi2zyiRe",
      "members": []
    },
    ...
  ]
}
```

#### Example Request With Pagination

###### Example Request

```
GET https://scim.us-east-1.amazonaws.com/{tenant_id}/scim/v2/Groups?cursor&filter=members.value eq "04285428-40b1-7000-1624-dbde7efebbbf"
Authorization: Bearer <bearer_token>
```

###### Example Response

```
{
  "itemsPerPage": 100,
  "nextCursor": "Q3Vyc29yR3JvdXBzRmlsdGVy",
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
GET https://scim.us-east-1.amazonaws.com/{tenant_id}/scim/v2/Groups?cursor=Q3Vyc29yR3JvdXBzRmlsdGVy&filter=members.value eq "04285428-40b1-7000-1624-dbde7efebbbf"
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

### Group id and

members

Both group `id` and `members` are interchangeable in
order.

###### Example Request

```
GET https://scim.us-east-1.amazonaws.com/{tenant_id}/scim/v2/Groups?filter=id eq "90677c608a-a9f17294-7931-41a5-9c00-6e7ace3c2c11" and members eq "90677c608a-787142a0-3f27-4cd3-afb6-8aed7ce87094"
User-Agent: Mozilla/5.0
Authorization: Bearer <bearer_token>
```

###### Example Response

```
HTTP/1.1 200
Date: Wed, 22 Jul 2020 23:06:38 GMT
Content-Type: application/json
x-amzn-RequestId: 65d18c02-fc7c-4f2b-9410-ed417acf4fb2

{
    "totalResults": 1,
    "itemsPerPage": 1,
    "startIndex": 1,
    "schemas": [
        "urn:ietf:params:scim:api:messages:2.0:ListResponse"
    ],
    "Resources": [
        {
            "id": "90677c608a-a9f17294-7931-41a5-9c00-6e7ace3c2c11",
            "meta": {
                "resourceType": "Group",
                "created": "2020-07-23T00:20:08Z",
                "lastModified": "2020-07-23T00:20:08Z"
            },
            "schemas": [
                "urn:ietf:params:scim:schemas:core:2.0:Group"
            ],
            "displayName": "Group Gamma",
            "members": []
        }
    ]
}
```
