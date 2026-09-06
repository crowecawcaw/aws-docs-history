

# Mainframe source artifacts collection
<a name="transform-app-mainframe-source-artifacts"></a>

This topic outlines the process for collecting mainframe source code and related artifacts to support mainframe modernization initiatives using AWS Transform. Proper collection and preparation of source artifacts are critical for successful analysis, migration planning, and implementation.

## Source code inventory
<a name="transform-app-mainframe-source-artifacts-inventory"></a>

### Application source code types
<a name="transform-app-mainframe-source-artifacts-app-types"></a>

The following application source code types are supported:
+ COBOL programs
+ JCL scripts
+ Assembler programs
+ PL/I programs
+ CICS transactions
+ Natural programs
+ REXX scripts
+ Easytrieve programs
+ Copybooks and includes
+ Proc libraries

### Database assets
<a name="transform-app-mainframe-source-artifacts-db-assets"></a>

The following database assets are supported:
+ DB2 DCLGEN and DDL scripts
+ IMS database definitions (PSBs and DBDs)
+ VSAM file definitions
+ Physical and logical database schemas
+ Database procedures and triggers

### Source code file extensions
<a name="transform-app-mainframe-source-artifacts-extensions"></a>

If you are not sure of the extension, leave it as blank or .txt and AWS Transform classifies it for you.

The following table lists common file extensions for mainframe source artifacts.


**Mainframe source code file extensions**  

| Language/Type | Common extensions | Description | 
| --- | --- | --- | 
| COBOL | .cbl, .cob, .cobol | COBOL source programs | 
| JCL | .jcl | Job Control Language scripts | 
| Assembler | .asm | Assembler language programs | 
| PL/I | .pl1 | PL/I language programs | 
| CICS Definition | .csd | CICS system definition (CSD) | 
| Natural | .nat | Natural programs | 
| REXX | .rex, .rexx | REXX scripts | 
| Easytrieve | .ezt | Easytrieve report programs | 
| Copybooks | .cpy | COBOL copybooks | 
| BMS | .bms | Basic Mapping Support (BMS) | 
| PL/I copybooks | .pl1\_copy | PL/I copybooks | 
| Db2 DCLGEN | .dcl | Db2 declarations generator | 
| Db2 definition | .sql, .ddl | Db2 database definitions | 
| IMS definition | .ims | IMS resource definition data set (IMS Stage 1) | 
| MFS | .mfs | IMS MFS (Message Format Service) | 
| PSB | .psb | IMS PSB (Program Specification Block) | 
| DBD | .dbd | IMS Database Definitions | 
| JCL Proc | .prc, .proc | JCL Procedure libraries | 
| JCL Includes | .inc | JCL Include files | 
| Macros | .mac | Assembler macros | 
| Control Cards | .ctl | JCL Utility control cards | 

## Collection methods
<a name="transform-app-mainframe-source-artifacts-collection"></a>

### Source code extraction
<a name="transform-app-mainframe-source-artifacts-extraction"></a>

Use secure FTP clients (WinSCP/FileZilla) for interactive source code extraction from mainframe PDS libraries.

### DB2 schema extraction
<a name="transform-app-mainframe-source-artifacts-db2"></a>

The DB2 LUW (Linux, UNIX, and Windows) client software includes the `db2look` utility as part of its installation package. The `db2look` utility extracts DDL (Data Definition Language) statements from a DB2 database.

Run the following command:

```
db2look -d {{DATABASE_NAME}} -i {{userid}} -w {{password}} -a -e -m -l -x -f -createdb -printdbcfg -o {{DATABASE_NAME}}.sql
```

The following list describes the parameters:
+ `-d {{DATABASE_NAME}}`: Specifies the name of the database to extract schema from
+ `-i {{userid}}`: User ID for database authentication
+ `-w {{password}}`: Password for database authentication
+ `-a`: Extracts authorization information (grants)
+ `-e`: Extracts all database objects (tables, views, indexes, and so on)
+ `-m`: Extracts statistics and physical characteristics
+ `-l`: Extracts table and column comments
+ `-x`: Extracts explain tables
+ `-f`: Formats the output for better readability
+ `-createdb`: Includes database creation statements
+ `-printdbcfg`: Includes database configuration parameters
+ `-o {{DATABASE_NAME}}.sql`: Specifies the output file name

