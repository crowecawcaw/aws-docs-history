# Troubleshoot AWS Private CA certificate revocation issues

## OCSP response latency

OCSP responsiveness may be slower if the caller is geographically distant from a
regional edge cache or from the Region of the issuing CA. For more information about
regional edge cache availability, see [Global Edge
Network](https://aws.amazon.com/cloudfront/details#Global_Edge_Network "https://aws.amazon.com/cloudfront/details#Global_Edge_Network"). We recommend issuing certificates in a Region near where they will
be used.

## Revocation of self-signed certificates

You can't revoke a self-signed CA certificate. To functionally revoke the certificate, delete the CA.
