# Install and configure the Terraform provisioning engine

To successfully use Terraform products with AWS Service Catalog, you must install and configure a
Terraform provisioning engine in the same account where you will be administering Terraform products.
To get started, you can use the Terraform provisioning engine provided by AWS, which installs and
configures the code and infrastructure required for the Terraform provisioning engine to work with AWS Service Catalog.
This one-time setup takes approximately 30 minutes. AWS Service Catalog provides a GitHub repository with instructions on
[installing and configuring the Terraform provisioning engine](https://github.com/aws-samples/service-catalog-engine-for-terraform-os "https://github.com/aws-samples/service-catalog-engine-for-terraform-os").

## Queue determination

When you call a provisioning operation, AWS Service Catalog prepares a payload message to send to the
relevant queue in the provisioning engine. In order to build the ARN for the queue,
AWS Service Catalog makes a the following assumptions:

- The provisioning engine is located in the account of the product owner
- The provisioning engine is located in the same region in which the call to AWS Service Catalog was made
- The provisioning engine queues follows the documented naming schema detailed below

For example, if ProvisionProduct is called in `us-east-1` from account 1111111111 using a
product created by account 0000000000000, AWS Service Catalog assumes the correct SQS ARN is
`arn:aws:sqs:us-east-1:0000000000000:ServiceCatalogTerraformOSProvisionOperationQueue`.

The same logic applies for the Lambda function called by `DescribeProvisioningParameters`.
