

# Amazon CloudWatch and AWS Organizations
<a name="services-that-can-integrate-cloudwatch"></a>

You can use AWS Organizations for Amazon CloudWatch for the following use cases:
+ Discover and understand the state of telemetry configuration for your AWS resources from a central view in the CloudWatch console. This simpliﬁes the process of auditing your telemetry collection configurations for multiple resource types across your AWS organization or account. You must turn on trusted access to use telemetry config across your organization.

  For more information, see [Auditing CloudWatch telemetry configurations](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/telemetry-config-cloudwatch.html) in the *Amazon CloudWatch User Guide*. 
+ Work with multiple accounts in Network Flow Monitor, a feature of Amazon CloudWatch Network Monitoring. Network Flow Monitor provides near real-time visibility into network performance for traffic between Amazon EC2 instances. After you turn on trusted access to integrate with Organizations, you can create a monitor to visualize network performance details across multiple accounts.

  For more information, see [ Initialize Network Flow Monitor for multi-account monitoring](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-NetworkFlowMonitor-multi-account.html) in the *Amazon CloudWatch User Guide*. 

Use the following information to help you integrate Amazon CloudWatch with AWS Organizations.



## Service-linked roles created when you enable integration
<a name="integrate-enable-slr-cloudwatch"></a>

Create the following [service-linked role](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_create-service-linked-role.html) in your organization's management account. The service-linked role is automatically created in member accounts when you enable trusted access. This role allows CloudWatch to perform supported operations within your organization's accounts in your organization. You can delete or modify this role only if you disable trusted access between CloudWatch and Organizations, or if you remove the member account from the organization.
+ `AWSServiceRoleForObservabilityAdmin`

## Service principals used by the service-linked roles
<a name="integrate-enable-svcprin-cloudwatch"></a>

The service-linked role in the previous section can be assumed only by the service principals authorized by the trust relationships defined for the role. The service-linked roles used by CloudWatch grant access to the following service principals:
+ `observabilityadmin.amazonaws.com`
+ `networkflowmonitor.amazonaws.com`
+ `topology.networkflowmonitor.amazonaws.com`

## Enabling trusted access with CloudWatch
<a name="integrate-enable-ta-cloudwatch"></a>

