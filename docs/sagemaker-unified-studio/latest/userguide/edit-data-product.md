# Edit data products in Amazon SageMaker Unified Studio

Amazon SageMaker Unified Studio enables data producers to group data assets into well-defined,
self-contained packages called data products that are tailored for specific business use
cases. For more information, see [Amazon SageMaker Unified Studio terminology and concepts](concepts.md "concepts.md").

Any Amazon SageMaker Unified Studio user with the required permissions can edit an Amazon SageMaker Unified Studio data
product.

To edit a data product complete the following steps.

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
5. Choose the data product that you want to edit. As part of editing a data
   product, you can do the following:
   - Choose **Create README** to add a README that will
     help users understand the page better.
   - Choose **Add terms** to add glossary terms. Make your
     selections of glossary terms in the **Add terms**
     window and then choose **Add terms**.
   - Choose **Add metadata form** and then select your
     form in the **Add metadata form** window and choose
     **Add**.
   - Expand **Actions**, choose **Edit**,
     make your edits to the name and description of the data product, and
     then choose **Update**.
   - On the **Assets** tab, remove one of the existing
     assets in the data product by choosing that asset, then expanding the
     three-dot action icon and choosing **Remove asset**.
     Confirm the asset removal by choosing **Remove** in the
     **Remove asset** pop-up window. When you republish,
     this asset will be removed from all subscribers to this data
     product.
   - On the **Assets** tab, add a new asset to the data
     product by choosing the **Add** button and then
     selecting one or more assets to be added to the data product.
