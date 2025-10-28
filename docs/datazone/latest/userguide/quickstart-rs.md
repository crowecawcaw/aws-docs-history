# Amazon DataZone quickstart with Amazon Redshift data

Complete the following quickstart steps to run through the complete data producer and data
consumer workflows in Amazon DataZone with sample Amazon Redshift data.

###### Quickstart steps

- [Step 1 - Create the Amazon DataZone domain and data
  portal](#create-domain-gs-rs "#create-domain-gs-rs")
- [Step 2 - Create the publishing
  project](#create-publishing-project-gs-rs "#create-publishing-project-gs-rs")
- [Step 3 - Create the environment](#create-environment-gs-rs "#create-environment-gs-rs")
- [Step 4 - Produce data for
  publishing](#produce-data-for-publishing-gs-rs "#produce-data-for-publishing-gs-rs")
- [Step 5 - Gather metadata from Amazon
  Redshift](#gather-metadata-from-glue-gs-rs "#gather-metadata-from-glue-gs-rs")
- [Step 6 - Curate and publish the data asset](#curate-data-asset-gs-rs "#curate-data-asset-gs-rs")
- [Step 7 - Create the project for
  data analysis](#create-project-for-data-analysis-gs-rs "#create-project-for-data-analysis-gs-rs")
- [Step 8 - Create an environment for data
  analysis](#create-environment-gs2-rs "#create-environment-gs2-rs")
- [Step 9 - Search the data catalog and
  subscribe to data](#search-catalog-subscribe-gs-rs "#search-catalog-subscribe-gs-rs")
- [Step 10 - Approve the subscription
  request](#approve-subscription-request-gs-rs "#approve-subscription-request-gs-rs")
- [Step 11 - Build a query and analyze data in Amazon
  Redshift](#analyze-data-gs-rs "#analyze-data-gs-rs")

## Step 1 - Create the Amazon DataZone domain and data

portal

Complete the following procedure to create an Amazon DataZone domain. For more information
about Amazon DataZone domains, see [Amazon DataZone terminology and concepts](datazone-concepts.md "datazone-concepts.md").

1. Navigate to the Amazon DataZone console at [https://console.aws.amazon.com/datazone](https://console.aws.amazon.com/datazone "https://console.aws.amazon.com/datazone"), sign in, and then choose
   **Create domain**.

###### Note

If you want to use an existing Amazon DataZone domain for this workflow, choose
View domains, then choose the domain that you want to use, and then
proceed to Step 2 of creating a publishing project. 2. On the **Create domain** page, provide values for the following
fields:

    * **Name** - specify a name for your domain. For the purposes of
     this workflow, you can call this domain `Marketing`.
    * **Description** - specify an optional domain
     description.
    * **Data encryption** - your data is encrypted by default with a
     key that AWS owns and manages for you. For this walkthrough, you can leave the
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
    * **Service access** - choose the **Use a custom service
     role** option and then choose the
     **AmazonDataZoneDomainExecutionRole** from the drop-down
     menu.
    * Under **Quick setup**, choose **Set up this account for
     data consumption and publishing**. This option enables the built-in
     Amazon DataZone blueprints of **Data lake** and **Data
     warehouse**, and configures the required permissions and resources to
     complete the rest of the steps in this workflow. For more information about
     Amazon DataZone blueprints, see [Amazon DataZone terminology and concepts](datazone-concepts.md "datazone-concepts.md").
    * Keep the remaining fields under **Permissions details** and
     **Tags** unchanged and then choose **Create
     domain**.

3. Once the domain is successfully created, choose this domain, and on the domain's
   summary page, note the **Data portal URL** for this domain. You can use
   this URL to access your Amazon DataZone data portal in order to complete the rest of the
   steps in this workflow.

###### Note

In the current release of Amazon DataZone, once the domain is created, the URL generated
for the data portal cannot be modified.

Domain creation can take several minutes to complete. Wait for the domain to have a
status of **Available** before proceeding to the next step.

## Step 2 - Create the publishing

project

The following section describes the steps of creating the publishing project in this
workflow.

1. Once you complete Step 1, navigate to the Amazon DataZone data portal using the data
   portal URL and log in using your single sign-on (SSO) or AWS IAM credentials.
2. Choose **Create project**, specify the project name, for example,
   for this workflow, you can name it **SalesDataPublishingProject**, then
   leave the rest of the fields unchanged, and then choose
   **Create**.

## Step 3 - Create the environment

The following section describes the steps of creating an environment in this
workflow.

1.  Once you complete Step 2, in the Amazon DataZone data portal, choose the
    `SalesDataPublishingProject` project that you created in the previous step,
    then choose the **Environments** tab, and then choose **Create
    environment**.
2.  On the **Create environment** page, specify the following and then
    choose **Create environment**.
    - **Name** - specify the name for the environment. For this
      walkthrough, you can call it `Default data warehouse environment`.
    - **Description** - specify a description for the
      environment.
    - **Environment profile** - choose the
      **DataWarehouseProfile** environment profile.
    - Provide the name of your Amazon Redshift cluster, database name, and the secret
      ARN for the Amazon Redshift cluster where your data is stored.

    ###### Note

    Make sure that your secret in AWS Secrets Manager includes the following
    tags (key/value):

        + For Amazon Redshift cluster - datazone.rs.cluster:
         <cluster\_name:database name>


        For Amazon Redshift Serverless workgroup - datazone.rs.workgroup:
         <workgroup\_name:database\_name>
        + AmazonDataZoneProject: <projectID>
        + AmazonDataZoneDomain: <domainID>For more information, see [Storing database credentials in AWS Secrets Manager](../../../redshift/latest/mgmt/data-api-access.md#data-api-secrets "../../../redshift/latest/mgmt/data-api-access.md#data-api-secrets").

    The database user you provide in the AWS Secrets Manager must have super
    user permissions.

## Step 4 - Produce data for

publishing

The following section describes the steps of producing data for publishing in this
workflow.

1. Once you complete Step 3, in the Amazon DataZone data portal, choose the
   `SalesDataPublishingProject` project, and then, in the right-hand panel,
   under **Analytics tools**, choose **Amazon Redshift**.
   This opens the Amazon Redshift query editor using your project’s credentials for
   authentication.
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

Make sure that the **mkt_sls_table** table is successfully created.
Now you have a data asset that can be published into the Amazon DataZone catalog.

## Step 5 - Gather metadata from Amazon

Redshift

The following section describes the steps of gathering metadata from Amazon
Redshift.

1. Once you complete Step 4, in the Amazon DataZone data portal, choose the
   `SalesDataPublishingProject` project, then choose the
   **Data** tab, and then choose **Data
   sources**.
2. Choose the source that was created as part of the environment creation process.
3. Choose **Run** next to the **Action** dropdown
   menu and then choose the refresh button. Once the data source run is complete, the
   assets are added to the Amazon DataZone inventory.

## Step 6 - Curate and publish the data asset

The following section describes the steps of curating and publishing the data asset in
this workflow.

1. Once you complete step 5, in the Amazon DataZone data portal, choose the
   `SalesDataPublishingProject` project, then choose the
   **Data** tab, choose **Inventory data**, and locate
   the `mkt_sls_table` table.
2. Open `mkt_sls_table` asset's details page to see the automatically
   generated business names. Choose the **Automatically generated
   metadata** icon to view the auto-generated names for asset and columns. You
   can either accept or reject each name individually or choose **Accept
   all** to apply the generated names. Optionally, you can also add the
   available metadata form to your asset and select glossary terms to classify your
   data.
3. Choose **Publish** to publish the `mkt_sls_table`
   asset.

## Step 7 - Create the project for

data analysis

The following section describes the steps of creating te project for data analysis in
this workflow.

1. Once you complete Step 6, in the Amazon DataZone data portal, choose **Create
   project**.
2. In the **Create project** page, specify the project name, for
   example, for this workflow, you can name it
   **MarketingDataAnalysisProject**, then leave the rest of the fields
   unchanged, and then choose **Create**.

## Step 8 - Create an environment for data

analysis

The following section describes the steps of creating an environment for data analysis
in this workflow.

1.  Once you complete Step 7, in the Amazon DataZone data portal, choose the
    `MarketingDataAnalysisProject` project that you created in the previous
    step, then choose the **Environments** tab, and then choose
    **Add environment**.
2.  On the **Create environment** page, specify the following and then
    choose **Create environment**.
    - **Name** - specify the name for the environment. For this
      walkthrough, you can call it `Default data warehouse environment`.
    - **Description** - specify a description for the
      environment.
    - **Environment profile** - choose
      **DataWarehouseProfile** environment profile.
    - Provide the name of your Amazon Redshift cluster, database name, and the secret
      ARN for the Amazon Redshift cluster where your data is stored.

    ###### Note

    Make sure that your secret in AWS Secrets Manager includes the following
    tags (key/value):

        + For Amazon Redshift cluster - datazone.rs.cluster:
         <cluster\_name:database name>


        For Amazon Redshift Serverless workgroup - datazone.rs.workgroup:
         <workgroup\_name:database\_name>
        + AmazonDataZoneProject: <projectID>
        + AmazonDataZoneDomain: <domainID>For more information, see [Storing database credentials in AWS Secrets Manager](../../../redshift/latest/mgmt/data-api-access.md#data-api-secrets "../../../redshift/latest/mgmt/data-api-access.md#data-api-secrets").

    The database user you provide in the AWS Secrets Manager must have super
    user permissions.
    - For this walkthrough, keep the rest of the fields unchanged.

## Step 9 - Search the data catalog and

subscribe to data

The following section describes the steps of searching the data catalog and subscribing
to data.

1. Once you complete Step 8, in the Amazon DataZone data portal, search for data assets
   using keywords (e.g., 'catalog' or 'sales') in the data portal's
   **Search** bar.

If necessary, apply filters or sorting, and once you locate the Product Sales Data
asset, you can choose it to open the asset's details page. 2. On the Product Sales Data asset's details page, choose
**Subscribe**. 3. In the dialog, choose your consumer project from the dropdown, provide the reason
for access request, and then choose **Subscribe**.

## Step 10 - Approve the subscription

request

The following section describes the steps of approving the subscription request in this
workflow.

1. Once you complete Step 9, in the Amazon DataZone data portal, choose the
   **SalesDataPublishingProject** project with which you published your
   asset.
2. Choose the **Data** tab, then **Published data**,
   and then **Incoming requests**.
3. Choose the view request link and then choose **Approve**.

## Step 11 - Build a query and analyze data in Amazon

Redshift

Now that you have successfully published an asset to the Amazon DataZone catalog and
subscribed to it, you can analyze it.

1. In the Amazon DataZone data portal, on the right-hand panel, click the Amazon Redshift
   link. This opens the Amazon Redshift query editor using project’s credential for
   authentication.
2. You can now run a query (select statement) on the subscribed table. You can click on
   the table (three-vertical-dots option) and choose preview to have select statement on
   the editor screen. Execute the query to see the results.
