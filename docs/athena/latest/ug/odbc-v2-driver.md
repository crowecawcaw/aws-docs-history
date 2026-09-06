

# Amazon Athena ODBC 2.x
<a name="odbc-v2-driver"></a>

You can use an ODBC connection to connect to Amazon Athena from many third-party SQL client tools and applications. You set up the ODBC connection on your client computer.

## Considerations and limitations
<a name="odbc-v2-driver-considerations-limitations"></a>

For information on migrating from the Athena ODBC 1.x driver to the Athena 2.x ODBC driver, see [Migrate to the ODBC 2.x driver](odbc-v2-driver-migrating.md).

## ODBC 2.x driver download
<a name="odbc-v2-driver-download"></a>

To download the Amazon Athena 2.x ODBC driver, visit the links on this page.

**Important**  
When you use the ODBC 2.x driver, be sure to note the following:  
**Open port 444** – Keep port 444, which Athena uses to stream query results, open to outbound traffic. When you use a PrivateLink endpoint to connect to Athena, ensure that the security group attached to the PrivateLink endpoint is open to inbound traffic on port 444. 
**athena:GetQueryResultsStream policy** – Add the `athena:GetQueryResultsStream` policy action to the IAM principals that use the ODBC driver. This policy action is not exposed directly with the API. It is used only with the ODBC and JDBC drivers as part of streaming results support. For an example policy, see [AWS managed policy: AWSQuicksightAthenaAccess](security-iam-awsmanpol.md#awsquicksightathenaaccess-managed-policy).
**Security update** – Version 2.1.0.0 includes security enhancements to authentication, query processing, and transport security components. We recommend upgrading to benefit from these improvements. For details, see the [Amazon Athena ODBC 2.x release notes](odbc-v2-driver-release-notes.md).
**Installation changes in version 2.2.0.0** – Starting from version 2.2.0.0, the installation process has changed for Windows, Linux, and macOS. On Windows, uninstall the previous driver version before installing 2.2.0.0. For more information, see [Linux](odbc-v2-driver-getting-started-linux.md), [macOS](odbc-v2-driver-getting-started-macos.md), and [Windows](odbc-v2-driver-getting-started-windows.md).

### Linux
<a name="connect-with-odbc-linux"></a>


| Driver version | Download link | 
| --- | --- | 
| ODBC 2.2.0.1 for Linux x86\_64 |  [Linux x86\_64 ODBC driver 2.2.0.1](https://downloads.athena.us-east-1.amazonaws.com/drivers/ODBC/v2.2.0.1/Linux/AmazonAthenaODBC-2.2.0.1-x86_64.rpm)  | 

### macOS
<a name="connect-with-odbc-macos"></a>


| Driver version | Download link | 
| --- | --- | 
| ODBC 2.2.0.1 for macOS |  [macOS ODBC driver 2.2.0.1](https://downloads.athena.us-east-1.amazonaws.com/drivers/ODBC/v2.2.0.1/Mac/AmazonAthenaODBC-2.2.0.1-macos11-universal.pkg)  | 

### Windows
<a name="connect-with-odbc-windows"></a>


| Driver version | Download link | 
| --- | --- | 
| ODBC 2.2.0.1 for Windows amd64 |  [Windows amd64 ODBC driver 2.2.0.1](https://downloads.athena.us-east-1.amazonaws.com/drivers/ODBC/v2.2.0.1/Windows/AmazonAthenaODBC-2.2.0.1-windows-amd64.msi)  | 

### Licenses
<a name="connect-with-odbc-licenses"></a>
+  [AWS license](https://downloads.athena.us-east-1.amazonaws.com/drivers/ODBC/v2.2.0.1/LICENSE.txt) 

## Trusted identity propagation with ODBC
<a name="odbc-v2-driver-trusted-identity"></a>

You can now connect to Amazon Athena using ODBC drivers with single sign-on capabilities through AWS Identity and Access Management Identity Center. When you access Athena from tools like PowerBI, Tableau, or DBeaver, your identity and permissions automatically propagate to Athena through IAM Identity Center. For more information, see [Use Trusted identity propagation with Amazon Athena drivers](using-trusted-identity-propagation.md).

**Topics**
+ [Considerations and limitations](#odbc-v2-driver-considerations-limitations)
+ [ODBC 2.x driver download](#odbc-v2-driver-download)
+ [Trusted identity propagation with ODBC](#odbc-v2-driver-trusted-identity)
+ [Get started with the ODBC 2.x driver](odbc-v2-driver-getting-started.md)
+ [Athena ODBC 2.x connection parameters](odbc-v2-driver-connection-parameters.md)
+ [Migrate to the ODBC 2.x driver](odbc-v2-driver-migrating.md)
+ [Troubleshoot the ODBC 2.x driver](odbc-v2-driver-troubleshooting.md)
+ [Amazon Athena ODBC 2.x release notes](odbc-v2-driver-release-notes.md)
+ [Previous versions of the Athena ODBC 2.x driver](odbc-v2-driver-previous-versions.md)