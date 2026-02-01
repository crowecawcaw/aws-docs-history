Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Creating a datashare in Amazon Redshift

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
   see Creating a datashare in Amazon Redshift.
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
