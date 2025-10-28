# Publish data products in Amazon SageMaker Unified Studio

Amazon SageMaker Unified Studio enables data producers to group data assets into well-defined,
self-contained packages called data products that are tailored for specific business use
cases. For more information, see [Amazon SageMaker Unified Studio terminology and concepts](concepts.md "concepts.md").

Any Amazon SageMaker Unified Studio user with the required permissions can publish an Amazon SageMaker Unified Studio data
product.

To publish a data product complete the following steps.

1. Navigate to Amazon SageMaker Unified Studio using the URL from your admin and log in
   using your SSO or AWS credentials.
2. Navigate to the project that contains the data product that you want to
   publish. You can do this by using the center menu at the top of the page and
   choosing **Browse all projects**, then choosing the name of the
   project that you want to navigate to.
3. Under **Project catalog**, choose
   **Assets**.
4. Choose the **Inventory** tab, and then choose the
   **Data products** filter. This displays existing data
   products in the project inventory.
5. Choose the data product that you want to publish. This opens the data product
   details page.
6. Choose **Publish**. Confirm the publishing of this data
   product by choosing **Publish data product**.

###### Note

Any unpublished data assets that are in this data product will become
published, but will only be available through this data product.
