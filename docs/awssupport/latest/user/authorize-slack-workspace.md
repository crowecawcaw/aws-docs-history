

# Authorize a Slack workspace
<a name="authorize-slack-workspace"></a>

After you authorize your workspace and give the AWS Support App permission to access it, you then need an AWS Identity and Access Management (IAM) role for your AWS account. The AWS Support App uses this role to call API operations from [AWS Support](https://docs.aws.amazon.com/awssupport/latest/APIReference/Welcome.html) and [Service Quotas](https://docs.aws.amazon.com/servicequotas/2019-06-24/apireference/Welcome.html) for you. For example, the AWS Support App uses the role to call the `CreateCase` operation to create a support case for you in Slack.

**Notes**  
Your Slack channel inherits permissions from the IAM role. All users in the Slack channel have the same permissions that are specified in the IAM policy attached to the role. For example, if your IAM policy grants full read and write permissions to your support cases, anyone in your Slack channel can create, update, and resolve your support cases. If your IAM policy allows the role read-only permissions, then users in your Slack channel can only view your support cases.
We recommend that you add the Slack workspaces and channels that you need to manage your support operations. We recommend that you configure private channels and only invite required users.

 You must authorize each Slack workspace that you want to use for your AWS account. If you have multiple AWS accounts, you must sign in to each account and repeat the following procedure to authorize the workspace. If your account belongs to an organization in AWS Organizations and you want to authorize multiple accounts, skip to [ Authorize multiple accounts](https://docs.aws.amazon.com/awssupport/latest/user/authorize-slack-workspace.html#authorize-multiple-accounts). 

**To authorize the Slack workspace for your AWS account**

1. Sign in to the [**AWS Support Center Console**](https://console.aws.amazon.com/support/app) and choose **Slack configuration**.

1. On the **Getting started** page, choose **Authorize workspace**.

1. If you're not already signed in to Slack, on the **Sign in to your workspace** page, enter your workspace name, and then choose **Continue**.

1. On the **AWS Support is requesting permission to access the your-workspace-name Slack** page, choose **Allow**.
**Note**  
If you can't allow Slack to access your workspace, make sure that you have permissions from your Slack administrator to add the AWS Support App to the workspace. See [Prerequisites](prerequisites-support-app-for-slack.md).

   On the **Slack configuration** page, your workspace name appears under **Workspaces**.

1. (Optional) To add more workspaces, choose **Authorize workspace** and repeat steps 3-4. You can add up to five workspaces to your account. 

1. (Optional) By default, your AWS account ID number appears as the account name in your Slack channel. To change this value, under **Account name**, choose **Edit**, enter your account name, and then choose **Save**. 
**Tip**  
Use a name that you and your team can easily recognize. The AWS Support App uses this name to identify your account in the Slack channel. You can update this name at any time.  
![Screenshot of how to edit an account name so that it appears in the AWS Support App for Slack.](http://docs.aws.amazon.com/awssupport/latest/user/images/supportapp/edit-account-name.png)

   Your workspace and account name appear on the **Slack configuration** page.  
![Slack workspace added to the AWS Support App configuration page.](http://docs.aws.amazon.com/awssupport/latest/user/images/supportapp/one-workplace-added-to-support-app.png)

## Authorize multiple accounts
<a name="authorize-multiple-accounts"></a>

If your account belongs to an organization in AWS Organizations, you can authorize multiple AWS accounts to use the same Slack workspace. You can use AWS CloudFormation templates to automate this process, or you can manually configure each account using the AWS Support App API.

### Use AWS CloudFormation templates
<a name="authorize-multiple-accounts-cloudformation"></a>

You can use [AWS CloudFormation](creating-resources-with-cloudformation.md) or [Terraform](creating-resources-with-cloudformation.md#terraform-support-app) to create your AWS Support App resources across multiple accounts. This is the recommended approach for managing multiple accounts at scale.

For more information, see [Creating AWS Support App in Slack resources with AWS CloudFormation](creating-resources-with-cloudformation.md).

### Use the AWS Support App API
<a name="authorize-multiple-accounts-api"></a>

If you prefer not to use AWS CloudFormation templates, you can manually authorize multiple accounts using the AWS Support App API. Complete the following steps for each member account that you want to add to the Slack workspace.

**To manually authorize multiple accounts**

1. In the management account (the account where you created the Slack workspace), authorize the Slack workspace. For more information, see the procedure in [Authorize a Slack workspace](#authorize-slack-workspace).

1. In each member account, call the [`RegisterSlackWorkspaceForOrganization`](https://docs.aws.amazon.com/supportapp/latest/APIReference/API_RegisterSlackWorkspaceForOrganization.html) API operation to register the Slack workspace for that account.

   This operation adds the member account to the Slack workspace that was authorized by the management account.

1. In each member account, create an IAM role with the required permissions for the AWS Support App. For more information, see [Managing access to the AWS Support App](support-app-permissions.md).

1. In each member account, call the [`CreateSlackChannelConfiguration`](https://docs.aws.amazon.com/supportapp/latest/APIReference/API_CreateSlackChannelConfiguration.html) API operation to configure a Slack channel for that account.

   This operation associates the Slack channel with the member account and specifies the IAM role that the AWS Support App uses to call AWS Support and Service Quotas operations.

**Note**  
Each member account must be part of the same organization in AWS Organizations as the management account that authorized the Slack workspace.