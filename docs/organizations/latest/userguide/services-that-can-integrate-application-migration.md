

# AWS Transform MGN (MGN) and AWS Organizations
<a name="services-that-can-integrate-application-migration"></a>

AWS Transform MGN simplifies, expedites, and reduces the cost of migrating applications to AWS. By integrating with Organizations, you can use the global view feature to manage large-scale migrations across multiple accounts. For more information see [ Setting up your AWS Organizations](https://docs.aws.amazon.com/mgn/latest/ug/setting-up-organizations.html) in the *MGN user guide*. 

Use the following information to help you integrate AWS Transform MGN with AWS Organizations.



## Service-linked roles created when you enable integration
<a name="integrate-enable-slr-application-migration"></a>

The following [service-linked role](https://docs.aws.amazon.com/IAM/latest/UserGuide/using-service-linked-roles.html) is automatically created in your organization's management account when you enable trusted access. This role allows MGN to perform supported operations within your organization's accounts in your organization.

You can delete or modify this role only if you disable trusted access between MGN and Organizations, or if you remove the member account from the organization.
+ `AWSServiceRoleForApplicationMigrationService `

## Service principals used by MGN
<a name="integrate-enable-svcprin-application-migration"></a>

The service-linked role in the previous section can be assumed only by the service principals authorized by the trust relationships defined for the role. The service-linked roles used by MGN grant access to the following service principals:
+ `mgn.amazonaws.com`

## Enabling trusted access with MGN
<a name="integrate-enable-ta-application-migration"></a>

When you enable trusted access with MGN you can use the global view feature, which allows you to manage large-scale migrations across multiple accounts. Global view provides visibility and the ability to perform specific actions on source servers, apps, and waves in different AWS accounts. For more information, see [Setting up your AWS Organizations](https://docs.aws.amazon.com/mgn/latest/ug/setting-up-organizations.html) in the *AWS Transform MGN user guide*.

For information about the permissions needed to enable trusted access, see [Permissions required to enable trusted access](orgs_integrate_services.md#orgs_trusted_access_perms).

You can enable trusted access using either the AWS Transform MGN console or the AWS Organizations console.

**Important**  
We strongly recommend that whenever possible, you use the AWS Transform MGN console or tools to enable integration with Organizations. This lets AWS Transform MGN perform any configuration that it requires, such as creating resources needed by the service. Proceed with these steps only if you can’t enable integration using the tools provided by AWS Transform MGN. For more information, see [this note](orgs_integrate_services.md#important-note-about-integration).   
If you enable trusted access by using the AWS Transform MGN console or tools then you don’t need to complete these steps.

You can enable trusted access by using either the AWS Organizations console, by running a AWS CLI command, or by calling an API operation in one of the AWS SDKs.

------
#### [ AWS Management Console ]

**To enable trusted service access using the Organizations console**

1. Sign in to the [AWS Organizations console](https://console.aws.amazon.com/organizations/v2). You must sign in as an IAM user, assume an IAM role, or sign in as the root user ([not recommended](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#lock-away-credentials)) in the organization’s management account.

1. In the navigation pane, choose **Services**.

1. Choose **AWS Transform MGN** in the list of services.

1. Choose **Enable trusted access**.

1. In the **Enable trusted access for AWS Transform MGN** dialog box, type **enable** to confirm, and then choose **Enable trusted access**.

1. If you are the administrator of only AWS Organizations, tell the administrator of AWS Transform MGN that they can now enable that service to work with AWS Organizations from the service console .

------
#### [ AWS CLI, AWS API ]

**To enable trusted service access using the OrganizationsCLI/SDK**  
Use the following AWS CLI commands or API operations to enable trusted service access:
+ AWS CLI: [enable-aws-service-access](https://docs.aws.amazon.com/cli/latest/reference/organizations/enable-aws-service-access.html)

  Run the following command to enable AWS Transform MGN as a trusted service with Organizations.

  ```
  $ aws organizations enable-aws-service-access \ 
      --service-principal mgn.amazonaws.com
  ```

  This command produces no output when successful.
+ AWS API: [EnableAWSServiceAccess](https://docs.aws.amazon.com/organizations/latest/APIReference/API_EnableAWSServiceAccess.html)

------

## Disabling trusted access with MGN
<a name="integrate-disable-ta-application-migration"></a>

Only an administrator in the Organizations management account can disable trusted access with MGN. 

You can disable trusted access using either the AWS Transform MGN or the AWS Organizations tools.

**Important**  
We strongly recommend that whenever possible, you use the AWS Transform MGN console or tools to disable integration with Organizations. This lets AWS Transform MGN perform any clean up that it requires, such as deleting resources or access roles that are no longer needed by the service. Proceed with these steps only if you can’t disable integration using the tools provided by AWS Transform MGN.  
If you disable trusted access by using the AWS Transform MGN console or tools then you don’t need to complete these steps.

You can disable trusted access by using either the AWS Organizations console, by running an Organizations AWS CLI command, or by calling an Organizations API operation in one of the AWS SDKs.

------
#### [ AWS Management Console ]

**To disable trusted service access using the Organizations console**

1. Sign in to the [AWS Organizations console](https://console.aws.amazon.com/organizations/v2). You must sign in as an IAM user, assume an IAM role, or sign in as the root user ([not recommended](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#lock-away-credentials)) in the organization’s management account.

1. In the navigation pane, choose **Services**.

1. Choose **AWS Transform MGN** in the list of services.

1. Choose **Disable trusted access**.

1. In the **Disable trusted access for AWS Transform MGN** dialog box, type **disable** to confirm, and then choose **Disable trusted access**.

1. If you are the administrator of only AWS Organizations, tell the administrator of AWS Transform MGN that they can now disable that service from working with AWS Organizations using the service console or tools .

------
#### [ AWS CLI, AWS API ]

**To disable trusted service access using the Organizations CLI/SDK**  
You can use the following AWS CLI commands or API operations to disable trusted service access:
+ AWS CLI: [disable-aws-service-access](https://docs.aws.amazon.com/cli/latest/reference/organizations/disable-aws-service-access.html)

  Run the following command to disable AWS Transform MGN as a trusted service with Organizations.

  ```
  $ aws organizations disable-aws-service-access \
      --service-principal mgn.amazonaws.com
  ```

  This command produces no output when successful.
+ AWS API: [DisableAWSServiceAccess](https://docs.aws.amazon.com/organizations/latest/APIReference/API_DisableAWSServiceAccess.html)

------

## Enabling a delegated administrator account for MGN
<a name="integrate-enable-da-application-migration"></a>

When you designate a member account as a delegated administrator for the organization, users and roles from that account can perform administrative actions for MGN that otherwise can be performed only by users or roles in the organization's management account. This helps you to separate management of the organization from management of MGN. For more information see [ Setting up your AWS Organizations](https://docs.aws.amazon.com/mgn/latest/ug/setting-up-organizations.html) in the *MGN user guide*. 

**Minimum permissions**  
Only a user or role in the Organizations management account can configure a member account as a delegated administrator for MGN in the organization

------
#### [ AWS CLI, AWS API ]

If you want to configure a delegated administrator account using the AWS CLI or one of the AWS SDKs, you can use the following commands:
+ AWS CLI: 

  ```
  $ aws organizations register-delegated-administrator \
      --account-id 123456789012 \
      --service-principal mgn.amazonaws.com
  ```
+ AWS SDK: Call the Organizations `RegisterDelegatedAdministrator` operation and the member account's ID number and identify the account service `mgn.amazonaws.com` as parameters. 

------

## Disabling a delegated administrator for MGN
<a name="integrate-disable-da-application-migration"></a>

 Only an administrator in the Organizations management account can remove a delegated administrator for MGN. You can remove the delegated administrator using the Organizations `DeregisterDelegatedAdministrator` CLI or SDK operation. 