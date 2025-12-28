# Overview of managing access

permissions to your CloudWatch Logs resources

To provide access, add permissions to your users, groups, or roles:

- Users and groups in AWS IAM Identity Center:

Create a permission set. Follow the instructions in [Create a permission set](../../../singlesignon/latest/userguide/howtocreatepermissionset.md "../../../singlesignon/latest/userguide/howtocreatepermissionset.md") in the _AWS IAM Identity Center User Guide_.

- Users managed in IAM through an identity provider:

Create a role for identity federation. Follow the instructions in [Create a role for a third-party identity provider (federation)](../../../IAM/latest/UserGuide/id_roles_create_for-idp.md "../../../IAM/latest/UserGuide/id_roles_create_for-idp.md")
in the _IAM User Guide_.

- IAM users:
  - Create a role that your user can assume. Follow the instructions in [Create a role for an IAM user](../../../IAM/latest/UserGuide/id_roles_create_for-user.md "../../../IAM/latest/UserGuide/id_roles_create_for-user.md") in the _IAM User Guide_.
  - (Not recommended) Attach a policy directly to a user or add a user to a user group. Follow the instructions in [Adding permissions to a user (console)](../../../IAM/latest/UserGuide/id_users_change-permissions.md#users_change_permissions-add-console "../../../IAM/latest/UserGuide/id_users_change-permissions.md#users_change_permissions-add-console") in the _IAM User Guide_.

###### Topics

- [CloudWatch Logs resources and operations](#CWL_ARN_Format "#CWL_ARN_Format")
- [Understanding resource
  ownership](#understanding-resource-ownership-cwl "#understanding-resource-ownership-cwl")
- [Managing access to resources](#managing-access-resources-cwl "#managing-access-resources-cwl")
- [Specifying policy elements:
  Actions, effects, and principals](#actions-effects-principals-cwl "#actions-effects-principals-cwl")
- [Specifying conditions in a policy](#policy-conditions-cwl "#policy-conditions-cwl")

## CloudWatch Logs resources and operations

In CloudWatch Logs the primary resources are log groups, log streams and destinations. CloudWatch Logs
does not support subresources (other resources for use with the primary
resource).

These resources and subresources have unique Amazon Resource Names (ARNs)
associated with them as shown in the following table.

| Resource type | ARN format                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| ------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Log group     | Both of the following are used. The second one, with the<br>`:*` at the end, is what is returned by the<br>`describe-log-groups` CLI command and the<br>\*_DescribeLogGroups_<br>• API.<br>arn:aws:logs:`region`:`account-id`:log-group:`log_group_name`<br>arn:aws:logs:`region`:`account-id`:log-group:`log_group_name`:\*<br>Use the first version, without the trailing `:*`,<br>in the following situations:<br>• In the `logGroupIdentifier` input field in<br>many CloudWatch Logs APIs.<br>• In the `resourceArn` field in tagging<br>APIs<br>• In IAM policies, when specifying<br>permissions for [TagResource](../../../AmazonCloudWatchLogs/latest/APIReference/API_TagResource.md "../../../AmazonCloudWatchLogs/latest/APIReference/API_TagResource.md"), [UntagResource](../../../AmazonCloudWatchLogs/latest/APIReference/API_UntagResource.md "../../../AmazonCloudWatchLogs/latest/APIReference/API_UntagResource.md"), and [ListTagsForResource](../../../AmazonCloudWatchLogs/latest/APIReference/API_ListTagsForResource.md "../../../AmazonCloudWatchLogs/latest/APIReference/API_ListTagsForResource.md").<br>Use the second version, with the trailing `:*`, to<br>refer to the ARN when specifying permissions in IAM policies<br>for all other API actions. |
| Log stream    | arn:aws:logs:`region`:`account-id`:log-group:`log_group_name`:log-stream:`log-stream-name`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| Destination   | arn:aws:logs:`region`:`account-id`:destination:`destination_name`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     |

For more information about ARNs, see [ARNs](../../../IAM/latest/UserGuide/Using_Identifiers.md#Identifiers_ARNs "../../../IAM/latest/UserGuide/Using_Identifiers.md#Identifiers_ARNs") in
_IAM User Guide_. For information about CloudWatch Logs ARNs, see
[Amazon Resource Names (ARNs)](../../../general/latest/gr/aws-arns-and-namespaces.md#arn-syntax-cloudwatch-logs "../../../general/latest/gr/aws-arns-and-namespaces.md#arn-syntax-cloudwatch-logs") in _Amazon Web Services General Reference_.
For an example of a policy that covers CloudWatch Logs, see [Using identity-based policies
(IAM policies) for CloudWatch Logs](iam-identity-based-access-control-cwl.md "iam-identity-based-access-control-cwl.md").

CloudWatch Logs provides a set of operations to work with the CloudWatch Logs resources. For a list of
available operations, see [CloudWatch Logs permissions reference](permissions-reference-cwl.md "permissions-reference-cwl.md").

## Understanding resource

ownership

The AWS account owns the resources that are created in the account, regardless
of who created the resources. Specifically, the resource owner is the AWS account
of the [principal
entity](../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md "../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md") (that is, the root account, a user, or an IAM role) that
authenticates the resource creation request. The following examples illustrate how
this works:

- If you use the root account credentials of your AWS account to create a
  log group, your AWS account is the owner of the CloudWatch Logs resource.
- If you create a user in your AWS account and grant permissions to create
  CloudWatch Logs resources to that user, the user can create CloudWatch Logs resources. However,
  your AWS account, to which the user belongs, owns the CloudWatch Logs
  resources.
- If you create an IAM role in your AWS account with permissions to
  create CloudWatch Logs resources, anyone who can assume the role can create CloudWatch Logs
  resources. Your AWS account, to which the role belongs, owns the CloudWatch Logs
  resources.

## Managing access to resources

A _permissions policy_ describes who has access to what. The
following section explains the available options for creating permissions
policies.

###### Note

This section discusses using IAM in the context of CloudWatch Logs. It doesn't
provide detailed information about the IAM service. For complete IAM
documentation, see [What is
IAM?](../../../IAM/latest/UserGuide/introduction.md "../../../IAM/latest/UserGuide/introduction.md") in the _IAM User Guide_. For information
about IAM policy syntax and descriptions, see [IAM policy reference](../../../IAM/latest/UserGuide/reference_policies.md "../../../IAM/latest/UserGuide/reference_policies.md")
in the _IAM User Guide_.

Policies attached to an IAM identity are referred to as identity-based policies
(IAM policies) and policies attached to a resource are referred to as
resource-based policies. CloudWatch Logs supports identity-based policies, and resource-based
policies for destinations, which are used to enable cross account subscriptions. For
more information, see [Cross-account cross-Region
subscriptions](CrossAccountSubscriptions.md "CrossAccountSubscriptions.md").

###### Topics

- [Log group
  permissions and Contributor Insights](#cloudwatch-logs-permissions-and-contributor-insights "#cloudwatch-logs-permissions-and-contributor-insights")
- [Resource-based policies](#resource-based-policies-cwl "#resource-based-policies-cwl")

### Log group

permissions and Contributor Insights

Contributor Insights is a feature of CloudWatch that enables you to analyze data
from log groups and create time series that display contributor data. You can
see metrics about the top-N contributors, the total number of unique
contributors, and their usage. For more information, see [Using
Contributor Insights to Analyze High-Cardinality Data](../monitoring/ContributorInsights.md "../monitoring/ContributorInsights.md").

When you grant a user the `cloudwatch:PutInsightRule` and
`cloudwatch:GetInsightRuleReport` permissions, that user can
create a rule that evaluates any log group in CloudWatch Logs and then see the results.
The results can contain contributor data for those log groups. Be sure to grant
these permissions only to users who should be able to view this data.

### Resource-based policies

CloudWatch Logs supports resource-based policies for destinations, which you can use to
enable cross account subscriptions. For more information, see [Step 1: Create a destination](CreateDestination.md "CreateDestination.md").
Destinations can be created using the [PutDestination](../../../AmazonCloudWatchLogs/latest/APIReference/API_PutDestination.md "../../../AmazonCloudWatchLogs/latest/APIReference/API_PutDestination.md") API, and
you can add a resource policy to the destination using the [PutDestinationPolicy](../../../AmazonCloudWatchLogs/latest/APIReference/API_PutDestinationPolicy.md "../../../AmazonCloudWatchLogs/latest/APIReference/API_PutDestinationPolicy.md") API. The following example allows another
AWS account with the account ID 111122223333 to subscribe their log
groups to the destination
`arn:aws:logs:us-east-1:123456789012:destination:testDestination`.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement" : [
 {
 "Sid" : "",
 "Effect" : "Allow",
 "Principal" : {
 "AWS" : "111122223333"
 },
 "Action" : "logs:PutSubscriptionFilter",
 "Resource" : "arn:aws:logs:us-east-1:123456789012:destination:testDestination"
 }
 ]
}`

```

## Specifying policy elements:

Actions, effects, and principals

For each CloudWatch Logs resource, the service defines a set of API operations. To grant
permissions for these API operations, CloudWatch Logs defines a set of actions that you can
specify in a policy. Some API operations can require permissions for more than one
action in order to perform the API operation. For more information about resources
and API operations, see [CloudWatch Logs resources and operations](#CWL_ARN_Format "#CWL_ARN_Format") and [CloudWatch Logs permissions reference](permissions-reference-cwl.md "permissions-reference-cwl.md").

The following are the basic policy elements:

- **Resource** – You use an Amazon
  Resource Name (ARN) to identify the resource that the policy applies to. For
  more information, see [CloudWatch Logs resources and operations](#CWL_ARN_Format "#CWL_ARN_Format").
- **Action** – You use action keywords to
  identify resource operations that you want to allow or deny. For example,
  the `logs.DescribeLogGroups` permission allows the user
  permissions to perform the `DescribeLogGroups` operation.
- **Effect** – You specify the effect,
  either allow or deny, when the user requests the specific action. If you
  don't explicitly grant access to (allow) a resource, access is implicitly
  denied. You can also explicitly deny access to a resource, which you might
  do to make sure that a user cannot access it, even if a different policy
  grants access.
- **Principal** – In identity-based
  policies (IAM policies), the user that the policy is attached to is the
  implicit principal. For resource-based policies, you specify the user,
  account, service, or other entity that you want to receive permissions
  (applies to resource-based policies only). CloudWatch Logs supports resource-based
  policies for destinations.

To learn more about IAM policy syntax and descriptions, see [AWS IAM Policy Reference](../../../IAM/latest/UserGuide/reference_policies.md "../../../IAM/latest/UserGuide/reference_policies.md")
in the _IAM User Guide_.

For a table showing all of the CloudWatch Logs API actions and the resources that they apply
to, see [CloudWatch Logs permissions reference](permissions-reference-cwl.md "permissions-reference-cwl.md").

## Specifying conditions in a policy

When you grant permissions, you can use the access policy language to specify the
conditions when a policy should take effect. For example, you might want a policy to
be applied only after a specific date. For more information about specifying
conditions in a policy language, see [Condition](../../../IAM/latest/UserGuide/reference_policies_elements_condition.md "../../../IAM/latest/UserGuide/reference_policies_elements_condition.md")
in the _IAM User Guide_.

To express conditions, you use predefined condition keys. For a list of context
keys supported by each AWS service and a list of AWS-wide policy keys, see
[Actions, resources, and condition keys for AWS services](../../../service-authorization/latest/reference/reference_policies_actions-resources-contextkeys.md "../../../service-authorization/latest/reference/reference_policies_actions-resources-contextkeys.md") and [AWS global
condition context keys](../../../IAM/latest/UserGuide/reference_policies_condition-keys.md "../../../IAM/latest/UserGuide/reference_policies_condition-keys.md") .

###### Note

You can use tags to control access to CloudWatch Logs resources, including log groups
and destinations. Access to log streams is controlled at the log group level,
because of the hierarchical relation between log groups and log streams. For
more information about using tags to control access, see [Controlling
access to Amazon Web Services resources using tags](../../../IAM/latest/UserGuide/access_tags.md "../../../IAM/latest/UserGuide/access_tags.md").
