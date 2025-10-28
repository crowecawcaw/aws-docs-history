# Syncing products to template files from GitHub, GitHub Enterprise,

or Bitbucket

AWS Service Catalog allows you to sync products to template files that are managed through external repository
provider. AWS Service Catalog refers to products with this type of template connection as _Git-synced_
products. Repository options include GitHub, GitHub Enterprise, or Bitbucket. After you authorize your AWS account
with an external repository account, you can create new AWS Service Catalog products or update existing products to sync
to a template file in the repository. When changes are made to the template file and committed in the repository
(for example, using git-push), AWS Service Catalog automatically detects the changes and creates a new product version
(artifact).

###### Topics

- [Required permissions to sync products to external template files](#required-perms-synced-repo "#required-perms-synced-repo")
- [Create an account connection](#create-synced-product "#create-synced-product")
- [Viewing Git-synced product connections](#view-repo-sync "#view-repo-sync")
- [Updating Git-synced product connections](#update-repo-sync "#update-repo-sync")
- [Deleting Git-synced product connections](#delete-repo-sync "#delete-repo-sync")
- [Syncing Terraform products to template files from GitHub, GitHub Enterprise,
  or Bitbucket](#git-synced-Terraform "#git-synced-Terraform")
- [AWS Region support for Git-synced products](git-sync-supported-regions.md "git-sync-supported-regions.md")

## Required permissions to sync products to external template files

You can use the following AWS Identity and Access Management (IAM) policy as a template to enable AWS Service Catalog administrators to sync products to template files
from an external repository. This policy includes required permissions from both CodeConnections and AWS Service Catalog.
AWS Service Catalog recommends that you copy the template policy below, and also use the AWS Service Catalog `AWSServiceCatalogAdminFullAccess`
[managed policy](security-iam-awsmanpol.md "security-iam-awsmanpol.md")
when enabling repository-synced products.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "CodeStarAccess",
 "Effect": "Allow",
 "Action": [
 "codestar-connections:UseConnection",
 "codestar-connections:PassConnection",
 "codestar-connections:CreateConnection",
 "codestar-connections:DeleteConnection",
 "codestar-connections:GetConnection",
 "codestar-connections:ListConnections",
 "codestar-connections:ListInstallationTargets",
 "codestar-connections:GetInstallationUrl",
 "codestar-connections:StartOAuthHandshake",
 "codestar-connections:UpdateConnectionInstallation",
 "codestar-connections:GetIndividualAccessToken"
 ],
 "Resource": "arn:aws:codestar-connections:*:*:connection/*"
 },
 {
 "Sid": "CreateSLR",
 "Effect": "Allow",
 "Action": "iam:CreateServiceLinkedRole",
 "Resource": "arn:aws:iam::*:role/aws-service-role/sync.servicecatalog.amazonaws.com/AWSServiceRoleForServiceCatalogArtifactSync",
 "Condition": {
 "StringLike": {
 "iam:AWSServiceName": "sync.servicecatalog.amazonaws.com"
 }
 }
 }
 ]
}`

```

## Create an account connection

Before syncing a template file to a AWS Service Catalog product, you must create and authorize a one-time, account-to-account connection.
You use this connection to specify the details of the repository containing the desired template file.
You can create a connection using the AWS Service Catalog console, CodeConnections console, AWS Command Line Interface (CLI), or CodeConnections APIs.

After establishing a connection, you can use the AWS Service Catalog console, AWS Service Catalog API, or CLI to create a synced AWS Service Catalog product.
AWS Service Catalog administrators can create new or update existing AWS Service Catalog products based on a template file in a
repository and branch. If a change is committed in the repository, AWS Service Catalog automatically detects the
change and creates a new product version. Previous product versions are maintained up to the
prescribed version limit and assigned a **deprecated** status.

Additionally, AWS Service Catalog automatically creates a service-linked role (SLR) after the connection is created. This SLR allows
AWS Service Catalog to detect any template file changes that are committed to the repository. The SLR also allows AWS Service Catalog to automatically
create new product versions for synced products. For more information about SLR permissions and functionality,
refer to [Service-linked roles for AWS Service Catalog](#required-perms-synced-repo "#required-perms-synced-repo").

###### To create a new Git-synced product

1. In the left navigation panel, choose **Product list**, and
   then choose **Create product**.
2. Enter the **Product details**.
3. In Version details, choose **Specify your code repository using an AWS CodeStar
   provider**, and then choose the **Create a new AWS CodeStar connection** link.
4. After you create the connection, refresh the connections list, and then select the new connection.
   Specify the repository details, including the **repository**, **branch**,
   and **template file path**.

For infomration about using a Terraform configuration file, see [Syncing Terraform products to template files from GitHub, GitHub Enterprise,
or Bitbucket](#git-synced-Terraform "#git-synced-Terraform") .

    1. (Optional when creating a new AWS Service Catalog product resource) In the **Support Details** section,
     add metadata for the product.
    2. (Optional when creating a new AWS Service Catalog product resource) In the **Tags** section, choose
     **Add new tag** and enter the **Key** and **Value** pairs.

5. Choose **Create new product**.

###### To create multiple Git-synced products

1. In the AWS Service Catalog console left navigation panel, choose **Product list**, and then
   choose **Create multiple git-managed products**.
2. Enter the **Common product details**.
3. In External repository details, select an **AWS CodeStar connection**,
   and then specify the **repository** and **branch**.
4. In the Add products pane, enter the **Template file path** and
   **Product name**. Choose **Add new item** and continue adding products
   as desired.
5. After adding all desired products, choose **Bulk create products**.

###### To connect an existing AWS Service Catalog product to an external repository

1. In the AWS Service Catalog console left navigation panel, choose **Product list**, and then
   choose **Connect products to an external repository**.
2. On the Select products page, select the products you want to connect to an
   external repository, and then choose **Next**.
3. On the Specify source details page, select an existing AWS CodeStar connection,
   and then specify the **repository**,the
   **branch**, and the **template file path**.
4. Choose **Next**.
5. On the Review and submit page, verify the connection details, and then
   choose **Connect products to an external repository**.

## Viewing Git-synced product connections

You can use the AWS Service Catalog console, API, or AWS CLI to view repository connection details. For AWS Service Catalog products that are linked to
a template file, you can retrieve information about the repository connection and the last time the template
was synced with the product from the **Last Sync Status**.

###### Note

You can view repository information and the **Last Sync Status** at the product level.
Users must have IAM permissions in the CodeConnections APIs to view repository details. Refer to
[Required permissions to sync AWS Service Catalog products to template files](#required-perms-synced-repo "#required-perms-synced-repo")
for more information about the required policy for these IAM permissions.

###### To view connection and repository details using AWS Management Console

1. In the left navigation panel, choose **Product list**.
2. Select the product from the list.
3. On the **Product** page, navigate to the **Product source details**
   section.
4. To view the source revision ID for a product version, choose the **Last version created** link.
   The **Version details** section display the source revision ID.

**To view connection and repository details using AWS CLI**

From the AWS CLI, run the following commands:

`$ aws servicecatalog describe-product-as-admin`

`$ aws servicecatalog describe-provisioning-artifact`

`$ aws servicecatalog search-product-as-admin`

`$ aws servicecatalog list-provisioning-artifacts`

## Updating Git-synced product connections

You can update existing account connections and Git-synced products using the AWS Service Catalog console,
AWS Service Catalog API, or AWS CLI.

To learn how to connect an existing AWS Service Catalog product to a template file, refer to [Creating new Git-synced product connections](#create-synced-product "#create-synced-product").

###### To update existing products to Git-synced products

1. In the left navigation panel, choose **Product list**, and then choose one
   of the following options:
   - To update a **single product**, select the product, navigate to the **Product source details** section,
     and then choose **Edit details**.
   - To update **multiple products**, choose **Connect products to an
     external repository**, select up to ten products, and then choose **Next**.

2. In the **Product source details** section, perform the following updates:
   - Specify the connection.
   - Specify the repository.
   - Specify the branch.
   - Name the template file.

3. Choose **Save changes**.

###### Note

For products not yet connected to an external repository, you can use the **Connect to an external repository**
option displayed in the alert at the top of the product info page after selecting the product.

You can also use the AWS Service Catalog console or the AWS CLI to

- Connect an existing AWS Service Catalog product to a template file in an external repository
- Update product metadata, including the product name, description, and tags.
- Reconfigure (update the sync to use a different repository source) a connection for a previously connected
  AWS Service Catalog product.

###### To update connection and repository details using AWS Service Catalog console

1. In the AWS Service Catalog console left navigation panel, choose **Product list**, and then
   select a product that is currently connected to an external repository.
2. In the **Product source details**
   section, choose **Edit product source**.
3. In the **Product source details** section, specify the new desired repository.
4. Choose **Save changes**.

**To update connection and repository details using AWS CLI**

From the AWS CLI run the `$ aws servicecatalog update-product` and `$ aws servicecatalog update-provisioning-artifact`
commands.

## Deleting Git-synced product connections

You can delete a connection between a AWS Service Catalog product and a template file
using the AWS Service Catalog console, CodeConnections API, or AWS CLI. When you disconnect a product from a template file,
the synced AWS Service Catalog product switches to a regularly managed product. After disconnecting the product,
if the template file is changed and committed in the previously connected repository, the changes are
_not_ reflected. To re-connect a AWS Service Catalog product to a template file in an external repository,
refer to Updating connections and synced AWS Service Catalog products.

###### To disconnect a Git-synced product using the AWS Service Catalog console

1. In the AWS Management Console, choose **Product list** from the left navigation panel.
2. Select a product from the list.
3. On the **Product** page, navigate to the **Product source details**
   section.
4. Choose **Disconnect**.
5. Confirm the action, and then choose **Disconnect**.

**To disconnect a Git-synced product using AWS CLI**

From the AWS CLI, run the `$ aws servicecatalog update-product` command. In the `ConnectionParameters`
input, remove the specified connection.

**To delete a connection using the CodeConnections API or AWS CLI**

In the CodeConnections API or AWS CLI, run the `$ aws codestar-connections delete-connection` command.

## Syncing Terraform products to template files from GitHub, GitHub Enterprise,

or Bitbucket

When creating a Git-synced product using a Terraform configuration file, the file
path only accepts the tar.gz format. Terraform folder formats are not accepted in the file path.
