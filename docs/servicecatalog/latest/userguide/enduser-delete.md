# Deleting provisioned products

To remove all AWS resources a provisioned product uses, delete the provisioned product.

Deleting a provisioned product terminates all resources and removes the provisioned product
from your provisioned product list.

###### Note

If you have already deleted the underlying physical resource for a provisioned product, you can use
the `RetainPhysicalResources` field in the `TerminateProvisionedProduct` API to delete
that product.

Delete a provisioned product only if you no longer need it. Before deleting a provisioned
product, record any information about the provisioned product or its resources, which you might
need later.

Before deleting a provisioned product, ensure it is in either the **Available**
or **Failed** state. Service Catalog can delete provisioned products only in these two states.

For more information on provisioned product status, see [Viewing Provisioned Product Status](enduser-viewstack.md#enduser-viewstack-status "enduser-viewstack.md#enduser-viewstack-status").

###### To delete a provisioned product

1. Navigate to the Provisioned products list page.
2. Select the provisioned product. On the **Actions** menu, choose
   **Terminate**.
3. In the **Terminate provisioned product** dialog box, do the following:
   1. Verify the provisioned product you want to delete, and then enter _terminate_.
   2. (Optional) Select **Ignore errors**. If you select this option, Service Catalog stops managing
      the provisioned product even if it cannot delete the product's underlying resources.
   3. Choose **Terminate provisioned product**.
