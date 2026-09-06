

# AWS Resilience Hub and AWS Organizations
<a name="services-that-can-integrate-resilience-hub"></a>

AWS Resilience Hub helps you define, validate, and track the resilience of your applications so that you can avoid unnecessary downtime caused by software, infrastructure, or operational disruptions.

When you integrate Resilience Hub with AWS Organizations, the management account enables trusted access and designates a delegated administrator account. With the delegated administrator account, you get organization-wide visibility into resilience posture and aggregated dashboards across member accounts.

For more information, see [AWS Organizations integration](https://docs.aws.amazon.com/resilience-hub/latest/userguide/next-gen-organizations.html) in the *AWS Resilience Hub User Guide*.

Use the following information to help you integrate AWS Resilience Hub with AWS Organizations.



## Service-linked roles created when you enable integration
<a name="integrate-enable-slr-resilience-hub"></a>

The following [service-linked role](https://docs.aws.amazon.com/IAM/latest/UserGuide/using-service-linked-roles.html) is automatically created in your organization's management account when you enable trusted access. This role allows Resilience Hub to perform supported operations within your organization's accounts in your organization.

You can delete or modify this role only if you disable trusted access between Resilience Hub and Organizations, or if you remove the member account from the organization.

For more information about how Resilience Hub uses this role, see [Service-Linked Roles](https://docs.aws.amazon.com/resilience-hub/latest/userguide/next-gen-org-slrs.html) in the *AWS Resilience Hub User Guide*.
+ `AWSServiceRoleForResilienceHub`

## Service principals used by the service-linked roles
<a name="integrate-enable-svcprin-resilience-hub"></a>

The service-linked role in the previous section can be assumed only by the service principals authorized by the trust relationships defined for the role. The service-linked roles used by Resilience Hub grant access to the following service principals:
+ `resiliencehub.amazonaws.com`

## To enable trusted access with AWS Resilience Hub
<a name="integrate-enable-ta-resilience-hub"></a>

For information about the permissions needed to enable trusted access, see [Permissions required to enable trusted access](orgs_integrate_services.md#orgs_trusted_access_perms).

Resilience Hub requires trusted access to AWS Organizations before you can designate a member account to be the delegated administrator for your organization.

You can only enable trusted access using AWS Resilience Hub.

**To enable trusted access using the Resilience Hub console**  
For instructions on enabling trusted access, see [Setting up AWS Organizations integration](https://docs.aws.amazon.com/resilience-hub/latest/userguide/next-gen-delegated-admin-setup.html) in the *AWS Resilience Hub User Guide*.

You can enable trusted access by running a Organizations AWS CLI command, or by calling an Organizations API operation in one of the AWS SDKs.

------
#### [ AWS CLI, AWS API ]

**To enable trusted service access using the Organizations CLI/SDK**  
Use the following AWS CLI commands or API operations to enable trusted service access:
+ AWS CLI: [enable-aws-service-access](https://docs.aws.amazon.com/cli/latest/reference/organizations/enable-aws-service-access.html)

  Run the following command to enable AWS Resilience Hub as a trusted service with Organizations.

  ```
  $ aws organizations enable-aws-service-access \
      --service-principal resiliencehub.amazonaws.com
  ```

  This command produces no output when successful.
+ AWS API: [EnableAWSServiceAccess](https://docs.aws.amazon.com/organizations/latest/APIReference/API_EnableAWSServiceAccess.html)

------

## To disable trusted access with Resilience Hub
<a name="integrate-disable-ta-resilience-hub"></a>

For information about the permissions needed to disable trusted access, see [Permissions required to disable trusted access](orgs_integrate_services.md#orgs_trusted_access_disable_perms).

Only an administrator in the AWS Organizations management account can disable trusted access with AWS Resilience Hub.

You can only disable trusted access using the Organizations tools.

You can disable trusted access by running a Organizations AWS CLI command, or by calling an Organizations API operation in one of the AWS SDKs.

------
#### [ AWS CLI, AWS API ]

**To disable trusted service access using the Organizations CLI/SDK**  
Use the following AWS CLI commands or API operations to disable trusted service access:
+ AWS CLI: [disable-aws-service-access](https://docs.aws.amazon.com/cli/latest/reference/organizations/disable-aws-service-access.html)

  Run the following command to disable AWS Resilience Hub as a trusted service with Organizations.

  ```
  $ aws organizations disable-aws-service-access \
      --service-principal resiliencehub.amazonaws.com
  ```

  This command produces no output when successful.
+ AWS API: [DisableAWSServiceAccess](https://docs.aws.amazon.com/organizations/latest/APIReference/API_DisableAWSServiceAccess.html)

------

## To enable a delegated administrator account for Resilience Hub
<a name="integrate-enable-da-resilience-hub"></a>

With the delegated administrator account, you get organization-wide visibility into resilience posture and aggregated dashboards across member accounts without signing in to individual accounts.

**Minimum permissions**  
Only a user or role in the Organizations management account with the following permissions can configure a member account as a delegated administrator for Resilience Hub in the organization:  
`organizations:RegisterDelegatedAdministrator`
`organizations:EnableAWSServiceAccess`

For instructions on enabling a delegated administrator account for Resilience Hub, see [Setting up AWS Organizations integration](https://docs.aws.amazon.com/resilience-hub/latest/userguide/next-gen-delegated-admin-setup.html) in the *AWS Resilience Hub User Guide*.

------
#### [ AWS CLI, AWS API ]

To configure a delegated administrator account using the AWS CLI or one of the AWS SDKs, use the following commands:
+ AWS CLI: 

  ```
  $ aws organizations register-delegated-administrator \
      --account-id 123456789012 \
      --service-principal resiliencehub.amazonaws.com
  ```
+ AWS SDK: To register the delegated administrator, call the Organizations `RegisterDelegatedAdministrator` operation. Provide the member account's ID and the service principal `resiliencehub.amazonaws.com` as parameters. 

------

## To disable a delegated administrator for Resilience Hub
<a name="integrate-disable-da-resilience-hub"></a>

Only an administrator in the Organizations management account can remove a delegated administrator for Resilience Hub. You can disable the delegated administrator using the Organizations `DeregisterDelegatedAdministrator` CLI or SDK operation.

------
#### [ AWS CLI, AWS API ]

To remove a delegated administrator account using the AWS CLI or one of the AWS SDKs, use the following commands:
+ AWS CLI: 

  ```
  $ aws organizations deregister-delegated-administrator \
      --account-id 123456789012 \
      --service-principal resiliencehub.amazonaws.com
  ```
+ AWS SDK: To remove the delegated administrator, call the Organizations `DeregisterDelegatedAdministrator` operation. Provide the member account's ID and the service principal `resiliencehub.amazonaws.com` as parameters. 

------