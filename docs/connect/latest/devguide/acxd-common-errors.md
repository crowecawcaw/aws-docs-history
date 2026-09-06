

# Common Errors
<a name="acxd-common-errors"></a>

This section lists the error types that the ACXD SDK may return.

## Common Errors
<a name="acxd-common-errors-list"></a>

### `ValidationException`
<a name="acxd-common-errors-validationexception"></a>

The input does not meet the required format or constraints. Check that all required parameters are included and that values are valid.

HTTP Status Code: 400

### `ResourceNotFoundException`
<a name="acxd-common-errors-resourcenotfoundexception"></a>

The specified resource does not exist. Verify the identifier and that the resource has not been deleted.

HTTP Status Code: 404

### `ConflictException`
<a name="acxd-common-errors-conflictexception"></a>

The request conflicts with an existing resource. For example, creating a secret with a name that already exists.

HTTP Status Code: 409

### `AccessDeniedException`
<a name="acxd-common-errors-accessdeniedexception"></a>

The programmatic user does not have permission to perform this action. Check the user's role configuration.

HTTP Status Code: 403

### `ThrottlingException`
<a name="acxd-common-errors-throttlingexception"></a>

The request rate is too high. The SDK automatically retries with exponential backoff.

HTTP Status Code: 429

### `InternalServerException`
<a name="acxd-common-errors-internalserverexception"></a>

An internal error occurred. This is retryable. The SDK automatically retries these requests.

HTTP Status Code: 500

### `SerializationException`
<a name="acxd-common-errors-serializationexception"></a>

The request body could not be parsed. Verify that the request body is valid JSON.

HTTP Status Code: 400

## Error Response Shape
<a name="acxd-common-errors-response-shape"></a>

All errors return a consistent JSON body:

```
{
    "type": "ResourceNotFoundException",
    "message": "Secret 'my-secret' not found.",
    "resourceId": "my-secret",
    "resourceType": "Secret"
}
```