For information about the permissions that you need to turn on trusted access, see [Permissions required to enable trusted access](orgs_integrate_services.md#orgs_trusted_access_perms).

You can enable trusted access using either the Amazon CloudWatch console or the AWS Organizations console.

**Important**  
We strongly recommend that whenever possible, you use the Amazon CloudWatch console or tools to enable integration with Organizations. This lets Amazon CloudWatch perform any configuration that it requires, such as creating resources needed by the service. Proceed with these steps only if you can’t enable integration using the tools provided by Amazon CloudWatch. For more information, see [this note](orgs_integrate_services.md#important-note-about-integration).   
If you enable trusted access by using the Amazon CloudWatch console or tools then you don’t need to complete these steps.

**To turn on trusted access using the CloudWatch console**  
See [ Turning on CloudWatch telemetry auditing](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/telemetry-config-turn-on.html) in the *Amazon CloudWatch User Guide*.

When you turn on trusted access in CloudWatch, you enable telemetry auditing and you can work with multiple accounts in Network Flow Monitor.

You can enable trusted access by using either the AWS Organizations console, by running a AWS CLI command, or by calling an API operation in one of the AWS SDKs.

------
#### [ AWS Management Console ]

**To enable trusted service access using the Organizations console**

1. Sign in to the [AWS Organizations console](https://console.aws.amazon.com/organizations/v2). You must sign in as an IAM user, assume an IAM role, or sign in as the root user ([not recommended](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#lock-away-credentials)) in the organization’s management account.

1. In the navigation pane, choose **Services**.

1. Choose **Amazon CloudWatch** in the list of services.

1. Choose **Enable trusted access**.

1. In the **Enable trusted access for Amazon CloudWatch** dialog box, type **enable** to confirm, and then choose **Enable trusted access**.

1. If you are the administrator of only AWS Organizations, tell the administrator of Amazon CloudWatch that they can now enable that service to work with AWS Organizations from the service console .

------
#### [ AWS CLI, AWS API ]

**To enable trusted service access using the OrganizationsCLI/SDK**  
Use the following AWS CLI commands or API operations to enable trusted service access:
+ AWS CLI: [enable-aws-service-access](https://docs.aws.amazon.com/cli/latest/reference/organizations/enable-aws-service-access.html)

  Run the following command to enable Amazon CloudWatch as a trusted service with Organizations.

  ```
  $ aws organizations enable-aws-service-access \ 
      --service-principal observabilityadmin.amazonaws.com
  ```

  This command produces no output when successful.
+ AWS API: [EnableAWSServiceAccess](https://docs.aws.amazon.com/organizations/latest/APIReference/API_EnableAWSServiceAccess.html)

------

## Turn off trusted access with CloudWatch
<a name="integrate-disable-ta-cloudwatch"></a>

For information about the permissions needed to disable trusted access, see [Permissions required to disable trusted access](orgs_integrate_services.md#orgs_trusted_access_disable_perms).

You can disable trusted access using either the Amazon CloudWatch or the AWS Organizations tools.

**Important**  
We strongly recommend that whenever possible, you use the Amazon CloudWatch console or tools to disable integration with Organizations. This lets Amazon CloudWatch perform any clean up that it requires, such as deleting resources or access roles that are no longer needed by the service. Proceed with these steps only if you can’t disable integration using the tools provided by Amazon CloudWatch.  
If you disable trusted access by using the Amazon CloudWatch console or tools then you don’t need to complete these steps.

**To turn off trusted access using the CloudWatch console**  
See [ Turning off CloudWatch telemetry auditing ](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/telemetry-config-turn-off.html) in the *Amazon CloudWatch User Guide*

When you turn off trusted access in CloudWatch, telemetry auditing is no longer active and you can no longer work with multiple accounts in Network Flow Monitor.

You can disable trusted access by running a Organizations AWS CLI command, or by calling an Organizations API operation in one of the AWS SDKs.

------
#### [ AWS CLI, AWS API ]

**To disable trusted service access using the Organizations CLI/SDK**  
Use the following AWS CLI commands or API operations to disable trusted service access:
+ AWS CLI: [disable-aws-service-access](https://docs.aws.amazon.com/cli/latest/reference/organizations/disable-aws-service-access.html)

  Run the following command to disable Amazon CloudWatch as a trusted service with Organizations.

  ```
  $ aws organizations disable-aws-service-access \
      --service-principal observabilityadmin.amazonaws.com
  ```

  This command produces no output when successful.
+ AWS API: [DisableAWSServiceAccess](https://docs.aws.amazon.com/organizations/latest/APIReference/API_DisableAWSServiceAccess.html)

------

## Registering a delegated administrator account for CloudWatch
<a name="integrate-enable-da-cloudwatch"></a>

When you register a member account as a delegated administrator account for the organization, users and roles from that account can perform administrative actions for CloudWatch that otherwise can be performed only by users or roles signed in with the organization's management account. Using a delegated administrator account helps you to separate management of the organization from management of features in CloudWatch. 

**Minimum permissions**  
Only an administrator in the Organizations management account can register a member account as a delegated administrator account for CloudWatch in the organization.

You can register a delegated administrator account using the CloudWatch console, or by using the Organizations `RegisterDelegatedAdministrator` API operation with the AWS Command Line Interface or an SDK.

For information on how to register a delegated administrator account by using the CloudWatch console, see [ Turning on CloudWatch telemetry auditing ](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/telemetry-config-turn-on.html) in the *Amazon CloudWatch User Guide*.

When you register a delegated administrator account in CloudWatch, you can use the account for management operations with telemetry auditing and with Network Flow Monitor.

## Deregister a delegated administrator for CloudWatch
<a name="integrate-disable-da-cloudwatch"></a>

**Minimum permissions**  
Only an administrator signed in with the Organizations management account can deregister a delegated administrator account for CloudWatch in the organization.

 You can deregister the delegated administrator account by using either the CloudWatch console, or by using the Organizations `DeregisterDelegatedAdministrator` API operation with the AWS Command Line Interface or an SDK. For more information, see [ Deregistering a delegated administrator account](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/telemetry-config-turn-on.html#telemetry-config-deregister-administrator) in the *Amazon CloudWatch User Guide*. 

When you deregister a delegated administrator account in CloudWatch, you can no longer use the account for management operations with telemetry auditing and with Network Flow Monitor.