# GetSchema

Information about supported SCIM schemas can be retrieved by making a request to the `/Schemas` endpoint. See the Examples section.

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

| Error                     | Condition                                                                                                                               | HTTP Status Code |
| ------------------------- | --------------------------------------------------------------------------------------------------------------------------------------- | ---------------- |
| `ValidationException`     | Request cannot be parsed, is syntactically incorrect, or violates<br>schema. This error also occurs if the operation is<br>unsupported. | 400              |
| `UnauthorizedException`   | Authorization header is invalid or missing. This error also<br>occurs if the tenant ID is incorrect.                                    | 401              |
| `AccessDeniedException`   | Operation is not permitted based on the supplied<br>authorization.                                                                      | 403              |
| `ThrottlingException`     | Too many requests exceeded the limits.                                                                                                  | 429              |
| `InternalServerException` | Service failed to process the request.                                                                                                  | 500              |

## Example

Following are example request and response for this API operation.

###### Example Request

```
GET /{tenant_id}/scim/v2/Schemas/urn:ietf:params:scim:schemas:core:2.0:User
User-Agent: Mozilla/5.0
Authorization: Bearer <bearer_token>
```

###### Example Response

```
HTTP/2 200 OK
Date: Fri, 12 May 2023 17:00:33 GMT
Content-Type: application/json
Content-Length: 2
x-amzn-Requestid: 80cc7268-02b8-4e37-a787-da7b9b7a1952
{
    "id" : "urn:ietf:params:scim:schemas:core:2.0:User",
    "name" : "User",
    "description" : "User Account",
    "attributes" : [
      {
        "name" : "userName",
        "type" : "string",
        "multiValued" : false,
        "description" : "Unique identifier for the User, typically used by the user to directly authenticate to the service provider. Each User MUST include a non-empty userName value.  This identifier MUST be unique across the service provider's entire set of Users. REQUIRED.",
        "required" : true,
        "caseExact" : false,
        "mutability" : "readWrite",
        "returned" : "default",
        "uniqueness" : "server"
      }
    ]
}
```
