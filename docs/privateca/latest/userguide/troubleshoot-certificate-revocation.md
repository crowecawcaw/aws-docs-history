# Troubleshoot AWS Private CA certificate revocation issues

## OCSP response latency

OCSP responsiveness may be slower if the caller is geographically distant from a
regional edge cache or from the Region of the issuing CA. For more information about
regional edge cache availability, see [Global Edge
Network](https://aws.amazon.com/cloudfront/details#Global_Edge_Network "https://aws.amazon.com/cloudfront/details#Global_Edge_Network"). We recommend issuing certificates in a Region near where they will
be used.

## Amazon S3 bucket creation failure for CRLs

Your private CA may fail to create a destination Amazon S3 bucket for your CRL if Amazon S3 **Block public access
(bucket settings)** are enforced on your account. Check your Amazon S3 settings
if this occurs. For more information, see [Using Amazon S3 Block
Public Access](../../../AmazonS3/latest/userguide/access-control-block-public-access.md "../../../AmazonS3/latest/userguide/access-control-block-public-access.md").

## Revocation of self-signed certificates

You can't revoke a self-signed CA certificate. To functionally revoke the certificate, delete the CA.
