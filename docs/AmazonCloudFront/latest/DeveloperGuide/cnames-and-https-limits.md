# Quotas on using SSL/TLS certificates with CloudFront (HTTPS

between viewers and CloudFront only)

Note the following quotas on using SSL/TLS certificates with
CloudFront. These quotas apply only to the SSL/TLS certificates that you provision by
using AWS Certificate Manager (ACM), that you import into ACM, or upload to the IAM
certificate store for HTTPS communication between viewers and CloudFront.

For more information, see [Increase the quotas for
SSL/TLS certificates](increasing-the-limit-for-ssl-tls-certificates.md "increasing-the-limit-for-ssl-tls-certificates.md").

**Maximum number of certificates per CloudFront distribution**

You can associate a maximum of one SSL/TLS certificate with each CloudFront
distribution.

**Maximum number of certificates that you can import into ACM or upload to the IAM
certificate store**

If you obtained your SSL/TLS certificates from a third-party CA, you must store the
certificates in one of the following locations:

- **AWS Certificate Manager** – For the
  current quota on the number of ACM certificates, see [Quotas](../../../acm/latest/userguide/acm-limits.md "../../../acm/latest/userguide/acm-limits.md") in the _AWS Certificate Manager User Guide_. The
  listed quota is a total that includes certificates that you
  provision by using ACM and certificates that you import into
  ACM.
- **IAM certificate store**
  – For the current quota (formerly known as limit) on the
  number of certificates that you can upload to the IAM
  certificate store for an AWS account, see [IAM and STS
  Limits](../../../IAM/latest/UserGuide/reference_iam-limits.md "../../../IAM/latest/UserGuide/reference_iam-limits.md") in the _IAM User Guide_. You
  can request a higher quota in the Service Quotas console.

**Maximum number of certificates per AWS account (dedicated IP addresses only)**

If you want to serve HTTPS requests by using dedicated IP addresses,
note the following:

- By default, CloudFront gives you permission to use two certificates
  with your AWS account, one for everyday use and one for when you
  need to rotate certificates for multiple distributions.
- If you need more than two custom SSL/TLS certificates for your AWS account, you can request a higher quota in the Service Quotas console.

**Use the same certificate for CloudFront distributions that were created by using different
AWS accounts**

If you're using a third-party CA and you want to use the same certificate with multiple
CloudFront distributions that were created by using different AWS accounts,
you must import the certificate into ACM or upload it to the IAM
certificate store once for each AWS account.

If you're using certificates provided by ACM, you can't configure
CloudFront to use certificates that were created by a different AWS
account.

**Use the same certificate for CloudFront and for other AWS services**

If you bought a certificate from a trusted certificate authority such
as Comodo, DigiCert, or Symantec, you can use the same certificate for
CloudFront and for other AWS services. If you're importing the certificate
into ACM, you need to import it only once to use it for multiple AWS
services.

If you're using certificates provided by ACM, the certificates are
stored in ACM.

**Use the same certificate for multiple CloudFront distributions**

You can use the same certificate for any or all of the CloudFront
distributions that you're using to serve HTTPS requests. Note the
following:

- You can use the same certificate both for serving requests
  using dedicated IP addresses and for serving requests using SNI.
- You can associate only one certificate with each
  distribution.
- Each distribution must include one or more alternate domain names that also appear in
  the **Common Name** field or the
  **Subject Alternative Names** field in the
  certificate.
- If you're serving HTTPS requests using dedicated IP addresses
  and you created all of your distributions by using the same AWS
  account, you can significantly reduce your cost by using the
  same certificate for all distributions. CloudFront charges for each
  certificate, not for each distribution.

For example, suppose you create three distributions by using
the same AWS account, and you use the same certificate for all
three distributions. You would be charged only one fee for using
dedicated IP addresses.

However, if you're serving HTTPS requests using dedicated IP addresses and using the
same certificate to create CloudFront distributions in different AWS
accounts, each account is charged the fee for using dedicated IP
addresses. For example, if you create three distributions by
using three different AWS accounts and you use the same
certificate for all three distributions, each account is charged
the full fee for using dedicated IP addresses.
