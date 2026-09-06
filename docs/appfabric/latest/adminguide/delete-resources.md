

# Delete AWS AppFabric for security resources
<a name="delete-resources"></a>

If you don't want to continue using AWS AppFabric for security, be sure to delete the data in the output locations you created during setup and your AppFabric for security resources to avoid incurring additional charges. To clean up your AppFabric resources, you must delete the resources in the reverse order in which you created them for each software as a service (SaaS) application: **Ingestion destinations** > **Ingestions** > **App authorization** > **App bundles**

After you’ve deleted your final app authorization, you can delete the app bundle.

**Topics**
+ [Delete an ingestion destination](#delete-ingestion-destinations)
+ [Delete an ingestion](#delete-ingestions)
+ [Delete an app authorization](#delete-app-authorizations)
+ [Delete an app bundle](#delete-app-bundles)

## Delete an ingestion destination
<a name="delete-ingestion-destinations"></a>

If you select an output location when you create an ingestion, AppFabric for security creates ingestion destinations on your behalf. To delete an ingestion destination, use the following steps:

1. Open the AppFabric console at [https://console.aws.amazon.com/appfabric/](https://console.aws.amazon.com/appfabric/).

1. From the **Getting started** page, expand the menu on the left.

1. Choose **Ingestions**.

1. Choose an app authorization.

1. Select the option button next to the destination that you want to delete and choose **Delete**.

1. Choose **Delete** on the delete destination dialog box to confirm.

1. Repeat the above steps for all of your destinations.

## Delete an ingestion
<a name="delete-ingestions"></a>

To delete an ingestion, use the following steps:

1. From the **Getting started** page, expand the menu on the left.

1. Choose **Ingestions**.

1. Select the option button that is next to your app authorization.

1. Choose the **Actions** dropdown menu.

1. Choose **Delete**.

1. Choose **Delete** on the delete ingestion dialog box to confirm.

## Delete an app authorization
<a name="delete-app-authorizations"></a>

To delete an app authorization, use the following steps:

1. From the **Getting started** page, expand the menu on the left.

1. Choose **App authorizations**.

1. Select the option button next to the app authorization that you want to delete.

1. Choose the **Actions** dropdown menu.

1. Choose **Delete**.

1. Choose **Delete** on the delete ingestion dialog box to confirm.

## Delete an app bundle
<a name="delete-app-bundles"></a>

To delete your app bundle, use the following steps:

1. From the **Getting started** page, expand the menu on the left.

1. Choose **App bundle**.

1. Choose the **Delete** button.

1. Type `delete` to confirm, and then choose **Delete**.