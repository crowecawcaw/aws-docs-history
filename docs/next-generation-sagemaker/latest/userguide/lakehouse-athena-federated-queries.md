# Get started with SageMaker Lakehouse

integrated access controls for Athena federated queries in Amazon SageMaker Unified Studio

Scaling data infrastructure creates challenges with data silos, fragmented access controls,
and complex connectivity requirements. Data analysts need to access information across multiple
storage systems but are frequently hindered by:

- **Complex connectivity setup** - Configuring connections to
  various data sources requires technical expertise and access to configuration details that
  analysts may not have.
- **Fragmented governance** - Different data sources have
  their own access control mechanisms, making consistent security policies difficult to
  implement.
- **Data duplication** - Copying data between systems for
  analysis increases costs and creates data consistency risks.
  To address the challenges of data silos and fragmented access, [SageMaker Lakehouse](../../../sagemaker-unified-studio/latest/userguide/lakehouse.md "../../../sagemaker-unified-studio/latest/userguide/lakehouse.md") with integrated access controls for
  [Amazon Athena](../../../athena/latest/ug/what-is.md "../../../athena/latest/ug/what-is.md")
  (Athena) federated queries offers:

- Streamlining the creation of connections to diverse data sources through a unified
  interface
- Centralizing access control management through [AWS Lake Formation](https://aws.amazon.com/lake-formation/ "https://aws.amazon.com/lake-formation/")
- Enabling in-place querying through federated catalogs without data movement
- Providing fine-grained permissions at the catalog, database, table, and column
  levels
- Exploring data for ad hoc reporting and proof of concept before setting up new zero-ETL pipelines
  SageMaker Lakehouse provides a unified environment for accessing, discovering, preparing,
  and analyzing data from various sources for machine learning (ML) and analytics workloads.
  Athena complements this as a serverless query service that analyzes data lake and federated data
  sources such as [Amazon DynamoDB](https://aws.amazon.com/dynamodb/ "https://aws.amazon.com/dynamodb/") and
  PostgreSQL, through using SQL without extract, transform, and load (ETL) scripts. Federated
  connections in SageMaker Lakehouse establish secure links to external data sources, enabling
  access without data movement. [Federated catalogs](../../../lake-formation/latest/dg/federated-catalog-data-connection.md "../../../lake-formation/latest/dg/federated-catalog-data-connection.md") organize metadata about these connected data sources, making them
  discoverable and queryable through the SageMaker Lakehouse interface. Federated queries use
  these connections to run SQL statements across multiple data sources simultaneously, breaking
  down data silos for comprehensive analysis.

## What you'll learn

This guide shows you how to use SageMaker Lakehouse with integrated access controls for
Athena federated queries. In this guide, you create an environment where data analysts can discover and
query data across sources while administrators maintain consistent governance and appropriate
security controls. This guide includes the following steps:

1. Set up federated connections between SageMaker Lakehouse and DynamoDB.
   - Create connections that serve as bridges between your SageMaker Lakehouse and
     external data sources.
   - Enable seamless data access while maintaining security boundaries.
   - Learn how connections eliminate the need for data movement or duplication.

2. Create federated catalogs for data discovery.
   - Establish catalogs that contains metadata and views about tables from your
     connected data sources.
   - Access data from the connected data source within your SageMaker Lakehouse
     environment.
   - Make external tables queryable through the Lakehouse interface.
   - Use catalogs as directories of available data assets to simplify discovery and
     access.

3. Implement column-level security using AWS Lake Formation
   - Configure fine-grained permissions for sensitive data.
   - Apply data access controls based on user roles and responsibilities.
   - Ensure consistent security policies across all data sources.

4. Validate security controls through Athena queries
   - Test access permissions with different user personas.
   - Verify that you properly protect sensitive data.
   - Confirm that authorized users can access appropriate data.

## Prerequisites

Before you begin, make sure you have the following:

- An AWS account with permission to create IAM roles and IAM policies.
- An [AWS Identity and Access Management](https://aws.amazon.com/iam/ "https://aws.amazon.com/iam/") (IAM) user with an access key and secret key to configure the [AWS Command Line Interface](https://aws.amazon.com/cli/ "https://aws.amazon.com/cli/") (AWS CLI).
- Your administrator role added as a data lake administrator in AWS Lake Formation.
  For more information about how to create and add a data lake administrator, see [Create a data lake administrator](../../../lake-formation/latest/dg/initial-lf-config.md#create-data-lake-admin "../../../lake-formation/latest/dg/initial-lf-config.md#create-data-lake-admin") in _AWS Lake Formation Developer
  Guide_.
- Administrator access to Amazon SageMaker Unified Studio. For more information about
  permissions of the administrator role, see [Lake Formation personas and IAM permissions reference](../../../lake-formation/latest/dg/permissions-reference.md#persona-user "../../../lake-formation/latest/dg/permissions-reference.md#persona-user") in the _AWS Lake Formation Developer Guide_. For more information about using the IAM
  Identity Center directory as your identity source, see [Configure user access with the default IAM Identity Center directory](../../../singlesignon/latest/userguide/quick-start-default-idc.md "../../../singlesignon/latest/userguide/quick-start-default-idc.md") in the
  _AWS IAM Identity Center User Guide_. For more information about
  how to access SageMaker, see [Accessing Amazon SageMaker Unified Studio](../../../sagemaker-unified-studio/latest/adminguide/what-is-sagemaker-unified-studio.md#acessing-sagemaker-unified-studio "../../../sagemaker-unified-studio/latest/adminguide/what-is-sagemaker-unified-studio.md#acessing-sagemaker-unified-studio") in the _Amazon SageMaker
  Unified Studio Administrator Guide_.
- A SageMaker Unified Studio domain with the SQL Analytics profile enabled. For more
  information about creating an Amazon SageMaker Unified Studio domain and a project, see [Setting up Amazon SageMaker](setting-up.md "setting-up.md") in the
  _Amazon SageMaker User Guide_. For more information about SQL analytics project profile, see
  [SAQL analytics project profile](../../../sagemaker-unified-studio/latest/adminguide/sql-analytics.md "../../../sagemaker-unified-studio/latest/adminguide/sql-analytics.md") in the
  _Amazon SageMaker Unified Studio Administrator Guide_.

###### Note

Add your administrator as an SSO user to your domain. For more information about how to
add an SSO user as a root domain owner, see [Step 1 - Create an Amazon SageMaker unified domain](setting-up.md#create-domain "setting-up.md#create-domain") in the _Amazon SageMaker User Guide_ and [Managing users in Amazon SageMaker Unified Studio](../../../sagemaker-unified-studio/latest/adminguide/user-management.md "../../../sagemaker-unified-studio/latest/adminguide/user-management.md") in the _Amazon SageMaker Unified
Studio Administrator Guide_.

- Two SageMaker Unified Studio projects set up for this guide:

      + An Admin project for creating connections. This project has a SQL analytics project profile.
      + A Data Analyst project for analyzing data, which includes both administrator and
       analysts as members. This project has a SQL analytics project profile.

  For more information about how to create a project in SageMaker Unified Studio, see [Setting up Amazon SageMaker](setting-up.md "setting-up.md") in the
  _Amazon SageMaker User Guide_.

###### Note

- To find the project role ARN for each project, in the SageMaker Unified Studio,
  choose the name of the project, choose **Project
  overview**, and find **Project role ARN** under
  **Project details**. For more information, see [Get project details](../../../sagemaker-unified-studio/latest/userguide/view-project-details.md "../../../sagemaker-unified-studio/latest/userguide/view-project-details.md") in the _Amazon SageMaker Unified Studio User
  Guide_.
- For more information about how to add members to your projects, see [Add project members](../../../sagemaker-unified-studio/latest/userguide/add-project-members.md "../../../sagemaker-unified-studio/latest/userguide/add-project-members.md") in the _Amazon SageMaker Unified Studio User
  Guide_.

- Administrator access to a data source. SageMaker Lakehouse connections support
  [several popular data sources](../../../sagemaker-unified-studio/latest/userguide/lakehouse-data-connection.md#lakehouse-data-connection-supported "../../../sagemaker-unified-studio/latest/userguide/lakehouse-data-connection.md#lakehouse-data-connection-supported"), such as Amazon DynamoDB, PostgreSQL, and [Amazon DocumentDB](https://aws.amazon.com/documentdb/ "https://aws.amazon.com/documentdb/"). In this guide, we
  use DynamoDB as the data source.
  - To set up data sources in DynamoDB:
    - You can create a new table in DynamoDB with the partition key
      `cust_id` and the sort key `zipcode` and another column
      `mobile` through [AWS CloudShell](https://aws.amazon.com/cloudshell/ "https://aws.amazon.com/cloudshell/") by using the following command:

    ```

    aws dynamodb create-table \
      --table-name customer_ddb \
      --attribute-definitions \
    AttributeName=cust_id,AttributeType=N \
    AttributeName=zipcode,AttributeType=N \
      --key-schema \
    AttributeName=cust_id,KeyType=HASH \
    AttributeName=zipcode,KeyType=RANGE \
      --provisioned-throughput \
    ReadCapacityUnits=5,WriteCapacityUnits=5 \
      --table-class STANDARD

    ```

    - You can populate the DynamoDB table with sample data by using the following
      commands:

    ```

    # First item
    aws dynamodb put-item \
      --table-name customer_ddb \
      --item '{"cust_id": {"N": "11"}, "zipcode": {"N": "2000"}, "mobile": {"N": "11113333"}}'

    # Second item
    aws dynamodb put-item \
      --table-name customer_ddb \
      --item '{"cust_id": {"N": "12"}, "zipcode": {"N": "2000"}, "mobile": {"N": "22224444"}}'

    # Third item
    aws dynamodb put-item \
      --table-name customer_ddb \
      --item '{"cust_id": {"N": "13"}, "zipcode": {"N": "3000"}, "mobile": {"N": "33335555"}}'

    # Fourth item
    aws dynamodb put-item \
      --table-name customer_ddb \
      --item '{"cust_id": {"N": "14"}, "zipcode": {"N": "4000"}, "mobile": {"N": "55556666"}}'

    ```

    For more information about setting up a DynamoDB data source by using AWS
    CloudShell, see [Amazon DynamoDB tutorial for AWS Cloud9](../../../cloud9/latest/user-guide/sample-dynamodb.md#sample-dynamodb-create-table "../../../cloud9/latest/user-guide/sample-dynamodb.md#sample-dynamodb-create-table") in the _AWS Cloud9
    User Guide_.
    - To allow the appropriate actions for the SageMaker Unified Studio projects to
      take on your DynamoDB data source, add a resource-based policy to your DynamoDB
      data source. Attach the following policy for the table
      `customer_ddb`.

    JSON

    ```
    `{
     "Version":"2012-10-17",
     "Statement": [
     {
     "Effect": "Allow",
     "Principal": {
     "AWS": [
     "arn:aws:iam::`111122223333`:role/`datazone_usr_role_xxxxxxxxxxxxxx_yyyyyyyyyyyyyy`",
     "arn:aws:iam::`111122223333`:role/`datazone_usr_role_zzzzzzzzzzzzzz_aaaaaaaaaaaaaa`"
     ]
     },
     "Action": [
     "dynamodb:Query",
     "dynamodb:Scan",
     "dynamodb:DescribeTable",
     "dynamodb:PartiQLSelect",
     "dynamodb:BatchWriteItem"
     ],
     "Resource": "arn:aws:dynamodb:`us-west-2`:`111122223333`:table/`customer_ddb`"
     }
     ]
    }`

    ```

    This example policy allows connecting to DynamoDB tables as a federated
    source. Replace `us-west-2` with your AWS Region,
    `111122223333` with the AWS account ID where
    DynamoDB is deployed, `customer_ddb` with the DynamoDB
    table that you intend to query from SageMaker Unified Studio,
    `datazone_usr_role_xxxxxxxxxxxxxx_yyyyyyyyyyyyyy` with
    the admin project role, and
    `datazone_usr_role_zzzzzzzzzzzzzz_aaaaaaaaaaaaaa` with
    the data analyst project role in SageMaker Unified Studio. For more information
    about how to attach a policy to a DynamoDB data source, see [Attach a policy to a DynamoDB existing table](../../../amazondynamodb/latest/developerguide/rbac-attach-resource-based-policy.md "../../../amazondynamodb/latest/developerguide/rbac-attach-resource-based-policy.md") in the _Amazon
    DynamoDB Developer Guide_.

## Step 1: Set up federated catalogs

The first step is to set up federated catalogs for our data sources using an administrator
account.

###### To set up federated catalogs

1. On the SageMaker Unified Studio console, for the domain you created in the
   prerequisite, choose **Open unified studio**.
2. Choose your admin project name under **Your
   projects**.
3. Choose **Data** in the navigation pane.
4. In the **Data explorer**, choose the plus icon to add a
   data source.
5. Under **Add data**, choose **Add
   connection**, choose **Next**.
6. Choose **Amazon DynamoDB**, and choose **Next**.
7. For **Name**, enter the name for your data source of
   DynamoDB.
8. Choose **Add data**.

SageMaker Unified Studio connects to the DynamoDB data source that you created in the
prerequisites, registers the data source as a federated catalog with SageMaker Lakehouse, and
displays it in your data explorer. The catalog references your DynamoDB data source.

###### To explore and query your data

1. Choose your admin project from SageMaker Unified Studio.
2. Choose **Data** in the navigation pane.
3. Choose the SageMaker Lakehouse catalog that you just created to view its contents. Use
   the data explorer to drill down to a table and choose **Query with
   Athena**.
4. In the query editor, run a sample SQL query to understand your data.

For example, run the following query. Replace
`your_federated_catalog_name` with the name of the federated catalog that you just created,
`default` with the name of
your database, and `your_table_name` with the name of your DynamoDB table.

To learn more, see [SQL analytics](../../../sagemaker-unified-studio/latest/userguide/sql-query.md "../../../sagemaker-unified-studio/latest/userguide/sql-query.md") in the _Amazon SageMaker Unified Studio User
Guide_.

```

select * from `your_federated_catalog_name`.`default`.`your_table_name` limit 10;

```

###### Note

Access to the data source in the SageMaker Unified Studio project is governed by the policies for the project role. Users whoever become the member of this admin project
use the same project role ARN and have the same full access level permissions to the
data source. For more information about how to add members to your projects, see [Add project members](../../../sagemaker-unified-studio/latest/userguide/add-project-members.md "../../../sagemaker-unified-studio/latest/userguide/add-project-members.md") in the _Amazon SageMaker Unified Studio User
Guide_. To grant fine-grained access permissions to [different user personas](../../../lake-formation/latest/dg/permissions-reference.md#lf-personas "../../../lake-formation/latest/dg/permissions-reference.md#lf-personas"), such as data analysts, create a separate data analyst
project and add the data analyst users as project members of the data analyst project. Step
2 shows how to set up the fine-grained permissions.

For more information about creating connections in SageMaker Lakehouse, see [Creating a connection in SageMaker Lakehouse](../../../sagemaker-unified-studio/latest/userguide/lakehouse-create-connection.md "../../../sagemaker-unified-studio/latest/userguide/lakehouse-create-connection.md") in the _Amazon
SageMaker Unified Studio User Guide_. For more information about creating
catalogs, see [Creating a catalog](../../../sagemaker-unified-studio/latest/userguide/lakehouse-create-catalog.md "../../../sagemaker-unified-studio/latest/userguide/lakehouse-create-catalog.md") in the _Amazon SageMaker Unified Studio User
Guide_.

## Step 2: Set up fine-grained

access permissions on federated catalogs

Security is a critical aspect of data access. SageMaker Lakehouse provides integrated
access controls that work with federated queries in Athena to ensure proper governance. You
can manage permissions at the catalog, database, and table levels. Administrators can apply
access controls at different levels of granularity to ensure sensitive data remains protected
while expanding data access.

This step is to delegate access permissions on your DynamoDB federated catalogs to other
users. You grant permissions to the data analyst persona. To set up the fine-grained access
permissions to the data analyst persona, you need to add permissions on your DynamoDB
federated catalogs to the SageMaker Unified Studio data analyst project role that you created
in the prerequisites section. This will ensure that access controls that you specify are enforced when
the data is queried. For more information about the Lake Formation personas and IAM
permissions, see [Lake
Formation personas and IAM permissions reference](../../../lake-formation/latest/dg/permissions-reference.md "../../../lake-formation/latest/dg/permissions-reference.md") in the _AWS Lake
Formation Developer Guide_.

###### To set up fine-grained access permissions on federated catalog and database

1. Navigate to Lake Formation in the [AWS Management Console](https://console.aws.amazon.com/ "https://console.aws.amazon.com/") as an administrator.
2. In the Lake Formation console, under **Data Catalog** in
   the navigation pane, choose **Catalogs**.
3. Choose the federated catalog name that you set up in [Step 1: Set up federated catalogs](#step-1-set-up-federated-catalogs "#step-1-set-up-federated-catalogs"). You'll see the
   databases.
4. Choose the database name in the catalog. You can see details for the database and
   manage permissions.
5. To set up permissions for the federated catalog and database to your SageMaker Unified
   Studio data analyst project (the data analyst project that you set up in prerequisites),
   from the **Actions** menu, choose **Grant**.
6. For **Principal type**, choose **Principals**.
7. For **Principals**, choose **IAM
   users and roles**.
8. For **IAM users and roles**, choose the project role ARN
   that you got from your data analyst project in the prerequisites section.
9. For **LF-Tags or catalog resources**, choose **Named Data Catalog resources**.
10. For **Catalogs**, choose the federated catalog name for
    the source (the federated catalog that you set up in Step 1) to grant permissions
    on.
11. For **Databases**, the console populates the databases for your
    DynamoDB data source.
12. For **Database permissions - Database permissions**,
    select **Describe**.
13. Choose **Grant**.

###### To set up fine-grained access permissions on the tables

For example, if you wish to restrict access to a sensitive column containing the mobile
phone number for each customer, the steps are as follows.

1. Navigate to Lake Formation in the [AWS Management Console](https://console.aws.amazon.com/ "https://console.aws.amazon.com/") as an administrator.
2. In the Lake Formation console, under **Data Catalog** in
   the navigation pane, choose **Tables**.
3. Under **Choose catalog**, choose the federated catalog
   name that you set up in Step 1.
4. Choose the table name in the catalog. You can see details for the table and manage
   permissions.
5. From the **Actions** menu, choose **Grant**.
6. For **Principal type**, choose **Principals**.
7. For **Principals**, choose **IAM
   users and roles**.
8. For **IAM users and roles**, choose the project role ARN
   that you got from your data analyst project in the prerequisites section.
9. For **LF-Tags or catalog resources**, choose **Named Data Catalog resources**.
10. For **Catalogs**, choose the federated catalog name for
    the source (the federated catalog that you set up in Step 1) to grant permissions
    on.
11. For **Databases**, the console populates the databases for our
    DynamoDB data source.
12. For **Tables**, the console populates the tables for your DynamoDB
    data source.
13. For **Table permissions - Table permissions**, select
    **Select**.
14. For **Data permissions**, choose **Column-based access**.
15. For **Choose permission filter**, choose **Include columns**.
16. For **Select columns**, choose columns
    `zipcode` and `cust_id`.
17. Choose **Grant**.

In this example, we demonstrate how to set up a basic column-level filter to restrict
access to sensitive data. However, SageMaker Lakehouse supports a broad range of fine-grained
access control scenarios beyond column filters that allow you to meet complex security and
compliance requirements across diverse data sources. For more information about managing
permissions on catalogs, see [Adding existing databases and catalogs using AWS Lake Formation permissions](../../../sagemaker-unified-studio/latest/userguide/lakehouse-add-catalog.md "../../../sagemaker-unified-studio/latest/userguide/lakehouse-add-catalog.md") in
the _Amazon SageMaker Unified Studio User Guide_ and [Managing Lake Formation Permissions](../../../lake-formation/latest/dg/managing-permissions.md "../../../lake-formation/latest/dg/managing-permissions.md") in the _AWS Lake Formation Developer
Guide_.

By implementing these fine-grained access controls, you can ensure that users only access
data they're authorized to see, maintaining compliance with your organization's security
policies. This creates a consistent security model across your data sources. Now, you have
successfully set up fine-grained access permissions on your DynamoDB federated catalog.

## Step 3: Validate

fine-grained access permissions on federated catalogs

After you set up federated catalogs with fine-grained access permissions in Step 2, run
queries to confirm access permissions are working as expected.

###### To validate fine-grained access permissions on federated catalogs

1. On the SageMaker Unified Studio console, for the domain you created in the
   prerequisite, choose **Open unified studio**.
2. Choose your data analyst project name under **Your
   projects**.
3. From the **Build** menu, choose **Query Editor**.
4. In the **Data explorer**, expand **Lakehouse**, choose the DynamoDB catalog that you created in Step 1.
5. Drill down to the table that you set up fine-grained access permissions in Step 2, and
   choose **Query with Athena** to run a sample query.

For example, run the following query. Replace
`your_federated_catalog_name` with the name of your catalog, `default` with the name of
your database, and `your_table_name` with the name of your DynamoDB table. To learn more,
see [SQL analytics](../../../sagemaker-unified-studio/latest/userguide/sql-query.md "../../../sagemaker-unified-studio/latest/userguide/sql-query.md") in the _Amazon SageMaker Unified Studio User
Guide_.

```

select * from `your_federated_catalog_name`.`default`.`your_table_name` limit 10;

```

Note how permissions are working as expected because the query result doesn't include
the mobile phone number column that was visible in the admin project view.

###### To have other users under the data analyst persona get the fine-grained access

permissions

1. Create data analyst SSO users or groups. For more information about how to
   add an SSO user to your domain, see [Managing users in Amazon SageMaker Unified Studio](../../../sagemaker-unified-studio/latest/adminguide/user-management.md "../../../sagemaker-unified-studio/latest/adminguide/user-management.md") in the _Amazon SageMaker Unified
   Studio Administrator Guide_.
2. Add these SSO users to your SageMaker Unified Studio domain. For more information about how to
   add an SSO user to your domain, see [Managing users in Amazon SageMaker Unified Studio](../../../sagemaker-unified-studio/latest/adminguide/user-management.md "../../../sagemaker-unified-studio/latest/adminguide/user-management.md") in the _Amazon SageMaker Unified
   Studio Administrator Guide_.
3. Add these users as members (**"Contributor"**) to your
   SageMaker Unified Studio data analyst project. The data analyst users can have access to
   this data analyst project and will only have access to a subset of data that's defined by
   the data lake administrator in Step 2. For more information about how to add members to
   your projects, see [Add project members](../../../sagemaker-unified-studio/latest/userguide/add-project-members.md "../../../sagemaker-unified-studio/latest/userguide/add-project-members.md") in the _Amazon SageMaker Unified Studio User
   Guide_.

## Step 4: Clean up

Make sure you remove the SageMaker Lakehouse resources to mitigate any unexpected costs.
Delete the following resources:

- The connections and catalogs that you created in Step 1.

Specifically, choose your project from SageMaker Unified Studio. Choose **Data** in the navigation pane. Choose the SageMaker Lakehouse
catalog that you created in Step 1. Choose the **Actions**
menu and choose **Remove**. Type "**Confirm**" and choose **Remove
connection**.

- The underlying DynamoDB data sources that you created in the prerequisites. For more
  information about deleting a DynamoDB table, see [Delete your DynamoDB table to clean up resources](../../../amazondynamodb/latest/developerguide/getting-started-step-6.md "../../../amazondynamodb/latest/developerguide/getting-started-step-6.md") in the _Amazon
  DynamoDB Developer Guide_.
- The SageMaker Unified Studio admin and data analyst projects that you created in the
  prerequisites. For more information about deleting projects, see [Delete a project](../../../sagemaker-unified-studio/latest/userguide/delete-project.md "../../../sagemaker-unified-studio/latest/userguide/delete-project.md") in the Amazon SageMaker Unified Studio User Guide.
- The SageMaker Unified Studio domain that you created in the prerequisites.

## Next steps

Now that you've successfully set up SageMaker Lakehouse integrated access controls for
Athena federated queries, consider these next steps to further enhance your data governance
and analytics capabilities:

- **Expand your data sources** - Connect [supported data sources](../../../sagemaker-unified-studio/latest/userguide/lakehouse-data-connection.md#lakehouse-data-connection-supported "../../../sagemaker-unified-studio/latest/userguide/lakehouse-data-connection.md#lakehouse-data-connection-supported") such as PostgreSQL, MySQL, or Amazon DocumentDB, to
  create a unified data ecosystem with consistent access controls.
- **Implement advanced security patterns** - Explore
  row-level security, cell-level filtering, and [attribute-based access control](https://aws.amazon.com/blogs/big-data/amazon-sagemaker-lakehouse-now-supports-attribute-based-access-control/ "https://aws.amazon.com/blogs/big-data/amazon-sagemaker-lakehouse-now-supports-attribute-based-access-control/") to meet complex compliance
  requirements across your organization. For more information, see [Managing Lake Formation Permissions](../../../lake-formation/latest/dg/managing-permissions.md "../../../lake-formation/latest/dg/managing-permissions.md") in the _AWS Lake Formation
  Developer Guide_.
- **Build analytics workflows** - Create end-to-end
  analytics pipelines that leverage federated queries for data preparation and ML model
  training.
- **Integrate with visualization tools** - Connect [Amazon QuickSight](https://aws.amazon.com/quicksight/ "https://aws.amazon.com/quicksight/") to your federated
  catalogs to create dashboards and visualizations with the same security controls.
- **Automate governance processes** - Use the Amazon Athena
  REST API ([CreateDataCatalog](../../../athena/latest/APIReference/API_CreateDataCatalog.md "../../../athena/latest/APIReference/API_CreateDataCatalog.md")), AWS CloudFormation ([`AWS::Athena::DataCatalog`](../../../AWSCloudFormation/latest/TemplateReference/aws-resource-athena-datacatalog.md "../../../AWSCloudFormation/latest/TemplateReference/aws-resource-athena-datacatalog.md")) or the AWS CDK ([CfnDataCatalog](../../../cdk/api/v2/docs/aws-cdk-lib.aws_athena.md "../../../cdk/api/v2/docs/aws-cdk-lib.aws_athena.md")) to automate the creation and management of federated
  connections and access controls. After creating a data catalog, you need to [create
  a data source connection](../../../athena/latest/ug/connect-to-a-data-source.md "../../../athena/latest/ug/connect-to-a-data-source.md") and [register your connection as a Glue Data Catalog](../../../athena/latest/ug/register-connection-as-gdc.md "../../../athena/latest/ug/register-connection-as-gdc.md").

This integration between SageMaker Lakehouse and Athena federated queries provides
significant benefits for organizations with diverse data ecosystems. Data scientists can now
analyze customer behavior by combining transaction data from PostgreSQL with clickstream data
in [Amazon S3](https://aws.amazon.com/s3/ "https://aws.amazon.com/s3/"). Financial analysts can query
historical market data alongside real-time trading information without complex ETL processes.
Healthcare researchers can analyze patient records stored in different systems while
maintaining compliance with privacy regulations.

For more information about federated queries in Athena and the data sources that support
fine-grained access controls, see [Register
your connection as a Glue Data Catalog](../../../athena/latest/ug/register-connection-as-gdc.md "../../../athena/latest/ug/register-connection-as-gdc.md") in the _Athena User
Guide_. For more information about extending your SageMaker Lakehouse environment,
see [Add Data to SageMaker Lakehouse](../../../sagemaker-unified-studio/latest/userguide/lakehouse-add-data.md "../../../sagemaker-unified-studio/latest/userguide/lakehouse-add-data.md") and [Publishing Data](../../../sagemaker-unified-studio/latest/userguide/lakehouse-publish.md "../../../sagemaker-unified-studio/latest/userguide/lakehouse-publish.md") in the _Amazon SageMaker Unified Studio User
Guide_. For more information about specific use cases and implementation examples,
see [Simplify data access for your enterprise using SageMaker Lakehouse](https://aws.amazon.com/blogs/big-data/simplify-data-access-for-your-enterprise-using-amazon-sagemaker-lakehouse/ "https://aws.amazon.com/blogs/big-data/simplify-data-access-for-your-enterprise-using-amazon-sagemaker-lakehouse/"), [Simplify analytics and AI/ML with new SageMaker Lakehouse](https://aws.amazon.com/blogs/aws/simplify-analytics-and-aiml-with-new-amazon-sagemaker-lakehouse/ "https://aws.amazon.com/blogs/aws/simplify-analytics-and-aiml-with-new-amazon-sagemaker-lakehouse/"), and [Catalog and govern Amazon Athena federated queries with SageMaker Lakehouse](https://aws.amazon.com/blogs/big-data/catalog-and-govern-amazon-athena-federated-queries-with-amazon-sagemaker-lakehouse/ "https://aws.amazon.com/blogs/big-data/catalog-and-govern-amazon-athena-federated-queries-with-amazon-sagemaker-lakehouse/")
in the _AWS Blog posts_.
