# Create AWS Glue connections

(for administrators)

To use data sources with the SQL extension, administrators can set up AWS Glue connections
for each data source. These connections store the necessary configuration details to access
and interact with the data sources. Once the connections are created, and the [appropriate
permissions](sagemaker-sql-extension-datasources-connection-permissions.md "sagemaker-sql-extension-datasources-connection-permissions.md") are granted, the connections become visible to all users of the [Amazon SageMaker Studio spaces](studio-updated-spaces.md "studio-updated-spaces.md") that share the same execution role.

To create these connections:

- First, create a JSON file that defines the connection properties for each data source.
  The JSON file includes details such as the data source identifier, access credentials, and
  other relevant configuration parameters to access the data sources through the AWS Glue connections.
- Then use the AWS Command Line Interface (AWS CLI) to create the AWS Glue connection, passing
  the JSON file as a parameter. The AWS CLI command reads the connection details
  from the JSON file and establishes the appropriate connection.

###### Note

The SQL extension supports creating connections using the AWS CLI
only.
Before creating AWS Glue connections, ensure that you complete the following steps:

- Install and configure the AWS Command Line Interface (AWS CLI). For more information about
  how to install and configure the AWS CLI, see [About AWS CLI version
  2](../../../cli/latest/userguide/cli-chap-welcome.md "../../../cli/latest/userguide/cli-chap-welcome.md"). Ensure that the access keys and tokens of the IAM user or role used to
  configure the AWS CLI have the required permissions to create AWS Glue
  connections. Add a policy that allows the `glue:CreateConnection` action
  otherwise.
- Understand how to use AWS Secrets Manager. We recommend that you use Secrets Manager to provide connection
  credentials and any other sensitive information for your data store. For more information
  on using Secrets Manager to store credentials, see [Storing connection
  credentials in AWS Secrets Manager](../../../glue/latest/dg/connection-properties-secrets-manager.md "../../../glue/latest/dg/connection-properties-secrets-manager.md").

## Create a connection

definition JSON file

To create an AWS Glue connection definition file, create a JSON file to define the
connection details on the machine where you have installed and configured the AWS CLI. For this example, name the file
`sagemaker-sql-connection.json`.

The connection definition file should follow the following general format:

- **Name** is the name for the connection.
- **Description** is a textual description of the
  connection.
- **ConnectionType** is the type of connection. Choose
  `REDSHIFT`, `ATHENA`, or `SNOWFLAKE`.
- **ConnectionProperties** is a map of key-value pairs
  for the connection properties, such as the ARN of your AWS secret, or the
  name of your database.

```
{
    "ConnectionInput": {
        "Name": <GLUE_CONNECTION_NAME>,
        "Description": <GLUE_CONNECTION_DESCRIPTION>,
        "ConnectionType": "REDSHIFT | ATHENA | SNOWFLAKE",
        "ConnectionProperties": {
            "PythonProperties": "{\"aws_secret_arn\": <SECRET_ARN>, \"database\": <...>}"
        }
    }
}
```

###### Note

