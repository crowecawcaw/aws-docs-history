

# Using CloudFront Functions with origin mutual TLS
<a name="origin-mtls-cloudfront-functions"></a>

CloudFront Functions provides lightweight, serverless compute at the edge to customize content delivery. When using origin mutual TLS with CloudFront Functions, there are specific behaviors and limitations to be aware of regarding origin selection and manipulation.

## Supported CloudFront Functions operations
<a name="supported-cloudfront-functions-operations"></a>

CloudFront Functions can interact with mTLS-enabled origins in the following ways:

### updateRequestOrigin()
<a name="update-request-origin-function"></a>

The updateRequestOrigin() function supports limited modifications when working with mTLS-enabled origins:
+ **Switching between origin mTLS origins:** You can update the request to route to a different origin that uses origin mTLS, provided both origins use the **same client certificate**. This allows you to implement custom routing logic while maintaining mutual TLS authentication. Switching between origins that make use of different certificates is supported through the `selectRequestOriginById()` and `createRequestOriginGroup()` APIs.
+ **Disabling origin mTLS:** You can switch from a mTLS-enabled origin to a non-mTLS origin by setting `mTLSConfig: 'off'` in the function. This provides flexibility to conditionally disable mutual TLS authentication based on request characteristics.

#### Example: Switching between origin mTLS origins with the same certificate
<a name="example-switching-mtls-origins"></a>

```
import cf from 'cloudfront';

function handler(event) {
    var request = event.request;

    // Route to different origin based on request path
    if (request.uri.startsWith('/api/v2')) {
        cf.updateRequestOrigin({
            "domainName": "api-v2.example.com",
            "mTLSConfig": "inherit",
            // If no value is provided for mTLSConfig, it defaults to inherit
            // Both origins must use the same certificate
        });
    }

    return request;
}
```

#### Example: Conditionally disabling origin mTLS
<a name="example-disabling-mtls"></a>

```
import cf from 'cloudfront';

function handler(event) {
    var request = event.request;

    // Disable mTLS for specific paths
    if (request.uri.startsWith('/public')) {
        cf.updateRequestOrigin({
            "domainName": "public-origin.example.com",
            "mTLSConfig": "off"
        });
    }

    return request;
}
```

### selectRequestOriginById()
<a name="select-request-origin-by-id-mtls"></a>

The `selectRequestOriginById()` function supports selecting origins that have mutual TLS (origin) enabled. You can use this function to dynamically route requests to mTLS-enabled origins configured in your distribution. When selecting a mutual TLS (origin) enabled origin by ID, CloudFront uses the client certificate configured for that origin in the distribution settings.

#### Example: Selecting a mutual TLS (origin) enabled origin by ID
<a name="example-select-mtls-origin-by-id"></a>

```
import cf from 'cloudfront';

function handler(event) {
    var request = event.request;

    // Select mTLS-enabled origin based on request characteristics
    if (request.uri.startsWith('/secure-api')) {
        cf.selectRequestOriginById("mtls-origin-1");
    }

    return request;
}
```

### createRequestOriginGroup()
<a name="create-request-origin-group-mtls"></a>

The `createRequestOriginGroup()` function supports creating origin groups that include mutual TLS (origin) enabled origins. You can dynamically create origin groups with mTLS-enabled origins for failover scenarios within CloudFront Functions.

#### Example: Creating an origin group with mutual TLS (origin) enabled origins
<a name="example-create-mtls-origin-group"></a>

```
import cf from 'cloudfront';

function handler(event) {
    // Create origin group with mTLS-enabled primary and failover origins
    cf.createRequestOriginGroup({
        "originIds": ["mtls-origin-primary", "mtls-origin-failover"],
        "failoverCriteria": {
            "statusCodes": [500, 502, 503, 504]
        }
    });

    return event.request;
}
```