# Security best practices for Cross-account access

to private CAs

An AWS Private CA administrator can share a CA with principals (users, roles, etc.) in
another AWS account. When a share has been received and accepted, the principal can
use the CA to issue end-entity certificates using AWS Private CA or AWS Certificate Manager resources. The
principal can use the CA to issue subordinate CA certificates using AWS Private CA.

###### Important

Charges associated with a certificate issued in a cross-account scenario are
billed to the AWS account that issues the certificate.

To share access to a CA, AWS Private CA administrators can choose either of the following
methods:

- Use AWS Resource Access Manager (RAM) to share the CA as a resource with a principal in another
  account or with AWS Organizations. RAM is a standard method for sharing AWS resources
  across accounts. For more information about RAM, see the [AWS RAM User Guide](../../../ram/latest/userguide.md "../../../ram/latest/userguide.md"). For more information about
  AWS Organizations, see the [AWS Organizations User Guide](../../../organizations/latest/userguide.md "../../../organizations/latest/userguide.md").
- Use the AWS Private CA API or CLI to attach a resource-based policy to a CA,
  thereby granting access to a principal in another account. For more information,
  see [Resource-based policies](pca-rbp.md "pca-rbp.md").
  The [Control access to the private CA](granting-ca-access.md "granting-ca-access.md") section of
  this guide provides workflows for granting access to CAs in both single-account and
  cross-account scenarios.
