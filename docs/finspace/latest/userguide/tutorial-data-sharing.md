After careful consideration, we decided to end support for Amazon FinSpace, effective October 7, 2026. Amazon FinSpace will no longer accept new customers beginning October 7, 2025. As an existing customer with an Amazon FinSpace environment created before October 7, 2025, you can continue to use the service as normal. After October 7, 2026, you will no longer be able to use Amazon FinSpace. For more information, see
[Amazon FinSpace end of support](amazon-finspace-end-of-support.md "amazon-finspace-end-of-support.md").

# Tutorial: Sharing data views using AWS Lake Formation

###### Important

Amazon FinSpace Dataset Browser will be discontinued on `March 26,
 2025`. Starting `November 29, 2023`, FinSpace will no longer accept the creation of new Dataset Browser
environments. Customers using [Amazon FinSpace with Managed Kdb Insights](https://aws.amazon.com/finspace/features/managed-kdb-insights/ "https://aws.amazon.com/finspace/features/managed-kdb-insights/") will not be affected. For more information, review the [FAQ](https://aws.amazon.com/finspace/faqs/ "https://aws.amazon.com/finspace/faqs/") or contact [AWS Support](https://aws.amazon.com/contact-us/ "https://aws.amazon.com/contact-us/") to assist with your
transition.

This tutorial guides you through steps to enable access to data views and query the
ingested data by using the integrated services. The topics in this tutorial explain how
to create a resource link and use it to anable access to the data views in the
infrastructure account.

## Prerequisites and considerations

Before you start this tutorial, complete the following prerequisites:

- Make sure that your Amazon FinSpace environment is enabled to share data views. You
  can request that your environment is enabled by creating a technical support
  case at [AWS Support](https://console.aws.amazon.com/support "https://console.aws.amazon.com/support"). For this, choose
  the service as **Amazon FinSpace**.

In the support case, specify that you want to enable data view sharing for
your FinSpace environment. Make sure that you include the environment ID and the
Region when you create the support case. For more information, see [Creating support cases](../../../awssupport/latest/user/case-management.md#creating-a-support-case "../../../awssupport/latest/user/case-management.md#creating-a-support-case") in the
_AWS Support User Guide_.

After data sharing is enabled in your FinSpace environment, all the data views
of the internal datasets in FinSpace are instantly available in the target Lake Formation
catalog as a Lake Formation table.

###### Note

    + If you have want to share data views from multiple environments, you need
     to create a separate support case for each environment.
    + If you want to disable data view sharing for your FinSpace environment, you need to create a new technical support case.

- Make sure that users or roles in the customer account have access to
  use Lake Formation and other required analytics engines such as Amazon Redshift, Athena, Quick Suite, Amazon EMR,
  and SageMaker AI.
- If you want to request data from an integrated service like Amazon Athena,
  ensure that an Amazon S3 location is configured.
- At least one user must be a Lake Formation data lake administrator to view shared
  resources.

## Step 1: Enable the link to the shared

database

To enable access to the shared data view, first you need to create a resource
link. A resource link is a Data Catalog object that is a link to a shared database or
table.

After you create a resource link and grant data permissions, you can use
integrated services to run queries on the shared databases or tables. For more
information on resource links, see the [AWS Lake Formation Developer Guide](../../../lake-formation/latest/dg/resource-links-about.md "../../../lake-formation/latest/dg/resource-links-about.md").

###### To create a resource link to a shared database

1. Open the AWS Lake Formation console at [https://console.aws.amazon.com/lakeformation/](https://console.aws.amazon.com/lakeformation/ "https://console.aws.amazon.com/lakeformation/").
2. In the navigation pane, choose **Databases**, and then
   choose the required shared database from the list. The shared database name
   starts with _finspace\__, followed by the
   Environment ID that you provided in the technical support case.

###### Note

The shared database is not available in the list on this page unless you
request access to it by creating a support case. 3. Choose **Actions** and then choose **Create
resource link**. 4. On the **Create resource link** page, enter the resource
link name. For the subsequent query, it's helpful if the resource link name is
the same as the database name. 5. Choose **Create**. The resource link is created, and you
can view the resource link name in italics under the **Name**
column on the **Databases** page.

After you create a resource link, only you can view and access it. To allow other
principals in your account to access the resource link, grant permissions on the
resource link.

###### To grant data permissions on the resource link

1. On the **Databases** page, under the
   **Name** column, choose the resource link name in
   italics.
2. Choose **Actions** and then choose
   **Grant**.
3. On the **Grant data permissions** page, under
   **Principals**, choose **IAM users and
   roles**.
4. Choose one or more users or roles from the **IAM users and
   roles** list.
5. In the **LF-Tags or catalog resources** section, choose
   **Named data catalog resources**, and then choose one or
   more databases to grant permissions to.
6. For the **Resource link permissions** section, choose
   _Describe_.
7. Choose **Grant**. You can now use the resource link to
   access the shared database.

###### Note

Granting permissions on a resource link doesn't grant permissions on the target
(shared) database or table. You must grant permissions on the target database
separately.

## Step 2: Enable access to the target

database and tables

After creating the resource link with permissions, you can use it to grant access
to the shared database and tables.

###### To grant access to the shared database

1. Open the AWS Lake Formation console at [https://console.aws.amazon.com/lakeformation/](https://console.aws.amazon.com/lakeformation/ "https://console.aws.amazon.com/lakeformation/").
2. In the navigation pane, choose **Databases**. Then, from
   the list, choose the resource link that you created in the previous
   step.
3. Choose **Actions** and then choose **Grant on
   target**.
4. On the **Grant data permissions** page, under
   **Principals**, choose **IAM users and
   roles**.
5. Choose one or more users or roles from the **IAM users and
   roles** list.
6. In the **LF-Tags or catalog resources** section, choose
   **Named data catalog resources**. Then, from the list, add
   the database that you selected while granting access to the resource
   link.
7. For the database permissions , select _Describe_.
8. Choose **Grant**.

###### To grant access to the tables

1. Open the AWS Lake Formation console at [https://console.aws.amazon.com/lakeformation/](https://console.aws.amazon.com/lakeformation/ "https://console.aws.amazon.com/lakeformation/").
2. In the navigation pane, choose **Tables**, and then choose
   the required table from the list.
3. Choose **Actions** and then choose
   **Grant**.
4. On the **Grant data permissions** page, under
   **Principals**, choose **IAM users and
   roles**.
5. Choose one or more users or roles from the **IAM users and
   roles** list.
6. In the **LF-Tags or catalog resources** section, choose
   **Named data catalog resources**. Then, from the list,
   choose the table that you want to grant permissions to.
7. For the table permissions, select _Describe_ and _Select_.
8. Choose **Grant**.

## Step 3: Query data by using integrated services

After you have access to the database and tables, you can use the integrated
services to query data in the tables.

The following procedure shows how to query data using Amazon Athena.

###### Note

Before you can run a query using Athena, you must specify a query result bucket
in Amazon S3. To set up an Amazon S3 query result location, see [Specifying
a query result location](../../../athena/latest/ug/querying.md#query-results-specify-location "../../../athena/latest/ug/querying.md#query-results-specify-location") in the _Amazon Athena User Guide_.

###### To query data using Amazon Athena

1. Open the AWS Lake Formation console at [https://console.aws.amazon.com/lakeformation/](https://console.aws.amazon.com/lakeformation/ "https://console.aws.amazon.com/lakeformation/").
2. In the navigation pane, choose **Tables**, and then choose
   the required table name from the list.
3. On the **Table details** page, choose
   **Actions** and then choose **View data**.
   You are taken to Athena to preview data.
4. Choose **Ok** in the dialog box to confirm navigating to
   Amazon Athena. The Athena query editor opens in a new browser tab.

###### Note

You will be charged separately for Athena queries. 5. In the Athena query editor, enter the SQL query and choose
**Run**.

You can view the query results at the bottom of the page.

###### Note

You must specify the resource link to include shared resources in the
query.

You can also use Amazon Redshift to query data in the data lake. For more information, see
the [AWS Lake Formation Developer Guide](../../../lake-formation/latest/dg/tut-query-redshift.md "../../../lake-formation/latest/dg/tut-query-redshift.md").
