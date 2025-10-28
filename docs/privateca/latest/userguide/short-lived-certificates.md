# Understand AWS Private CA CA modes

AWS Private CA supports the creation of a certificate authority (CA) in either of two
modes. The modes, general-purpose and short-lived certificate, affect the allowed
validity period of the certificates issued by the CA.

###### Note

AWS Private CA does not perform validity checks on root CA certificates.

## General-purpose (default)

This mode permits the CA to issue certificates with any validity period. Most
applications use certificates of this type. Typically, the CA also specifies a
revocation mechanism.

## Short-lived certificate

This mode defines a CA that exclusively issues certificates with a maximum
validity period of seven days. These short-lived certificates expire so quickly that
they can be deployed without a revocation mechanism in place. For some applications,
it makes more sense to frequently deploy short-lived certificates than to incur the
network and processing overhead of revocation.

Short-lived certificates must be the last CA in the certificate hierarchy. There
is significant overhead because the private CA must be renewed every seven
days.

CAs with short-lived certificate mode cost less than general-purpose CAs. For more
information, see [AWS Private Certificate Authority
Pricing](https://aws.amazon.com/private-ca/pricing/ "https://aws.amazon.com/private-ca/pricing/").

To create a CA that issues short-lived certificates, set the
`UsageMode` parameter to short-lived certificate using the [create a CA](create-CA.md "create-CA.md") procedure for creating a CA.

###### Note

AWS Certificate Manager cannot issue certificates signed by a private CA with short-lived
mode.

Use of short-lived certificates is supported by the following AWS
services:

- [Amazon AppStream](../../../appstream/latest/developerguide.md "../../../appstream/latest/developerguide.md")
- [Amazon WorkSpaces](../../../workspaces/latest/adminguide.md "../../../workspaces/latest/adminguide.md")
