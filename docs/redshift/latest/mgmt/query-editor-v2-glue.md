Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Querying the AWS Glue Data Catalog

You can use query editor v2 to query data cataloged in your AWS Glue Data Catalog by using specific SQL
commands and granting the permissions outlined in this section. By default, the AWS Glue Data Catalog
is listed as a query editor v2 database named `awsdatacatalog`. Querying the AWS Glue Data Catalog
is not available in all Amazon Redshift AWS Regions. Use the SHOW command to determine if this
capability is available. For more information about AWS Glue, see [What is AWS Glue?](../../../glue/latest/dg/what-is-glue.md "../../../glue/latest/dg/what-is-glue.md") in the
_AWS Glue Developer Guide_.

###### Note

Querying the AWS Glue Data Catalog is only supported in Amazon Redshift RA3 node type clusters and
Amazon Redshift Serverless.

You can configure your data warehouse and view the AWS Glue database objects cataloged
using the following SQL commands:

- SHOW – to display whether `awsdatacatalog` is mounted for the
  currently connected data warehouse. For example, to show the
  `data_catalog_auto_mount` parameter value, run:

```
SHOW data_catalog_auto_mount;
```

For more information, see [SHOW](../dg/r_SHOW.md "../dg/r_SHOW.md") in the
_Amazon Redshift Database Developer Guide_.

- ALTER SYSTEM – to change the system-level configuration of
  `data_catalog_auto_mount`. For example, to change the
  `data_catalog_auto_mount` parameter value to `on`,
  run:

```
ALTER SYSTEM SET data_catalog_auto_mount = on;
```

The change takes effect when a provisioned cluster is rebooted or a serverless
workgroup is automatically paused and resumed. For more information, see [ALTER
SYSTEM](../dg/r_ALTER_SYSTEM.md "../dg/r_ALTER_SYSTEM.md") in the _Amazon Redshift Database Developer Guide_.

- SHOW SCHEMAS – shows a list of schemas. The schemas in the database named
  `awsdatacatalog` represent the AWS Glue databases cataloged in the
  AWS Glue Data Catalog. For example, to show these schemas, run:

```
SHOW SCHEMAS FROM DATABASE awsdatacatalog;
```

For more information, see [SHOW SCHEMAS](../dg/r_SHOW_SCHEMAS.md "../dg/r_SHOW_SCHEMAS.md") in the
_Amazon Redshift Database Developer Guide_.

- SHOW TABLES – shows a list of tables in a schema. For example, to show the
  tables in the AWS Glue Data Catalog database named `awsdatacatalog` that are in
  schema `myglue` run:

```
SHOW TABLES FROM SCHEMA awsdatacatalog.myschema;
```

For more information, see [SHOW TABLES](../dg/r_SHOW_TABLES.md "../dg/r_SHOW_TABLES.md") in the
_Amazon Redshift Database Developer Guide_.

- SHOW COLUMNS – shows a list of columns in a table. For example, to show the
  columns in the AWS Glue Data Catalog database named `awsdatacatalog` that are in
  schema `myglue` and table `mytable` run:

```
SHOW COLUMNS FROM TABLE awsdatacatalog.myglue.mytable;
```

For more information, see [SHOW COLUMNS](../dg/r_SHOW_COLUMNS.md "../dg/r_SHOW_COLUMNS.md") in the
_Amazon Redshift Database Developer Guide_.

###### To grant your IAM user or role permission to query the AWS Glue Data Catalog,

1. In the tree-view pane, connect to your initial database in your provisioned
   cluster or serverless workgroup using the **Database user name and
   password** authentication method. For example, connect to the
   `dev` database using the admin user and password you used when you
   created the cluster or workgroup.
2. In an editor tab, run the following SQL statement to grant an IAM user access to
   the AWS Glue Data Catalog.

```
GRANT USAGE ON DATABASE awsdatacatalog to "`IAM:myIAMUser`"
```

Where `IAM:myIAMUser` is an IAM user that you want to
grant usage privilege to the AWS Glue Data Catalog. Alternatively, you can grant usage
privilege to `IAMR:myIAMRole` for an IAM role. 3. In the tree-view pane, edit or delete the connection to the cluster or workgroup
you previously created. Connect to either your cluster or workgroup in one of the
following ways:

    * To access the `awsdatacatalog` database from a cluster, you
     must use the authentication method **Temporary credentials using
     your IAM identity**. For more information about this
     authentication method, see [Connecting to an Amazon Redshift database](query-editor-v2-connecting.md "query-editor-v2-connecting.md"). Your query editor v2 administrator
     might need to configure the **Account settings** for the
     account to display this authentication method on the connection
     window.
    * To access the `awsdatacatalog` database from a workgroup, you
     must use the authentication method **Federated user**. For
     more information about this authentication method, see [Connecting to an Amazon Redshift database](query-editor-v2-connecting.md "query-editor-v2-connecting.md").

4. With the granted privilege, you can use your IAM identity to run SQL against
   your AWS Glue Data Catalog.
   After connecting, you can use query editor v2 to query data cataloged in AWS Glue Data Catalog. On the query editor v2
   tree-view pane, choose the cluster or workgroup and `awsdatacatalog` database. In
   the editor or notebook pane, confirm the correct cluster or workgroup is chosen. The
   database chosen should be the initial Amazon Redshift database such as `dev`. For
   information about authoring queries, see [Authoring queries with Amazon Redshift](query-editor-v2-query-run.md "query-editor-v2-query-run.md") and [Notebooks in Amazon Redshift](query-editor-v2-notebooks.md "query-editor-v2-notebooks.md"). The
   database named `awsdatacatalog` is reserved to reference the external Data Catalog
   database in your account. Queries against the `awsdatacatalog` database can only
   be read-only. Use three-part notation to reference the table in your SELECT statement. Where
   the first part is the database name, the second part is the AWS Glue database name, and the
   third part is the AWS Glue table name.

```
SELECT * FROM awsdatacatalog.`<aws-glue-db-name`>.<`aws-glue-table-name`>;
```

You can perform various scenarios that read the AWS Glue Data Catalog data and populate Amazon Redshift
tables.

The following example SQL joins two tables that are defined in AWS Glue.

```
SELECT pn.emp_id, alias, role, project_name
FROM "awsdatacatalog"."empl_db"."project_name_table" pn,
"awsdatacatalog"."empl_db"."project_alias_table" pa
WHERE pn.emp_id = pa.emp_id;
```

The following example SQL creates an Amazon Redshift table and populates it with data from a join of
two AWS Glue tables.

```
CREATE TABLE dev.public.glue AS
SELECT pn.emp_id, alias, role, project_name
FROM "awsdatacatalog"."empl_db"."project_name_table" pn,
"awsdatacatalog"."empl_db"."project_alias_table" pa
WHERE pn.emp_id = pa.emp_id;
```

## Querying Amazon S3 tables (preview)

You can use query editor v2 to query data held in Amazon S3table catalogs mounted to the AWS Glue Data Catalog.
Amazon S3 table catalogs are mounted to the AWS Glue Data Catalog on creation, and automatically appear as external databases
on all provisioned clusters and serverless workgroups in the same AWS Region under the same account.
For more information on accessing Amazon S3 tables using Amazon Redshift, see
[Accessing Amazon S3 tables with Amazon Redshift](../../../AmazonS3/latest/userguide/s3-tables-integrating-redshift.md "../../../AmazonS3/latest/userguide/s3-tables-integrating-redshift.md") in the Amazon Simple Storage Service User Guide.
