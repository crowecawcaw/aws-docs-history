# Implement certificate revocation for mutual TLS (viewer) with CloudFront Functions and KeyValueStore

You can use CloudFront Connection Functions with KeyValueStore to implement certificate
revocation checking. This lets you maintain a list of revoked certificate serial numbers
and check client certificates against this list during the TLS handshake.

To implement certificate revocation, you need these components:

- A distribution configured with viewer mTLS
- A KeyValueStore containing revoked certificate serial numbers
- A Connection Function that queries the KeyValueStore to check certificate
  status
  When a client connects, CloudFront validates the certificate against the trust store, then
  runs your Connection Function. Your function checks the certificate serial number
  against the KeyValueStore and allows or denies the connection.

###### Topics

- [Step 1: Create a KeyValueStore for revoked certificates](create-kvs-revoked-certificates.md "create-kvs-revoked-certificates.md")
- [Step 2: Create the revocation Connection Function](create-revocation-connection-function.md "create-revocation-connection-function.md")
- [Step 3: Test your revocation function](test-revocation-function.md "test-revocation-function.md")
- [Step 4: Associate the function to your distribution](associate-function-distribution.md "associate-function-distribution.md")
- [Advanced revocation scenarios](advanced-revocation-scenarios.md "advanced-revocation-scenarios.md")
