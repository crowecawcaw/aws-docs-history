

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# Querying datashares
<a name="query-datashare-console"></a>

With Amazon Redshift, you can query data across datashares from producer clusters to securely access live data without copying or transferring it. The following sections cover the details of setting up and querying datashares in your Amazon Redshift environment.

## Creating databases from datashares
<a name="create-database-from-datashare-console"></a>

To start querying data in the datashare, create a database from a datashare. You can create only one database from a specified datashare.

1. Sign in to the AWS Management Console and open the Amazon Redshift console at [https://console.aws.amazon.com/redshiftv2/](https://console.aws.amazon.com/redshiftv2/).

1. On the navigation menu, choose **Clusters**, then choose your cluster. The cluster details page appears.

1. Choose **Datashares**. The datashare list appears.

1. In the **Datashares from other clusters** section, choose **Connect to database**. For more information, see [Connecting to a database](connect-database-console.md).

1. Choose a datashare that you want to create databases from, then choose **Create database from datashare**. The Create database from datashare page appears.

1. In the **Database name**, specify a database name. The database name must be 1–64 alphanumeric characters (lowercase only) and it can't be a reserved word.

1. Choose **Create**.

After the database is created, you can query data in the database.