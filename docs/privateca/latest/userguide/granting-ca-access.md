# Control access to the private CA

Any user with the necessary permissions on a private CA from AWS Private CA can use that
CA to sign other certificates. The CA owner can issue certificates or delegate the
required permissions for issuing certificates to an AWS Identity and Access Management (IAM) user that resides
in the same AWS account. A user that resides in a different AWS account can also
issue certificates if authorized by the CA owner through a [resource-based policy](pca-rbp.md "pca-rbp.md").

Authorized users, whether single-account or cross-account, can use AWS Private CA or
AWS Certificate Manager resources when issuing certificates. Certificates that are issued from the
AWS Private CA [IssueCertificate](../APIReference/API_IssueCertificate.md "../APIReference/API_IssueCertificate.md")
API or [issue-certificate](../../../cli/latest/reference/acm-pca/issue-certificate.md "../../../cli/latest/reference/acm-pca/issue-certificate.md") CLI
command are unmanaged. Such certificates require manual installation on target devices
and manual renewal when they expire. Certificates issued from the ACM console, the
ACM [RequestCertificate](../../../acm/latest/APIReference/API_RequestCertificate.md "../../../acm/latest/APIReference/API_RequestCertificate.md")
API, or the [request-certificate](../../../cli/latest/reference/acm/request-certificate.md "../../../cli/latest/reference/acm/request-certificate.md") CLI command are managed. Such certificates can easily
be installed in services that are integrated with ACM. If the CA administrator permits
it and the issuer's account has a [service-linked
role](../../../acm/latest/userguide/acm-slr.md "../../../acm/latest/userguide/acm-slr.md") in place for ACM, managed certificates are renewed automatically when
they expire.

###### Topics

- [Create single-account permissions for an IAM
  user](assign-permissions.md "assign-permissions.md")
- [Attach a policy for cross-account access](pca-ram.md "pca-ram.md")
