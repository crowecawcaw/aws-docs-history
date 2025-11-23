# Monitor accounts across your

organization

If you choose to monitor applications across your organization, log into your
organization management account. You can optionally set up an organization member
account as a **delegated administrator**. You can only have one
delegated administrator at a time and can modify the administrator settings later.
Both the management account and the delegated administrator account that you set up
have access to all insights across all accounts in your organization.

You can either add cross account support for your organization using the Console,
or you can do so by using the AWS CLI.

## Onboard with the DevOps Guru Console

You can use the Console to add support for accounts across your
organization.

###### Use the Console to enable DevOps Guru to view aggregated insights

1. Open the Amazon DevOps Guru console at [https://console.aws.amazon.com/devops-guru/](https://console.aws.amazon.com/devops-guru/ "https://console.aws.amazon.com/devops-guru/").
2. Choose **Monitor applications across your
   organizations** as the setup type.
3. Choose which account you'd like to use as your delegated
   administrator. Then, choose **Register delegated
   administrator**. This provides access to a consolidated
   view for any account that has DevOps Guru enabled. The delegated administrator
   has a consolidated view of all DevOps Guru insights and metrics across your
   organization. You can enable other accounts with SSM quick setup or
   AWS CloudFormation stack sets. To learn more about quick
   setup, see [Configure DevOps Guru with Quick Setup](../../../systems-manager/latest/userguide/quick-setup-devops.md "../../../systems-manager/latest/userguide/quick-setup-devops.md"). To learn more about
   setting up with stack sets, see [Working with
   stacks](../../../AWSCloudFormation/latest/UserGuide/stacks.md "../../../AWSCloudFormation/latest/UserGuide/stacks.md") in the _CloudFormation User Guide_, and
   [Step 2 – Determine coverage for
   DevOps Guru](setting-up.md#setting-up-determine-coverage "setting-up.md#setting-up-determine-coverage"). and [Using CloudFormation stacks to identify resources in your DevOps Guru applications](working-with-cfn-stacks.md "working-with-cfn-stacks.md").

## Onboard with the AWS

CLI

You can use the AWS CLI to enable DevOps Guru to view aggregated insights. Run the
following commands.

```
aws iam create-service-linked-role --aws-service-name devops-guru.amazonaws.com --description "My service-linked role to support DevOps Guru"

aws organizations enable-aws-service-access --service-principal devops-guru.amazonaws.com

aws organizations register-delegated-administrator --account-id >ACCOUNT_ID< --service-principal devops-guru.amazonaws.com
```

The following table describes the commands.

| Command                            | Description                                                                                                                     |
| ---------------------------------- | ------------------------------------------------------------------------------------------------------------------------------- |
| `create-service-linked-role`       | Gives DevOps Guru permission to gather information about your<br>organization. Don't proceed if this step is not<br>successful. |
| `enable-aws-service-access`        | Onboards your organization to DevOps Guru.                                                                                      |
| `register-delegated-administrator` | Gives access to the member account to view<br>insights.                                                                         |
