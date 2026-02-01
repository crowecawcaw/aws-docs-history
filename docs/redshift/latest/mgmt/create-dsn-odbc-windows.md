Amazon Redshift will no longer support the creation of new Python UDFs starting Patch 198.
Existing Python UDFs will continue to function until June 30, 2026. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Creating a system DSN entry for an ODBC

connection

After you download and install the ODBC driver, add a data source name
(DSN) entry to the client computer or Amazon EC2 instance. SQL client tools use
this data source to connect to the Amazon Redshift database.

We recommend that you create a system DSN instead of a user DSN. Some
applications load the data using a different user account. These
applications might not be able to detect user DSNs that are created under
another user account.

###### Note

For authentication using AWS Identity and Access Management (IAM) credentials or identity
provider (IdP) credentials, additional steps are required. For more
information, see [Step
5: Configure a JDBC or ODBC connection to use IAM credentials](generating-iam-credentials-steps.md#generating-iam-credentials-configure-jdbc-odbc "generating-iam-credentials-steps.md#generating-iam-credentials-configure-jdbc-odbc").

For information about how to create a system DSN entry, see the
[Amazon Redshift ODBC connector installation and configuration guide](https://s3.amazonaws.com/redshift-downloads/drivers/odbc/1.6.1.1000/Amazon+Redshift+ODBC+Connector+Install+Guide.pdf "https://s3.amazonaws.com/redshift-downloads/drivers/odbc/1.6.1.1000/Amazon+Redshift+ODBC+Connector+Install+Guide.pdf").

###### To create a system DSN entry for an ODBC connection on

Windows

1. In the **Start** menu, open **ODBC Data
   Sources**.

Make sure that you choose the ODBC Data Source Administrator that
has the same bitness as the client application that you are using to
connect to Amazon Redshift. 2. In the **ODBC Data Source Administrator**, choose
the **Driver** tab and locate the driver
folder:

    * **Amazon Redshift ODBC Driver (64-bit)**
    * **Amazon Redshift ODBC Driver (32-bit)**

3. Choose the **System DSN** tab to configure the
   driver for all users on the computer, or the **User
   DSN** tab to configure the driver for your user account
   only.
4. Choose **Add**. The **Create New Data
   Source** window opens.
5. Choose the **Amazon Redshift** ODBC driver, and then
   choose **Finish**. The **Amazon Redshift ODBC
   Driver DSN Setup** window opens.
6. Under **Connection Settings**, enter the
   following information:

###### Data source name

Enter a name for the data source. You can use any name that
you want to identify the data source later when you create the
connection to the cluster. For example, if you followed the
_Amazon Redshift Getting Started Guide_, you might type
`exampleclusterdsn` to make it easy to remember
the cluster that you associate with this DSN.

###### Server

Specify the endpoint for your Amazon Redshift cluster. You can find
this information in the Amazon Redshift console on the cluster's
details page. For more information, see [Configuring connections in Amazon Redshift](configuring-connections.md "configuring-connections.md").

###### Port

Enter the port number that the database uses.
Use the port that
the cluster was configured to use when it was launched or
modified.

###### Database

Enter the name of the Amazon Redshift database. If you launched your
cluster without specifying a database name, enter
`dev`. Otherwise,
use the name that you chose during the launch process. If you
followed the _Amazon Redshift Getting Started Guide_, enter
`dev`. 7. Under **Authentication**, specify the
configuration options to configure standard or IAM authentication.
For information about authentication options, see "Configuring
Authentication on Windows" in _Amazon Redshift ODBC Connector
Installation and Configuration Guide_. 8. Under **SSL Settings**, specify a value for the
following:

###### SSL

authentication

Choose a mode for handling Secure Sockets Layer (SSL). In a
test environment, you might use `prefer`. However,
for production environments and when secure data exchange is
required, use `verify-ca` or
`verify-full`. For more information about using SSL
on Windows, see "Configuring SSL Verification on Windows" in
_Amazon Redshift ODBC Connector Installation and
Configuration Guide_. 9. Under **Additional Options**, specify options on
how to return query results to your SQL client tool or application.
For more information, see "Configuring Additional Options on
Windows" in _Amazon Redshift ODBC Connector Installation and
Configuration Guide_. 10. In **Logging Options**, specify values for the
logging option. For more information, see "Configuring Logging
Options on Windows" in _Amazon Redshift ODBC Connector
Installation and Configuration Guide_.

Then choose **OK**. 11. Under **Data Type Options**, specify values for
data types. For more information, see "Configuring Data Type Options
on Windows" in _Amazon Redshift ODBC Connector Installation and
Configuration Guide_.

Then choose **OK**. 12. Choose **Test**. If the client computer can
connect to the Amazon Redshift database, you see the following message:
**Connection successful**.

If the client computer fails to connect to the database, you can
troubleshoot possible issues. For more information, see [Troubleshooting connection issues in
Amazon Redshift](troubleshooting-connections.md "troubleshooting-connections.md"). 13. Configure TCP keepalives on Windows to prevent connections from
timing out. For information about how to configure TCP keepalives on
Windows, see _Amazon Redshift ODBC Connector Installation and
Configuration Guide_. 14. To help troubleshooting, configure logging. For information about
how to configure logging on Windows, see _Amazon Redshift ODBC
Connector Installation and Configuration Guide_.
