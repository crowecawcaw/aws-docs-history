

# AWS CloudTrail and AWS Organizations
<a name="services-that-can-integrate-cloudtrail"></a>

AWS CloudTrail is an AWS service that helps you enable governance, compliance, and operational and risk auditing of your AWS account. Using AWS CloudTrail, a user in a management account can create an organization trail that logs all events for all AWS accounts in that organization. Organization trails are automatically applied to all member accounts in the organization. Member accounts can see the organization trail, but can't modify or delete it. By default, member accounts don't have access to the log files for the organization trail in the Amazon S3 bucket. This helps you uniformly apply and enforce your event logging strategy across the accounts in your organization.

For more information, see [ Creating a Trail for an Organization](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/creating-trail-organization.html) in the *AWS CloudTrail User Guide*. 

Use the following information to help you integrate AWS CloudTrail with AWS Organizations.



## Service-linked roles created when you enable integration
<a name="integrate-enable-slr-cloudtrail"></a>

The following [service-linked role](https://docs.aws.amazon.com/IAM/latest/UserGuide/using-service-linked-roles.html) is automatically created in your organization's management account when you enable trusted access. This role allows CloudTrail to perform supported operations within your organization's accounts in your organization.

You can delete or modify this role only if you disable trusted access between CloudTrail and Organizations, or if you remove the member account from the organization.
+ `AWSServiceRoleForCloudTrail`

## Service principals used by the service-linked roles
<a name="integrate-enable-svcprin-cloudtrail"></a>

The service-linked role in the previous section can be assumed only by the service principals authorized by the trust relationships defined for the role. The service-linked roles used by CloudTrail grant access to the following service principals:
+ `cloudtrail.amazonaws.com`

## Enabling trusted access with CloudTrail
<a name="integrate-enable-ta-cloudtrail"></a>

For information about the permissions needed to enable trusted access, see [Permissions required to enable trusted access](orgs_integrate_services.md#orgs_trusted_access_perms).

If you enable trusted access by creating a trail from the AWS CloudTrail console, trusted access is configured automatically for you (recommended). You can also enable trusted access using the AWS Organizations console. You must sign in with your AWS Organizations management account to create an organization trail.

If you choose to create an organization trail using the AWS CLI or the AWS API, you must manually configure trusted access. For more information, see [ Enabling CloudTrail as a trusted service in AWS Organizations](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-create-and-update-an-organizational-trail-by-using-the-aws-cli.html#cloudtrail-create-organization-trail-by-using-the-cli-enable-trusted-service) in the *AWS CloudTrail User Guide.*

**Important**  
 We strongly recommend that whenever possible, you use the AWS CloudTrail console or tools to enable integration with Organizations. 

You can enable trusted access by running a Organizations AWS CLI command, or by calling an Organizations API operation in one of the AWS SDKs.

------
#### [ AWS CLI, AWS API ]

**To enable trusted service access using the Organizations CLI/SDK**  
Use the following AWS CLI commands or API operations to enable trusted service access:
+ AWS CLI: [enable-aws-service-access](https://docs.aws.amazon.com/cli/latest/reference/organizations/enable-aws-service-access.html)

  Run the following command to enable AWS CloudTrail as a trusted service with Organizations.

  ```
  $ aws organizations enable-aws-service-access \
      --service-principal cloudtrail.amazonaws.com
  ```

  This command produces no output when successful.
+ AWS API: [EnableAWSServiceAccess](https://docs.aws.amazon.com/organizations/latest/APIReference/API_EnableAWSServiceAccess.html)

------

## Disabling trusted access with CloudTrail
<a name="integrate-disable-ta-cloudtrail"></a>

For information about the permissions needed to disable trusted access, see [Permissions required to disable trusted access](orgs_integrate_services.md#orgs_trusted_access_disable_perms).

 AWS CloudTrail requires trusted access with AWS Organizations to work with organization trails and organization event data stores. If you disable trusted access using AWS Organizations while you're using AWS CloudTrail, all organization trails for member accounts are deleted because CloudTrail can't access the organization. All management account organization trails and organization event data stores are converted to account-level trails and event data stores. The `AWSServiceRoleForCloudTrail` role created for integration between CloudTrail and AWS Organizations stays in the account. If you re-enable trusted access, CloudTrail will not take action on existing trails and event data stores. The management account must update any account-level trails and event data stores to apply them to the organization. 

To convert an account-level trail or event data store to an organization trail or organization event data store, do the following:
+ From the CloudTrail console, update the [trail](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-update-a-trail-console.html) or [event data store](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/query-event-data-store-update.html) and choose the **Enable for all accounts in my organization** option.
+ From the AWS CLI, do the following:
  + To update a trail, run the [update-trail](https://docs.aws.amazon.com/cli/latest/reference/cloudtrail/update-trail.html) command and include the `--is-organization-trail` parameter.
  + To update an event data store, run the [update-event-data-store](https://docs.aws.amazon.com/cli/latest/reference/cloudtrail/update-event-data-store.html) command and include the `--organization-enabled` parameter.

Only an administrator in the AWS Organizations management account can disable trusted access with AWS CloudTrail. You can disable trusted access only with the Organizations tools, using either the AWS Organizations console, running an Organizations AWS CLI command, or calling an Organizations API operation in one of the AWS SDKs.

You can disable trusted access by using either the AWS Organizations console, by running an Organizations AWS CLI command, or by calling an Organizations API operation in one of the AWS SDKs.

------
#### [ AWS Management Console ]

**To disable trusted service access using the Organizations console**

1. Sign in to the [AWS Organizations console](https://console.aws.amazon.com/organizations/v2). You must sign in as an IAM user, assume an IAM role, or sign in as the root user ([not recommended](https://docs.aws.amazon.com/IAM/latest/UserGuide/best-practices.html#lock-away-credentials)) in the organization’s management account.

1. In the navigation pane, choose **Services**.

1. Choose **AWS CloudTrail** in the list of services.

1. Choose **Disable trusted access**.

1. In the **Disable trusted access for AWS CloudTrail** dialog box, type **disable** to confirm, and then choose **Disable trusted access**.

1. If you are the administrator of only AWS Organizations, tell the administrator of AWS CloudTrail that they can now disable that service from working with AWS Organizations using the service console or tools .

------
#### [ AWS CLI, AWS API ]

**To disable trusted service access using the Organizations CLI/SDK**  
You can use the following AWS CLI commands or API operations to disable trusted service access:
+ AWS CLI: [disable-aws-service-access](https://docs.aws.amazon.com/cli/latest/reference/organizations/disable-aws-service-access.html)

  Run the following command to disable AWS CloudTrail as a trusted service with Organizations.

  ```
  $ aws organizations disable-aws-service-access \
      --service-principal cloudtrail.amazonaws.com
  ```

  This command produces no output when successful.
+ AWS API: [DisableAWSServiceAccess](https://docs.aws.amazon.com/organizations/latest/APIReference/API_DisableAWSServiceAccess.html)

------

## Enabling a delegated administrator account for CloudTrail
<a name="integrate-enable-da-cloudtrail"></a>

When you use CloudTrail with Organizations, you can register any account within the organization to act as a CloudTrail delegated administrator to manage the organization's trails and event data stores on behalf of the organization. A delegated administrator is a member account in an organization that can perform the same administrative tasks in CloudTrail as the management account. 

**Minimum permissions**  
Only an administrator in the Organizations management account can register a delegated administrator for CloudTrail.

You can register a delegated administrator account using the CloudTrail console, or by using the Organizations `RegisterDelegatedAdministrator` CLI or SDK operation. To register a delegated administrator using the CloudTrail console, see [ Add a CloudTrail delegated administrator](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-add-delegated-administrator.html). 

## Disabling a delegated administrator for CloudTrail
<a name="integrate-disable-da-cloudtrail"></a>

 Only an administrator in the Organizations management account can remove a delegated administrator for CloudTrail. You can remove the delegated administrator using either the CloudTrail console, or by using the Organizations `DeregisterDelegatedAdministrator` CLI or SDK operation. For information on how to remove a delegated administrator using the CloudTrail console, see [Remove a CloudTrail delegated administrator](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-remove-delegated-administrator.html) . 