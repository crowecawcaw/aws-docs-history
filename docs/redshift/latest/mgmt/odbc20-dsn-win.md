Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Creating a system DSN entry for an ODBC

connection

After you download and install the ODBC driver, add a data source name (DSN) entry
to the client computer or Amazon EC2 instance. SQL client tools can use this data source
to connect to the Amazon Redshift database.

We recommend that you create a system DSN instead of a user DSN. Some applications
load the data using a different database user account, and might not be able to
detect user DSNs that are created under another database user account.

###### Note

For authentication using AWS Identity and Access Management (IAM) credentials or identity provider
(IdP) credentials, additional steps are required. For more information, see
[Configure a JDBC or ODBC connection to use IAM
credentials](generating-iam-credentials-configure-jdbc-odbc.md "generating-iam-credentials-configure-jdbc-odbc.md").

To create a system DSN entry for an ODBC connection:

1. In the **Start** menu, type "ODBC Data Sources." Choose
   **ODBC Data Sources**.

Make sure that you choose the ODBC Data Source Administrator that has the
same bitness as the client application that you are using to connect to
Amazon Redshift. 2. In the **ODBC Data Source Administrator**, choose the
**Driver** tab and locate the following driver folder:
**Amazon Redshift ODBC Driver (x64)**. 3. Choose the **System DSN** tab to configure the driver for
all users on the computer, or the **User DSN** tab to
configure the driver for your database user account only. 4. Choose **Add**. The **Create New Data
Source** window opens. 5. Choose the **Amazon Redshift ODBC driver (x64)**, and then
choose **Finish**. The **Amazon Redshift ODBC Driver DSN
Setup** window opens. 6. Under the **Connection Settings** section, enter the
following information:

    * ###### Data source name


     Enter a name for the data source. For example, if you
     followed the *Amazon Redshift Getting Started
     Guide*, you might type `exampleclusterdsn`
     to make it easy to remember the cluster that you associate with
     this DSN.
    * ###### Server


     Specify the endpoint host for your Amazon Redshift cluster. You can
     find this information in the Amazon Redshift console on the cluster's
     details page. For more information, see [Configuring connections in Amazon Redshift](configuring-connections.md "configuring-connections.md") .
    * ###### Port


     Enter the port number that the database uses. Depending on
     the port you selected when creating, modifying or migrating the
     cluster, allow access to the selected port.
    * ###### Database


     Enter the name of the Amazon Redshift database. If you launched your
     cluster without specifying a database name, enter
     `dev`. Otherwise, use the name that you chose
     during the launch process. If you followed the
     *Amazon Redshift Getting Started Guide*, enter
     `dev`.

7. Under the **Authentication** section, specify the
   configuration options to configure standard or IAM authentication.
8. Choose **SSL Options** and specify a value for the
   following:
   - ###### Authentication mode

   Choose a mode for handling Secure Sockets Layer (SSL). In a
   test environment, you might use `prefer`. However,
   for production environments and when secure data exchange is
   required, use `verify-ca` or
   `verify-full`.
   - ###### Min TLS

   Optionally, choose the minimum version of TLS/SSL that the
   driver allows the data store to use for encrypting connections.
   For example, if you specify TLS 1.2, TLS 1.1 can't be used to
   encrypt connections. The default version is TLS 1.2.

9. In the **Proxy** tab, specify any proxy connection
   setting.
10. In the **Cursor** tab, specify options on how to return
    query results to your SQL client tool or application.
11. In **Advanced Options**, specify values for
    `logLevel`, `logPath`, `compression`,
    and other options.
12. Choose **Test**. If the client computer can connect to
    the Amazon Redshift database, the following message appears: **Connection
    successful**. If the client computer fails to connect to the
    database, you can troubleshoot possible issues by generating a log file and
    contacting AWS support. For information on generating logs, see (LINK).
13. Choose **OK**.
