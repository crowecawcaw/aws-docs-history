AWS Mainframe Modernization Service (Managed Runtime Environment experience) is no longer open to new customers. For
capabilities similar to AWS Mainframe Modernization Service (Managed Runtime Environment experience) explore AWS Mainframe Modernization Service (Self-Managed
Experience). Existing customers can continue to use the service as normal. For more information, see [AWS Mainframe Modernization
availability change](mainframe-modernization-availability-change.md "mainframe-modernization-availability-change.md").

# Datasets Utilities

## BLUESAMCOPY/BLUESAMCREATE/BLUESAMDELETE/BLUESAMCLEAR

These utility programs provide essential dataset manipulation functions on [Blusam datasets](ba-shared-blusam.md "ba-shared-blusam.md").

The `bypassBluesamStatus` flag (stored in JobContext) determines whether to bypass the normal dataset status validation that prevents concurrent access conflicts between online and batch processes.

When `bypassBluesamStatus` is true:

- Skips normal dataset status checks during operations
- Allows access to datasets that might normally be blocked

### BLUESAMCOPY

The BLUESAMCOPY program copies data and metadata structure from one Bluesam dataset to another.

#### Parameters

The BLUESAMCOPY program takes two parameters:

- `FROM=<source dataset name>` - Source dataset to copy from
- `TO=<target dataset name>` - Target dataset to copy to

#### Behavior

- If target dataset doesn't exist, creates it with source's metadata structure
- If target exists, clears it before copying (overwrites existing data)
- The operation proceeds when datasets are not in use by online processes or when `bypassBluesamStatus` is set to true
- Preserves keys, compression, record length, and other metadata properties

#### Error Handling

Returns code 1 if source dataset doesn't exist or if either dataset is in use by online processes.

#### Sample Usage

```
import ...

mpr = applicationContext.getBean("com.netfective.bluage.gapwalk.rt.call.ExecutionController",MainProgramRunner.class)

// copy bluesam dataset
res = mpr.withArguments("FROM=MYBLUESAMTABLE","TO=MYBLUESAMTABLE2").runProgram("BLUESAMCOPY")
```

### BLUESAMCREATE

The BLUESAMCREATE program creates a Bluesam dataset with the specified parameters.

#### Parameters

The BLUESAMCREATE program takes seven parameters:

- `name=<dataset name>` - Dataset to create (mandatory)
- `compress=<true/false>` - Enable compression (optional, default: false)
- `fixedLength=<true/false>` - Fixed length records status (optional, default: false)
- `recordLength=<integer>` - Record length in bytes (optional, default: -1)
- `primaryKey=<key id>,duplicates=<true/false>,fields=<offset,length,...>` - Primary key specification (optional)
- `key=<altkey id>,duplicates=<true/false>,fields=<offset,length,...>` - Alternate key (can have multiple or 0)
- `clearExisting=true/false` - Clear existing dataset (optional default: true)

Specific keys parameters explanations:

- `duplicates`: Whether duplicates value are allowed or not for the given key;
- `fields`: Field positions (1-based) and lengths that define the key;

#### Behavior

- If dataset doesn't exist, creates it with specified parameters
- If dataset exists, clears it if `clearExisting=true`
- The operation proceeds when datasets are not in use by online processes or when `bypassBluesamStatus` is set to `true`

#### Error Conditions

Returns code 0 in all cases.

#### Sample Usage

```
import ...

mpr = applicationContext.getBean("com.netfective.bluage.gapwalk.rt.call.ExecutionController",MainProgramRunner.class)

// create bluesam dataset
mpr.withArguments(
      "name=MYBLUESAMTABLE",
      "compress=FALSE",
      "fixedLength=true",
      "recordLength=54",
      "primaryKey=MYKEY_PK,duplicates=FALSE,fields=0,6")
    .runProgram("BLUESAMCREATE")
```

### BLUESAMDELETE

The BLUESAMDELETE program deletes Bluesam datasets.

#### Parameters

The BLUESAMDELETE program takes 1 or more parameters:

- `<dataset name>` - dataset to delete (can have multiple)

#### Behavior

