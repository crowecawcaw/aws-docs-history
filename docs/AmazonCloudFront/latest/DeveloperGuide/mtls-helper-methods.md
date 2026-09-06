

# Helper methods for mutual TLS
<a name="mtls-helper-methods"></a>

CloudFront provides mTLS-specific helper functions in the `cf.mtls` namespace for viewer request functions. These functions rename, reformat, or combine client certificate headers before forwarding the request to your origin.

```
import cf from "cloudfront";
```

## `cf.mtls.renameClientCertHeaders`
<a name="mtls-rename-client-cert-headers"></a>

Renames certificate metadata headers to custom header names.

```
cf.mtls.renameClientCertHeaders({
    "CloudFront-Viewer-Cert-Pem": "X-Client-Cert",
    "CloudFront-Viewer-Cert-Serial-Number": "X-Client-Cert-Serial",
    "CloudFront-Viewer-Cert-Issuer": "X-Client-Cert-Issuer",
});
```

Allowed source headers:
+ `CloudFront-Viewer-Cert-Pem`
+ `CloudFront-Viewer-Cert-Serial-Number`
+ `CloudFront-Viewer-Cert-Issuer`
+ `CloudFront-Viewer-Cert-Subject`
+ `CloudFront-Viewer-Cert-Validity`
+ `CloudFront-Viewer-Cert-Present`
+ `CloudFront-Viewer-Cert-Sha256`
+ `Client-Cert`
+ `Client-Cert-Chain`

## `cf.mtls.renamePemHeaders`
<a name="mtls-rename-pem-headers"></a>

Renames PEM certificate headers and optionally reformats the certificate encoding.

```
cf.mtls.renamePemHeaders({
    "Client-Cert": {
        "newHeaderName": "X-Leaf-Cert",
        "pemCertFormatInfo": {
            "certHeader": "-----CUSTOM HEADER-----",
            "certFooter": "-----CUSTOM FOOTER-----",
            "certEndMarker": "",
            "keepNewlinesInCertData": true
        }
    },
    "Client-Cert-Chain": {
        "newHeaderName": "X-Intermediate-Certs",
        "pemCertFormatInfo": {
            "certHeader": "-----CUSTOM HEADER-----",
            "certFooter": "-----CUSTOM FOOTER-----",
            "certEndMarker": "",
            "keepNewlinesInCertData": true
        }
    }
});
```

Allowed source headers:
+ In passthrough mode: `Client-Cert`, `Client-Cert-Chain`
+ In required/optional mode: `Cloudfront-Viewer-Cert-PEM`

**`pemCertFormatInfo` fields:**

For `Cloudfront-Viewer-Cert-PEM`:
+ `certHeader` replaces `-----BEGIN CERTIFICATE-----`.
+ `certFooter` replaces `-----END CERTIFICATE-----`.
+ `certEndMarker` sets a custom string after the certFooter.
+ `keepNewlinesInCertData` (default: `true`) preserves newlines in base64 data when true.

For `Client-Cert` and `Client-Cert-Chain`:
+ `certHeader` replaces `:`.
+ `certFooter` replaces `:`.
+ `certEndMarker` sets a custom string after the certFooter.
+ `keepNewlinesInCertData` (default: `false`) preserves newlines in base64 data when true.

## `cf.mtls.combinePemHeaders`
<a name="mtls-combine-pem-headers"></a>

Combines `Client-Cert` and `Client-Cert-Chain` into a single header containing the full certificate chain.

```
cf.mtls.combinePemHeaders({
    "newHeaderName": "X-Full-Chain",
    "pemCertFormatInfo": {
        "certHeader": "-----BEGIN CERTIFICATE-----",
        "certFooter": "-----END CERTIFICATE-----",
        "certEndMarker": "\n",
        "keepNewlinesInCertData": false
    }
});
```

`certEndMarker` sets the delimiter between certificates.

**Note**  
These helper functions can be used in all mTLS modes (required, optional, and passthrough). However, `cf.mtls.combinePemHeaders` only has effect in passthrough mode — in required and optional modes, the `Client-Cert` and `Client-Cert-Chain` headers are not present, so the function is a no-op.
If `cf.mtls.*` methods and `cf.updateRequestOrigin()` with `customHeaders` target the same header name, CloudFront returns a 502 error.
In Passthrough mode, CloudFront drops any incoming `Client-Cert` or `Client-Cert-Chain` headers and re-adds them from the actual client certificate.
CloudFront doesn't present the full raw PEM certificate contents in any edge functions.