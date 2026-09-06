

# AWS Managed Services (AMS) Self-Service Reporting (SSR) and AWS Organizations
<a name="services-that-can-integrate-managed-services"></a>

[AWS Managed Services (AMS) Self-Service Reporting (SSR)](https://aws.amazon.com/managed-services) collects data from various native AWS services and provides access to reports on major AMS offerings. SSR provides the information that you can use to support operations, configuration management, asset management, security management, and compliance.

After you integrate with AWS Organizations, you can enable Aggregated self-service reporting (SSR). This is an AMS feature that allows Advanced and Accelerate customers to view their existing Self-service reports aggregated at the organization level, cross-account. This gives you visibility into key operational metrics such as patch compliance, backup coverage, and incidents across all AMS-managed accounts within AWS Organizations.

Use the following information to help you integrate AWS Managed Services (AMS) Self-Service Reporting (SSR) with AWS Organizations.



## Service-linked roles created when you enable integration
<a name="integrate-enable-slr-managed-services"></a>

The following [service-linked role](https://docs.aws.amazon.com/IAM/latest/UserGuide/using-service-linked-roles.html) is automatically created in your organization's management account when you enable trusted access. This role allows AMS to perform supported operations within your organization's accounts in your organization.

You can delete or modify this role only if you disable trusted access between AMS and Organizations, or if you remove the member account from the organization.
+ `AWSServiceRoleForManagedServices_SelfServiceReporting`

## Service principals used by the service-linked roles
<a name="integrate-enable-svcprin-managed-services"></a>

The service-linked role in the previous section can be assumed only by the service principals authorized by the trust relationships defined for the role. The service-linked roles used by AMS grant access to the following service principals:
+ `selfservicereporting.managedservices.amazonaws.com`

## Enabling trusted access with AMS
<a name="integrate-enable-ta-managed-services"></a>

For information about the permissions needed to enable trusted access, see [Permissions required to enable trusted access](orgs_integrate_services.md#orgs_trusted_access_perms).

You can enable trusted access by running a Organizations AWS CLI command, or by calling an Organizations API operation in one of the AWS SDKs.

------
#### [ AWS CLI, AWS API ]

**To enable trusted service access using the Organizations CLI/SDK**  
Use the following AWS CLI commands or API operations to enable trusted service access:
+ AWS CLI: [enable-aws-service-access](https://docs.aws.amazon.com/cli/latest/reference/organizations/enable-aws-service-access.html)

  Run the following command to enable AWS Managed Services (AMS) Self-Service Reporting (SSR) as a trusted service with Organizations.

  ```
  $ aws organizations enable-aws-service-access \
      --service-principal selfservicereporting.managedservices.amazonaws.com
  ```

  This command produces no output when successful.
+ AWS API: [EnableAWSServiceAccess](https://docs.aws.amazon.com/organizations/latest/APIReference/API_EnableAWSServiceAccess.html)

------

## Disabling trusted access with AMS
<a name="integrate-disable-ta-managed-services"></a>

For information about the permissions needed to disable trusted access, see [Permissions required to disable trusted access](orgs_integrate_services.md#orgs_trusted_access_disable_perms).

You can only disable trusted access using the Organizations tools.

You can disable trusted access by running a Organizations AWS CLI command, or by calling an Organizations API operation in one of the AWS SDKs.

------
#### [ AWS CLI, AWS API ]

**To disable trusted service access using the Organizations CLI/SDK**  
Use the following AWS CLI commands or API operations to disable trusted service access:
+ AWS CLI: [disable-aws-service-access](https://docs.aws.amazon.com/cli/latest/reference/organizations/disable-aws-service-access.html)

  Run the following command to disable AWS Managed Services (AMS) Self-Service Reporting (SSR) as a trusted service with Organizations.

  ```
  $ aws organizations disable-aws-service-access \
      --service-principal selfservicereporting.managedservices.amazonaws.com
  ```

  This command produces no output when successful.
+ AWS API: [DisableAWSServiceAccess](https://docs.aws.amazon.com/organizations/latest/APIReference/API_DisableAWSServiceAccess.html)

------

## Enabling a delegated administrator account for AMS
<a name="integrate-enable-da-managed-services"></a>

Delegated administrator accounts can view AMS reports (such as patch and backup) across all the accounts in a single aggregated view in the AMS console.

You can add a delegated administrator using either the AMS console or API, or by using the Organizations `RegisterDelegatedAdministrator` CLI or SDK operation.

## Disabling a delegated administrator for AMS
<a name="integrate-disable-da-managed-services"></a>

Only an administrator in the organization management account can configure a delegated administrator for AMS.

You can remove the delegated administrator using either the AMS console or API, or by using the Organizations `DeregisterDelegatedAdministrator` CLI or SDK operation.