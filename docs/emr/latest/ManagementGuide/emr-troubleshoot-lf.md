# Troubleshoot common issues when using Amazon EMR with AWS Lake Formation

This section walks you through the process of troubleshooting common issues when using
Amazon EMR with AWS Lake Formation.

## Data lake access not allowed

You must explicitly opt in to data filtering on Amazon EMR clusters before you can analyze and process data in your data lake. When data access fails, you will see a generic `Access is not allowed` message in the output of your notebook entries.

To opt in and allow data filtering on Amazon EMR, see [Allow data
filtering on Amazon EMR](../../../lake-formation/latest/dg/getting-started-setup.md#emr-switch "../../../lake-formation/latest/dg/getting-started-setup.md#emr-switch") in the _AWS Lake Formation Developer Guide_ for
instructions.

## Session expiration

The session timeout for EMR Notebooks and Zeppelin is controlled by the IAM Role for
Lake Formation's `Maximum CLI/API session duration` setting. The default value for this setting is one hour.
When a session timeout occurs, you will see the following message in the output of your
notebook entries when trying to run Spark SQL commands.

```
Error 401    HTTP ERROR: 401 Problem accessing /sessions/2/statements.
Reason:  JWT token included in request failed validation.
Powered by Jetty:// 9.3.24.v20180605   org.springframework.web.client.HttpClientErrorException: 401 JWT token included in request failed validation…
```

To validate your session, refresh the page. You will be prompted to re-authenticate
using your IdP and be redirected back to the Notebook. You can continue to run queries
after re-authentication.

## No permissions for user on requested table

When attempting to access a table that you do not have access to, you will see the
following exception in the output of your notebook entries when trying to run Spark SQL
commands.

```
org.apache.spark.sql.AnalysisException: org.apache.hadoop.hive.ql.metadata.HiveException: Unable to fetch table table.
Resource does not exist or requester is not authorized to access requested permissions.
(Service: AWSGlue; Status Code: 400; Error Code: AccessDeniedException; Request ID: …
```

To access the table, you must grant access to the user by updating the permissions
associated with this table in Lake Formation.

## Querying cross-account data shared with Lake Formation

When you use Amazon EMR to access data shared with you from another account, some Spark
libraries will attempt to call `Glue:GetUserDefinedFunctions` API operation. Since
versions 1 and 2 of the AWS RAM managed permissions does not support this action, you receive the
following error message:

`"ERROR: User: arn:aws:sts::012345678901:assumed-role/my-spark-role/i-06ab8c2b59299508a is not authorized to perform: glue:GetUserDefinedFunctions on resource: arn:exampleCatalogResource because no resource-based policy allows the glue:GetUserDefinedFunctions action"`

To resolve this error, the data lake administrator who created the resource share must
update the AWS RAM managed permissions attached to the resource share. Version 3 of the AWS RAM
managed permissions allows principals to perform the `glue:GetUserDefinedFunctions`
action.

If you create a new resource share, Lake Formation applies the latest version of the AWS RAM managed
permission by default, and no action is required by you. To enable cross-account data access for
existing resource shares, you need to update the AWS RAM managed permissions to version 3.

You can view the AWS RAM permissions assigned to resources shared with you in AWS RAM. The
following permissions are included in version 3:

```
Databases
  AWSRAMPermissionGlueDatabaseReadWriteForCatalog
  AWSRAMPermissionGlueDatabaseReadWrite

Tables
  AWSRAMPermissionGlueTableReadWriteForCatalog
  AWSRAMPermissionGlueTableReadWriteForDatabase

AllTables
  AWSRAMPermissionGlueAllTablesReadWriteForCatalog
  AWSRAMPermissionGlueAllTablesReadWriteForDatabase

```

###### To update AWS RAM managed permissions version of existing resource shares

You (data lake administrator) can either [update AWS RAM managed permissions to a newer version](../../../ram/latest/userguide/working-with-sharing-update-permissions.md "../../../ram/latest/userguide/working-with-sharing-update-permissions.md") by following instructions in the
_AWS RAM User Guide_ or you can revoke all existing
permissions for the resource type and regrant them. If you revoke permissions, AWS RAM deletes
the AWS RAM resource share associated with the resource type. When you regrant permissions, AWS RAM
creates new resource shares attaching the latest version of AWS RAM managed permissions.

## Inserting into, creating, and altering

tables

Inserting into, creating, or altering tables in databases protected by Lake Formation
policies is not supported. When performing these operations, you will see the following exception in the
output of your notebook entries when trying to run Spark SQL commands:

```
java.io.IOException: com.amazon.ws.emr.hadoop.fs.shaded.com.amazonaws.services.s3.model.AmazonS3Exception:
            Access Denied (Service: Amazon S3; Status Code: 403; Error Code: AccessDenied; Request ID: …
```

For more information, see [Limitations of Amazon EMR integration with AWS Lake Formation](emr-lf-scope.md#emr-lf-limitations "emr-lf-scope.md#emr-lf-limitations").
