AWS Mainframe Modernization Service (Managed Runtime Environment experience) is no longer open to new customers. For
capabilities similar to AWS Mainframe Modernization Service (Managed Runtime Environment experience) explore AWS Mainframe Modernization Service (Self-Managed
Experience). Existing customers can continue to use the service as normal. For more information, see [AWS Mainframe Modernization
availability change](mainframe-modernization-availability-change.md "mainframe-modernization-availability-change.md").

# Add configuration properties for the managed application with AWS Blu Age engine

You can add a file in the `config` folder for your refactored application that will give you access to new features in the AWS Blu Age runtime engine.
You must name this file `user-properties.yml`.
This file doesn’t replace the application definition but extends it.
This topic describes the properties you can include in the `user-properties.yml` file.

###### Note

You can’t change some parameters because they are controlled either by AWS Mainframe Modernization or by the application definition.
All parameters defined in the application definition for your application have priority over the parameters you specify in `user-properties.yml`.

For more information about the structure of refactored applications, see [Structure of AWS Blu Age managed
applications](applications-m2-other-resources-structure.md "applications-m2-other-resources-structure.md").

The following diagram shows where to locate the `user-properties.yml` file within the structure of the AWS Blu Age sample application, PlanetsDemo.

```
PlanetsDemo-v1/
   ├─ config/
   │  ├─ application-PlanetsDemo.yml
   │  ├─ user-properties.yml
   ├─ jics/
   ├─ webapps/
```

## Configuration properties reference

This is the list of available properties. All parameters are optional.

###### Topics

