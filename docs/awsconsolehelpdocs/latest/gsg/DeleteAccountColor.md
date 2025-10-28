# DeleteAccountColor

Deletes the account color setting.

## Request Syntax

```
DELETE /v1/account-color HTTP/1.1
```

## Request Parameters

This operation does not use request parameters.

## Request Body

This operation does not have a request body.

## Response Body

This operation does not return a response body.

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
