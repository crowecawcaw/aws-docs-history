# Publish data products in Amazon DataZone

Amazon DataZone enables data producers to group data assets into well-defined,
self-contained packages called data products that are tailored for specific business
use-cases. For more information, see [Amazon DataZone terminology and concepts](datazone-concepts.md "datazone-concepts.md").

To publish data products, you must be the owner or the contributor of the project.
[Metadata enforcement rules for
publishing](metadata-rules-publishing.md "metadata-rules-publishing.md") can be configured to establish clear metadata requirements for
data producers, restricting when a data product can be published.

To publish a data product complete the following steps.

1. Navigate to the Amazon DataZone data portal URL and sign in using single sign-on
   (SSO) or your AWS credentials. If you’re an Amazon DataZone administrator, you can
   navigate to the Amazon DataZone console at [https://console.aws.amazon.com/datazone](https://console.aws.amazon.com/datazone "https://console.aws.amazon.com/datazone") and sign in with the
   AWS account where the domain was created, then choose **Open data
   portal**.
2. In the Amazon DataZone data portal, choose the project in which the data product
   that you want to publish lives.
3. Choose the **Data** tab, then choose **Inventory
   data**, and then choose the **Data products**
   filter. This displays all unpublished existing data products.
4. Choose the data product that you want to publish, and then choose
   **Publish**. Confirm the publishing of this data product by
   choosing **Publish data product**.

###### Note

Any unpublished data assets that are in this data product will become
published, but will only be available through this data product.
