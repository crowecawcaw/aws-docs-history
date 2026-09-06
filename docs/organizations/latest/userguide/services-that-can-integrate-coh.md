

# AWS Cost Optimization Hub and AWS Organizations
<a name="services-that-can-integrate-coh"></a>

AWS Cost Optimization Hub is an AWS Billing and Cost Management feature that helps you consolidate and prioritize cost optimization recommendations across your AWS accounts and AWS Regions, so that you can get the most out of your AWS spend. When you use Cost Optimization Hub with AWS Organizations you can easily identify, filter, and aggregate AWS cost optimization recommendations across your Organizations member accounts and AWS Regions. 

For more information, see [ Cost Optimization Hub ](https://docs.aws.amazon.com/cost-management/latest/userguide/cost-optimization-hub.html) in the *AWS Cost Management User Guide*.

Use the following information to help you integrate AWS Cost Optimization Hub with AWS Organizations.



## Service-linked roles created when you enable integration
<a name="integrate-enable-slr-coh"></a>

The following [service-linked role](https://docs.aws.amazon.com/IAM/latest/UserGuide/using-service-linked-roles.html) is automatically created in your organization's management account when you enable trusted access. This role allows Cost Optimization Hub to perform supported operations within your organization's accounts in your organization.

You can delete or modify this role only if you disable trusted access between Cost Optimization Hub and Organizations, or if you remove the member account from the organization.

For more information, see [ Service-linked role permissions for Cost Optimization Hub ](https://docs.aws.amazon.com/cost-management/latest/userguide/cost-optimization-hub-SLR.html#cost-optimization-hub-SLR-permissions) in the *AWS Cost Management User Guide*.
+ `AWSServiceRoleForCostOptimizationHub`

## Service principals used by Cost Optimization Hub
<a name="integrate-enable-svcprin-coh"></a>

Cost Optimization Hub uses the `cost-optimization-hub.bcm.amazonaws.com` service principal.

## Enabling trusted access with Cost Optimization Hub
<a name="integrate-enable-ta-coh"></a>

For information about the permissions needed to enable trusted access, see [Permissions required to enable trusted access](orgs_integrate_services.md#orgs_trusted_access_perms).

When you opt in using your organization's management account and include all member accounts within the organization, trusted access for Cost Optimization Hub is automatically enabled in your organization account. 

You can enable trusted access by using either the AWS Organizations console, by running a AWS CLI command, or by calling an API operation in one of the AWS SDKs.

------
#### [ AWS Management Console ]

**To enable trusted service access using the Organizations console**

1. Sign in to the [AWS Organizations console](https://console.aws.amazon.com/organizations/v2). You must sign in as an IAM user, assume an IAM role, or sign in as the root user ([not recommended](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#lock-away-credentials)) in the organization’s management account.

1. In the navigation pane, choose **Services**.

1. Choose **AWS Cost Optimization Hub** in the list of services.

1. Choose **Enable trusted access**.

1. In the **Enable trusted access for AWS Cost Optimization Hub** dialog box, type **enable** to confirm, and then choose **Enable trusted access**.

1. If you are the administrator of only AWS Organizations, tell the administrator of AWS Cost Optimization Hub that they can now enable that service to work with AWS Organizations from the service console .

------
#### [ AWS CLI, AWS API ]

**To enable trusted service access using the OrganizationsCLI/SDK**  
Use the following AWS CLI commands or API operations to enable trusted service access:
+ AWS CLI: [enable-aws-service-access](https://docs.aws.amazon.com/cli/latest/reference/organizations/enable-aws-service-access.html)

  Run the following command to enable AWS Cost Optimization Hub as a trusted service with Organizations.

  ```
  $ aws organizations enable-aws-service-access \ 
      --service-principal cost-optimization-hub.bcm.amazonaws.com
  ```

  This command produces no output when successful.
+ AWS API: [EnableAWSServiceAccess](https://docs.aws.amazon.com/organizations/latest/APIReference/API_EnableAWSServiceAccess.html)

------

## Disabling trusted access
<a name="integrate-disable-ta-coh"></a>

For information about the permissions needed to disable trusted access, see [Permissions required to disable trusted access](orgs_integrate_services.md#orgs_trusted_access_disable_perms).

You can only disable trusted access using the Organizations tools.

**Important**  
 If you disable Cost Optimization Hub trusted access after you opt in, Cost Optimization Hub denies access to recommendations for your organization's member accounts. Moreover, the member accounts within the organization aren't opted in to Cost Optimization Hub. Learn more in [Cost Optimization Hub and Organizations trusted access ](https://docs.aws.amazon.com/cost-management/latest/userguide/coh-trusted-access.html) in the *AWS Cost Management User Guide*.

You can disable trusted access by running a Organizations AWS CLI command, or by calling an Organizations API operation in one of the AWS SDKs.

------
#### [ AWS CLI, AWS API ]

**To disable trusted service access using the Organizations CLI/SDK**  
Use the following AWS CLI commands or API operations to disable trusted service access:
+ AWS CLI: [disable-aws-service-access](https://docs.aws.amazon.com/cli/latest/reference/organizations/disable-aws-service-access.html)

  Run the following command to disable AWS Cost Optimization Hub as a trusted service with Organizations.

  ```
  $ aws organizations disable-aws-service-access \
      --service-principal cost-optimization-hub.bcm.amazonaws.com
  ```

  This command produces no output when successful.
+ AWS API: [DisableAWSServiceAccess](https://docs.aws.amazon.com/organizations/latest/APIReference/API_DisableAWSServiceAccess.html)

------

## Enabling a delegated administrator account for Cost Optimization Hub
<a name="integrate-enable-da-coh"></a>

When you designate a member account to be a delegated administrator for the organization, the designated account can retrieve Cost Optimization Hub recommendations for all accounts under your organization and manage Cost Optimization Hub preferences, giving you greater flexibility to centrally identify resource optimization opportunities. 

**Minimum permissions**  
Only a user or role in the Organizations management account with the following permission can configure a member account as a delegated administrator for Cost Optimization Hub in the organization:

For instructions about enabling a delegated administrator account for Cost Optimization Hub, see [ Delegate an administrator account](https://docs.aws.amazon.com/cost-management/latest/userguide/coh-delegated-admin.html) in the *AWS Cost Management User Guide*. 

## Disabling a delegated administrator for Cost Optimization Hub
<a name="integrate-disable-da-coh"></a>

 Only an administrator in the Organizations management account can remove a delegated administrator for Cost Optimization Hub. 

To disable the delegated admin Cost Optimization Hub account using the Cost Optimization Hub console, see [ Delegate an administrator account](https://docs.aws.amazon.com/cost-management/latest/userguide/coh-delegated-admin.html) in the *AWS Cost Management User Guide*.

 To remove a delegated administrator using the AWS CLI, see [`deregister-delegated-administrator`](https://docs.aws.amazon.com/cli/latest/) in the *AWS Config CLI Reference*.