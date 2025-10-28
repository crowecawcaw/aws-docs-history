# Manually create an asset in

Amazon SageMaker Unified Studio

In Amazon SageMaker Unified Studio, an asset is an entity that presents a single physical data object (for
example, a table, a dashboard, a file) or virtual data object (for example, a view). For
more information, see [Amazon SageMaker Unified Studio terminology and concepts](concepts.md "concepts.md"). Publishing an
asset manually is a one-time operation. You don't specify a run schedule for the asset,
so it's not updated automatically if its source changes.

To manually create an asset through a project, you must be the owner or contributor of
that project.

###### To create an asset manually

1. Navigate to Amazon SageMaker Unified Studio using the URL from your admin and log in
   using your SSO or AWS credentials.
2. Choose **Select project** from the top navigation pane and
   select the project that you want to create an asset in.
3. Under **Project catalog** in the left side navigation, choose
   **Assets**.
4. On the **Inventory** tab, choose **Create**,
   then choose **Create asset**. choose **Create
   asset**.
5. For **Data asset details**, configure the following
   settings:
   - **Name** – The name of the asset.
   - **Description** – A description of the
     asset.

6. Choose **Next**.
7. For **Asset type details**, configure the following
   settings:
   - **Asset type** – The type of asset.
   - **Revision**.

8. If you are adding an **S3 object collection**, for
   **S3 location**, enter the Amazon Resource Name (ARN) of
   the source S3 bucket.

Optionally, enter an S3 access point. For more information, see [Managing data access with Amazon S3 access
points](../../../AmazonS3/latest/userguide/access-points.md "../../../AmazonS3/latest/userguide/access-points.md"). 9. Choose **Next**. 10. Review the selections, then choose **Create**.

After the asset is created, it will be stored in the inventory until you
decide to publish it.
