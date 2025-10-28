# GetAccountColor

Gets the color associated with the account.

## Request Syntax

```
GET /v1/account-color HTTP/1.1
```

The request does not use URI parameters or include a request body.

## Response Syntax

```
HTTP/1.1 200
Content-type: application/json

{
    "color": "string"
}
```

## Response Elements

**color**

The color associated with the account.

Type: String

Valid Values: none | pink | purple | darkBlue | lightBlue | teal | green | yellow | orange | red

## Errors

For information about errors common to all actions, see Common Errors.

**AccessDeniedException**

User does not have sufficient access to perform this action.

HTTP Status Code: 403

**InternalServerException**

Unexpected error during processing of request.

HTTP Status Code: 500

**ThrottlingException**

Request was denied due to request throttling.

HTTP Status Code: 429

**ValidationException**

This exception is thrown when the notification event fails validation.

HTTP Status Code: 400
