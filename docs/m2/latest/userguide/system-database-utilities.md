AWS Mainframe Modernization Service (Managed Runtime Environment experience) is no longer open to new customers. For
capabilities similar to AWS Mainframe Modernization Service (Managed Runtime Environment experience) explore AWS Mainframe Modernization Service (Self-Managed
Experience). Existing customers can continue to use the service as normal. For more information, see [AWS Mainframe Modernization
availability change](mainframe-modernization-availability-change.md "mainframe-modernization-availability-change.md").

# Database Utilities

This section is about database related utilities. On legacy platforms, these programs usually operate on DB2 databases, whereas alternative databases are chosen (AWS Aurora being a popular choice) on modern environments.

## DSNTEP2/DSNTEP4

### DSNTEP2/DSNTEP4 Purpose

The DNSTEP utility executes SQL queries from input datasets and writes results to output datasets. It automatically rewrites legacy SQL queries for modernized target databases (beyond DB2) and supports multiple `SYSIN` dataset types: streams, Blusam datasets, flat files, GDG generations, and datasets concatenations.

### DSNTEP2/DSNTEP4 Signature

The utility takes no arguments and uses two datasets:

- `SYSIN`: Input dataset containing SQL statements
- `SYSPRINT`: Output dataset for query results (`SELECT` queries only)

### DSNTEP2/DSNTEP4 related configuration parameters

The behaviour of the utility is influenced by the following configuration parameters:

- `unload.sqlCodePointShift`
- `unload.noPad`
- `unload.nbi.whenNull`
- `unload.nbi.whenNotNull`
- `unload.useDatabaseConfiguration`
- `unload.format.date`
- `unload.format.time`
- `unload.format.timestamp`
- `hasGraphic`
- `forcedDate`
- `frozenDate`

