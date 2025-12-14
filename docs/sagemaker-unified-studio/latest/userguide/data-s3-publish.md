# Sharing Amazon S3 data

Sharing data with other users in Amazon SageMaker Unified Studio means that you and other users can access the same data in multiple projects.
There are two ways to share data with other users in Amazon SageMaker Unified Studio:

- Publish Amazon S3 data to the catalog. This means that other projects can create
  subscription requests to request access to the data you publish. When you approve a subscription request,
  the other project will then have access to that data.
- Share Amazon S3 data directly with consumers. This means that the data you share is available to
  the projects you specify right away, without needing a subscription process.
  In both cases, you can track and manage access to your data in the **Project catalog** page of your project in Amazon SageMaker Unified Studio. You have the option to choose whether to grant read-only or read and write access.

Amazon SageMaker Unified Studio grants access to subscribed assets using Amazon S3 Access Grants. When a subscription is revoked, a project member may still get Amazon S3 Access Grants credentials for up to 5 minutes, and credentials can be used for 15 minutes.
As a result, a user may have access to the data for up to 20 minutes after the access is revoked in SageMaker Unified Studio.

## Publish Amazon S3 data to the catalog

When you publish data to the Amazon SageMaker Catalog, other projects in your Amazon SageMaker Unified Studio domain can create
subscription requests to request access to the data you published. When you approve a subscription request,
the other project will then have access to that data.

1. Navigate to Amazon SageMaker Unified Studio using the URL from your admin and log in
   using your SSO or AWS credentials.
2. Navigate to the project that contains your Amazon S3 connection.
3. On the **Data** page, in the side navigation,
   choose **S3** to explore your S3 data assets.
4. Choose the name of the S3 folder or bucket you want to publish.
5. Choose **Actions**, then choose **Publish to Catalog**.
   A confirmation window appears.
6. Choose **Publish** to confirm that you want the S3 data to be discoverable in the Amazon SageMaker Catalog.
   This means that members of other projects in the domain can create subscription requests for the data asset.
   When you review subscription requests, you will have the option to grant read-only or read and write access to the data.
   If you approve the subscription request, they will have access to the S3 data asset in their project.

The S3 data folder or bucket you published then appears in the Amazon SageMaker Catalog as a data asset of type
**S3 Object Collection**.

## Share Amazon S3 data directly with consumers

Sharing data directly in this way makes it so that the data you share is available to
the projects you specify right away, without needing a subscription process. You will first publish your dataset, and then share it.

1. Navigate to Amazon SageMaker Unified Studio using the URL from your admin and log in
   using your SSO or AWS credentials.
2. Navigate to the project that contains your Amazon S3 connection.
3. On the **Data** page, in the side navigation, explore your S3 data assets.
4. Choose the name of the S3 folder or bucket you want to publish.
5. Choose **Actions**, then choose **Publish to Catalog**. A confirmation window appears.
6. Choose **Publish**
7. Navigate to the **Assets**page from the left navigation and select the asset you want to share.
8. Choose **Actions**, then choose **Share**.
9. Use the dropdown to select projects that you want to share the S3 data with, then choose **Next**.
10. Select the access type. For read-only access, move to the next step. To grant read and write access to users in the other project, select **Read and write access**.
11. Choose **Share**.

The S3 data asset is then shown in the project catalog under approved subscrion
requests. You can choose to revoke access at any time. For more information about
subscription requests, see [Data discovery, subscription, and consumption](discover-data.md "discover-data.md").
