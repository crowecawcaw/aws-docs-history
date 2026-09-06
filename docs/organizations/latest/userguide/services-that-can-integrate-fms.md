

# AWS Firewall Manager and AWS Organizations
<a name="services-that-can-integrate-fms"></a>

AWS Firewall Manager is a security management service you use to centrally configure and manage firewall rules and other protections across the AWS accounts and applications in your organization. Using Firewall Manager, you can roll out AWS WAF rules, create AWS Shield Advanced protections, configure and audit Amazon Virtual Private Cloud (Amazon VPC) security groups, and deploy AWS Network Firewalls. Use Firewall Manager to set up your protections just once and have them automatically applied across all accounts and resources within your organization, even as new resources and accounts are added. For more information about AWS Firewall Manager, see the *[AWS Firewall Manager Developer Guide](https://docs.aws.amazon.com/waf/latest/developerguide/fms-chapter.html)*.

Use the following information to help you integrate AWS Firewall Manager with AWS Organizations.



## Service-linked roles created when you enable integration
<a name="integrate-enable-slr-fms"></a>

The following [service-linked role](https://docs.aws.amazon.com/IAM/latest/UserGuide/using-service-linked-roles.html) is automatically created in your organization's management account when you enable trusted access. This role allows Firewall Manager to perform supported operations within your organization's accounts in your organization.

You can delete or modify this role only if you disable trusted access between Firewall Manager and Organizations, or if you remove the member account from the organization.
+ `AWSServiceRoleForFMS`

When you enable trusted access for AWS Firewall Manager, the `AWSServiceRoleForFMS` service-linked role is automatically created in every member account in the organization. This includes accounts that join the organization later, either by invitation or by being created in the organization.

Standalone accounts and accounts in a different organization don't receive this role and can't be managed by Firewall Manager.

## Service principals used by the service-linked roles
<a name="integrate-enable-svcprin-fms"></a>

The service-linked role in the previous section can be assumed only by the service principals authorized by the trust relationships defined for the role. The service-linked roles used by Firewall Manager grant access to the following service principals:
+ `fms.amazonaws.com`

## Enabling trusted access with Firewall Manager
<a name="integrate-enable-ta-fms"></a>

For information about the permissions needed to enable trusted access, see [Permissions required to enable trusted access](orgs_integrate_services.md#orgs_trusted_access_perms).

You can enable trusted access using either the AWS Firewall Manager console or the AWS Organizations console.

**Important**  
We strongly recommend that whenever possible, you use the AWS Firewall Manager console or tools to enable integration with Organizations. This lets AWS Firewall Manager perform any configuration that it requires, such as creating resources needed by the service. Proceed with these steps only if you can’t enable integration using the tools provided by AWS Firewall Manager. For more information, see [this note](orgs_integrate_services.md#important-note-about-integration).   
If you enable trusted access by using the AWS Firewall Manager console or tools then you don’t need to complete these steps.

You must sign in with your AWS Organizations management account and configure an account within the organization as the AWS Firewall Manager administrator account. For more information, see [Set the AWS Firewall Manager Administrator Account](https://docs.aws.amazon.com/waf/latest/developerguide/enable-integration.html) in the *AWS Firewall Manager Developer Guide*.

You can enable trusted access by using either the AWS Organizations console, by running a AWS CLI command, or by calling an API operation in one of the AWS SDKs.

------
#### [ AWS Management Console ]

**To enable trusted service access using the Organizations console**

1. Sign in to the [AWS Organizations console](https://console.aws.amazon.com/organizations/v2). You must sign in as an IAM user, assume an IAM role, or sign in as the root user ([not recommended](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#lock-away-credentials)) in the organization’s management account.

1. In the navigation pane, choose **Services**.

1. Choose **AWS Firewall Manager** in the list of services.

1. Choose **Enable trusted access**.

1. In the **Enable trusted access for AWS Firewall Manager** dialog box, type **enable** to confirm, and then choose **Enable trusted access**.

1. If you are the administrator of only AWS Organizations, tell the administrator of AWS Firewall Manager that they can now enable that service to work with AWS Organizations from the service console .

------
#### [ AWS CLI, AWS API ]

**To enable trusted service access using the OrganizationsCLI/SDK**  
Use the following AWS CLI commands or API operations to enable trusted service access:
+ AWS CLI: [enable-aws-service-access](https://docs.aws.amazon.com/cli/latest/reference/organizations/enable-aws-service-access.html)

  Run the following command to enable AWS Firewall Manager as a trusted service with Organizations.

  ```
  $ aws organizations enable-aws-service-access \ 
      --service-principal fms.amazonaws.com
  ```

  This command produces no output when successful.
+ AWS API: [EnableAWSServiceAccess](https://docs.aws.amazon.com/organizations/latest/APIReference/API_EnableAWSServiceAccess.html)

------

## Disabling trusted access with Firewall Manager
<a name="integrate-disable-ta-fms"></a>

For information about the permissions needed to disable trusted access, see [Permissions required to disable trusted access](orgs_integrate_services.md#orgs_trusted_access_disable_perms).

You can disable trusted access using either the AWS Firewall Manager or the AWS Organizations tools.

**Important**  
We strongly recommend that whenever possible, you use the AWS Firewall Manager console or tools to disable integration with Organizations. This lets AWS Firewall Manager perform any clean up that it requires, such as deleting resources or access roles that are no longer needed by the service. Proceed with these steps only if you can’t disable integration using the tools provided by AWS Firewall Manager.  
If you disable trusted access by using the AWS Firewall Manager console or tools then you don’t need to complete these steps.

**To disable trusted access using the Firewall Manager console**  
You can change or revoke the AWS Firewall Manager administrator account by following the instructions in [Designating a Different Account as the AWS Firewall Manager Administrator Account](https://docs.aws.amazon.com/waf/latest/developerguide/fms-change-administrator.html) in the *AWS Firewall Manager Developer Guide*.

If you revoke the administrator account, you must sign in to the AWS Organizations management account and set a new administrator account for AWS Firewall Manager.

You can disable trusted access by using either the AWS Organizations console, by running an Organizations AWS CLI command, or by calling an Organizations API operation in one of the AWS SDKs.

------
#### [ AWS Management Console ]

**To disable trusted service access using the Organizations console**

1. Sign in to the [AWS Organizations console](https://console.aws.amazon.com/organizations/v2). You must sign in as an IAM user, assume an IAM role, or sign in as the root user ([not recommended](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#lock-away-credentials)) in the organization’s management account.

1. In the navigation pane, choose **Services**.

1. Choose **AWS Firewall Manager** in the list of services.

1. Choose **Disable trusted access**.

1. In the **Disable trusted access for AWS Firewall Manager** dialog box, type **disable** to confirm, and then choose **Disable trusted access**.

1. If you are the administrator of only AWS Organizations, tell the administrator of AWS Firewall Manager that they can now disable that service from working with AWS Organizations using the service console or tools .

------
#### [ AWS CLI, AWS API ]

**To disable trusted service access using the Organizations CLI/SDK**  
You can use the following AWS CLI commands or API operations to disable trusted service access:
+ AWS CLI: [disable-aws-service-access](https://docs.aws.amazon.com/cli/latest/reference/organizations/disable-aws-service-access.html)

  Run the following command to disable AWS Firewall Manager as a trusted service with Organizations.

  ```
  $ aws organizations disable-aws-service-access \
      --service-principal fms.amazonaws.com
  ```

  This command produces no output when successful.
+ AWS API: [DisableAWSServiceAccess](https://docs.aws.amazon.com/organizations/latest/APIReference/API_DisableAWSServiceAccess.html)

------

## Enabling a delegated administrator account for Firewall Manager
<a name="integrate-enable-da-fms"></a>

When you designate a member account as a delegated administrator for the organization, users and roles from that account can perform administrative actions for Firewall Manager that otherwise can be performed only by users or roles in the organization's management account. This helps you to separate management of the organization from management of Firewall Manager.

**Minimum permissions**  
Only a user or role in the Organizations management account can configure a member account as a delegated administrator for Firewall Manager in the organization.

For instructions on how to designate a member account as the Firewall Manager administrator for the organization, see [Set the AWS Firewall Manager Administrator Account](https://docs.aws.amazon.com/waf/latest/developerguide/enable-integration.html) in the *AWS Firewall Manager Developer Guide*.