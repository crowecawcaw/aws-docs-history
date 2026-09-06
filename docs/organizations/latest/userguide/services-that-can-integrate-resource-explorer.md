

# AWS Resource Explorer and AWS Organizations
<a name="services-that-can-integrate-resource-explorer"></a>

AWS Resource Explorer is a resource search and discovery service. With Resource Explorer, you can explore your resources, such as Amazon Elastic Compute Cloud instances, Amazon Kinesis Data Streams, or Amazon DynamoDB tables, using an internet search engine-like experience. You can search for your resources using resource metadata such as names, tags, and IDs. Resource Explorer works across AWS Regions in your account to simplify your cross-Region workloads.

When you integrate Resource Explorer with AWS Organizations, you can gather evidence from a broader source by including multiple AWS accounts from your organization within the scope of your assessments.

Use the following information to help you integrate AWS Resource Explorer with AWS Organizations.



## Service-linked roles created when you enable integration
<a name="integrate-enable-slr-resource-explorer"></a>

The following [service-linked role](https://docs.aws.amazon.com/IAM/latest/UserGuide/using-service-linked-roles.html) is automatically created in your organization's management account when you enable trusted access. This role allows Resource Explorer to perform supported operations within your organization's accounts in your organization.

You can delete or modify this role only if you disable trusted access between Resource Explorer and Organizations, or if you remove the member account from the organization.

For more information about how Resource Explorer uses this role, see [Using service-linked roles](https://docs.aws.amazon.com/resource-explorer/latest/userguide/security_iam_service-linked-roles.html) in the *AWS Resource Explorer Users Guide*.
+ `AWSServiceRoleForResourceExplorer`

## Service principals used by the service-linked roles
<a name="integrate-enable-svcprin-resource-explorer"></a>

The service-linked role in the previous section can be assumed only by the service principals authorized by the trust relationships defined for the role. The service-linked roles used by Resource Explorer grant access to the following service principals:
+ `resource-explorer-2.amazonaws.com`

## To enable trusted access with AWS Resource Explorer
<a name="integrate-enable-ta-resource-explorer"></a>

For information about the permissions needed to enable trusted access, see [Permissions required to enable trusted access](orgs_integrate_services.md#orgs_trusted_access_perms).

Resource Explorer requires trusted access to AWS Organizations before you can designate a member account to be the delegated administrator for your organization.

 You can enable trusted access using either the Resource Explorer console or the Organizations console. We strongly recommend that whenever possible, you use the Resource Explorer console or tools to enable integration with Organizations. This lets AWS Resource Explorer perform any configuration that it requires, such as creating resources needed by the service. 

**To enable trusted access using the Resource Explorer console**  
For instructions about enabling trusted access, see [Prerequisites to using Resource Explorer](https://docs.aws.amazon.com/resource-explorer/latest/userguide/getting-started-setting-up-prereqs.html) in the *AWS Resource Explorer User Guide*.

**Note**  
If you configure a delegated administrator using the AWS Resource Explorer console, then AWS Resource Explorer automatically enables trusted access for you.

You can enable trusted access by running a Organizations AWS CLI command, or by calling an Organizations API operation in one of the AWS SDKs.

------
#### [ AWS CLI, AWS API ]

**To enable trusted service access using the Organizations CLI/SDK**  
Use the following AWS CLI commands or API operations to enable trusted service access:
+ AWS CLI: [enable-aws-service-access](https://docs.aws.amazon.com/cli/latest/reference/organizations/enable-aws-service-access.html)

  Run the following command to enable AWS Resource Explorer as a trusted service with Organizations.

  ```
  $ aws organizations enable-aws-service-access \
      --service-principal resource-explorer-2.amazonaws.com
  ```

  This command produces no output when successful.
+ AWS API: [EnableAWSServiceAccess](https://docs.aws.amazon.com/organizations/latest/APIReference/API_EnableAWSServiceAccess.html)

------

## To disable trusted access with Resource Explorer
<a name="integrate-disable-ta-resource-explorer"></a>

For information about the permissions needed to disable trusted access, see [Permissions required to disable trusted access](orgs_integrate_services.md#orgs_trusted_access_disable_perms).

Only an administrator in the AWS Organizations management account can disable trusted access with AWS Resource Explorer.

You can disable trusted access using either the AWS Resource Explorer or the AWS Organizations tools.

**Important**  
We strongly recommend that whenever possible, you use the AWS Resource Explorer console or tools to disable integration with Organizations. This lets AWS Resource Explorer perform any clean up that it requires, such as deleting resources or access roles that are no longer needed by the service. Proceed with these steps only if you can’t disable integration using the tools provided by AWS Resource Explorer.  
If you disable trusted access by using the AWS Resource Explorer console or tools then you don’t need to complete these steps.

You can disable trusted access by running a Organizations AWS CLI command, or by calling an Organizations API operation in one of the AWS SDKs.

------
#### [ AWS CLI, AWS API ]

**To disable trusted service access using the Organizations CLI/SDK**  
Use the following AWS CLI commands or API operations to disable trusted service access:
+ AWS CLI: [disable-aws-service-access](https://docs.aws.amazon.com/cli/latest/reference/organizations/disable-aws-service-access.html)

  Run the following command to disable AWS Resource Explorer as a trusted service with Organizations.

  ```
  $ aws organizations disable-aws-service-access \
      --service-principal resource-explorer-2.amazonaws.com
  ```

  This command produces no output when successful.
+ AWS API: [DisableAWSServiceAccess](https://docs.aws.amazon.com/organizations/latest/APIReference/API_DisableAWSServiceAccess.html)

------

## Enabling a delegated administrator account for Resource Explorer
<a name="integrate-enable-da-resource-explorer"></a>

Use your delegated administrator account to create multi-account resource views and scope it to an organizational unit or your entire organization. You can share multi-account views with any account in your organization via AWS Resource Access Manager by creating resource shares. 

**Minimum permissions**  
Only a user or role in the Organizations management account with the following permission can configure a member account as a delegated administrator for Resource Explorer in the organization:  
`resource-explorer:RegisterAccount`

For instruction about enabling a delegated administrator account for Resource Explorer, see [Setting Up](https://docs.aws.amazon.com/resource-explorer/latest/userguide/getting-started-setting-up-prereqs.html) in the *AWS Resource Explorer User Guide*.

If you configure a delegated administrator using the AWS Resource Explorer console, then Resource Explorer automatically enables trusted access for you. 

------
#### [ AWS CLI, AWS API ]

If you want to configure a delegated administrator account using the AWS CLI or one of the AWS SDKs, you can use the following commands:
+ AWS CLI: 

  ```
  $ aws organizations register-delegated-administrator \
      --account-id 123456789012 \
      --service-principal resource-explorer-2.amazonaws.com
  ```
+ AWS SDK: Call the Organizations `RegisterDelegatedAdministrator` operation and the member account's ID number and identify the account service `resource-explorer-2.amazonaws.com` as parameters. 

------

## Disabling a delegated administrator for Resource Explorer
<a name="integrate-disable-da-resource-explorer"></a>

 Only an administrator in the Organizations management account or in the Resource Explorer delegated administrator account can remove a delegated administrator for Resource Explorer. You can disable trusted access using the Organizations `DeregisterDelegatedAdministrator` CLI or SDK operation. 