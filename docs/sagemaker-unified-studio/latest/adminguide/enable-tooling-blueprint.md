

# Enable Tooling blueprint
<a name="enable-tooling-blueprint"></a>

Before you can create projects with compute capabilities, you must enable the Tooling blueprint and configure its provisioning settings. The Tooling blueprint provisions IAM roles, security groups, and an Amazon SageMaker unified domain for each project.

To enable the Tooling blueprint, complete the following steps.

Before you begin, verify that you have the following:
+ Domain administrator access to the Amazon SageMaker Unified Studio domain
+ An AWS account with permissions to create IAM roles and manage resources

1. Navigate to the Amazon SageMaker management console at [https://console.aws.amazon.com/datazone](https://console.aws.amazon.com/datazone) and use the region selector in the top navigation bar to choose the appropriate AWS Region.

1. Choose **View domains** and choose the domain's name from the list. The name is a hyperlink.

1. On the domain's details page, navigate to the **Blueprints** tab.

1. In the Tooling blueprint section, choose **Enable** and then specify the following configurations:
   + **Provisioning role** — Amazon SageMaker Unified Studio uses this role to provision and manage resources defined in the selected blueprints in your account. Amazon SageMaker Unified Studio can auto-create this role or you can provide your own.
   + **Manage access role** — This role grants Amazon SageMaker Unified Studio permissions to publish, grant access, and revoke access to Amazon SageMaker Lakehouse, AWS Glue Data Catalog, and Amazon Redshift data. It also grants Amazon SageMaker Unified Studio permissions to publish and manage subscriptions on Amazon SageMaker Catalog data and AI assets.
   + **Query execution role** — This role is used while running a query execution. AWS Lake Formation assumes this role to vend credentials needed by Amazon Athena during query execution.
   + **Amazon S3 bucket for projects** — Amazon SageMaker Unified Studio requires an S3 bucket in your AWS account for storing project artifacts and data.
   + **Virtual private cloud (VPC)** — Select a VPC configured for use with Amazon SageMaker Unified Studio. For more information, see [Configure VPC Networking for Amazon SageMaker Unified Studio Domain](vpc-networking-iam-based-domains.md).
   + **Data encryption** — This setting is optional. By default, your data is encrypted with an AWS managed key. To choose a different key, customize your encryption settings.
   + **User role policy** — This is an optional advanced configuration. Amazon SageMaker Unified Studio creates IAM roles for project users to perform data analytics, AI, and ML actions. You can attach your own AWS IAM policies to the role rather than using the default system-managed policy. The IAM policy must include all necessary permissions required for the service to function properly.
   + **Authorized domain units** — Domain units where projects can access resources defined by the blueprints.

1. After you specify all configuration settings, choose **Enable blueprint**.

After you enable the Tooling blueprint, you can create projects that use compute capabilities. To configure blueprint parameters such as idle timeout settings and permissions boundaries, see [Manage Tooling blueprint parameters](manage-tooling-blueprint.md).