- [Gapwalk application properties](#gapwalk-app-props "#gapwalk-app-props")
- [Gapwalk batchscript properties](#gapwalk-batch-props "#gapwalk-batch-props")
- [Gapwalk Blugen properties](#gapwalk-blugen-props "#gapwalk-blugen-props")
- [Gapwalk CL command properties](#gapwalk-cl-props "#gapwalk-cl-props")
- [Gapwalk CL runner properties](#gapwalk-cl-runner-props "#gapwalk-cl-runner-props")
- [Gapwalk JHDB properties](#gapwalk-jhdb-props "#gapwalk-jhdb-props")
- [Gapwalk JICS properties](#gapwalk-jics-props "#gapwalk-jics-props")
- [Gapwalk runtime properties](#gapwalk-runtime-props "#gapwalk-runtime-props")
- [Gapwalk utility program properties](#gapwalk-utility-props "#gapwalk-utility-props")
- [Other properties](#other-props "#other-props")

### Gapwalk application properties

**bluesam.fileLoading.commitInterval**

Optional. The Blusam commit interval.

Type: number

Default: 100000

**card.encoding**

Optional. Card encoding: to be used with `useControlMVariable`.

Type: string

Default: CP1145

**checkinputfilesize**

Optional. Specifies whether to release a check if the file size is a multiple of record size.

Type: boolean

Default: false

**database.cursor.overflow.allowed**

Optional. Specifies whether to allow the cursor overflow.
Set to `true` to perform a next call on the cursor whatever its position.
Set to `false` to check whether the cursor is at the last position before performing a next call on cursor.
Only enable if cursor is SCROLLABLE (SENSITIVE or INSENSITIVE)

Type: boolean

Default: true

**dataSimplifier.onInvalidNumericData**

Optional. How to react when decoding invalid numeric data.
Allowed values are `reject`, `toleratespaces`, `toleratespaceslowvalues`, `toleratemost`.

Type: string

Default: reject

**defaultKeepExistingFiles**

Optional. Specifies whether to set the dataset default previous value.

Type: boolean

Default: false

**disposition.checkexistence**

Optional. Specifies whether to release a check on file existence for Dataset with DISP SHR or OLD.

Type: boolean

Default: false

**externalSort.threshold**

Optional. The sort threshold: when to switch to external (merge) sort.

Type: string

Default: null

`externalSort.threshold: 12MB`

**blockSizeDefault**

Optional. The default block size to be used for BDW bytes.

Type: number

Default: 32760

`blockSizeDefault: 32760`

**forceHR**

Optional. Specifies whether to use Human Readable SYSPRINT, either on console or file output.

Type: boolean

Default: false

**forcedDate**

Optional. Forces a specific date and time in the database. Use only during development
and testing.

Default: null

`forcedDate: 2022-08-26T12:59:58.123456+01:57`

**frozenDate**

Optional. Freezes the date and time in the database. Use only during development and
testing.

Default: false

`frozenDate: false`

**ims.messages.extendedSize**

Optional. Specifies whether to set the extendedSize on ims messages.

Type: boolean

Default: false

**lockTimeout**

Optional. The timeout in milliseconds of a transaction when unable to acquire a lock within a specified timeframe.

Type: number

Default: 500

**mapTransfo.prefixes**

Optional. List of prefixes to be used when transforming controlM variables. Each one separated by comma.

Type: string

Default: &,@,%%

**query.useConcatCondition**

Optional. Specifies whether key condition is built by key concatenation or not.

Type: boolean

Default: false

**rollbackOnRTE**

Optional. Specifies whether to rollback implicit run unit transaction on runtime exceptions.

Type: boolean

Default: false

**sctThreadLimit**

Optional. The thread limit for triggering scripts.

Type: number

Default: 5

**sqlCodePointShift**

Optional. The sql code point shift.
Shifts the codepoint for control characters that we might encounter when migrating legacy rdbms data to a modern rdbms.
For example, you could specify `384` to match unicode character `\u0180`.

Type: number

Default: 0

**sqlIntegerOverflowAllowed**

Optional. Specifies whether to allow the SQL integer overflow, meaning whether placing larger values in the host variable is allowed.

Type: boolean

Default: false

**stepFailWhenAbend**

Optional. Specifies whether to raise an abend if a step fails or completes execution.

Type: boolean

Default: true

**stopExecutionWhenProgNotFound**

Optional. Specifies whether to stop running if a program isn't found.
If set to `true`, interrupts the run if a program is not found.

Type: boolean

Default: true

**uppercaseUserInput**

Optional. Specifies whether user input must be in uppercase.

Type: boolean

Default: true

**useControlMVariable**

Optional. Specifies whether to use control-M specification for variable replacement.

Type: boolean

Default: false

**jcl.checkpoint.expireTimeout**

Optional. Specifies time duration to retain JCL checkpoints in the persistence provider
or in-memory registry.

Type: number

Default: -1

**jcl.checkpoint.expireTimeoutUnit**

Optional. Specifies time duration unit for the
`jcl.checkpoint.expireTimeout` property. Supported enum
constant values: `java.util.concurrent.TimeUnit`.

Type: string

Default: SECONDS

### Gapwalk batchscript properties

**encoding**

Optional. The encoding used in batchscript projects (not with groovy).
Expects a valid encoding `CP1047`, `IBM930`, `ASCII`, `UTF-8`...

Type: string

Default: ASCII

### Gapwalk Blugen properties

**managers.trancode**

Optional. The dialog manager trancode mapping.
Allows you to map a JICS transaction code to a dialog manager.
Expected format is `trancode1:dialogManager1;trancode2:dialogManager2;`.

Type: string

Default: null

`managers.trancode: OR12:MYDIALOG1`

### Gapwalk CL command properties

**commands-off**

Optional. List of commands to turn off, separated by comma.
Allowed values are `PGM_BASIC`, `RCVMSG`, `SNDRCVF`, `CHGVAR`, `QCLRDTAQ`, `RTVJOBA`, `ADDLFM`, `ADDPFM`, `RCVF`, `OVRDBF`, `DLTOVR`, `CPYF`, `SNDDTAQ`.
Useful when you want to disable or overwrite an existing program.
`PGM_BASIC` is a specific AWS Blu Age Runtime program designed for debugging purposes.

Type: string

Default: null

**spring.datasource.primary.jndi-name**

Optional. The primary Java Naming And Directory Interface (JNDI) datasource.

Type: string

Default: jdbc/primary

**zonedMode**

Optional. The mode for encoding or decoding zoned data types.
Allowed values are `EBCDIC_STRICT` / `EBCDIC_MODIFIED` / `AS400`.

Type: string

Default: EBCDIC_STRICT

### Gapwalk CL runner properties

**cl.configuration.context.encoding**

Optional. The encoding of CL files.
Expects a valid encoding `CP1047`, `IBM930`, `ASCII`, `UTF-8`...

Type: string

Default: CP297

**cl.zonedMode**

Optional. The mode for encoding or decoding control language (CL) commands.
Allowed values are `EBCDIC_STRICT` / `EBCDIC_MODIFIED` / `AS400`.

Type: string

Default: EBCDIC_STRICT

### Gapwalk JHDB properties

**ims.programs**

Optional. List of IMS programs to use.
Separate each parameter with a semicolon (`;`) and each transaction with a comma (`,`).
For example: `ims.programs: PCP008,PCT008;PCP054,PCT054;PCP066,PCT066;PCP068,PCT068;`

Type: string

Default: null

**jhdb.checkpointPath**

Optional. If `jhdb.checkpointPersistence` is not `none` then this parameter allows you to set up the checkpoint persistence path (checkpoint.dat file storage location), all the checkpoints data contained in the registry are serialized and backed up in a file (checkpoint.dat) located in provided folder.
Note that only checkpoint data (scriptId, stepId, database position, and checkpoint area) are concerned by this backup.

Type: string

Default: file:./setup/

**jhdb.checkpointPersistence**

Optional. The checkpoint persistence mode.
Allowed values are `none` / `add` / `end`.
Use `add` to persist checkpoints when a new one is created and added to the registry.
Use `end` to persist checkpoint at server shutdown.
Any other values disable the persistence.
Note that each time a new checkpoint is added to the registry, all the existing checkpoints will be serialized and the file will be erased.
It is not an append to the existing data in the file.
So depending on the number of checkpoints, it can have some effect on performance.

Type: string

Default: none

**jhdb.configuration.context.encoding**

Optional. The JHDB (Java Hierarchical Database) encoding.
Expects a valid encoding string `CP1047`, `IBM930`, `ASCII`, `UTF-8`...

Type: string

Default: CP297

**jhdb.identificationCardData**

Optional. Used to hardcode some "operator identification card data" to the MID field designated by the CARD parameter.

Type: string

Default: ""

**jhdb.lterm**

Optional. Allow you to force a common logical terminal ID in the case of an IMS emulation. If not set then sessionId is used.

Type: string

Default: null

**jhdb.metadata.extrapath**

A configuration parameter that specifies an extra, runtime-specific root folder for psbs and dbds folders.

Type: string

Default: file:./setup/

###### Note

Currently, for deployment constraints, you must copy your dbds and psbs directories in the config directory of your application
or in a subdirectory of the config directory: e.g., config/setup

```
config
|- setup
   |- dbds
   |- psbs
```

and set in application-jhdb.yml

`jhdb.metadata.extrapath: file: ./config/setup/`

**jhdb.navigation.cachenexts**

Optional. The cache duration (in milliseconds) used in hierarchical navigation for an RDBMS.

Type: number

Default: 5000

**jhdb.query.limitJoinUsage**

Optional. Specifies whether to use the limit join usage parameter on RDBMS graphs.

Type: boolean

Default: true

**jhdb.use-db-prefix**

Optional. Specifies whether to enable a database prefix in hierarchical navigation for an RDBMS.

Type: boolean

Default: true

### Gapwalk JICS properties

**jics.data.dataJsonInitLocation**

Optional. Location of the json file prepared by the Analyzer from parsing CSD, and used to initialize the jics database,

Type: string

Default: ""

**jics.db.dataScriptLocation**

Optional. Location of the initJics.sql script, prepared by Analyzer from parsing CSD exports from the mainframe.

Type: string

Default: ""

**jics.db.dataTestQueryLocation**

Optional. Location of a sql script containing a single sql query that is expected to return a count of objects (for example: counting number of records in the jics program table).
If the count equals 0, database will be loaded using the `jics.db.dataScriptLocation` script, otherwise database load will be skipped.

Type: string

Default: ""

**jics.db.ddlScriptLocation**

Optional. The Jics ddl script location. Allows you to initiate the jics database schema using a .sql script.

Type: string

Default: ""

`jics.db.ddlScriptLocation: ./jics/sql/jics.sql`

**jics.db.schemaTestQueryLocation**

Optional. Location of the sql file that should contain a unique query that returns the number of objects in the jics schema (if any).

Type: string

Default: ""

**jics.runUnitLauncherPool.enable**

Optional. Specifies whether to activate the run unit launcher pool in JICS.

Type: boolean

Default: false

**jics.runUnitLauncherPool.size**

Optional. The run unit launcher pool size in JICS.

Type: number

Default: 20

**jics.runUnitLauncherPool.validationInterval**

Optional: The validation interval of the run unit launcher pool in JICS, expressed in milliseconds.

Type: number

Default: 1000

**jics.queues.sqs.region**

Optional. The AWS Region for Amazon SQS, used in JICS.
It is advised to be set the same region of the deployed application for performance, but it is not mandatory.

Type: string

Default: eu-west-1

**jics.xa.agent.timeout**

Optional. Defines the maximum duration for the xa agent responsible for managing distributed transactions, to complete its operations.

Type: number

Default: null

**mq.queues.sqs.region**

Optional. The AWS Region for the Amazon SQS MQ service.

Type: string

Default: eu-west-3

**taskExecutor.allowCoreThreadTimeOut**

Optional. Specifies whether to allow core threads to time out in JCIS. This enables dynamic growing and shrinking even in combination with a non-zero queue (since the max pool size will only grow once the queue is full).

Type: boolean

Default: false

**taskExecutor.corePoolSize**

Optional. When a transaction in a terminal is initiated via a groovy script, a new thread is created.
Use this parameter to setup the core pool size.

Type: number

Default: 5

**taskExecutor.maxPoolSize**

Optional. When a transaction in a terminal is initiated via a groovy script, a new thead is created.
Use this parameter to setup the max pool size (max number of parallel threads).

Type: number

Default: 10

**taskExecutor.queueCapacity**

Optional. When a transaction in a terminal is initiated via a groovy script, a new thead is created.
Use this parameter to setup the queue size. (= maximum number of pending transactions when `taskExecutor.maxPoolSize` is reached)

Type: number

Default: 50

### Gapwalk runtime properties

**cacheMetadata**

Optional. Specifies whether to cache database metadata.

Type: boolean

Default: true

**check-groovy-file**

Optional. Specifies whether to check groovy files content before registering.

Type: boolean

Default: true

**databaseStatistics**

Optional. Specifies whether to allow SQL builders to collect and display statistics information.

Type: boolean

Default: false

**dateTimeFormat**

Optional. The dateTimeFormat describes how to spill database date time timestamp type into data simplifier entities.
Allowed values are `ISO` / `EUR` / `USA` / `LOCAL`

Type: string

Default: ISO

**dbDateFormat**

Optional. The database target date format.

Type: string

Default: yyyy-MM-dd

**dbTimeFormat**

Optional. The database target time format.

Type: string

Default: HH:mm:ss

**dbTimestampFormat**

Optional. The database target timestamp format.

Type: string

Default: yyyy-MM-dd HH:mm:ss.SSSSSS

**fetchSize**

Optional. The fetchSize value for cursors. Use when fetching data using chunks by load/unload utils.

Type: number

Default: 10

**forceDisableSQLTrimStringType**

Optional. Specifies whether to disable trim of all sql string parameters.

Type: boolean

Default: false

**localDateFormat**

Optional. List of local date formats. Separate each format with `|`.

Type: string

**localTimeFormat**

Optional. List of local time formats. Separate each format with `|` .

Type: string

**localTimestampFormat**

Optional. List of local timestamp formats. Separate each format with `|`.

Type: string

Default:

**pgmDateFormat**

Optional. The date time format used in the programs.

Type: string

Default: yyyy-MM-dd

**pgmTimeFormat**

Optional. The time format used for pgm (programs) execution.

Type: string

Default: HH.mm.ss

**pgmTimestampFormat**

Optional. The timestamp format.

Type: string

Default: yyyy-MM-dd-HH.mm.ss.SSSSSS

### Gapwalk utility program properties

**jcl.type**

Optional. `.jcl` file type.
Allowed values are `jcl` / `vse`.
The IDCAMS utility PRINT/REPRO commands return 4 if the file is empty for non-vse jcl.

Type: string

Default: mvs

**listcat.variablelengthpreprocessor.enabled**

Optional. Specifies whether to enable the variable length preprocessor for the LISTCAT command.

Type: boolean

Default: false

**listcat.variablelengthpreprocessor.type**

Optional. The type of objects contained in the listcat file, if you enable `listcat.variablelengthpreprocessor.enabled`.
Allowed values are `rdw` / `bdw`.

Type: string

Default: rdw

**load.batchSize**

Optional. The load utility batch size.

Type: number

Default: 0

**load.format.dbDate**

Optional. The load utility database format to use.

Type: string

Default: yyyy-MM-dd

**load.format.dbTime**

Optional. The load utility database time to use.

Type: string

Default: HH:mm:ss

**load.format.localDate**

Optional. The load utility local date format to use.

Type: string

Default: dd.MM.yyyy|dd/MM/yyyy|yyyy-MM-dd

**load.format.localTime**

Optional. The load utility local time format to use.

Type: string

Default: HH:mm:ss|HH.mm.ss

**load.sqlCodePointShift**

Optional. The SQL code pointshift for load utility.
Runs the shifting characters process. Required when your target database from DB2 is Postgresql.

Type: number

Default: 0

**sysPunchEncoding**

Optional. The syspunch encoding character set. Supported values are `Cp1047` / `ASCII`.

Type: string

Default: ASCII

**treatLargeNumberAsInteger**

Optional. Specifies whether to treat large numbers as `Integer`. They are treated as `BigDecimal` by default.

Type: boolean

Default: false

**unload.chunkSize**

Optional. Chunk size used for unload utility.

Type: number

Default: 0

**unload.columnFiller**

Optional. The unload utility column filler.

Type: string

Default: space

**unload.fetchSize**

Optional. Allows you to tune the fetch size when handling cursors in the unload utility.

Type: number

Default: 0

**unload.format.date**

Optional. If `unload.useDatabaseConfiguration` is enabled, the date format to
use in the unload utility.

Type: string

Default: MM/dd/yyyy

**unload.format.time**

Optional. If `unload.useDatabaseConfiguration` is enabled, the time format to use in the unload utility.

Type: string

Default: HH.mm.ss

**unload.format.timestamp**

Optional. If `unload.useDatabaseConfiguration` is enabled, the timestamp format to use in the unload utility.

Type: string

Default: yyyy-MM-dd-HH.mm.ss.SSSSSS

**unload.nbi.whenNotNull**

Optional. The Null Byte Indicator (nbi) value to add when value from database is not null.

Type: hexadecimal

Default: 00

**unload.nbi.whenNull**

Optional. The Null Byte Indicator (nbi) value to add when value from database is null.

Type: hexadecimal

Default: 6F

**unload.nbi.writeNullIndicator**

Optional. Specifies whether to write out the null indicator in the unload output file.

Type: boolean

Default: false

**unload.sqlCodePointShift**

Optional. The SQL code pointshift for unload utility. Runs the shifting characters process. Required when your target database from DB2 is Postgresql.

Type: number

Default: 0

**unload.useDatabaseConfiguration**

Optional. Specifies whether to use the date or time configuration from application-main.yml in unload utility.

Type: boolean

Default: false

**unload.varCharIsNull**

Optional. Use this parameter in INFTILB program, if set to `true` then all not nullable fields with blank (space) values returns an empty string.

Type: boolean

Default: false

### Other properties

**qtemp.cleanup.threshold.hours**

Optional. To specify when `qtemp.dblog` is enabled. The db partition lifetime (in hours).

Type: number

Default: 0

**qtemp.dblog**

Optional. Whether to enable QTEMP Database logging.

Type: boolean

Default: false

**qtemp.uuid.length**

Optional. The QTEMP unique id length.

Type: number

Default: 9

**quartz.scheduler.stand-by-if-error**

Optional. Specifies whether to trigger job execution if the job scheduler is in standby mode. If true, When enabled job execution is not triggered.

Type: boolean

Default: false

**warmUpCache**

Optional. Specifies whether to load all datacom table data into a warm up cache at server start.

Type: boolean

Default: false
