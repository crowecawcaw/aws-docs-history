Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Connecting to a database

With Amazon Redshift, you can establish a connection to your data warehouse cluster and
execute SQL queries, load data, or perform administrative tasks. Connecting to a
database refers to the process of creating a secure channel between a client
application or tool and the Amazon Redshift cluster. The following sections will provide
step-by-step instructions on how to connect to an Amazon Redshift database.

Connect to a database to view databases and objects within databases in this
cluster or to view datashares.

The user credentials used to connect to a specified database must have the
necessary permissions to view all datashares.

If there is no local connection, do one of the following:

- In the cluster details page, from the **Databases** tab, in
  the **Databases** or **Datashare objects**
  section, choose **Connect to database** to view database
  objects in the cluster.
- In the cluster details page, from the **Datashares** tab,
  do one of the following:
  - In the **Datashares from other clusters** section,
    choose **Connect to database** to view datashares from
    other clusters.
  - In the **Datashares created in my cluster** section,
    choose **Connect to database** to view datashares in
    your cluster.

- On the **Connect to database** window, do one of the
  following:

      + If you choose **Create a new connection**, choose
       **AWS Secrets Manager** to use a stored secret to
       authenticate access for the connection.


      Or, choose **Temporary credentials** to use database
       credentials to authenticate access for the connection. Specify values for
       **Database name** and **Database
       user**.


      Choose **Connect**.
      + Choose **Use a recent connection** to connect to
       another database that you have the necessary permissions.


      Amazon Redshift automatically makes the connection.

  After a database connection is established, you can start creating datashares,
  querying datashares, or creating databases from datashares.
