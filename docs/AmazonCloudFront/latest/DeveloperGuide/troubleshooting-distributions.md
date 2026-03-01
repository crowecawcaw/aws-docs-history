# Troubleshooting distribution issues

Use the information here to help you diagnose and fix certificate errors,
access-denied issues, or other common issues that you might encounter when setting up
your website or application with Amazon CloudFront distributions.

###### Topics

- [CloudFront returns an Access Denied error](#access-denied "#access-denied")
- [CloudFront returns an InvalidViewerCertificate error when I try to add an alternate domain name](#troubleshooting-distributions-certificates "#troubleshooting-distributions-certificates")
- [CloudFront returns an incorrectly configured DNS record error when I try to add a new CNAME](#troubleshoot-incorrectly-configured-DNS-record-error "#troubleshoot-incorrectly-configured-DNS-record-error")
- [I can't view the files in my distribution](#troubleshooting-web-distribution "#troubleshooting-web-distribution")
- [Error message: Certificate: <certificate-id> is being used by CloudFront](#troubleshooting-certificate-error "#troubleshooting-certificate-error")

## CloudFront returns an Access Denied error

If you're using an Amazon S3 bucket as the origin for your CloudFront distribution, you might
see an Access Denied (403) error message in the following examples.

###### Contents

- [You specified a missing object from the Amazon S3 origin](troubleshooting-distributions.md#missing-object-in-s3-bucket "troubleshooting-distributions.md#missing-object-in-s3-bucket")
- [Your Amazon S3 origin is missing IAM permissions](troubleshooting-distributions.md#access-denied-origin-missing-iam-permissions "troubleshooting-distributions.md#access-denied-origin-missing-iam-permissions")
- [You're using invalid credentials or don't have sufficient permissions](troubleshooting-distributions.md#access-denied-missing-iam-permissions "troubleshooting-distributions.md#access-denied-missing-iam-permissions")

### You specified a missing object from the Amazon S3 origin

Verify that the requested object in your bucket exists. Object names are case
sensitive. Entering an invalid object name can return an access denied error
code.

For example, if you follow the [CloudFront tutorial](GettingStarted.md "GettingStarted.md") to
create a basic distribution, you create an Amazon S3 bucket as the origin and upload
an example `index.html` file.

In your web browser, if you enter
`https://d111111abcdef8.cloudfront.net/`INDEX`.HTML`
instead of
`https://d111111abcdef8.cloudfront.net/`index`.html`,
you might see a similar message because the `index.html` file
in the URL path is case sensitive.

```
<Error>
<Code>AccessDenied</Code>
<Message>Access Denied</Message>
<RequestId>22Q367AHT7Y1ABCD</RequestId>
<HostId>
ABCDE/Vg+7PSNa/d/IfFQ8Fb92TGQ0KH0ZwG5iEKbc6+e06DdMS1ZW+ryB9GFRIVtS66rSSy6So=
</HostId>
</Error>

```

### Your Amazon S3 origin is missing IAM permissions

Verify that you've selected the correct Amazon S3 bucket as the origin domain and
name. The origin (Amazon S3) must have the correct permissions.

If you don’t specify the correct permissions, an `AccessDenied` message can
appear for your viewers.

When you distribute content from Amazon S3 and you’re also using AWS Key Management Service (AWS KMS)
service-side encryption (SSE-KMS), there are additional IAM permissions that
you need to specify for the KMS key and Amazon S3 bucket. Your CloudFront distribution
needs these permissions to use the KMS key, which is used for encryption of
the origin Amazon S3 bucket..

The configurations to the Amazon S3 bucket policy allow the CloudFront distribution to
retrieve the encrypted objects for content delivery.

###### To verify your Amazon S3 bucket and KMS key permissions

1. Verify that the KMS key that you’re using is the same key that your
   Amazon S3 bucket uses for default encryption. For more information, see
   [Specifying server-side encryption with AWS KMS
   (SSE-KMS)](../../../AmazonS3/latest/userguide/specifying-kms-encryption.md "../../../AmazonS3/latest/userguide/specifying-kms-encryption.md") in the _Amazon Simple Storage Service User Guide_.
2. Verify that the objects in the bucket are encrypted with the same
   KMS key. You can select any object from the Amazon S3 bucket and check the
   server-side encryption settings to verify the KMS key ARN.
3. Edit the Amazon S3 bucket policy to grant CloudFront permission to call the
   `GetObject` API operation from the Amazon S3 bucket. For an
   example Amazon S3 bucket policy that uses origin access control, see [Grant CloudFront permission to access the S3 bucket](private-content-restricting-access-to-s3.md#oac-permission-to-access-s3 "private-content-restricting-access-to-s3.md#oac-permission-to-access-s3").
4. Edit the KMS key policy to grant CloudFront permission to perform the
   actions to `Encrypt`, `Decrypt`, and
   `GenerateDataKey*`. To align with least privilege
   permission, specify a `Condition` element so that only the
   specified CloudFront distribution can perform the listed actions. You can
   customize the policy for your existing AWS KMS policy. For an example
   KMS key policy, see the [SSE-KMS](private-content-restricting-access-to-s3.md#oac-permissions-sse-kms "private-content-restricting-access-to-s3.md#oac-permissions-sse-kms").

If you’re using origin access identity (OAI) instead of OAC, the permissions
to the Amazon S3 bucket are slightly different because you grant permission to an
identity instead of the AWS service. For more information, see [Give an origin access identity permission to read files in the Amazon S3 bucket](private-content-restricting-access-to-s3.md#private-content-granting-permissions-to-oai "private-content-restricting-access-to-s3.md#private-content-granting-permissions-to-oai").

If you still can't view your files in your distribution, see [I can't view the files in my distribution](#troubleshooting-web-distribution "#troubleshooting-web-distribution").

### You're using invalid credentials or don't have sufficient permissions

An Access Denied error message can appear if you’re using incorrect or expired
AWS SCT credentials (access key and secret key) or your IAM role or user is
missing a required permission to perform an action on a CloudFront resource. For more
information about access denied error messages, see [Troubleshooting access denied error messages](../../../IAM/latest/UserGuide/troubleshoot_access-denied.md "../../../IAM/latest/UserGuide/troubleshoot_access-denied.md") in
the _IAM User Guide_.

For information about how IAM works with CloudFront, see [Identity and Access Management for Amazon CloudFront](security-iam.md "security-iam.md").

## CloudFront returns an InvalidViewerCertificate error when I try to add an alternate domain name

If CloudFront returns an `InvalidViewerCertificate` error when you try to add
an alternate domain name (CNAME) to your distribution, review the following
information to help troubleshoot the problem. This error can indicate that one of
the following issues must be resolved before you can successfully add the alternate
domain name.

The following errors are listed in the order in which CloudFront checks for
authorization to add an alternate domain name. This can help you troubleshoot issues
because based on the error that CloudFront returns, you can tell which verification checks
have completed successfully.

**There's no certificate attached to your distribution.**

To add an alternate domain name (CNAME), you must attach a trusted,
valid certificate to your distribution. Please review the requirements,
obtain a valid certificate that meets them, attach it to your
distribution, and then try again. For more information, see [Requirements for using alternate domain names](CNAMEs.md#alternate-domain-names-requirements "CNAMEs.md#alternate-domain-names-requirements").

**There are too many certificates in the certificate chain for the
certificate that you've attached.**

You can only have up to five certificates in a certificate chain.
Reduce the number of certificates in the chain, and then try
again.

**The certificate chain includes one or more certificates that aren't valid
for the current date.**

The certificate chain for a certificate that you have added has one or
more certificates that aren't valid, either because a certificate isn't
valid yet or a certificate has expired. Check the **Not Valid
Before** and **Not Valid After** fields in
the certificates in your certificate chain to make sure that all of the
certificates are valid based on the dates that you've listed.

**The certificate that you've attached isn't signed by a trusted Certificate
Authority (CA).**

The certificate that you attach to CloudFront to verify an alternate domain
name cannot be a self-signed certificate. It must be signed by a trusted
CA. For more information, see [Requirements for using alternate domain names](CNAMEs.md#alternate-domain-names-requirements "CNAMEs.md#alternate-domain-names-requirements").

**The certificate that you've attached isn't formatted correctly**

The domain name and IP address format that are included in the
certificate, and the format of the certificate itself, must follow the
standard for certificates.

**There was a CloudFront internal error.**

CloudFront was blocked by an internal issue and couldn't make validation
checks for certificates. In this scenario, CloudFront returns an HTTP 500
status code and indicates that there is an internal CloudFront problem with
attaching the certificate. Wait a few minutes, and then try again to add
the alternate domain name with the certificate.

**The certificate that you've attached doesn't cover the alternate domain
name that you're trying to add.**

For each alternate domain name that you add, CloudFront requires that you
attach a valid SSL/TLS certificate from a trusted Certificate Authority
(CA) that covers the domain name, to validate your authorization to use
it. Please update your certificate to include a domain name that covers
the CNAME that you're trying to add. For more information and examples
of using domain names with wildcards, see [Requirements for using alternate domain names](CNAMEs.md#alternate-domain-names-requirements "CNAMEs.md#alternate-domain-names-requirements").

## CloudFront returns an incorrectly configured DNS record error when I try to add a new CNAME

When you have an existing wildcard DNS entry pointing to a CloudFront distribution, if
you try to add a new CNAME with a more specific name, you might encounter the
following error:

```
One or more aliases specified for the distribution includes an incorrectly configured DNS record that points to another CloudFront distribution. You must update the DNS record to correct the problem.
```

This error occurs because CloudFront queries the DNS against the CNAME and the wildcard
DNS entry resolves to another distribution.

To resolve this, first create another distribution, then create a DNS entry
pointing to the new distribution. Finally, add the more specific CNAME. For more
information on how to add CNAMEs, see [Add an alternate domain name](CreatingCNAME.md "CreatingCNAME.md").

## I can't view the files in my distribution

If you can't view the files in your CloudFront distribution, see the following topics
for some common solutions.

### Did you sign up for both CloudFront and Amazon S3?

To use Amazon CloudFront with an Amazon S3 origin, you must sign up for both CloudFront and Amazon S3,
separately. For more information about signing up for CloudFront and Amazon S3, see [Set up your AWS account](setting-up-cloudfront.md "setting-up-cloudfront.md").

### Are your Amazon S3 bucket and object permissions set correctly?

If you're using CloudFront with an Amazon S3 origin, the original versions of your
content are stored in an S3 bucket. To serve the content to your viewers, we
recommend that you use CloudFront Origin Access Control (OAC) to secure Amazon S3 bucket
access. This means your S3 bucket is reachable only through CloudFront. OAC controls
viewer access and secure delivery via CloudFront. For more information about OAC, see
[Restrict access to an Amazon S3 origin](private-content-restricting-access-to-s3.md "private-content-restricting-access-to-s3.md").

For more information about managing your bucket access, see [Blocking public access to your Amazon S3
storage](../../../AmazonS3/latest/userguide/access-control-block-public-access.md "../../../AmazonS3/latest/userguide/access-control-block-public-access.md") in the _Amazon S3 User Guide_.

Object properties and bucket properties are independent. You must explicitly
grant privileges to each object in Amazon S3. Objects do not inherit properties from
buckets, and object properties must be set independently of the bucket.

### Is your alternate domain name (CNAME) correctly configured?

If you already have an existing CNAME record for your domain name, update that
record or replace it with a new one that points to your distribution's domain
name.

Also, make sure that your CNAME record points to your distribution's domain
name, not your Amazon S3 bucket. You can confirm that the CNAME record in your DNS
system points to your distribution's domain name. To do so, use a DNS tool like
**dig**.

The following example shows a dig request for a domain name called
`images.example.com` and the relevant part of the response. Under
`ANSWER SECTION`, see the line that contains `CNAME`.
The CNAME record for your domain name is set up correctly if the value on the
right side of CNAME is your CloudFront distribution's domain name. If it's your Amazon S3
origin server bucket or some other domain name, then the CNAME record is set up
incorrectly.

```
[prompt]> dig images.example.com

; <<> DiG 9.3.3rc2 <<> images.example.com
;; global options:	printcmd
;; Got answer:
;; ->>HEADER<<- opcode: QUERY, status: NOERROR, id: 15917
;; flags: qr rd ra; QUERY: 1, ANSWER: 9, AUTHORITY: 2, ADDITIONAL: 0
;; QUESTION SECTION:
;images.example.com.		 IN		A
;; ANSWER SECTION:
images.example.com. 10800 IN	CNAME	d111111abcdef8.cloudfront.net.
...
...
```

For more information about CNAMEs, see [Use custom URLs by adding alternate domain names (CNAMEs)](CNAMEs.md "CNAMEs.md").

### Are you referencing the correct URL for your CloudFront distribution?

Make sure that the URL that you're referencing uses the domain name (or CNAME)
of your CloudFront distribution, not your Amazon S3 bucket or custom origin.

### Do you need help troubleshooting a custom origin?

If you need AWS to help you troubleshoot a custom origin, we probably will
need to inspect the `X-Amz-Cf-Id` header entries from your requests.
If you are not already logging these entries, you might want to consider it for
the future. For more information, see [Use Amazon EC2 (or another custom origin)](DownloadDistS3AndCustomOrigins.md#concept_CustomOrigin "DownloadDistS3AndCustomOrigins.md#concept_CustomOrigin").
For further help, see the [AWS
Support Center](https://console.aws.amazon.com/support/home?#/ "https://console.aws.amazon.com/support/home?#/").

## Error message: Certificate: <certificate-id> is being used by CloudFront

**Problem:** You're trying to delete an SSL/TLS
certificate from the IAM certificate store, and you're getting the message
"Certificate: <certificate-id> is being used by CloudFront."

**Solution:** Every CloudFront distribution must be
associated either with the default CloudFront certificate or with a custom SSL/TLS
certificate. Before you can delete an SSL/TLS certificate, you must either rotate
the certificate (replace the current custom SSL/TLS certificate with another custom
SSL/TLS certificate) or revert from using a custom SSL/TLS certificate to using the
default CloudFront certificate. To fix that, complete the steps in one of the following
procedures:

- [Rotate SSL/TLS certificates](cnames-and-https-rotate-certificates.md "cnames-and-https-rotate-certificates.md")
- [Revert from a custom SSL/TLS certificate to the default CloudFront certificate](cnames-and-https-revert-to-cf-certificate.md "cnames-and-https-revert-to-cf-certificate.md")
