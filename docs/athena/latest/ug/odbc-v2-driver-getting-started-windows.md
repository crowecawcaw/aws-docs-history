# Windows

If you want to use a Windows client computer to access Amazon Athena, the Amazon Athena ODBC driver
is required.

## Windows system requirements

Install the Amazon Athena ODBC driver on client computers that will access Amazon Athena
databases directly instead of using a web browser.

The Windows system you use must meet the following requirements:

- You have administrator rights
- One of the following operating systems:
  - Windows 11, 10, or 8.1
  - Windows Server 2019, 2016, or 2012
  - Supported processor architecture : x86_64 (64-bit)

- At least 100 MB of available disk space
- [Microsoft Visual C++ Redistributable for Visual Studio](https://visualstudio.microsoft.com/downloads/#microsoft-visual-c-redistributable-for-visual-studio-2022 "https://visualstudio.microsoft.com/downloads/#microsoft-visual-c-redistributable-for-visual-studio-2022") for 64-bit
  Windows is installed.

## Installing the Amazon Athena ODBC driver

###### To download and install the Amazon Athena ODBC driver for Windows

1. [Download](odbc-v2-driver.md#odbc-v2-driver-download "odbc-v2-driver.md#odbc-v2-driver-download") the
   `AmazonAthenaODBC-2.`x`.`x`.`x`.msi`
   installation file.
2. Launch the installation file, and then choose
   **Next**.
3. To accept the terms of the license agreement, select the check box, and then
   choose **Next**.
4. To change the installation location, choose **Browse**,
   browse to the desired folder, and then choose **OK**.
5. To accept the installation location, choose **Next**.
6. Choose **Install**.
7. When the installation completes, choose **Finish**.

## Ways to set driver configuration options

To control the behavior of the Amazon Athena ODBC driver in Windows, you can set driver
configuration options in the following ways:

- In the **ODBC Data Source Administrator** program when you
  configure a data source name (DSN).
- By adding or changing Windows registry keys in the following location:

```
HKEY_LOCAL_MACHINE\SOFTWARE\ODBC\ODBC.INI\YOUR_DSN_NAME
```

- By setting driver options in the connection string when you connect
  programmatically.

## Configuring a data source name on Windows

After you download and install the ODBC driver, you must add a data source name (DSN)
entry to the client computer or Amazon EC2 instance. SQL client tools use this data source to
connect to and query Amazon Athena.

###### To create a system DSN entry

1. From the Windows **Start** menu, right-click **ODBC
   Data Sources (64 bit)**, and then choose **More**,
   **Run as administrator**.
2. In the **ODBC Data Source Administrator**, choose the
   **Drivers** tab.
3. In the **Name** column, verify that **Amazon Athena ODBC
   (x64)** is present.
4. Do one of the following:
   - To configure the driver for all users on the computer, choose the
     **System DSN** tab. Because applications that use a
     different account to load data might not be able to detect user DSNs
     from another account, we recommend the system DSN configuration
     option.

   ###### Note

   Using the **System DSN** option requires
   administrative privileges.
   - To configure the driver for your user account only, choose the
     **User DSN** tab.

5. Choose **Add**. The **Create New Data
   Source** dialog box opens.
6. Choose **Amazon Athena ODBC (x64)**, and then choose
   **Finish**.
7. In the **Amazon Athena ODBC Configuration** dialog box, enter the
   following information. For detailed information about these options, see [Main ODBC 2.x connection parameters](odbc-v2-driver-main-connection-parameters.md "odbc-v2-driver-main-connection-parameters.md").
   - For **Data Source Name**, enter a name that you want
     to use to identify the data source.
   - For **Description**, enter a description to help you
     identify the data source.
   - For **Region**, enter the name of the AWS Region
     that you will use Athena in (for example, `us-west-1`).
   - For **Catalog**, enter the name of the Amazon Athena
     catalog. The default is **AwsDataCatalog**, which is
     used by AWS Glue.
   - For **Database**, enter the name of the Amazon Athena
     database. The default is **default**.
   - For **Workgroup**, enter the name of the Amazon Athena
     workgroup. The default is **primary**.
   - For **S3 Output Location**, enter the location in
     Amazon S3 where the query results will be stored (for example,
     `s3://amzn-s3-demo-bucket/`).
   - (Optional) For **Encryption Options**, choose an
     encryption option. The default is `NOT_SET`.
   - (Optional) For **KMS Key**, choose an encryption KMS
     key if required.

8. To specify configuration options for IAM authentication, choose
   **Authentication Options.**
9. Enter the following information:
   - For **Authentication Type**, choose **IAM
     Credentials**. This is the default. For more information
     about available authentication types, see [Authentication options](odbc-v2-driver-authentication-options.md "odbc-v2-driver-authentication-options.md").
   - For **Username**, enter a user name.
   - For **Password**, enter a password.
   - For **Session Token**, enter a session token if you
     want to use temporary AWS credentials. For information about temporary
     credentials, see [Using temporary credentials with AWS resources](../../../IAM/latest/UserGuide/id_credentials_temp_use-resources.md "../../../IAM/latest/UserGuide/id_credentials_temp_use-resources.md") in the
     _IAM User Guide_.

10. Choose **OK**.
11. At the bottom of the **Amazon Athena ODBC Configuration**
    dialog box, choose **Test**. If the client computer connects
    successfully to Amazon Athena, the **Connection test** box reports
    **Connection successful**. If not, the box reports
    **Connection failed** with corresponding error
    information.
12. Choose **OK** to close the connection test. The data source
    that you created now appears in the list of data source names.

## Using a DSN-less connection on Windows

You can use a DSN-less connection to connect to a database without a Data Source Name
(DSN). The following example shows a connection string for the Amazon Athena ODBC (x64) ODBC
driver that connects to Amazon Athena.

```
DRIVER={Amazon Athena ODBC (x64)};Catalog=AwsDataCatalog;AwsRegion=us-west-1;Schema=test_schema;S3OutputLocation=
s3://amzn-s3-demo-bucket/;AuthenticationType=IAM Credentials;UID=YOUR_UID;PWD=YOUR_PWD;
```
