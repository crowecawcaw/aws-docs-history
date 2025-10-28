# macOS

If you want to use a macOS client computer to access Amazon Athena, the Amazon Athena ODBC driver
is required.

## macOS

system requirements

Each macOS computer where you install the driver must meet the following
requirements.

- Use macOS version 14 or later.
- Have 100 MB of disk space available.
- Use version 3.52.16 or later of [iODBC](https://www.iodbc.org/dataspace/doc/iodbc/wiki/iodbcWiki/WelcomeVisitors "https://www.iodbc.org/dataspace/doc/iodbc/wiki/iodbcWiki/WelcomeVisitors").

## Installing the ODBC data connector on macOS

Use the following procedure to download and install the Amazon Athena ODBC driver for
macOS operating systems.

###### To download and install the Amazon Athena ODBC driver for macOS

1. Download the `.pkg` package file.
2. Double-click the `.pkg` file.
3. Follow the steps in the wizard to install the driver.
4. On the **License Agreement** page, press
   **Continue**, and then choose
   **Agree**.
5. Choose **Install**.
6. When the installation completes, choose **Finish**.
7. Enter the following command to verify that the driver is installed:

```
> pkgutil --pkgs | grep athenaodbc
```

Depending on your system, the output can look like one of the
following.

```
com.amazon.athenaodbc-x86_64.Config
com.amazon.athenaodbc-x86_64.Driver
```

or

```
com.amazon.athenaodbc-arm64.Config
com.amazon.athenaodbc-arm64.Driver
```

## Configuring a data source name on macOS

After the driver is installed, you can find example `.odbc.ini` and
`.odbcinst.ini` files in the following locations:

- Intel processor computers:
  `/opt/athena/odbc/x86_64/ini/`
- ARM processor computers:
  `/opt/athena/odbc/arm64/ini/`

Use the `.ini` files in this location as examples for configuring
the Amazon Athena ODBC driver and data source name (DSN).

###### Note

By default, ODBC driver managers use the hidden configuration files
`.odbc.ini` and `.odbcinst.ini`, which are
located in the home directory.

To specify the path to the `.odbc.ini` and
`.odbcinst.ini` files using the iODBC driver manager, perform the
following steps.

###### To specify ODBC `.ini` file locations using iODBC driver

manager

1. Set `ODBCINI` to the full path and file name of the
   `odbc.ini` file.
   - For macOS computers that have Intel processors, use the following
     syntax.

   ```
   export ODBCINI=/opt/athena/odbc/x86_64/ini/odbc.ini
   ```

   - For macOS computers that have ARM processors, use the following
     syntax.

   ```
   export ODBCINI=/opt/athena/odbc/arm64/ini/odbc.ini
   ```

2. Set `ODBCSYSINI` to the full path and file name of the
   `odbcinst.ini` file.
   - For macOS computers that have Intel processors, use the following
     syntax.

   ```
   export ODBCSYSINI=/opt/athena/odbc/x86_64/ini/odbcinst.ini
   ```

   - For macOS computers that have ARM processors, use the following
     syntax.

   ```
   export ODBCSYSINI=/opt/athena/odbc/arm64/ini/odbcinst.ini
   ```

3. If you want to use a data source name (DSN) to connect to your data store,
   configure the `odbc.ini` file to define data source names
   (DSNs). Set the properties in the `odbc.ini` file to create a
   DSN that specifies the connection information for your data store, as in the
   following example.

```
[ODBC Data Sources]
athena_odbc_test=Amazon Athena ODBC (x64)

[ATHENA_WIDE_SETTINGS] # Special DSN-name to signal driver about logging configuration.
LogLevel=0             # set to 1 to enable ODBC driver logs
UseAwsLogger=0         # set to 1 to enable AWS-SDK logs
LogPath=/opt/athena/odbc/logs/ # Path to store the log files. Permissions to the location are required.

[athena_odbc_test]
Description=Amazon Athena ODBC (x64)
# For ARM:
Driver=/opt/athena/odbc/arm64/lib/libathena-odbc-arm64.dylib
# For Intel:
# Driver=/opt/athena/odbc/x86_64/lib/libathena-odbc-x86_64.dylib
AwsRegion=us-west-1
Workgroup=primary
Catalog=AwsDataCatalog
Schema=default
AuthenticationType=IAM Credentials
UID=
PWD=
S3OutputLocation=s3://amzn-s3-demo-bucket/
```

4. Configure the `odbcinst.ini` file, as in the following
   example.

```
[ODBC Drivers]
Amazon Athena ODBC (x64)=Installed

[Amazon Athena ODBC (x64)]
# For ARM:
Driver=/opt/athena/odbc/arm64/lib/libathena-odbc-arm64.dylib
Setup=/opt/athena/odbc/arm64/lib/libathena-odbc-arm64.dylib
# For Intel:
# Driver=/opt/athena/odbc/x86_64/lib/libathena-odbc-x86_64.dylib
# Setup=/opt/athena/odbc/x86_64/lib/libathena-odbc-x86_64.dylib
```

5. After you install and configure the Amazon Athena ODBC driver, use the
   `iodbctest` command-line tool to verify the connection,
   as in the following example.

```
`username`@ % iodbctest
iODBC Demonstration program
This program shows an interactive SQL processor
Driver Manager: 03.52.1623.0502

Enter ODBC connect string (? shows list): ?

DSN                              | Driver
------------------------------------------------------------------------------
athena_odbc_test                 | Amazon Athena ODBC (x64)

Enter ODBC connect string (? shows list): DSN=athena_odbc_test;
Driver: 2.0.2.1 (Amazon Athena ODBC Driver)

SQL>
```
