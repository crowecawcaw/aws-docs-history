# Delete data products in Amazon SageMaker Unified Studio

Amazon SageMaker Unified Studio enables data producers to group data assets into well-defined,
self-contained packages called data products that are tailored for specific business use
cases. For more information, see [Amazon SageMaker Unified Studio terminology and concepts](concepts.md "concepts.md").

Any Amazon SageMaker Unified Studio user with the required permissions can delete an Amazon SageMaker Unified Studio data
product.

To delete a data product complete the following steps.

1. Navigate to Amazon SageMaker Unified Studio using the URL from your admin and log in
   using your SSO or AWS credentials.
2. Navigate to the project that contains the data product that you want to
   delete. You can do this by using the center menu at the top of the page and
   choosing **Browse all projects**, then choosing the name of the
   project that you want to navigate to.
3. Under **Project catalog**, choose
   **Assets**.
4. Choose the **Inventory** tab, and then choose the
   **Data products** filter. This displays existing data
   products in the project inventory.
5. Choose the data product that you want to delete.
6. Expand **Actions** and choose **Delete**.
   Confirm the deletion of this data product by typing `delete` in the
   text field and then choosing **Delete**.

###### Note

Deleting a data product has the following effects:

    * The data product will no longer be available to publish, view, or
     subscribe to.
    * Any data assets that are only available through this data product
     will no longer be visible in the data catalog. They will not be
     deleted from your inventory assets.
