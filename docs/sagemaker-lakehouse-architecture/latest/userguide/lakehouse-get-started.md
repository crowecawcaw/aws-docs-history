# Getting started with the lakehouse architecture of Amazon SageMaker

This guide helps you accomplish common tasks like finding relevant datasets, running SQL
queries against your data warehouse and data lake simultaneously, collaborating with team
members through data publishing, and maintaining data governance standards. Your administrator
will provide the necessary access permissions and project roles to get started.

###### Topics

- [Prerequisites](#lakehouse-get-started-prerequisites "#lakehouse-get-started-prerequisites")
- [Create a project](#lakehouse-create-project "#lakehouse-create-project")
- [Browse data](#lakehouse-get-started-browse "#lakehouse-get-started-browse")
- [Upload data](#lakehouse-getting-started-upload-data "#lakehouse-getting-started-upload-data")
- [Query data](#lakehouse-get-started-query "#lakehouse-get-started-query")
- [Adding data sources in lakehouse architecture](lakehouse-add-data.md "lakehouse-add-data.md")
- [Publishing data in lakehouse architecture](lakehouse-publish.md "lakehouse-publish.md")

## Prerequisites

- Your administrator must grant you access to the [lakehouse architecture](../../../sagemaker-unified-studio/latest/userguide/getting-started-access-the-portal.md "../../../sagemaker-unified-studio/latest/userguide/getting-started-access-the-portal.md").

If you don't have access to it, contact your administrator. For more information, see
[https://docs.aws.amazon.com/sagemaker-unified-studio/latest/userguide/getting-started-access-the-portal.html](../../../sagemaker-unified-studio/latest/userguide/getting-started-access-the-portal.md "../../../sagemaker-unified-studio/latest/userguide/getting-started-access-the-portal.md").

- You must have a Amazon SageMaker Unified Studio project and with the proper project membership role.

If you don't have proper access to a project, contact your administrator. To view your
project membership role, choose **Actions** on the top right corner of
the project overview page, then choose **Manage members**. You will see
your membership role in the **Role** column.

## Create a project

You can create a project from a project profile, which defines a template for projects in
your domain. To use lakehouse architecture, your project must be created using either [Data analytics and AI-ML model development](../../../sagemaker-unified-studio/latest/adminguide/data-analytics-ai-model-development.md "../../../sagemaker-unified-studio/latest/adminguide/data-analytics-ai-model-development.md") or [SQL
analytics](../../../sagemaker-unified-studio/latest/adminguide/project-profiles.md "../../../sagemaker-unified-studio/latest/adminguide/project-profiles.md") project profile. For more information about creating a project, see [Create
a project](../../../sagemaker-unified-studio/latest/userguide/getting-started-create-a-project.md "../../../sagemaker-unified-studio/latest/userguide/getting-started-create-a-project.md") from lakehouse architecture User Guide.

When using lakehouse architecture, you can create the following resources in the lakehouse:

1. **Databases in AWS Glue Data Catalog**

lakehouse architecture is implemented on AWS Glue and AWS Lake Formation in your AWS account. 2. **A catalog to store data in Redshift Managed Storage (RMS)
format**

You will create a catalog in RMS format. To view the catalog, navigate to the AWS Lake Formation
console at [https://console.aws.amazon.com/lakeformation/](https://console.aws.amazon.com/lakeformation/ "https://console.aws.amazon.com/lakeformation/"), you should be able to see the
catalog from the **Catalogs** list. 3. **Provisioning permissions**

You will create an IAM role when you create a project. Each project has a dedicated
IAM role. This IAM role has permission to the resources that are created from this
project. The Amazon Resource Name (ARN) of this IAM role is visible from
**Project details** section of the **Project
overview** page.

## Browse data

You can browse data in lakehouse architecture by completing the following steps.

###### To browse data

1. Choose a project to view the data.
2. On project page, from the left navigation, choose **Data**. This
   opens the **Data** explorer in the middle of the page.

The **Data** explorer includes: **Lakehouse**,
**Redshift**, and **S3**. 3. Expand **Lakehouse** to view catalogs, databases, tables.

## Upload data

You can upload data in CSV or JSON format to a catalog. To upload data, follow the
instructions in [Uploading data](lakehouse-upload-data.md "lakehouse-upload-data.md").

After uploading data is complete, you will see the table listed within the database under
**AwsDataCatalog**.

## Query data

You can query data using supported query editor.

###### To query data

1. On **Lakehouse**, choose **AwsDataCatalog** on top.
   Expand the catalog to view the list of databases. Choose a database.
2. From a selected database, choose a table. Then choose the three dot menu to the right
   of the table to view supported tools for data query.
3. Choose **Query with Athena**. This opens the **Data
   explorer** page where you can run SQL queries. You might find information in
   [SQL reference
   for Athena](../../../athena/latest/ug/ddl-sql-reference.md "../../../athena/latest/ug/ddl-sql-reference.md") helpful.
4. Choose **Query with Amazon Redshift**. This opens the **Data
   explorer** page where you can run SQL queries. You might find information in
   [Querying a
   database using the query editor v2](../../../redshift/latest/mgmt/query-editor-v2.md "../../../redshift/latest/mgmt/query-editor-v2.md") helpful.

To subscribe an asset, see [Request subscription to assets in Amazon SageMaker Unified Studio](../../../sagemaker-unified-studio/latest/userguide/subscribe-to-data-assets-managed.md "../../../sagemaker-unified-studio/latest/userguide/subscribe-to-data-assets-managed.md").

To publish data to the catalog from the lakehouse inventory, see [Publishing data in lakehouse architecture](lakehouse-publish.md "lakehouse-publish.md").
