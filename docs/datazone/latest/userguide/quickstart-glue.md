# Amazon DataZone quickstart with AWS Glue data

Complete the following quickstart steps to run through the complete data producer and data
consumer workflows in Amazon DataZone with sample AWS Glue data.

###### Quickstart steps

- [Step 1 - Create the Amazon DataZone domain and data
  portal](#create-domain-gs-glue "#create-domain-gs-glue")
- [Step 2 - Create the publishing
  project](#create-publishing-project-gs-glue "#create-publishing-project-gs-glue")
- [Step 3 - Create the environment](#create-environment-gs-glue "#create-environment-gs-glue")
- [Step 4 - Produce data for
  publishing](#produce-data-for-publishing-gs-glue "#produce-data-for-publishing-gs-glue")
- [Step 5 - Gather metadata from AWS
  Glue](#gather-metadata-from-glue-gs-glue "#gather-metadata-from-glue-gs-glue")
- [Step 6 - Curate and publish the data
  asset](#curate-data-asset-gs-glue "#curate-data-asset-gs-glue")
- [Step 7 - Create the project for
  data analysis](#create-project-for-data-analysis-gs-glue "#create-project-for-data-analysis-gs-glue")
- [Step 8 - Create an environment for data
  analysis](#create-environment-gs2-glue "#create-environment-gs2-glue")
- [Step 9 - Search the data catalog and
  subscribe to data](#search-catalog-subscribe-gs-glue "#search-catalog-subscribe-gs-glue")
- [Step 10 - Approve the subscription
  request](#approve-subscription-request-gs-glue "#approve-subscription-request-gs-glue")
- [Step 11 - Build a query and analyze data in Amazon
  Athena](#analyze-data-gs-glue "#analyze-data-gs-glue")

## Step 1 - Create the Amazon DataZone domain and data

portal

This section describes the steps of creating an Amazon DataZone domain and data portal for
this workflow.

Complete the following procedure to create an Amazon DataZone domain. For more information
about Amazon DataZone domains, see [Amazon DataZone terminology and concepts](datazone-concepts.md "datazone-concepts.md").

1. Navigate to the Amazon DataZone console at [https://console.aws.amazon.com/datazone](https://console.aws.amazon.com/datazone "https://console.aws.amazon.com/datazone"), sign in, and then choose
   **Create domain**.

###### Note

If you want to use an existing Amazon DataZone domain for this workflow, choose
**View domains**, then choose the domain that you want to use, and
then proceed to Step 2 of creating a publishing project. 2. On the **Create domain** page, provide values for the following
fields:

    * **Name** - specify a name for your domain. For the purposes of
     this workflow, you can call this domain **Marketing**.
    * **Description** - specify an optional domain
     description.
    * **Data encryption** - your data is encrypted by default with a
     key that AWS owns and manages for you. For this use case, you can leave the
     default data encryption settings.


    For more information about using customer managed keys, see [Data encryption at rest for Amazon DataZone](encryption-rest-datazone.md "encryption-rest-datazone.md"). If
     you use your own KMS key for data encryption, you must include the following
     statement in your default [AmazonDataZoneDomainExecutionRole](AmazonDataZoneDomainExecutionRole.md "AmazonDataZoneDomainExecutionRole.md").



    JSON





    ```
    `{
     "Version":"2012-10-17",
     "Statement": [
     {
     "Sid": "Statement1",
     "Effect": "Allow",
     "Action": [
     "kms:Decrypt",
     "kms:DescribeKey",
     "kms:GenerateDataKey"
     ],
     "Resource": [
     "arn:aws:kms:us-east-1:111122223333:key/1234abcd-12ab-34cd-56ef-1234567890ab"
     ]
     }
     ]
    }`

    ```
    * **Service access** - leave the selected by default
     **Use a default role** option unchanged.


    ###### Note

    If you are using an existing Amazon DataZone domain for this workflow, you can
     choose **Use an existing service role** option and then choose an
     existing role from the drop-down menu.
    * Under **Quick setup**, choose **Set up this account for
     data consumption and publishing**. This option enables the built-in
     Amazon DataZone blueprints of **Data lake** and **Data
     warehouse**, and configures the required permissions, resources, a
     default project, and default data lake and data warehouse environment profiles for
     this account. For more information about Amazon DataZone blueprints, see [Amazon DataZone terminology and concepts](datazone-concepts.md "datazone-concepts.md").
    * Keep the remaining fields under **Permissions details**
     unchanged.


    ###### Note

    If you have an existing Amazon DataZone domain, you can choose the **Use an
     existing service role** option and then choose an existing role from
     the drop-down menu for the **Glue Manage Access role**,
     **Redshift Manage Access role**, and **Provisioning
     role**.
    * Keep the fields under **Tags** unchanged.
    * Choose **Create domain**.

3. Once the domain is successfully created, choose this domain, and on the domain's
   summary page, note the **Data portal URL** for this domain. You can use
   this URL to access your Amazon DataZone data portal in order to complete the rest of the
   steps in this workflow. You can also navigate to the data portal by choosing
   **Open data portal**.

###### Note

In the current release of Amazon DataZone, once the domain is created, the URL generated
for the data portal cannot be modified.

Domain creation can take several minutes to complete. Wait for the domain to have a
status of **Available** before proceeding to the next step.

## Step 2 - Create the publishing

project

This section describes the steps required to create the publishing project for this
workflow.

1. Once you complete Step 1 above and create a domain, you'll see the **Welcome
   to Amazon DataZone!** window. In this window, choose **Create
   project**.
2. Specify the project name, for example, for this workflow, you can name it
   **SalesDataPublishingProject**, then leave the rest of the fields
   unchanged, and then choose **Create**.

## Step 3 - Create the environment

This section describes the steps required to create an environment for this
workflow.

1. Once you complete Step 2 above and create your project, you'll see the
   **Your project is ready to use** window. In this window, choose
   **Create environment**.
2. On the **Create environment** page, specify the following and then
   choose **Create environment**.
3. Specify values for the following:
   - **Name** - specify the name for the environment. For this
     walkthrough, you can call it `Default data lake environment`.
   - **Description** - specify a description for the
     environment.
   - **Environment profile** - choose the
     **DataLakeProfile** environment profile. This enables you to use
     Amazon DataZone in this workflow to work with data in Amazon S3, AWS Glue Catalog, and
     Amazon Athena.
   - For this walkthrough, keep the rest of the fields unchanged.

4. Choose **Create environment**.

## Step 4 - Produce data for

publishing

This section describes the steps required to produce data for publishing in this
workflow.

1. Once you complete step 3 above, in your `SalesDataPublishingProject`
   project, in the right-hand panel, under **Analytics tools**, choose
   **Amazon Athena**. This opens the Athena query editor using your
   project’s credentials for authentication. Make sure that your publishing environment is
   selected in the **Amazon DataZone environment** dropdown and the
   `<environment_name>%_pub_db` database is selected as in the query
   editor.
2. For this walkthrough, you are using the **Create Table as Select**
   (CTAS) query script to create a new table that you want to publish to Amazon DataZone. In
   your query editor, execute this CTAS script to create a `mkt_sls_table` table
   that you can publish and make available for search and subscription.

```

CREATE TABLE mkt_sls_table AS
SELECT 146776932 AS ord_num, 23 AS sales_qty_sld, 23.4 AS wholesale_cost, 45.0 as lst_pr, 43.0 as sell_pr, 2.0 as disnt, 12 as ship_mode,13 as warehouse_id, 23 as item_id, 34 as ctlg_page, 232 as ship_cust_id, 4556 as bill_cust_id
UNION ALL SELECT 46776931, 24, 24.4, 46, 44, 1, 14, 15, 24, 35, 222, 4551
UNION ALL SELECT 46777394, 42, 43.4, 60, 50, 10, 30, 20, 27, 43, 241, 4565
UNION ALL SELECT 46777831, 33, 40.4, 51, 46, 15, 16, 26, 33, 40, 234, 4563
UNION ALL SELECT 46779160, 29, 26.4, 50, 61, 8, 31, 15, 36, 40, 242, 4562
UNION ALL SELECT 46778595, 43, 28.4, 49, 47, 7, 28, 22, 27, 43, 224, 4555
UNION ALL SELECT 46779482, 34, 33.4, 64, 44, 10, 17, 27, 43, 52, 222, 4556
UNION ALL SELECT 46779650, 39, 37.4, 51, 62, 13, 31, 25, 31, 52, 224, 4551
UNION ALL SELECT 46780524, 33, 40.4, 60, 53, 18, 32, 31, 31, 39, 232, 4563
UNION ALL SELECT 46780634, 39, 35.4, 46, 44, 16, 33, 19, 31, 52, 242, 4557
UNION ALL SELECT 46781887, 24, 30.4, 54, 62, 13, 18, 29, 24, 52, 223, 4561

```

Make sure that the **mkt_sls_table** table is successfully created
in the **Tables and views** section on the left-hand side. Now you have
a data asset that can be published into the Amazon DataZone catalog.

## Step 5 - Gather metadata from AWS

Glue

This section describes the step of gathering metadata from AWS Glue for this
workflow.

1. Once you complete step 4 above, in the Amazon DataZone data portal, choose the
   `SalesDataPublishingProject` project, then choose the
   **Data** tab, and then choose **Data sources** in
   the left-hand panel.
2. Choose the source that was created as part of the environment creation process.
3. Choose **Run** next to the **Action** dropdown
   menu and then choose the refresh button. Once the data source run is complete, the
   assets are added to the Amazon DataZone inventory.

## Step 6 - Curate and publish the data

asset

This section describes the steps of curating and publishing the data asset in this
workflow.

1. Once you complete step 5 above, in the Amazon DataZone data portal, choose the
   `SalesDataPublishingProject` project that you created in the previous step,
   choose the **Data** tab, choose **Inventory data** in
   the left-hand panel, and locate the `mkt_sls_table` table.
2. Open `mkt_sls_table` asset's details page to see the automatically
   generated business names. Choose the **Automatically generated
   metadata** icon to view the auto-generated names for asset and columns. You
   can either accept or reject each name individually or choose **Accept
   all** to apply the generated names. Optionally, you can also add the
   available metadata form to your asset and select glossary terms to classify your
   data.
3. Choose **Publish asset** to publish the `mkt_sls_table`
   asset.

## Step 7 - Create the project for

data analysis

This section describes the steps of creating the project for data analysis. This is the
beginning of the data consumer steps of this workflow.

1. Once you complete step 6 above, in the Amazon DataZone data portal, choose
   **Create project** from the **Project** drop-down
   menu.
2. On the **Create project** page, specify the project name, for
   example, for this workflow, you can name it
   **MarketingDataAnalysisProject**, then leave the rest of the fields
   unchanged, and then choose **Create**.

## Step 8 - Create an environment for data

analysis

This section describes the steps of creating an environment for data analysis.

1. Once you complete step 7 above, in the Amazon DataZone data portal, choose the
   `MarketingDataAnalysisProject` project, then choose the
   **Environments** tab, and then choose **Create
   environment**.
2. On the **Create environment** page, specify the following and then
   choose **Create environment**.
   - **Name** - specify the name for the environment. For this
     walkthrough, you can call it `Default data lake environment`.
   - **Description** - specify a description for the
     environment.
   - **Environment profile** - choose the built-in
     **DataLakeProfile** environment profile.
   - For this walkthrough, keep the rest of the fields unchanged.

## Step 9 - Search the data catalog and

subscribe to data

This section describes the steps of searching the data catalog and subscribing to
data.

1. Once you complete step 8 above, in the Amazon DataZone data portal, choose the Amazon DataZone
   icon, and in the Amazon DataZone **Search** field, search for data assets
   using keywords (e.g., 'catalog' or 'sales') in the data portal's
   **Search** bar.

If necessary, apply filters or sorting, and once you locate the **Product
Sales Data** asset, you can choose it to open the asset's details
page. 2. On the **Catalog Sales Data** asset's details page, choose
**Subscribe**. 3. In the **Subscribe** dialog, choose your
**MarketingDataAnalysisProject** consumer project from the dropdown,
then specify the reason for your subscription request, and then choose
**Subscribe**.

## Step 10 - Approve the subscription

request

This section describes the steps of approving the subscription request.

1. Once you complete step 9 above, in the Amazon DataZone data portal, choose the
   **SalesDataPublishingProject** project with which you published your
   asset.
2. Choose the **Data** tab, then **Published data**,
   and then chose **Incoming requests**.
3. Now you can see the row for the new request that needs an approval. Choose
   **View request**. Provide a reason for approval and choose
   **Approve**.

## Step 11 - Build a query and analyze data in Amazon

Athena

Now that you have successfully published an asset to the Amazon DataZone catalog and
subscribed to it, you can analyze it.

1. In the Amazon DataZone data portal, choose your
   **MarketingDataAnalysisProject** consumer project and then, from the
   right-hand panel, under **Analytics tools**, choose the **Query
   data** link with Amazon Athena. This opens the Amazon Athena query editor
   using your project’s credentials for authentication. Choose the
   **MarketingDataAnalysisProject** consumer environment from the
   **Amazon DataZone Environment** dropdown in the query editor and then
   choose your project's `<environment_name>%sub_db` from the database
   dropdown.
2. You can now run queries on the subscribed table. You can choose the table from
   **Tables and Views**, and then choose **Preview** to
   have the select statement on the editor screen. Run the query to see the results.
