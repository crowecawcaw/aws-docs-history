# Viewer mTLS headers for cache policies and forwarded to origin

When using mutual TLS authentication, CloudFront can extract information from client certificates and forward it to your origins as HTTP headers. This allows your origin servers to access certificate details without implementing certificate validation logic.

The following headers are available to for creating cache behaviors:

| Header name                          | Description                                                                                                                   | Example value                                                    |
| ------------------------------------ | ----------------------------------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------- |
| CloudFront-Viewer-Cert-Serial-Number | Hexadecimal representation of the certificate serial number                                                                   | 4a:3f:5c:92:d1:e8:7b:6c                                          |
| CloudFront-Viewer-Cert-Issuer        | RFC2253 string representation of the issuer's distinguished name (DN)                                                         | CN=rootcamtls.com,OU=rootCA,O=mTLS,L=Seattle,ST=Washington,C=US  |
| CloudFront-Viewer-Cert-Subject       | RFC2253 string representation of the subject's distinguished name (DN)                                                        | CN=client\_.com,OU=client-3,O=mTLS,ST=Washington,C=US            |
| CloudFront-Viewer-Cert-Present       | Either 1 (present) or 0 (not present) indicating whether the certificate is present. This value is always 1 in Required mode. | 1                                                                |
| CloudFront-Viewer-Cert-Sha256        | The SHA256 hash of the client certificate                                                                                     | 01fbf94fef5569753420c349f49adbfd80af5275377816e3ab1fb371b29cb586 |

For origin requests, two additional headers are supplied, in addition the headers above made available for cache behaviors:

| Header name                     | Description                                       | Example value                                                                                                          |
| ------------------------------- | ------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------- |
| CloudFront-Viewer-Cert-Validity | ISO8601 format of the notBefore and notAfter date | CloudFront-Viewer-Cert-Validity: NotBefore=2023-09-21T01:50:17Z;NotAfter=2024-09-20T01:50:17Z                          |
| CloudFront-Viewer-Cert-Pem      | URL-encoded PEM format of the leaf certificate    | CloudFront-Viewer-Cert-Pem: -----BEGIN%20CERTIFICATE-----%0AMIIG<...reduced...>NmrUlw%0A-----END%20CERTIFICATE-----%0A |

## Configure header forwarding

### Console

In verify mode, CloudFront automatically adds the CloudFront-Viewer-Cert-\* headers to all viewer requests. To forward these headers to your origin:

1. From the main list distributions page, select your distribution with
   viewer mTLS enabled and go to the **Behaviors**
   tab
2. Select the cache behavior and choose **Edit**
3. In the **Origin request policy** section, choose
   **Create policy** or select an existing
   policy
4. Ensure the following headers are included in the origin request policy:
   - CloudFront-Viewer-Cert-Serial-Number
   - CloudFront-Viewer-Cert-Issuer
   - CloudFront-Viewer-Cert-Subject
   - CloudFront-Viewer-Cert-Present
   - Cloudfront-Viewer-Cert-Sha256
   - CloudFront-Viewer-Cert-Validity
   - CloudFront-Viewer-Cert-Pem

5. Choose **Create** (for new policies) or
   **Save changes** (for existing policies)
6. Select the policy within your cache behavior and save changes

### Using AWS CLI

The following example shows how to create an origin request policy that includes mTLS headers for verify mode:

```
aws cloudfront create-origin-request-policy \
  --origin-request-policy-config '{
    "Name": "MTLSHeadersPolicy",
    "HeadersConfig": {
      "HeaderBehavior": "whitelist",
      "Headers": {
        "Quantity": 5,
        "Items": [
          "CloudFront-Viewer-Cert-Serial-Number",
          "CloudFront-Viewer-Cert-Issuer",
          "CloudFront-Viewer-Cert-Subject",
          "CloudFront-Viewer-Cert-Validity",
          "CloudFront-Viewer-Cert-Pem"
        ]
      }
    },
    "CookiesConfig": {
      "CookieBehavior": "none"
    },
    "QueryStringsConfig": {
      "QueryStringBehavior": "none"
    }
  }'
```

## Header processing considerations

When working with certificate headers, consider these best practices:

- **Header validation:** Verify certificate header values at your origin as an additional security measure
- **Header size limits:** The PEM certificate headers can be large, ensure your origin server can handle them
- **Cache considerations:** Using certificate headers in your cache key increases cache fragmentation
- **Cross-origin requests:** If your application uses CORS, then you may need to configure it to allow the certificate headers

## Next steps

After configuring header forwarding, you can implement certificate revocation
checking using CloudFront Connection Functions and KeyValueStore. For details on
implementing revocation checks, see [Revocation using CloudFront Connection Function and KVS](revocation-connection-function-kvs.md "revocation-connection-function-kvs.md").
