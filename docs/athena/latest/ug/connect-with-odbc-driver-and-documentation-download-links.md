

# Athena ODBC 1.x driver
<a name="connect-with-odbc-driver-and-documentation-download-links"></a>

You can use an ODBC connection to connect to Athena from third-party SQL client tools and applications. Use the links on this page to download the Amazon Athena 1.x ODBC driver License Agreement, ODBC drivers, and ODBC documentation. For information about the ODBC connection string, see the ODBC Driver Installation and Configuration Guide PDF file, downloadable from this page. For permissions information, see [Control access through JDBC and ODBC connections](policy-actions.md).

**Important**  
When you use the ODBC 1.x driver, be sure to note the following requirements:  
**Open port 444** – Keep port 444, which Athena uses to stream query results, open to outbound traffic. When you use a PrivateLink endpoint to connect to Athena, ensure that the security group attached to the PrivateLink endpoint is open to inbound traffic on port 444. 
**athena:GetQueryResultsStream policy** – Add the `athena:GetQueryResultsStream` policy action to the IAM principals that use the ODBC driver. This policy action is not exposed directly with the API. It is used only with the ODBC and JDBC drivers as part of streaming results support. For an example policy, see [AWS managed policy: AWSQuicksightAthenaAccess](security-iam-awsmanpol.md#awsquicksightathenaaccess-managed-policy). 

## Windows
<a name="connect-with-odbc-windows"></a>


| Driver version | Download link | 
| --- | --- | 
| ODBC 1.3.7.10001 for Windows 32-bit | [Windows 32 bit ODBC driver 1.3.7.10001](https://downloads.athena.us-east-1.amazonaws.com/drivers/ODBC/SimbaAthenaODBC_1.3.7.10001/Windows/SimbaAthena_1.3.7.10001_32-bit.msi) | 
| ODBC 1.3.7.10001 for Windows 64-bit | [Windows 64 bit ODBC driver 1.3.7.10001](https://downloads.athena.us-east-1.amazonaws.com/drivers/ODBC/SimbaAthenaODBC_1.3.7.10001/Windows/SimbaAthena_1.3.7.10001_64-bit.msi) | 

## Linux
<a name="connect-with-odbc-linux"></a>


| Driver version | Download link | 
| --- | --- | 
| ODBC 1.3.7.10001 for Linux 32-bit | [Linux 32 bit ODBC driver 1.3.7.10001](https://downloads.athena.us-east-1.amazonaws.com/drivers/ODBC/SimbaAthenaODBC_1.3.7.10001/Linux/simbaathena-1.3.7.10001.el8.i686.rpm) | 
| ODBC 1.3.7.10001 for Linux 64-bit | [Linux 64 bit ODBC driver 1.3.7.10001](https://downloads.athena.us-east-1.amazonaws.com/drivers/ODBC/SimbaAthenaODBC_1.3.7.10001/Linux/simbaathena-1.3.7.10001.el8.x86_64.rpm) | 

## OSX
<a name="connect-with-odbc-osx"></a>


| Driver version | Download link | 
| --- | --- | 
| ODBC 1.3.7.10001 for OSX | [OSX ODBC driver 1.3.7.10001](https://downloads.athena.us-east-1.amazonaws.com/drivers/ODBC/SimbaAthenaODBC_1.3.7.10001/OSX/SimbaAthena_1.3.7.10001.dmg) | 

## Documentation
<a name="connect-with-odbc-driver-documentation"></a>


| Content | Documentation link | 
| --- | --- | 
| Amazon Athena ODBC driver license agreement |  [License agreement](https://downloads.athena.us-east-1.amazonaws.com/agreement/ODBC/Amazon+Athena+ODBC+Driver+License+Agreement.pdf)  | 
| Documentation for ODBC 1.3.7.10001 | [ODBC driver installation and configuration guide version 1.3.7.10001](https://downloads.athena.us-east-1.amazonaws.com/drivers/ODBC/SimbaAthenaODBC_1.3.7.10001/docs/Simba+Amazon+Athena+ODBC+Connector+Install+and+Configuration+Guide.pdf) | 
| Release Notes for ODBC 1.3.7.10001 | [ODBC driver release notes version 1.3.7.10001](https://downloads.athena.us-east-1.amazonaws.com/drivers/ODBC/SimbaAthenaODBC_1.3.7.10001/docs/release-notes.txt) | 

## ODBC driver notes
<a name="connect-with-odbc-configuration"></a>

**Connecting Without Using a Proxy**  
If you want to specify certain hosts that the driver connects to without using a proxy, you can use the optional `NonProxyHost` property in your ODBC connection string.

The `NonProxyHost` property specifies a comma-separated list of hosts that the connector can access without going through the proxy server when a proxy connection is enabled, as in the following example:

```
.amazonaws.com,localhost,.example.net,.example.com
```

The `NonProxyHost` connection parameter is passed to the `CURLOPT_NOPROXY` curl option. For information about the `CURLOPT_NOPROXY` format, see [CURLOPT\_NOPROXY](https://curl.se/libcurl/c/CURLOPT_NOPROXY.html) in the curl documentation. 