• AWS Systems Manager Change Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see
[AWS Systems Manager Change Manager availability change](change-manager-availability-change.md "change-manager-availability-change.md").

 

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see
[Amazon CloudWatch Dashboard documentation](../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md "../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md").

# Configuring roles and permissions for

Systems Manager Explorer

Integrated Setup automatically creates and configures AWS Identity and Access Management (IAM) roles for
AWS Systems Manager Explorer and AWS Systems Manager OpsCenter. If you completed Integrated Setup, then you
don't need to perform any additional tasks to configure roles and permissions for
Explorer. However, you must configure permission for OpsCenter, as described later
in this topic.

Integrated Setup creates and configures the following roles for working with
Explorer and OpsCenter.

- `AWSServiceRoleForAmazonSSM`: Provides access to AWS
  resources managed or used by Systems Manager.
- `OpsItem-CWE-Role`: Allows CloudWatch Events and EventBridge to create OpsItems in
  response to common events.
- `AWSServiceRoleForAmazonSSM_AccountDiscovery`: Allows Systems Manager to
  call other AWS services to discover AWS account information when
  synchronizing data. For more information about this role, see [Using roles to collect AWS account information for OpsCenter and Explorer](using-service-linked-roles-service-action-2.md "using-service-linked-roles-service-action-2.md").
- `AmazonSSMExplorerExport`: Allows Explorer to export OpsData to
  a comma-separated value (CSV) file.
  If you configure Explorer to display data from multiple accounts and Regions by
  using AWS Organizations and a resource data sync, then Systems Manager creates the
  `AWSServiceRoleForAmazonSSM_AccountDiscovery` service-linked role.
  Systems Manager uses this role to get information about your AWS accounts in AWS Organizations. The
  role uses the following permissions policy.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement":[
 {
 "Effect":"Allow",
 "Action":[
 "organizations:DescribeAccount",
 "organizations:DescribeOrganization",
 "organizations:ListAccounts",
 "organizations:ListAWSServiceAccessForOrganization",
 "organizations:ListChildren",
 "organizations:ListParents"
 ],
 "Resource":"*"
 }
 ]
}`

```

For more information about the
`AWSServiceRoleForAmazonSSM_AccountDiscovery` role, see [Using roles to collect AWS account information for OpsCenter and Explorer](using-service-linked-roles-service-action-2.md "using-service-linked-roles-service-action-2.md").

## Configuring

permissions for Systems Manager OpsCenter

After you complete Integrated Setup, you must configure user, group, or role
permissions so that users can perform actions in OpsCenter.

###### Before you begin

You can configure OpsCenter to create and manage OpsItems for a single
account or across multiple accounts. If you configure OpsCenter to create
and manage OpsItems across multiple accounts, you can use either the Systems Manager
delegated administrator account or the AWS Organizations management account to
manually create, view, or edit OpsItems in other accounts. For more information
about the Systems Manager delegated administrator account, see [Configuring a delegated
administrator for Explorer](Explorer-setup-delegated-administrator.md "Explorer-setup-delegated-administrator.md").

If you configure OpsCenter for a single account, you can only view or edit
OpsItems in the account where OpsItems were created. You can't share or transfer OpsItems
across AWS accounts. For this reason, we recommend that you configure
permissions for OpsCenter in the AWS account that is used to run your AWS
workloads. You can then create users or groups in that account. In this way,
multiple operations engineers or IT professionals can create, view, and edit
OpsItems in the same AWS account.

Explorer and OpsCenter use the following API operations. You can use all
features of Explorer and OpsCenter if your user, group, or role has access to
these actions. You can also create more restrictive access, as described later
in this section.

- [CreateOpsItem](../APIReference/API_CreateOpsItem.md "../APIReference/API_CreateOpsItem.md")
- [CreateResourceDataSync](../APIReference/API_CreateResourceDataSync.md "../APIReference/API_CreateResourceDataSync.md")
- [DescribeOpsItems](../APIReference/API_DescribeOpsItems.md "../APIReference/API_DescribeOpsItems.md")
- [DeleteResourceDataSync](../APIReference/API_DeleteResourceDataSync.md "../APIReference/API_DeleteResourceDataSync.md")
- [GetOpsItem](../APIReference/API_GetOpsItem.md "../APIReference/API_GetOpsItem.md")
- [GetOpsSummary](../APIReference/API_GetOpsSummary.md "../APIReference/API_GetOpsSummary.md")
- [ListResourceDataSync](../APIReference/API_ListResourceDataSync.md "../APIReference/API_ListResourceDataSync.md")
- [UpdateOpsItem](../APIReference/API_UpdateOpsItem.md "../APIReference/API_UpdateOpsItem.md")
- [UpdateResourceDataSync](../APIReference/API_UpdateResourceDataSync.md "../APIReference/API_UpdateResourceDataSync.md")

