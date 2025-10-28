# Updating existing Terraform Open Source products and provisioned products to the

External product type

To continue support of HashiCorp technologies, as a result of the recent licensing changes to Terraform,
AWS Service Catalog changed any previous references of _Terraform Open Source_ to _External_.
The External product type includes support for Terraform Community Edition, previously known as Terraform Open Source.
AWS Service Catalog no longer supports Terraform Open Source as a valid product type for any
_new_ products or provisioned products. You can only update or terminate existing Terraform Open Source resources, including product versions and provisioned
products.

If you have not already done so, you must transition all existing Terraform Open Source products and provisioned products to External products, by
following the instructions in this section.

1. Update your existing Terraform Reference Engine for AWS Service Catalog to include support for both
   **External** and **Terraform Open Source**
   product types. For instructions about updating your Terraform Reference Engine, review our
   [GitHub Repository](https://github.com/aws-samples/service-catalog-engine-for-terraform-os "https://github.com/aws-samples/service-catalog-engine-for-terraform-os").
2. Recreate any existing Terraform Open Source products using the new External product type.
3. Delete any existing products that use the Terraform Open Source product type.
4. Reprovision remaining resources to use the new External product type.
5. Terminate any existing provisioned products that use the Terraform Open Source product type.
   After transitioning your existing products, use the External product type
   for any new products that use a tar.gz configuration file.

AWS Service Catalog will support customers through this change as needed. If these changes require
extensive effort for your account, or impact critical product workloads, contact your account
representitive to request assistance.
