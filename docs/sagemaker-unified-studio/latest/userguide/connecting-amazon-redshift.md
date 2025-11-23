# Connecting to Amazon Redshift

You can create a data connection to Amazon Redshift to query data warehouses from Amazon SageMaker Unified Studio.
You can connect to both provisioned clusters and serverless workgroups.

## VPC Requirements

Amazon Redshift connections use different connection methods depending on the tool you are
using in Amazon SageMaker Unified Studio.

- Visual ETL and data processing jobs require your Amazon Redshift database to be in the
  same VPC as Amazon SageMaker Unified Studio domain. To configure that refer to the following documentation:
  [Step 1](../adminguide/configure-vpc-networking-iam-based-domains.md "../adminguide/configure-vpc-networking-iam-based-domains.md"), [Step 2](../adminguide/update-individual-projects-vpc.md "../adminguide/update-individual-projects-vpc.md"). You might need to contact Administrator to complete that
  configuration.
- Query Editor and Data notebooks do not require VPC configuration.

## Steps to connect to Amazon Redshift from Amazon SageMaker Unified Studio

1. In the navigation pane, choose **Connections**.
2. Choose **Create connection**.
3. In the gallery that opens, select Amazon Redshift.
4. For **Name** enter a descriptive name for your connection.
5. Configure the connection properties:
   1. **Redshift compute** - Select existing compute or enter a JDBC
      URL.
      1. JDBC URL format: `jdbc:redshift://endpoint:port/database`.

   2. **EnforceSSL** - Select to enable encrypted communication
      (recommended).
   3. **JDBC URL Parameters** - Optional configuration parameters for
      the JDBC/ODBC driver in the following format:
      `<key1>=<value1>;<key2>=<value2>`.

6. Authentication option, you can select one of the options below
   1. **IAM** - generates a database username based on your IAM
      identity. You can apply grants directly to this user, or use the RedshiftDbUser
      principal tag on your project execution role to connect as a different database
      user.
   2. **Username and password** - Provide a username and password for
      the database that you are connecting to. We will store your credentials in AWS
      Secrets Manager.
   3. **AWS Secrets Manager** - Choose a secret in AWS Secrets
      Manager with the credentials. You might need to contact your Administrator to create
      a secret.

7. **Access role ARN** - optional. Required when connecting to
   resources in a different AWS account. See [Gaining access to Amazon Redshift resources](compute-prerequisite-redshift.md "compute-prerequisite-redshift.md").
8. Choose **Create connection**.

## Steps to connect to Amazon SageMaker Unified Studio from Amazon

Redshift console pages

These steps describe how Amazon Redshift customers can automatically create an Amazon
Redshift connection within the Amazon SageMaker Unified Studio environment from the Amazon
Redshift Management Console and Amazon Redshift Query Editor v2 (QEv2). This functionality
is available from the following Amazon Redshift console pages:

- Landing page
- Provisioned dashboard
- Serverless dashboard
- Cluster list
- Cluster detail
- Serverless workgroup and namespace list pages
- Workgroup and namespace detail pages

When a user selects the "Query in SageMaker Unified Studio" option, they will be
prompted to choose the Amazon Redshift cluster they want to use. Amazon SageMaker Unified Studio
will then issue temporary credentials and provision the session, redirecting the user into
the Amazon SageMaker Unified Studio environment where they can begin querying data
immediately.

## Steps to connect to Amazon SageMaker Unified Studio from Amazon Redshift Query Editor

v2

These steps describe how Amazon Redshift customers can automatically create an Amazon
Redshift connection within the Amazon SageMaker Unified Studio environment from the Amazon Redshift
Query Editor v2 (QEv2). This functionality is available within Amazon Redshift Query Editor
v2 under a "Run in SageMaker Unified Studio" button in the following locations.

- As a tooltip option next to the "Run" button in the SQL editor
- As a tooltip option next to the "Run" button in notebook cells

If the connection selected is using IAM authentication then when the user clicks on "Run
in Amazon SageMaker Unified Studio" button, the query currently typed in the active editor (SQL or
notebook cell) will be executed directly in the Amazon SageMaker Unified Studio environment.

## Redshift Access using IAM

Authentication

IAM authentication generates temporary database credentials based on your AWS
identity, eliminating the need to manage database passwords. When you connect using IAM
authentication, Amazon SageMaker Unified Studio maps your IAM identity to a database user.

### How IAM Authentication Works

When connecting with IAM authentication, your database username is automatically
generated based on your IAM identity. By default, the username follows the pattern
`IAMR:<your-federated-identity>`. You can customize this behavior
using the RedshiftDbUser principal tag on your project execution role to specify a
different database user.

### Using Principal Tags

Principal tags allow you to control which database user is used when connecting to
Redshift. Configure the RedshiftDbUser tag on your project execution role in IAM. When
this tag is set, your connection will use `IAMR:<tag-value>` as the
database username instead of the federated IAM identity.

For more information about setting up principal tags, see [Setting up principal tags to connect a cluster or workgroup from query editor
v2](../../../redshift/latest/mgmt/query-editor-v2-getting-started.md#query-editor-v2-principal-tags-iam "../../../redshift/latest/mgmt/query-editor-v2-getting-started.md#query-editor-v2-principal-tags-iam").

## Troubleshooting Database Access

If after establishing a connection, you do not see expected databases, schemas, or
tables, follow the steps described below.

First identify your effective database user by running the following SQL:

```
SELECT current_user;
```

Your database username follows these patterns:

- Federated: `IAMR:<your-federated-identity>`
- With RedshiftDbUser tag on the project execution role:
  `IAMR:<tag-value>`

### Common Access Issues

**Databases are not displayed**

Your database user lacks connection privileges. The database administrator
must grant:

```
GRANT CONNECT ON DATABASE <database_name> TO "IAMR:<your-identity>";
```

**Schemas are not displayed**

Your database user lacks schema usage privileges. The database administrator
must grant:

```
GRANT USAGE ON SCHEMA <schema_name> TO "IAMR:<your-identity>";
```

**Tables are not displayed**

Your database user lacks table access privileges. The database administrator
must grant:

```
GRANT SELECT ON ALL TABLES IN SCHEMA <schema_name> TO "IAMR:<your-identity>";
```

For more information on grants in Redshift, see [GRANT](../../../redshift/latest/dg/r_GRANT.md "../../../redshift/latest/dg/r_GRANT.md").
