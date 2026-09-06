

# Permit account instance creation in member accounts
<a name="enable-account-instance-console"></a>

If you enabled IAM Identity Center before November 15, 2023, you have an [organization instance](organization-instances-identity-center.md) of IAM Identity Center with the ability for member accounts to create account instances disabled by default. You can choose whether your member accounts can create account instances by enabling the account instance feature in the IAM Identity Center console. 

**To enable creation of account instances by member accounts in your organization**
**Important**  
Enabling account instances of IAM Identity Center for member accounts is a one-time operation. This means that this operation cannot be reversed. Once enabled, you can limit the creation of account instances by creating a service control policy (SCP). For instructions, see [Control account instance creation with Services Control Policies](https://docs.aws.amazon.com/singlesignon/latest/userguide/control-account-instance.html).

1. Open the [IAM Identity Center console](https://console.aws.amazon.com/singlesignon).

1. Choose **Settings**, and then choose the **Management** tab.

1. In the **Account instances of IAM Identity Center** section, choose **Enable account instances of IAM Identity Center**.

1. In the **Enable account instances of IAM Identity Center** dialog box, confirm that you want to allow member accounts in your organization to create account instances by choosing **Enable**.