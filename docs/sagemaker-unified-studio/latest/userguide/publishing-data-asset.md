# Publish assets to the Amazon SageMaker Unified Studio catalog from the

project inventory

You can publish Amazon SageMaker Unified Studio assets and their metadata from project inventories into the
Amazon SageMaker Unified Studio catalog. You can only publish the most recent version of an asset to the
catalog.

Consider the following when publishing assets to the catalog:

- To publish an asset to the catalog, you must be the owner or contributor of
  the project that contains the asset.
- For Amazon Redshift assets, ensure that the Amazon Redshift clusters associated with both
  publisher and subscriber clusters meet all the requirements for Amazon Redshift data
  sharing in order for Amazon SageMaker Unified Studio to manage access for Redshift tables and views.
  See [Data sharing concepts for
  Amazon Redshift](../../../redshift/latest/dg/concepts.md "../../../redshift/latest/dg/concepts.md").

## Publish an asset in Amazon SageMaker Unified Studio

If you didn't choose to make assets immediately discoverable in the data catalog
when you created a data source, perform the following steps to publish them
later.

###### To publish an asset

1. Navigate to Amazon SageMaker Unified Studio using the URL from your admin and log in
   using your SSO or AWS credentials.
2. Choose **Select project** from the top navigation pane
   and select the project to which the asset belongs.
3. Under **Project catalog** in the left side navigation,
   choose **Assets**.
4. Make sure you are on the **Inventory** tab, then choose
   the name of the asset that you want to publish. You are then brought to the
   asset details page.

###### Note

By default, all assets require subscription approval, which means a
data owner must approve all subscription requests to the asset. If you
want to change this setting before publishing the asset, open the asset
details and choose **Edit** next to
**Subscription approval**. You can change this
setting later by modifying and re-publishing the asset. 5. Choose **Publish asset**. The asset is directly published
to the catalog.

If you make changes to the asset, such as modifying its approval
requirements, you can choose
**Re-publish asset** to publish the updates to the
catalog.
