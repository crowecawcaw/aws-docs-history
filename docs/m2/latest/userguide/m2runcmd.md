AWS Mainframe Modernization Service (Managed Runtime Environment experience) is no longer open to new customers. For
capabilities similar to AWS Mainframe Modernization Service (Managed Runtime Environment experience) explore AWS Mainframe Modernization Service (Self-Managed
Experience). Existing customers can continue to use the service as normal. For more information, see [AWS Mainframe Modernization
availability change](mainframe-modernization-availability-change.md "mainframe-modernization-availability-change.md").

# M2RUNCMD batch utility

You can use M2RUNCMD, a batch utility program, to run Rocket Software (formerly Micro Focus) commands,
scripts, and system calls directly from JCL instead of running them from a terminal or
command prompt. The output from the commands is logged to the batch job's spool log.

###### Topics

- [Supported platforms](#m2runcmd-platforms "#m2runcmd-platforms")
- [Configure M2RUNCMD for AWS Mainframe Modernization runtime on Amazon EC2
  (including AppStream 2.0)](#m2runcmd-configure "#m2runcmd-configure")
- [Sample JCLs](#m2runcmd-sample-jcls "#m2runcmd-sample-jcls")

## Supported platforms

You can use M2RUNCMD on the following platforms:

- Rocket Software Runtime (on Amazon EC2)
- All variants of Rocket Software Enterprise Developer (ED) and Rocket Software Enterprise Server
  (ES) products.

## Configure M2RUNCMD for AWS Mainframe Modernization runtime on Amazon EC2

(including AppStream 2.0)

If your migrated applications are running on AWS Mainframe Modernization runtime on Amazon EC2, configure M2RUNCMD as follows.

- Change the [Micro Focus JES Program Path](https://www.microfocus.com/documentation/enterprise-developer/ed80/ED-Eclipse/index.html?t=GUID-BC8A1796-9EDE-48EB-8363-31C9BDE7F96B.html "https://www.microfocus.com/documentation/enterprise-developer/ed80/ED-Eclipse/index.html?t=GUID-BC8A1796-9EDE-48EB-8363-31C9BDE7F96B.html") to include the binary location for
  batch utilities. If you must specify multiple paths, use colons (:) to separate
  paths on Linux and semicolons (;) on Windows.
  - Linux:
    `/opt/aws/m2/microfocus/utilities/64bit`
  - Windows (32bit):
    `C:\AWS\M2\MicroFocus\Utilities\32bit`
  - Windows (64bit):
    `C:\AWS\M2\MicroFocus\Utilities\64bit`

## Sample JCLs

To test the installation, you can use either of the following sample JCLs.

**RUNSCRL1.jcl**

This sample JCL creates a script and runs it. The first step creates a script
called `/tmp/TEST_SCRIPT.sh` and with content from `SYSUT1`
in-stream data. The second step sets the run permission and runs the script created in
the first step. You can also choose to perform only the second step to run already
existing Rocket Software and system commands.

```
//RUNSCRL1 JOB 'RUN SCRIPT',CLASS=A,MSGCLASS=X,TIME=1440
//*
//*
//*-------------------------------------------------------------------*
//*  CREATE SCRIPT (LINUX)
//*-------------------------------------------------------------------*
//*
//STEP0010 EXEC PGM=IEBGENER
//*
//SYSPRINT DD SYSOUT=*
//SYSIN    DD DUMMY
//*
//SYSUT1   DD *
#!/bin/bash

set -x

## ECHO PATH ENVIRONMNET VARIABLE
echo $PATH

## CLOSE/DISABLE VSAM FILE
casfile -r$ES_SERVER -oc  -ed -dACCTFIL

## OPEN/ENABLE VSAM FILE
casfile -r$ES_SERVER -ooi -ee -dACCTFIL

exit $?
/*
//SYSUT2   DD DSN=&&TEMP,
//            DISP=(NEW,CATLG,DELETE),
//            DCB=(RECFM=LSEQ,LRECL=300,DSORG=PS,BLKSIZE=0)
//*MFE: %PCDSN='/tmp/TEST_SCRIPT.sh'
//*
//*-------------------------------------------------------------------*
//*   RUN SCRIPT (LINUX)                                              *
//*-------------------------------------------------------------------*
//*
//STEP0020 EXEC PGM=RUNCMD
//*
//SYSOUT  DD  SYSOUT=*
//*
//SYSIN   DD *
*RUN SCRIPT
 sh /tmp/TEST_SCRIPT.sh
/*
//
```

**SYSOUT**

The output from the command or script that is run, is written into the
`SYSOUT` log. For each carried out command, it displays the
command, output, and return code.

```
************ CMD Start ************

CMD_STR: sh /tmp/TEST_SCRIPT.sh
CMD_OUT:
+ echo /opt/microfocus/EnterpriseServer/bin:/sbin:/bin:/usr/sbin:/usr/bin
/opt/microfocus/EnterpriseServer/bin:/sbin:/bin:/usr/sbin:/usr/bin
+ casfile -rMYDEV -oc -ed -dACCTFIL
-Return Code:   0
Highest return code:    0
+ casfile -rMYDEV -ooi -ee -dACCTFIL
-Return Code:   8
Highest return code:    8
+ exit 8

CMD_RC=8

************  CMD End  ************
```

**RUNCMDL1.jcl**

This sample JCL uses RUNCMD to run multiple commands.

```
//RUNCMDL1 JOB 'RUN CMD',CLASS=A,MSGCLASS=X,TIME=1440
//*
//*
//*-------------------------------------------------------------------*
//*   RUN SYSTEM COMMANDS                                             *
//*-------------------------------------------------------------------*
//*
//STEP0001 EXEC PGM=RUNCMD
//*
//SYSOUT  DD  SYSOUT=*
//*
//SYSIN   DD *
*LIST DIRECTORY
 ls
*ECHO PATH ENVIRONMNET VARIABLE
 echo $PATH
/*
//
```
