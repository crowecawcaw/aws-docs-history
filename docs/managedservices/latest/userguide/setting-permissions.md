# Setting permissions in AMS with IAM roles and profiles

AMS uses AWS Identity and Access Management (IAM) to manage users, security credentials such as access keys, and permissions that control which AWS
resources users and applications can access.
AMS provides a default IAM user role and a default Amazon EC2 instance profile (which includes a statement allowing the resource access
to the default IAM user role).

## Requesting a new IAM user role or instance profile

AMS uses an IAM role to set user permissions through your federation service and an IAM instance profile as a
container for that IAM role.

You can request a custom IAM role with the
Deployment | Advanced stack components | Identity and Access Management (IAM) | Create entity or policy (managed automation) change type (ct-3dpd8mdd9jn1r),
or an IAM instance profile with the
Management | Applications | IAM instance profile | Create Management | Applications | IAM instance profile | Create (managed automation) change type (ct-0ixp4ch2tiu04).
See the descriptions of each in this section.

###### Note

AMS has an IAM policy, `customer_deny_policy` that blocks out dangerous
namespaces and actions. This policy is attached to all AMS customer roles by
default and is rarely a problem for users. Your IAM user and role requests don't
include this policy, but automatic inclusion of the `customer_deny_policy` in requests for IAM roles helps AMS
deploy new IAM instance profiles more quickly. You can request the exclusion of
the `customer_deny_policy` policy. However, this request will go
through a weighty security review and is likely to be declined due to security reasons.
