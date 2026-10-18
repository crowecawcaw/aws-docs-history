

# Amazon Athena in AWS GovCloud (US)
<a name="govcloud-athena"></a>

Amazon Athena is an interactive query service that makes it easy to analyze data directly in Amazon Simple Storage Service (Amazon S3) using standard SQL. With a few actions in the AWS Management Console, you can point Athena at your data stored in Amazon S3 and begin using standard SQL to run ad-hoc queries and get results in seconds. Athena is serverless, so there is no infrastructure to set up or manage, and you pay only for the queries you run. Athena scales automatically—executing queries in parallel—so results are fast, even with large datasets and complex queries.

## Region availability
<a name="_region_availability"></a>

This service is available in the following AWS GovCloud (US) Regions:
+  AWS GovCloud (US-West) 
+  AWS GovCloud (US-East) 

## How Athena differs
<a name="govcloud-athena-diffs"></a>

The following differences apply to Athena:
+ Granting AWS Lake Formation permissions to Amazon Athena users who authenticate through the JDBC or ODBC driver using a SAML identity provider is not available.

## JDBC driver download links
<a name="govcloud-athena-jdbc-driver-download-links"></a>

Use the links in this section to download the latest JDBC 3.x driver for Athena.

### JDBC driver uber jar
<a name="_jdbc_driver_uber_jar"></a>

