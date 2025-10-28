# Enable Tooling blueprint

The tooling blueprint creates resources for the project, including IAM user roles,
security groups, and Amazon SageMaker unified domains.

You can perform the following procedure to enable the Tooling blueprint.

1. Navigate to the Amazon SageMaker management console at [https://console.aws.amazon.com/datazone](https://console.aws.amazon.com/datazone "https://console.aws.amazon.com/datazone") and use the region selector
   in the top navigation bar to choose the appropriate AWS Region.
2. Choose **View domains** and choose the domain’s name from the
   list. The name is a hyperlink.
3. On the domain's details page, navigate to the **Blueprints**
   tab.
4. In the Tooling blueprint section, choose **Enable** and then
   specify the following configurations:
   - Provisioning role - Amazon SageMaker Unified Studio uses this role to provision and manage
     resources defined in the selected blueprints in your account.
   - Manage access role - this role grants Amazon SageMaker Unified Studio permissions to
     publish, grant access, and revoke access to Amazon SageMaker Lakehouse,
     AWS Glue Data Catalog and Amazon Redshift data. It also grants
     Amazon SageMaker Unified Studio to publish and manage subscriptions on Amazon SageMaker
     Catalog data and AI assets.
   - Query execution role - this role is used while running a query
     execution. AWS LakeFormation assumes this role to vend credentials
     needed by Amazon Athena during query execution.
   - Amazon S3 bucket for projects - Amazon SageMaker Unified Studio requires an S3 bucket for
     projects in your AWS account.
   - Virtual private cloud (VPC) - Select a VPC in which to provision your
     Amazon SageMaker Unified Studio domain. VPCs tagged with Amazon SageMaker Unified Studio should be correctly
     configured.
   - Data encryption - your data is encrypted by default with a key that
     AWS owns and manages for you. To choose a different key, customize
     your encryption settings.
   - User role policy - Amazon SageMaker Unified Studio creates IAM roles for project users to
     perform data analytics, AI, and ML actions. You can attach your own
     AWS IAM policies to the role rather than using the default
     system-managed policy. This provides more granular control over
     permissions but requires knowledge of IAM policy configuration. The IAM
     policy must include all necessary permissions required for the service
     to function properly.
   - Authorized domain units - domain units where projects can access
     resources defined by the blueprints.

5. Once all the configuration settings have been specified, choose **Enable
   blueprint**.
