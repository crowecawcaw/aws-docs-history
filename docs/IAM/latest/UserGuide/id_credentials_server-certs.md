# Manage server certificates in IAM

To enable HTTPS connections to your website or application in AWS, you need an SSL/TLS
_server certificate_. For certificates in a Region supported by AWS Certificate Manager
(ACM), we recommend that you use ACM to provision, manage, and deploy your server
certificates. In unsupported Regions, you must use IAM as a certificate manager. To learn
which Regions ACM supports, see [AWS Certificate Manager endpoints and
quotas](../../../general/latest/gr/acm.md "../../../general/latest/gr/acm.md") in the _AWS General Reference_.

###### Important

ACM is the preferred tool to provision, manage, and deploy your
server certificates. With ACM you can request a certificate or deploy an existing ACM or
external certificate to AWS resources. Certificates provided by ACM are free and
automatically renew. In a [supported Region](../../../general/latest/gr/acm.md "../../../general/latest/gr/acm.md"), you can
use ACM to manage server certificates from the console or programmatically. For more
information about using ACM, see the [_AWS Certificate Manager User Guide_](../../../acm/latest/userguide/acm-overview.md "../../../acm/latest/userguide/acm-overview.md"). For more information about requesting an
ACM certificate, see [Request a Public
Certificate](../../../acm/latest/userguide/gs-acm-request-public.md "../../../acm/latest/userguide/gs-acm-request-public.md") or [Request a
Private Certificate](../../../acm/latest/userguide/gs-acm-request-private.md "../../../acm/latest/userguide/gs-acm-request-private.md") in the _AWS Certificate Manager User Guide_. For more information
about importing third-party certificates into ACM, see [Importing Certificates](../../../acm/latest/userguide/import-certificate.md "../../../acm/latest/userguide/import-certificate.md") in the
_AWS Certificate Manager User Guide_.

Use IAM as a certificate manager only when you must support HTTPS connections in a Region
that is not [supported by ACM](../../../general/latest/gr/acm.md "../../../general/latest/gr/acm.md"). IAM securely
encrypts your private keys and stores the encrypted version in IAM SSL certificate storage.
IAM supports deploying server certificates in all Regions, but you must obtain your
certificate from an external provider for use with AWS. You cannot upload an ACM certificate
to IAM. Additionally, you cannot manage your certificates from the IAM Console.

For more information about uploading third-party certificates to IAM, see the following
topics.

###### Topics

