# Opting in to AWS Compute Optimizer

Use the following procedure to opt in your account, or the accounts within your organization, to AWS Compute Optimizer.
You can opt in using the Compute Optimizer console or the AWS Command Line Interface (AWS CLI).

###### Note

If your account is already opted in, but you want to opt in again to re-enable trusted
access for Compute Optimizer in your organization. You can opt in again, but this must be done using the
AWS CLI. When you opt in using the AWS CLI, run the `update-enrollment-status`
command and specify the `--include-member-accounts` parameter. Alternatively, you
can enable trusted access directly in the AWS Organizations console or by using AWS CLI or API. For
more information, see [Using AWS Organizations
with other AWS services](../../../organizations/latest/userguide/orgs_integrate_services.md "../../../organizations/latest/userguide/orgs_integrate_services.md") in the _AWS Organizations User Guide_.

## Prerequisites

Make sure your IAM identity has appropriate permissions to opt in to AWS Compute Optimizer. The suggested policy that
grants this permission is [Policy to opt in to Compute Optimizer](security-iam.md#opting-in-access "security-iam.md#opting-in-access").

## Procedure

Console

###### To opt in to Compute Optimizer

1. Open the Compute Optimizer console at [https://console.aws.amazon.com/compute-optimizer/](https://console.aws.amazon.com/compute-optimizer/ "https://console.aws.amazon.com/compute-optimizer/").

If this is your first time using the Compute Optimizer console, the **Compute Optimizer landing
page** is displayed. 2. Choose **Get started**. 3. On the **Account setup** page, review the **Getting
started** and **Setting up your account**
sections. 4. The following options are displayed if the account that you're signed in to is
the management account of your organization. Choose one before continuing to the next
step.

    * **Only this account** - Choose this option to
     opt in only the account that you’re currently signed in to. If you choose this
     option, Compute Optimizer analyzes resources that are in the individual account, and
     generates optimization recommendations for those resources.
    * **All accounts within this organization** -
     Choose this option to opt in the account you’re currently signed in to, and all
     of its member accounts. If you choose this option, Compute Optimizer analyzes resources that
     are in all accounts in the organization, and generates optimization
     recommendations for those resources.


    ###### Note

    If you add any new member accounts to your organization after you opt in, Compute Optimizer
     automatically opts in those accounts.

5. Choose **Opt in**. By opting in, you indicate that you agree to
   and understand the requirements to opt in to Compute Optimizer.

After you opt in, you're redirected to the dashboard in the Compute Optimizer console. At the
same time, the service immediately starts analyzing the configuration and utilization
metrics of your AWS resources. For more information, see [Metrics analyzed by AWS Compute Optimizer](metrics.md "metrics.md").

###### Note

When you complete the opt in process, it can up to 24 hours for the opted-in accounts to
appear in the Compute Optimizer console.

CLI

###### To opt in to Compute Optimizer

1. Open a terminal or command prompt window.

If you didn't already install the AWS CLI already, install and configure it to
work with Compute Optimizer. For more information, see [Installing the AWS CLI](../../../cli/latest/userguide/cli-chap-install.md "../../../cli/latest/userguide/cli-chap-install.md") and [Quickly
Configuring the AWS CLI](../../../cli/latest/userguide/cli-chap-configure.md#cli-quick-configuration "../../../cli/latest/userguide/cli-chap-configure.md#cli-quick-configuration") in the _AWS Command Line Interface User
Guide_. 2. Enter one of the following commands. Choose if you want to opt in your
individual account or the management account of your organization and all its member
accounts.

    * To opt in your individual account:



    ```
    `aws compute-optimizer update-enrollment-status --status Active`
    ```
    * To opt in the management account of an organization and include all member
     accounts within the organization:



    ```
    `aws compute-optimizer update-enrollment-status --status Active --include-member-accounts`
    ```

After you opt in to Compute Optimizer using the previous command, the service begins analyzing
the configuration and utilization metrics of your AWS resources. For more information,
see [Metrics analyzed by AWS Compute Optimizer](metrics.md "metrics.md").

## Next steps

- Make sure that your AWS resources meet the necessary requirements for Compute Optimizer to generate your receommendations.
  And allow for at least 24 hours for your optimization recommendations to be generated.
  be generated. For more information, see [Resource requirements](requirements.md "requirements.md").
- View the findings and recommendations in the dashboard and recommendation
  pages of the Compute Optimizer console. For more information, see [Using the AWS Compute Optimizer dashboard](viewing-dashboard.md "viewing-dashboard.md") and [Viewing resource recommendations](viewing-recommendations.md "viewing-recommendations.md").
- Consider extending the lookback period from the 14-day default period to 93 days by activating the
  enhanced infrastructure metrics feature. For more information, see [Enhanced infrastructure metrics](enhanced-infrastructure-metrics.md "enhanced-infrastructure-metrics.md").
- Using the management account of your organization, you can delegate a member account
  as an administrator for Compute Optimizer. For more
  information, see [Delegating an administrator account](delegate-administrator-account.md "delegate-administrator-account.md").

## Additional resources

- [Identity and Access Management for AWS Compute Optimizer](security-iam.md "security-iam.md")
- [AWS managed policies for AWS Compute Optimizer](managed-policies.md "managed-policies.md")
- [Using service-linked roles for AWS Compute Optimizer](using-service-linked-roles.md "using-service-linked-roles.md")
- Troubleshooting — [Troubleshooting in Compute Optimizer](troubleshooting-account-opt-in.md "troubleshooting-account-opt-in.md")
