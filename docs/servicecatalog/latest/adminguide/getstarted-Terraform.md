# Getting started with a Terraform product

AWS Service Catalog enables quick, self-service provisioning with governance for your
[HashiCorp Terraform](https://developer.hashicorp.com/terraform/intro/terraform-editions "https://developer.hashicorp.com/terraform/intro/terraform-editions") configurations within AWS.
You can use AWS Service Catalog as a single tool to organize, govern, and distribute your Terraform configurations at scale within AWS.
AWS Service Catalog supports Terraform across several key features, including cataloging of standardized and pre-approved Terraform templates,
access control, versioning, tagging, and sharing to other AWS accounts. In AWS Service Catalog, your end users see a
simple list of products and versions they have access to, and can then deploy those products in a single action.

###### Note

To continue support of HashiCorp technologies, as a result of the recent licensing changes to Terraform,
AWS Service Catalog changed any previous references of _Terraform Open Source_ to _External_.
The External product type includes support for the Terraform Community Edition, previously known as Terraform Open Source.
For more information and instructions about migrating your existing
Terraform Open Source products and provisioned products to the External product type, review
[Updating existing Terraform Open Source products and provisioned products to the
External product type](update_terraform_open_source_to_external.md "update_terraform_open_source_to_external.md").

The steps in the following tutorial will help you get started with a Terraform product in AWS Service Catalog.

As the catalog administrator, you work in a central administrator
account (hub account). Both Terrafrm Community Edition and Terraform Cloud products require a Terraform provisioning
engine, which you can learn more about in [Provisioning engine for Terraform Community Edition (External product type)](getstarted-terraform-engine.md#getstarted-terraform-engine-os "getstarted-terraform-engine.md#getstarted-terraform-engine-os") and
[Provisioning engine for Terraform Cloud](getstarted-terraform-engine.md#getstarted-terraform-engine-cloud "getstarted-terraform-engine.md#getstarted-terraform-engine-cloud") .

During the tutorial, you perform the following tasks in the administrator account:

- Create a Terraform product using either the _Terraform Cloud_ or _External_ product type. Service Catalog uses the
  External product type to support Terraform Community Edition products.
- Associate the product with a portfolio
- Create a launch constraint to allow your end users to provision the product
- Tag the product
- Share the portfolio and the Terraform product with the end user account (spoke account)
  In the tutorial, you share a portfolio using the organization sharing option from the admin hub
  account, which is also the management account of the Organization. For more information on
  organization sharing, see [Sharing a Portfolio](catalogs_portfolios_sharing_how-to-share.md "catalogs_portfolios_sharing_how-to-share.md").

The AWS resource contained in the Terraform product you
create in the tutorial is a simple Amazon S3 bucket.

###### Note

Before you begin,
make sure
that you complete the action items
in [Setting Up AWS Service Catalog](setup.md "setup.md").

###### Topics

- [Updating existing Terraform Open Source products and provisioned products to the
  External product type](update_terraform_open_source_to_external.md "update_terraform_open_source_to_external.md")
- [Prerequisite: Configure your Terraform provisioning engine](getstarted-terraform-engine.md "getstarted-terraform-engine.md")
- [Step 1: Terraform configuration file download](getstarted-template-Terraform.md "getstarted-template-Terraform.md")
- [Step 2: Create a Terraform product](getstarted-product-Terraform.md "getstarted-product-Terraform.md")
- [Step 3: Create a AWS Service Catalog portfolio](getstarted-portfolio-Terraform.md "getstarted-portfolio-Terraform.md")
- [Step 4: Add product to portfolio](getstarted-portfolio-add-product-Terraform.md "getstarted-portfolio-add-product-Terraform.md")
- [Step 5: Create launch roles](getstarted-launchrole-Terraform.md "getstarted-launchrole-Terraform.md")
- [Step 6: Add a Launch constraint to your Terraform product](getstarted-launchconstraint-Terraform.md "getstarted-launchconstraint-Terraform.md")
- [Step 7: Grant end user access](getstarted-deploy-Terraform.md "getstarted-deploy-Terraform.md")
- [Step 8: Share portfolio with end user](getstarted-share-portfolio-end-user-Terraform.md "getstarted-share-portfolio-end-user-Terraform.md")
- [Step 9: Test the end user experience](getstarted-verify-Terraform.md "getstarted-verify-Terraform.md")
- [Step 10: Monitoring Terraform provisioning operations](getstarted-monitoring-Terraform.md "getstarted-monitoring-Terraform.md")
