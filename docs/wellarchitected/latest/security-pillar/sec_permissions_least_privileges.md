# SEC03-BP02 Grant least privilege access

Grant only the access that users require to perform specific actions
on specific resources under specific conditions. Use group and
identity attributes to dynamically set permissions at scale, rather
than defining permissions for individual users. For example, you can
allow a group of developers access to manage only resources for
their project. This way, if a developer leaves the project, their
access is automatically revoked without changing the underlying
access policies.

**Desired outcome:** Users have only
the minimum permissions required for their specific job functions.
You use separate AWS accounts to isolate developers from production
environments. When developers need to access production environments
for specific tasks, they are granted limited and controlled access
only for the duration of those tasks. Their production access is
immediately revoked after they complete the necessary work. You
conduct regular reviews of permissions and promptly revoke them when
no longer needed, such as when a user changes roles or leaves the
organization. You restrict administrator privileges to a small,
trusted group to reduce risk exposure. You give machine or system
accounts only the minimum permissions required to perform their
intended tasks.

**Common anti-patterns:**

- By default, you grant users administrator permissions.
- You use the root user account for daily activities.
- You create overly permissive policies without proper scoping.
- Your permissions reviews are infrequent, which leads to
  permissions creep.
- You rely solely on attribute-based access control for
  environment isolation or permissions management.

**Level of risk exposed if this best practice is not established:**
High

## Implementation guidance

