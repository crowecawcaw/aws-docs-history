# Unpublish data products in Amazon SageMaker Unified Studio

Amazon SageMaker Unified Studio enables data producers to group data assets into well-defined,
self-contained packages called data products that are tailored for specific business use
cases. For more information, see [Amazon SageMaker Unified Studio terminology and concepts](concepts.md "concepts.md").

Any Amazon SageMaker Unified Studio user with the required permissions can unpublish an Amazon SageMaker Unified Studio data
product.

To unpublish a data product complete the following steps.

1. Navigate to Amazon SageMaker Unified Studio using the URL from your admin and log in
   using your SSO or AWS credentials.
2. Navigate to the project that contains the data product that you want to
   unpublish. You can do this by using the center menu at the top of the page and
   choosing **Browse all projects**, then choosing the name of the
   project that you want to navigate to.
3. Under **Project catalog**, choose
   **Assets**.
4. Choose the **Inventory** tab, and then choose the
   **Data products** filter. This displays existing data
   products in the project inventory.
5. Choose the data product that you want to unpublish. This opens the data
   product details page.
6. Expand **Actions** and choose
   **Unpublish**. Confirm the unpublishing of this data product by
   choosing **Unpublish**.

###### Note

Unpublishing a data product has the following effects:

    * This data product will no longer be available to view or to
     subscribe to.
    * Any data assets that are only available through this data product
     will no longer be available.
    * All active subscriptions to this data product will remain.
    * Any individually published data assets will not be
     affected.