Please see [Available properties for optional web
applications](ba-runtime-key-value.md#ba-runtime-key-value-web "ba-runtime-key-value.md#ba-runtime-key-value-web") for details about configuring these parameters.

### DSNTEP2/DSNTEP4 Checks / Errors handling

- If, for any reason, an exception occurs during query run, an error message will be logged and a `StopRunUnitException` will be thrown, leading to halt the current run unit.
- If the `SYSIN` is a concatenation of various datasets and any of the datasets is unsupported, a `RuntimeException` will be thrown. Currently, only flat files and GDG generations kinds are supported as parts of a concatenated file, when used as input with DSNTEP2/4.

### DSNTEP2/DSNTEP4 Sample usages

Here is a sample JCL usage of DNSTEP4:

```
//********************************************************************
//* RETRIEVE DATA FROM TABLE AP_JBI7_INVOICE                      *
//********************************************************************
//*
//DSNTEP03 EXEC PGM=DSNTEP4,DYNAMNBR=20
//SYSPRINT DD DSN=output(out012.txt),
//            DISP=SHR,DCB=(RECFM=FB,LRECL=1152)
//SYSIN    DD *
  SELECT * FROM BUR000.AP_JBI7_INVOICE WITH UR;
```

and the matching modernized groovy script snippet:

```
def stepDSNTEP03(Object shell, Map params, Map programResults){
    shell.with {
        if (checkValidProgramResults(programResults)) {
            return execStep("DSNTEP03", "DSNTEP4", programResults, {
                    mpr
                        .withFileConfigurations(new FileConfigurationUtils()
                        .withJobContext(jobContext)
                        .fileSystem("SYSPRINT")
                        .path("output(out012.txt)").recordSize(1152)
                        .disposition("SHR")
                        .build()
                        .fileSystem("SYSIN")
                        .stream(
"""  SELECT * FROM BUR000.AP_JBI7_INVOICE WITH UR;
  """, getEncoding())
                        .build()
                        .getFileConfigurations(fcmap))
                        .withParameters(params)
                    .runProgram("DSNTEP4")
                })
        }
    }
}
```

Please note that the SQL query is provided "as-is" to the DSNTEP2/4 utility, without any modification.

## DSNUTILB

### DSNUTILB Purpose

Database utility for loading, copying, and managing data. Usually operates on legacy DB2 databases; modernized version supports AWS Aurora and other target databases.

### DSNUTILB Signature

By nature, DSNUTILB is rather intended to be called by modernized job scripts.

Takes no arguments; reads commands from `SYSIN` dataset.

Supported commands are:

- `TEMPLATE` (dynamic allocation of datasets)
- `LISTDEF` (group database objects into lists, usable by other commands)
- `COPY` (create copies of database objects)
- `LOAD` (load records into tables)
- `DISCARD` (delete records from tables)

For extra details about the commands, please consult the related proper legacy documentation.

### DSNUTILB related configuration parameters

The behaviour of the utility is influenced by the following configuration parameters:

- `unload.useDatabaseConfiguration`
- `load.format.localDate`
- `load.format.dbDate`
- `load.format.localTime`
- `load.format.dbTime`
- `load.sqlCodePointShift`
- `convertGraphicDataToFullWidth`

Please see [Available properties for optional web
applications](ba-runtime-key-value.md#ba-runtime-key-value-web "ba-runtime-key-value.md#ba-runtime-key-value-web") for details about configuring these parameters.

### DSNUTILB Checks / Errors handling

- If the `SYSIN` dataset does not contain any usable command, a `RuntimeException` will be thrown.
- If any exception occurs during database operations, an error message will be logged, the return code will be set to 8 and a `StopRunUnitException` will be thrown (halting the current run unit).

### DSNUTILB Sample usages

Here is a sample usage of DSNUTILB in a JCL script:

```
//********************************************************************
//* LOAD DATA IN TABLE AP_JBI7_INVOICE.                           *
//********************************************************************
//DSN01  EXEC PGM=DSNUTILB,DYNAMNBR=20
//SYSREC DD  DSN=input(input021.data),
//           DISP=SHR
//           DCB=(RECFM=FB,LRECL=76)
//SYSIN  DD  DSN=input(dsn01.card),
//           DISP=SHR
```

with the commands card content (dsn01.card) -- used to load data into database, from a flat file exported from the legacy platform --:

```
  LOAD         DATA
               INDDN         SYSREC
               RESUME        NO
               LOG           YES
               NOCOPYPEND
               SORTDEVT      SYSDA
               SORTNUM       12
               SORTKEYS      100000
               DISCARDS      0
               INTO TABLE    BUR000.AP_JB17_INVOICE
               WHEN (76:76) = 'L'
 ( IDENTIFIER        POSITION(1:1)        SMALLINT
  ,CUST_ID           POSITION(10)         VARCHAR
                                          NULLIF(39) = '?'
  ,CUST_KD           POSITION(40:43)      CHAR
  ,INVC_AMNT         POSITION(44:49)      NUMERIC
  ,INVC_DAT          POSITION(50:75)      TIMESTAMP EXTERNAL(26)
 )
```

and the matching groovy modernized script snippet:

```
// STEP DSN01 - PGM - DSNUTILB****************************************************
def stepDSN01(Object shell, Map params, Map programResults){
    shell.with {
        if (checkValidProgramResults(programResults)) {
            return execStep("DSN01", "DSNUTILB", programResults, {
                mpr
                    .withFileConfigurations(new FileConfigurationUtils()
                        .withJobContext(jobContext)
                        .fileSystem("SYSREC")
                        .path("input(input021.data)").recordSize(76)
                        .disposition("SHR")
                        .build()
                        .fileSystem("SYSIN")
                        .path("input(dsn01.card)")
                        .disposition("SHR")
                        .build()
                        .getFileConfigurations(fcmap))
                    .withParameters(params)
                    .runProgram("DSNUTILB")
                    })
            }
    }
}
```

## INFUTILB / INZUTILB

### INFUTILB Purpose

INFUTILB/INZUTILB are utility programs used to extract data from databases -- unload -- (DB2 on legacy environment) and convert it to various output formats.

Legacy SQL queries are being automatically adapted on-the-fly to match modern target databases requirements (supported engines: PostgreSQL, Oracle and DB2).

### INFUTILB / INZUTILB Signature

The following program aliases can be used (and match the corresponding legacy sort utilities name):

- `INFUTILB`
- `INZUTILB`

The utility does not take any argument but reads the commands to run from the `SYSIN` dataset (a "control card"). Extracted records from the database are written to the `SYSREC` dataset and the optional `SYSPUNCH` dataset is used to store the control card that can be used to reload data (using other utilities, such as [DSNUTILB](#dsnutilb "#dsnutilb") for instance).

By nature, INFUTILB/INZUTILB are mostly intended to be called by modernized job scripts.

To get details about supported commands, please refer to the proper legacy documentation. The INFUTILB/INZUTILB are using legacy "control cards" datasets "as-is".

### INFUTILB / INZUTILB related configuration parameters

The behaviour of the utility is influenced by the following configuration parameters:

- `unload.sqlCodePointShift`
- `unload.noPad`
- `unload.nbi.whenNull`
- `unload.nbi.whenNotNull`
- `unload.useDatabaseConfiguration`
- `unload.format.date`
- `unload.format.time`
- `unload.format.timestamp`
- `unload.columnFiller`
- `unload.varCharIsNull`
- `unload.DFSIGDCB`
- `hasGraphic`
- `forcedDate`
- `frozenDate`

Please see [Available properties for optional web
applications](ba-runtime-key-value.md#ba-runtime-key-value-web "ba-runtime-key-value.md#ba-runtime-key-value-web") for details about configuring these parameters.

### INFUTILB / INZUTILB Checks / Errors handling

- If the target database is not part of the supported databases engines (PostgreSQL, Oracle and DB2), the program return code will be set to 8 and an `UnsupportedOperationException` will be thrown.
- If the program fails to delete temporary files, the return code will be set to 4, an error message will be logged, but the program run won't be interrupted.
- For all the following cases, the program return code will set to either 4 or 8, and an `AbendException` will be thrown (halting the program run):
  - If the `SYSREC` dataset is not one of the supported kinds (either GDG or File system based dataset); return code 4;
  - If the `SYSPUNCH` dataset is not one of the supported kinds (either GDG or File system based dataset or `DUMMY`); return code 4;
  - If the program is unable to retrieve the `SYSREC` dataset record size (not set or not defined in the datasets catalog) ; return code 8;
  - If the program is unable to retrieve the `SYSPUNCH` dataset record size (not set or not defined in the datasets catalog) ; return code 8;
  - If the query used to create the `SYSREC` dataset contents is not valid (the faulty query will be logged); return code 4;
  - If any exception occurs while fetching data from the database; return code 8;
  - If the `OUTDDN` command is missing in `SYSIN` dataset, for an unload duty; return code 8;
  - If no valid command could be found in `SYSIN` dataset; return code 8;

### INFUTILB / INZUTILB Sample usages

Here is a sample legacy jcl script snippet:

```
//********************************************************************
//* UNLOAD DATA FROM TABLE AP_JBI7_INVOICE.                       *
//********************************************************************
//INF1   EXEC PGM=INFUTILB
//SYSREC DD  DSN=output(out032.data),
//           DISP=SHR
//           DCB=(RECFM=FB,LRECL=90)
//SYSIN  DD  DSN=input(inf12.card),
//           DISP=SHR
```

that uses the following commands card (inf12.card) to unload some data from the database (here, records are selected based on their date):

```
  UNLOAD
      SELECT * FROM BUR000.AP_JB17_INVOICE
      WHERE INVC_DAT >=
      CONCAT(STRIP(CHAR(YEAR(CURRENT DATE - 100 YEAR))),'-01-01-00.00.00.000000')
      AND INVC_DAT >=
      CONCAT('2025-01-01-',CONCAT((CURRENT TIME),'.000000'))
      AND INVC_DAT >= (CURRENT TIMESTAMP - 100 YEAR)
      ORDER BY identifier ASC
        OUTDDN (SYSREC)
        FORMAT DSNTIAUL
```

and the matching groovy script snippet, result of the automated jcl modernization:

```
// STEP INF1 - PGM - INFUTILB*****************************************************
def stepINF1(Object shell, Map params, Map programResults){
    shell.with {
        if (checkValidProgramResults(programResults)) {
            return execStep("INF1", "INFUTILB", programResults, {
                mpr
                    .withFileConfigurations(new FileConfigurationUtils()
                        .withJobContext(jobContext)
                        .fileSystem("SYSREC")
                        .path("output(out032.data)").recordSize(90)
                        .disposition("SHR")
                        .build()
                        .fileSystem("SYSIN")
                        .path("input(inf12.card)")
                        .disposition("SHR")
                        .build()
                        .getFileConfigurations(fcmap))
                    .withParameters(params)
                    .runProgram("INFUTILB")
                })
        }
    }
}
```

## JXHDBCLR

### JXHDBCLR Purpose

JXHDBCLR is a database clearing utility program, found on GS21 platforms, that truncates tables according to provided specific statements found in a commands card.

### JXHDBCLR Signature

It does not take any argument but reads statements from the `SYSIN` dataset (the commands card).

Due to its nature, it is mostly intended to be called by modernized jobs scripts.

### JXHDBCLR related configuration parameters

The behaviour of the utility is influenced by the following configuration parameters:

- `unload.sqlCodePointShift`
- `unload.noPad`
- `unload.nbi.whenNull`
- `unload.nbi.whenNotNull`
- `unload.useDatabaseConfiguration`
- `unload.format.date`
- `unload.format.time`
- `unload.format.timestamp`
- `hasGraphic`
- `forcedDate`
- `frozenDate`

Please see [Available properties for optional web
applications](ba-runtime-key-value.md#ba-runtime-key-value-web "ba-runtime-key-value.md#ba-runtime-key-value-web") for details about configuring these parameters.

### JXHDBCLR Checks / Errors handling

If not tables to truncate can be found, a warning message will be logged, but the program run won't be interrupted.

If some failures occur during tables truncation, the program return code will be set to 4, error messages will be logged, but the program run won't be interrupted.

For any of the following conditions, the program return code will be set to 8 and an `AbendException` will be thrown (halting the program run):

- If the commands card content is empty;
- if any exception occurs during that parsing of processing of the commands;

### JXHDBCLR Sample usages

A sample JXHDBCLR usage with an inlined commands card:

```
//*******************************************************************
//**  Step 1 - JXHDBCLR UTILITY - DBCLEAR TYPE=2/3
//*******************************************************************
//STEP01  EXEC PGM=JXHDBCLR,REGION=256K,PARM='LINECNT=0'
//SYSPRINT DD SYSOUT=*
//SYSIN    DD *
    DBCLEAR    SCHEMA=MUSICSCH,TYPE=3,CHECK=YES
    DEFINE     RANGE=(SINGERDEST)
END
```

and the matching modernized groovy script snippet:

```
// STEP STEP01 - PGM - JXHDBCLR***************************************************
def stepSTEP01(Object shell, Map params, Map programResults){
 shell.with {
        if (checkValidProgramResults(programResults)) {
            return execStep("STEP01", "JXHDBCLR", programResults, {
                mpr
                    .withFileConfigurations(new FileConfigurationUtils()
                        .withJobContext(jobContext)
                        .systemOut("SYSPRINT")
                        .output("*")
                        .build()
                        .fileSystem("SYSIN")
                        .stream(
"""    DBCLEAR    SCHEMA=MUSICSCH,TYPE=3,CHECK=YES
    DEFINE     RANGE=(SINGER)
END""", getEncoding())
                        .build()
                        .getFileConfigurations())
                    .withArguments(getParm("LINECNT=0"))
                    .withParameters(params)
                    .runProgram("JXHDBCLR")
                })
        }
    }
}
```

The inlined card from legacy is kept "as-is", using a stream.
