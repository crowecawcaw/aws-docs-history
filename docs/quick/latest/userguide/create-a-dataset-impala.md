# Creating a dataset using an Apache Impala data

source

Apache Impala is a high-performance massively parallel processing (MPP) SQL query
engine designed to run natively on Apache Hadoop. Use the procedure below to establish a
secure connection between Quick Sight and Apache Impala.

All traffic between Quick Sight and Apache Impala is encrypted using SSL.
Quick Sight supports standard username and password authentication for Impala
connections.

To establish a connection, you'll need to configure SSL settings in your Impala
instance, prepare your authentication credentials, set up the connection in Quick Sight
using your Impala server details, and validate the connection to ensure secure data
access.

###### To create a dataset using an Apache Impala data source

1. On the Quick start page, choose **Data**.
2. On the **Data** page, choose
   **Create**.
3. Choose **Data source**.
4. Choose **Impala**, then choose
   **Next**.
5. Enter a name for the data source.
6. For public connections:
   1. Enter connection details for **Database server**,
      **HTTP Path**, **Port**,
      **Username**, and
      **Password**.
   2. Once the validation is successful, choose **Create data
      source**.

7. For private connections:
   1. Coordinate with your administrator to set up a VPC connection before
      entering connection details.

   You or your administrator can [configure the VPC
   connection in Quick](vpc-creating-a-connection-in-quicksight.md "vpc-creating-a-connection-in-quicksight.md"). SSL is enabled by default to ensure
   secure data transmission. If you encounter connection validation errors,
   please verify your connection and VPC details.

   If issues persist, consult your administrator to confirm that your
   Certificate Authority is included in Quick Sight's [approved list of
   certificates](configure-access.md#ca-certificates "configure-access.md#ca-certificates").

8. In the **Choose your table** menu, you can either:
   1. Choose a specific schema or table, then choose
      **Select**.
   2. Choose **Use custom SQL** to write your own SQL
      query.

9. After completing your selection, you will be redirected to the data
   preparation page. Make any adjustments to your data, then choose
   **Publish & visualize** to analyze your Impala data in
   Quick Sight.

###### Note

This connector supports:

- Username and password authentication
- Public and private connections
- Table discovery and custom SQL queries
- Full data refresh during ingestion
- SPICE storage only
