AWS Mainframe Modernization Service (Managed Runtime Environment experience) is no longer open to new customers. For
capabilities similar to AWS Mainframe Modernization Service (Managed Runtime Environment experience) explore AWS Mainframe Modernization Service (Self-Managed
Experience). Existing customers can continue to use the service as normal. For more information, see [AWS Mainframe Modernization
availability change](mainframe-modernization-availability-change.md "mainframe-modernization-availability-change.md").

# M2WAIT batch utility

M2WAIT is a mainframe utility program that enables you to introduce a wait period in your JCL scripts by specifying a time duration in seconds, minutes, or hours.
You can call M2WAIT directly from JCL by passing the time you want to wait as an input parameter.
Internally, the M2WAIT program calls the Rocket Software (formerly Micro Focus) supplied module `C$SLEEP` to wait for a specified time.

###### Note

You can use Micro Focus aliases to replace what you have in your JCL scripts.
For more information, see [JES Alias](https://www.microfocus.com/documentation/enterprise-developer/ed80/ED-Eclipse/GUID-D4206FF9-32C4-43E7-9413-5E7E96AA8092.html "https://www.microfocus.com/documentation/enterprise-developer/ed80/ED-Eclipse/GUID-D4206FF9-32C4-43E7-9413-5E7E96AA8092.html") in the Micro Focus documentation.

###### Topics

- [Supported platforms](#m2wait-platforms "#m2wait-platforms")
- [Configure M2WAIT for AWS Mainframe Modernization Managed](#m2wait-configure-managed "#m2wait-configure-managed")
- [Configure M2WAIT for AWS Mainframe Modernization runtime on Amazon EC2 (including WorkSpaces Applications)](#m2wait-configure-customer-infra "#m2wait-configure-customer-infra")
- [Sample JCL](#m2wait-jcl "#m2wait-jcl")

## Supported platforms

You can use M2WAIT on any of the following platforms:

- AWS Mainframe Modernization Rocket Software (formerly Micro Focus) Managed
- Rocket Software Runtime (on Amazon EC2)
- All variants of Rocket Software Enterprise Developer (ED) and Rocket Software Enterprise Server (ES)
  products.

## Configure M2WAIT for AWS Mainframe Modernization Managed

If your migrated applications are running on AWS Mainframe Modernization Managed, you will need to configure M2WAIT as follows.

- Use the program M2WAIT in your JCL by passing input parameter as shown in [Sample JCL](#m2wait-jcl "#m2wait-jcl").

## Configure M2WAIT for AWS Mainframe Modernization runtime on Amazon EC2 (including WorkSpaces Applications)

If your migrated applications are running on AWS Mainframe Modernization runtime on Amazon EC2, configure M2WAIT as follows.

1. Change the [Micro Focus JES Program Path](https://www.microfocus.com/documentation/enterprise-developer/ed80/ED-Eclipse/GUID-BC8A1796-9EDE-48EB-8363-31C9BDE7F96B.html "https://www.microfocus.com/documentation/enterprise-developer/ed80/ED-Eclipse/GUID-BC8A1796-9EDE-48EB-8363-31C9BDE7F96B.html") to include the binary location for batch utilities.
   If you need to specify multiple paths, use colons (`:`) to separate paths on Linux and semicolons (`;`) on Windows.
   - Linux: `/opt/aws/m2/microfocus/utilities/64bit`
   - Windows (32bit): `C:\AWS\M2\MicroFocus\Utilities\32bit`
   - Windows (64bit): `C:\AWS\M2\MicroFocus\Utilities\64bit`

2. Use the program M2WAIT in your JCL by passing the input parameter as shown in [Sample JCL](#m2wait-jcl "#m2wait-jcl").

## Sample JCL

To test the installation, you can use the `M2WAIT1.jcl` program.

This sample JCL shows how to call M2WAIT and pass it several different durations.

```
//M2WAIT1 JOB 'M2WAIT',CLASS=A,MSGCLASS=X,TIME=1440
//*
//* Copyright Amazon.com, Inc. or its affiliates.*
//* All Rights Reserved.*
//*
//*-------------------------------------------------------------------**
//* Wait for 12 Seconds*
//*-------------------------------------------------------------------**
//*
//STEP01 EXEC PGM=M2WAIT,PARM='S012'
//SYSOUT DD SYSOUT=*
//*
//*-------------------------------------------------------------------**
//* Wait for 0 Seconds (defaulted to 10 Seconds)*
//*-------------------------------------------------------------------**
//*
//STEP02 EXEC PGM=M2WAIT,PARM='S000'
//SYSOUT DD SYSOUT=*
//*
//*-------------------------------------------------------------------**
//* Wait for 1 Minute*
//*-------------------------------------------------------------------**
//*
//STEP03 EXEC PGM=M2WAIT,PARM='M001'
//SYSOUT DD SYSOUT=*
//*
//
```
