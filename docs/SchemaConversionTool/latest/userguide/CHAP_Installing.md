# Installing AWS Schema Conversion Tool

You can install AWS SCT on the following operating systems:

- Microsoft Windows 10
- Fedora Linux 36 and higher
- Ubuntu Linux 18 and higher

###### To install AWS SCT

1. Download the compressed file that contains the AWS SCT installer, using the
   link for your operating system. All compressed files have a .zip extension. When
   you extract the AWS SCT installer file, it will be in the appropriate format
   for your operating system.
   - [Microsoft Windows](https://s3.amazonaws.com/publicsctdownload/Windows/aws-schema-conversion-tool-1.0.latest.zip "https://s3.amazonaws.com/publicsctdownload/Windows/aws-schema-conversion-tool-1.0.latest.zip")
   - [Ubuntu Linux (.deb)](https://s3.amazonaws.com/publicsctdownload/Ubuntu/aws-schema-conversion-tool-1.0.latest.zip "https://s3.amazonaws.com/publicsctdownload/Ubuntu/aws-schema-conversion-tool-1.0.latest.zip")
   - [Fedora Linux (.rpm)](https://s3.amazonaws.com/publicsctdownload/Fedora/aws-schema-conversion-tool-1.0.latest.zip "https://s3.amazonaws.com/publicsctdownload/Fedora/aws-schema-conversion-tool-1.0.latest.zip")

2. Extract the AWS SCT installer file for your operating system, shown following.

| Operating system  | File name                                                  |
| ----------------- | ---------------------------------------------------------- |
| Fedora Linux      | `aws-schema-conversion-tool-1.0.`build-number`.x86_64.rpm` |
| Microsoft Windows | `AWS Schema Conversion Tool-1.0.`build-number`.msi`        |
| Ubuntu Linux      | `aws-schema-conversion-tool-1.0.`build-number`.deb`        |

3. Run the AWS SCT installer file extracted in the previous step.
   Use the instructions for your operating system,
   shown following.

| Operating system  | Install instructions                                                                                                                                       |
| ----------------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------- |
| Fedora Linux      | Run the following command<br>in the folder that you downloaded the file to:<br>`sudo yum install aws-schema-conversion-tool-1.0.`build-number`.x86_64.rpm` |
| Microsoft Windows | Double-click the file to run the installer.                                                                                                                |
| Ubuntu Linux      | Run the following command<br>in the folder that you downloaded the file to:<br>`sudo dpkg -i aws-schema-conversion-tool-1.0.`build-number`.deb`            |

4. Download the Java Database Connectivity (JDBC) drivers
   for your source and target database engines.
   For instructions and download links, see [Installing JDBC drivers for AWS Schema Conversion Tool](CHAP_Installing.md "CHAP_Installing.md").

Now, you have completed the setup of the AWS SCT application. Double-click the application icon to run AWS SCT.
