# AWS Certificate Manager public certificates

After you request a public certificate you must validate domain ownership, as described in
[Validate domain ownership for AWS Certificate Manager public
certificates](domain-ownership-validation.md "domain-ownership-validation.md").

Public ACM certificates follow the X.509 standard and are subject to the following
restrictions:

- **Names:** You must use DNS-compliant subject names.
  For more information, see [Domain Names](acm-concepts.md#concept-dn "acm-concepts.md#concept-dn").
- **Algorithm:** For encryption, the certificate
  private key algorithm must be either 2048-bit RSA, 256-bit ECDSA, or 384-bit
  ECDSA.
- **Expiration:** Each certificate is valid for
  198 days.
- **Renewal:** ACM attempts to renew a public
  certificate automatically 45 days before expiration.

###### Note

Public ACM certificates can be installed on Amazon EC2 instances that are connected to a
[Nitro Enclave](acm-services.md#acm-nitro-enclave "acm-services.md#acm-nitro-enclave"). You can also [export a public certificate](export-public-certificate.md "export-public-certificate.md")
to use on any Amazon EC2 instance. For information about
setting up a standalone web server on an Amazon EC2 instance not connected to a Nitro Enclave, see [Tutorial: Install a LAMP web server
on Amazon Linux 2](../../../AWSEC2/latest/UserGuide/ec2-lamp-amazon-linux-2.md "../../../AWSEC2/latest/UserGuide/ec2-lamp-amazon-linux-2.md") or [Tutorial:
Install a LAMP web server with the Amazon Linux AMI](../../../AWSEC2/latest/UserGuide/install-LAMP.md "../../../AWSEC2/latest/UserGuide/install-LAMP.md").

Administrators can use ACM [Conditional Key
Policies](acm-conditions.md "acm-conditions.md") to control how end users issue new certificates. These Conditional keys
allow restrictions to be placed on domains, validation methods, and other attributes related
to a certificate request. If you encounter problems when requesting a certificate, see [Troubleshoot certificate requests](troubleshooting-cert-requests.md "troubleshooting-cert-requests.md").

To request a certificate for a private PKI using AWS Private CA, see [Request a private certificate in
AWS Certificate Manager](gs-acm-request-private.md "gs-acm-request-private.md").

###### Topics

- [AWS Certificate Manager public certificate
  characteristics and limitations](acm-certificate-characteristics.md "acm-certificate-characteristics.md")
- [Request a public certificate in
  AWS Certificate Manager](acm-public-certificates.md "acm-public-certificates.md")
- [AWS Certificate Manager exportable public certificates](acm-exportable-certificates.md "acm-exportable-certificates.md")
- [Validate domain ownership for AWS Certificate Manager public
  certificates](domain-ownership-validation.md "domain-ownership-validation.md")
