• AWS Systems Manager Change Manager is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see
[AWS Systems Manager Change Manager availability change](change-manager-availability-change.md "change-manager-availability-change.md").

 

• The AWS Systems Manager CloudWatch Dashboard will no longer be available after April 30, 2026. Customers can continue to use Amazon CloudWatch console to view, create, and manage their Amazon CloudWatch dashboards, just as they do today. For more information, see
[Amazon CloudWatch Dashboard documentation](../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md "../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Dashboards.md").

# Using roles to collect AWS account information for OpsCenter and Explorer

Systems Manager uses the service-linked role named **`AWSServiceRoleForAmazonSSM_AccountDiscovery`**. AWS Systems Manager uses this IAM service role to call other AWS services to discover
AWS account information.

## Service-linked

role permissions for Systems Manager account discovery

The `AWSServiceRoleForAmazonSSM_AccountDiscovery` service-linked role trusts the following
services to assume the role:

- `accountdiscovery.ssm.amazonaws.com`

The role permissions policy allows Systems Manager to complete the following
actions on the specified resources:

- `organizations:DescribeAccount`
- `organizations:DescribeOrganizationalUnit`
- `organizations:DescribeOrganization`
- `organizations:ListAccounts`
- `organizations:ListAWSServiceAccessForOrganization`
- `organizations:ListChildren`
- `organizations:ListParents`
- `organizations:ListDelegatedServicesForAccount`
- `organizations:ListDelegatedAdministrators`
- `organizations:ListRoots`

You must configure permissions to allow an IAM entity (such as a user,
group, or role) to create, edit, or delete a service-linked role. For more
information, see [Service-linked role permissions](../../../IAM/latest/UserGuide/using-service-linked-roles.md#service-linked-role-permissions "../../../IAM/latest/UserGuide/using-service-linked-roles.md#service-linked-role-permissions") in the
_IAM User Guide_.

## Creating the

`AWSServiceRoleForAmazonSSM_AccountDiscovery` service-linked role for
Systems Manager

You must create a service-linked role if you want to use Explorer and
OpsCenter, tools in Systems Manager, across multiple AWS accounts. For OpsCenter, you
must manually create the service-linked role. For more information, see [(Optional)
Manually set up OpsCenter to centrally manage OpsItems across accounts](OpsCenter-getting-started-multiple-accounts.md "OpsCenter-getting-started-multiple-accounts.md").

For Explorer, if you create a resource data sync by using Systems Manager in the
AWS Management Console, you can create the service-linked role by choosing the
**Create role** button. If you want to create a resource
data sync programmatically, then you must create the role before you create the
resource data sync. You can create the role by using the [CreateServiceLinkedRole](../../../IAM/latest/APIReference/API_CreateServiceLinkedRole.md "../../../IAM/latest/APIReference/API_CreateServiceLinkedRole.md") API operation.

## Editing the

`AWSServiceRoleForAmazonSSM_AccountDiscovery` service-linked role for
Systems Manager

Systems Manager doesn't allow you to edit the `AWSServiceRoleForAmazonSSM_AccountDiscovery`
service-linked role. After you create a service-linked role, you can't change
the name of the role because various entities might reference the role. However,
you can edit the description of the role using IAM. For more information, see
[Editing a service-linked role](../../../IAM/latest/UserGuide/using-service-linked-roles.md#edit-service-linked-role "../../../IAM/latest/UserGuide/using-service-linked-roles.md#edit-service-linked-role") in the
_IAM User Guide_.

## Deleting the

`AWSServiceRoleForAmazonSSM_AccountDiscovery` service-linked role for
Systems Manager

If you no longer need to use a feature or service that requires a
service-linked role, we recommend that you delete that role. That way you don’t
have an unused entity that isn't actively monitored or maintained. However, you
must clean up your service-linked role before you can manually delete it.

### Cleaning up the `AWSServiceRoleForAmazonSSM_AccountDiscovery` service-linked role

Before you can use IAM to delete the `AWSServiceRoleForAmazonSSM_AccountDiscovery`
service-linked role, you must first delete all Explorer resource data syncs.

###### Note

If the Systems Manager service is using the role when you try to delete
the resources, then the deletion might fail. If that happens, wait for a
few minutes and try the operation again.

### Manually delete the

`AWSServiceRoleForAmazonSSM_AccountDiscovery` service-linked role

Use the IAM console, the AWS CLI, or the AWS API to delete the
`AWSServiceRoleForAmazonSSM_AccountDiscovery` service-linked role. For more information,
see [Deleting a service-linked role](../../../IAM/latest/UserGuide/using-service-linked-roles.md#delete-service-linked-role "../../../IAM/latest/UserGuide/using-service-linked-roles.md#delete-service-linked-role") in the
_IAM User Guide_.

## Supported Regions for the

Systems Manager  `AWSServiceRoleForAmazonSSM_AccountDiscovery` service-linked role

Systems Manager supports using service-linked roles in all of the regions where
the service is available. For more information, see [AWS Systems Manager endpoints and quotas](../../../general/latest/gr/ssm.md "../../../general/latest/gr/ssm.md").

## Updates to the AWSServiceRoleForAmazonSSM_AccountDiscovery

service-linked role

View details about updates to the AWSServiceRoleForAmazonSSM_AccountDiscovery service-linked role since
this service began tracking these changes. For automatic alerts about changes to
this page, subscribe to the RSS feed on the Systems Manager [Document history](systems-manager-release-history.md "systems-manager-release-history.md") page.

| Change                | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | Date             |
| --------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ---------------- |
| New permissions added | This service-linked role now includes<br>`organizations:DescribeOrganizationalUnit`<br>and `organizations:ListRoots` permissions. These<br>permissions enable an AWS Organizations management account or a Systems Manager<br>delegated administrator account to work with OpsItems across<br>accounts. For more information, see [(Optional)<br>Manually set up OpsCenter to centrally manage OpsItems across accounts](OpsCenter-getting-started-multiple-accounts.md "OpsCenter-getting-started-multiple-accounts.md"). | October 17, 2022 |
