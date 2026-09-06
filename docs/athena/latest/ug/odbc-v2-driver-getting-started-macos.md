

# macOS
<a name="odbc-v2-driver-getting-started-macos"></a>

If you want to use a macOS client computer to access Amazon Athena, the Amazon Athena ODBC driver is required.

## macOS system requirements
<a name="odbc-v2-driver-getting-started-macos-macos-system-requirements"></a>

Each macOS computer where you install the driver must meet the following requirements.
+ Use macOS version 14 or later.
+ Have 100 MB of disk space available.
+ Use version 3.52.16 or later of [iODBC](https://www.iodbc.org/dataspace/doc/iodbc/wiki/iodbcWiki/WelcomeVisitors).

## Installing the ODBC data connector on macOS
<a name="odbc-v2-driver-getting-started-macos-installing-the-odbc-data-connector-on-macos"></a>

Use the following procedure to download and install the Amazon Athena ODBC driver for macOS operating systems.

**To download and install the Amazon Athena ODBC driver for macOS**

1. Download the `.pkg` package file.

1. Double-click the `.pkg` file.

1. Follow the steps in the wizard to install the driver.

1. On the **License Agreement** page, press **Continue**, and then choose **Agree**.

1. Choose **Install**.

1. When the installation completes, choose **Finish**.

1. Enter the following command to verify that the driver is installed:

   ```
   > pkgutil --pkgs | grep athena.odbc
   ```

   If the driver installed successfully, the output resembles the following.

   ```
   com.amazon.athena.odbc.Runtime
   com.amazon.athena.odbc.Documentation
   ```

## Configuring a data source name on macOS
<a name="odbc-v2-driver-getting-started-macos-configuring-a-data-source-name-on-macos"></a>

After the driver is installed, you can find example `odbc.ini.example` and `odbcinst.ini.example` files in the following location:
+ `/opt/amazon/athena-odbc/share/athena-odbc/`

Copy the example files to a configuration directory and remove the `.example` extension. Use these files as a starting point for configuring the Amazon Athena ODBC driver and data source name (DSN).

```
sudo mkdir -p /opt/amazon/athena-odbc/etc/athena-odbc
sudo cp /opt/amazon/athena-odbc/share/athena-odbc/odbc.ini.example /opt/amazon/athena-odbc/etc/athena-odbc/odbc.ini
sudo cp /opt/amazon/athena-odbc/share/athena-odbc/odbcinst.ini.example /opt/amazon/athena-odbc/etc/athena-odbc/odbcinst.ini
```

**Note**  
By default, ODBC driver managers use the hidden configuration files `.odbc.ini` and `.odbcinst.ini`, which are located in the home directory.

To specify the path to the `odbc.ini` and `odbcinst.ini` files using the iODBC driver manager, perform the following steps.

**To specify ODBC `.ini` file locations using iODBC driver manager**

1. Set `ODBCINI` to the full path and file name of the `odbc.ini` file, as in the following example.

   ```
   export ODBCINI=/opt/amazon/athena-odbc/etc/athena-odbc/odbc.ini
   ```

1. Set `ODBCSYSINI` to the full path of the directory that contains the `odbcinst.ini` file, as in the following example.

   ```
   export ODBCSYSINI=/opt/amazon/athena-odbc/etc/athena-odbc
   ```

1. If you want to use a data source name (DSN) to connect to your data store, configure the `odbc.ini` file to define data source names (DSNs). Set the properties in the `odbc.ini` file to create a DSN that specifies the connection information for your data store, as in the following example.

   ```
   [ODBC Data Sources]
   athena_odbc_test=Amazon Athena ODBC (x64)
   
   [ATHENA_WIDE_SETTINGS] # Special DSN-name to signal driver about logging configuration.
   LogLevel=0             # set to 1 to enable ODBC driver logs
   UseAwsLogger=0         # set to 1 to enable AWS-SDK logs
   LogPath=/opt/amazon/athena-odbc/logs/ # Path to store the log files. Permissions to the location are required.
   
   [athena_odbc_test]
   Description=Amazon Athena ODBC (x64)
   Driver=/opt/amazon/athena-odbc/lib/libathenaodbc.dylib
   AwsRegion=us-west-1
   Workgroup=primary
   Catalog=AwsDataCatalog
   Schema=default
   AuthenticationType=IAM Credentials
   UID=
   PWD=
   S3OutputLocation=s3://amzn-s3-demo-bucket/
   ```

1. Configure the `odbcinst.ini` file, as in the following example.

   ```
   [ODBC Drivers]
   Amazon Athena ODBC (x64)=Installed
   
   [Amazon Athena ODBC (x64)]
   Driver=/opt/amazon/athena-odbc/lib/libathenaodbc.dylib
   Setup=/opt/amazon/athena-odbc/lib/libathenaodbc.dylib
   ```

1. After you install and configure the Amazon Athena ODBC driver, use the `iodbctest` command-line tool to verify the connection, as in the following example.

   ```
   {{username}}@ % iodbctest
   iODBC Demonstration program
   This program shows an interactive SQL processor
   Driver Manager: 03.52.1623.0502 
   
   Enter ODBC connect string (? shows list): ? 
   
   DSN                              | Driver
   ------------------------------------------------------------------------------
   athena_odbc_test                 | Amazon Athena ODBC (x64) 
   
   Enter ODBC connect string (? shows list): DSN=athena_odbc_test;
   Driver: 2.x.y.z (Amazon Athena ODBC Driver) 
   
   SQL>
   ```