- The operation proceeds when datasets are not in use by online processes or when `bypassBluesamStatus` is set to `true`
- If dataset exists, delete it

#### Error Conditions

Returns code 0 in all cases.

#### Sample Usage

```
import ...

mpr = applicationContext.getBean("com.netfective.bluage.gapwalk.rt.call.ExecutionController",MainProgramRunner.class)

// delete bluesam datasets
res = mpr.withArguments("MYBLUESAMTABLE","MYBLUESAMTABLE2","MYBLUESAMTABLE3").runProgram("BLUESAMDELETE")
```

### BLUESAMCLEAR

The BLUESAMCLEAR program removes all data from existing datasets while preserving their structure and metadata.

#### Parameters

The BLUESAMCLEAR program takes 1 or more parameters:

- `<dataset name>` - dataset to clear (can have multiple)

#### Behavior

- The operation proceeds when datasets are not in use by online processes or when `bypassBluesamStatus` is set to `true`
- If dataset exists, clear it

#### Error Conditions

Returns code 0 in all cases.

#### Sample Usage

```
import ...

mpr = applicationContext.getBean("com.netfective.bluage.gapwalk.rt.call.ExecutionController",MainProgramRunner.class)

// clear bluesam datasets
res = mpr.withArguments("MYBLUESAMTABLE","MYBLUESAMTABLE2").runProgram("BLUESAMCLEAR")
```

## BPXWDYN

This utility program simulates the z/OS BPXWDYN service for dynamic dataset allocation and deallocation. In modern applications, the file allocations are done in Groovy scripts through `FileConfigurationUtils` builder api. This program allows dynamic management of these allocations without Groovy, which is essential for interactive or conditional file processing in modernized applications.

### Parameters

The legacy argument format is preserved. Expects a single argument containing a 2-byte size header followed by the command string.

command string format for allocation: `ALLOC DD(<name>) DSN('<dsn>') SHR?`

command string format for deallocation: `FREE DD(<name>)`

### Error Handling

- Set error code 0 for success, 1 for failure
- Throws RuntimeException for invalid commands or parameters

### Sample Usage

Here is a Java sample usage of the BPXWDYN program, resulting from a COBOL modernization through AWS transform:

The COBOL code:

```
   01  WK-AREA.
       03  DS-ALLOC-STRING.
           05  DS-LENGTH          PIC S9(004) COMP VALUE 100.
           05  DS-TEXT            PIC  X(100) VALUE
            "ALLOC DD(INFILE) DSN('A.B.JCLLIB(XYZ470)') SHR".
...
           01  RC-RETURN-CODE-AREA.
       03  RC-RETURN-CODE         PIC S9(008) COMP.
...
     CALL  'BPXWDYN'  USING  DS-ALLOC-STRING RETURNING RC-RETURN-CODE.
```

and the matching Java modernization:

```
private final Group dsAllocString = new Group(root).named("DS-ALLOC-STRING");
private final Elementary dsLength = new Elementary(dsAllocString,new BinaryType(4, 0, "STD", false, false, true),Short.valueOf("100")).named("DS-LENGTH");
private final Elementary dsText = new Elementary(dsAllocString,new AlphanumericType(100),"ALLOC DD(INFILE) DSN('A.B.JCLLIB(XYZ470)') SHR").named("DS-TEXT");
...
private final Group root = new Group(getData()).named("RC-RETURN-CODE-AREA");
private final Elementary rcReturnCode = new Elementary(root,new BinaryType(8, 0, "STD", false, false, true)).named("RC-RETURN-CODE");
...
    // Call to utility program  BPXWDYN
ctrl.callSubProgram(
       "BPXWDYN",
        CallBuilder.newInstance().byReference(ctx.getWkArea().getDsAllocStringReference()).getArguments(), ctx);

ctx.getRcReturnCodeArea().setRcReturnCode(NumberUtils.convert(ctx.getProgramReturned()).intValue());
```

## GDGUTILS

GDGs (Generation Data Group) allow applications to work with versioned datasets where each execution creates a new generation while maintaining access to previous generations. This utility creates and manages these dataset generations. This utility is meant to be called in groovy scripts.

