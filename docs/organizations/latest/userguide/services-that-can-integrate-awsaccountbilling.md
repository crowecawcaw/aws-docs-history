

# AWS Billing and Cost Management and AWS Organizations
<a name="services-that-can-integrate-awsaccountbilling"></a>

AWS Billing and Cost Management provides a suite of features to help you set up your billing, retrieve and pay invoices, and analyze, organize, plan, and optimize your costs. When you use Billing and Cost Management with AWS Organizations you allow [ split cost allocation data](https://docs.aws.amazon.com/cur/latest/userguide/split-cost-allocation-data.html) to retrieve AWS Organizations information, if applicable, and collect telemetry data for the split cost allocation data services that you opted into.

Use the following information to help you integrate AWS Billing and Cost Management with AWS Organizations.



## Service-linked roles created when you enable integration
<a name="integrate-enable-slr-awsaccountbilling"></a>

The following [service-linked role](https://docs.aws.amazon.com/IAM/latest/UserGuide/using-service-linked-roles.html) is automatically created in your organization's management account when you enable trusted access. This role allows Billing and Cost Management to perform supported operations within your organization's accounts in your organization.

You can delete or modify this role only if you disable trusted access between Billing and Cost Management and Organizations, or if you remove the member account from the organization.

For more information, see [ Service-linked role permissions for Billing and Cost Management ](https://docs.aws.amazon.com/awsaccountbilling/latest/aboutv2/security_iam_service-with-iam.html#security_iam_service-with-iam-roles-service-linked) in the *Billing and Cost Management User Guide*. 
+ `AWSServiceRoleForSplitCostAllocationData`

## Service principals used by Billing and Cost Management
<a name="integrate-enable-svcprin-awsaccountbilling"></a>

The service-linked role in the previous section can be assumed only by the service principals authorized by the trust relationships defined for the role. The service-linked roles used by Billing and Cost Management grant access to the following service principals:

Billing and Cost Management uses the ` billing-cost-management.amazonaws.com` service principal.

## Enabling trusted access with Billing and Cost Management
<a name="integrate-enable-ta-awsaccountbilling"></a>

For information about the permissions needed to enable trusted access, see [Permissions required to enable trusted access](orgs_integrate_services.md#orgs_trusted_access_perms).

With trusted access enabled via management account, customers can take advantage of the split cost allocation data feature under Billing and Cost Management. When customers enable split cost allocation data for Amazon Elastic Kubernetes Service with Amazon Managed Service for Prometheus, trusted access is invoked to create service-linked roles for all member accounts within the Organization. This allows split cost allocation data to collect telemetry data from customers' Amazon Managed Service for Prometheus work spaces and perform cost allocation based on those metrics. 

You can only enable trusted access using the Organizations tools.

You can enable trusted access by running a Organizations AWS CLI command, or by calling an Organizations API operation in one of the AWS SDKs.

------
#### [ AWS CLI, AWS API ]

**To enable trusted service access using the Organizations CLI/SDK**  
Use the following AWS CLI commands or API operations to enable trusted service access:
+ AWS CLI: [enable-aws-service-access](https://docs.aws.amazon.com/cli/latest/reference/organizations/enable-aws-service-access.html)

  Run the following command to enable AWS Billing and Cost Management as a trusted service with Organizations.

  ```
  $ aws organizations enable-aws-service-access \
      --service-principal  billing-cost-management.amazonaws.com
  ```

  This command produces no output when successful.
+ AWS API: [EnableAWSServiceAccess](https://docs.aws.amazon.com/organizations/latest/APIReference/API_EnableAWSServiceAccess.html)

------

## Disabling trusted access
<a name="integrate-disable-ta-awsaccountbilling"></a>

For information about the permissions needed to disable trusted access, see [Permissions required to disable trusted access](orgs_integrate_services.md#orgs_trusted_access_disable_perms).

You can only disable trusted access using the Organizations tools.

You can disable trusted access by running a Organizations AWS CLI command, or by calling an Organizations API operation in one of the AWS SDKs.

------
#### [ AWS CLI, AWS API ]

**To disable trusted service access using the Organizations CLI/SDK**  
Use the following AWS CLI commands or API operations to disable trusted service access:
+ AWS CLI: [disable-aws-service-access](https://docs.aws.amazon.com/cli/latest/reference/organizations/disable-aws-service-access.html)

  Run the following command to disable AWS Billing and Cost Management as a trusted service with Organizations.

  ```
  $ aws organizations disable-aws-service-access \
      --service-principal  billing-cost-management.amazonaws.com
  ```

  This command produces no output when successful.
+ AWS API: [DisableAWSServiceAccess](https://docs.aws.amazon.com/organizations/latest/APIReference/API_DisableAWSServiceAccess.html)

------