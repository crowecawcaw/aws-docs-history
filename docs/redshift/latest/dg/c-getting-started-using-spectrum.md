Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Getting started with Amazon Redshift

Spectrum

In this tutorial, you learn how to use Amazon Redshift Spectrum to query data directly from files
on Amazon S3. If you already have a cluster and a SQL client, you can complete this tutorial with minimal setup.

###### Note

Redshift Spectrum queries incur additional charges. The cost of running the sample
queries in this tutorial is nominal. For more information about pricing, see [Amazon Redshift Spectrum
pricing](https://aws.amazon.com/redshift/pricing/#redshift-spectrum-pricing "https://aws.amazon.com/redshift/pricing/#redshift-spectrum-pricing").

## Prerequisites

To use Redshift Spectrum, you need an Amazon Redshift cluster and a SQL client that's connected
to your cluster so that you can run SQL commands. The cluster and the data files in
Amazon S3 must be in the same AWS Region.

For information about how to create an Amazon Redshift cluster, see
[Get started with Amazon Redshift provisioned data warehouses](../gsg/new-user.md "../gsg/new-user.md") in the _Amazon Redshift Getting Started Guide_.
For information about ways to connect to a cluster, see
[Connecting to Amazon Redshift data warehouses](../gsg/database-tasks.md "../gsg/database-tasks.md") in the _Amazon Redshift Getting Started Guide_.

In some of the examples that follow, the sample data is in the
US East (N. Virginia) Region (`us-east-1`), so you need a cluster that is also in `us-east-1`.
Or, you can use Amazon S3 to copy data objects from the following buckets and folders to your bucket in the AWS Region where your cluster is located:

- `s3://redshift-downloads/tickit/spectrum/customers/*`
- `s3://redshift-downloads/tickit/spectrum/sales_partition/*`
- `s3://redshift-downloads/tickit/spectrum/sales/*`
- `s3://redshift-downloads/tickit/spectrum/salesevent/*`

Run an Amazon S3 command similar to the following to copy sample data that is located in the US East (N. Virginia)
to your AWS Region. Before running the command create your bucket and folders in your bucket to match your Amazon S3 copy command.
The output of the Amazon S3 copy command confirms that the files are copied to the `bucket-name` in your desired AWS Region.

```
aws s3 cp s3://redshift-downloads/tickit/spectrum/ s3://`bucket-name`/tickit/spectrum/ --copy-props none --recursive
```

## Getting started with Redshift Spectrum using AWS CloudFormation

As an alternative to the following steps, you can access the Redshift Spectrum DataLake
AWS CloudFormation template to create a stack with an Amazon S3 bucket that you can query. For more
information, see [Launch your AWS CloudFormation stack and then query your data in Amazon S3](#c-getting-started-using-spectrum-query-s3-data-cfn "#c-getting-started-using-spectrum-query-s3-data-cfn").

## Getting started with Redshift Spectrum step

by step

To get started using Amazon Redshift Spectrum, follow these steps:

- [Step 1. Create an IAM
  role for Amazon Redshift](#c-getting-started-using-spectrum-create-role "#c-getting-started-using-spectrum-create-role")
- [Step 2: Associate the IAM
  role with your cluster](#c-getting-started-using-spectrum-add-role "#c-getting-started-using-spectrum-add-role")
- [Step 3: Create
  an external schema and an external table](#c-getting-started-using-spectrum-create-external-table "#c-getting-started-using-spectrum-create-external-table")
- [Step 4: Query your data
  in Amazon S3](#c-getting-started-using-spectrum-query-s3-data "#c-getting-started-using-spectrum-query-s3-data")

## Step 1. Create an IAM

role for Amazon Redshift

Your cluster needs authorization to access your external Data Catalog in AWS Glue or
Amazon Athena and your data files in Amazon S3. To provide that authorization, you reference an
AWS Identity and Access Management (IAM) role that is attached to your cluster. For more information about using
roles with Amazon Redshift, see [Authorizing
COPY and UNLOAD Operations Using IAM Roles](../mgmt/copy-unload-iam-role.md "../mgmt/copy-unload-iam-role.md").

###### Note

In certain cases, you can migrate your Athena Data Catalog to an AWS Glue Data
Catalog. You can do this if your cluster is in an AWS Region where AWS Glue is supported
and you have Redshift Spectrum external tables in the Athena Data Catalog. To use the AWS Glue Data
Catalog with Redshift Spectrum, you might need to change your IAM policies. For more information,
see [Upgrading to the AWS Glue
Data Catalog](../../../athena/latest/ug/glue-athena.md#glue-upgrade "../../../athena/latest/ug/glue-athena.md#glue-upgrade") in the _Athena User Guide_.

When you create a role for Amazon Redshift, choose one of the following approaches:

- If you are using Redshift Spectrum with either an Athena Data Catalog or AWS Glue Data Catalog, follow the
  steps outlined in [To create an IAM role for
  Amazon Redshift](#spectrum-get-started-create-role "#spectrum-get-started-create-role").
- If you are using Redshift Spectrum with an AWS Glue Data Catalog that is enabled for AWS Lake Formation, follow the steps outlined
  in these procedures:
  - [To create an IAM role
    for Amazon Redshift using an AWS Glue Data Catalog enabled for AWS Lake Formation](#spectrum-get-started-create-role-lake-formation "#spectrum-get-started-create-role-lake-formation")
  - [To grant SELECT permissions on the table to query in the Lake Formation database](#spectrum-get-started-grant-lake-formation-table "#spectrum-get-started-grant-lake-formation-table")

###### To create an IAM role for

Amazon Redshift

1. Open the [IAM
   console](https://console.aws.amazon.com/iam/home?#home "https://console.aws.amazon.com/iam/home?#home").
2. In the navigation pane, choose **Roles**.
3. Choose **Create role**.
4. Choose **AWS service** as the trusted entity, and then choose **Redshift** as the use case.
5. Under **Use case for other AWS services**, choose **Redshift - Customizable** and then choose **Next**.
6. The **Add permissions policy** page appears. Choose
   `AmazonS3ReadOnlyAccess` and `AWSGlueConsoleFullAccess`,
   if you're using the AWS Glue Data Catalog. Or choose
   `AmazonAthenaFullAccess` if you're using the Athena Data
   Catalog. Choose **Next**.

###### Note

The `AmazonS3ReadOnlyAccess` policy gives your cluster read-only
access to all Amazon S3 buckets. To grant access to only the AWS sample data bucket,
create a new policy and add the following permissions.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "s3:Get*",
 "s3:List*"
 ],
 "Resource": "arn:aws:s3:::redshift-downloads/*"
 }
 ]
}`

```

7. For **Role name**, enter a name for your role, for example
   `myspectrum_role`.
8. Review the information, and then choose **Create
   role**.
9. In the navigation pane, choose **Roles**. Choose the name of
   your new role to view the summary, and then copy the **Role
   ARN** to your clipboard. This value is the Amazon Resource Name (ARN)
   for the role that you just created. You use that value when you create external
   tables to reference your data files on Amazon S3.

###### To create an IAM role

for Amazon Redshift using an AWS Glue Data Catalog enabled for AWS Lake Formation

1. Open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. In the navigation pane, choose **Policies**.

If this is your first time choosing **Policies**, the
**Welcome to Managed Policies** page appears. Choose
**Get Started**. 3. Choose **Create policy**. 4. Choose to create the policy on the **JSON** tab. 5. Paste in the following JSON policy document, which grants access to the Data Catalog
but denies the administrator permissions for Lake Formation.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "RedshiftPolicyForLF",
 "Effect": "Allow",
 "Action": [
 "glue:*",
 "lakeformation:GetDataAccess"
 ],
 "Resource": "*"
 }
 ]
}`

```

6. When you are finished, choose **Review** to review the policy. The
   policy validator reports any syntax errors.
7. On the **Review policy** page, for **Name**
   enter `myspectrum_policy` to name the policy that you are
   creating. Enter a **Description** (optional). Review the policy
   **Summary** to see the permissions that are granted by your
   policy. Then choose **Create policy** to save your work.

After you create a policy, you can provide access to your users.

To provide access, add permissions to your users, groups, or roles:

- Users and groups in AWS IAM Identity Center:

Create a permission set. Follow the instructions in [Create a permission set](../../../singlesignon/latest/userguide/howtocreatepermissionset.md "../../../singlesignon/latest/userguide/howtocreatepermissionset.md") in the _AWS IAM Identity Center User Guide_.

- Users managed in IAM through an identity provider:

Create a role for identity federation. Follow the instructions in [Create a role for a third-party identity provider (federation)](../../../IAM/latest/UserGuide/id_roles_create_for-idp.md "../../../IAM/latest/UserGuide/id_roles_create_for-idp.md")
in the _IAM User Guide_.

- IAM users:
  - Create a role that your user can assume. Follow the instructions in [Create a role for an IAM user](../../../IAM/latest/UserGuide/id_roles_create_for-user.md "../../../IAM/latest/UserGuide/id_roles_create_for-user.md") in the _IAM User Guide_.
  - (Not recommended) Attach a policy directly to a user or add a user to a user group. Follow the instructions in [Adding permissions to a user (console)](../../../IAM/latest/UserGuide/id_users_change-permissions.md#users_change_permissions-add-console "../../../IAM/latest/UserGuide/id_users_change-permissions.md#users_change_permissions-add-console") in the _IAM User Guide_.

###### To grant SELECT permissions on the table to query in the Lake Formation database

1.  Open the Lake Formation console at [https://console.aws.amazon.com/lakeformation/](https://console.aws.amazon.com/lakeformation/ "https://console.aws.amazon.com/lakeformation/").
2.  In the navigation pane, choose **Data lake permissions**, and then choose
    **Grant**.
3.  Follow the instructions in [Granting table permissions using the named resource method](../../../lake-formation/latest/dg/granting-table-permissions.md "../../../lake-formation/latest/dg/granting-table-permissions.md") in the
    _AWS Lake Formation Developer Guide_.
    Provide the following information:
    - For **IAM role**, choose the IAM role you created,
      `myspectrum_role`. When you run the Amazon Redshift Query Editor, it
      uses this IAM role for permission to the data.

    ###### Note

    To grant SELECT permission on the table in a Lake Formation–enabled Data Catalog to query, do the
    following:

        + Register the path for the data in Lake Formation.
        + Grant users permission to that path in Lake Formation.
        + Created tables can be found in the path registered in Lake Formation.

4.  Choose **Grant**.

###### Important

As a best practice, allow access only to the underlying Amazon S3 objects through Lake Formation permissions.
To prevent unapproved access, remove any permission granted to Amazon S3 objects
outside of Lake Formation. If you previously accessed Amazon S3 objects before setting up
Lake Formation, remove any IAM policies or bucket permissions that previously were set up.
For more information, see
[Upgrading AWS Glue Data Permissions to the AWS Lake Formation Model](../../../lake-formation/latest/dg/upgrade-glue-lake-formation.md "../../../lake-formation/latest/dg/upgrade-glue-lake-formation.md") and [Lake Formation Permissions](../../../lake-formation/latest/dg/lake-formation-permissions.md "../../../lake-formation/latest/dg/lake-formation-permissions.md").

## Step 2: Associate the IAM

role with your cluster

Now you have an IAM role that authorizes Amazon Redshift to access the external Data Catalog and
Amazon S3 for you. At this point, you must associate that role with your Amazon Redshift cluster.

###### To associate an IAM role with a cluster

1. Sign in to the AWS Management Console and open the Amazon Redshift console at
   [https://console.aws.amazon.com/redshiftv2/](https://console.aws.amazon.com/redshiftv2/ "https://console.aws.amazon.com/redshiftv2/").
2. On the navigation menu, choose **Clusters**, then choose
   the name of the cluster that you want to update.
3. For **Actions**, choose **Manage IAM
   roles**. The **IAM roles** page appears.
4. Either choose **Enter ARN** and then enter an ARN or an IAM role, or choose an IAM role from the list.
   Then choose **Add IAM role** to add it to the list of **Attached IAM roles**.
5. Choose **Done** to associate the IAM role with the cluster.
   The cluster is modified to complete the change.

## Step 3: Create

an external schema and an external table

Create external tables in an external schema. The external schema references a
database in the external data catalog and provides the IAM role ARN that authorizes your
cluster to access Amazon S3 on your behalf. You can create an external database in an
Amazon Athena Data Catalog, AWS Glue Data Catalog, or an Apache Hive metastore, such as Amazon EMR. For
this example, you create the external database in an Amazon Athena Data Catalog when you
create the external schema Amazon Redshift. For more information, see [External schemas in Amazon Redshift
Spectrum](c-spectrum-external-schemas.md "c-spectrum-external-schemas.md").

###### To create an external

schema and an external table

1. To create an external schema, replace the IAM role ARN in the following command
   with the role ARN you created in [step 1](#c-getting-started-using-spectrum-create-role "#c-getting-started-using-spectrum-create-role"). Then run
   the command in your SQL client.

```
create external schema myspectrum_schema
from data catalog
database 'myspectrum_db'
iam_role 'arn:aws:iam::123456789012:role/myspectrum_role'
create external database if not exists;
```

2. To create an external table, run the following CREATE EXTERNAL TABLE
   command.

###### Note

Your cluster and the Amazon S3 bucket must be in the same AWS Region.
For this example CREATE EXTERNAL TABLE command,
the Amazon S3 bucket with the sample data is located in the US East (N. Virginia) AWS Region.
To see the source data, download the
[`sales_ts.000` file](https://s3.amazonaws.com/redshift-downloads/tickit/spectrum/sales/sales_ts.000 "https://s3.amazonaws.com/redshift-downloads/tickit/spectrum/sales/sales_ts.000").

You can modify this example to run in a different AWS Region.
Create an Amazon S3 bucket in your desired AWS Region.
Copy the sales data with an Amazon S3 copy command.
Then update the location option in the example `CREATE EXTERNAL TABLE` command to your bucket.

```
aws s3 cp s3://redshift-downloads/tickit/spectrum/sales/ s3://`bucket-name`/tickit/spectrum/sales/ --copy-props none --recursive
```

The output of the Amazon S3 copy command confirms that the file was copied to the `bucket-name` in your desired AWS Region.

```
copy: s3://redshift-downloads/tickit/spectrum/sales/sales_ts.000 to s3://`bucket-name`/tickit/spectrum/sales/sales_ts.000
```

```
create external table myspectrum_schema.sales(
salesid integer,
listid integer,
sellerid integer,
buyerid integer,
eventid integer,
dateid smallint,
qtysold smallint,
pricepaid decimal(8,2),
commission decimal(8,2),
saletime timestamp)
row format delimited
fields terminated by '\t'
stored as textfile
location 's3://redshift-downloads/tickit/spectrum/sales/'
table properties ('numRows'='172000');
```

## Step 4: Query your data

in Amazon S3

After your external tables are created, you can query them using the same SELECT
statements that you use to query other Amazon Redshift tables. These SELECT statement queries
include joining tables, aggregating data, and filtering on predicates.

###### To query your data in Amazon S3

1. Get the number of rows in the MYSPECTRUM_SCHEMA.SALES table.

```
select count(*) from myspectrum_schema.sales;
```

```
count
------
172462
```

2. Keep your larger fact tables in Amazon S3 and your smaller dimension tables in Amazon Redshift,
   as a best practice. If you loaded the sample data in [Load data](../gsg/cm-dev-t-load-sample-data.md "../gsg/cm-dev-t-load-sample-data.md"), you
   have a table named EVENT in your database. If not, create the EVENT table by using
   the following command.

```
create table event(
eventid integer not null distkey,
venueid smallint not null,
catid smallint not null,
dateid smallint not null sortkey,
eventname varchar(200),
starttime timestamp);
```

3. Load the EVENT table by replacing the IAM role ARN in the following COPY
   command with the role ARN you created in [Step 1. Create an IAM
   role for Amazon Redshift](#c-getting-started-using-spectrum-create-role "#c-getting-started-using-spectrum-create-role").
   You can optionally download and view the
   [source data for the `allevents_pipe.txt`](https://s3.amazonaws.com/redshift-downloads/tickit/allevents_pipe.txt "https://s3.amazonaws.com/redshift-downloads/tickit/allevents_pipe.txt")
   from an Amazon S3 bucket in AWS Region `us-east-1`.

```
copy event from 's3://redshift-downloads/tickit/allevents_pipe.txt'
iam_role 'arn:aws:iam::123456789012:role/myspectrum_role'
delimiter '|' timeformat 'YYYY-MM-DD HH:MI:SS' region 'us-east-1';
```

The following example joins the external Amazon S3 table MYSPECTRUM_SCHEMA.SALES with the local
Amazon Redshift table EVENT to find the total sales for the top 10 events.

```
select top 10 myspectrum_schema.sales.eventid, sum(myspectrum_schema.sales.pricepaid) from myspectrum_schema.sales, event
where myspectrum_schema.sales.eventid = event.eventid
and myspectrum_schema.sales.pricepaid > 30
group by myspectrum_schema.sales.eventid
order by 2 desc;
```

```
eventid | sum
--------+---------
    289 | 51846.00
   7895 | 51049.00
   1602 | 50301.00
    851 | 49956.00
   7315 | 49823.00
   6471 | 47997.00
   2118 | 47863.00
    984 | 46780.00
   7851 | 46661.00
   5638 | 46280.00
```

4. View the query plan for the previous query. Notice the `S3 Seq Scan`,
   `S3 HashAggregate`, and `S3 Query Scan` steps that were
   run against the data on Amazon S3.

```
explain
select top 10 myspectrum_schema.sales.eventid, sum(myspectrum_schema.sales.pricepaid)
from myspectrum_schema.sales, event
where myspectrum_schema.sales.eventid = event.eventid
and myspectrum_schema.sales.pricepaid > 30
group by myspectrum_schema.sales.eventid
order by 2 desc;
```

```

QUERY PLAN
-----------------------------------------------------------------------------
XN Limit  (cost=1001055770628.63..1001055770628.65 rows=10 width=31)
  ->  XN Merge  (cost=1001055770628.63..1001055770629.13 rows=200 width=31)
        Merge Key: sum(sales.derived_col2)
        ->  XN Network  (cost=1001055770628.63..1001055770629.13 rows=200 width=31)
              Send to leader
              ->  XN Sort  (cost=1001055770628.63..1001055770629.13 rows=200 width=31)
                    Sort Key: sum(sales.derived_col2)
                    ->  XN HashAggregate  (cost=1055770620.49..1055770620.99 rows=200 width=31)
                          ->  XN Hash Join DS_BCAST_INNER  (cost=3119.97..1055769620.49 rows=200000 width=31)
                                Hash Cond: ("outer".derived_col1 = "inner".eventid)
                                ->  XN S3 Query Scan sales  (cost=3010.00..5010.50 rows=200000 width=31)
                                      ->  S3 HashAggregate  (cost=3010.00..3010.50 rows=200000 width=16)
                                            ->  S3 Seq Scan myspectrum_schema.sales location:"s3://redshift-downloads/tickit/spectrum/sales" format:TEXT  (cost=0.00..2150.00 rows=172000 width=16)
                                                  Filter: (pricepaid > 30.00)
                                ->  XN Hash  (cost=87.98..87.98 rows=8798 width=4)
                                      ->  XN Seq Scan on event  (cost=0.00..87.98 rows=8798 width=4)
```

## Launch your AWS CloudFormation stack and then query your data in Amazon S3

After you create an Amazon Redshift cluster and connect to the cluster, you can install your
Redshift Spectrum DataLake AWS CloudFormation template and then query your data.

CloudFormation installs the Redshift Spectrum Getting Started DataLake template and creates a stack that includes the following:

- A role named `myspectrum_role` associated with your Redshift cluster
- An external schema named `myspectrum_schema`
- An external table named `sales` in an Amazon S3 bucket
- A Redshift table named `event` loaded with data

###### To launch your Redshift Spectrum Getting Started DataLake CloudFormation stack

1. Choose [**Launch CFN stack**](cloudformation/home.md#/stacks/new?stackName=DataLake&templateURL=https://s3.amazonaws.com/redshift-downloads/docs-downloads/DataLake.yml "cloudformation/home.md#/stacks/new?stackName=DataLake&templateURL=https://s3.amazonaws.com/redshift-downloads/docs-downloads/DataLake.yml").
   The CloudFormation console opens with the DataLake.yml template selected.

You can also download and customize the Redshift Spectrum Getting Started DataLake
CloudFormation [CFN template](https://s3.amazonaws.com/redshift-downloads/docs-downloads/DataLake.yml "https://s3.amazonaws.com/redshift-downloads/docs-downloads/DataLake.yml"), then open CloudFormation console ([https://console.aws.amazon.com/cloudformation](https://console.aws.amazon.com/cloudformation/ "https://console.aws.amazon.com/cloudformation/")) and
create a stack with the customized template. 2. Choose **Next**. 3. Under **Parameters**, enter the Amazon Redshift cluster name, database name, and your database user name. 4. Choose **Next**.

The stack options appear. 5. Choose **Next** to accept the default settings. 6. Review the information and under **Capabilities**, and choose **I
acknowledge that AWS CloudFormation might create IAM
resources**. 7. Choose **Create stack**.

If an error occurs while the stack is being created, see the following
information:

- View the CloudFormation **Events** tab for information that can help you resolve the error.
- Delete the DataLake CloudFormation stack before trying the operation again.
- Make sure that you are connected to your Amazon Redshift database.
- Make sure that you entered the correct information for the Amazon Redshift cluster name, database name, and database user name.

### Query your data in Amazon S3

You query external tables using the same SELECT
statements that you use to query other Amazon Redshift tables. These SELECT statement queries
include joining tables, aggregating data, and filtering on predicates.

The following query returns the number of rows in the `myspectrum_schema.sales` external table.

```
select count(*) from myspectrum_schema.sales;
```

```
count
------
172462
```

### Join an external table with a local table

The following example joins the external table `myspectrum_schema.sales` with the local table `event` to find the total sales for the top 10 events.

```
select top 10 myspectrum_schema.sales.eventid, sum(myspectrum_schema.sales.pricepaid) from myspectrum_schema.sales, event
where myspectrum_schema.sales.eventid = event.eventid
and myspectrum_schema.sales.pricepaid > 30
group by myspectrum_schema.sales.eventid
order by 2 desc;
```

```
eventid | sum
--------+---------
    289 | 51846.00
   7895 | 51049.00
   1602 | 50301.00
    851 | 49956.00
   7315 | 49823.00
   6471 | 47997.00
   2118 | 47863.00
    984 | 46780.00
   7851 | 46661.00
   5638 | 46280.00
```

### View the query

plan

View the query plan for the previous query. Note the `S3 Seq Scan`,
`S3 HashAggregate`, and `S3 Query Scan` steps that were run
on the data on Amazon S3.

```
explain
select top 10 myspectrum_schema.sales.eventid, sum(myspectrum_schema.sales.pricepaid)
from myspectrum_schema.sales, event
where myspectrum_schema.sales.eventid = event.eventid
and myspectrum_schema.sales.pricepaid > 30
group by myspectrum_schema.sales.eventid
order by 2 desc;
```

```

QUERY PLAN
-----------------------------------------------------------------------------
XN Limit  (cost=1001055770628.63..1001055770628.65 rows=10 width=31)
  ->  XN Merge  (cost=1001055770628.63..1001055770629.13 rows=200 width=31)
        Merge Key: sum(sales.derived_col2)
        ->  XN Network  (cost=1001055770628.63..1001055770629.13 rows=200 width=31)
              Send to leader
              ->  XN Sort  (cost=1001055770628.63..1001055770629.13 rows=200 width=31)
                    Sort Key: sum(sales.derived_col2)
                    ->  XN HashAggregate  (cost=1055770620.49..1055770620.99 rows=200 width=31)
                          ->  XN Hash Join DS_BCAST_INNER  (cost=3119.97..1055769620.49 rows=200000 width=31)
                                Hash Cond: ("outer".derived_col1 = "inner".eventid)
                                ->  XN S3 Query Scan sales  (cost=3010.00..5010.50 rows=200000 width=31)
                                      ->  S3 HashAggregate  (cost=3010.00..3010.50 rows=200000 width=16)
                                            ->  S3 Seq Scan spectrum.sales location:"s3://redshift-downloads/tickit/spectrum/sales" format:TEXT  (cost=0.00..2150.00 rows=172000 width=16)
                                                  Filter: (pricepaid > 30.00)
                                ->  XN Hash  (cost=87.98..87.98 rows=8798 width=4)
                                      ->  XN Seq Scan on event  (cost=0.00..87.98 rows=8798 width=4)
```
