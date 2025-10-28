# Prerequisite: Configure your Terraform provisioning engine

As a prerequisite to creating Terraform products in AWS Service Catalog, you must install and configure a provisioning engine in your Service Catalog administrator account (hub account).
The provisioning engine is required for both Terraform Community Edition products (using the External product type) and Terraform Cloud products (using the Terraform Cloud
product type).

###### Note

Engine configuration is a one-time setup that takes approximately 30 minutes.

## Provisioning engine for Terraform Community Edition (External product type)

AWS Service Catalog uses the _External_ product type to support Terraform Community Edition products.
The _External_ product type
also supports other provisioning tools, including Pulumi, Ansible, Chef, and more based on the configuration of the provisioning engine.

For AWS Service Catalog products that use the External product type with HashiCorp's Terraform Community Edition, you
must install and configure a Terraform provisioning engine in your AWS Service Catalog administrator account (hub account).
AWS manages this engine and its resources.

AWS Service Catalog provides a GitHub repository with instructions on
[installing and configuring the AWS-provided Terraform provisioning engine](https://github.com/aws-samples/service-catalog-engine-for-terraform-os/ "https://github.com/aws-samples/service-catalog-engine-for-terraform-os/"). The repo includes
the following information:

- Required installation tools
- Building the code
- Deploying to an AWS account
- Additional information about provisioning workflows, quality assurance, and limitations

## Provisioning engine for Terraform Cloud

For AWS Service Catalog products that use the Terraform Cloud product type with HashiCorp's Terraform Cloud, you
must install and configure a Terraform provisioning engine in your AWS Service Catalog administrator account (hub account).
HashiCorp manages this engine in a remote environment.

HashiCorp provides a GitHub repository with instructions on configuring the
[Terraform Cloud engine for AWS Service Catalog](https://github.com/hashicorp/aws-service-catalog-engine-for-tfc "https://github.com/hashicorp/aws-service-catalog-engine-for-tfc"). The repo includes
the following information:

- Required installation tools
- Building the code
- Deploying to an AWS account
- Additional information about provisioning workflows, quality assurance, and limitations
