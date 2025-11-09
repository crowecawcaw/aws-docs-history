AWS Mainframe Modernization Service (Managed Runtime Environment experience) is no longer open to new customers. For
capabilities similar to AWS Mainframe Modernization Service (Managed Runtime Environment experience) explore AWS Mainframe Modernization Service (Self-Managed
Experience). Existing customers can continue to use the service as normal. For more information, see [AWS Mainframe Modernization
availability change](mainframe-modernization-availability-change.md "mainframe-modernization-availability-change.md").

# M2DFUTIL batch utility

M2DFUTIL is a JCL utility program that provides backup, restore, delete, and copy functions
on datasets, similar to the support provided by the mainframe ADRDSSU utility. This program
retains many of the SYSIN parameters from ADRDSSU, which streamlines the process to migrate to
this new utility.

###### Topics

- [Supported platforms](#m2dfutil-platforms "#m2dfutil-platforms")
- [Platform requirements](#m2dfutil-platform "#m2dfutil-platform")
- [Planned future support](#m2udfutil-future-support "#m2udfutil-future-support")
- [Asset locations](#mdfutil-assets "#mdfutil-assets")
- [Configure M2DFUTIL or AWS Mainframe Modernization runtime on Amazon EC2 (including
  AppStream 2.0)](#mdfutil-dependencies "#mdfutil-dependencies")
- [General syntax](#mdfutil-syntax "#mdfutil-syntax")
- [Sample JCLs](#mdfutil-sample-jcls "#mdfutil-sample-jcls")

## Supported platforms

You can use M2DFUTIL on any of the following platforms:

- Rocket Software (formerly Micro Focus) ES on Windows (64 bit and 32 bit)
- Rocket Software ES on Linux (64 bit)

## Platform requirements

M2DFUTIL depends on calling a script to perform a regular expression test. On Windows, you
must install Windows Services for Linux (WSL) for this script to run.

## Planned future support

Features that are not currently available from the mainframe ADRDSSU utility, but are in the
future scope include:

- M2 Managed
- VSAM
- COPY support for file name renaming
- RENAME support for RESTORE
- Multiple INCLUDE and EXCLUDE
- BY clause for subselecting by DSORG, CREDT, EXPDT
- MWAIT clause to retry enqueue failures
- S3 storage support for DUMP/RESTORE

## Asset locations

The load module for this utility is called `M2DFUTIL.so` on Linux
and `M2DFUTIL.dll` on Windows.
This load module can be found in the following locations:

- Linux: `/opt/aws/m2/microfocus/utilities/64bit`
- Windows (32 bit): `C:\AWS\M2\MicroFocus\Utilities\32bit`
- Windows (64 bit): `C:\AWS\M2\MicroFocus\Utilities\64bit`

The script used for regular expression testing is called `compare.sh`.
This script can be found in the following locations:

- Linux: `/opt/aws/m2/microfocus/utilities/scripts`
- Windows (32 bit): `C:\AWS\M2\MicroFocus\Utilities\scripts`

## Configure M2DFUTIL or AWS Mainframe Modernization runtime on Amazon EC2 (including

AppStream 2.0)

Configure your Enterprise Server region with the following:

- Add the following variables in **[ES-Environment]**
  - `M2DFUTILS_BASE_LOC` - The default location for DUMP output
  - `M2DFUTILS_SCRIPTPATH` - The location of the
    `compare.sh` script documented in **Asset
    Locations**
  - `M2DFUTILS_VERBOSE` - [VERBOSE or NORMAL]. This controls the level of
    detail in the `SYSPRINT` output

- Verify that the load module path is added to the `JES\Configuration\JES Program
Path` setting
- Verify that the scripts in the utilities directory have run permissions. You can add a run
  permission using the `chmod + x <script name>` command, in the Linux
  environment

## General syntax

### DUMP

Provides the ability to copy files from the present cataloged location to a backup location.
This location must currently be a file system.

#### Process

DUMP will perform the following:

1. Create the target location directory.
2. Catalog the target location directory as a PDS member.
3. Determine the files to be included by processing the INCLUDE parameter.
4. Deselect included files by processing the EXCLUDE parameter.
5. Determine if the files being dumped are to be DELETED.
6. Enqueue the files to be processed.
7. Copy the files.
8. Export the copied files cataloged DCB information to a side file in the target location
   to assist with future RESTORE operations.

#### Syntax

```
DUMP
TARGET ( TARGET LOCATION  )    -
INCLUDE ( DSN. )
[ EXCLUDE ( DSN ) ]
[ CANCEL | IGNORE ]
[ DELETE ]
```

#### Required parameters

Following are the required parameters for DUMP:

- `SYSPRINT DD NAME` - To contain additional logging information
- `TARGET` - Target location. It can be either:
  - Full path of the dump location
  - Subdirectory name created in the location defined in the **M2DFUTILS_BASE_LOC** variable

- `INCLUDE` - Either a single named DSNAME or a valid mainframe DSN
  search string
- `EXCLUDE` - Either a single named DSNAME or a valid mainframe DSN
  search string

#### Optional parameters

- CANCEL - Cancel if any error occurs. Files that were processed will be retained
- (Default) IGNORE - Ignore any error and process until end
- DELETE - If no ENQ error occurs, then the file is deleted and is uncataloged

### DELETE

Provides the ability to mass delete and uncatalog files. Files are not backed up.

#### Process

DELETE will perform the following:

1. Determine the files to be included by processing the INCLUDE parameter.
2. Deselect included files by processing the EXCLUDE parameter.
3. Enqueue the files to be processed. Setting the disposition to OLD, DELETE, KEEP.

#### Syntax

```
DELETE
INCLUDE ( DSN )
[ EXCLUDE ( DSN ) ]
[ CANCEL | IGNORE ]
[ DELETE ]
```

#### Required parameters

Following are the required parameters for DELETE:

- `SYSPRINT DD NAME` - To contain additional logging information
- `INCLUDE` - Either a single named DSNAME or a valid mainframe DSN
  search string
- `EXCLUDE` - Either a single named DSNAME or a valid mainframe DSN
  search string

#### Optional parameters

- CANCEL - Cancel if any error occurs. Files that are processed will be retained
- (Default) IGNORE - Ignore any error and process until end

### RESTORE

Provides the ability to restore files previously backed up using DUMP.
Files are restored to the original cataloged location unless RENAME is used to alter the restored DSNAME.

#### Process

RESTORE will perform the following:

1. Validate the source location directory.
2. Determine the files to be included by processing the catalog export file.
3. Deselect included files by processing the EXCLUDE parameter.
4. Enqueue the files to be processed.
5. Catalog files that aren't cataloged based on their export information.
6. If a file is already cataloged and the export catalog information is the same, RESTORE
   will replace the cataloged dataset if the REPLACE option is set.

#### Syntax

```
RESTORE
SOURCE ( TARGET LOCATION )
INCLUDE ( DSN )
[ EXCLUDE ( DSN ) ]
[ CANCEL | IGNORE ]
[ REPLACE]
```

#### Required parameters

Following are the required parameters for RESTORE:

- `SYSPRINT DD NAME` - To contain additional logging information
- `SOURCE` - Source location. It can be either:
  - Full path of the dump location
  - Subdirectory name created in the location defined in the **M2DFUTILS_BASE_LOC** variable

- `INCLUDE` - Either a single named DSNAME or a valid mainframe DSN
  search string
- `EXCLUDE` - Either a single named DSNAME or a valid mainframe DSN
  search string

#### Optional parameters

- CANCEL - Cancel if any error. Files processed retained
- (Default) IGNORE - Ignore any error and process until end
- REPLACE - If the file being restored is already cataloged and the catalog records are the
  same, then replace the cataloged file

## Sample JCLs

**DUMP job**

This job will create a subdirectory called `TESTDUMP`. This is the
default backup location specified by the **M2DFUTILS_BASE_LOC**
variable. It will create a PDS library for this backup called
`M2DFUTILS.TESTDUMP`. The exported catalog data is stored in a line
sequential file in the backup directory called `CATDUMP.DAT`. All files
selected will be copied to this backup directory.

```
//M2DFDMP JOB 'M2DFDMP',CLASS=A,MSGCLASS=X
//STEP001  EXEC PGM=M2DFUTIL
//SYSPRINT DD DSN=TESTDUMP.SYSPRINT,
//        DISP=(NEW,CATLG,DELETE),
//        DCB=(RECFM=LSEQ,LRECL=256)
//SYSIN    DD *
DUMP TARGET(TESTDUMP)               -
     INCLUDE(TEST.FB.FILE*.ABC)     -
 CANCEL
/*
//
```

**DELETE job**

This job will delete all files from the catalog that match the INCLUDE parameter.

```
/M2DFDEL JOB 'M2DFDEL',CLASS=A,MSGCLASS=X
//STEP001  EXEC PGM=M2DFUTIL
//SYSPRINT DD DSN=TESTDEL.SYSPRINT,
//        DISP=(NEW,CATLG,DELETE),
//        DCB=(RECFM=LSEQ,LRECL=256)
//SYSPRINT DD SYSOUT=A
//SYSIN    DD *
  DELETE                               -
     INCLUDE(TEST.FB.FILE*.ABC)        -
 CANCEL
/*
 //
```

**RESTORE job**

This job will restore the files that match the INCLUDE parameter from the
`TESTDUMP` backup location. Files that are cataloged will be replaced if the
cataloged file is the same as the one in the CATDUMP export and the REPLACE option is
specified.

```
//M2DFREST JOB 'M2DFREST',CLASS=A,MSGCLASS=X
//STEP001  EXEC PGM=M2DFUTIL
////SYSPRINT DD DSN=TESTREST.SYSPRINT,
//        DISP=(NEW,CATLG,DELETE),
//        DCB=(RECFM=LSEQ,LRECL=256)
//SYSPRINT DD SYSOUT=A
//SYSIN    DD *
RESTORE SOURCE(TESTDUMP)               -
     INCLUDE(TEST.FB.FILE*.ABC)        -
 IGNORE
 REPLACE
/*
//
```
