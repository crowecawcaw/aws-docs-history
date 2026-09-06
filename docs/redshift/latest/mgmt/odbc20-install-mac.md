

 Amazon Redshift will no longer support the use of Python UDFs after June 30, 2026. We will start enforcing it in phases. For more information on the details of Python end of life and migration options, see the [ blog post ](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/) that was published on June 30, 2025. 

# Downloading and installing the Amazon Redshift ODBC driver
<a name="odbc20-install-mac"></a>

Use the following procedure to download and install the Amazon Redshift ODBC driver on Apple macOS. Only use a different driver if you're running a third-party application that is certified for use with Amazon Redshift, and that application requires that specific driver.

To download and install the ODBC driver: 

1. Download the following driver: [64-bit ODBC driver version 2.2.2.0](https://s3.amazonaws.com/redshift-downloads/drivers/odbc/2.2.2.0/AmazonRedshiftODBC-64-bit.2.2.2.0.universal.pkg) 

   This driver is supported on both x86\_64 and arm64 architectures. The name for this driver is **Amazon Redshift ODBC Driver (x64)**.

1. Review the [ Amazon Redshift ODBC driver version 2.x license](https://github.com/aws/amazon-redshift-odbc-driver/blob/master/LICENSE).

1. Double-click the .pkg file, then follow the steps in the wizard to install the driver. Alternatively, run the following command:

   ```
   sudo installer -pkg {{PKGFileName}} -target /
   ```

   Replace `PKGFileName` with the pkg package file name. For example, the following command demonstrates installing the 64-bit driver:

   ```
   sudo installer -pkg ./AmazonRedshiftODBC-64-bit.X.X.XX.X.universal.pkg -target /
   ```