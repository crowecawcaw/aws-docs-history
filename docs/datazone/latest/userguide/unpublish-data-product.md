# Unpublish data products in Amazon DataZone

Amazon DataZone enables data producers to group data assets into well-defined,
self-contained packages called data products that are tailored for specific business
use-cases. For more information, see [Amazon DataZone terminology and concepts](datazone-concepts.md "datazone-concepts.md").

To unpublish a data product, you must be the owner or the contributor of the project
to which the data product belongs.

To unpublish a data product complete the following steps.

1. Navigate to the Amazon DataZone data portal URL and sign in using single sign-on
   (SSO) or your AWS credentials. If you’re an Amazon DataZone administrator, you can
   navigate to the Amazon DataZone console at [https://console.aws.amazon.com/datazone](https://console.aws.amazon.com/datazone "https://console.aws.amazon.com/datazone") and sign in with the
   AWS account where the domain was created, then choose **Open data
   portal**.
2. In the Amazon DataZone data portal, choose the project in which the data product
   that you want to unpublish lives.
3. Choose the **Data** tab, then choose **Inventory
   data** or **Published data**, and then choose the
   **Data products** filter. This displays all existing data
   products.
4. Choose the data product that you want to unpublish, and then expand
   **Actions** and choose **Unpublish**.
   Confirm the unpublishing of this data product by choosing
   **Unpublish**.

###### Note

Unpublishing a data product has the following effects:

    * This data product will no longer be available to view or to
     subscribe.
    * Any data assets that are only available through this data product
     will no longer be available.
    * All active subscriptions to this data product will remain.
    * Any individually published data assets will not be
     affected.