The following download packages the driver and all its dependencies in the same `.jar` file. This download is commonly used for third-party SQL clients.

 [3.8.2 uber jar](https://aws-analytics-downloads-us-gov-west-1.s3.us-gov-west-1.amazonaws.com/athena/JDBC/3.8.2/athena-jdbc-3.8.2-with-dependencies.jar) 

### JDBC driver lean jar
<a name="_jdbc_driver_lean_jar"></a>

The following download is a `.zip` file that contains the lean `.jar` for the driver and separate `.jar` files for the driver’s dependencies. This download is commonly used for custom applications that might have dependencies that conflict with the dependencies that the driver uses.

 [3.8.2 lean jar](https://aws-analytics-downloads-us-gov-west-1.s3.us-gov-west-1.amazonaws.com/athena/JDBC/3.8.2/athena-jdbc-3.8.2-lean-jar-and-separate-dependencies-jars.zip) 

### License
<a name="_license"></a>

The following link contains the license agreement for the JDBC 3.x driver.

 [License](https://aws-analytics-downloads-us-gov-west-1.s3.us-gov-west-1.amazonaws.com/athena/JDBC/3.8.2/LICENSE.txt) 

## Previous versions of the Athena JDBC 3.x driver
<a name="jdbc-v3-driver-previous-versions"></a>

We highly recommend that you use the latest version of the JDBC 3.x driver. The latest version of the driver contains the most recent improvements and fixes. Use an older version only if your application experiences incompatibilities with the latest version.

### JDBC driver uber jar
<a name="jdbc-v3-driver-download-uber-jar-previous"></a>

The following download packages the driver and all its dependencies in the same `.jar` file. This download is commonly used for third-party SQL clients.
+  [3.8.1 uber jar](https://aws-analytics-downloads-us-gov-west-1.s3.us-gov-west-1.amazonaws.com/athena/JDBC/3.8.1/athena-jdbc-3.8.1-with-dependencies.jar) 
+  [3.8.0 uber jar](https://aws-analytics-downloads-us-gov-west-1.s3.us-gov-west-1.amazonaws.com/athena/JDBC/3.8.0/athena-jdbc-3.8.0-with-dependencies.jar) 
+  [3.7.0 uber jar](https://aws-analytics-downloads-us-gov-west-1.s3.us-gov-west-1.amazonaws.com/athena/JDBC/3.7.0/athena-jdbc-3.7.0-with-dependencies.jar) 
+  [3.6.0 uber jar](https://aws-analytics-downloads-us-gov-west-1.s3.us-gov-west-1.amazonaws.com/athena/JDBC/3.6.0/athena-jdbc-3.6.0-with-dependencies.jar) 
+  [3.5.1 uber jar](https://aws-analytics-downloads-us-gov-west-1.s3.us-gov-west-1.amazonaws.com/athena/JDBC/3.5.1/athena-jdbc-3.5.1-with-dependencies.jar) 
+  [3.5.0 uber jar](https://aws-analytics-downloads-us-gov-west-1.s3.us-gov-west-1.amazonaws.com/athena/JDBC/3.5.0/athena-jdbc-3.5.0-with-dependencies.jar) 
+  [3.4.0 uber jar](https://aws-analytics-downloads-us-gov-west-1.s3.us-gov-west-1.amazonaws.com/athena/JDBC/3.4.0/athena-jdbc-3.4.0-with-dependencies.jar) 
+  [3.3.0 uber jar](https://aws-analytics-downloads-us-gov-west-1.s3.us-gov-west-1.amazonaws.com/athena/JDBC/3.3.0/athena-jdbc-3.3.0-with-dependencies.jar) 
+  [3.2.2 uber jar](https://aws-analytics-downloads-us-gov-west-1.s3.us-gov-west-1.amazonaws.com/athena/JDBC/3.2.2/athena-jdbc-3.2.2-with-dependencies.jar) 
+  [3.2.1 uber jar](https://aws-analytics-downloads-us-gov-west-1.s3.us-gov-west-1.amazonaws.com/athena/JDBC/3.2.1/athena-jdbc-3.2.1-with-dependencies.jar) 
+  [3.2.0 uber jar](https://aws-analytics-downloads-us-gov-west-1.s3.us-gov-west-1.amazonaws.com/athena/JDBC/3.2.0/athena-jdbc-3.2.0-with-dependencies.jar) 
+  [3.1.0 uber jar](https://aws-analytics-downloads-us-gov-west-1.s3.us-gov-west-1.amazonaws.com/athena/JDBC/3.1.0/athena-jdbc-3.1.0-with-dependencies.jar) 
+  [3.0.0 uber jar](https://aws-analytics-downloads-us-gov-west-1.s3.us-gov-west-1.amazonaws.com/athena/JDBC/3.0.0/athena-jdbc-3.0.0-with-dependencies.jar) 

### JDBC driver lean jar
<a name="jdbc-v3-driver-download-lean-jar-previous"></a>

The following download is a `.zip` file that contains the lean `.jar` for the driver and separate `.jar` files for the driver’s dependencies. This download is commonly used for custom applications that might have dependencies that conflict with the dependencies that the driver uses.
+  [3.8.1 lean jar](https://aws-analytics-downloads-us-gov-west-1.s3.us-gov-west-1.amazonaws.com/athena/JDBC/3.8.1/athena-jdbc-3.8.1-lean-jar-and-separate-dependencies-jars.zip) 
+  [3.8.0 lean jar](https://aws-analytics-downloads-us-gov-west-1.s3.us-gov-west-1.amazonaws.com/athena/JDBC/3.8.0/athena-jdbc-3.8.0-lean-jar-and-separate-dependencies-jars.zip) 
+  [3.7.0 lean jar](https://aws-analytics-downloads-us-gov-west-1.s3.us-gov-west-1.amazonaws.com/athena/JDBC/3.7.0/athena-jdbc-3.7.0-lean-jar-and-separate-dependencies-jars.zip) 
+  [3.6.0 lean jar](https://aws-analytics-downloads-us-gov-west-1.s3.us-gov-west-1.amazonaws.com/athena/JDBC/3.6.0/athena-jdbc-3.6.0-lean-jar-and-separate-dependencies-jars.zip) 
+  [3.5.1 lean jar](https://aws-analytics-downloads-us-gov-west-1.s3.us-gov-west-1.amazonaws.com/athena/JDBC/3.5.1/athena-jdbc-3.5.1-lean-jar-and-separate-dependencies-jars.zip) 
+  [3.5.0 lean jar](https://aws-analytics-downloads-us-gov-west-1.s3.us-gov-west-1.amazonaws.com/athena/JDBC/3.5.0/athena-jdbc-3.5.0-lean-jar-and-separate-dependencies-jars.zip) 
+  [3.4.0 lean jar](https://aws-analytics-downloads-us-gov-west-1.s3.us-gov-west-1.amazonaws.com/athena/JDBC/3.4.0/athena-jdbc-3.4.0-lean-jar-and-separate-dependencies-jars.zip) 
+  [3.3.0 lean jar](https://aws-analytics-downloads-us-gov-west-1.s3.us-gov-west-1.amazonaws.com/athena/JDBC/3.3.0/athena-jdbc-3.3.0-lean-jar-and-separate-dependencies-jars.zip) 
+  [3.2.2 lean jar](https://aws-analytics-downloads-us-gov-west-1.s3.us-gov-west-1.amazonaws.com/athena/JDBC/3.2.2/athena-jdbc-3.2.2-lean-jar-and-separate-dependencies-jars.zip) 
+  [3.2.1 lean jar](https://aws-analytics-downloads-us-gov-west-1.s3.us-gov-west-1.amazonaws.com/athena/JDBC/3.2.1/athena-jdbc-3.2.1-lean-jar-and-separate-dependencies-jars.zip) 
+  [3.2.0 lean jar](https://aws-analytics-downloads-us-gov-west-1.s3.us-gov-west-1.amazonaws.com/athena/JDBC/3.2.0/athena-jdbc-3.2.0-lean-jar-and-separate-dependencies-jars.zip) 
+  [3.1.0 lean jar](https://aws-analytics-downloads-us-gov-west-1.s3.us-gov-west-1.amazonaws.com/athena/JDBC/3.1.0/athena-jdbc-3.1.0-lean-jar-and-separate-dependencies-jars.zip) 
+  [3.0.0 lean jar](https://aws-analytics-downloads-us-gov-west-1.s3.us-gov-west-1.amazonaws.com/athena/JDBC/3.0.0/athena-jdbc-3.0.0-lean-jar-and-separate-dependencies-jars.zip) 

### Licenses
<a name="jdbc-v3-driver-license-previous"></a>
+  [3.8.1 license](https://aws-analytics-downloads-us-gov-west-1.s3.us-gov-west-1.amazonaws.com/athena/JDBC/3.8.1/LICENSE.txt) 
+  [3.8.0 license](https://aws-analytics-downloads-us-gov-west-1.s3.us-gov-west-1.amazonaws.com/athena/JDBC/3.8.0/LICENSE.txt) 
+  [3.7.0 license](https://aws-analytics-downloads-us-gov-west-1.s3.us-gov-west-1.amazonaws.com/athena/JDBC/3.7.0/LICENSE.txt) 
+  [3.6.0 license](https://aws-analytics-downloads-us-gov-west-1.s3.us-gov-west-1.amazonaws.com/athena/JDBC/3.6.0/LICENSE.txt) 
+  [3.5.1 license](https://aws-analytics-downloads-us-gov-west-1.s3.us-gov-west-1.amazonaws.com/athena/JDBC/3.5.1/LICENSE.txt) 
+  [3.5.0 license](https://aws-analytics-downloads-us-gov-west-1.s3.us-gov-west-1.amazonaws.com/athena/JDBC/3.5.0/LICENSE.txt) 
+  [3.4.0 license](https://aws-analytics-downloads-us-gov-west-1.s3.us-gov-west-1.amazonaws.com/athena/JDBC/3.4.0/LICENSE.txt) 
+  [3.3.0 license](https://aws-analytics-downloads-us-gov-west-1.s3.us-gov-west-1.amazonaws.com/athena/JDBC/3.3.0/LICENSE.txt) 
+  [3.2.2 license](https://aws-analytics-downloads-us-gov-west-1.s3.us-gov-west-1.amazonaws.com/athena/JDBC/3.2.2/LICENSE.txt) 
+  [3.2.1 license](https://aws-analytics-downloads-us-gov-west-1.s3.us-gov-west-1.amazonaws.com/athena/JDBC/3.2.1/LICENSE.txt) 
+  [3.2.0 license](https://aws-analytics-downloads-us-gov-west-1.s3.us-gov-west-1.amazonaws.com/athena/JDBC/3.2.0/LICENSE.txt) 
+  [3.1.0 license](https://aws-analytics-downloads-us-gov-west-1.s3.us-gov-west-1.amazonaws.com/athena/JDBC/3.1.0/LICENSE.txt) 
+  [3.0.0 license](https://aws-analytics-downloads-us-gov-west-1.s3.us-gov-west-1.amazonaws.com/athena/JDBC/3.0.0/LICENSE.txt) 

## ODBC driver download links
<a name="govcloud-athena-odbc-driver-download-links"></a>

Use the links in this section to download the latest ODBC 2.x driver for Athena.

### Linux
<a name="_linux"></a>


| Driver version | Download link | 
| --- | --- | 
| ODBC 2.4.0.0 for Linux x86\_64 |  [Linux x86\_64 ODBC driver 2.4.0.0](https://aws-analytics-downloads-us-gov-west-1.s3.us-gov-west-1.amazonaws.com/athena/ODBC/v2.4.0.0/Linux/AmazonAthenaODBC-2.4.0.0-x86_64.rpm)  | 

To verify the Linux package, download the following files:
+  [Linux package public key](https://aws-analytics-downloads-us-gov-west-1.s3.us-gov-west-1.amazonaws.com/athena/ODBC/v2.4.0.0/Linux/public_key.pem) 
+  [Linux package signature](https://aws-analytics-downloads-us-gov-west-1.s3.us-gov-west-1.amazonaws.com/athena/ODBC/v2.4.0.0/Linux/signature.bin) 

### macOS
<a name="_macos"></a>


| Driver version | Download link | 
| --- | --- | 
| ODBC 2.4.0.0 for macOS |  [macOS ODBC driver 2.4.0.0](https://aws-analytics-downloads-us-gov-west-1.s3.us-gov-west-1.amazonaws.com/athena/ODBC/v2.4.0.0/Mac/AmazonAthenaODBC-2.4.0.0-macos11-universal.pkg)  | 

### Windows
<a name="_windows"></a>


| Driver version | Download link | 
| --- | --- | 
| ODBC 2.4.0.0 for Windows amd64 |  [Windows amd64 ODBC driver 2.4.0.0](https://aws-analytics-downloads-us-gov-west-1.s3.us-gov-west-1.amazonaws.com/athena/ODBC/v2.4.0.0/Windows/AmazonAthenaODBC-2.4.0.0-windows-amd64.msi)  | 

### Licenses
<a name="_licenses"></a>
+  [AWS license](https://aws-analytics-downloads-us-gov-west-1.s3.us-gov-west-1.amazonaws.com/athena/ODBC/v2.4.0.0/LICENSE.txt) 

## Previous versions of the Athena ODBC 2.x driver
<a name="odbc-v2-driver-previous-versions"></a>

We highly recommend that you use the latest version of the ODBC 2.x driver. The latest version of the driver contains the most recent improvements and fixes. Use an older version only if your application experiences incompatibilities with the latest version.

### Linux
<a name="connect-with-odbc-linux-previous"></a>


| Driver version | Download link | 
| --- | --- | 
| ODBC 2.2.0.1 for Linux 64-bit |  [Linux 64 bit ODBC driver 2.2.0.1](https://aws-analytics-downloads-us-gov-west-1.s3.us-gov-west-1.amazonaws.com/athena/ODBC/v2.2.0.1/Linux/AmazonAthenaODBC-2.2.0.1-x86_64.rpm)  | 
| ODBC 2.2.0.0 for Linux 64-bit |  [Linux 64 bit ODBC driver 2.2.0.0](https://aws-analytics-downloads-us-gov-west-1.s3.us-gov-west-1.amazonaws.com/athena/ODBC/v2.2.0.0/Linux/AmazonAthenaODBC-2.2.0.0-x86_64.rpm)  | 
| ODBC 2.1.0.0 for Linux 64-bit |  [Linux 64 bit ODBC driver 2.1.0.0](https://aws-analytics-downloads-us-gov-west-1.s3.us-gov-west-1.amazonaws.com/athena/ODBC/v2.1.0.0/Linux/AmazonAthenaODBC-2.1.0.0.rpm)  | 
| ODBC 2.0.6.0 for Linux 64-bit |  [Linux 64 bit ODBC driver 2.0.6.0](https://aws-analytics-downloads-us-gov-west-1.s3.us-gov-west-1.amazonaws.com/athena/ODBC/v2.0.6.0/Linux/AmazonAthenaODBC-2.0.6.0.rpm)  | 
| ODBC 2.0.5.1 for Linux 64-bit |  [Linux 64 bit ODBC driver 2.0.5.1](https://aws-analytics-downloads-us-gov-west-1.s3.us-gov-west-1.amazonaws.com/athena/ODBC/v2.0.5.1/Linux/AmazonAthenaODBC-2.0.5.1.rpm)  | 
| ODBC 2.0.5.0 for Linux 64-bit |  [Linux 64 bit ODBC driver 2.0.5.0](https://aws-analytics-downloads-us-gov-west-1.s3.us-gov-west-1.amazonaws.com/athena/ODBC/v2.0.5.0/Linux/AmazonAthenaODBC-2.0.5.0.rpm)  | 
| ODBC 2.0.4.0 for Linux 64-bit |  [Linux 64 bit ODBC driver 2.0.4.0](https://aws-analytics-downloads-us-gov-west-1.s3.us-gov-west-1.amazonaws.com/athena/ODBC/v2.0.4.0/Linux/AmazonAthenaODBC-2.0.4.0.rpm)  | 
| ODBC 2.0.3.0 for Linux 64-bit |  [Linux 64 bit ODBC driver 2.0.3.0](https://aws-analytics-downloads-us-gov-west-1.s3.us-gov-west-1.amazonaws.com/athena/ODBC/v2.0.3.0/Linux/AmazonAthenaODBC-2.0.3.0.rpm)  | 
| ODBC 2.0.2.2 for Linux 64-bit |  [Linux 64 bit ODBC driver 2.0.2.2](https://aws-analytics-downloads-us-gov-west-1.s3.us-gov-west-1.amazonaws.com/athena/ODBC/v2.0.2.2/Linux/AmazonAthenaODBC-2.0.2.2.rpm)  | 

### macOS
<a name="connect-with-odbc-macos-previous"></a>


| Driver version | Download link | 
| --- | --- | 
| ODBC 2.2.0.1 for macOS Universal |  [macOS Universal ODBC driver 2.2.0.1](https://aws-analytics-downloads-us-gov-west-1.s3.us-gov-west-1.amazonaws.com/athena/ODBC/v2.2.0.1/Mac/AmazonAthenaODBC-2.2.0.1-macos11-universal.pkg)  | 
| ODBC 2.2.0.0 for macOS Universal |  [macOS Universal ODBC driver 2.2.0.0](https://aws-analytics-downloads-us-gov-west-1.s3.us-gov-west-1.amazonaws.com/athena/ODBC/v2.2.0.0/Mac/AmazonAthenaODBC-2.2.0.0-macos11-universal.pkg)  | 
| ODBC 2.1.0.0 for macOS 64-bit (ARM) |  [macOS 64 bit ODBC driver 2.1.0.0 (ARM)](https://aws-analytics-downloads-us-gov-west-1.s3.us-gov-west-1.amazonaws.com/athena/ODBC/v2.1.0.0/Mac/AmazonAthenaODBC-2.1.0.0_arm.pkg)  | 
| ODBC 2.1.0.0 for macOS 64-bit (Intel) |  [macOS 64 bit ODBC driver 2.1.0.0 (Intel)](https://aws-analytics-downloads-us-gov-west-1.s3.us-gov-west-1.amazonaws.com/athena/ODBC/v2.1.0.0/Mac/AmazonAthenaODBC-2.1.0.0_x86.pkg)  | 
| ODBC 2.0.6.0 for macOS 64-bit (ARM) |  [macOS 64 bit ODBC driver 2.0.6.0 (ARM)](https://aws-analytics-downloads-us-gov-west-1.s3.us-gov-west-1.amazonaws.com/athena/ODBC/v2.0.6.0/Mac/AmazonAthenaODBC-2.0.6.0_arm.pkg)  | 
| ODBC 2.0.6.0 for macOS 64-bit (Intel) |  [macOS 64 bit ODBC driver 2.0.6.0 (Intel)](https://aws-analytics-downloads-us-gov-west-1.s3.us-gov-west-1.amazonaws.com/athena/ODBC/v2.0.6.0/Mac/AmazonAthenaODBC-2.0.6.0_x86.pkg)  | 
| ODBC 2.0.5.1 for macOS 64-bit (ARM) |  [macOS 64 bit ODBC driver 2.0.5.1 (ARM)](https://aws-analytics-downloads-us-gov-west-1.s3.us-gov-west-1.amazonaws.com/athena/ODBC/v2.0.5.1/Mac/AmazonAthenaODBC-2.0.5.1_arm.pkg)  | 
| ODBC 2.0.5.1 for macOS 64-bit (Intel) |  [macOS 64 bit ODBC driver 2.0.5.1 (Intel)](https://aws-analytics-downloads-us-gov-west-1.s3.us-gov-west-1.amazonaws.com/athena/ODBC/v2.0.5.1/Mac/AmazonAthenaODBC-2.0.5.1_x86.pkg)  | 
| ODBC 2.0.5.0 for macOS 64-bit (ARM) |  [macOS 64 bit ODBC driver 2.0.5.0 (ARM)](https://aws-analytics-downloads-us-gov-west-1.s3.us-gov-west-1.amazonaws.com/athena/ODBC/v2.0.5.0/Mac/AmazonAthenaODBC-2.0.5.0_arm.pkg)  | 
| ODBC 2.0.5.0 for macOS 64-bit (Intel) |  [macOS 64 bit ODBC driver 2.0.5.0 (Intel)](https://aws-analytics-downloads-us-gov-west-1.s3.us-gov-west-1.amazonaws.com/athena/ODBC/v2.0.5.0/Mac/AmazonAthenaODBC-2.0.5.0_x86.pkg)  | 
| ODBC 2.0.4.0 for macOS 64-bit (ARM) |  [macOS 64 bit ODBC driver 2.0.4.0 (ARM)](https://aws-analytics-downloads-us-gov-west-1.s3.us-gov-west-1.amazonaws.com/athena/ODBC/v2.0.4.0/Mac/AmazonAthenaODBC-2.0.4.0_arm.pkg)  | 
| ODBC 2.0.4.0 for macOS 64-bit (Intel) |  [macOS 64 bit ODBC driver 2.0.4.0 (Intel)](https://aws-analytics-downloads-us-gov-west-1.s3.us-gov-west-1.amazonaws.com/athena/ODBC/v2.0.4.0/Mac/AmazonAthenaODBC-2.0.4.0_x86.pkg)  | 
| ODBC 2.0.3.0 for macOS 64-bit (ARM) |  [macOS 64 bit ODBC driver 2.0.3.0 (ARM)](https://aws-analytics-downloads-us-gov-west-1.s3.us-gov-west-1.amazonaws.com/athena/ODBC/v2.0.3.0/Mac/AmazonAthenaODBC-2.0.3.0_arm.pkg)  | 
| ODBC 2.0.3.0 for macOS 64-bit (Intel) |  [macOS 64 bit ODBC driver 2.0.3.0 (Intel)](https://aws-analytics-downloads-us-gov-west-1.s3.us-gov-west-1.amazonaws.com/athena/ODBC/v2.0.3.0/Mac/AmazonAthenaODBC-2.0.3.0_x86.pkg)  | 
| ODBC 2.0.2.2 for macOS 64-bit (ARM) |  [macOS 64 bit ODBC driver 2.0.2.2 (ARM)](https://aws-analytics-downloads-us-gov-west-1.s3.us-gov-west-1.amazonaws.com/athena/ODBC/v2.0.2.2/Mac/AmazonAthenaODBC-2.0.2.2_arm.pkg)  | 
| ODBC 2.0.2.2 for macOS 64-bit (Intel) |  [macOS 64 bit ODBC driver 2.0.2.2 (Intel)](https://aws-analytics-downloads-us-gov-west-1.s3.us-gov-west-1.amazonaws.com/athena/ODBC/v2.0.2.2/Mac/AmazonAthenaODBC-2.0.2.2_x86.pkg)  | 

### Windows
<a name="connect-with-odbc-windows-previous"></a>


| Driver version | Download link | 
| --- | --- | 
| ODBC 2.2.0.1 for Windows 64-bit |  [Windows 64 bit ODBC driver 2.2.0.1](https://aws-analytics-downloads-us-gov-west-1.s3.us-gov-west-1.amazonaws.com/athena/ODBC/v2.2.0.1/Windows/AmazonAthenaODBC-2.2.0.1-windows-amd64.msi)  | 
| ODBC 2.2.0.0 for Windows 64-bit |  [Windows 64 bit ODBC driver 2.2.0.0](https://aws-analytics-downloads-us-gov-west-1.s3.us-gov-west-1.amazonaws.com/athena/ODBC/v2.2.0.0/Windows/AmazonAthenaODBC-2.2.0.0-windows-amd64.msi)  | 
| ODBC 2.1.0.0 for Windows 64-bit |  [Windows 64 bit ODBC driver 2.1.0.0](https://aws-analytics-downloads-us-gov-west-1.s3.us-gov-west-1.amazonaws.com/athena/ODBC/v2.1.0.0/Windows/AmazonAthenaODBC-2.1.0.0.msi)  | 
| ODBC 2.0.6.0 for Windows 64-bit |  [Windows 64 bit ODBC driver 2.0.6.0](https://aws-analytics-downloads-us-gov-west-1.s3.us-gov-west-1.amazonaws.com/athena/ODBC/v2.0.6.0/Windows/AmazonAthenaODBC-2.0.6.0.msi)  | 
| ODBC 2.0.5.1 for Windows 64-bit |  [Windows 64 bit ODBC driver 2.0.5.1](https://aws-analytics-downloads-us-gov-west-1.s3.us-gov-west-1.amazonaws.com/athena/ODBC/v2.0.5.1/Windows/AmazonAthenaODBC-2.0.5.1.msi)  | 
| ODBC 2.0.5.0 for Windows 64-bit |  [Windows 64 bit ODBC driver 2.0.5.0](https://aws-analytics-downloads-us-gov-west-1.s3.us-gov-west-1.amazonaws.com/athena/ODBC/v2.0.5.0/Windows/AmazonAthenaODBC-2.0.5.0.msi)  | 
| ODBC 2.0.4.0 for Windows 64-bit |  [Windows 64 bit ODBC driver 2.0.4.0](https://aws-analytics-downloads-us-gov-west-1.s3.us-gov-west-1.amazonaws.com/athena/ODBC/v2.0.4.0/Windows/AmazonAthenaODBC-2.0.4.0.msi)  | 
| ODBC 2.0.3.0 for Windows 64-bit |  [Windows 64 bit ODBC driver 2.0.3.0](https://aws-analytics-downloads-us-gov-west-1.s3.us-gov-west-1.amazonaws.com/athena/ODBC/v2.0.3.0/Windows/AmazonAthenaODBC-2.0.3.0.msi)  | 
| ODBC 2.0.2.2 for Windows 64-bit |  [Windows 64 bit ODBC driver 2.0.2.2](https://aws-analytics-downloads-us-gov-west-1.s3.us-gov-west-1.amazonaws.com/athena/ODBC/v2.0.2.2/Windows/AmazonAthenaODBC-2.0.2.2.msi)  | 
| ODBC 2.0.2.1 for Windows 64-bit |  [Windows 64 bit ODBC driver 2.0.2.1](https://aws-analytics-downloads-us-gov-west-1.s3.us-gov-west-1.amazonaws.com/athena/ODBC/v2.0.2.1/Windows/AmazonAthenaODBC-2.0.2.1.msi)  | 
| ODBC 2.0.2.0 for Windows 64-bit |  [Windows 64 bit ODBC driver 2.0.2.0](https://aws-analytics-downloads-us-gov-west-1.s3.us-gov-west-1.amazonaws.com/athena/ODBC/v2.0.2.0/Windows/AmazonAthenaODBC-2.0.2.0.msi)  | 
| ODBC 2.0.1.1 for Windows 64-bit |  [Windows 64 bit ODBC driver 2.0.1.1](https://aws-analytics-downloads-us-gov-west-1.s3.us-gov-west-1.amazonaws.com/athena/ODBC/v2.0.1.1/Windows/AmazonAthenaODBC-2.0.1.1.msi)  | 
| ODBC 2.0.1.0 for Windows 64-bit |  [Windows 64 bit ODBC driver 2.0.1.0](https://aws-analytics-downloads-us-gov-west-1.s3.us-gov-west-1.amazonaws.com/athena/ODBC/v2.0.1.0/Windows/AmazonAthenaODBC-2.0.1.0.msi)  | 

### Licenses
<a name="odbc-v2-license-previous"></a>
+  [ODBC 2.2.0.1 license](https://aws-analytics-downloads-us-gov-west-1.s3.us-gov-west-1.amazonaws.com/athena/ODBC/v2.2.0.1/LICENSE.txt) 
+  [ODBC 2.2.0.0 license](https://aws-analytics-downloads-us-gov-west-1.s3.us-gov-west-1.amazonaws.com/athena/ODBC/v2.2.0.0/LICENSE.txt) 
+  [ODBC 2.1.0.0 license](https://aws-analytics-downloads-us-gov-west-1.s3.us-gov-west-1.amazonaws.com/athena/ODBC/v2.1.0.0/LICENSE.txt) 
+  [ODBC 2.0.6.0 license](https://aws-analytics-downloads-us-gov-west-1.s3.us-gov-west-1.amazonaws.com/athena/ODBC/v2.0.6.0/LICENSE.txt) 
+  [ODBC 2.0.5.1 license](https://aws-analytics-downloads-us-gov-west-1.s3.us-gov-west-1.amazonaws.com/athena/ODBC/v2.0.5.1/LICENSE.txt) 
+  [ODBC 2.0.5.0 license](https://aws-analytics-downloads-us-gov-west-1.s3.us-gov-west-1.amazonaws.com/athena/ODBC/v2.0.5.0/LICENSE.txt) 
+  [ODBC 2.0.4.0 license](https://aws-analytics-downloads-us-gov-west-1.s3.us-gov-west-1.amazonaws.com/athena/ODBC/v2.0.4.0/LICENSE.txt) 
+  [ODBC 2.0.3.0 license](https://aws-analytics-downloads-us-gov-west-1.s3.us-gov-west-1.amazonaws.com/athena/ODBC/v2.0.3.0/LICENSE.txt) 
+  [ODBC 2.0.2.2 license](https://aws-analytics-downloads-us-gov-west-1.s3.us-gov-west-1.amazonaws.com/athena/ODBC/v2.0.2.2/LICENSE.txt) 
+  [ODBC 2.0.2.1 license](https://aws-analytics-downloads-us-gov-west-1.s3.us-gov-west-1.amazonaws.com/athena/ODBC/v2.0.2.1/LICENSE.txt) 
+  [ODBC 2.0.2.0 license](https://aws-analytics-downloads-us-gov-west-1.s3.us-gov-west-1.amazonaws.com/athena/ODBC/v2.0.2.0/LICENSE.txt) 
+  [ODBC 2.0.1.1 license](https://aws-analytics-downloads-us-gov-west-1.s3.us-gov-west-1.amazonaws.com/athena/ODBC/v2.0.1.1/LICENSE.txt) 
+  [ODBC 2.0.1.0 license](https://aws-analytics-downloads-us-gov-west-1.s3.us-gov-west-1.amazonaws.com/athena/ODBC/v2.0.1.0/LICENSE.txt) 

## Documentation
<a name="govcloud-athena-docs"></a>
+  [Amazon Athena documentation](https://docs.aws.amazon.com/athena/latest/ug/what-is.html) 

## Export-controlled content
<a name="govcloud-athena-itar"></a>

For AWS Services architected within the AWS GovCloud (US) Regions, the following list explains how certain components of data may leave the AWS GovCloud (US) Regions in the normal course of the service offerings. The list can be used as a guide to help meet applicable customer compliance obligations. Data not included in the following list remains within the AWS GovCloud (US) Regions.
+ Amazon Athena metadata is not permitted to contain export-controlled data. This metadata includes:
  + Database Name
  + Table Name
  + Partitions
  + Query Names
  + Query Strings