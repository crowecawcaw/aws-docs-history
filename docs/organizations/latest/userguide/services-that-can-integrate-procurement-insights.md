

# AWS Marketplace procurement insights dashboard and AWS Organizations
<a name="services-that-can-integrate-procurement-insights"></a>

You use the AWS Marketplace procurement insights dashboard to view agreements and cost-analysis data for all of the AWS accounts in your organization. When integrated with Organizations, AWS Marketplace procurement insights dashboard listens to organization changes, such as an account joining the organization, and aggregates data for their corresponding agreements to build their dashboards. 

For more information, see [Procurement insights ](https://docs.aws.amazon.com/marketplace/latest/buyerguide/procurement-insights.html) in the *AWS Marketplace Buyer Guide*.

Use the following information to help you integrate AWS Marketplace procurement insights dashboard with AWS Organizations.



## Service-linked roles and managed policies created when you enable integration
<a name="integrate-enable-slr-procurement-insights"></a>

 When you activate the AWS Marketplace procurement insights dashboard dashboard the [`AWSServiceRoleForProcurementInsightsPolicy`](https://docs.aws.amazon.com/marketplace/latest/buyerguide/buyer-service-linked-role-procurement.html) service-linked role and the [`AWSServiceRoleForProcurementInsightsPolicy`](https://docs.aws.amazon.com/marketplace/latest/buyerguide/buyer-security-iam-awsmanpol.html#aws-procurement-insights) AWS managed policy are created.

## Enabling trusted access with AWS Marketplace procurement insights
<a name="integrate-enable-ta-procurement-insights"></a>

Enabling trusted access grants the AWS Marketplace procurement insights dashboard the ability to integrate with the customer's Organizations service. AWS Marketplace procurement insights dashboard listens to organization changes, such as an account joining the organization, and aggregates data for their corresponding agreements to build their dashboards. 

For information about the permissions needed to enable trusted access, see [Permissions required to enable trusted access](orgs_integrate_services.md#orgs_trusted_access_perms).

You can enable trusted access using either the AWS Marketplace procurement insights dashboard console or the AWS Organizations console.

**Important**  
We strongly recommend that whenever possible, you use the AWS Marketplace procurement insights dashboard console or tools to enable integration with Organizations. This lets AWS Marketplace procurement insights dashboard perform any configuration that it requires, such as creating resources needed by the service. Proceed with these steps only if you can’t enable integration using the tools provided by AWS Marketplace procurement insights dashboard. For more information, see [this note](orgs_integrate_services.md#important-note-about-integration).   
If you enable trusted access by using the AWS Marketplace procurement insights dashboard console or tools then you don’t need to complete these steps.

**To enable trusted access by enabling the AWS Marketplace procurement insights dashboard**  
See [Enabling the AWS Marketplace procurement insights dashboard](https://docs.aws.amazon.com/marketplace/latest/buyerguide/enabling-procurement-insights.html) in the *AWS Marketplace Buyer Guide*.

**To enable trusted access using Organizations tools**

You can enable trusted access by using either the AWS Organizations console, by running a AWS CLI command, or by calling an API operation in one of the AWS SDKs.

------
#### [ AWS Management Console ]

**To enable trusted service access using the Organizations console**

1. Sign in to the [AWS Organizations console](https://console.aws.amazon.com/organizations/v2). You must sign in as an IAM user, assume an IAM role, or sign in as the root user ([not recommended](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#lock-away-credentials)) in the organization’s management account.

1. In the navigation pane, choose **Services**.

1. Choose **AWS Marketplace procurement insights dashboard** in the list of services.

1. Choose **Enable trusted access**.

1. In the **Enable trusted access for AWS Marketplace procurement insights dashboard** dialog box, type **enable** to confirm, and then choose **Enable trusted access**.

1. If you are the administrator of only AWS Organizations, tell the administrator of AWS Marketplace procurement insights dashboard that they can now enable that service to work with AWS Organizations from the service console .

------
#### [ AWS CLI, AWS API ]

**To enable trusted service access using the OrganizationsCLI/SDK**  
Use the following AWS CLI commands or API operations to enable trusted service access:
+ AWS CLI: [enable-aws-service-access](https://docs.aws.amazon.com/cli/latest/reference/organizations/enable-aws-service-access.html)

  Run the following command to enable AWS Marketplace procurement insights dashboard as a trusted service with Organizations.

  ```
  $ aws organizations enable-aws-service-access \ 
      --service-principal procurement-insights.marketplace.amazonaws.com
  ```

  This command produces no output when successful.
+ AWS API: [EnableAWSServiceAccess](https://docs.aws.amazon.com/organizations/latest/APIReference/API_EnableAWSServiceAccess.html)

------

## Disabling trusted access with AWS Marketplace procurement insights
<a name="integrate-disable-ta-procurement-insights"></a>

For information about the permissions needed to enable trusted access, see [Permissions required to enable trusted access](orgs_integrate_services.md#orgs_trusted_access_perms).

You can only disable trusted access using the Organizations tools.

You can disable trusted access by running a Organizations AWS CLI command, or by calling an Organizations API operation in one of the AWS SDKs.

------
#### [ AWS CLI, AWS API ]

**To disable trusted service access using the Organizations CLI/SDK**  
Use the following AWS CLI commands or API operations to disable trusted service access:
+ AWS CLI: [disable-aws-service-access](https://docs.aws.amazon.com/cli/latest/reference/organizations/disable-aws-service-access.html)

  Run the following command to disable AWS Marketplace procurement insights dashboard as a trusted service with Organizations.

  ```
  $ aws organizations disable-aws-service-access \
      --service-principal procurement-insights.marketplace.amazonaws.com
  ```

  This command produces no output when successful.
+ AWS API: [DisableAWSServiceAccess](https://docs.aws.amazon.com/organizations/latest/APIReference/API_DisableAWSServiceAccess.html)

------

## Enabling a delegated administrator account for AWS Marketplace procurement insights
<a name="integrate-enable-da-procurement-insights"></a>

To configure a delegated administrator in the AWS Marketplace procurement insights console, see See [Registering delegated administrators>](https://docs.aws.amazon.com/marketplace/latest/buyerguide/management-delegates.html#management-register-delegate) in the *AWS Marketplace Buyer Guide*.

 You can also configure a delegated administrator by using the Organizations `RegisterDelegatedAdministrator` API. For more information, see [ RegisterDelegatedAdministrator](https://docs.aws.amazon.com/cli/latest/reference/organizations/register-delegated-administrator.html) in the * Organizations Command Reference*.

## Disabling a delegated administrator for AWS Marketplace procurement insights
<a name="integrate-disable-da-procurement-insights"></a>

Only an administrator in the organization management account can configure a delegated administrator for AWS Marketplace procurement insights.

To remove a delegated administrator through the AWS Marketplace procurement insights console, see [Deregistering delegated administrators](https://docs.aws.amazon.com/marketplace/latest/buyerguide/management-delegates.html#management-deregister-delegate) in the *AWS Marketplace Buyer Guide*.

You can also remove the delegated administrator by using the Organizations `DeregisterDelegatedAdministrator` CLI or SDK operation.