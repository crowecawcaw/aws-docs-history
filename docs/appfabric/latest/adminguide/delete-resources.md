# Delete AWS AppFabric for security resources

If you don't want to continue using AWS AppFabric for security, be sure to delete the data in the output
locations you created during setup and your AppFabric for security resources to avoid incurring additional
charges. To clean up your AppFabric resources, you must delete the resources in the reverse
order in which you created them for each software as a service (SaaS) application: **Ingestion destinations** > **Ingestions** > **App authorization** >
**App bundles**

After you’ve deleted your final app authorization, you can delete the app bundle.

###### Topics

- [Delete an ingestion destination](#delete-ingestion-destinations "#delete-ingestion-destinations")
- [Delete an ingestion](#delete-ingestions "#delete-ingestions")
- [Delete an app authorization](#delete-app-authorizations "#delete-app-authorizations")
- [Delete an app bundle](#delete-app-bundles "#delete-app-bundles")

## Delete an ingestion destination

If you select an output location when you create an ingestion, AppFabric for security creates ingestion
destinations on your behalf. To delete an ingestion destination, use the following
steps:

1. Open the AppFabric console at [https://console.aws.amazon.com/appfabric/](https://console.aws.amazon.com/appfabric/ "https://console.aws.amazon.com/appfabric/").
2. From the **Getting started** page, expand the menu on the
   left.
3. Choose **Ingestions**.
4. Choose an app authorization.
5. Select the option button next to the destination that you want to delete and
   choose **Delete**.
6. Choose **Delete** on the delete destination dialog box to
   confirm.
7. Repeat the above steps for all of your destinations.

## Delete an ingestion

To delete an ingestion, use the following steps:

1. From the **Getting started** page, expand the menu on the
   left.
2. Choose **Ingestions**.
3. Select the option button that is next to your app authorization.
4. Choose the **Actions** dropdown menu.
5. Choose **Delete**.
6. Choose **Delete** on the delete ingestion dialog box to
   confirm.

## Delete an app authorization

To delete an app authorization, use the following steps:

1. From the **Getting started** page, expand the menu on the
   left.
2. Choose **App authorizations**.
3. Select the option button next to the app authorization that you want to
   delete.
4. Choose the **Actions** dropdown menu.
5. Choose **Delete**.
6. Choose **Delete** on the delete ingestion dialog box to
   confirm.

## Delete an app bundle

To delete your app bundle, use the following steps:

1. From the **Getting started** page, expand the menu on the
   left.
2. Choose **App bundle**.
3. Choose the **Delete** button.
4. Type `delete` to confirm, and then choose
   **Delete**.
