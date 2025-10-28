# Linux

If you want use a Linux client computer to access Amazon Athena, the Amazon Athena ODBC driver is
required.

## Linux

system requirements

Each Linux client computer where you install the driver must meet the following
requirements.

- You have root access.
- Use one of the following Linux distributions:
  - Red Hat Enterprise Linux (RHEL) 7 or 8
  - CentOS 7 or 8.

- Have 100 MB of disk space available.
- Use version 2.3.1 or later of [unixODBC](https://www.unixodbc.org/ "https://www.unixodbc.org/").
- Use version 2.26 or later of the [GNU C Library](https://www.gnu.org/software/libc/ "https://www.gnu.org/software/libc/")
  (glibc).

## Installing the ODBC data connector on Linux

Use the following procedure to install the Amazon Athena ODBC driver on a Linux operating
system.

###### To install the Amazon Athena ODBC driver on Linux

1. Enter one of the following commands:

```
sudo rpm -Uvh AmazonAthenaODBC-2.X.Y.Z.rpm
```

or

```
sudo yum --nogpgcheck localinstall AmazonAthenaODBC-2.X.Y.Z.rpm
```

2. After the installation finishes, enter one of the following commands to verify
   that the driver is installed:
   - ```
     yum list | grep amazon-athena-odbc-driver
     ```

   ```

   Output:



   ```

   amazon-athena-odbc-driver.x86_64 2.0.2.1-1.amzn2int installed

   ````
   * ```
   rpm -qa | grep amazon
   ````

   Output:

   ```
   amazon-athena-odbc-driver-2.0.2.1-1.amzn2int.x86_64
   ```

## Configuring a data source name on Linux

After the driver is installed, you can find example `.odbc.ini` and
`.odbcinst.ini` files in the following location:

- `/opt/athena/odbc/ini/`.

Use the `.ini` files in this location as examples for configuring
the Amazon Athena ODBC driver and data source name (DSN).

###### Note

By default, ODBC driver managers use the hidden configuration files
`.odbc.ini` and `.odbcinst.ini`, which are
located in the home directory.

To specify the path to the `.odbc.ini` and
`.odbcinst.ini` files using unixODBC, perform the following
steps.

###### To specify ODBC `.ini` file locations using unixODBC

1. Set `ODBCINI` to the full path and file name of the
   `odbc.ini` file, as in the following example.

```
export ODBCINI=/opt/athena/odbc/ini/odbc.ini
```

2. Set `ODBCSYSINI` to the full path of the directory that contains
   the `odbcinst.ini` file, as in the following example.

```
export ODBCSYSINI=/opt/athena/odbc/ini
```

3. Enter the following command to verify that you are using the unixODBC driver
   manager and the correct `odbc*.ini` files:

```
`username` % odbcinst -j
```

Sample output

```
unixODBC 2.3.1
DRIVERS............: /opt/athena/odbc/ini/odbcinst.ini
SYSTEM DATA SOURCES: /opt/athena/odbc/ini/odbc.ini
FILE DATA SOURCES..: /opt/athena/odbc/ini/ODBCDataSources
USER DATA SOURCES..: /opt/athena/odbc/ini/odbc.ini
SQLULEN Size.......: 8
SQLLEN Size........: 8
SQLSETPOSIROW Size.: 8
```

4. If you want to use a data source name (DSN) to connect to your data store,
   configure the `odbc.ini` file to define data source names
   (DSNs). Set the properties in the `odbc.ini` file to create a
   DSN that specifies the connection information for your data store, as in the
   following example.

```
[ODBC Data Sources]
athena_odbc_test=Amazon Athena ODBC (x64)

[ATHENA_WIDE_SETTINGS]  # Special DSN-name to signal driver about logging configuration.
LogLevel=0              # To enable ODBC driver logs, set this to 1.
UseAwsLogger=0          # To enable AWS-SDK logs, set this to 1.
LogPath=/opt/athena/odbc/logs/ # Path to store the log files. Permissions to the location are required.

[athena_odbc_test]
Driver=/opt/athena/odbc/lib/libathena-odbc.so
AwsRegion=us-west-1
Workgroup=primary
Catalog=AwsDataCatalog
Schema=default
AuthenticationType=IAM Credentials
UID=
PWD=
S3OutputLocation=s3://amzn-s3-demo-bucket/
```

5. Configure the `odbcinst.ini` file, as in the following
   example.

```
[ODBC Drivers]
Amazon Athena ODBC (x64)=Installed

[Amazon Athena ODBC (x64)]
Driver=/opt/athena/odbc/lib/libathena-odbc.so
Setup=/opt/athena/odbc/lib/libathena-odbc.so
```

6. After you install and configure the Amazon Athena ODBC driver, use the unixODBC
   `isql` command-line tool to verify the connection, as in
   the following example.

````
`username` % isql -v "athena_odbc_test"
+---------------------------------------+
| Connected!                            |
|                                       |
| sql-statement                         |
| help [tablename]                      |
| quit                                  |
|                                       | +---------------------------------------+ SQL> ``` ## Verify the ODBC driver signature ###### Important We recommend verifying the Athena ODBC driver RPM signature before installing it on your machine. Follow these steps to verify the signature of the Athena ODBC driver RPM package: 1. **Prepare the templates** Prepare the commands with appropriate public key, RPM signature, and the corresponding access link to the RPM scripts hosted in Amazon S3 buckets. You must download the following to your device. <br>• [Athena ODBC driver](https://downloads.athena.us-east-1.amazonaws.com/drivers/ODBC/v2.0.4.0/Linux/AmazonAthenaODBC-2.0.4.0.rpm "https://downloads.athena.us-east-1.amazonaws.com/drivers/ODBC/v2.0.4.0/Linux/AmazonAthenaODBC-2.0.4.0.rpm") <br>• [Public Key](https://downloads.athena.us-east-1.amazonaws.com/drivers/ODBC/v2.0.4.0/Linux/public_key.pem "https://downloads.athena.us-east-1.amazonaws.com/drivers/ODBC/v2.0.4.0/Linux/public_key.pem") <br>• [Athena ODBC RPM signature](https://downloads.athena.us-east-1.amazonaws.com/drivers/ODBC/v2.0.4.0/Linux/signature.bin "https://downloads.athena.us-east-1.amazonaws.com/drivers/ODBC/v2.0.4.0/Linux/signature.bin") 2. Download the Athena ODBC driver, public key, and Athena ODBC RPM signature to your device. 3. Run the following command to verify ODBC driver signature: ``` openssl dgst -sha256 -verify public_key.pem -signature signature.bin AmazonAthenaODBC-2.0.4.0.rpm ``` If verification passes, you will see a message similar to `Verified OK`. This means you can now proceed to install the Athena ODBC driver. If it fails with a message `Verification Failure`, it means that the signature on RPM has been tampered. Ensure that all the three files mentioned in step 1 are present, the paths are correctly specified ,and the files haven't been modified since download and then retry the verification process.
````
