

# AWS Identity and Access Management and AWS Organizations
<a name="services-that-can-integrate-iam"></a>

AWS Identity and Access Management is a web service for securely controlling access to AWS services. 

You can use [service last accessed data](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_access-advisor.html) in IAM to help you better understand AWS activity across your organization. You can use this data to create and update [service control policies (SCPs)](orgs_manage_policies_scps.md) that restrict access to only the AWS services that your organization's accounts use. 

For an example, see [Using Data to Refine Permissions for an Organizational Unit](https://docs.aws.amazon.com/IAM/latest/UserGuide/access_policies_access-advisor-example-scenarios.html#access_policies_access-advisor-reduce-permissions-orgs) in the *IAM User Guide.*

IAM lets you centrally manage root user credentials and perform privileged tasks on member accounts. After you enable root access management, which enables trusted access for IAM in AWS Organizations, you can centrally secure the root user credentials of member accounts. Member accounts can't sign in to their root user or perform password recovery for their root user. The management account or a delegated administrator account for IAM can also perform some privileged tasks on member accounts using short-term root access. Short-term privileged sessions give you temporary credentials that you can scope to take privileged actions on a member account in your organization. 

For more information, see [Centrally manage root access for member accounts](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_root-user.html#id_root-user-access-management) in the *IAM User Guide*. 

Use the following information to help you integrate AWS Identity and Access Management with AWS Organizations. 

## Enabling trusted access with IAM
<a name="integrate-enable-ta-iam"></a>

When you enable root access management, trusted access is enabled for IAM in AWS Organizations. 

## Disabling trusted access with IAM
<a name="integrate-disable-ta-iam"></a>

For information about the permissions needed to disable trusted access, see [Permissions required to disable trusted access](orgs_integrate_services.md#orgs_trusted_access_disable_perms).

Only an administrator in the AWS Organizations management account can disable trusted access with AWS Identity and Access Management.

You can only disable trusted access using the Organizations tools.

You can disable trusted access by using either the AWS Organizations console, by running an Organizations AWS CLI command, or by calling an Organizations API operation in one of the AWS SDKs.

------
#### [ AWS Management Console ]

**To disable trusted service access using the Organizations console**

1. Sign in to the [AWS Organizations console](https://console.aws.amazon.com/organizations/v2). You must sign in as an IAM user, assume an IAM role, or sign in as the root user ([not recommended](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#lock-away-credentials)) in the organization’s management account.

1. In the navigation pane, choose **Services**.

1. Choose **AWS Identity and Access Management** in the list of services.

1. Choose **Disable trusted access**.

1. In the **Disable trusted access for AWS Identity and Access Management** dialog box, type **disable** to confirm, and then choose **Disable trusted access**.

1. If you are the administrator of only AWS Organizations, tell the administrator of AWS Identity and Access Management that they can now disable that service from working with AWS Organizations using the service console or tools .

------
#### [ AWS CLI, AWS API ]

**To disable trusted service access using the Organizations CLI/SDK**  
You can use the following AWS CLI commands or API operations to disable trusted service access:
+ AWS CLI: [disable-aws-service-access](https://docs.aws.amazon.com/cli/latest/reference/organizations/disable-aws-service-access.html)

  Run the following command to disable AWS Identity and Access Management as a trusted service with Organizations.

  ```
  $ aws organizations disable-aws-service-access \
      --service-principal iam.amazonaws.com
  ```

  This command produces no output when successful.
+ AWS API: [DisableAWSServiceAccess](https://docs.aws.amazon.com/organizations/latest/APIReference/API_DisableAWSServiceAccess.html)

------

## Enabling a delegated administrator account for IAM
<a name="integrate-enable-da-iam"></a>

When you designate a member account as a delegated administrator for the organization, users and roles from that account can perform privileged tasks on member accounts that otherwise can be performed only by users or roles in the organization's management account. For more information, see [Perform a privileged task on an Organizations member account](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_root-user-privileged-task.html) in the IAM User Guide.

Only an administrator in the organization management account can configure a delegated administrator for IAM.

You can specify a delegated administrator account from the IAM console or API, or by using the Organizations CLI or SDK operation. 

## Disabling a delegated administrator for IAM
<a name="integrate-disable-da-iam"></a>

Only an administrator in either the Organizations management account or the IAM delegated admin account can remove a delegated administrator account from the organization. You can disable delegated administration using the Organizations `DeregisterDelegatedAdministrator` CLI or SDK operation.