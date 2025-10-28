# Updating templates for provisioned products

You can change the current template of a provisioned product to a different template.
For example if you have an EC2 product in Service Catalog, you can update that EC2
product to retain the same provisioned product ID, but change the template to a S3
bucket.

###### Note

Updating templates is not supported for provisioned Terraform Open Source or Terraform Cloud products. If
you want to use a different template for an existing Terraform product, you must
delete the product and then create a new product using the desired template.

###### To update a template for a provisioned product

1. In the left navigation menu, choose **Provisioned
   products**.
2. In **Provisioned products**, choose a provisioned product and
   select **Actions**, **Update**.

Note that you can also select **Actions**,
**Update** in the **Provisioned product details** page. 3. (Optional) In **Product details**, choose
**Change product**.

In **Change product**, note this warning:

_Changing the product will update this provisioned
product to a different product template. This may terminate resources and
create new resources._

You can update a provisioned product to a different version within the same
product. 4. (Optional) In **Products**, choose the product
you want to update with a different template. Then choose **Change**.

In **Product details**, note this warning:

_[Product name] will be updated from [current template
name] to [new template name]. However, the name of your provisioned product,
[Provisioned Product name], will not change._

You can update a provisioned product to a different version within the same
product. 5. In **Product versions**, choose the version of
the product you want. 6. In **Parameters**, choose the appropriate
parameters. 7. Choose **Update**.

In **Provisioned product details**, you can see
the details of the update. The provisioned product name does not change, but the
provisioned product now has a different template.
