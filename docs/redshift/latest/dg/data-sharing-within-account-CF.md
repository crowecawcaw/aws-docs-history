Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Getting started with data sharing with

AWS CloudFormation in Amazon Redshift

You can automate data sharing setup by using an AWS CloudFormation stack, which provisions
AWS resources. The CloudFormation stack sets up data sharing between two Amazon Redshift clusters in
the same AWS account. Thus, you can start data sharing without running SQL statements
to provision your resources.

The stack creates a datashare on the cluster that you designate. The datashare
includes a table and sample read-only data. This data can be read by your other Amazon Redshift
cluster.

If you want to start sharing data in an AWS account by running SQL statements to
set up a datashare and grant permissions, without using CloudFormation, see [Sharing read access to data within an
AWS account](within-account.md "within-account.md").

Before running the data sharing CloudFormation stack, you must be logged in with a user
that has permission to create an IAM role and a Lambda function. You also need two Amazon Redshift
clusters in the same account. You use one, the _producer_, to share the sample data, and the other, the _consumer_, to read it. The primary requirement for these
clusters is that each use RA3 nodes. For additional requirements, see [Considerations for data sharing in
Amazon Redshift](datashare-considerations.md "datashare-considerations.md").

For more information about getting started setting up an Amazon Redshift cluster, see [Get started with Amazon Redshift provisioned data
warehouses](../gsg/new-user.md "../gsg/new-user.md"). For more information about automating setup with CloudFormation, see
[What is AWS CloudFormation?](../../../AWSCloudFormation/latest/UserGuide/Welcome.md "../../../AWSCloudFormation/latest/UserGuide/Welcome.md")

###### Important

Before launching your CloudFormation stack, make sure you have two Amazon Redshift
clusters in the same account and that the clusters use RA3 nodes. Make sure each
cluster has a database and a superuser. For more information, see [CREATE DATABASE](r_CREATE_DATABASE.md "r_CREATE_DATABASE.md") and [superuser](r_superusers.md "r_superusers.md").

###### To launch your CloudFormation stack for Amazon Redshift data sharing:

1. Click [**Launch CFN stack**](https://console.aws.amazon.com/cloudformation/home?#/stacks/new?stackName=DataShare&templateURL=https://s3.amazonaws.com/redshift-downloads/docs-downloads/DataShare.yml "https://console.aws.amazon.com/cloudformation/home?#/stacks/new?stackName=DataShare&templateURL=https://s3.amazonaws.com/redshift-downloads/docs-downloads/DataShare.yml"), which takes you to the
   CloudFormation service in the AWS Management Console.

If you are prompted, sign in.

The stack creation process starts, referencing a CloudFormation template file,
which is stored in Amazon S3. A CloudFormation _template_ is a text file in JSON format that declares AWS
resources that make up a stack. For more information about CloudFormation
templates, see [Learn template basics](../../../AWSCloudFormation/latest/UserGuide/gettingstarted.md "../../../AWSCloudFormation/latest/UserGuide/gettingstarted.md"). 2. Choose **Next** to enter the stack details. 3. Under **Parameters**, for each cluster, enter the
following:

    * Your Amazon Redshift cluster name, for example
     `ra3-consumer-cluster`
    * Your database name, for example `dev`
    * The name of your database user, for example
     `consumeruser`

We recommend using test clusters, because the stack creates several database
objects.

Choose **Next**. 4. The stack options appear.

Choose **Next** to accept the default settings. 5. Under **Capabilities**, choose **I acknowledge that
AWS CloudFormation might create IAM resources.** 6. Choose **Create stack**.
CloudFormation takes about 10 minutes to build the Amazon Redshift stack using the template,
creating a datashare called `myproducer_share`. The stack creates the
datashare in the database specified in the stack details. Only objects from that
database can be shared.

If an error occurs while the stack is created, do the following:

- Make sure that you entered the correct cluster name, database name, and
  database user name for each Redshift cluster.
- Make sure that your cluster has RA3 nodes.
- Make sure you are logged in with a user that has permission to create an
  IAM role and a Lambda function. For more information about creating IAM
  roles, see [Creating IAM
  roles](../../../IAM/latest/UserGuide/id_roles_create.md "../../../IAM/latest/UserGuide/id_roles_create.md"). For more information about policies for Λ function
  creation, see [Function development](../../../lambda/latest/dg/access-control-identity-based.md#permissions-user-function "../../../lambda/latest/dg/access-control-identity-based.md#permissions-user-function").

## Querying the datashare that

you created

To use the following procedure, make sure that you have the required permissions
for running queries on each cluster described.

###### To query your datashare:

1. Connect to the producer cluster on the database entered when your CloudFormation
   stack was created, using a client tool such as the Amazon Redshift query editor v2.
2. Query for datashares.

```
`SHOW DATASHARES;`

`+------------------+-------------+-----------------+-------------------+------------+------------+---------------------+-----------+------------------+--------------------------------------+
| share_name | share_owner | source_database | consumer_database | share_type | createdate | is_publicaccessible | share_acl | producer_account | producer_namespace |
+------------------+-------------+-----------------+-------------------+------------+------------+---------------------+-----------+------------------+--------------------------------------+
| myproducer_share | 100 | sample_data_dev | myconsumer_db | INBOUND | NULL | true | NULL | `producer-acct` | `your-producer-namespace` |
+------------------+-------------+-----------------+-------------------+------------+------------+---------------------+-----------+------------------+--------------------------------------+`
```

The preceding command returns the name of the datashare created by the
stack, called `myproducer_share`. It also returns the name of the
database associated with the datashare, `myconsumer_db`.

Copy the producer namespace identifier to use in a later step. 3. Describe objects in the datashare.

```
`DESC DATASHARE myproducer_share;`

`+------------------+--------------------------------------+------------+------------------+-------------+-------------------------------------+-------------+
| producer_account | producer_namespace | share_type | share_name | object_type | object_name | include_new |
+------------------+--------------------------------------+------------+------------------+-------------+-------------------------------------+-------------+
| `producer-acct` | `your-producer-namespace` | OUTBOUND | myproducer_share | schema | myproducer_schema | true |
| `producer-acct` | `your-producer-namespace` | OUTBOUND | myproducer_share | table | myproducer_schema.tickit_sales | NULL |
| `producer-acct` | `your-producer-namespace` | OUTBOUND | myproducer_share | view | myproducer_schema.ticket_sales_view | NULL |
+------------------+--------------------------------------+------------+------------------+-------------+-------------------------------------+-------------+`
```

When you describe the datashare, it returns properties for tables and views.
The stack adds tables and views with sample data to the producer database, for
example `tickit_sales` and `tickit_sales_view`. For more
information about the TICKIT sample database, see [Sample database](c_sampledb.md "c_sampledb.md").

You don't have to delegate permissions on the datashare to run queries. The
stack grants the necessary permissions. 4. Connect to the consumer cluster using your client tool. Describe the
datashare, specifying the producer's namespace.

```
DESC DATASHARE myproducer_share OF NAMESPACE '<namespace id>'; --specify the unique identifier for the producer namespace

`+------------------+--------------------------------------+------------+------------------+-------------+-------------------------------------+-------------+
| producer_account | producer_namespace | share_type | share_name | object_type | object_name | include_new |
+------------------+--------------------------------------+------------+------------------+-------------+-------------------------------------+-------------+
| `producer-acct` | `your-producer-namespace` | INBOUND | myproducer_share | schema | myproducer_schema | NULL |
| `producer-acct` | `your-producer-namespace` | INBOUND | myproducer_share | table | myproducer_schema.tickit_sales | NULL |
| `producer-acct` | `your-producer-namespace` | INBOUND | myproducer_share | view | myproducer_schema.ticket_sales_view | NULL |
+------------------+--------------------------------------+------------+------------------+-------------+-------------------------------------+-------------+`
```

5. You can query tables in the datashare by specifying the datashare's database
   and schema. For more information, see [Cross-database query examples](cross-database_example.md "cross-database_example.md"). The following queries return sales
   and seller data from the SALES table in the TICKIT sample database. For more
   information, see [Sample database](c_sampledb.md "c_sampledb.md").

```
`SELECT * FROM myconsumer_db.myproducer_schema.tickit_sales_view;`

`+---------+--------+----------+---------+---------+--------+---------+-----------+------------+---------------------+
| salesid | listid | sellerid | buyerid | eventid | dateid | qtysold | pricepaid | commission | saletime |
+---------+--------+----------+---------+---------+--------+---------+-----------+------------+---------------------+
| 1 | 1 | 36861 | 21191 | 7872 | 1875 | 4 | 728 | 109.2 | 2008-02-18 02:36:48 |
| 2 | 4 | 8117 | 11498 | 4337 | 1983 | 2 | 76 | 11.4 | 2008-06-06 05:00:16 |
| 3 | 5 | 1616 | 17433 | 8647 | 1983 | 2 | 350 | 52.5 | 2008-06-06 08:26:17 |
| 4 | 5 | 1616 | 19715 | 8647 | 1986 | 1 | 175 | 26.25 | 2008-06-09 08:38:52 |
| 5 | 6 | 47402 | 14115 | 8240 | 2069 | 2 | 154 | 23.1 | 2008-08-31 09:17:02 |
+---------+--------+----------+---------+---------+--------+---------+-----------+------------+---------------------+`
```

###### Note

The query runs against the view in the shared schema. You can't connect
directly to databases created from datashares. They are read-only. 6. To run a query that includes aggregations, use the following example.

```
`SELECT * FROM myconsumer_db.myproducer_schema.tickit_sales ORDER BY 1,2 LIMIT 5;`

`+---------+--------+----------+---------+---------+--------+---------+-----------+------------+---------------------+
| salesid | listid | sellerid | buyerid | eventid | dateid | qtysold | pricepaid | commission | saletime |
+---------+--------+----------+---------+---------+--------+---------+-----------+------------+---------------------+
| 1 | 1 | 36861 | 21191 | 7872 | 1875 | 4 | 728 | 109.2 | 2008-02-18 02:36:48 |
| 2 | 4 | 8117 | 11498 | 4337 | 1983 | 2 | 76 | 11.4 | 2008-06-06 05:00:16 |
| 3 | 5 | 1616 | 17433 | 8647 | 1983 | 2 | 350 | 52.5 | 2008-06-06 08:26:17 |
| 4 | 5 | 1616 | 19715 | 8647 | 1986 | 1 | 175 | 26.25 | 2008-06-09 08:38:52 |
| 5 | 6 | 47402 | 14115 | 8240 | 2069 | 2 | 154 | 23.1 | 2008-08-31 09:17:02 |
+---------+--------+----------+---------+---------+--------+---------+-----------+------------+---------------------+`
```

The query returns sales and seller data from the sample TICKIT data.

For more examples of datashare queries, see [Sharing read access to data within an
AWS account](within-account.md "within-account.md").