- [Upload a server certificate (AWS API)](#upload-server-certificate "#upload-server-certificate")
- [AWS API operations for server
  certificates](#id_credentials_server-certs-api "#id_credentials_server-certs-api")
- [Troubleshoot server certificates](#server-certificate-troubleshooting "#server-certificate-troubleshooting")

## Upload a server certificate (AWS API)

To upload a server certificate to IAM, you must provide the certificate and its matching
private key. When the certificate is not self-signed, you must also provide a certificate
chain. (You don't need a certificate chain when uploading a self-signed certificate.) Before
you upload a certificate, ensure that you have all these items and that they meet the
following criteria:

- The certificate must be valid at the time of upload. You cannot upload a certificate
  before its validity period begins (the certificate's `NotBefore` date) or after
  it expires (the certificate's `NotAfter` date).
- The private key must be unencrypted. You cannot upload a private key that is protected
  by a password or passphrase. For help decrypting an encrypted private key, see [Troubleshoot server certificates](#server-certificate-troubleshooting "#server-certificate-troubleshooting").
- The certificate, private key, and certificate chain must all be PEM-encoded. For help
  converting these items to PEM format, see [Troubleshoot server certificates](#server-certificate-troubleshooting "#server-certificate-troubleshooting").

To use the [IAM API](../APIReference.md "../APIReference.md") to upload a certificate, send an
[UploadServerCertificate](../APIReference/API_UploadServerCertificate.md "../APIReference/API_UploadServerCertificate.md")
request. The following example shows how to do this with the [AWS Command Line Interface (AWS CLI)](https://aws.amazon.com/cli/ "https://aws.amazon.com/cli/"). The example assumes the following:

- The PEM-encoded certificate is stored in a file named
  `Certificate.pem`.
- The PEM-encoded certificate chain is stored in a file named
  `CertificateChain.pem`.
- The PEM-encoded, unencrypted private key is stored in a file named
  `PrivateKey.pem`.
- (Optional) You want to tag the server certificate with a key–value pair. For
  example, you might add the tag key `Department` and the tag value
  `Engineering` to help you identify and organize your certificates.

To use the following example command, replace these file names with your own. Replace
`ExampleCertificate` with a name for your uploaded certificate. If
you want to tag the certificate, replace the `ExampleKey` and
`ExampleValue` tag key-value pair with your own values. Type the
command on one continuous line. The following example includes line breaks and extra spaces to
make it easier to read.

```
aws iam upload-server-certificate --server-certificate-name `ExampleCertificate`
                                    --certificate-body file://`Certificate.pem`
                                    --certificate-chain file://`CertificateChain.pem`
                                    --private-key file://`PrivateKey.pem`
                                    --tags '{"Key": "`ExampleKey`", "Value": "`ExampleValue`"}'
```

When the preceding command is successful, it returns metadata about the uploaded
certificate, including its [Amazon Resource Name (ARN)](reference_identifiers.md#identifiers-arns "reference_identifiers.md#identifiers-arns"),
its friendly name, its identifier (ID), its expiration date, tags, and more.

###### Note

If you are uploading a server certificate to use with Amazon CloudFront, you must specify a path
using the `--path` option. The path must begin with `/cloudfront` and
must include a trailing slash (for example, `/cloudfront/test/`).

To use the AWS Tools for Windows PowerShell to upload a certificate, use [Publish-IAMServerCertificate](../../../powershell/latest/reference/Index.md "../../../powershell/latest/reference/Index.md").

## AWS API operations for server

certificates

Use the following commands to view, tag, rename, and delete server certificates.

- Use [GetServerCertificate](../APIReference/API_GetServerCertificate.md "../APIReference/API_GetServerCertificate.md") to retrieve a certificate. This request returns the
  certificate, the certificate chain (if one was uploaded), and metadata about the
  certificate.

###### Note

You cannot download or retrieve a private key from IAM after you upload it.

- Use [Get-IAMServerCertificate](../../../powershell/latest/reference/Index.md "../../../powershell/latest/reference/Index.md") to retrieve a certificate.
- Use [ListServerCertificates](../APIReference/API_ListServerCertificates.md "../APIReference/API_ListServerCertificates.md") to list your uploaded server certificates. The request
  returns a list that contains metadata about each certificate.
- Use [Get-IAMServerCertificates](../../../powershell/latest/reference/Index.md "../../../powershell/latest/reference/Index.md") to list your uploaded server certificates.
- Use [TagServerCertificate](../APIReference/API_TagServerCertificate.md "../APIReference/API_TagServerCertificate.md") to tag an existing server certificate.
- Use [UntagServerCertificate](../APIReference/API_UntagServerCertificate.md "../APIReference/API_UntagServerCertificate.md") to untag a server certificate.
- Use [UpdateServerCertificate](../APIReference/API_UpdateServerCertificate.md "../APIReference/API_UpdateServerCertificate.md") to rename a server certificate or update its
  path.

The following example shows how to do this with the AWS CLI.

To use the following example command, replace the old and new certificate names and
the certificate path, and type the command on one continuous line. The following example
includes line breaks and extra spaces to make it easier to read.

```
aws iam update-server-certificate --server-certificate-name `ExampleCertificate`
                                    --new-server-certificate-name `CloudFrontCertificate`
                                    --new-path `/cloudfront/`
```

To use the AWS Tools for Windows PowerShell to rename a server certificate or update its path, use [Update-IAMServerCertificate](../../../powershell/latest/reference/Index.md "../../../powershell/latest/reference/Index.md").

- Use [DeleteServerCertificate](../APIReference/API_DeleteServerCertificate.md "../APIReference/API_DeleteServerCertificate.md") to delete a server certificate.

To use the AWS Tools for Windows PowerShell to delete a server certificate, use [Remove-IAMServerCertificate](../../../powershell/latest/reference/Index.md "../../../powershell/latest/reference/Index.md").

## Troubleshoot server certificates

Before you can upload a certificate to IAM, you must make sure that the certificate,
private key, and certificate chain are all PEM-encoded. You must also ensure that the private
key is unencrypted. See the following examples.

###### Example PEM-encoded certificate

```
-----BEGIN CERTIFICATE-----
`Base64-encoded certificate`
-----END CERTIFICATE-----
```

###### Example PEM-encoded, unencrypted private key

```
-----BEGIN RSA PRIVATE KEY-----
`Base64-encoded private key`
-----END RSA PRIVATE KEY-----
```

###### Example PEM-encoded certificate chain

A certificate chain contains one or more certificates. You can use a text editor, the
copy command in Windows, or the Linux cat command to concatenate your certificate files into
a chain. When you include multiple certificates, each certificate must certify the preceding
certificate. You accomplish this by concatenating the certificates, including the root CA
certificate last.

The following example contains three certificates, but your certificate chain might
contain more or fewer certificates.

```
-----BEGIN CERTIFICATE-----
`Base64-encoded certificate`
-----END CERTIFICATE-----
-----BEGIN CERTIFICATE-----
`Base64-encoded certificate`
-----END CERTIFICATE-----
-----BEGIN CERTIFICATE-----
`Base64-encoded certificate`
-----END CERTIFICATE-----
```

If these items are not in the right format for uploading to IAM, you can use [OpenSSL](https://openssl.org/ "https://openssl.org/") to convert them to the right format.

**To convert a certificate or certificate chain from DER to PEM**

Use the [OpenSSL **x509** command](https://openssl.org/docs/manmaster/man1/x509.html "https://openssl.org/docs/manmaster/man1/x509.html"), as in the following example. In the
following example command, replace
`Certificate.der` with the name of the
file that contains your DER-encoded certificate. Replace
`Certificate.pem` with the preferred
name of the output file to contain the PEM-encoded certificate.

```
openssl x509 -inform DER -in `Certificate.der` -outform PEM -out `Certificate.pem`
```

 

**To convert a private key from DER to PEM**

Use the [OpenSSL **rsa** command](https://openssl.org/docs/manmaster/man1/rsa.html "https://openssl.org/docs/manmaster/man1/rsa.html"), as in the following example. In the
following example command, replace
`PrivateKey.der` with the name of the
file that contains your DER-encoded private key. Replace
`PrivateKey.pem` with the preferred
name of the output file to contain the PEM-encoded private key.

```
openssl rsa -inform DER -in `PrivateKey.der` -outform PEM -out `PrivateKey.pem`
```

 

**To decrypt an encrypted private key (remove the password or passphrase)**

Use the [OpenSSL **rsa** command](https://openssl.org/docs/manmaster/man1/rsa.html "https://openssl.org/docs/manmaster/man1/rsa.html"), as in the following example. To use the
following example command, replace
`EncryptedPrivateKey.pem` with the
name of the file that contains your encrypted private key. Replace
`PrivateKey.pem` with the preferred
name of the output file to contain the PEM-encoded unencrypted private key.

```
openssl rsa -in `EncryptedPrivateKey.pem` -out `PrivateKey.pem`
```

 

**To convert a certificate bundle from PKCS#12 (PFX) to PEM**

Use the [OpenSSL **pkcs12** command](https://openssl.org/docs/manmaster/man1/pkcs12.html "https://openssl.org/docs/manmaster/man1/pkcs12.html"), as in the following example. In the
following example command, replace
`CertificateBundle.p12` with the name
of the file that contains your PKCS#12-encoded certificate bundle. Replace
`CertificateBundle.pem` with the
preferred name of the output file to contain the PEM-encoded certificate bundle.

```
openssl pkcs12 -in `CertificateBundle.p12` -out `CertificateBundle.pem` -nodes
```

 

**To convert a certificate bundle from PKCS#7 to PEM**

Use the [OpenSSL **pkcs7** command](https://openssl.org/docs/manmaster/man1/pkcs7.html "https://openssl.org/docs/manmaster/man1/pkcs7.html"), as in the following example. In the
following example command, replace
`CertificateBundle.p7b` with the name
of the file that contains your PKCS#7-encoded certificate bundle. Replace
`CertificateBundle.pem` with the
preferred name of the output file to contain the PEM-encoded certificate bundle.

```
openssl pkcs7 -in `CertificateBundle.p7b` -print_certs -out `CertificateBundle.pem`
```