### Extracting catalog information from mainframe
<a name="transform-app-mainframe-source-artifacts-catalog"></a>

The LISTCAT command in IDCAMS is a utility for retrieving catalog information about datasets on the mainframe. This is useful during mainframe modernization projects to inventory datasets and understand their characteristics.

```
//LSTCATJ JOB 'LISTCAT',CLASS=A,MSGCLASS=X,NOTIFY=&SYSUID
//*
//STEP1 EXEC PGM=IDCAMS
//*
//SYSPRINT DD DSN=AWS.M2.CATALOG.LIST,
//            DISP=(NEW,CATLG,DELETE),
//            SPACE=(CYL,(1,1),RLSE),
//            DCB=(RECFM=FBA,LRECL=133,BLKSIZE=0)
//*
//SYSIN DD *
  LISTCAT ENT('AWS.M2.CARDDEMO.*') ALL
  LISTCAT ENT('SYS1.*') ALL
/*
```

### Extracting CICS definitions
<a name="transform-app-mainframe-source-artifacts-cics"></a>

The IBM-provided DFHCSDUP utility can extract CICS resource definitions from the CICS System Definition (CSD) file.

Use the following JCL to unload existing definitions from the DFHCSD:

```
//CSDEXTJ JOB 'EXTRACT CSD',CLASS=A,MSGCLASS=X,NOTIFY=&SYSUID
//*
//STEP1 EXEC PGM=DFHCSDUP,REGION=0M,
//          PARM='CSD(READONLY),PAGESIZE(60),NOCOMPAT'
//*
//STEPLIB  DD DSN={{your-hlq}}.SDFHLOAD,DISP=SHR
//DFHCSD   DD DSN={{your-hlq}}.DFHCSD,DISP=SHR
//*
//CBDOUT   DD DSN={{your-hlq}}.CSD,
//            DISP=(NEW,CATLG,DELETE),
//            SPACE=(CYL,(1,1),RLSE),
//            DCB=(RECFM=FB,LRECL=80,BLKSIZE=0)
//SYSPRINT DD SYSOUT=*
//SYSIN DD *
  EXTRACT GROUP({{cics-group}}) USERPROGRAM(DFH0CBDC) OBJECTS
/*
```

### Extracting IMS definitions
<a name="transform-app-mainframe-source-artifacts-ims"></a>

To extract IMS definitions, you can generate the IMS Transaction file by using the DFSURDD0 utility. This utility creates stage 1 macro statements that you can use for migration purposes. Only IMS Stage 1 is currently supported.

Use the following JCL to extract IMS definitions:

```
//IMSEXTJ JOB 'IMS STAGE 1',CLASS=A,MSGCLASS=X,NOTIFY=&SYSUID
//*
//STEP1 EXEC PGM=DFSURDD0,MEMLIMIT=12G
//*
//STEPLIB  DD DISP=SHR,DSN={{your-hlq}}.SDFSRESL
//*
//RDDSDSN DD DISP=SHR,DSN={{your-rdds}}
//*
//SYSOUT   DD DSN={{your-hlq}}.STAGE1.IMS,
//            DISP=(NEW,CATLG,DELETE),
//            SPACE=(CYL,(1,1),RLSE),
//            DCB=(RECFM=FB,LRECL=80,BLKSIZE=0)
//SYSPRINT DD SYSOUT=*
//SYSIN DD *
  OUTPUT=MAC
/*
```

### Extracting CA-7 scheduler information
<a name="transform-app-mainframe-source-artifacts-ca7"></a>

CA-7 job schedule information is comprised in LJOB reports. Use the LJOB utility with the `LIST=NODD` parameter to generate the reports on the mainframe. The reports must have a `.ca7` extension. Each report must have ANSI carriage control characters in column 1. You can create a report with carriage control characters in column 1 by specifying `DCB=RECFM=FBA` (or FA) in the JCL used to run the LJOB utility.

