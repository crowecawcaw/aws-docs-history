# Troubleshoot multi-account self-managed roles in an AWS global network

AWS Global Networks for Transit Gateways uses AWS CloudFormation StackSets to deploy the required
`IAMRoleForAWSNetworkManagerCrossAccountResourceAccess` role and the CloudWatch
monitoring `CloudWatch-CrossAccountSharingRole` role in your AWS Organizations member
accounts for cross-account access. For a CloudFormation StackSets-managed deployment, IAM
roles must have the required policies attached, as well as the trusted relationship to allow
registered delegated administrators and the management account the ability to assume these
roles. In a self-managed deployment, you own the responsibility to attach the appropriate
policies and to manage the trusted relationship required for the delegated administrator and
management accounts to access multiple accounts.

###### Important

We strongly recommend that you use the global networks console for enabling multi-account
settings using the global networks console as this automatically sets up all required roles
and permissions for multi-account access. Choosing an alternative approach requires an
advanced level of expertise and opens the multi-account setup for your global network to
be more prone to error.

If the CloudFormation StackSets deployment fails, and the **Review required**
message is **IAM role exists**, follow the steps below in [IAM role exists](#nm-multi-iam-role-exists "#nm-multi-iam-role-exists") to change
the role from **Self-managed** to **StackSets-managed**.
For any message other than **IAM role exists**, file an AWS Support
case. For more information on creating a support case, see [Creating a
support case](../../../awssupport/latest/user/case-management.md#creating-a-support-case "../../../awssupport/latest/user/case-management.md#creating-a-support-case") in the _AWS Support User Guide_.

## IAM role exists

If the IAM role has the exact same name in a current the member account, these roles
appear in the **IAM role deployments status** with a status of
**Self-managed**. In order to change this to StackSets-managed,
delete the IAM role from the member account with the duplicate role name. After
deleting the IAM role, use the global networks console to retry the role deployment. For the
steps to retry a role deployment, see [Manage IAM multi-account role deployments in an AWS global
network](nm-multi-manage-iam.md "nm-multi-manage-iam.md") to retry the role deployment.

###### To change a role from self-managed to StackSets-managed

1. Access the AWS Identity and Access Management (IAM) console at [https://console.aws.amazon.com/iamv2/home?#/](https://console.aws.amazon.com/iamv2/home?#/ "https://console.aws.amazon.com/iamv2/home?#/") with the member account that has a self-managed role
   status.
2. In the navigation pane, choose **Roles**.
3. In the **Roles** field, search for the role name you want to
   delete.
4. Choose the role, and then choose **Delete**.
5. Confirm that you want to delete the role.

###### Warning

This might break other functionality if a custom role has other attached
policies or trusted relationships. 6. Access the global networks console at [https://console.aws.amazon.com/networkmanager/home/](https://console.aws.amazon.com/networkmanager/home "https://console.aws.amazon.com/networkmanager/home") with the AWS Organizations management
account. 7. Choose **Get started**. 8. In the navigation pane, choose **Settings**. 9. In the **IAM role deployment status section**, choose
**Retry role deployment**.

Depending on the size of your organization, it might take several minutes or
longer to disable trusted access. During this time you won't be able to
re-enable trusted access.