### Parameters

parameter order doesn't matter

- `action=<create|refreshevents>` - Operation to perform (mandatory)
- `gdgname=<name>` - Name of the GDG base (mandatory)
- `storageProvider=<filesystem|bluesam>` - Storage backend
- `relativeGeneration=<+integer>` - Relative generation number (e.g., +1 for next)
- `absoluteGeneration=integer` - Absolute generation number
- `recordLength=<integer>` - Record size in the dataset
- `fixedLength=<true/false>` - Specifies that the records have a fixed length in the dataset
- `ownerPath=<File system path>` - The path to store the dataset (filesystem specific, mandatory for that case)
- `compress=<true/false>` - Indicates that the data should stay compressed in memory if data were compressed in the data store (bluesam specific) (Optional, false is the default value)
- `catalog` - Specifies the dataset is to be cataloged (Optional)
- `warmUp` - Indicates that the dataset should be loaded into memory when opened (bluesam specific) (Optional)

relativeGeneration or absoluteGeneration: one of these properties needs to be set.

### Operations

- create: Creates a new GDG dataset generation according to GDG metadata (Handles both filesystem and Bluesam storage)
- refreshevents: Adjusts generation number (Gdg Metadata) without creating new datasets (Used when restarting failed jobs that already created datasets)

### Error Handling

- Set error code 0 for success, 1 for failure
- Throws RuntimeException for invalid commands or parameters

### Sample Usage

Gdg creation operation: the following code create a bluesam generation (43) for `IC.PLI.GDGTEST` dataset

```
import ...

mpr = applicationContext.getBean("com.netfective.bluage.gapwalk.rt.call.ExecutionController",MainProgramRunner.class)

Map params = new Hashtable()
params.put("jobContext", jobContext)
Object[] args =["action=create","gdgname=IC.PLI.GDGTEST","absoluteGeneration=43","storageProvider=bluesam","recordLength=80"]
mpr.withParameters(params).withArguments(args).runProgram("GDGUTILS")
```

Gdg refreshevents operation: only relativeGeneration is relevant for this operation. The following code update the generation number (+1 compared to the current generation) for `IC.PLI.GDGTEST` dataset

```
import ...

mpr = applicationContext.getBean("com.netfective.bluage.gapwalk.rt.call.ExecutionController",MainProgramRunner.class)

Map params = new Hashtable()
params.put("jobContext", jobContext)
Object[] args =["action=refreshevents","gdgname=IC.PLI.GDGTEST","relativeGeneration=1","storageProvider=bluesam"]
mpr.withParameters(params).withArguments(args).runProgram("GDGUTILS")
```

## ICEGENER/SYNCGENR

This utility program mimics the behavior of the z/OS system utility ICEGENER, it copies datasets from input (SYSUT1 dataset) to output (SYSUT2 dataset). This Java implementation provides equivalent functionality supporting both filesystem and Bluesam storage.

### Parameters

No argument

### Required Datasets

- SYSUT1: Input dataset/file
- SYSUT2: Output dataset/file

### Disposition Handling for SYSUT2 Dataset

- NEW: Create new dataset/file
- OLD/SHR: Use existing dataset/file (must exist)
- MOD: Modify, create if missing, append if exists

### Error Handling

- Set error code 0 if copy succeed, 1 if fails
- Throws `IllegalStateException` for invalid usage of Bluseam dataset

### Sample Usage

Here is a Groovy sample usage of the ICEGENER program, resulting from a JCL modernization through AWS transform:

The JCL code:

```
//STEP01    EXEC PGM=ICEGENER
//SYSUT1   DD DSN=POI.INPUT,DISP=SHR
//SYSUT2   DD DSN=POI.OUTPU,
//            DISP=(,CATLG,DELETE),
//            UNIT=3490,
//            DCB=(RECFM=FB,LRECL=100)
/*
```

and the matching Groovy modernization:

