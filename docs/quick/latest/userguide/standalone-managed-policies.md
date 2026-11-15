

# AWS managed policies for AWS Quick
<a name="standalone-managed-policies"></a>

AWS Quick Free, Plus, and Max accounts use an AWS managed policy so that AWS Quick can operate on your behalf. AWS services maintain and update AWS managed policies. You can't change the permissions in AWS managed policies. For more information about AWS managed policies, see [AWS managed policies](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_managed-vs-inline.html#aws-managed-policies) in the *IAM User Guide*.

**Topics**
+ [AWS managed policy: AmazonQuickSuiteAccessPolicy](#standalone-managed-policies-AmazonQuickSuiteAccessPolicy)
+ [AWS Quick updates to AWS managed policies](#standalone-managed-policies-updates)

## AWS managed policy: AmazonQuickSuiteAccessPolicy
<a name="standalone-managed-policies-AmazonQuickSuiteAccessPolicy"></a>

The `AmazonQuickSuiteAccessPolicy` AWS managed policy applies only to [AWS Quick Free, Plus, and Max accounts](standalone-admin-guide.md). AWS Quick uses this policy to manage its IAM Identity Center application, identity store users and groups, user subscriptions, and AWS Quick resources for these accounts.

AWS Quick automatically creates the `AmazonQuickSuiteAccessRole` service role, attaches this policy to it, and uses it on your behalf. You don't need to configure, attach, or manage this policy yourself.

**Important**  
This policy is intended only for use by the AWS Quick service. Don't attach `AmazonQuickSuiteAccessPolicy` to your own IAM users, groups, or roles.

With AWS Quick, sensitive operations are tightly scoped: token runtime actions are limited to your IAM Identity Center applications, sign-in token creation is restricted to resources in your own account, and role assumption and role passing are limited to the dedicated `AmazonQuickSuiteAccessRole` in your account.

**Permissions details**

This policy includes the following permissions:
+ `quicksight` – Lets AWS Quick use all AWS Quick actions to create, read, update, and delete AWS Quick resources, such as dashboards, analyses, datasets, data sources, and users, on your behalf.
+ `identitystore` – Lets AWS Quick read and manage the users and groups in your IAM Identity Center identity store, including looking up, creating, updating, and deleting users and groups and resolving their identifiers and group memberships.
+ `sso` – Lets AWS Quick discover your IAM Identity Center instance and manage its own Identity Center application end to end, including creating, updating, describing, and deleting the application; configuring its authentication method, grants, and access scopes; managing user and group assignments; and associating or disassociating profiles.
+ `sso-oauth` – Lets AWS Quick create, inspect, and revoke OAuth tokens through IAM Identity Center to authenticate requests and manage sessions for signed-in users. This access is scoped to IAM Identity Center application resources.
+ `signin` – Lets AWS Quick create an OAuth 2.0 token that is used in the sign-in flow for your users. This access is restricted by a condition to resources in your own account.
+ `sts` – Lets AWS Quick assume a role, set session context, and tag the session to obtain temporary credentials to act on your behalf. This access is limited to the dedicated `AmazonQuickSuiteAccessRole` in your own account.
+ `iam` – Lets AWS Quick pass a role to AWS services as part of its operations. This access is restricted to the dedicated `AmazonQuickSuiteAccessRole` in your own account.
+ `user-subscriptions` – Lets AWS Quick manage your subscription plan and the per-user claims associated with it, including reading your current plan, previewing plan changes, configuring overage behavior, and creating or updating claims.
+ `organizations` – Lets AWS Quick read your AWS Organizations configuration to determine your organization context and confirm which AWS services have trusted access enabled. This access is read-only.

To view the `AmazonQuickSuiteAccessPolicy`, see [AmazonQuickSuiteAccessPolicy](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AmazonQuickSuiteAccessPolicy.html) in the AWS Managed Policy reference.



## AWS Quick updates to AWS managed policies
<a name="standalone-managed-policies-updates"></a>

View details about updates to AWS managed policies for AWS Quick since this service began tracking these changes. For automatic alerts about changes to this page, subscribe to the RSS feed on the [AWS Quick Document History](doc-history.md) page.




| Change | Description | Date | 
| --- | --- | --- | 
| `AmazonQuickSuiteAccessPolicy` – New policy | AWS Quick added a new AWS managed policy that lets AWS Quick manage its IAM Identity Center application, identity store users and groups, user subscriptions, and AWS Quick resources on your behalf. | October 12, 2026 | 