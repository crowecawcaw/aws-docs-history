# Enable trusted access in an AWS global network

Enabling trust is a one-time task that deploys the required service-linked roles (SLRs)
and custom Identity and Access Management (IAM) roles to all accounts in your organization
that can be assumed by the management account or [delegated
administrators](nm-delegate-admin.md "nm-delegate-admin.md") for access across multiple accounts. For more information about
trusted access, see [Trusted access](nm-multi-account.md#nm-multi-trust "nm-multi-account.md#nm-multi-trust").

###### To enable multi-account trusted access

1. Log into the global networks console at [https://console.aws.amazon.com/networkmanager/home/](https://console.aws.amazon.com/networkmanager/home "https://console.aws.amazon.com/networkmanager/home"), using the AWS Organizations management
   account.
2. Choose **Get started**.
3. In the navigation pane, choose **Enable trusted access**.
4. From the **Permission level** dropdown list in **Enable
   trusted access,** choose the Permission level for the Network Manager console switch
   role `IAMRoleForAWSNetworkManagerCrossAccountResourceAccess`. This role is
   deployed to all member accounts and is assumed by the delegated administrator or
   management account when accessing resources from other accounts using the global networks
   console. You can choose only one permission level for all accounts. Permission can be one
   of the following:
   - **Read-only** — Assign this permission if the delegated
     administrator and management accounts only need to review information about resources
     from other accounts in the global network while using the console switch role, but
     don't need to make any changes.
   - **Admin** — Assign this permission if the delegated administrator
     and management accounts need to be able to modify resources from other accounts in the
     global network while using the global networks console switch role.

5. Choose **Enable trusted access**.

Depending on your organization size, it might take a few minutes or more to enable
trusted access. During this time the **State** shown in the
**Trusted access** section displays **Enabling in
progress**. When access is enabled, the **State** changes to
**Enabled**. Additionally, the **IAM role deployments
status** section at the bottom of the page displays the status of the IAM
roles being deployed to member accounts of the organization. 6. After trusted access is enabled, you can register delegated administrators.
