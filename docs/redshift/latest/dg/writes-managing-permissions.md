Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Managing permissions for a

datashares in Amazon Redshift

As a producer administrator, you retain control for the datasets you are
sharing. You can add new objects to or remove them from the datashare. You can
also grant or revoke access to datashares as a whole for the consumer clusters,
AWS accounts, or AWS Regions. When permissions are revoked, consumer clusters
immediately lose access to the shared objects and stop seeing them in the list of
INBOUND datashares in SVV_DATASHARES.

The following example creates the datashare `salesshare`, adds the
schema `public`, and adds the table
`public.tickit_sales_redshift` to `salesshare`. It also
grants usage permissions on `salesshare` to the specified
namespace.

```
CREATE DATASHARE salesshare;

ALTER DATASHARE salesshare ADD SCHEMA public;

ALTER DATASHARE salesshare ADD TABLE public.tickit_sales_redshift;

GRANT USAGE ON DATASHARE salesshare TO NAMESPACE '13b8833d-17c6-4f16-8fe4-1a018f5ed00d';
```

For CREATE DATASHARE, superusers and database owners can create datashares. For
more information, see [CREATE DATASHARE](r_CREATE_DATASHARE.md "r_CREATE_DATASHARE.md"). For ALTER DATASHARE, the owner of the
datashare with the required permissions on the datashare objects to be added or
removed can alter the datashare. For information, see [ALTER DATASHARE](r_ALTER_DATASHARE.md "r_ALTER_DATASHARE.md").

As a producer administrator, when you drop a datashare, it stops being listed
on consumer clusters. The databases and schema references created on the consumer
cluster from the dropped datashare continue to exist with no objects in them. The
consumer administrator must delete these databases manually.

On the consumer side, a consumer administrator can determine which users and
roles should get access to the shared data by creating a database from the
datashare. Depending on the options you choose when creating the database, you can
control access to it as follows. For more information about creating a database
from a datashare, see [CREATE DATABASE](r_CREATE_DATABASE.md "r_CREATE_DATABASE.md").

For more information about setting up a datashare and reading data from a
consumer, see [Sharing read access to
data within an AWS account](within-account.md "within-account.md").

###### Creating the database without the WITH PERMISSIONS clause

An administrator can control access at the database or schema level. To
control access at the schema level, the administrator must create an external
schema from the Amazon Redshift database created from the datashare.

The following example grants permissions to access a shared table at the
database level and schema level.

```
GRANT USAGE ON DATABASE sales_db TO Bob;

CREATE EXTERNAL SCHEMA sales_schema FROM REDSHIFT DATABASE sales_db SCHEMA 'public';

GRANT USAGE ON SCHEMA sales_schema TO ROLE Analyst_role;
```

To further restrict access, you can create views on top of shared objects,
exposing only the necessary data. You can then use these views to give access to
the users and roles.

After the users are granted access to the database or schema, they will have
access to all shared objects in that database or schema.

###### Creating the database with the WITH PERMISSIONS clause

After granting usage rights on the database or schema, an administrator can
further control access using the same permission granting process as they would
on a local database or schema. Without individual object permissions, users
can’t access any objects in the datashared database or schema even after being
granted the USAGE permission.

The following example grants permissions to access a shared table at the
database level.

```
GRANT USAGE ON DATABASE sales_db TO Bob;
GRANT USAGE FOR SCHEMAS IN DATABASE sales_db TO Bob;
GRANT SELECT ON sales_db.public.tickit_sales_redshift TO Bob;
```

After being granted access to the database or schema, users still need to be
given the relevant permissions for any objects in the database or schema that you
want them to access.

## Granular sharing using WITH

PERMISSIONS

You can use granular sharing using WITH PERMISSIONS to enable clusters or
Serverless workgroups to query the datashare. This process assumes the
datashare is originating from another cluster or Amazon Redshift Serverless namespace
in your account, or it is coming from another account and has been
associated with the namespace you are using.

1. The consumer database administrator can create a database from the
   datashare.

```
CREATE DATABASE my_ds_db [WITH PERMISSIONS] FROM DATASHARE my_datashare OF NAMESPACE 'abc123def';
```

If you create a database WITH PERMISSIONS, you can grant granular
permissions on datashare objects to different users and roles. Without
this, all users and roles granted USAGE permission on the datashare
database are granted all permissions on all objects within the
datashare database. 2. The following shows how to grant permissions to a Redshift
database user or role. You must be connected to a local database to
run these statements. You cannot run these statements if you execute a
USE command on the datashare database before running the grant
statements.

```
GRANT USAGE ON DATABASE my_ds_db TO ROLE data_eng;
GRANT CREATE, USAGE ON SCHEMA my_ds_db.my_shared_schema TO ROLE data_eng;
GRANT ALL ON ALL TABLES IN SCHEMA my_ds_db.my_shared_schema TO ROLE data_eng;

GRANT USAGE ON DATABASE my_ds_db TO bi_user;
GRANT USAGE ON SCHEMA my_ds_db.my_shared_schema TO bi_user;
GRANT SELECT ON my_ds_db.my_shared_schema.table1 TO bi_user;
```
