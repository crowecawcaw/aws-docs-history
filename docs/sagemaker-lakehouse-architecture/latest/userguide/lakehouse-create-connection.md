# Creating connections in lakehouse architecture

Amazon SageMaker Unified Studio provides an interface for managing and utilizing data connections across various
AWS services and external data sources. With Amazon SageMaker Unified Studio, you create, configure, and manage
connections to databases, data warehouses, and applications all from a single platform.
Amazon SageMaker Unified Studio allows you to explore your connected data sources, preview sample data, and
seamlessly use these connections in SQL queries and Spark notebooks without having to switch
between different interfaces or manage complex connection details manually.

## Access the data explorer in a project

1. Open your web browser and navigate to Amazon SageMaker Unified Studio.
2. Enter your corporate credentials (usually integrated with Amazon IAM Identity
   Center).
3. After successful authentication, you'll be directed to the Amazon SageMaker Unified Studio home page. On
   the home page, you'll see a list of projects you have access to. Select the project
   you want to work with by clicking on its name.
4. From the dropdown menu, select the **Data** or **Data
   Management** option. This will open the Data section of the project
   overview page. In this data explorer, you can see a tree-like structure representing
   your data sources.

## Create a new connection to add data

sources

###### To add a new data source

1. In the data explorer, select the **+** button. Click this button
   to start adding a new data source.
2. In the modal, select **Add connection**. You'll be presented with
   a gallery of connector options. Select the connector you need. For supported data
   sources, see .

###### Note

lakehouse architecture currently supports lowercase table, column, and database names. For
optimal experience in lakehouse architecture, ensure that all database identifiers are in
lowercase. 3. You must configure your connector details. For example, if you choose to use a
DynamoDB connection (preview), fill in the required fields, which can include:

    * Name: A unique identifier for this connection in Amazon SageMaker Unified Studio.


    * Description (optional): A description of the connection.

###### Note

Each supported data source can have different parameters for the connection.
Contact your administrator if you need them.

To see your DynamoDB tables displayed in lakehouse architecture after you add the connection, your
administrator must grant you access through resource policies in the Amazon DynamoDB
console.

###### To grant access to a DynamoDB table, your administrator can complete the following

steps.

1. Sign in to the AWS Management Console and open the Amazon DynamoDB console at [https://console.aws.amazon.com/dynamodb/](https://console.aws.amazon.com/dynamodb/ "https://console.aws.amazon.com/dynamodb/").
2. On the left navigation of the DynamoDB console, choose
   **Tables**.
3. From the **Tables** page, choose the table to add access
   to.
4. On the details page of the selected table, choose
   **Permission**.
5. On the **Resource-based policy for table** section, update the
   policy with the project role ARN in `Condition`.

###### Note

You can find the project ARN on the Page details page in the lakehouse architecture.

The following is an example policy. It allows access of the IAM role named
`datazone_user_role_projectid` to perform the allowed actions
(`Query`, `Scan`, `DescribeTable`,
`PartiQLSelect`) on the specified DynamoDB table. Administrators should
choose to allow or deny the set of actions.

```
{
    "Sid": "Statement1",
    "Effect": "Allow",
    "Principal": "*",
    "Action": [
        "dynamodb:Query",
        "dynamodb:Scan",
        "dynamodb:DescribeTable",
        "dynamodb:PartiQLSelect"
     ],
    "Resource": "arn:aws:dynamodb:`region`:`account`:table/`table_name`",
    "Condition": {
        "ArnEquals": {
        "aws:PrincipalArn": "arn:aws:iam::`region`:role/`datazone_user_role_projectid`"
        }
    }
}
```

## Explore a connected data source

After you have connected your data source, you can explore the data source in the data
explorer.

1. After your connection is created, return to the data explorer.
2. You should now see your new connection listed in
   **Lakehouse**.
3. Expand the new connection to view available databases.
4. Expand a database to explore its schema.
5. You can select a table name to view more details about that table, such as Schema
   details and a list of tables. You can then examine the tables themselves by selecting
   a table.
6. You will be able to see tabs for **Columns** and **Sample
   data**. In the **Columns** view, you can view a list of
   columns in the table, as well as the data types for each column. In the
   **Sample data** view, you can see the rows of data from the table
   and use built-in sorting and filtering options to explore the data.

## Authentication and tagging for creating

connections

You administrator must create credentials and configure the secret tags for you before
you create a connection.

**Credentials**

When creating a connection, if you choose a data source that requires the credentials
for **Authentication**, contact your administrator because they must
create and provide these credentials. There are two types of the credentials:

- User name and password
- AWS Secrets Manager

**Secret tags**

- To ensure the secret can only be used for a particular project, your administrator
  must tag with the `AmazonDataZoneProject` tag key and the value will be
  `projectId`.
- To use the secret across multiple projects, your administrator must tag the secret
  with `for-use-with-all-datazone-projects = true`.
