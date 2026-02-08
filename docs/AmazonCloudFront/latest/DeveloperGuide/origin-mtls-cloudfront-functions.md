# Using CloudFront Functions with mutual TLS (origin)

CloudFront Functions provides lightweight, serverless compute at the edge to customize content delivery. When using mutual TLS (origin) with CloudFront Functions, there are specific behaviors and limitations to be aware of regarding origin selection and manipulation.

## Supported CloudFront Functions operations

CloudFront Functions can interact with mutual TLS (origin) enabled origins in the following ways:

### updateRequestOrigin()

The updateRequestOrigin() function supports limited modifications when working with mutual TLS (origin) enabled origins:

- **Switching between mutual TLS (origin) origins:** You can update the request to route to a different origin that uses mutual TLS (origin), provided both origins use the **same client certificate**. This allows you to implement custom routing logic while maintaining mutual TLS authentication.
- **Disabling mutual TLS (origin):** You can switch from a mutual TLS (origin) enabled origin to a non-mutual TLS origin by setting `mTLSConfig: 'off'` in the function. This provides flexibility to conditionally disable mutual TLS authentication based on request characteristics.

#### Example: Switching between mutual TLS (origin) origins with the same certificate

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

#### Example: Conditionally disabling mutual TLS (origin)

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

The following CloudFront Functions operations do not support mutual TLS (origin) enabled origins at general availability:

### selectRequestOriginById()

The `selectRequestOriginById()` function cannot select an origin that has mutual TLS (origin) enabled. Attempting to select a mutual TLS (origin) enabled origin using this function will result in a validation error.

If your use case requires dynamic origin selection with mutual TLS (origin), use `updateRequestOrigin()` instead, ensuring all target origins use the same client certificate.

### createRequestOriginGroup()

The `createRequestOriginGroup()` function does not support creating origin groups that include mutual TLS (origin) enabled origins. Origin groups with mutual TLS (origin) origins cannot be created dynamically through CloudFront Functions.

If you need origin failover capabilities with mutual TLS (origin), configure origin groups directly in your CloudFront distribution settings rather than creating them dynamically in functions.
