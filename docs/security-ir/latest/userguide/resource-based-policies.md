# Resource-Based Policies

**Resource-based
policies within AWS Security Incident
Response**

Supports resource-based policies: No

Resource-based policies are JSON policy documents that you
attach to a resource. Examples of resource-based policies are
IAM _role trust policies_ and Amazon S3
_bucket policies_. In services that support
resource-based policies, service administrators can use them to
control access to a specific resource. For the resource where
the policy is attached, the policy defines what actions a
specified principal can perform on that resource and under what
conditions. You must
[specify
a principal](../../../IAM/latest/UserGuide/reference_policies_elements_principal.md "../../../IAM/latest/UserGuide/reference_policies_elements_principal.md") in a resource-based policy. Principals can
include accounts, users, roles, federated users, or AWS
services.

For more information, refer to
[Cross
account resource access in IAM](../../../IAM/latest/UserGuide/access_policies-cross-account-resource-access.md "../../../IAM/latest/UserGuide/access_policies-cross-account-resource-access.md") in the _IAM User
Guide_.
