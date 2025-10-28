# Connecting the Data Catalog to an external Hive metastore

To connect the AWS Glue Data Catalog to a Hive metastore, you need to deploy an AWS SAM application called [GlueDataCatalogFederation-HiveMetastore](https://console.aws.amazon.com/lambda/home#/create/app?applicationId=arn:aws:serverlessrepo:us-east-1:766175011753:applications/GlueDataCatalogFederation-HiveMetastore "https://console.aws.amazon.com/lambda/home#/create/app?applicationId=arn:aws:serverlessrepo:us-east-1:766175011753:applications/GlueDataCatalogFederation-HiveMetastore"). It creates the resources required to connect the external Hive metastore with the
Data Catalog. You can access the AWS SAM application in the AWS Serverless Application Repository.

The AWS SAM application creates the connection for the Hive metastore behind
Amazon API Gateway using a Lambda function. The AWS SAM application uses a uniform resource identifier
(URI) as an input from the user and connects the external Hive metastore to the Data Catalog. When
a user runs a query on Hive tables, the Data Catalog calls the API Gateway endpoint. The endpoint invokes
the Lambda function to retrieve the metadata of the Hive tables.

###### To connect the Data Catalog to the Hive metastore and set up permissions

1. ###### Deploy the AWS SAM application.
   1. Sign in to the AWS Management Console and open the AWS Serverless Application Repository.
   2. In the navigation pane, choose **Available
      applications**.
   3. Choose **Public applications**.
   4. Select the option **Show apps that create custom IAM roles or resource
      policies**.
   5. In the search box, enter the name **GlueDataCatalogFederation-HiveMetastore**.
   6. Choose the **GlueDataCatalogFederation-HiveMetastore** application.
   7. Under **Application Settings**, enter the following
      minimum required settings for your Lambda function:
      - **Application name** - A name for your AWS SAM application.
      - **GlueConnectionName** - A name for the connection.
      - **HiveMetastoreURIs** - The URI of your Hive metastore host.
      - **LambdaMemory** - The amount of Lambda memory in MB
        from 128-10240. The default is 1024.
      - **LambdaTimeout** - The maximum Lambda invocation runtime in seconds. The
        default is 30.
      - **VPCSecurityGroupIds** and **VPCSubnetIds** - Information
        for the VPC where the Hive metastore exists.

   8. Select **I acknowledge that this app creates custom IAM roles and resource policies**. For more information, choose the **Info** link.
   9. At the bottom right of the **Application settings** section, choose **Deploy**. When the deployment is complete, the Lambda function appears in the **Resources** section in the Lambda console.
      The application is deployed to Lambda. Its name is prepended with
      **serverlessrepo-** to indicate that the application was deployed from
      the AWS Serverless Application Repository. Selecting the application takes you to the **Resources** page
      where each of the resources of the application that were deployed are listed. The
      resources include the Lambda function that allows communication between the Data Catalog and the
      Hive metastore, the AWS Glue connection, and other resources that are needed for the database
      federation.

2. ###### Create a federated database in the Data Catalog.

After you've created a connection to the Hive metastore, you can create
federated databases in the Data Catalog that point to the external Hive metastore databases.
You need to create a corresponding database in the Data Catalog for every Hive metastore
database that you're connecting to the Data Catalog.

Lake Formation console

    1. On the **Data sharing** page, choose the
     **Shared databases** tab, and then choose **Create
     database**.
    2. For **Connection name**, choose the name of your Hive metastore connection
     from the dropdown menu.
    3. Enter a unique database name and the federation source identifier for the database. This is
     the name that you use in your SQL statements when you query tables. The name can
     consist of a maximum of 255 characters maximum and must be unique within your
     account.
    4. Choose **Create database**.

AWS CLI

```
aws glue create-database \
'{
 "CatalogId": "`<111122223333>`",
  "database-input": {
    "Name":"`<fed_glue_db>`",
    "FederatedDatabase":{
        "Identifier":"`<hive_db_on_emr>`",
        "ConnectionName":"`<hms_connection>`"
     }
   }
 }'

```

3. ###### View tables in the federated database.

After you've created the federated database, you can view the list of tables in your
Hive metastore using the Lake Formation console or the AWS CLI.

Lake Formation console

    1. Select the database name from the **Shared databases**
     tab.
    2. On the **Databases** page, choose **View
     tables**.

AWS CLI
The following examples show how to retrieve the connection definition, the
database name, and some or all tables in the database. Replace the ID of the Data
Catalog with the valid AWS account ID that you used to created the database.
Replace `hms_connection` with the connection name.

```
aws glue get-connection \
--name `<hms_connection>`  \
--catalog-id `111122223333`
```

```
aws glue get-database \
--name `<fed_glu_db>` \
--catalog-id `111122223333`
```

```
aws glue get-tables \
--database-name `<fed_glue_db>` \
--catalog-id `111122223333`
```

```
aws glue get-table \
--database-name `<fed_glue_db>` \
--name `<hive_table_name>` \
--catalog-id `111122223333`
```

4. ###### Grant permissions.

After you’ve created the database, you can grant permissions to other IAM
users and roles in your account or to external AWS accounts and organizations. You will
not be able to grant write data permissions (insert, delete) and metadata permissions
(alter, drop, create) on the federated databases. For more information on granting
permissions, see [Managing Lake Formation permissions](managing-permissions.md "managing-permissions.md"). 5. ###### Query the federated databases.

After you grant permissions, users can sign in and start querying the
federated database using Athena and Amazon Redshift. Users can now use the local database name to
reference the Hive database in SQL queries.

**Example Amazon Athena query syntax**

Replace `fed_glue_db` with the local database name that you created
earlier.

`Select * from fed_glue_db.customers limit 10;`
