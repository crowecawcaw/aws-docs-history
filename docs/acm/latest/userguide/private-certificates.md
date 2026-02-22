# Private certificates in AWS Certificate Manager

If you have access to an existing private CA created by AWS Private CA, AWS Certificate Manager (ACM)
can request a certificate suited for use in your private key infrastructure (PKI). The
CA may either reside in your account or be shared with you by a different account. For
information about creating a private CA, see [Create a Private Certificate Authority](../../../privateca/latest/userguide/create-CA.md "../../../privateca/latest/userguide/create-CA.md").

Certificates signed by a private CA are not trusted by default, and ACM does not
support any form of validation for
them.
Consequently, an administrator must take action to install them in your organization's
client trust stores.

Private ACM certificates follow the X.509 standard and are subject to the following
restrictions:

- **Names:** You must use DNS-compliant subject
  names. For more information, see [Domain Names](acm-concepts.md#concept-dn "acm-concepts.md#concept-dn").
- **Algorithm:** For encryption, the certificate
  private key algorithm must be either 2048-bit RSA, 256-bit ECDSA, or 384-bit
  ECDSA.

###### Note

The specified signing algorithm family (RSA or ECDSA) must match the
algorithm family of the CA's secret key.

- **Expiration:** Each private certificate is valid for
  13 months (395 days). The end date of the signing CA certificate must exceed the end
  date of the requested certificate, or else the certificate request will
  fail.

###### Note

Private certificates have a longer validity period than public certificates.
Public ACM certificates are valid for 198 days. For more information
about public certificates, see [Request a public certificate in
AWS Certificate Manager](acm-public-certificates.md "acm-public-certificates.md").

- **Renewal:** ACM attempts to renew a private
  certificate automatically after 11 months.
  The private CA used to sign the end-entity certificates is subject to its own
  restrictions:

- The CA must have a status of Active.

###### Note

Unlike publicly trusted certificates, certificates signed by a private CA do not
require validation.

###### Topics

- [Conditions for using AWS Private CA to sign ACM private
  certificates](ca-access.md "ca-access.md")
- [Request a private certificate in
  AWS Certificate Manager](gs-acm-request-private.md "gs-acm-request-private.md")
- [Export an AWS Certificate Manager private certificate](export-private.md "export-private.md")
