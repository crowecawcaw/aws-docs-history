

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# Downloading and installing the Amazon Redshift ODBC driver
<a name="odbc-driver-windows-how-to-install"></a>

Use the following procedure to download the Amazon Redshift ODBC drivers for Windows operating systems. Only use a driver other than these if you're running a third-party application that is certified for use with Amazon Redshift and that requires a specific driver. 

**To install the ODBC driver**

1. Download one of the following, depending on the system architecture of your SQL client tool or application: 
   + [64-bit ODBC driver version 1.6.3](https://s3.amazonaws.com/redshift-downloads/drivers/odbc/1.6.3.1008/AmazonRedshiftODBC64-1.6.3.1008.msi) 

     The name for this driver is Amazon Redshift (x64).
   + [32-bit ODBC driver version 1.4.52](https://s3.amazonaws.com/redshift-downloads/drivers/odbc/1.4.52.1000/AmazonRedshiftODBC32-1.4.52.1000.msi) 

     The name for this driver is Amazon Redshift (x86). The 32-bit ODBC drivers are discontinued. Further updates will not be released, except for urgent security patches.
**Note**  
Download the MSI package that corresponds to the system architecture of your SQL client tool or application. For example, if your SQL client tool is 64-bit, install the 64-bit driver.

    Then download and review the [Amazon Redshift ODBC and JDBC driver license agreement](https://s3.amazonaws.com/redshift-downloads/drivers/Amazon+Redshift+ODBC+and+JDBC+Driver+License+Agreement.pdf). 

1.  Double-click the .msi file, and then follow the steps in the wizard to install the driver. 