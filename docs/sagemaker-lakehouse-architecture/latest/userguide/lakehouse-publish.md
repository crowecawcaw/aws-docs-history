# Publishing data in lakehouse architecture

After you have added data in the lakehouse architecture, you can publish the data to share it with other
users in the lakehouse architecture. Data that is published is viewable as an asset in the project catalog
and the Amazon SageMaker Catalog, and other users can create subscription requests in the
Amazon SageMaker Catalog to include that data in their projects.

To publish data in the lakehouse architecture, complete the following steps:

1. Navigate to lakehouse architecture using the URL from your admin and log in
   using your SSO or AWS credentials.
2. Navigate to the project that contains the data that you want to publish in the lakehouse architecture.
   To do this, use the center menu at the top of the landing page and choose **Browse
   all projects**, then choose the name of the project that you want to navigate
   to.
3. In the center menu, choose **Data**. This takes you to the Data
   page.
4. Do either of the following:
   - If you want to publish a regular AWS Glue table, expand the catalog in the data
     navigation to view the list of databases in lakehouse architecture, then choose a database that
     contains the asset that you want to publish. Choose this table from the selected
     database and then proceed to the rest of the steps in this procedure to publish this
     table to the catalog.
   - If you want to publish an Amazon S3 table to the catalog, you must first complete
     the following steps to create a data source for the S3 Tables catalog and schedule its
     run job. Then you can proceed to the rest of the steps in this procedure to publish
     the S3 table to the catalog.
     - Navigate to **Data sources** and then choose **Create
       data source**.
     - On the **Step 1: Define source** page, specify the name for
       this data source, then under **Data source type** - choose
       **AWS Glue (Lakehouse)**, under **Data
       Selection** - choose **Enter the catalog name** and
       then speciy the name of your S3 tables catalog (s3tablescatalog/<catalog
       name>, then choose your database from that catalog (use the drop down menu),
       and then choose **Next**.
     - On the **Step 2: Add details** page, leave all the default
       settings and choose **Next**.
     - On the **Step 3: Set up schedule** page, choose a run
       preference and then choose **Next**.
     - On the **Step 4: review** page, review your selections and
       then choose **Create**.

     Once the data source for the S3 tables catalog is created and run, you can
     proceed with the rest of the steps below to locate your S3 table and publish it to
     the catalog.

5. Expand the **Actions** menu, then choose **Publish to
   catalog**.
6. Confirm the action in the pop-up window by choosing **Publish to
   catalog**.

The lakehouse architecture then fetches metadata for the asset. After a few minutes, the metadata
is fetched and a success message appears. 7. (Optional) Choose **View details** to view the asset in the project
catalog.
When it is successfully published you can view it in the **Assets**
section of the project catalog and users in other projects can subscribe to it from the
Amazon SageMaker Catalog.

You can use the project catalog to re-publish the data if you make changes, or to
unpublish the data from Amazon SageMaker Catalog. For more information, see [Data inventory and publishing](../../../sagemaker-unified-studio/latest/userguide/data-publishing.md "../../../sagemaker-unified-studio/latest/userguide/data-publishing.md").