```
mpr
    .withFileConfigurations(new FileConfigurationUtils()
        .withJobContext(jobContext)
        .bluesam("SYSUT1")
        .dataset("POI.INPUT")
        .disposition("SHR")
        .build()
        .bluesam("SYSUT2")
        .dataset("POI.OUTPU")
        .normalTermination("CATLG")
        .abnormalTermination("DELETE")
        .build()
        .getFileConfigurations())
    .withParameters(params)
    .runProgram("ICEGENER")
```

## IDCAMS/KQCAMS

This utility program mimics the behavior of the legacy programs IDCAMS, which is a mainframe data management tool used for VSAM (Virtual Storage Access Method) file operations. It processes the legacy IDCAMS commands, maintaining the same syntax as the original SYSIN inputs.

### Context

The program behavior can be configured by two parameters defined in `application-utility-pgm.yml`:

- jclType: JCL type identifier (vse or mvs). The IDCAMS utility PRINT/REPRO commands return 4 if the file is empty for non-vse jcl
- forcedCharsetIdcams: Optional charset override for IDCAMS processing

### Parameters

No argument. Operations are passed through the SYSIN dataset.

### Required Datasets

- SYSIN - Contains IDCAMS command statements
- Input/Output datasets - As referenced in IDCAMS commands (Depending on IDCAMS Statement)

### Key Features / Supported Commands

The details about the IDCAMS commands found in the SYSIN control card are not given here but should be fetched from the existing relevant legacy platforms documentations.

- DEFINE - Creates VSAM clusters and datasets
- DELETE - Removes datasets (supports wildcards)
- REPRO - Copies data between datasets
- PRINT - Displays dataset contents
- VERIFY - Validates dataset existence and integrity
- ALTER - Modifies dataset attributes (renaming)
- ALLOC - Allocates datasets dynamically
- SET - Manages condition codes (LASTCC/MAXCC)
- IF-THEN-ELSE - Conditional command execution
- CANCEL - Terminates job execution

### Error Handling

- Set error code 0 if last command succeeds, -1 if fails
- The SET (LASTCC) commands can be used to override the error code, e.g `SET LASTCC = 0`

### Sample Usage

Here is a Groovy sample usage of the IDCAMS program, resulting from a JCL modernization through AWS transform:

The JCL code:

```
//STEP15 EXEC PGM=IDCAMS
//SYSPRINT DD   SYSOUT=*
//ACCTDATA DD DISP=SHR,
//         DSN=AWS.M2.CARDDEMO.ACCTDATA.PS
//ACCTVSAM DD DISP=SHR,
//         DSN=AWS.M2.CARDDEMO.ACCTDATA.VSAM.KSDS
//SYSIN    DD   *
  REPRO INFILE(ACCTDATA) OUTFILE(ACCTVSAM)
/*
```

and the matching Groovy modernization:

```
mpr.withFileConfigurations(new FileConfigurationUtils()
    .withJobContext(jobContext)
    .systemOut("SYSPRINT")
    .output("*")
    .build()
    .bluesam("ACCTDATA")
    .dataset("AWS.M2.CARDDEMO.ACCTDATA.PS")
    .disposition("SHR")
    .build()
    .bluesam("ACCTVSAM")
    .dataset("AWS.M2.CARDDEMO.ACCTDATA.VSAM.KSDS")
    .disposition("SHR")
    .build()
    .fileSystem("SYSIN")
    .stream("REPRO INFILE(ACCTDATA) OUTFILE(ACCTVSAM)", getEncoding())
    .build()
    .getFileConfigurations())
.withParameters(params)
.runProgram("IDCAMS")
```

## IEBGENER/JSDGENER

This program replicates IEBGENER utility. It's used for copying and manipulating sequential datasets. This implementation extends basic copy functionality by supporting IEBGENER control statements for advanced data processing operations.

### Parameters

No argument. Operations are passed through the SYSIN dataset.

### Required Datasets

- SYSIN: contains control statements (Optional, if not defined, IEBGENER program is identical to ICEGENER)
- SYSUT1: Input dataset/file
- SYSUT2: Output dataset/file

### Key Features / Supported IEBGENER Control Statements

The details about the IEBGENER control statement found in the SYSIN control cards are not given here but should be fetched from the existing relevant legacy platforms documentations.

