# Creating a resource link to a shared Data Catalog

table

You can create a resource link to a shared table in any AWS Region by using the AWS Lake Formation console, API, or
AWS Command Line Interface (AWS CLI).

###### To create a resource link to a shared table (console)

1. Open the AWS Lake Formation console at [https://console.aws.amazon.com/lakeformation/](https://console.aws.amazon.com/lakeformation/ "https://console.aws.amazon.com/lakeformation/"). Sign in as a principal who
   has the Lake Formation `CREATE_TABLE` permission on the database to contain the resource
   link.
2. In the navigation pane, choose **Tables** under Data Catalog, and
   then choose **Create**, **Resource link**.
3. On the **Create resource link** page, provide the following information:

**Resource link name**

Enter a name that adheres to the same rules as a table name. The name can be the
same as the target shared table.

**Database**

The database in the local Data Catalog to contain the resource link.

**Shared table owner Region**

If you are creating the resource link in a different Region, select the region
of the target shared table.

**Shared table**

Select a shared table from the list, or enter a local (owned) or shared table
name.

The list contains all the tables shared with your account. Note the database and
owner account ID that are listed with each table. If you don't see a table that you
know was shared with your account, check the following:

    * If you aren't a data lake administrator, check that the data lake
     administrator granted you Lake Formation permissions on the table.
    * If you are a data lake administrator, and your account is not in the same
     AWS organization as the granting account, ensure that you have accepted the
     AWS Resource Access Manager (AWS RAM) resource share invitation for the table. For more information,
     see [Accepting a resource share invitation from AWS RAM](accepting-ram-invite.md "accepting-ram-invite.md").

**Shared table's database**

If you selected a shared table from the list, this field is populated with the
shared table's database in the external account. Otherwise, enter a local database
(for a resource link to a local table) or the shared table's database in the
external account.

**Shared table owner**

If you selected a shared table from the list, this field is populated with the
shared table's owner account ID. Otherwise, enter your AWS account ID (for a
resource link to a local table) or the ID of the AWS account that shared the
table. 4. Choose **Create** to create the resource link.

You can then view the resource link name under the **Name** column on
the **Tables** page. 5. (Optional) Grant the Lake Formation `DESCRIBE` permission on the resource link to
principals that must be able to view the link and access the target table.

However, granting permissions on a resource link doesn't grant permissions on the
target (linked) database or table. You must grant permissions on the target database
separately for the table/resource link to be visible in Athena.

###### To create a resource link to a shared table in the same Region (AWS CLI)

1. Enter a command similar to the following.

```
aws glue create-table --database-name myissues --table-input '{"Name":"my_customers","TargetTable":{"CatalogId":"111122223333","DatabaseName":"issues","Name":"customers"}}'
```

This command creates a resource link named `my_customers` to the shared
table `customers`, which is in the database `issues` in the AWS
account 1111-2222-3333. The resource link is stored in the local database
`myissues`. 2. (Optional) Grant the Lake Formation `DESCRIBE` permission on the resource link to
principals that must be able to view the link and access the target table.

However, granting permissions on a resource link doesn't grant permissions on
the target (linked) table. You must grant permissions on the target database separately for the table/resource link to be visible in Athena.

###### To create a resource link to a shared table in a different Region (AWS CLI)

1. Enter a command similar to the following.

```
aws glue create-table --region eu-west-1 --cli-input-json '{
    "CatalogId": "111122223333",
    "DatabaseName": "ireland_db",
    "TableInput": {
        "Name": "rl_useast1salestb_ireland",
        "TargetTable": {
            "CatalogId": "444455556666",
            "DatabaseName": "useast1_salesdb",
            "Region": "us-east-1",
            "Name":"useast1_salestb"
        }
    }
}‘
```

This command creates a resource link named `rl_useast1salestb_ireland`
in the Europe (Ireland) Region to the shared table `useast1_salestb`, which
is in the database `useast1_salesdb` in the AWS account
444455556666 in the US East (N. Virginia) Region. The resource link is stored in the local database
`ireland_db`. 2. Grant the Lake Formation `DESCRIBE` permission to principals that must be able to
view the link and access the link target through the link.

However, granting permissions on a resource link doesn't grant permissions on the
target (linked) table. You must grant permissions on the target table separately for the
table/resource link to be visible in Athena.

###### See also:

- [How resource links work in Lake Formation](resource-links-about.md "resource-links-about.md")
- [DESCRIBE](lf-permissions-reference.md#perm-describe "lf-permissions-reference.md#perm-describe")
