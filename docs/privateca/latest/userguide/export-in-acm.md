# Export a private certificate and its secret key

AWS Private CA cannot directly export a private certificate that it has signed and issued.
However, you can use AWS Certificate Manager to export such a certificate along with its encrypted secret
key. The certificate is then completely portable for deployment anywhere in your private
PKI. For more information, see [Exporting a
private certificate](../../../acm/latest/userguide/export-private.md "../../../acm/latest/userguide/export-private.md") in the AWS Certificate Manager User Guide.

As an added benefit, AWS Certificate Manager provides managed renewal for private certificates that
were issued using the ACM console, the `RequestCertificate` action of the
ACM API, or the **request-certificate** command in the ACM section of
the AWS CLI. For more information about renewals, see [Renewing certificates in a private
PKI.](../../../acm/latest/userguide/renew-private-cert.md "../../../acm/latest/userguide/renew-private-cert.md")
