AWS Mainframe Modernization Service (Managed Runtime Environment experience) will no longer be open to new customers starting on November 7, 2025. If you would like to use the service, please sign up prior to November 7, 2025. For capabilities similar to AWS Mainframe Modernization Service (Managed Runtime Environment experience) explore AWS Mainframe Modernization Service (Self-Managed Experience). Existing customers can continue to use the service as normal. For more information, see
[AWS Mainframe Modernization availability change](mainframe-modernization-availability-change.md "mainframe-modernization-availability-change.md").

# TXT2PDF batch utility

TXT2PDF is a mainframe utility program commonly used to convert a text file to a PDF file.
This utility uses the same source code for TXT2PDF (z/OS freeware). We modified it to run under
the AWS Mainframe Modernization Rocket Software (formerly Micro Focus) runtime environment.

###### Topics

- [Supported platforms](#txt2pdf-platforms "#txt2pdf-platforms")
- [Configure TXT2PDF for AWS Mainframe Modernization Managed](#txt2pdf-configure-managed "#txt2pdf-configure-managed")
- [Configure TXT2PDF for AWS Mainframe Modernization runtime on Amazon EC2 (including AppStream 2.0)](#txt2pdf-configure-customer-infra "#txt2pdf-configure-customer-infra")
- [Sample JCL](#txt2pdf-jcl "#txt2pdf-jcl")
- [Modifications](#txt2pdf-mods "#txt2pdf-mods")
- [References](#txt2pdf-ref "#txt2pdf-ref")

## Supported platforms

You can use TXT2PDF on any of the following platforms:

- AWS Mainframe Modernization Rocket Software Managed
- Rocket Software Runtime (on Amazon EC2)
- All variants of Rocket Enterprise Developer (ED) and Rocket Enterprise Server (ES) products.

## Configure TXT2PDF for AWS Mainframe Modernization Managed

If your migrated applications are running on AWS Mainframe Modernization Managed, configure TXT2PDF as follows.

- Create a REXX EXEC library called `AWS.M2.REXX.EXEC`. Download these
  [REXX modules](https://drm0z31ua8gi7.cloudfront.net/utilities/mf/TXT2PDF/rexx/TXT2PDF_rexx.zip "https://drm0z31ua8gi7.cloudfront.net/utilities/mf/TXT2PDF/rexx/TXT2PDF_rexx.zip") and copy them into the library.
  - `TXT2PDF.rex` - TXT2PDF z/OS freeware (modified)
  - `TXT2PDFD.rex` - TXT2PDF z/OS freeware (unmodified)
  - `TXT2PDFX.rex` - TXT2PDF z/OS freeware (modified)
  - `M2GETOS.rex` - To check the OS type (Windows or Linux)

To test your configuration, see [Sample JCL](#txt2pdf-jcl "#txt2pdf-jcl").

## Configure TXT2PDF for AWS Mainframe Modernization runtime on Amazon EC2 (including AppStream 2.0)

If your migrated applications are running on AWS Mainframe Modernization runtime on Amazon EC2, configure TXT2PDF as follows.

1. Set the Rocket Software environment variable `MFREXX_CHARSET` to the appropriate value,
   such as “`A`" for ASCII data.

###### Important

Entering the wrong value could cause data conversion issues (from EBCDIC to ASCII), making the resulting PDF unreadable or inoperable.
We recommend setting `MFREXX_CHARSET` to match `MF_CHARSET`. 2. Change the [Micro Focus JES Program Path](https://www.microfocus.com/documentation/enterprise-developer/ed80/ED-Eclipse/GUID-BC8A1796-9EDE-48EB-8363-31C9BDE7F96B.html "https://www.microfocus.com/documentation/enterprise-developer/ed80/ED-Eclipse/GUID-BC8A1796-9EDE-48EB-8363-31C9BDE7F96B.html") to include the binary location for batch utilities.
If you need to specify multiple paths, use colons (`:`) to separate paths on Linux and semicolons (`;`) on Windows.

    * Linux: `/opt/aws/m2/microfocus/utilities/64bit`
    * Windows (32bit): `C:\AWS\M2\MicroFocus\Utilities\32bit`
    * Windows (64bit): `C:\AWS\M2\MicroFocus\Utilities\64bit`

3. Create a REXX EXEC library called `AWS.M2.REXX.EXEC``.
   Download these [REXX modules](https://drm0z31ua8gi7.cloudfront.net/utilities/mf/TXT2PDF/rexx/TXT2PDF_rexx.zip "https://drm0z31ua8gi7.cloudfront.net/utilities/mf/TXT2PDF/rexx/TXT2PDF_rexx.zip") and copy them into the library.
   - `TXT2PDF.rex` - TXT2PDF z/OS freeware (modified)
   - `TXT2PDFD.rex` - TXT2PDF z/OS freeware (unmodified)
   - `TXT2PDFX.rex` - TXT2PDF z/OS freeware (modified)
   - `M2GETOS.rex` - To check the OS type (Windows or Linux)

To test your configuration, see [Sample JCL](#txt2pdf-jcl "#txt2pdf-jcl").

## Sample JCL

To test the installation, you can use either of the following sample JCL files.

**TXT2PDF1.jcl**

This sample JCL file uses a DD name for the TXT2PDF conversion.

```
//TXT2PDF1 JOB 'TXT2PDF1',CLASS=A,MSGCLASS=X,TIME=1440
//*
//* Copyright Amazon.com, Inc. or its affiliates.*
//* All Rights Reserved.*
//*
//*-------------------------------------------------------------------**
//* PRE DELETE*
//*-------------------------------------------------------------------**
//*
//PREDEL  EXEC PGM=IEFBR14
//*
//DD01     DD DSN=AWS.M2.TXT2PDF1.PDF.VB,
//            DISP=(MOD,DELETE,DELETE)
//*
//DD02     DD DSN=AWS.M2.TXT2PDF1.PDF,
//            DISP=(MOD,DELETE,DELETE)
//*
//*-------------------------------------------------------------------**
//* CALL TXT2PDF TO CONVERT FROM TEXT TO PDF (VB)*
//*-------------------------------------------------------------------**
//*
//STEP01 EXEC PGM=IKJEFT1B
//*
//SYSEXEC  DD DISP=SHR,DSN=AWS.M2.REXX.EXEC
//*
//INDD     DD *
1THIS IS THE FIRST LINE ON THE PAGE 1
0THIS IS THE THIRD LINE ON THE PAGE 1
-THIS IS THE   6TH LINE ON THE PAGE 1
THIS IS THE   7TH LINE ON THE PAGE 1
+____________________________________ - OVERSTRIKE 7TH LINE
1THIS IS THE FIRST LINE ON THE PAGE 2
0THIS IS THE THIRD LINE ON THE PAGE 2
-THIS IS THE   6TH LINE ON THE PAGE 2
THIS IS THE   7TH LINE ON THE PAGE 2
+____________________________________ - OVERSTRIKE 7TH LINE
/*
//*
//OUTDD    DD DSN=AWS.M2.TXT2PDF1.PDF.VB,
//            DISP=(NEW,CATLG,DELETE),
//            DCB=(LRECL=256,DSORG=PS,RECFM=VB,BLKSIZE=0)
//*
//SYSTSPRT DD SYSOUT=*
//SYSTSIN  DD DDNAME=SYSIN
//*
//SYSIN    DD *
%TXT2PDF BROWSE Y IN DD:INDD +
OUT DD:OUTDD +
CC YES
/*
//*
//*-------------------------------------------------------------------**
//* CONVERT PDF (VB) TO PDF (LSEQ - BYTE STREAM)*
//*-------------------------------------------------------------------**
//*
//STEP02 EXEC PGM=VB2LSEQ
//*
//INFILE   DD DSN=AWS.M2.TXT2PDF1.PDF.VB,DISP=SHR
//*
//OUTFILE  DD DSN=AWS.M2.TXT2PDF1.PDF,
//            DISP=(NEW,CATLG,DELETE),
//            DCB=(LRECL=256,DSORG=PS,RECFM=LSEQ,BLKSIZE=0)
//*
//SYSOUT   DD SYSOUT=*
//*
//
```

**TXT2PDF2.jcl**

This sample JCL uses a DSN name for the TXT2PDF conversion.

```
//TXT2PDF2 JOB 'TXT2PDF2',CLASS=A,MSGCLASS=X,TIME=1440
//*
//* Copyright Amazon.com, Inc. or its affiliates.*
//* All Rights Reserved.*
//*
//*-------------------------------------------------------------------**
//* PRE DELETE*
//*-------------------------------------------------------------------**
//*
//PREDEL  EXEC PGM=IEFBR14
//*
//DD01     DD DSN=AWS.M2.TXT2PDF2.PDF.VB,
//            DISP=(MOD,DELETE,DELETE)
//*
//DD02     DD DSN=AWS.M2.TXT2PDF2.PDF,
//            DISP=(MOD,DELETE,DELETE)
//*
//*-------------------------------------------------------------------**
//* CALL TXT2PDF TO CONVERT FROM TEXT TO PDF (VB)*
//*-------------------------------------------------------------------**
//*
//STEP01 EXEC PGM=IKJEFT1B
//*
//SYSEXEC  DD DISP=SHR,DSN=AWS.M2.REXX.EXEC
//*
//INDD     DD *
1THIS IS THE FIRST LINE ON THE PAGE 1
0THIS IS THE THIRD LINE ON THE PAGE 1
-THIS IS THE   6TH LINE ON THE PAGE 1
THIS IS THE   7TH LINE ON THE PAGE 1
+____________________________________ - OVERSTRIKE 7TH LINE
1THIS IS THE FIRST LINE ON THE PAGE 2
0THIS IS THE THIRD LINE ON THE PAGE 2
-THIS IS THE   6TH LINE ON THE PAGE 2
THIS IS THE   7TH LINE ON THE PAGE 2
+____________________________________ - OVERSTRIKE 7TH LINE
/*
//*
//SYSTSPRT DD SYSOUT=*
//SYSTSIN  DD DDNAME=SYSIN
//*
//SYSIN    DD *
%TXT2PDF BROWSE Y IN DD:INDD +
OUT 'AWS.M2.TXT2PDF2.PDF.VB' +
CC YES
/*
//*
//*-------------------------------------------------------------------**
//* CONVERT PDF (VB) TO PDF (LSEQ - BYTE STREAM)*
//*-------------------------------------------------------------------**
//*
//STEP02 EXEC PGM=VB2LSEQ
//*
//INFILE   DD DSN=AWS.M2.TXT2PDF2.PDF.VB,DISP=SHR
//*
//OUTFILE  DD DSN=AWS.M2.TXT2PDF2.PDF,
//            DISP=(NEW,CATLG,DELETE),
//            DCB=(LRECL=256,DSORG=PS,RECFM=LSEQ,BLKSIZE=0)
//*
//SYSOUT   DD SYSOUT=*
//*
//
```

## Modifications

To make the TXT2PDF program run on the AWS Mainframe Modernization Rocket Software runtime environment, we made the following changes:

- Changes to the source code to ensure compatibility with the Rocket Software REXX runtime
- Changes to ensure that the program can run on both Windows and Linux operating systems
- Modifications to support both EBCDIC and ASCII runtime

## References

TXT2PDF references and source code:

- [Text to PDF converter](https://homerow.net/rexx/txt2pdf/ "https://homerow.net/rexx/txt2pdf/")
- [z/OS Freeware TCP/IP and Mail Tools](http://www.lbdsoftware.com/tcpip.html "http://www.lbdsoftware.com/tcpip.html")
- [TXT2PDF User Reference Guide](http://www.lbdsoftware.com/TXT2PDF-User-Guide.pdf "http://www.lbdsoftware.com/TXT2PDF-User-Guide.pdf")
