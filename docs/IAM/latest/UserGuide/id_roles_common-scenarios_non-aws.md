# Access for non AWS workloads

An [IAM role](id_roles.md "id_roles.md") is an object in AWS Identity and Access Management (IAM) that is
assigned [permissions](access_policies.md "access_policies.md"). When you [assume that role](id_roles_manage-assume.md "id_roles_manage-assume.md") using an IAM identity or an identity
from outside of AWS, it provides you with temporary security credentials for your role
session. You might have workloads running in your data center or other infrastructure
outside of AWS that must access your AWS resources. Instead of creating, distributing,
and managing long-term access keys, you can use AWS Identity and Access Management Roles Anywhere
(IAM Roles Anywhere) to authenticate your non AWS workloads. IAM Roles Anywhere uses
X.509 certificates from your certificate authority (CA) to authenticate identities and
securely provide access to AWS services with the temporary credentials provided by an
IAM role.

###### To use IAM Roles Anywhere

1. Set up a CA using [AWS Private Certificate Authority](../../../privateca/latest/userguide/PcaWelcome.md "../../../privateca/latest/userguide/PcaWelcome.md") or
   use a CA from your own PKI infrastructure.
2. After you have set up a CA, you create an object in IAM Roles Anywhere called a
   _trust anchor_. This anchor establishes trust between
   IAM Roles Anywhere and your CA for authentication.
3. You can then configure your existing IAM roles, or create new roles that trust
   the IAM Roles Anywhere service.
4. Authenticate your non AWS workloads with IAM Roles Anywhere using
   the trust anchor. AWS grants the non AWS workload temporary credentials to the
   IAM role that has access to your AWS resources.

## Additional resources

The following resources can help you learn more about providing access to non-AWS
workloads.

- For more information about configuring IAM Roles Anywhere,
  see [What is
  AWS Identity and Access Management Roles Anywhere](../../../rolesanywhere/latest/userguide/introduction.md "../../../rolesanywhere/latest/userguide/introduction.md") in the _IAM Roles Anywhere User Guide_.
- To learn how to set up public key infrastructure (PKI) for
  IAM Roles Anywhere, see [IAM Roles Anywhere with an
  external certificate authority](https://aws.amazon.com/blogs/ "https://aws.amazon.com/blogs/") in the _AWS Security
  Blog_.
