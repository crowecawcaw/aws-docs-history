# Republish data products in Amazon SageMaker Unified Studio

Amazon SageMaker Unified Studio enables data producers to group data assets into well-defined,
self-contained packages called data products that are tailored for specific business use
cases. For more information, see [Amazon SageMaker Unified Studio terminology and concepts](concepts.md "concepts.md").

Any Amazon SageMaker Unified Studio user with the required permissions can republish an Amazon SageMaker Unified Studio data
product.

To republish a data product complete the following steps.

1. Navigate to Amazon SageMaker Unified Studio using the URL from your admin and log in
   using your SSO or AWS credentials.
2. Navigate to the project that contains the data product that you want to edit.
   You can do this by using the center menu at the top of the page and choosing
   **Browse all projects**, then choosing the name of the
   project that you want to navigate to.
3. Under **Project catalog**, choose
   **Assets**.
4. Choose the **Inventory** tab, and then choose the
   **Data products** filter. This displays existing data
   products in the project inventory.
5. Choose the data product that you want to republish.
6. Make the desired edits to the data product. For more information, see [Edit data products in Amazon SageMaker Unified Studio](edit-data-product.md "edit-data-product.md").
7. On the data product's details page, choose **Re-publish**.
   Confirm this action by choosing **Re-publish data product** in
   the **Re-publish data product** pop-up window.

###### Note

Republishing this data product will update the following for all
subscribers:

    * If assets have been removed from the data product, subscribers
     will no longer have access to these assets.
    * If assets have been added to the data product, subscribers will
     get access to these assets.
    * New published versions of data assets will be available.