If you prefer, you can specify read-only permission by adding the following
inline policy to your account, group, or role.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "ssm:GetOpsItem",
 "ssm:GetOpsSummary",
 "ssm:DescribeOpsItems",
 "ssm:GetServiceSetting",
 "ssm:ListResourceDataSync"
 ],
 "Resource": "*"
 }
 ]
}`

```

For more information about creating and editing IAM policies, see [Creating IAM
Policies](../../../IAM/latest/UserGuide/access_policies_create.md "../../../IAM/latest/UserGuide/access_policies_create.md") in the _IAM User Guide_. For
information about how to assign this policy to an IAM group, see [Attaching a Policy
to an IAM Group](../../../IAM/latest/UserGuide/id_groups_manage_attach-policy.md "../../../IAM/latest/UserGuide/id_groups_manage_attach-policy.md").

Create a permission using the following and add it to your users, groups, or
roles:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "ssm:GetOpsItem",
 "ssm:UpdateOpsItem",
 "ssm:DescribeOpsItems",
 "ssm:CreateOpsItem",
 "ssm:CreateResourceDataSync",
 "ssm:DeleteResourceDataSync",
 "ssm:ListResourceDataSync",
 "ssm:UpdateResourceDataSync"

 ],
 "Resource": "*"
 }
 ]
}`

```

Depending on the identity application that you are using in your organization,
you can select any of the following options to configure user access.

To provide access, add permissions to your users, groups, or roles:

- Users and groups in AWS IAM Identity Center:

Create a permission set. Follow the instructions in [Create a permission set](../../../singlesignon/latest/userguide/howtocreatepermissionset.md "../../../singlesignon/latest/userguide/howtocreatepermissionset.md") in the _AWS IAM Identity Center User Guide_.

- Users managed in IAM through an identity provider:

Create a role for identity federation. Follow the instructions in [Create a role for a third-party identity provider (federation)](../../../IAM/latest/UserGuide/id_roles_create_for-idp.md "../../../IAM/latest/UserGuide/id_roles_create_for-idp.md")
in the _IAM User Guide_.

- IAM users:
  - Create a role that your user can assume. Follow the instructions in [Create a role for an IAM user](../../../IAM/latest/UserGuide/id_roles_create_for-user.md "../../../IAM/latest/UserGuide/id_roles_create_for-user.md") in the _IAM User Guide_.
  - (Not recommended) Attach a policy directly to a user or add a user to a user group. Follow the instructions in [Adding permissions to a user (console)](../../../IAM/latest/UserGuide/id_users_change-permissions.md#users_change_permissions-add-console "../../../IAM/latest/UserGuide/id_users_change-permissions.md#users_change_permissions-add-console") in the _IAM User Guide_.

### Restricting access to OpsItems by using tags

You can also restrict access to OpsItems by using an inline IAM policy that
specifies tags. Here is an example that specifies a tag key of
_Department_ and a tag value of
_Finance_. With this policy, the user can only call
the _GetOpsItem_ API operation to view OpsItems that were
previously tagged with Key=Department and Value=Finance. Users can't view
any other OpsItems.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "ssm:GetOpsItem"
 ],
 "Resource": "*"
 ,
 "Condition": { "StringEquals": { "ssm:resourceTag/Department": "Finance" } }
 }
 ]
}`

```

Here is an example that specifies API operations for viewing and updating
OpsItems. This policy also specifies two sets of tag key-value pairs:
Department-Finance and Project-Unity.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement":[
 {
 "Effect":"Allow",
 "Action":[
 "ssm:GetOpsItem",
 "ssm:UpdateOpsItem"
 ],
 "Resource":"*",
 "Condition":{
 "StringEquals":{
 "ssm:resourceTag/Department":"Finance",
 "ssm:resourceTag/Project":"Unity"
 }
 }
 }
 ]
}`

```

For information about adding tags to an OpsItem, see [Create OpsItems manually](OpsCenter-manually-create-OpsItems.md "OpsCenter-manually-create-OpsItems.md").
