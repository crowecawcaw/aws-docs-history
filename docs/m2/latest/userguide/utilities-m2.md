AWS Mainframe Modernization Service (Managed Runtime Environment experience) is no longer open to new customers. For
capabilities similar to AWS Mainframe Modernization Service (Managed Runtime Environment experience) explore AWS Mainframe Modernization Service (Self-Managed
Experience). Existing customers can continue to use the service as normal. For more information, see [AWS Mainframe Modernization
availability change](mainframe-modernization-availability-change.md "mainframe-modernization-availability-change.md").

# Available batch utilities in AWS Mainframe Modernization

Mainframe applications often use batch utility programs to perform specific functions such as sorting data, transferring files using FTP, loading data into databases like DB2, unloading data from databases, and so on.

When you migrate your applications to AWS Mainframe Modernization, you need functionally equivalent replacement utilities that can perform the same tasks as the ones you used on the mainframe.
Some of these utilities might already be available as part of the AWS Mainframe Modernization runtime engines, but we are providing the following replacement utilities:

- M2SFTP - enables secure file transfer using SFTP protocol.
- M2WAIT - waits for a specified amount of time before continuing with the next step in a batch job.
- TXT2PDF - converts text files to PDF format.
- M2DFUTIL - provides backup, restore, delete, and copy functions on data sets that is
  similar to the support provided by the mainframe ADRDSSU utility.
- M2RUNCMD - lets you run Rocket Software (formerly Micro Focus) commands, scripts, and system calls directly from
  JCL.
  We developed these batch utilities based on customer feedback and designed them to provide the same functionality as the mainframe utilities.
  The goal is to make your transition from mainframe to AWS Mainframe Modernization as smooth as possible.

###### Topics

- [Binary Location](#location-utilities "#location-utilities")
- [M2SFTP batch utility](m2sftp.md "m2sftp.md")
- [M2WAIT batch utility](m2wait.md "m2wait.md")
- [TXT2PDF batch utility](txt2pdf.md "txt2pdf.md")
- [M2DFUTIL batch utility](m2dfutil.md "m2dfutil.md")
- [M2RUNCMD batch utility](m2runcmd.md "m2runcmd.md")

## Binary Location

These utilities are preinstalled on the Rocket Enterprise Developer (ED) and Rocket Software (ES) products. You can find them
in the following location for all variants of ED and ES:

- Linux: `/opt/aws/m2/microfocus/utilities/64bit`
- Windows (32 bit): `C:\AWS\M2\MicroFocus\Utilities\32bit`
- Windows (64 bit): `C:\AWS\M2\MicroFocus\Utilities\64bit`