- The properties within the `ConnectionProperties` key consist of
  stringified key-value pairs. Escape any double quotes used in the keys or values with
  a backslash (`\`) character.
- All properties available in Secrets Manager can also be directly provided through
  `PythonProperties`. However, it is not recommended to include sensitive
  fields such as passwords in `PythonProperties`. Instead, the preferred
  approach is to use Secrets Manager.

Connection definition files specific to different data stores can be found in the
following sections.

The connection definition files for each data source contain the specific properties and
configuration required to connect to those data stores from the SQL extension. Refer to
the appropriate section for details on defining connections to that source.

- To create an AWS Glue connection for Amazon Redshift, see the sample definition file in [Configure an
  AWS Glue connection for Amazon Redshift](#sagemaker-sql-extension-redshift-glue-connection-config "#sagemaker-sql-extension-redshift-glue-connection-config").
- To create an AWS Glue connection for Amazon Athena, see the sample definition file in [Configure an
  AWS Glue connection for Athena](#sagemaker-sql-extension-athena-glue-connection-config "#sagemaker-sql-extension-athena-glue-connection-config").
- To create an AWS Glue connection for Snowflake, see the sample definition file in [Configure an
  AWS Glue connection for Snowflake](#sagemaker-sql-extension-snowflake-glue-connection-config "#sagemaker-sql-extension-snowflake-glue-connection-config").

This section provides details on the secret and connection properties in JSON
definition files that are specific to Amazon Redshift. Before creating your connection
configuration file, we recommend storing your Amazon Redshift access credentials as a secret in
Secrets Manager. Alternatively, you can generate temporary database credentials based on
permissions granted through an AWS Identity and Access Management (IAM) permissions policy to manage the access
that your users have to your Amazon Redshift database. For more information, see [Using
IAM authentication to generate database user credentials](../../../redshift/latest/mgmt/generating-user-credentials.md "../../../redshift/latest/mgmt/generating-user-credentials.md").

#### Create a secret for Amazon Redshift

access credentials

###### To store Amazon Redshift information in AWS Secrets Manager

1. From the AWS console, navigate to Secrets Manager.
2. Choose **Store a new secret**.
3. Under **Secret type**, choose **Credentials for
   Amazon Redshift**.
4. Enter the administrator username and password configured when launching the
   Amazon Redshift cluster.
5. Select the Amazon Redshift cluster associated with the secrets.
6. Name your secret.
7. The remaining settings can be left at their default values for initial secret
   creation, or customized if required.
8. Create the secret and retrieve its ARN.

#### Configure

an AWS Glue connection for Amazon Redshift

The SQL extension connects to data sources using custom AWS Glue connections. For
general information on creating AWS Glue connections to connect a data source, see [Create AWS Glue connections
(for administrators)](sagemaker-sql-extension-datasources-glue-connection.md "sagemaker-sql-extension-datasources-glue-connection.md"). The following
example is a sample AWS Glue connection definition for connecting to Amazon Redshift.

Before creating a new connection, keep these recommendations in mind:

- The properties within the `PythonProperties` key consist of
  stringified key-value pairs. Escape any double quotes used in the keys or values
  with a backslash (`\`) character.
- In the connection definition file, enter the name and description of the
  connection, replace the ARN of the secret in `aws_secret_arn` with the
  ARN of the secret previously created.
- Ensure that the database declared by its name in the connection definition
  above matches the cluster database. You can verify this by going to the cluster
  details page on [Amazon Redshift console](https://console.aws.amazon.com/redshiftv2/ "https://console.aws.amazon.com/redshiftv2/"), and
  verifying the database name under **Database configurations** in
  **Properties** section.
- For additional parameters, see the list of connection properties supported by
  Amazon Redshift in [Amazon Redshift connection parameters](sagemaker-sql-extension-connection-properties.md#sagemaker-sql-extension-connection-properties-redshift "sagemaker-sql-extension-connection-properties.md#sagemaker-sql-extension-connection-properties-redshift").

###### Note

    + By default, the SQL extension connector for Python runs all queries in
     a transaction, unless the `auto_commit` in connection properties
     is set to `true`.
    + You can add all connection parameters, including the
     `database` name, to a secret.

```
{
  "ConnectionInput": {
      "Name": "`Redshift connection name`",
      "Description": "`Redshift connection description`",
      "ConnectionType": "REDSHIFT",
      "ConnectionProperties": {
          "PythonProperties":"{\"aws_secret_arn\": \"`arn:aws:secretsmanager:region:account_id:secret:secret_name`\", \"database\":\"`database_name`\", \"database_metadata_current_db_only\": false}"
      }
  }
}
```

Once your definition file is updated, follow the steps in [Create AWS Glue
connections](#sagemaker-sql-extension-datasources-glue-connection-creation "#sagemaker-sql-extension-datasources-glue-connection-creation") to create
your AWS Glue connection.

This section provides details on the connection properties in JSON definition files
that are specific to Athena.

#### Configure an

AWS Glue connection for Athena

The SQL extension connects to data sources using custom AWS Glue connections. For
general information on creating AWS Glue connections to connect a data source, see [Create AWS Glue connections
(for administrators)](sagemaker-sql-extension-datasources-glue-connection.md "sagemaker-sql-extension-datasources-glue-connection.md"). The following
example is a sample AWS Glue connection definition for connecting to Athena.

Before creating a new connection, keep these recommendations in mind:

- The properties within the `ConnectionProperties` key consist of
  stringified key-value pairs. Escape any double quotes used in the keys or values
  with a backslash (`\`) character.
- In the connection definition file, enter the name and description of the
  connection, replace the `catalog_name` with the name of your catalog,
  `s3_staging_dir` with the Amazon S3 URI (Uniform Resource Identifier) of
  your output directory in your Amazon S3 bucket, and the `region_name` with
  the region of your Amazon S3 bucket.
- For additional parameters, refer to the list of connection properties
  supported by Athena in [Athena connection parameters](sagemaker-sql-extension-connection-properties.md#sagemaker-sql-extension-connection-properties-athena "sagemaker-sql-extension-connection-properties.md#sagemaker-sql-extension-connection-properties-athena").

###### Note

    + You can add all connection parameters, including the
     `catalog_name` or `s3_staging_dir`, to a
     secret.
    + If you specify a `workgroup`, you don't need to specify
     `s3_staging_dir`.

```
{
    "ConnectionInput": {
        "Name": "`Athena connection name`",
        "Description": "`Athena connection description`",
        "ConnectionType": "ATHENA",
        "ConnectionProperties": {
            "PythonProperties": "{\"catalog_name\": \"`catalog_name`\",\"s3_staging_dir\": \"`s3://amzn-s3-demo-bucket_in_same_region/output_query_results_dir/`\", \"region_name\": \"`region\`"}"
        }
    }
}
```

Once your definition file is updated, follow the steps in [Create AWS Glue
connections](#sagemaker-sql-extension-datasources-glue-connection-creation "#sagemaker-sql-extension-datasources-glue-connection-creation") to create
your AWS Glue connection.

This section provides details on the secret and connection properties in JSON
definition files that are specific to Snowflake. Before creating your connection
configuration file, we recommend storing your Snowflake access credentials as a secret
in Secrets Manager.

#### Create a secret for

Snowflake access credentials

###### To store Amazon Redshift information in Secrets Manager

1. From the AWS console, navigate to AWS Secrets Manager.
2. Choose **Store a new secret**.
3. Under **Secret type**, choose **Other type of
   secret**.
4. In the key-value pair, choose **Plaintext**, and then copy
   the following JSON content. Replace the `user`, `password`,
   and `account` by their values.

```
{
    "user":"`snowflake_user`",
    "password":"`snowflake_password`",
    "account":"`account_id`"
}
```

5. Name the secret.
6. The remaining settings can be left at their default values for initial secret
   creation, or customized if required.
7. Create the secret and retrieve its ARN.

#### Configure

an AWS Glue connection for Snowflake

The SQL extension connects to data sources using custom AWS Glue connections. For
general information on creating AWS Glue connections to connect a data source, see [Create AWS Glue connections
(for administrators)](sagemaker-sql-extension-datasources-glue-connection.md "sagemaker-sql-extension-datasources-glue-connection.md"). The following
example is a sample AWS Glue connection definition for connecting to Snowflake.

Before creating a new connection, keep these recommendations in mind:

- The properties within the `ConnectionProperties` key consist of
  stringified key-value pairs. Escape any double quotes used in the keys or values
  with a backslash (`\`) character.
- In the connection definition file, enter the name and description of the
  connection, then replace the ARN of the secret in `aws_secret_arn` with
  the ARN of the secret previously created, and your account ID in
  `account`.
- For additional parameters, refer to the list of connection properties
  supported by Snowflake in [Snowflake connection parameters](sagemaker-sql-extension-connection-properties.md#sagemaker-sql-extension-connection-properties-snowflake "sagemaker-sql-extension-connection-properties.md#sagemaker-sql-extension-connection-properties-snowflake").

###### Note

You can add all connection parameters, including the `account`,
to a secret.

```
{
    "ConnectionInput": {
        "Name": "`Snowflake connection name`",
        "Description": "`Snowflake connection description`",
        "ConnectionType": "SNOWFLAKE",
        "ConnectionProperties": {
            "PythonProperties":  "{\"aws_secret_arn\": \"`arn:aws:secretsmanager:region:account_id:secret:secret_name`\", \"account\":\"`account_id`\"}"}"
        }
    }
}
```

Once your definition file is updated, follow the steps in [Create AWS Glue
connections](#sagemaker-sql-extension-datasources-glue-connection-creation "#sagemaker-sql-extension-datasources-glue-connection-creation") to create
your AWS Glue connection.

## Create AWS Glue

connections

To create an AWS Glue connection through the AWS CLI, use your connection
definition file and run this AWS CLI command. Replace the `region`
placeholder with your AWS Region name and provide the local path to your
definition file.

###### Note

The path to your configuration definition file must be preceded by
`file://`.

```
aws --region `region` glue create-connection --cli-input-json file://`path_to_file/sagemaker-sql-connection.json`
```

Verify that the AWS Glue connection was created by running the following command and check
for your connection name.

```
aws --region `region` glue get-connections
```

Alternatively, you can update an existing AWS Glue connection as follows:

- Modify the AWS Glue connection definition file as required.
- Run the following command to update the connection.

```
aws --region `region` glue update-connection --name `glue_connection_name` --cli-input-json file://`path_to_file/sagemaker-sql-connection.json`
```
