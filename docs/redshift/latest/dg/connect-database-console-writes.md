Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Connecting to a database in

Amazon Redshift

With Amazon Redshift, you can establish a connection to your data warehouse cluster and
execute SQL queries, load data, or perform administrative tasks. Connecting to a
database refers to the process of creating a secure channel between a client
application or tool and the Amazon Redshift cluster. The following sections provide step-by-step
instructions on how to connect to an Amazon Redshift database.

Console
Connect to a database to view databases and objects within databases or
to view datashares in the Amazon Redshift data warehouse. The user credentials used to
connect to a specified database must have the necessary permissions to view
all datashares.

If there is no local connection, do one of the following:

- If you are a producer administrator, go to the
  **Clusters** tab for provisioned clusters, or the
  **Namespaces configuration** tab for Serverless
  endpoints. Select the respective cluster or namespace from the list.
- In the cluster or namespace details page, from the
  **Datashares** tab, choose **Connect to
  database** and do one of the following:
  - In the **Datashares from other namespaces and
    AWS accounts** section, view datashares from other
    clusters, namespaces, or accounts.
  - In the **Datashares created in my cluster**
    section, view datashares in your cluster.

- On the **Connect to database** window, do one of
  the following:
  - If you choose **Create a new connection**,
    choose **AWS Secrets Manager** to use a stored
    secret to authenticate access for the connection.

  Or, choose **Temporary credentials** to use
  database credentials to authenticate access for the connection.
  Specify values for **Database name** and
  **Database user**.

  Choose **Connect**.
  - Choose **Use a recent connection** to
    connect to another database that you have the necessary
    permissions.

  Amazon Redshift automatically makes the connection.

After a database connection is established, you can start creating
datashares, querying datashares, or creating databases from
datashares.