- GENERATE - defines the overall structure of the data manipulation process by specifying the maximum number of record types (MAXNAME) and fields (MAXFLDS) to be processed
- RECORD - defines the actual layout and content of each record type by specifying the position, length, and format of individual fields that will be either copied from the input dataset or generated with specific values
- LABEL/MEMBER/EXIT are not supported

example:

```
GENERATE MAXNAME=3,MAXFLDS=5
RECORD TYPE=1,
       FIELD=(1,1,CH,VALUE='H'),
       FIELD=(2,30,CH,VALUE='EMPLOYEE REPORT 2024         ')
RECORD TYPE=2,
       FIELD=(1,1,CH,VALUE='D'),
       FIELD=(2,10,CH),              /* Name */
       FIELD=(12,8,CH),             /* Birth date */
       FIELD=(20,8,CH,VALUE='ACTIVE')
RECORD TYPE=3,
       FIELD=(1,1,CH,VALUE='F'),
       FIELD=(2,30,CH,VALUE='END OF REPORT              ')
```

### Error Handling

Set error code 0 if copy succeed, 1 if fails.

### Sample Usage

Here is a Groovy sample usage of the IEBGENER program, resulting from a JCL modernization through AWS transform:

The JCL code:

```
//GENDATA  EXEC PGM=IEBGENER
//SYSUT1   DD DSN=INPUT.EMPLOYEE.DATA,
//            DISP=SHR
//SYSUT2   DD DSN=OUTPUT.EMPLOYEE.FILE,
//            DISP=(NEW,CATLG,DELETE),
//            SPACE=(TRK,(1,1)),
//            DCB=(RECFM=FB,LRECL=80,BLKSIZE=27920)
//SYSIN    DD *
  GENERATE MAXNAME=2,MAXFLDS=5
  RECORD TYPE=1,
         FIELD=(1,1,CH,VALUE='H'),
         FIELD=(2,30,CH,VALUE='EMPLOYEE SALARY REPORT 2024    ')
  RECORD TYPE=2,
         FIELD=(1,1,CH,VALUE='D'),
         FIELD=(2,10,CH),              /* Name from input */
         FIELD=(12,8,CH),             /* Birth date from input */
         FIELD=(20,8,CH),             /* Dept from input */
         FIELD=(28,8,CH)              /* Salary from input */
/*
```

and the matching Groovy modernization:

```
mpr
    .withFileConfigurations(new FileConfigurationUtils()
        .withJobContext(jobContext)
        .systemOut("SYSPRINT")
        .output("*")
        .build()
        .bluesam("SYSUT1")
        .dataset("INPUT.EMPLOYEE.DATA")
        .disposition("SHR")
        .build()
        .bluesam("SYSUT2")
        .dataset("OUTPUT.EMPLOYEE.FILE")
        .disposition("NEW")
        .normalTermination("CATLG")
        .abnormalTermination("DELETE")
        .build()
        .fileSystem("SYSIN")
        .stream( """GENERATE MAXNAME=2,MAXFLDS=5
  RECORD TYPE=1,
         FIELD=(1,1,CH,VALUE='H'),
         FIELD=(2,30,CH,VALUE='EMPLOYEE SALARY REPORT 2024    ')
  RECORD TYPE=2,
         FIELD=(1,1,CH,VALUE='D'),
         FIELD=(2,10,CH),              /* Name from input */
         FIELD=(12,8,CH),             /* Birth date from input */
         FIELD=(20,8,CH),             /* Dept from input */
         FIELD=(28,8,CH)              /* Salary from input */""", getEncoding())
        .build()
        .getFileConfigurations())
    .withParameters(params)
    .runProgram("IEBGENER")
```

## IEFBR14

IEFBR14 is a "do nothing" program that simply returns with a return code of 0 (zero). Its primary use is for dataset allocation, deletion, or catalog maintenance through DD statements, without performing any actual data processing.

### Parameters

No argument

### Error Handling

Set always error code 0.

### Sample Usage

Here is a Groovy sample usage of the IEFBR14 program, resulting from a JCL modernization through AWS transform:

The JCL code to create a new sequential dataset:

```
//STEP1    EXEC PGM=IEFBR14
//NEWSEQ   DD DSN=USER.NEW.SEQ.DATA,
//            DISP=(NEW,CATLG,DELETE),
//            SPACE=(TRK,(10,5)),
//            DCB=(RECFM=FB,LRECL=80,BLKSIZE=27920)
```

and the matching Groovy modernization:

```
mpr
    .withFileConfigurations(new FileConfigurationUtils()
        .withJobContext(jobContext)
        .bluesam("NEWSEQ")
        .dataset("USER.NEW.SEQ.DATA")
        .disposition("NEW")
        .normalTermination("CATLG")
        .abnormalTermination("DELETE")
        .build()
        .getFileConfigurations())
    .withParameters(params)
    .runProgram("IEFBR14")
```

The JCL code to delete a existing dataset:

```
//STEP3    EXEC PGM=IEFBR14
//DELDD    DD DSN=USER.OLD.DATASET,
//            DISP=(OLD,DELETE,DELETE)
```

and the matching Groovy modernization:

```
mpr
    .withFileConfigurations(new FileConfigurationUtils()
        .withJobContext(jobContext)
        .bluesam("DELDD")
        .dataset("USER.OLD.DATASET")
        .disposition("OLD")
        .normalTermination("DELETE")
        .abnormalTermination("DELETE")
        .build()
        .getFileConfigurations())
    .withParameters(params)
    .runProgram("IEFBR14")
```

## JCLBCICS

This program manages datasets status, it enables/disables datasets based on configuration, supporting both individual files and wildcard patterns: it changes STATUS field in JICS table file_table.

### Parameters

No argument. Operations are passed through a `DatasetsConfiguration` object, e.g

```
mpr.withDatasetsConfiguration(new DatasetsConfiguration().close(<Dataset Name>)
```

### Context

The program behavior can be configured by two parameters:

In `application-utility-pgm.yml`:

- `jclbcics.ddname.size` (default is 8): it globally configures dataset name size; if this value is set and dataset name length is less than this value, dataset name will be truncated.

In individual step of the Groovy file calling the program

- `JCLBCICS_OVERRIDDEN_SIZE`: it overrides the global dataset name size:

```
TreeMap stepMapTransfo = [:]
Map stepParams = ["MapTransfo":stepMapTransfo]
stepParams["MapTransfo"]["JCLBCICS_OVERRIDDEN_SIZE"] = '6'
```

If the adjusted dd name size (after truncature) is less than 8, the dd name is considered as a wild card and the function operates for all datasets starting with this dd name.

### Key Features

The supported operations are:

- OPEN: Sets datasets to ENABLED status
- CLOSE: Sets datasets to DISABLED status

These operations are declared through `DatasetsConfiguration` builder class:

```
new DatasetsConfiguration().close(<DD name>).open(<DD name>)
```

DD name: name of dataset, wildcard \* is accepted if dd name size is less than maximum dd name size (8).

### Error Handling

Set error code 0

### Sample Usage

Here is a Groovy sample usage of the JCLBCICS program:

it disables the dataset `UFOLJ3P`, it enables all datasets starting with AX, it enables all datasets starting with DX

```
import com.netfective.bluage.gapwalk.rt.call.MainProgramRunner
import com.netfective.bluage.gapwalk.rt.call.ProgramExecutionResult
import com.netfective.bluage.gapwalk.rt.io.support.DatasetsConfiguration

MainProgramRunner mpr = applicationContext.getBean("com.netfective.bluage.gapwalk.rt.call.ExecutionController",MainProgramRunner.class)
def TreeMap stepMapTransfo = [:]
def Map stepParams = ['MapTransfo':stepMapTransfo]
stepParams['MapTransfo']['JCLBCICS_OVERRIDDEN_SIZE'] = '7'

ProgramExecutionResult res = mpr
.withDatasetsConfiguration(new DatasetsConfiguration().close("UFOLJ3P").open("AX*").open("DX"))
.withParameters(stepParams)
.runProgram("JCLBCICS")
```