The principle of
[least
privilege](../../../IAM/latest/UserGuide/best-practices.md#grant-least-privilege "../../../IAM/latest/UserGuide/best-practices.md#grant-least-privilege") states that identities should only be permitted
to perform the smallest set of actions necessary to fulfill a
specific task. This balances usability, efficiency, and security.
Operating under this principle helps limit unintended access and
helps track who has access to what resources. IAM users and roles
have no permissions by default. The root user has full access by
default and should be tightly controlled, monitored, and used only
for
[tasks
that require root access](../../../accounts/latest/reference/root-user-tasks.md "../../../accounts/latest/reference/root-user-tasks.md").

IAM policies are used to explicitly grant permissions to IAM roles
or specific resources. For example, identity-based policies can be
attached to IAM groups, while S3 buckets can be controlled by
resource-based policies.

When you create an IAM policy, you can specify the service
actions, resources, and conditions that must be true for AWS to
allow or deny access. AWS supports a variety of conditions to help
you scope down access. For example, by using the
PrincipalOrgID
[condition
key](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md"), you can deny actions if the requestor isn't a part of
your AWS Organization.

You can also control requests that AWS services make on your
behalf, such as AWS CloudFormation creating an AWS Lambda
function, using the CalledVia condition key.
You can layer different policy types to establish defense-in-depth
and limit the overall permissions of your users. You can also
restrict what permissions can be granted and under what
conditions. For example, you can allow your workload teams to
create their own IAM policies for systems they build, but only if
they apply a
[Permission
Boundary](../../../IAM/latest/UserGuide/access_policies_boundaries.md "../../../IAM/latest/UserGuide/access_policies_boundaries.md") to limit the maximum permissions they can grant.

### Implementation steps

- **Implement least privilege
  policies**: Assign access policies with least
  privilege to IAM groups and roles to reflect the user's role
  or function that you have defined.
- **Isolate development and production
  environments through separate AWS accounts**: Use
  separate AWS accounts for development and production
  environments, and control access between them using
  [service
  control policies](../../../organizations/latest/userguide/orgs_manage_policies_scps.md "../../../organizations/latest/userguide/orgs_manage_policies_scps.md"), resource policies, and identity
  policies.
- **Base policies on API
  usage**: One way to determine the needed
  permissions is to review AWS CloudTrail logs. You can use
  this review to create permissions tailored to the actions
  that the user actually performs within AWS.
  [IAM Access Analyzer](../../../IAM/latest/UserGuide/what-is-access-analyzer.md "../../../IAM/latest/UserGuide/what-is-access-analyzer.md") can
  [automatically
  generate](../../../IAM/latest/UserGuide/access-analyzer-policy-generation.md "../../../IAM/latest/UserGuide/access-analyzer-policy-generation.md") an IAM policy based on access activity. You
  can use IAM Access Advisor at the organization or account
  level to
  [track
  the last accessed information for a particular
  policy](../../../IAM/latest/UserGuide/access_policies_access-advisor.md "../../../IAM/latest/UserGuide/access_policies_access-advisor.md").
- **Consider using
  [AWS managed policies for job functions](../../../IAM/latest/UserGuide/access_policies_job-functions.md "../../../IAM/latest/UserGuide/access_policies_job-functions.md")**: When
  you begin to create fine-grained permissions policies, it
  can be helpful to use AWS managed policies for common job
  roles, such as billing, database administrators, and data
  scientists. These policies can help narrow the access that
  users have while you determine how to implement the least
  privilege policies.
- **Remove unnecessary
  permissions:** Detect and remove unused IAM
  entities, credentials, and permissions to achieve the
  principle of least privilege. You can use
  [IAM Access Analyzer](../../../IAM/latest/UserGuide/access-analyzer-findings.md "../../../IAM/latest/UserGuide/access-analyzer-findings.md") to identify external and unused
  access, and
  [IAM Access Analyzer policy generation](../../../IAM/latest/UserGuide/access-analyzer-policy-generation.md "../../../IAM/latest/UserGuide/access-analyzer-policy-generation.md") can help fine-tune
  permissions policies.
- **Ensure that users have limited
  access to production environments:** Users should
  only have access to production environments with a valid use
  case. After the user performs the specific tasks that
  required production access, access should be revoked.
  Limiting access to production environments helps prevent
  unintended production-impacting events and lowers the scope
  of impact of unintended access.
- **Consider permissions
  boundaries:** A
  [permissions
  boundary](../../../IAM/latest/UserGuide/access_policies_boundaries.md "../../../IAM/latest/UserGuide/access_policies_boundaries.md") is a feature for using a managed policy that
  sets the maximum permissions that an identity-based policy
  can grant to an IAM entity. An entity's permissions boundary
  allows it to perform only the actions that are allowed by
  both its identity-based policies and its permissions
  boundaries.
- **Refine access using attribute-based
  access control and resource tags**
  [Attribute-based
  access control (ABAC)](../../../IAM/latest/UserGuide/introduction_attribute-based-access-control.md "../../../IAM/latest/UserGuide/introduction_attribute-based-access-control.md") using resource tags can be used
  to refine permissions when supported. You can use an ABAC
  model that compares principal tags to resource tags to
  refine access based on custom dimensions you define. This
  approach can simplify and reduce the number of permission
  policies in your organization.

      + It is recommended that ABAC only be used for access
       control when both the principals and resources are owned
       by your AWS Organization. External parties may use the
       same tag names and values as your organization for their
       own principals and resources. If you rely solely on
       these name-value pairs for granting access to external
       party principals or resources, you may provide
       unintended permissions.

- **Use service control policies for AWS Organizations:**
  [Service
  control policies](../../../organizations/latest/userguide/orgs_manage_policies_scps.md "../../../organizations/latest/userguide/orgs_manage_policies_scps.md") centrally control the maximum
  available permissions for member accounts in your
  organization. Importantly, you can use service control
  policies to restrict root user permissions in member
  accounts. Also consider using AWS Control Tower, which
  provides prescriptive managed controls that enrich AWS Organizations. You can also define your own controls within
  Control Tower.
- **Establish a user lifecycle policy
  for your organization:** User lifecycle policies
  define tasks to perform when users are onboarded onto AWS,
  change job role or scope, or no longer need access to AWS.
  Perform permission reviews during each step of a user's
  lifecycle to verify that permissions are properly
  restrictive and to avoid permissions creep.
- **Establish a regular schedule to
  review permissions and remove any unneeded
  permissions:** You should regularly review user
  access to verify that users do not have overly permissive
  access.
  [AWS Config](../../../config/latest/developerguide/WhatIsConfig.md "../../../config/latest/developerguide/WhatIsConfig.md") and IAM Access Analyzer can help during user
  permissions audits.
- **Establish a job role
  matrix:** A job role matrix visualizes the various
  roles and access levels required within your AWS footprint.
  With a job role matrix, you can define and separate
  permissions based on user responsibilities within your
  organization. Use groups instead of applying permissions
  directly to individual users or roles.

## Resources

**Related documents:**

- [Grant
  least privilege](../../../IAM/latest/UserGuide/best-practices.md#grant-least-privilege "../../../IAM/latest/UserGuide/best-practices.md#grant-least-privilege")
- [Permissions
  boundaries for IAM entities](../../../IAM/latest/UserGuide/access_policies_boundaries.md "../../../IAM/latest/UserGuide/access_policies_boundaries.md")
- [Techniques
  for writing least privilege IAM policies](https://aws.amazon.com/blogs/security/techniques-for-writing-least-privilege-iam-policies/ "https://aws.amazon.com/blogs/security/techniques-for-writing-least-privilege-iam-policies/")
- [IAM Access Analyzer makes it easier to implement least privilege
  permissions by generating IAM policies based on access
  activity](https://aws.amazon.com/blogs/security/iam-access-analyzer-makes-it-easier-to-implement-least-privilege-permissions-by-generating-iam-policies-based-on-access-activity/ "https://aws.amazon.com/blogs/security/iam-access-analyzer-makes-it-easier-to-implement-least-privilege-permissions-by-generating-iam-policies-based-on-access-activity/")
- [Delegate
  permission management to developers by using IAM permissions
  boundaries](https://aws.amazon.com/blogs/security/delegate-permission-management-to-developers-using-iam-permissions-boundaries/ "https://aws.amazon.com/blogs/security/delegate-permission-management-to-developers-using-iam-permissions-boundaries/")
- [Refining
  Permissions using last accessed information](../../../IAM/latest/UserGuide/access_policies_access-advisor.md "../../../IAM/latest/UserGuide/access_policies_access-advisor.md")
- [IAM
  policy types and when to use them](../../../IAM/latest/UserGuide/access_policies.md "../../../IAM/latest/UserGuide/access_policies.md")
- [Testing
  IAM policies with the IAM policy simulator](../../../IAM/latest/UserGuide/access_policies_testing-policies.md "../../../IAM/latest/UserGuide/access_policies_testing-policies.md")
- [Guardrails
  in AWS Control Tower](../../../controltower/latest/userguide/guardrails.md "../../../controltower/latest/userguide/guardrails.md")
- [Zero
  Trust architectures: An AWS perspective](https://aws.amazon.com/blogs/security/zero-trust-architectures-an-aws-perspective/ "https://aws.amazon.com/blogs/security/zero-trust-architectures-an-aws-perspective/")
- [How
  to implement the principle of least privilege with
  CloudFormation StackSets](https://aws.amazon.com/blogs/security/how-to-implement-the-principle-of-least-privilege-with-cloudformation-stacksets/ "https://aws.amazon.com/blogs/security/how-to-implement-the-principle-of-least-privilege-with-cloudformation-stacksets/")
- [Attribute-based
  access control (ABAC)](../../../IAM/latest/UserGuide/introduction_attribute-based-access-control.md "../../../IAM/latest/UserGuide/introduction_attribute-based-access-control.md")
- [Reducing
  policy scope by viewing user activity](../../../IAM/latest/UserGuide/access_policies_access-advisor.md "../../../IAM/latest/UserGuide/access_policies_access-advisor.md")
- [View
  role access](../../../IAM/latest/UserGuide/id_roles_manage_delete.md "../../../IAM/latest/UserGuide/id_roles_manage_delete.md")
- [Use
  Tagging to Organize Your Environment and Drive
  Accountability](../../../aws-technical-content/latest/cost-optimization-laying-the-foundation/tagging.md "../../../aws-technical-content/latest/cost-optimization-laying-the-foundation/tagging.md")
- [AWS Tagging Strategies](https://aws.amazon.com/answers/account-management/aws-tagging-strategies/ "https://aws.amazon.com/answers/account-management/aws-tagging-strategies/")
- [Tagging
  AWS resources](https://aws.amazon.com/premiumsupport/knowledge-center/tagging-resources/ "https://aws.amazon.com/premiumsupport/knowledge-center/tagging-resources/")

**Related videos:**

- [Next-generation
  permissions management](https://www.youtube.com/watch?v=8vsD_aTtuTo "https://www.youtube.com/watch?v=8vsD_aTtuTo")
- [Zero
  Trust: An AWS perspective](https://www.youtube.com/watch?v=1p5G1-4s1r0 "https://www.youtube.com/watch?v=1p5G1-4s1r0")
