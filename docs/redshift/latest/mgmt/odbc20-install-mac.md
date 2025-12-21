Amazon Redshift will no longer support the creation of new Python UDFs starting November 1, 2025.
If you would like to use Python UDFs, create the UDFs prior to that date.
Existing Python UDFs will continue to function as normal. For more information, see the
[blog post](https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/ "https://aws.amazon.com/blogs/big-data/amazon-redshift-python-user-defined-functions-will-reach-end-of-support-after-june-30-2026/") .

# Downloading and installing the Amazon Redshift ODBC driver

Use the following procedure to download and install the Amazon Redshift ODBC driver on
Apple MacOS. Only use a different driver if you're running a
third-party application that is certified for use with Amazon Redshift, and that
application requires that specific driver.

To download and install the ODBC driver:

1. Download the following driver: [64-bit ODBC driver version 2.1.12.0](https://s3.amazonaws.com/redshift-downloads/drivers/odbc/2.1.12.0/AmazonRedshiftODBC-64-bit.2.1.12.0.universal.pkg "https://s3.amazonaws.com/redshift-downloads/drivers/odbc/2.1.12.0/AmazonRedshiftODBC-64-bit.2.1.12.0.universal.pkg")

This driver is supported on both x86_64 and arm64 architectures. The name for this driver is **Amazon Redshift ODBC Driver
(x64)**. 2. Review the [Amazon Redshift ODBC driver version 2.x license](https://github.com/aws/amazon-redshift-odbc-driver/blob/master/LICENSE "https://github.com/aws/amazon-redshift-odbc-driver/blob/master/LICENSE"). 3. Double-click the .pkg file, then follow the steps in the wizard to install
the driver. Alternatively, run the following command:

```
sudo installer -pkg `PKGFileName` -target /
```

Replace `PKGFileName` with the pkg package file name. For
example, the following command demonstrates installing the 64-bit
driver:

```
sudo installer -pkg ./AmazonRedshiftODBC-64-bit.X.X.XX.X.universal.pkg -target /
```
