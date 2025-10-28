# Set up for customization

The next sections give steps to set up Account Factory for the customization process. We
recommend that you set up [delegated
admin](../../../accounts/latest/reference/using-orgs-delegated-admin.md "../../../accounts/latest/reference/using-orgs-delegated-admin.md") for the hub account, before you begin these steps.

###### Summary

- **Step 1. Create the required role.** Create an
  IAM role that grants permission for AWS Control Tower to have access to the (hub)
  account, where the Service Catalog products, also called blueprints, are stored.
- **Step 2. Create the AWS Service Catalog product.** Create the
  AWS Service Catalog product (also called a “blueprint product”) that you'll need for baselining
  the custom account.
- **Step 3. Review your custom blueprint.** Inspect
  the AWS Service Catalog product (blueprint) that you created.
- **Step 4. Call your blueprint to create a customized
  account.** Enter the blueprint product information and the role
  information into the proper fields in Account Factory, in the AWS Control Tower console, while
  creating the account.
