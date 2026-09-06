

# Enabling trusted access for S3 Storage Lens
<a name="storage_lens_with_organizations_enabling_trusted_access"></a>

By enabling trusted access, you allow Amazon S3 Storage Lens to access your AWS Organizations hierarchy, membership, and structure through AWS Organizations API operations. S3 Storage Lens then becomes a trusted service for your entire organization's structure.

Whenever a dashboard configuration is created, S3 Storage Lens creates service-linked roles in your organization's management or delegated administrator accounts. The service-linked role grants S3 Storage Lens permission to perform the following actions: 
+ Describe organizations
+ List accounts
+ Verify a list of AWS service access for the organizations
+ Get delegated administrators for the organizations



S3 Storage Lens can then ensure that it has access to collect the cross-account metrics for the accounts in your organization. For more information, see [ Using service-linked roles for Amazon S3 Storage Lens](https://docs.aws.amazon.com/AmazonS3/latest/userguide/using-service-linked-roles.html). 

After enabling trusted access, you can assign delegated administrator access to accounts in your organization. When an account is marked as a delegated administrator for a service, the account receives authorization to access all read-only organization API operations. This access provides the delegated administrator visibility to the members and structures of your organization so that they too can create S3 Storage Lens dashboards.

**Note**  
Trusted access can only be enabled by the [management account](https://docs.aws.amazon.com/managedservices/latest/userguide/management-account.html).
 Only the management account and delegated administrators can create S3 Storage Lens dashboards or configurations for your organization.