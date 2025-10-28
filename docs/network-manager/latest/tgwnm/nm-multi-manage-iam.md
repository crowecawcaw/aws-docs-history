# Manage IAM multi-account role deployments in an AWS global

network

The **IAM role deployments status** section displays the current role
deployments status for all member accounts set up in your account.

- **Member account ID** — The account ID for the account set up in
  AWS Organizations. This includes member accounts and members that have been registered as delegated
  administrators.
- **CloudWatch role status** — The status of the account's
  Amazon CloudWatch role. If you enable multi-account using the Network Manager console,
  this is **StackSets-managed** if deployed successfully. Otherwise, this
  is **Self-managed**.
- **Console role status** — The status of the account's Network Manager
  console role. If you enable multi-account using the Network Manager console, this is
  **StackSets-managed** if deployed successfully. Otherwise, this is
  **Self-managed**.
- **Review required** — This applies only to
  **Self-managed** roles. A review is required to ensure that the
  permissions set up for the account are correct. For more information, see [Multi-account access roles for AWS Global Networks for Transit Gateways](nm-custom-multi-role.md "nm-custom-multi-role.md").
  If you make changes to your role policies, or if you've updated a self-managed role, you
  can deploy the updated policy to your AWS Organizations accounts.

###### To retry the IAM role deployment status

1. Access the Network Manager console at [https://console.aws.amazon.com/networkmanager/home/](https://console.aws.amazon.com/networkmanager/home "https://console.aws.amazon.com/networkmanager/home") with the management account.
2. Under **Connectivity**, choose **Global Networks**.
3. In the navigation pane, choose **Settings**.
4. In the **IAM role deployments status** section, choose
   **Retry role deployment**.

Depending on your organization size and the number of member accounts in your
organization, this could take several minutes. During this time you won't be able to
register or deregister any new delegated administrators.
