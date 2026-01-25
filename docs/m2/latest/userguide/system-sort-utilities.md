AWS Mainframe Modernization Service (Managed Runtime Environment experience) is no longer open to new customers. For
capabilities similar to AWS Mainframe Modernization Service (Managed Runtime Environment experience) explore AWS Mainframe Modernization Service (Self-Managed
Experience). Existing customers can continue to use the service as normal. For more information, see [AWS Mainframe Modernization
availability change](mainframe-modernization-availability-change.md "mainframe-modernization-availability-change.md").

# Sort Utilities

The sort utilities rely on datasets whose reference holds a special meaning for the utility. Hence, all the sort utilities on the modernized side share the same invokation pattern in groovy scripts:

```
mpr.withFileConfigurations(<FILE CONFIGURATIONS DETAILS>...)
   .withParameters(params)
   .runProgram("<SORT UTILITY ALIAS>")
```

where `mpr` is a `MainProgramRunner` instance (see the Scripts calling programs section in [this page](ba-shared-structure.md#ba-shared-structure-run-call "ba-shared-structure.md#ba-shared-structure-run-call")). The sort utilities aliases are given in the sections below.

The `DD` (datasets definitions) entries from the JCL script are modernized as entries in the details of the file configuration which serve as argument to the `mpr.withFileConfigurations()` method. See the samples below for illustrations of that concept.

## SORT/SYNCSORT/ICEMAN

### Purpose

This program emulates various mainframe SORT utilities, used to sort/merge/copy data from datasets, based on provided criteria. The following program aliases can be used (and match the corresponding legacy sort utility name):

- `SORT`
- `SYNCSORT`
- `ICEMAN`

The details about the SORT/MERGE directives found in the control cards and the legacy sort utility features are not given here but should be fetched from the existing relevant legacy platforms documentations.

### Signature

The program does not take any argument but relies on specific datasets references instead:

- The `SYSIN` dataset (a.k.a the "control card") holds the sort/merge control statements
- The optional `SYMNAMES` dataset holds variable substitution directives in the SYSIN content
- The optional `SORTXDUP` or `SORTXSUM` dataset can be used to store duplicate records
- The datasets prefixed with `SORTIN` or `SORTDBIN` hold records to be processed (inputs)
- The `SORTOUT` dataset holds the results from the program (output)
- The `SORTWK` definitions for SORT WORK datasets found in some legacy jobs scripts are ignored (and not represented in the modernized call); sort work data sets will always be dynamically allocated in the modern environment
- The two datasets whose DD starts with `SORTJN` (prefix) contain records that will be concerned by join keys directives (used to join datasets during the sort process)

For instance, considering the following join keys directives:

```
JOINKEYS FILE=F1,FIELDS=(13,5,A)
JOINKEYS FILE=F2,FIELDS=(24,5,A)
```

Here, the join key is of length 5, and starts at:

- position 13 for records in dataset `SORTJNF1` (concatenation of `SORTJN` prefix and file `F1`)
- position 24 for records in dataset `SORTJNF2` (concatenation of `SORTJN` prefix and file `F2`)

### Checks / Errors Handling

- If the input file (`SORTIN`) has a `SHR` disposition but cannot be found, an error message is logged, the program return code is set to 1 and the program run is halted (no sort will happen, no output will be produced)

For the following cases, a `RuntimeException` holding a dedicated message will be thrown:

- If the program invokation requires connection to a database (when `SORTDBIN` dataset is used, not `SORTIN`) but not valid data source could be found
- If the output file (`SORTOUT`) is not properly defined
- If a command found in the control card cannot be understood or is not supported
- If not exactly two input files are provided for a `SORT JOINKEYS` case

### Sample Usage

#### MERGE Sample

Here is a sample `ICEMAN` invokation from a job script snippet:

The control card is inlined and commands to merge fields from the input files (see the `SYSIN` entry)

```
//*
//PASOSO03 EXEC PGM=ICEMAN,REGION=0M
//SORTIN01 DD DSN=input(input809a.data),DISP=SHR,LRECL=10
//SORTIN02 DD DSN=input(input809b.data),DISP=SHR,LRECL=10
//SORTOUT  DD DSN=output(out809.txt),DISP=(,PASS),LRECL=10
//SORTWK01 DD SPACE=(281,(156300,156300),RLSE),AVGREC=U
//SORTWK02 DD SPACE=(281,(156300,156300),RLSE),AVGREC=U
//SYSIN    DD *
   MERGE  FIELDS=(1,6,PD,A,7,2,CH,A)
   END
/*
```

And the matching modernized groovy script snippet -- please note that, as already mentioned, the `SORTWK` entries are not taken into account during the modernization process, and that the inlined control card is exactly matching the legacy control card content.

```
// STEP PASOSO03 - PGM - ICEMAN***************************************************
def stepPASOSO03(Object shell, Map params, Map programResults){
    shell.with {
        if (checkValidProgramResults(programResults)) {
            return execStep("PASOSO03", "ICEMAN", programResults, {
                mpr
                    .withFileConfigurations(new FileConfigurationUtils()
                        .withJobContext(jobContext)
                        .fileSystem("SORTIN01")
                        .path("input(input809a.data)").recordSize(10)
                        .disposition("SHR")
                        .build()
                        .fileSystem("SORTIN02")
                        .path("input(input809b.data)").recordSize(10)
                        .disposition("SHR")
                        .build()
                        .fileSystem("SORTOUT")
                        .path("output(out809.txt)").recordSize(10)
                        .normalTermination("PASS")
                        .build()
                        .fileSystem("SYSIN")
                        .stream(
"""   MERGE  FIELDS=(1,6,PD,A,7,2,CH,A)
   END                                                                          """, getEncoding())
                        .build()
                        .getFileConfigurations())
                        .withParameters(params)
                    .runProgram("ICEMAN")
                })
        }
    }
}
```

#### Simple SORT Sample

A simple legacy SORT step (job script snippet) with inlined control card, picked up from the carddemo sample application:

```
//*********************************************************************
//* CREATE COPY OF TRANSACT FILE WITH CARD NUMBER AND TRAN ID AS KEY
//*********************************************************************
//STEP010  EXEC PGM=SORT
//SORTIN   DD  DISP=SHR,DSN=AWS.M2.CARDDEMO.TRANSACT.VSAM.KSDS
//SYSPRINT DD  SYSOUT=*
//SYSOUT   DD  SYSOUT=*
//SORTOUT  DD  DSN=AWS.M2.CARDDEMO.TRXFL.SEQ,
//             DISP=(NEW,CATLG,DELETE),UNIT=SYSDA,
//             DCB=(LRECL=350,BLKSIZE=3500,RECFM=FB),
//             SPACE=(CYL,(1,1),RLSE)
//SYSIN    DD *
  SORT FIELDS=(263,16,CH,A,1,16,CH,A)
  OUTREC FIELDS=(1:263,16,17:1,262,279:279,50)
/*
```

and the matching modernized groovy script snippet:

```
// STEP STEP010 - PGM - SORT******************************************************
def stepSTEP010(Object shell, Map params, Map programResults){
    shell.with {
        if (checkValidProgramResults(programResults)) {
            return execStep("STEP010", "SORT", programResults, {
                mpr
                    .withFileConfigurations(new FileConfigurationUtils()
                        .withJobContext(jobContext)
                        .bluesam("SORTIN")
                        .dataset("AWS.M2.CARDDEMO.TRANSACT.VSAM.KSDS")
                        .disposition("SHR")
                        .build()
                        .systemOut("SYSPRINT")
                        .output("*")
                        .build()
                        .systemOut("SYSOUT")
                        .output("*")
                        .build()
                        .fileSystem("SORTOUT")
                        .path("AWS.M2.CARDDEMO.TRXFL.SEQ").recordSize(350)
                        .disposition("NEW")
                        .normalTermination("CATLG")
                        .abnormalTermination("DELETE")
                        .build()
                        .fileSystem("SYSIN")
                        .stream(
"""  SORT FIELDS=(263,16,CH,A,1,16,CH,A)
  OUTREC FIELDS=(1:263,16,17:1,262,279:279,50)""", getEncoding())
                        .build()
                        .getFileConfigurations())
                    .withParameters(params)
                    .runProgram("SORT")
                })
        }
    }
}
```

Please note that the inlined control card is used "as-is", without any modification from the legacy control card content.

## ICETOOL

### Purpose

The ICETOOL utility is used to perform multiple operations on datasets in a single job step (data manipulation, sorting and analysis).

The following core operators are being supported:

- `COPY` - Copies data from input to output files
- `SORT` - Sorts data using specified sort cards/criteria
- `SELECT` - Filters and selects specific records based on conditions
- `SPLICE` - Merges/joins data from multiple sources
- `COUNT` - Counts records meeting specified criteria
- `OCCUR` - Analyzes occurrence patterns in data

For the SPLICE operator, the utility will use a multi-threaded approach based on data chunking strategies to ensure an optimized performance.

Details about operators should be fetched from the proper legacy platform documentation.

### Signature

The `ICETOOL` utility does not take any parameter, but relies on specific datasets:

- `TOOLIN` dataset contains the control statements to be processed by the utility
- `TOOLMSG` and `DFSMSG` datasets are not used by the modernized `ICETOOL` utility for now (ignored)
- `IN` is the prefix for input datasets (records to be processed)
- `OUT` is the prefix for output datasets (records resulting from the processing)
- other datasets might be referenced by control statements in the control card

### Checks / Errors Handling

For the following cases, a `RuntimeException` will be thrown with a related message:

- If the operator used in one of the control statements is not supported
- For any operator, if an unsupported directive is provided

### Sample Usage

#### ICETOOL SORT Sample

Here is a legacy jcl sample using ICETOOL for sorting purposes:

- each SORT operator control statement uses a dedicated control card, whose reference is specified through the USING keyword
- all control cards are defined after the `TOOLIN` definition, and are inlined (see `SEL1CNTL` and following `*CNTL` entries)

```
//SAMPLO52 EXEC PGM=ICETOOL,REGION=1024K
//TOOLMSG  DD SYSOUT=*
//DFSMSG   DD SYSOUT=*
//IN1      DD DSN=input(input846a.data),DISP=SHR
//            DCB=(RECFM=F,LRECL=8)
//IN2      DD DSN=input(input846b.data),DISP=SHR
//            DCB=(RECFM=F,LRECL=8)
//OUT1     DD DSN=output(out846a.txt),DISP=(,CATLG)
//            DCB=(RECFM=F,LRECL=8)
//OUT2     DD DSN=output(out846b.txt),DISP=(,CATLG)
//            DCB=(RECFM=V)
//OUT3     DD DSN=output(out846c.txt),DISP=(,CATLG)
//            DCB=(RECFM=V)
//TOOLIN   DD *
  SORT FROM(IN1) TO(OUT1) USING(SEL1)
  SORT FROM(IN2) TO(OUT1) USING(SEL2)
  SORT FROM(IN1) TO(OUT2) USING(SEL3)
  SORT FROM(IN2) TO(OUT2) USING(SEL4)
  SORT FROM(IN1) TO(OUT3) USING(SEL5)
  SORT FROM(IN2) TO(OUT3) USING(SEL6)
/*
//SEL1CNTL DD *
    OPTION COPY
    OUTFIL BUILD=(1,8,JFY=(SHIFT=LEFT,TRAIL=C'*'))
//*
//SEL2CNTL DD *
   OPTION COPY,SKIPREC=1
   OUTFIL BUILD=(1,8,JFY=(SHIFT=LEFT,TRAIL=C'*'))
//*
//SEL3CNTL DD *
    OPTION COPY
    OUTFIL BUILD=(1,8,JFY=(SHIFT=LEFT,TRAIL=C'*')),
    FTOV,VLTRIM=C' '
//*
//SEL4CNTL DD *
    OPTION COPY,SKIPREC=1
    OUTFIL BUILD=(1,8,JFY=(SHIFT=LEFT,TRAIL=C'*')),
    FTOV,VLTRIM=C' '
//*
//SEL5CNTL DD *
    OPTION COPY
    OUTFIL BUILD=(1,8,JFY=(SHIFT=LEFT,TRAIL=C'*')),
    FTOV,VLTRIM=C' '
//*
//SEL6CNTL DD *
    OPTION COPY,SKIPREC=1
    OUTFIL BUILD=(1,7,JFY=(SHIFT=LEFT,TRAIL=C'*')),
    FTOV,VLTRIM=C' '
//*
```

Once modernized, the matching groovy script snippet looks like:

```
// STEP SAMPLO52 - PGM - ICETOOL**************************************************
def stepSAMPLO52(Object shell, Map params, Map programResults){
    shell.with {
        if (checkValidProgramResults(programResults)) {
            return execStep("SAMPLO52", "ICETOOL", programResults, {
                mpr
                    .withFileConfigurations(new FileConfigurationUtils()
                        .withJobContext(jobContext)
                        .systemOut("TOOLMSG")
                        .output("*")
                        .build()
                        .systemOut("DFSMSG")
                        .output("*")
                        .build()
                        .fileSystem("IN1")
                        .path("input(input846a.data)").recordSize(8)
                        .disposition("SHR")
                        .build()
                        .fileSystem("IN2")
                        .path("input(input846b.data)").recordSize(8)
                        .disposition("SHR")
                        .build()
                        .fileSystem("OUT1")
                        .path("output(out846a.txt)").recordSize(8)
                        .normalTermination("CATLG")
                        .build()
                        .fileSystem("OUT2")
                        .path("output(out846b.txt)").rdw(true)
                        .normalTermination("CATLG")
                        .build()
                        .fileSystem("OUT3")
                        .path("output(out846c.txt)").rdw(true)
                        .normalTermination("CATLG")
                        .build()
                        .fileSystem("TOOLIN")
                        .stream(
"""  SORT FROM(IN1) TO(OUT1) USING(SEL1)
  SORT FROM(IN2) TO(OUT1) USING(SEL2)
  SORT FROM(IN1) TO(OUT2) USING(SEL3)
  SORT FROM(IN2) TO(OUT2) USING(SEL4)
  SORT FROM(IN1) TO(OUT3) USING(SEL5)
  SORT FROM(IN2) TO(OUT3) USING(SEL6)               """, getEncoding())
                        .build()
                        .fileSystem("SEL1CNTL")
                        .stream(
"""    OPTION COPY
    OUTFIL BUILD=(1,8,JFY=(SHIFT=LEFT,TRAIL=C'*')) """, getEncoding())
                        .build()
                        .fileSystem("SEL2CNTL")
                        .stream(
"""   OPTION COPY,SKIPREC=1
   OUTFIL BUILD=(1,8,JFY=(SHIFT=LEFT,TRAIL=C'*'))""", getEncoding())
                        .build()
                        .fileSystem("SEL3CNTL")
                        .stream(
"""    OPTION COPY
    OUTFIL BUILD=(1,8,JFY=(SHIFT=LEFT,TRAIL=C'*')),
    FTOV,VLTRIM=C' '""", getEncoding())
                        .build()
                        .fileSystem("SEL4CNTL")
                        .stream(
"""    OPTION COPY,SKIPREC=1
    OUTFIL BUILD=(1,8,JFY=(SHIFT=LEFT,TRAIL=C'*')),
    FTOV,VLTRIM=C' '""", getEncoding())
                        .build()
                        .fileSystem("SEL5CNTL")
                        .stream(
"""    OPTION COPY
    OUTFIL BUILD=(1,8,JFY=(SHIFT=LEFT,TRAIL=C'*')),
    FTOV,VLTRIM=C' '""", getEncoding())
                        .build()
                        .fileSystem("SEL6CNTL")
                        .stream(
"""    OPTION COPY,SKIPREC=1
    OUTFIL BUILD=(1,7,JFY=(SHIFT=LEFT,TRAIL=C'*')),
    FTOV,VLTRIM=C' '""", getEncoding())
                        .build()
                        .getFileConfigurations())
                    .withParameters(params)
                    .runProgram("ICETOOL")
                })
        }
    }
}
```

Notes:

- The inlined control cards are used "as-is"; no transformation whatsoever happened, from the legacy control cards
- `TOOLMSG` and `DFSMSG` are defined in the modernized version, but will be ignored at run time
- Both in legacy and modernized versions, the control cards are defined with the `CNTL` suffix, but referenced without the suffix in the directives from `TOOLIN` dataset: e.g. In `SORT FROM(IN1) TO(OUT1) USING(SEL1)`, the `USING(SEL1)` refers to the `SEL1CNTL` dataset definition

#### ICETOOL COPY Sample

Here is another ICETOOL sample, using the COPY operator. The `TOOLIN` is inlined in the jcl script snippet:

```
//SAMPLO51 EXEC PGM=ICETOOL,REGION=1024K
//TOOLMSG  DD SYSOUT=*
//DFSMSG   DD SYSOUT=*
//IN1      DD DSN=input(input831.data),DISP=SHR
//            DCB=(RECFM=F,LRECL=12)
//OUT1     DD DSN=output(out831a.txt),DISP=OLD
//            DCB=(RECFM=F,LRECL=12)
//OUT2     DD DSN=output(out831b.txt),DISP=OLD
//            DCB=(RECFM=F,LRECL=12)
//TOOLIN   DD *
  COPY FROM(IN1) TO(OUT1,OUT2) USING(SEL1)
/*
//SEL1CNTL DD *
  OPTION COPY
  OUTFIL INCLUDE=(7,2,CH,EQ,C'10')
//*
```

And here is the matching modernized groovy script snippet:

```
// STEP SAMPLO51 - PGM - ICETOOL**************************************************
def stepSAMPLO51(Object shell, Map params, Map programResults){
    shell.with {
        if (checkValidProgramResults(programResults)) {
            return execStep("SAMPLO51", "ICETOOL", programResults, {
                mpr
                    .withFileConfigurations(new FileConfigurationUtils()
                        .withJobContext(jobContext)
                        .systemOut("TOOLMSG")
                        .output("*")
                        .build()
                        .systemOut("DFSMSG")
                        .output("*")
                        .build()
                        .fileSystem("IN1")
                        .path("input(input831.data)").recordSize(12)
                        .disposition("SHR")
                        .build()
                        .fileSystem("OUT1")
                        .path("output(out831a.txt)").recordSize(12)
                        .disposition("OLD")
                        .build()
                        .fileSystem("OUT2")
                        .path("output(out831b.txt)").recordSize(12)
                        .disposition("OLD")
                        .build()
                        .fileSystem("TOOLIN")
                        .stream(
"""  COPY FROM(IN1) TO(OUT1,OUT2) USING(SEL1)
  COPY FROM(IN1) TO(OUT3,OUT4)
  COPY FROM(IN1) TO(OUT4)
  COPY FROM(IN1) TO(OUT5,OUT6)                       """, getEncoding())
                        .build()
                        .fileSystem("SEL1CNTL")
                        .stream(
"""  OPTION COPY
  OUTFIL INCLUDE=(7,2,CH,EQ,C'10')""", getEncoding())
                        .build()
                        .getFileConfigurations())
                    .withParameters(params)
                    .runProgram("ICETOOL")
                })
        }
    }
}
```

## MFSORT

### Purpose

This utility program is intended to mimic the behaviour of the sort utility named MFSORT found on Micro Focus environments (it is usually invoked from the command line or in scripts on legacy environments).

Internally, the program is delegating the actual sort operations to the [SORT/SYNCSORT/ICEMAN](#sort-syncsort-iceman "#sort-syncsort-iceman") utility program.

### Signature

Only the following legacy syntax is being supported: `mfsort take <control card>`

The direct instructions call as `mfsort <instructions>` is NOT supported.

It does not take any argument; the _take_ directive is emulated using a dataset referenced as `TAKE`, that contains the commands for MFSORT to operate.

### Checks / Errors Handling

- If the `TAKE` dataset is missing or invalid, a `RuntimeException` will be thrown
- The [Checks / Errors Handling](#sort-error "#sort-error") apply here as well, given the delegation from MFSORT to SORT

### Sample Usage

The following command invocation shows a sample MFSORT usage:

```
mfsort take TESTSRT1.CTL
```

Here is the matching modernized adapted groovy script snippet:

```
mpr.withFileConfigurations(new FileConfigurationUtils()
.fileSystem("TAKE")
.path("input(TESTSRT1.CTL)")
.build()
.getFileConfigurations())
.withArguments("input") // relative path for use and give files
.runProgram("MFSORT");
```
