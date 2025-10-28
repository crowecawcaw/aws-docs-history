# Publish assets to the Amazon DataZone catalog from

the project inventory

You can publish Amazon DataZone assets and their metadata from project inventories into the
Amazon DataZone catalog. You can only publish the most recent version of an asset to the
catalog.

Consider the following when publishing assets to the catalog:

- To publish an asset to the catalog, you must be the owner or the contributor
  of that project.
- For Amazon Redshift assets, ensure that the Amazon Redshift clusters associated with both
  publisher and subscriber clusters meet all the requirements for Amazon Redshift data
  sharing in order for Amazon DataZone to manage access for Redshift tables and views.
  See [Data sharing concepts for
  Amazon Redshift](../../../redshift/latest/dg/concepts.md "../../../redshift/latest/dg/concepts.md").
- Amazon DataZone only supports access management for assets published from the
  AWS Glue Data Catalog and Amazon Redshift. For all other assets, such as Amazon S3 objects, Amazon DataZone
  does not manage access for approved subscribers. If you subscribe to these
  unmanaged assets, you're notified with the following message:

`Subscription approval does not provide access to data. Subscription
 grants on this asset are not managed by Amazon DataZone. For more information or
 help, reach out to your administrator.`

## Publish an asset in Amazon DataZone

If you didn't choose to make assets immediately discoverable in the data catalog
when you created a data source, perform the following steps to publish them
later.

###### To publish an asset

1. Navigate to the Amazon DataZone data portal URL and sign in using single
   sign-on (SSO) or your AWS credentials. If you’re an Amazon DataZone
   administrator, you can navigate to the Amazon DataZone console at [https://console.aws.amazon.com/datazone](https://console.aws.amazon.com/datazone "https://console.aws.amazon.com/datazone") and sign in with the
   AWS account where the domain was created, then choose **Open data
   portal**.
2. Choose **Select project** from the top navigation pane
   and select the project to which the asset belongs.
3. Navigate to the **Data** tab for the project.
4. Choose **Inventory data** from the left navigation pane,
   then select the asset that you want to publish.

###### Note

By default, all assets require subscription approval, which means a
data owner must approve all subscription requests to the asset. If you
want to change this setting before publishing the asset, open the asset
details and choose **Edit** next to
**Subscription approval**. You can change this
setting later by modifying and re-publishing the asset. 5. Choose **Publish asset**. The asset is directly published
to the catalog.

If you make changes to the asset, such as modifying its approval
requirements , you can choose
**Re-publish** to publish the updates to the
catalog.
