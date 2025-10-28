# Adding products

You can add products to a portfolio
by uploading a new product directly
to an existing portfolio
or
by associating an existing product
from your catalog
to the portfolio.

###### Note

When you create a AWS Service Catalog product,
you can upload an AWS CloudFormation template or Terraform configuration file.
The AWS CloudFormation template is stored
in an Amazon Simple Storage Service (Amazon S3) bucket,
and the bucket name begins
with "**_cf-templates-_**."
You also must have permission
to retrieve objects
from additional buckets
when provisioning a product.
For more information,
see [Creating products](productmgmt-cloudresource.md#productmgmt-cloudresource-troubleshooting "productmgmt-cloudresource.md#productmgmt-cloudresource-troubleshooting").

## Adding a new product

You add new products directly from the **Portfolio
details** page. When you create a product from this page, AWS Service Catalog adds it to the
currently selected portfolio.

###### To add a new product

1. Navigate to the **Portfolios** page, and then choose the name of the portfolio to
   which you want to add the product.
2. On the **Portfolio details** page, expand the
   **Products** section, and then choose **Upload new product**.
3. For **Enter product details**, enter the following:
   - **Product name** – The name of the product.
   - **Product description** (optional) – The
     product description. This description is shown in the product listing to help you
     choose the correct product.
   - **Description** – The full description. This description is
     shown in the product listing to help you choose the correct product.
   - **Owner or Distributor** – The name or email address of the
     owner. The contact information for the distributor is optional.
   - **Vendor** (optional) – The name of the application's
     publisher. This field allows you to sort the products list to make it easier to find
     products.

4. On the **Version details** page, enter the following:
   - **Choose template** – For AWS CloudFormation products, choose your own template file,
     an AWS CloudFormation template from a local drive or a URL that points to a template stored in Amazon S3, an existing
     AWS CloudFormation Stack ARN template, or a template file stored in an external repository.

   For Teraform products, choose your own template file, a tar.gz configuration file from a local drive or
   a URL that points to a template stored in Amazon S3, or a tar.gz configuration file stored in an
   external repository.
   - **Version name** (optional) – The name of the product
     version (e.g., "v1", "v2beta"). No spaces are allowed.
   - **Description** (optional) – A description of the product
     version including how this version differs from the previous version.

5. For **Enter support details**, enter the following:
   - **Email contact** (optional) – The email address for
     reporting issues with the product.
   - **Support link** (optional) – An URL to a site where users
     can find support information or file tickets. The URL must begin with
     `http://` or `https://`. Administrators are responsible for
     maintaining the accuracy and access of support information.
   - **Support description** (optional) – A
     description of how you should use the **Email contact** and
     **Support link**.

6. Choose **Create product.**

## Adding an existing product

You can add existing products to a portfolio from three places: **Portfolios** list, **Portfolio details** page, or
the **Product list** page.

###### To add an existing product to a portfolio

1. Navigate to the **Portfolios** page.
2. Choose a portfolio. Then choose **Actions** - **Add product to portfolio**.
3. Choose a product, and then choose **Add product to portfolio**.

## Removing a product from a portfolio

When you no longer want to use a product, remove it from a portfolio. The product is
still available in your catalog from the **Products** page, and you can still add it to
other portfolios. You can remove multiple products from a portfolio at one time.

###### To remove a product from a portfolio

1. Navigate to the **Portfolios** page, and then choose the portfolio that contains
   the product. The **Portfolio details** page opens.
2. Expand the **Products** section.
3. Choose one or more products, and then choose **Remove**.
4. Confirm your choice.
