# Republish data products in Amazon DataZone

Amazon DataZone enables data producers to group data assets into well-defined,
self-contained packages called data products that are tailored for specific business
use-cases. For more information, see [Amazon DataZone terminology and concepts](datazone-concepts.md "datazone-concepts.md").

To republish a data product, you must be the owner or the contributor of the project.
[Metadata enforcement rules for
publishing](metadata-rules-publishing.md "metadata-rules-publishing.md") can be configured to establish clear metadata requirements for
data producers, restricting when a data product can be republished.

To republish a data product complete the following steps.

1. Navigate to the Amazon DataZone data portal URL and sign in using single sign-on
   (SSO) or your AWS credentials. If you’re an Amazon DataZone administrator, you can
   navigate to the Amazon DataZone console at [https://console.aws.amazon.com/datazone](https://console.aws.amazon.com/datazone "https://console.aws.amazon.com/datazone") and sign in with the
   AWS account where the domain was created, then choose **Open data
   portal**.
2. In the Amazon DataZone data portal, choose the project in which the data product
   that you want to republish lives.
3. Choose the **Data** tab, then choose **Published
   data**, and then choose the **Data products**
   filter.
4. Choose the data product that you want to republish, and then choose the
   **Assets** tab.
5. On the **Assets** tab, do one of the following:
   - remove one of the existing assets in the data product by choosing that
     asset, then expanding the action icon and choosing **Remove
     asset**. Confirm the asset removal by choosing
     **Remove** in the **Remove asset**
     pop up window. Once you republish, this asset will be removed from all
     subscribers to this data product.
   - Add a new asset to the data product by choosing the Add button and
     then selecting one or more assets to be added to the data product.

6. On the data product's details page, choose **Re-publish**.
   Confirm this action by choosing **Republish** in the
   **Republish data product** pop up window.

###### Note

Republishing this data product will update the following for all
subscribers:

    * If assets have been removed from the data product, subscribers
     will no longer have access to these assets.
    * If assets have been added to the data product, subscribers will
     get access to these assets.
    * New published versions of data assets will be available.
