# Common Errors

This section lists the error types that the ACXD SDK may return.

## Common Errors

### `ValidationException`

The input does not meet the required format or constraints. Check that all required parameters are included and that values are valid.

HTTP Status Code: 400

### `ResourceNotFoundException`

The specified resource does not exist. Verify the identifier and that the resource has not been deleted.

HTTP Status Code: 404

### `ConflictException`

The request conflicts with an existing resource. For example, creating a secret with a name that already exists.

HTTP Status Code: 409

### `AccessDeniedException`

The programmatic user does not have permission to perform this action. Check the user's role configuration.

HTTP Status Code: 403

### `ThrottlingException`

The request rate is too high. The SDK automatically retries with exponential backoff.

HTTP Status Code: 429

### `InternalServerException`

An internal error occurred. This is retryable. The SDK automatically retries these requests.

HTTP Status Code: 500

### `SerializationException`

The request body could not be parsed. Verify that the request body is valid JSON.

HTTP Status Code: 400

## Error Response Shape

All errors return a consistent JSON body:

```
{
    "type": "ResourceNotFoundException",
    "message": "Secret 'my-secret' not found.",
    "resourceId": "my-secret",
    "resourceType": "Secret"
}
```
