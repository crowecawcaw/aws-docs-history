Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Querying data through

AWS Lake Formation

Using AWS Lake Formation makes it easier to centrally govern and secure your data lake, and to
provide data access. Configuring identity propagation to Lake Formation through AWS IAM Identity Center and
Redshift makes it so an administrator can allow fine-grained access to an Amazon S3 data lake,
based on the organization's identity-provider (IdP) groups. These groups are managed through
AWS IAM Identity Center. This section shows how to configure a couple use cases, querying from a data
lake and querying from a data share, that demonstrate how to leverage AWS IAM Identity Center with
Redshift to connect to Lake Formation-governed resources.

## Using an

AWS IAM Identity Center and Redshift connection to query a data lake

These steps cover a use case where you use AWS IAM Identity Center connected to Redshift to query
a data lake that's governed by Lake Formation.

**Prerequisites**

This procedure has several prerequisite steps:

1. AWS IAM Identity Center must be set up to support authentication and identity management with
   Redshift. You can enable AWS IAM Identity Center from the console and select an identity-provider
   (IdP) source. After this, synchronize a set of your IdP users with AWS IAM Identity Center. You
   must also set up a connection between AWS IAM Identity Center and Redshift, following the steps
   detailed previously in this document.
2. Create a new Amazon Redshift cluster and enable identity management through AWS IAM Identity Center in
   the configuration steps.
3. Create a managed AWS IAM Identity Center application for Lake Formation and configure it. This follows
   setting up the connection between AWS IAM Identity Center and Redshift. The steps are the
   following:
   1. In the
      AWS CLI,
      use the
      `modify-redshift-idc-application`
      command
      to enable the Lake Formation service integration with the AWS IAM Identity Center
      managed application for Redshift. This call includes the
      `service-integrations` parameter, which is set to a configuration
      string value that enables authorization to Lake Formation.
   2. Configure Lake Formation by
      using
      the
      `create-lake-formation-identity-center-configuration`
      command. This creates an AWS IAM Identity Center application for Lake Formation, which
      is visible in the AWS IAM Identity Center portal. The administrator must set the
      `––cli-input-json` argument, whose value is the path to
      a JSON file that uses the standard format for all AWS CLI API calls. You must
      include values for the following:
      - `CatalogId` – The Lake Formation catalog ID.
      - `InstanceArn` – The AWS IAM Identity Center instance ARN
        value.

After the administrator completes the prerequisite configuration, the database
administrator can create an external schema for the purpose of querying the data
lake.

1. **The administrator creates the external schema**
   – The Redshift database administrator connects to the database and creates an
   external schema, using the following SQL statement:

```
CREATE EXTERNAL SCHEMA if not exists my_external_schema from DATA CATALOG database 'my_lf_integrated_db' catalog_id '12345678901234';
```

Note that specifying an IAM role isn't required in this case, because access is
managed through AWS IAM Identity Center. 2. **The administrator grants permissions** – The
administrator grants usage to an AWS IAM Identity Center group, which grants permissions on
Redshift resources. This is done by running a SQL statement like the
following:

```
GRANT USAGE ON SCHEMA "my_external_schema" to "MYCO:sales";
```

Subsequently, the administrator grants Lake Formation permissions on objects, based on
requirements for the organization, using the AWS CLI:

```
aws lakeformation grant-permissions ...
```

3. **Users run queries** – At this point, an
   AWS IAM Identity Center user that's part of the sales group, for illustration purposes, can log in
   via query editor v2 to the Redshift database. Then they can run a query that accesses a table
   in the external schema, like the following sample:

```
SELECT * from my_external_schema.table1;
```

## Using an

AWS IAM Identity Center and Redshift connection to connect to a datashare

You can access a datashare from a different Redshift data warehouse when access is
managed through AWS IAM Identity Center. To do this, you run a query to set up an external database.
Prior to completing these steps, it's assumed that you have a connection set up between
Redshift and AWS IAM Identity Center, and you've created the AWS Lake Formation application, as detailed in the
previous procedure.

1. **Creating the external database** – The
   administrator creates an external database for data sharing, referencing it through
   its ARN. The following is a sample that shows how to do it:

```
CREATE DATABASE "redshift_external_db" FROM ARN 'arn:aws:glue:us-east-1:123456789012:database/redshift_external_db-iad' WITH NO DATA CATALOG SCHEMA;
```

In this use case, where you are using AWS IAM Identity Center with Redshift for identity
management, the IAM role isn't included. 2. **The admin sets up permissions** – After
creating a database, the administrator grants usage to an AWS IAM Identity Center group. This
grants permissions on Redshift resources:

```
GRANT USAGE ON DATABASE "my_external_db" to "MYCO:sales";
```

The administrator also grants Lake Formation permissions on objects, using the AWS
CLI:

```
aws lakeformation grant-permissions ...
```

3. **Users run queries** – A user from the sales
   group can query a table in the database, based on the permissions assigned:

```
select * from redshift_external_db.public.employees;
```

For more information about granting permissions on a data lake and granting permissions
on data shares, see [Granting permissions
to users and groups](../../../lake-formation/latest/dg/grant-permissions-sso.md "../../../lake-formation/latest/dg/grant-permissions-sso.md"). For more information about granting usage to a schema or to a
database, see [GRANT](../dg/r_GRANT.md "../dg/r_GRANT.md").
