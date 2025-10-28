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
2. From the top center menu, choose **Browse all
   projects**.
3. Select the name of the project to navigate to that project. You can select
   either one of the projects that you created manually or the project that was
   automatically created when you've onboarded your Amazon SageMaker Lakehouse
   data.
4. Choose the **Data** tab, then choose the catalog that you
   want to work with under **Lakehose** and navigate down to the
   database and the table asset that you want to share.
5. Choose the asset that you want to share, then expand
   **Actions**, and choose **Share**.
6. In the **Share table** window, specify the project with which
   you want to share this asset and then choose **Share**.

###### Note

In the current release of Amazon SageMaker Unified Studio, sharing row and column filters is not
supported.
