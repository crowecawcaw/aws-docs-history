# Managing Versions

You assign product versions when you create a product, and you can update product versions any time.

Versions have an AWS CloudFormation template, a title, a description, a status, and guidance.

## Version Status

A version can have one of three statuses:

- **Active** - An active version appears in the version list and allows users to launch it.
- **Inactive** - An inactive version is hidden from the version list. Existing provisioned products launched from this version will not be affected.
- **Deleted** - A deleted version is removed from the version list. Deleting a version cannot be undone.

## Version Guidance

You can set version guidance to provide information to end users about the product version. Version guidance only affects active product versions.

There are two options for version guidance:

- **None** - By default, product versions do not have any guidance. End users can use
  that version to update and launch provisioned products.
- **Deprecated** - Users cannot launch new provisioned products using a deprecated product version.
  If a p provisioned product launched previously uses a now deprecated version, users can only update that provisioned product
  using the existing version or a new version.

## Updating Versions

You assign product versions when creating a product, and you can also update a version any time. For more information about creating a product, see [Creating Products](productmgmt-cloudresource.md "productmgmt-cloudresource.md").

###### To update a product version

1. In the AWS Service Catalog console, choose **Products**.
2. From the product list, choose the product you want to update the version of.
3. On the **Product details** page, choose the **Versions** tab, then choose the version you want to update.
4. On the **Version details** page, edit the product version, then choose **Save changes**.
