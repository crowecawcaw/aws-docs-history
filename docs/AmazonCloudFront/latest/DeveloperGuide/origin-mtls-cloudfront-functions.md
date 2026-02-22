# Using CloudFront Functions with origin mutual TLS

CloudFront Functions provides lightweight, serverless compute at the edge to customize content delivery. When using origin mutual TLS with CloudFront Functions, there are specific behaviors and limitations to be aware of regarding origin selection and manipulation.

## Supported CloudFront Functions operations

CloudFront Functions can interact with mTLS-enabled origins in the following ways:

### updateRequestOrigin()

The updateRequestOrigin() function supports limited modifications when working with mTLS-enabled origins:

- **Switching between origin mTLS origins:** You can update the request to route to a different origin that uses origin mTLS, provided both origins use the **same client certificate**. This allows you to implement custom routing logic while maintaining mutual TLS authentication.
- **Disabling origin mTLS:** You can switch from a mTLS-enabled origin to a non-mTLS origin by setting `mTLSConfig: 'off'` in the function. This provides flexibility to conditionally disable mutual TLS authentication based on request characteristics.

#### Example: Switching between origin mTLS origins with the same certificate

```
function handler(event) {
    var request = event.request;

    // Route to different origin based on request path
    if (request.uri.startsWith('/api/v2')) {
        request.origin = {
            domainName: 'api-v2.example.com',
            customHeaders: {},
            // Both origins must use the same certificate
        };
    }

    return request;
}
```

#### Example: Conditionally disabling origin mTLS

```
function handler(event) {
    var request = event.request;

    // Disable mTLS for specific paths
    if (request.uri.startsWith('/public')) {
        request.origin = {
            domainName: 'public-origin.example.com',
            customHeaders: {},
            mTLSConfig: 'off'
        };
    }

    return request;
}
```

## Unsupported CloudFront Functions operations

The following CloudFront Functions operations do not support mTLS-enabled origins at general availability:

### selectRequestOriginById()

The `selectRequestOriginById()` function cannot select an origin that has origin mTLS enabled. Attempting to select a mTLS-enabled origin using this function will result in a validation error.

If your use case requires dynamic origin selection with origin mTLS, use `updateRequestOrigin()` instead, ensuring all target origins use the same client certificate.

### createRequestOriginGroup()

The `createRequestOriginGroup()` function does not support creating origin groups that include mTLS-enabled origins. Origin groups with origin mTLS origins cannot be created dynamically through CloudFront Functions.

If you need origin failover capabilities with origin mTLS, configure origin groups directly in your CloudFront distribution settings rather than creating them dynamically in functions.
