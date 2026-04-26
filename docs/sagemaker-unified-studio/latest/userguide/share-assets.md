# Share assets

In the current release of Amazon SageMaker Unified Studio, you can share your Amazon S3 assets, AWS Glue
(SageMaker Lakehouse) assets, and your Amazon QuickSight assets with other projects or
users/groups.

For more information about sharing your Amazon QuickSight assets, see [Share Amazon QuickSight dashboards](share-qs-dashboard.md "share-qs-dashboard.md").

For more information about sharing your Amazon S3 assets, see [Sharing Amazon S3 data](data-s3-publish.md "data-s3-publish.md").

To share your AWS Glue (SageMaker Lakehouse) data, complete the following
procedure:

1. Navigate to Amazon SageMaker Unified Studio using the URL from your admin and log in
   using your SSO or AWS credentials.
2. From the project selector dropdown at the top of the page, choose the project. You can select
   either one of the projects that you created manually or the project that was
   automatically created when you've onboarded your Amazon SageMaker Lakehouse
   data.
3. In the left navigation pane, choose **Data**, then choose the catalog that you
   want to work with under **Lakehouse** and navigate down to the
   database and the table asset that you want to share.
4. Choose the asset that you want to share, then expand
   **Actions**, and choose **Share**.
5. In the **Share table** window, specify the project with which
   you want to share this asset and then choose **Share**.

###### Note

In the current release of Amazon SageMaker Unified Studio, sharing row and column filters is not
supported.
