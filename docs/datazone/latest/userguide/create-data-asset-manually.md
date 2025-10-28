# Manually create an asset in

Amazon DataZone

In Amazon DataZone, an asset is an entity that presents a single physical data object (for
example, a table, a dashboard, a file) or virtual data object (for example, a view). For
more information, see [Amazon DataZone terminology and concepts](datazone-concepts.md "datazone-concepts.md"). Publishing an asset manually is a one-time
operation. You don't specify a run schedule for the asset, so it's not updated
automatically if its source changes.

To manually create an asset through a project, you must be the owner or the
contributor of that project.

###### To create an asset manually

1. Navigate to the Amazon DataZone data portal URL and sign in using single sign-on
   (SSO) or your AWS credentials. If you’re an Amazon DataZone administrator, you can
   navigate to the Amazon DataZone console at [https://console.aws.amazon.com/datazone](https://console.aws.amazon.com/datazone "https://console.aws.amazon.com/datazone") and sign in with the
   AWS account where the domain was created, then choose **Open data
   portal**.
2. Choose **Select project** from the top navigation pane and
   select the project to which to create the asset.
3. Navigate to the **Data** tab for the project.
4. Choose **Data sources** from the left navigation pane, then
   choose **Create data asset**.
5. For **Asset details**, configure the following
   settings:
   - **Asset type** – The type of asset.
   - **Name** – The name of the asset.
   - **Description** – A description of the
     asset.

6. For **S3 location**, enter the Amazon Resource Name (ARN) of
   the source S3 bucket.

Optionally, enter an S3 access point. For more information, see [Managing data access with Amazon S3 access
points](../../../AmazonS3/latest/userguide/access-points.md "../../../AmazonS3/latest/userguide/access-points.md"). 7. For **Publishing settings**, choose whether assets are
immediately discoverable in the catalog. If you only add them to the inventory,
you can choose subscription terms later to publish them to the catalog. 8. Choose **Create**.

Once the asset is created, it will either be directly published as an active
asset in the catalog, or will be stored in the inventory until you decide to
publish it.
