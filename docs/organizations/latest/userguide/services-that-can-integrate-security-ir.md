

# AWS Security Incident Response and AWS Organizations
<a name="services-that-can-integrate-security-ir"></a>

AWS Security Incident Response is a security service that provides 24/7, live, human-assisted security incident support to help customers respond rapidly to cybersecurity incidents such as credential theft and ransomware attacks. By integrating with Organizations you enable security coverage for your entire organization. For more information, see [ Managing AWS Security Incident Response accounts with AWS Organizations](https://docs.aws.amazon.com/security-ir/latest/userguide/security-ir-organizations.html) in the *Security Incident Response User Guide*. 

Use the following information to help you integrate AWS Security Incident Response with AWS Organizations.



## Service-linked roles created when you enable integration
<a name="integrate-enable-slr-security-ir"></a>

The following service-linked roles are automatically created in your organization's management account when you enable trusted access. 
+ `AWSServiceRoleForSecurityIncidentResponse` - used for creating Security Incident Response membership - your subscription to the service through AWS Organizations.
+ `AWSServiceRoleForSecurityIncidentResponse_Triage` - used only when you enable the triage feature during sign-up.

## Expected `CreateServiceLinkedRole` events in AWS CloudTrail
<a name="expected-createservicelinkedrole-events"></a>

To deliver new features and to make sure that required resources remain correctly configured, AWS Security Incident Response periodically updates the service's underlying infrastructure. Each update triggers a deployment that creates the required service-linked role. If the role already exists, the `CreateServiceLinkedRole` call returns an exception that indicates the role is already present. This exception is expected and handled by the service, and the deployment continues normally.

As a result, you might see `InvalidInputException` entries for `CreateServiceLinkedRole` in your CloudTrail event history. These entries are expected behavior, have no impact on your accounts, and require no action.

## Service principals used by Security Incident Response
<a name="integrate-enable-svcprin-security-ir"></a>

 The service-linked roles in the previous section can be assumed only by the service principals authorized by the trust relationships defined for the role. The service-linked roles used by Security Incident Response grant access to the following service principal: 
+ `security-ir.amazonaws.com`

## Enabling trusted access to Security Incident Response
<a name="integrate-enable-ta-security-ir"></a>

Enabling trusted access to Security Incident Response allows the service to keep track of your organization's structure and ensure that all accounts in the organization have active security incident coverage. It also allows the service to use a service-linked role in member accounts for triaging capabilities when you enable the triage feature.

For information about the permissions needed to enable trusted access, see [Permissions required to enable trusted access](orgs_integrate_services.md#orgs_trusted_access_perms).

You can enable trusted access using either the AWS Security Incident Response console or the AWS Organizations console.

**Important**  
We strongly recommend that whenever possible, you use the AWS Security Incident Response console or tools to enable integration with Organizations. This lets AWS Security Incident Response perform any configuration that it requires, such as creating resources needed by the service. Proceed with these steps only if you can’t enable integration using the tools provided by AWS Security Incident Response. For more information, see [this note](orgs_integrate_services.md#important-note-about-integration).   
If you enable trusted access by using the AWS Security Incident Response console or tools then you don’t need to complete these steps.

Organizations automatically enables the Organizations trusted access when you use the Security Incident Response console for setup and management. If you use the Security Incident Response CLI/SDK then you have to manually enable trusted access by using the [EnableAWSServiceAccess API](https://docs.aws.amazon.com/organizations/latest/APIReference/API_EnableAWSServiceAccess.html). To learn how to enable trusted access through the Security Incident Response console, see [ Enabling trusted access for AWS Account Management](https://docs.aws.amazon.com/security-ir/latest/userguide/using-orgs-trusted-access.html) in the *Security Incident Response User Guide*.

You can enable trusted access by using either the AWS Organizations console, by running a AWS CLI command, or by calling an API operation in one of the AWS SDKs.

------
#### [ AWS Management Console ]

**To enable trusted service access using the Organizations console**

1. Sign in to the [AWS Organizations console](https://console.aws.amazon.com/organizations/v2). You must sign in as an IAM user, assume an IAM role, or sign in as the root user ([not recommended](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#lock-away-credentials)) in the organization’s management account.

1. In the navigation pane, choose **Services**.

1. Choose **AWS Security Incident Response** in the list of services.

1. Choose **Enable trusted access**.

1. In the **Enable trusted access for AWS Security Incident Response** dialog box, type **enable** to confirm, and then choose **Enable trusted access**.

1. If you are the administrator of only AWS Organizations, tell the administrator of AWS Security Incident Response that they can now enable that service to work with AWS Organizations from the service console .

------
#### [ AWS CLI, AWS API ]

**To enable trusted service access using the OrganizationsCLI/SDK**  
Use the following AWS CLI commands or API operations to enable trusted service access:
+ AWS CLI: [enable-aws-service-access](https://docs.aws.amazon.com/cli/latest/reference/organizations/enable-aws-service-access.html)

  Run the following command to enable AWS Security Incident Response as a trusted service with Organizations.

  ```
  $ aws organizations enable-aws-service-access \ 
      --service-principal security-ir.amazonaws.com
  ```

  This command produces no output when successful.
+ AWS API: [EnableAWSServiceAccess](https://docs.aws.amazon.com/organizations/latest/APIReference/API_EnableAWSServiceAccess.html)

------

## Disabling trusted access with Security Incident Response
<a name="integrate-disable-ta-security-ir"></a>

Only an administrator in the Organizations management account can disable trusted access with Security Incident Response. 

You can only disable trusted access using the Organizations tools.

You can disable trusted access by using either the AWS Organizations console, by running an Organizations AWS CLI command, or by calling an Organizations API operation in one of the AWS SDKs.

------
#### [ AWS Management Console ]

**To disable trusted service access using the Organizations console**

1. Sign in to the [AWS Organizations console](https://console.aws.amazon.com/organizations/v2). You must sign in as an IAM user, assume an IAM role, or sign in as the root user ([not recommended](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#lock-away-credentials)) in the organization’s management account.

1. In the navigation pane, choose **Services**.

1. Choose **AWS Security Incident Response** in the list of services.

1. Choose **Disable trusted access**.

1. In the **Disable trusted access for AWS Security Incident Response** dialog box, type **disable** to confirm, and then choose **Disable trusted access**.

1. If you are the administrator of only AWS Organizations, tell the administrator of AWS Security Incident Response that they can now disable that service from working with AWS Organizations using the service console or tools .

------
#### [ AWS CLI, AWS API ]

**To disable trusted service access using the Organizations CLI/SDK**  
You can use the following AWS CLI commands or API operations to disable trusted service access:
+ AWS CLI: [disable-aws-service-access](https://docs.aws.amazon.com/cli/latest/reference/organizations/disable-aws-service-access.html)

  Run the following command to disable AWS Security Incident Response as a trusted service with Organizations.

  ```
  $ aws organizations disable-aws-service-access \
      --service-principal security-ir.amazonaws.com
  ```

  This command produces no output when successful.
+ AWS API: [DisableAWSServiceAccess](https://docs.aws.amazon.com/organizations/latest/APIReference/API_DisableAWSServiceAccess.html)

------

## Enabling a delegated administrator account for Security Incident Response
<a name="integrate-enable-da-security-ir"></a>

When you designate a member account as a delegated administrator for the organization, users and roles from that account can perform administrative actions for Security Incident Response that otherwise can be performed only by users or roles in the organization's management account. This helps you to separate management of the organization from management of Security Incident Response. For more information, see [ Managing AWS Security Incident Response accounts with AWS Organizations](https://docs.aws.amazon.com/security-ir/latest/userguide/security-ir-organizations.html) in the *Security Incident Response User Guide*.

**Minimum permissions**  
Only a user or role in the Organizations management account can configure a member account as a delegated administrator for Security Incident Response in the organization

To learn how to configure a delegated administrator through the Security Incident Response console, see [ Designating a delegated Security Incident Response administrator account ](https://docs.aws.amazon.com/security-ir/latest/userguide/delegated-admin-designate.html) in the *Security Incident Response User Guide*.

------
#### [ AWS CLI, AWS API ]

If you want to configure a delegated administrator account using the AWS CLI or one of the AWS SDKs, you can use the following commands:
+ AWS CLI: 

  ```
  $ aws organizations register-delegated-administrator \
      --account-id 123456789012 \
      --service-principal security-ir.amazonaws.com
  ```
+ AWS SDK: Call the Organizations `RegisterDelegatedAdministrator` operation and the member account's ID number and identify the account service `security-ir.amazonaws.com` as parameters. 

------

## Disabling a delegated administrator for Security Incident Response
<a name="integrate-disable-da-security-ir"></a>

**Important**  
If membership was created from the delegated administrator account, deregistering the delegated administrator is a destructive action and will cause service disruption. To re-register DA:   
Sign in to the Security Incident Response console at https://console.aws.amazon.com/security-ir/home\#/membership/settings
Cancel membership from the service console. Membership remains active until the end of billing cycle.
 Once membership is cancelled disable service access through the Organizations console, CLI or SDK. 

 Only an administrator in the Organizations management account can remove a delegated administrator for Security Incident Response. You can remove the delegated administrator using the Organizations `DeregisterDelegatedAdministrator` CLI or SDK operation.