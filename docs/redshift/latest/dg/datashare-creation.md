Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Creating datashares

With Amazon Redshift, you can share live data across Amazon Redshift clusters or AWS accounts using
datashares. A datashare is a consumer-producer object that allows you to share live
data from your Amazon Redshift cluster with other clusters or AWS accounts. Creating
datashares enables secure data sharing while maintaining control over access and
ensuring data remains up-to-date. The following sections provide details on creating
datashares and adding database objects such as schemas, tables, and views to share
live data securely.

## Create a datashare

A datashare is a logical container of database objects, permissions, and
consumers. Consumers are Amazon Redshift provisioned clusters or Amazon Redshift Serverless namespaces
in your account and other AWS accounts. Each datashare is associated with the
database it's created in and only objects from that database can be added. As a
producer administrator, you can create datashares on the console and with SQL by
following one of the below procedures.

Console

On the console, you can create datashares from the
**Datashares** tabs in the cluster or namespace
details page. After the datashare is created, you can create databases
from the datashare on a consumer as a consumer administrator.

1. Sign in to the AWS Management Console and open the Amazon Redshift console at
   [https://console.aws.amazon.com/redshiftv2/](https://console.aws.amazon.com/redshiftv2/ "https://console.aws.amazon.com/redshiftv2/").
2. On the navigation menu, choose **Clusters**,
   then choose your cluster. The cluster details page appears.
3. In the cluster or namespace details page, from the
   **Datashares** tab, in the
   **Datashares** section, connect to a database
   if you don't have a database connection. In the
   **Datashares created in my account** section,
   choose **Create datashare**. The **Create
   datashare** page appears.
4. Choose **Create datashare**. You can only
   create a datashare from a local database. If you haven't
   connected to the database, the **Connect to
   database** page appears. Follow the steps in [Connecting to a database](connect-database-console.md "connect-database-console.md") to connect to a
   database. If there is a recent connection, the **Create
   datashare** page appears.
5. In the **Datashare information** section,
   choose one of the following:
   - Choose **Datashare** to create datashares
     to share data for read or write purpose across different Amazon Redshift
     data warehouses (provisioned clusters or Serverless
     endpoints) or in the same AWS account or different
     AWS accounts.
   - Choose **AWS Data Exchange datashare** to create
     datashares to license your data through AWS Data Exchange.

6. Specify values for **Datashare name**,
   **Database name**, and **Publicly
   accessible**. When you change the database name, make a
   new database connection.
7. Add objects to your datashare either using the **Scoped
   permissions** or **Direct
   permissions** sections. To add objects to a datashare,
   see [Creating a datashare in Amazon Redshift](writes-creating-datashare.md "writes-creating-datashare.md").
8. In the **Data consumers** section, you can
   choose to publish to Amazon Redshift, or publish to the AWS Glue Data Catalog, which
   starts the process of sharing data with Lake Formation. Publishing your
   datashare to Amazon Redshift means sharing your data with another namespace or
   Amazon Redshift account that acts as the consumer.

###### Note

Once the datashare is created, you can't edit the
configuration to publish to the other option. 9. Choose **Create datashare**.

SQL
The following command creates a datashare:

```
CREATE DATASHARE salesshare;
```

At the time of datashare creation, each datashare is associated with a
database. Only objects from that database can be shared in that
datashare. Multiple datashares can be created on the same database with
the same or different granularity of objects. There is no limit on the
number of datashares a cluster can create. You can also use the Amazon Redshift
console to create datashares. For more information, see [CREATE DATASHARE](r_CREATE_DATASHARE.md "r_CREATE_DATASHARE.md").

You can also control security restrictions to the datashare during
creation. The following example shows that the consumer with a public IP
access is allowed to read the datashare.

```
CREATE DATASHARE my_datashare [PUBLICACCESSIBLE = TRUE];
```

Setting PUBLICACCESSIBLE = TRUE allows consumers to query your
datashare from publicly accessible clusters and provisioned workgroups.
Leave this out or explicitly set it to false if you do not want to allow
it.

You can modify properties about the type of consumers after you create
a datashare. For example, you can define that clusters that want to
consume data from a given datashare can't be publicly accessible. Queries
from consumer clusters that don't meet security restrictions specified in
datashare are rejected at query runtime. For more information, see [ALTER DATASHARE](r_ALTER_DATASHARE.md "r_ALTER_DATASHARE.md").

## Add datashare objects to

datashares

You can add database objects of various types on the console and with SQL by
following one of the below procedures.

Console
You can add objects to your datashare either using **Scoped
permissions** or **Direct permissions**
sections. Select either **Grant scoped permissions** or
**Grant direct permissions** to add objects. Select
the **Add** button to add objects. A dialog appears.
Perform the following steps:

1. If you select **Grant scoped permissions**, the
   **Grant scoped permissions** page appears where
   you can grant scoped permissions at either a database or a schema
   level. Datashares with scoped permissions have the specified
   permissions on all current and future objects within the database
   or schema. For more details see, [Scoped permissions](t_scoped-permissions.md "t_scoped-permissions.md").
   1. Next, select **Database scoped
      permissions** to grant scoped permissions at the
      database level. When you grant scoped permissions, they apply
      to the current database while creating the datashare. These
      permissions can’t be granted to individual objects and are
      applicable to both existing and new objects (schemas, tables,
      views, UDFs).
   2. Select the scoped permission(s) for the schemas, table or
      views or user-defined functions. This means all objects in
      the database have the selected permissions granted to
      consumers. Select **Grant** to complete
      granting database scoped permissions.
   3. Then, select **Schema scoped
      permissions** to grant scoped permissions at the
      schema level. When you grant schema-scoped permissions, all
      objects added to the schema have the specified datashare
      permissions.
   4. Select the schema you want to add to the datashare from
      the dropdown. You can select only a single schema at a time.
      Then, select direct permission(s) you want to grant on the
      selected schema.
   5. Select scoped permission(s) for your schema objects such
      as tables, views and user-defined functions. Permissions are
      granted on all matching objects in the schema. These can be
      either existing objects or those added in the future. When
      it's applied, you can't remove a permission from an object
      without revoking the scoped permissions.
   6. Select **Grant** to complete granting
      schema scoped permissions.

2. If you select **Grant direct permissions**, the
   **Grant direct permissions** page appears where
   you can grant direct permissions at each objects level such as
   schema, table, view or user-defined function. To grant direct
   permissions, you must first add the relevant schemas to the
   datashare.
   1. Next, select **Grant direct permissions**
      to schemas to apply direct permissions on specific schema.
      Then, select schema permission(s) for your schema objects
      such as tables, views and user-defined functions and select
      the schema you want added to the datashare. Select
      **Grant** to complete adding schema to
      the datashare.
   2. After you have a schema added to your datashare, you can
      proceed with adding direct permissions for your schema
      objects. Select **Grant direct permissions** again. The **Grant direct
      permissions** page appears. Then, navigate to the
      direct permissions tabs for schema objects.
   3. Select **Grant direct permissions to tables and
      views** to grant object level direct permissions
      on these objects. Select the required direct permission(s)
      and the required objects from the list. Use the search field
      to find datashare objects. Select Grant to complete adding
      tables and views to the datashare.
   4. Select **Grant direct permissions to user-defined
      functions** to grant object level direct
      permissions on user-defined functions. Select the required
      direct permission(s) and the required objects from the list.
      Use the search field to find datashare objects. Select
      **Grant** to complete adding user-defined
      functions to the datashare.

3. You can also choose whether you want to **Add future
   objects**. When you choose to include datashare objects
   added to the schema, it means that objects added to the schema are
   added to the datashare automatically.
4. Choose **Add** to complete the section and add
   the objects. They're listed under the **Datashare
   objects**.
5. After you add objects, you can select individual objects and
   edit their permissions. If you select a schema, a dialog appears
   that asks if you would like to add **Scoped
   permissions**. This makes it so each existing or added
   object to the schema has a pre-selected set of permissions,
   appropriate for the object type. For instance, the administrator
   can set that all added tables have SELECT and UPDATE permissions,
   for instance.
6. All datashare objects are listed under the **Scoped
   permissions** or **Direct
   permissions** sections.
7. In the **Data consumers** section, you can add
   namespaces or add AWS accounts as consumers of the datashare.
8. Choose **Create datashare** to save your
   changes.

After you create the datashare, it appears in the list under
**Datashares created in my namespace**. If you choose
a datashare from the list, you can view its consumers, its objects, and
other properties.

SQL
With SQL, the datashare owner must grant USAGE on the schemas they
want to add to the datashare. The GRANT is used to grant various actions
on the schema, including CREATE and USAGE. The schemas hold shared
objects:

```
CREATE SCHEMA myshared_schema1;
CREATE SCHEMA myshared_schema2;

GRANT USAGE ON SCHEMA myshared_schema1 TO DATASHARE my_datashare;
GRANT CREATE, USAGE ON SCHEMA myshared_schema2 TO DATASHARE my_datashare;
```

Alternatively, the administrator can continue to run ALTER commands to
add a schema to the datashare. Only USAGE permissions are granted when a
schema is added this way.

```
ALTER DATASHARE my_datashare ADD SCHEMA myshared_schema1;
```

After the administrator adds schemas, they can grant datashare
permissions on objects in the schema. These can be both read and write
permissions. The GRANT ALL sample shows how to grant all
permissions.

```
GRANT SELECT, INSERT ON TABLE myshared_schema1.table1, myshared_schema1.table2, myshared_schema2.table1
TO DATASHARE my_datashare;

GRANT ALL ON TABLE myshared_schema1.table4 TO DATASHARE my_datashare;
```

You can continue to run commands like ALTER DATASHARE to add tables.
When you do, only SELECT permissions are granted on the objects
added.

```
ALTER DATASHARE my_datashare ADD TABLE myshared_schema1.table1, myshared_schema1.table2, myshared_schema2.table1;
```

You can grant scoped permissions to a datashare on all objects of a
type within a database or schema. Datashares with scoped permissions have
the specified permissions on all current and future objects within the
database or schema.

You can view the scope of database-level scoped permissions in [SVV_DATABASE_PRIVILEGES](r_SVV_DATABASE_PRIVILEGES.md "r_SVV_DATABASE_PRIVILEGES.md"). You can view the scope of
schema-level scoped permissions in [SVV_SCHEMA_PRIVILEGES](r_SVV_SCHEMA_PRIVILEGES.md "r_SVV_SCHEMA_PRIVILEGES.md").

The following is the syntax for granting scoped permissions to
datashares. For more information about scoped permissions, see [Scoped permissions](t_scoped-permissions.md "t_scoped-permissions.md").

```
GRANT { CREATE | USAGE | ALTER | DROP } [,...] | ALL [ PRIVILEGES ] }FOR SCHEMAS IN
DATABASE db_name
TO DATASHARE { datashare_name}

GRANT { { SELECT | INSERT | UPDATE | DELETE | DROP | ALTER | TRUNCATE | REFERENCES } [, ...] } | ALL [PRIVILEGES] } }FOR TABLES IN
{SCHEMA schema_name [DATABASE db_name ] | DATABASE db_name }
TO DATASHARE { datashare_name}

GRANT { EXECUTE | ALL [ PRIVILEGES ] }FOR FUNCTIONS IN
{SCHEMA schema_name [DATABASE db_name ] | DATABASE db_name }
TO DATASHARE { datashare_name}
```

## Add data consumers to

datashares

You can add one or more data consumers to the datashares. Data consumers can be
namespaces that uniquely identified Amazon Redshift clusters or AWS accounts.

You must explicitly choose to turn off or turn on sharing your datashare to
clusters with public access.

- Choose **Add namespaces to the datashare**. Namespaces
  are globally unique identifier (GUID) for Amazon Redshift cluster.
- Choose **Add AWS accounts** to the datashare. The
  specified AWS accounts must have access permissions to the
  datashare.
