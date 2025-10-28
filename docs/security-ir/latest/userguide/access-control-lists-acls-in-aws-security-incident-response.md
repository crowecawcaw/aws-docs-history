# Access control lists (ACLs) in

AWS Security Incident Response

**Supports ACLs:** No

Access control lists (ACLs) control which principals (account
members, users, or roles) have permissions to access a
resource. ACLs are similar to resource-based policies,
although they do not use the JSON policy document format.

**Attribute-based
access control (ABAC) with AWS Security Incident
Response**

**Supports ABAC (tags in
policies):** Yes

Attribute-based access control (ABAC) is an authorization
strategy that defines permissions based on attributes. In AWS,
these attributes are called _tags_. You can
attach tags to IAM entities (users or roles) and to many AWS
resources. Tagging entities and resources is the first step of
ABAC. Then you design ABAC policies to allow operations when
the principal's tag matches the tag on the resource that they
are trying to access. ABAC is helpful in environments that are
growing rapidly and helps with situations where policy
management becomes cumbersome.

To control access based on tags, you provide tag information
in the
[condition
element](../../../IAM/latest/UserGuide/reference_policies_elements_condition.md "../../../IAM/latest/UserGuide/reference_policies_elements_condition.md") of a policy using the AWS:ResourceTag/key-name,
AWS:RequestTag/key-name, or AWS:TagKeys condition keys. If a
service supports all three condition keys for every resource
type, then the value is **Yes**
for the service. If a service supports all three condition
keys for only some resource types, then the value is
**Partial**. For more
information about ABAC, see
[What
is ABAC?](../../../IAM/latest/UserGuide/introduction_attribute-based-access-control.md "../../../IAM/latest/UserGuide/introduction_attribute-based-access-control.md") in the _IAM User Guide_. To
view a tutorial with steps for setting up ABAC, see
[Use
attribute-based access control (ABAC)](../../../IAM/latest/UserGuide/tutorial_attribute-based-access-control.md "../../../IAM/latest/UserGuide/tutorial_attribute-based-access-control.md") in the
_IAM User Guide_.

**Temporary
credentials with Amazon AWS Security Incident
Response**

**Supports temporary credentials:** Yes

AWS services don't work when you sign in using temporary credentials. For additional information, including
which AWS services work with temporary credentials, see [AWS services that work with IAM](../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md "../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md") in the _IAM User Guide_. You are using temporary credentials if you sign in to the AWS Management
Console using any method except a user name and password. For example, when you access AWS using your company's single sign-on (SSO) link, that process automatically
creates temporary credentials. You also automatically create temporary credentials when you sign in to the console as a user and then switch roles. For more information
about switching roles, see [Switching to a role (console)](../../../IAM/latest/UserGuide/id_roles_use_switch-role-console.md "../../../IAM/latest/UserGuide/id_roles_use_switch-role-console.md")
in the _IAM User Guide_.

You can manually create temporary credentials using the AWS
CLI or AWS API. You can then use those temporary credentials
to access AWS. AWS recommends that you dynamically generate
temporary credentials instead of using long-term access keys.
For more information, see
[Temporary
security credentials in IAM](../../../IAM/latest/UserGuide/id_credentials_temp.md "../../../IAM/latest/UserGuide/id_credentials_temp.md").

**Forward
access sessions for AWS Security Incident
Response**

**Supports forward access sessions
(FAS):** Yes

When you use an IAM user or role to perform actions in AWS,
you are considered a principal. When you use some services,
you might perform an action that then initiates another action
in a different service. FAS uses the permissions of the
principal calling an AWS service, combined with the requesting
AWS service to make requests to downstream services. FAS
requests are only made when a service receives a request that
requires interactions with other AWS services or resources to
complete. In this case, you must have permissions to perform
both actions. For policy details when making FAS requests, see
[Forward
access sessions](../../../IAM/latest/UserGuide/access_forward_access_sessions.md "../../../IAM/latest/UserGuide/access_forward_access_sessions.md").
