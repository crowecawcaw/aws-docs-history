

# Linux
<a name="odbc-v2-driver-getting-started-linux"></a>

If you want use a Linux client computer to access Amazon Athena, the Amazon Athena ODBC driver is required.

## Linux system requirements
<a name="odbc-v2-driver-getting-started-linux-linux-system-requirements"></a>

Each Linux client computer where you install the driver must meet the following requirements.
+ You have root access.
+ Use one of the following Linux distributions:
  + Amazon Linux 2023
  + Red Hat Enterprise Linux (RHEL) 9 or later. On RHEL 9, use Amazon Athena ODBC driver version 2.2.0.2 or later. Versions 2.1.0.0 through 2.2.0.1 can fail to install because they require `GLIBCXX` symbol versions that are unavailable in the standard RHEL 9 repositories.
+ Have 100 MB of disk space available.
+ Use version 2.3.9 or later of [unixODBC](https://www.unixodbc.org/).
+ Use version 2.34 or later of the [GNU C Library](https://www.gnu.org/software/libc/) (glibc).

## Installing the ODBC data connector on Linux
<a name="odbc-v2-driver-getting-started-linux-installing-the-odbc-data-connector-on-linux"></a>

Use the following procedure to install the Amazon Athena ODBC driver on a Linux operating system.

**To install the Amazon Athena ODBC driver on Linux**

1. Enter one of the following commands:

   ```
   sudo rpm -Uvh AmazonAthenaODBC-2.X.Y.Z-x86_64.rpm
   ```

   or

   ```
   sudo yum --nogpgcheck localinstall AmazonAthenaODBC-2.X.Y.Z-x86_64.rpm
   ```

1. After the installation finishes, enter one of the following commands to verify that the driver is installed:
   + 

     ```
     yum list | grep amazon-athena-odbc-driver
     ```

     Output:

     ```
     amazon-athena-odbc-driver.x86_64 2.2.0.1-1.amzn2023 installed
     ```
   + 

     ```
     rpm -qa | grep amazon
     ```

     Output:

     ```
     amazon-athena-odbc-driver-2.2.0.1-1.amzn2023.x86_64
     ```

## Configuring a data source name on Linux
<a name="odbc-v2-driver-getting-started-linux-configuring-a-data-source-name-on-linux"></a>

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

To specify the path to the `odbc.ini` and `odbcinst.ini` files using unixODBC, perform the following steps.

**To specify ODBC `.ini` file locations using unixODBC**

1. Set `ODBCINI` to the full path and file name of the `odbc.ini` file, as in the following example.

   ```
   export ODBCINI=/opt/amazon/athena-odbc/etc/athena-odbc/odbc.ini
   ```

1. Set `ODBCSYSINI` to the full path of the directory that contains the `odbcinst.ini` file, as in the following example.

   ```
   export ODBCSYSINI=/opt/amazon/athena-odbc/etc/athena-odbc
   ```

1. Enter the following command to verify that you are using the unixODBC driver manager and the correct `odbc*.ini` files:

   ```
   {{username}} % odbcinst -j
   ```

   Sample output

   ```
   unixODBC 2.3.1
   DRIVERS............: /opt/amazon/athena-odbc/etc/athena-odbc/odbcinst.ini
   SYSTEM DATA SOURCES: /opt/amazon/athena-odbc/etc/athena-odbc/odbc.ini
   FILE DATA SOURCES..: /opt/amazon/athena-odbc/etc/athena-odbc/ODBCDataSources
   USER DATA SOURCES..: /opt/amazon/athena-odbc/etc/athena-odbc/odbc.ini
   SQLULEN Size.......: 8
   SQLLEN Size........: 8
   SQLSETPOSIROW Size.: 8
   ```

1. If you want to use a data source name (DSN) to connect to your data store, configure the `odbc.ini` file to define data source names (DSNs). Set the properties in the `odbc.ini` file to create a DSN that specifies the connection information for your data store, as in the following example.

   ```
   [ODBC Data Sources]
   athena_odbc_test=Amazon Athena ODBC (x64)
   
   [ATHENA_WIDE_SETTINGS]  # Special DSN-name to signal driver about logging configuration.
   LogLevel=0              # To enable ODBC driver logs, set this to 1.
   UseAwsLogger=0          # To enable AWS-SDK logs, set this to 1.
   LogPath=/opt/amazon/athena-odbc/logs/ # Path to store the log files. Permissions to the location are required.
   
   [athena_odbc_test]
   Driver=/opt/amazon/athena-odbc/lib/libathenaodbc.so
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
   Driver=/opt/amazon/athena-odbc/lib/libathenaodbc.so
   Setup=/opt/amazon/athena-odbc/lib/libathenaodbc.so
   ```

1. After you install and configure the Amazon Athena ODBC driver, use the unixODBC `isql` command-line tool to verify the connection, as in the following example.

   ```
   {{username}} % isql -v "athena_odbc_test" 
   +---------------------------------------+
   | Connected!                            |
   |                                       |
   | sql-statement                         |
   | help [tablename]                      |
   | quit                                  |
   |                                       |
   +---------------------------------------+
   SQL>
   ```

## Verify the ODBC driver signature
<a name="verify-odbc-linux-signature"></a>

**Important**  
We recommend verifying the Athena ODBC driver RPM signature before installing it on your machine.

Follow these steps to verify the signature of the Athena ODBC driver RPM package:

1. **Prepare the templates**

   Prepare the commands with appropriate public key, RPM signature, and the corresponding access link to the RPM scripts hosted in Amazon S3 buckets. You must download the following to your device.
   +  [Athena ODBC driver](https://downloads.athena.us-east-1.amazonaws.com/drivers/ODBC/v2.2.0.1/Linux/AmazonAthenaODBC-2.2.0.1-x86_64.rpm) 
   +  [Public Key](https://downloads.athena.us-east-1.amazonaws.com/drivers/ODBC/v2.2.0.1/Linux/public_key.pem) 
   +  [Athena ODBC RPM signature](https://downloads.athena.us-east-1.amazonaws.com/drivers/ODBC/v2.2.0.1/Linux/signature.bin) 

1. Download the Athena ODBC driver, public key, and Athena ODBC RPM signature to your device. 

1. Run the following command to verify ODBC driver signature:

   ```
   openssl dgst -sha256 -verify public_key.pem -signature signature.bin AmazonAthenaODBC-2.2.0.1-x86_64.rpm
   ```

   If verification passes, you will see a message similar to `Verified OK`. This means you can now proceed to install the Athena ODBC driver. 

   If it fails with a message `Verification Failure`, it means that the signature on RPM has been tampered. Ensure that all the three files mentioned in step 1 are present, the paths are correctly specified ,and the files haven't been modified since download and then retry the verification process.