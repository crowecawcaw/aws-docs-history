#

Updating products

When you update a product's template, you create a new version of the product.
New product versions are automatically available to all users who have access to a portfolio
containing the product.

###### Note

When updating an existing product, you cannot change the product type (AWS CloudFormation or Teraform). For example, if you update a
AWS CloudFormation product, you cannot replace the existing AWS CloudFormation template with a Terraform tar.gz configuration file. You must update the
existing AWS CloudFormation template file with a new AWS CloudFormation template file.

End users who are currently running a provisioned product of the previous product version can update their
provisioned product to the new version.
When a new version of a product is available,
users can use the **Update provisioned product** command
on the **Provisioned product list** or **Provisioned product details** pages.

Before you create a new version of a product, AWS Service Catalog recommends that you test your product updates in AWS CloudFormation or
in the Terraform engine to ensure that they function properly.

###### To create a new product version

1. Navigate
   to the **Product list** page.
2. Choose the product product
   that you would like
   to update.
   You're directed
   to the _Product details_ page.
3. On the _Product details_ page,
   expand the **Versions** tab,
   and then choose **Create new version**.
4. Under **Version details**,
   perform the following:
   - **Choose template** – There are four ways to add a template
     file.

   _Use a local template file_ - Upload an AWS CloudFormation template
   or a Terraform tar.gz configuration file from a local drive.

   _Use an Amazon S3 URL_ - Specify a URL that points to an
   AWS CloudFormation template or a Terraform tar.gz configuration file stored in Amazon S3.
   If you specify an Amazon S3 URL, it
   must begin with https://.

   _Use an external repository_ - Specify your GitHub,
   GitHub Enterprise, or Bitbucket code repository. AWS Service Catalog allows you to sync products to
   template files. For Terraform products, the template file format is required to be
   a single file archived in Tar and compressed in Gzip.

   _Use an existing CloudFormation stack_ - Enter
   the ARN for an existing CloudFormation stack. This method does not support Terraform Cloud or
   External products.
   - **Version title** – The name of the product version (e.g.,
     "v1", "v2beta"). No spaces are allowed.
   - **Description** (optional) – A description of the product
     version, including how this version differs from the previous version.

5. Choose **Create product version**.
   You can also use CodePipeline to create and configure a pipeline to deploy your
   product template to AWS Service Catalog, and deliver your changes in your source repository. For more
   information, see [Tutorial:
   Create a Pipeline That Deploys to AWS Service Catalog](../../../codepipeline/latest/userguide/tutorials-S3-servicecatalog.md "../../../codepipeline/latest/userguide/tutorials-S3-servicecatalog.md").