For example: `LJOB,JOB=ZBN*,LIST=ALL`

For more information, see the [Broadcom documentation](https://www.broadcom.com/products/mainframe/job-scheduling/workload-automation).

### Extracting SMF data
<a name="transform-app-mainframe-source-artifacts-smf"></a>

System Management Facility (SMF) records provide activity metrics used by AWS Transform to analyze batch job and CICS transaction usage. The following SMF record types are supported: 14, 15, 30 (sub type 5), 64, 102, 110 (sub type 1 with data class 1, 3, and 4).

**Format requirements for SMF records:**
+ Must include record types 30 and 110 (at minimum)
+ Must be in raw binary EBCDIC format with RDW (Record Descriptor Word) bytes included
+ Must be provided as one of the following:
  + A file up to 600 MB compressed in .zip format
  + A file up to 5 GB compressed in .tar.gz or .gz format
+ Must be stored in a separate folder from your source code in Amazon S3

Provide a minimum of 13 months of SMF records to capture annual batch cycles and seasonal patterns that shorter timeframes might miss.

#### Option 1: Extract and sort SMF records
<a name="transform-app-mainframe-source-artifacts-smf-option1"></a>

Use the following sample JCL to extract and sort SMF records:

```
//SMFEXTR  JOB (ACCT),'EXTRACT SMF',CLASS=A,
//             MSGCLASS=X,NOTIFY=&SYSUID
//*-------------------------------------------------------------------*
//* SMF RECORD EXTRACTION TEMPLATE
//* CUSTOMIZE: Job card, dataset names, date range, record types
//*-------------------------------------------------------------------*
//*
//* STEP 1: EXTRACT SMF RECORDS
//*
//EXTRACT  EXEC PGM=IFASMFDP
//SYSPRINT DD SYSOUT=*
//*
//* INPUT: Specify your SMF datasets (MAN files or GDG)
//*
//DUMPIN   DD DISP=SHR,DSN={{SYS1.MAN1}}
//         DD DISP=SHR,DSN={{SYS1.MAN2}}
//         DD DISP=SHR,DSN={{SYS1.MAN3}}
//*
//* OUTPUT: Extracted SMF records
//*
//DUMPOUT  DD DSN={{your.hlq}}.SMF.EXTRACT,
//            DISP=(NEW,CATLG,DELETE),
//            UNIT=SYSDA,
//            SPACE=(CYL,(500,100),RLSE),
//            DCB=(RECFM=VBS,LRECL=32760,BLKSIZE=27998)
//*
//* CONTROL CARDS
//*
//SYSIN    DD *
  INDD(DUMPIN,OPTIONS(DUMP))
  OUTDD(DUMPOUT,TYPE(14,15,30,110))
  DATE({{yyyy/ddd,yyyy/ddd}})
  START(0000)
  END(2359)
/*
//*
//* STEP 2: SORT EXTRACTED RECORDS (OPTIONAL)
//*
//SORT     EXEC PGM=SORT
//SORTIN   DD DISP=SHR,DSN={{your.hlq}}.SMF.EXTRACT
//SORTOUT  DD DSN={{your.hlq}}.SMF.SORTED,
//            DISP=(NEW,CATLG,DELETE),
//            UNIT=SYSDA,
//            SPACE=(CYL,(500,100),RLSE),
//            DCB=(RECFM=VBS,LRECL=32760)
//SORTWK01 DD UNIT=SYSDA,SPACE=(CYL,(50))
//SORTWK02 DD UNIT=SYSDA,SPACE=(CYL,(50))
//SORTWK03 DD UNIT=SYSDA,SPACE=(CYL,(50))
//SYSOUT   DD SYSOUT=*
//SYSPRINT DD SYSOUT=*
//SYSIN    DD *
  SORT FIELDS=(11,4,CH,A,7,4,CH,A,15,4,CH,A),EQUALS
/*
```

Customize the following values in the preceding JCL:

1. Job card: Update account, class, and msgclass

1. DUMPIN: Point to your SMF datasets

1. DUMPOUT: Specify output dataset name and HLQ

1. TYPE: Select record types (14, 15, 30, 110 or others)

1. DATE: Format yyyy/ddd (for example, 2026/055,2026/056)

1. SPACE: Adjust based on expected data volume

1. Remove SORT step if not needed

#### Option 2: Extract SMF data with DFSORT
<a name="transform-app-mainframe-source-artifacts-smf-option2"></a>

You can use DFSORT to consolidate and report historical SMF data. This is helpful if you store your SMF records in a GDG by day or week. The following job uses DFSORT to consolidate SMF records from the SORTIN file and filter based on the records specified in the INCLUDE COND parameter.

```
//EXTRSMF JOB 'EXTRACT SMF RECORDS',CLASS=S,MSGCLASS=H,
// MSGLEVEL=(1,1),REGION=0M,NOTIFY=&SYSUID,TIME=1440
//SORTJES2 EXEC PGM=SORT,REGION=0M
//SYSOUT DD SYSOUT=*
//SORTMSG DD SYSOUT=*
//SORTIN DD DISP=SHR,DSN={{your.hlq}}.SMF.EXTRACT
//SORTOUT DD DSN={{your.hlq}}.SMF.OUTPUT,
// DISP=(MOD,CATLG,DELETE),
// DCB=(BUFNO=20,
// RECFM=VBS,LRECL=32760,BLKSIZE=27998),
// SPACE=(CYL,(1400,900),RLSE)
//SORTWK1 DD UNIT=SYSDA,SPACE=(CYL,(30,50))
//SORTWK2 DD UNIT=SYSDA,SPACE=(CYL,(30,50))
//SORTWK3 DD UNIT=SYSDA,SPACE=(CYL,(30,50))
//SORTWK4 DD UNIT=SYSDA,SPACE=(CYL,(30,50))
//SYSIN DD *
OPTION COPY
INCLUDE COND=(6,1,BI,EQ,X'0E',OR,6,1,BI,EQ,X'0F',OR,
6,1,BI,EQ,X'1E',OR,6,1,BI,EQ,X'40',OR,
6,1,BI,EQ,X'50',OR,6,1,BI,EQ,X'59',OR,
6,1,BI,EQ,X'5C',OR,6,1,BI,EQ,X'65',OR,
6,1,BI,EQ,X'66',OR,6,1,BI,EQ,X'6E')
```

To download the data while keeping the RDW data, you can use an FTP server to receive the extracted file. Make sure the data is transferred in binary format and the RDW option is used so the RDW is included in the data transfer. The following job shows a sample FTP job to transfer this file.

```
//EXTRSMF JOB 'EXTRACT SMF RECORDS',CLASS=A,MSGCLASS=H,
// MSGLEVEL=(1,1),REGION=0M,NOTIFY=&SYSUID,TIME=1440
//STEP1 EXEC PGM=FTP,REGION=2048K
//SYSIN DD *
{{10.10.10.10}}
{{userid}}
{{password}}
type i
LOCSITE RDW
put '{{your.hlq}}.SMF.OUTPUT' {{SMFREQS.SMF}}
quit
```

### Uploading SCRT report
<a name="transform-app-mainframe-source-artifacts-scrt"></a>

You can also upload a Sub-Capacity Reporting Tool (SCRT) report into AWS Transform.

## Application inventory upload
<a name="transform-app-mainframe-source-artifacts-upload"></a>

After you collect all artifacts, complete the following steps:

1. Organize files into subfolders by artifact type (for example, /cobol, /jcl, /copybooks, /db2, /ims, /cics, /ca7).

1. Compress the top-level folder into a single .zip file.

1. Upload the .zip file to the Amazon S3 bucket connected to your AWS Transform workspace.

**Note**  
SMF records must be placed in a separate folder from your source code within the Amazon S3 bucket, and must be in .tar.gz or .gz format.

For detailed instructions on connecting your Amazon S3 bucket to AWS Transform, see [Set up a connector](transform-app-mainframe-workflow.md#transform-app-mainframe-workflow-setup-connector).