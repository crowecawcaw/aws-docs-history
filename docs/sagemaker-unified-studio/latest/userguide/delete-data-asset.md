# Delete an Amazon SageMaker Unified Studio asset

When you no longer need an asset in Amazon SageMaker Unified Studio, you can permanently delete it. Deleting
an asset is different than unpublishing an asset from the catalog. You can delete an
asset and its related listing in the catalog so that it's not visible in any search
results. To delete the asset listing, you must first revoke all of its subscriptions.

To delete an asset, you must be the owner or the contributor of the project to which
the asset belongs.

###### Note

In order to delete an asset listing, you must first revoke all existing
subscriptions to the asset, and the asset must be removed from all data products.
You can't delete an asset listing that has existing subscribers or that is included
in a current data product.

###### To delete an asset

1. Navigate to Amazon SageMaker Unified Studio using the URL from your admin and log in
   using your SSO or AWS credentials.
2. Choose **Select project** from the top navigation pane and
   select the project to which the asset belongs.
3. Under **Project catalog** in the left side navigation, choose
   **Assets**.
4. On the **Inventory** tab, choose the name of the asset that
   you want to unpublish. This opens the asset details page.
5. Expand the **Actions** menu, then choose
   **Delete**.
6. In the pop-up window, type `delete` to confirm deletion, then
   choose **Delete**.

When the asset is deleted, it's no longer available to view or subscribe
to.
