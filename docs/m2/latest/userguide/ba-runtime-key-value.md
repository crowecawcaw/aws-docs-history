

**AWS Mainframe Modernization self-managed experience** is no longer open to new customers. For capabilities similar to AWS Mainframe Modernization self-managed experience, explore capabilities from vendor-direct offerings and from AWS Transform. Existing customers can continue to use the service as normal. For more information, see [AWS Mainframe Modernization availability change](https://docs.aws.amazon.com/m2/latest/userguide/mainframe-modernization-availability-change.html). 

**AWS Mainframe Modernization Service (Managed Runtime Environment experience)** is no longer open to new customers. For capabilities similar to AWS Mainframe Modernization Service (Managed Runtime Environment experience) explore AWS Mainframe Modernization Service (Self-Managed Experience). Existing customers can continue to use the service as normal. For more information, see [AWS Mainframe Modernization availability change](https://docs.aws.amazon.com/m2/latest/userguide/mainframe-modernization-availability-change.html). 

# Enable properties for AWS Transform for mainframe Runtime
<a name="ba-runtime-key-value"></a>

In Spring Boot applications `application-main.yml` is the configuration file in which we define different kinds of properties such as the listening port, database connectivity, and many more. You can use this page to learn about the available properties for AWS Transform for mainframe Runtime and how to enable them.

**Topics**
+ [YML notation](#ba-runtime-key-value-yml)
+ [Quick start / Use cases](#ba-runtime-key-value-use-cases)
+ [Available properties for the main application](#ba-runtime-key-value-main)
+ [Available properties for optional web applications](#ba-runtime-key-value-web)
+ [Available properties for the client application](#ba-runtime-key-value-client)
+ [Configure API access logging](#ba-runtime-api-access-logging)
+ [Configure Distributed Tracing](#ba-runtime-distributed-tracing)

## YML notation
<a name="ba-runtime-key-value-yml"></a>

In the following documentation, a property such as `parent.child1.child2=true` is written as follows in YAML format.

```
 parent:
  child1:
    child2: true
```

## Quick start / Use cases
<a name="ba-runtime-key-value-use-cases"></a>

The following use cases show examples of the applicable keys and values.
+ Default application-main.yml

  ```
  ----
  #### DEFAULT APPLICATION-MAIN.YML FILE      #####
  #### SHOWING USEFUL CONFIGURATION ELEMENTS #####
  #### SHOULD BE OVERRIDDEN AND EXTERNALIZED   #####
  
  #################################
  ##### Logging configuration #####
  #################################
  logging:
    config: classpath:logback-main.xml
    level.org.springframework.beans.factory.support.DefaultListableBeanFactory : WARN
  
  ################################
  ##### Spring configuration #####
  ################################
  spring:
    quartz:
      auto-startup: false
      scheduler-name: Default
      properties:
        org.quartz.threadPool.threadCount: 1
    jta:
      enabled: false
      atomikos.properties.maxTimeout : 600000 
      atomikos.properties.default-jta-timeout : 100000 
    jpa:
  # DISABLE OpenEntityManagerInViewInterceptor   
      open-in-view: false
      # Fix Postgres JPA Error:
      # Method org.postgresql.jdbc.PgConnection.createClob() is not yet implemented.
      properties.hibernate.temp.use_jdbc_metadata_defaults : false
  #####################################
  ##### Jics tables configuration #####
  #####################################
  
      # The dialect should match the jics datasource choice
      database-platform : org.hibernate.dialect.PostgreSQLDialect # org.hibernate.dialect.PostgreSQLDialect, org.hibernate.dialect.SQLServerDialect
      
      # those properties can be used to create and initialize jics tables automatically.
  #    properties:
  #      hibernate:
  #      globally_quoted_identifiers: true
  #        hbm2ddl:
  #           import_files_sql_extractor : org.hibernate.tool.hbm2ddl.MultipleLinesSqlCommandExtractor
  #           import_files : file:./setup/initJics.sql
  #           auto : create
  
  ##########################
  ###### Level 2 cache #####
  ##########################
  #        cache:
  #          use_second_level_cache: true
  #          use_query_cache: true
  #          region:
  #            factory_class: org.hibernate.cache.ehcache.EhCacheRegionFactory
  #      javax:
  #        persistence:
  #          sharedCache:
  #            mode: ENABLE_SELECTIVE
  ##########################
  ###### Redis settings #####
  ##########################
    session:
      store-type: none #redis
      
  # Secret manager configuration for global Redis cache
      aws:
        client:
          gapwalk:
            redis:
              secret: arn:aws:secretsmanager:XXXX
  
  #########################################
  ##### JICS datasource configuration #####
  #########################################
  datasource:
    jicsDs:
      driver-class-name : org.postgresql.Driver # org.postgresql.Driver, com.microsoft.sqlserver.jdbc.SQLServerDriver
      url: jdbc:postgresql://localhost/jics # jdbc:postgresql://localhost:5433/jics, jdbc:sqlserver://localhost\SQLEXPRESS:1434;databasename=jics;
      username: jics
      password: jics
      type : org.postgresql.ds.PGSimpleDataSource # org.postgresql.ds.PGSimpleDataSource, com.microsoft.sqlserver.jdbc.SQLServerDataSource
  
  #####################################################
  ##### Embedded Bluesam datasource configuration #####
  #####################################################
    bluesamDs :
      driver-class-name : org.postgresql.Driver
      url : jdbc:postgresql://localhost/bluesam
      username : bluesam
      password : bluesam
      type : org.postgresql.ds.PGSimpleDataSource
  
  ##########################################
  ##### Embedded Bluesam configuration #####
  ##########################################
  bluesam :
    cache : ehcache
    persistence : pgsql
    ehcache:
      resource-pool:
        size: 4GB
    write-behind:
      enabled: true
    pgsql :
      dataSource : bluesamDs
  
  #########################
  ##### Jics settings #####
  #########################
  rabbitmq.host: localhost
  jics: 
    cache: false #redis
    resource-definitions.store-type: jpa # default value: jpa, other possible value: redis
    
  jics.disableSyncpoint : false
  #jics.initList:
  #jics.parameters.datform: DDMMYY
  #jics.parameters.applid: VELOCITY
  #jics.parameters.sysid: CICS
  #jics.parameters.eibtrmid: TERM
  #jics.parameters.userid: MYUSERID
  #jics.parameters.username: MYUSERNAME
  #jics.parameters.opid: XXX
  #jics.parameters.cwa.length: 0
  #jics.parameters.netname: MYNETNAME
  #jics.parameters.jobname: MJOBNAME
  #jics.parameters.sysname: SYSNAME
  
  ##############################################
  ##### Jics RunUnitLauncher pool settings #####
  ##############################################
  #jics.runUnitLauncherPool.enable: false
  #jics.runUnitLauncherPool.size: 20
  #jics.runUnitLauncherPool.validationInterval: 1000
  
  #########################
  ##### Jhdb settings #####
  #########################
  #jhdb.lterm: LTERMVAL
  #jhdb.identificationCardData: SomeIDData
  
  ###################################
  ##### DateHelper configuration ####
  ###################################
  #forcedDate: "2013-08-26T12:59:58+01:57"
  
  #############################
  ##### Sort configuration ####
  #############################
  #externalSort.threshold: 256MB
  
  ###################################
  ##### Server timeout (10 min)  ####
  ###################################
  spring.mvc.async.request-timeout: 600000
  
  ###############################
  ##### DATABASE STATISTICS  ####
  ###############################
  databaseStatistics : false
  
  ######################
  ##### CALLS GRAPH ####
  ######################
  callGraph : false
  
  ####################################
  #####     SSL configuration    #####
  ####################################
  gapwalk.ssl.enabled : true
  gapwalk.ssl.trustStore : "./config/clientkey.jks"
  gapwalk.ssl.trustStorePassword : mysslcertifpassword
   
  ##################################
  ##### MQ settings #####
  ##################################
  mq.queues: jmsmq
  mq.queues.jmsMQQueueManagers[0].jmsMQQueueManager: QM1
  mq.queues.jmsMQQueueManagers[0].jmsMQAppName: Gapwalk
  mq.queues.jmsMQQueueManagers[0].jmsMQChannel: DEV.APP.SVRCONN
  mq.queues.jmsMQQueueManagers[0].jmsMQHost: localhost
  mq.queues.jmsMQQueueManagers[0].jmsMQPort: 1415
  mq.queues.jmsMQQueueManagers[0].jmsMQUserid: app
  mq.queues.jmsMQQueueManagers[0].jmsMQSSLCipher: "*TLS12ORHIGHER"
  mq.queues.jmsMQQueueManagers[1].jmsMQQueueManager: QM2
  mq.queues.jmsMQQueueManagers[1].jmsMQAppName: Gapwalk
  mq.queues.jmsMQQueueManagers[1].jmsMQChannel: DEV.APP.SVRCONN
  mq.queues.jmsMQQueueManagers[1].jmsMQHost: localhost
  mq.queues.jmsMQQueueManagers[1].jmsMQPort: 1415
  mq.queues.jmsMQQueueManagers[1].jmsMQUserid: app
  
  #########################################################
  ##### Configuration properties for JMS MQ connection ####
  #########################################################
  mq.queues.jms.connectionfactory.borrow-connection-timeout: 31 # Timeout, in seconds, for borrowing connections from the pool.
  mq.queues.jms.connectionfactory.ignore-session-transacted-flag: true # Whether or not to ignore the transacted flag when creating a session.
  mq.queues.jms.connectionfactory.local-transaction-mode: false # Whether or not to include local transactions.
  mq.queues.jms.connectionfactory.maintenance-interval: 62 # The time, in seconds, between runs of the pool's maintenance thread.
  mq.queues.jms.connectionfactory.max-idle-time: 63 # The time, in seconds, after which connections are cleaned up from the pool.
  mq.queues.jms.connectionfactory.max-lifetime: 0 # The time, in seconds, that a connection can be pooled for before being destroyed. 0 denotes no limit.
  mq.queues.jms.connectionfactory.max-pool-size: 1 # The maximum size of the pool. This property will be overwritten by mq.queues.jmsMQQueueManagers[N].jmsMQMaxPoolSize property (if provided).
  mq.queues.jms.connectionfactory.min-pool-size: 1 # The minimum size of the pool.
  mq.queues.jms.connectionfactory.reap-timeout: 0 # The reap timeout, in seconds, for borrowed connections. 0 denotes no limit.
  
  
  ###############################
  ##### SQL SHIFT CODE POINT ####
  ###############################
  # Code point 384 match unicode character \u0180
  sqlCodePointShift : 384 
  
  ###############################
  ##### LOCK TIMEOUT RECORD  ####
  ###############################
  # Blu4IV record lock timeout 
  lockTimeout : 100
  
  ##############################
  ##### REPORTS OUTPUT PATH ####
  ##############################
  reportOutputPath: reports
  
  ##############################
  ##### TASK EXECUTOR       ####
  ##############################
  taskExecutor: 
    corePoolSize: 5
    maxPoolSize: 10
    queueCapacity: 50
    allowCoreThreadTimeOut: false
    
  ##############################
  ##### PROGRAM NOT FOUND   ####
  ##############################
  stopExecutionWhenProgNotFound: false
  
  ######################################################
  #####  DISP DEFAULT VALUE (to be removed one day) ####
  ######################################################
  defaultKeepExistingFiles: true
  
  ######################################################
  #####  BLOCKSIZE DEFAULT VALUE  ####
  ######################################################
  #blockSizeDefault: 32760
  
  #####################################
  #####  JOBQUEUE CONFIGURATION    ####
  #####################################
  jobqueue:
    api.enabled: false
    impl: none # possible values: quartz, none
    schedulers:  # list of schedulers
      -
        name: queue1
        threadCount: 5
      -
        name: queue2
        threadCount: 5
        
  ################################################################################
  ##### QUERY BUILDING                                                          ##
  # useConcatCondition : false by default 
  # if true, in the query, the where condition is build with key concatenation  ##
  ################################################################################
  # query.useConcatCondition: true
  
  ########################################
  #####  JCL Batch Restart Mechanism  ####
  ########################################
  jcl:
  checkpoint:
  enabled: false
  #expireTimeout: -1
  #expireTimeoutUnit: SECONDS # Supported values: java.util.concurrent.TimeUnit
  #provider: redis
  
  ##############################
  #####  System parameters  ####
  ##############################
  system.date.format:MDY  
  system.date.separator: "/"
  
  #############################################################
  #####  Database metadata schema inclusion configuration  ####
  #############################################################
  gapwalk:
    database:
      metadata:
         schema-inclusion:
            enabled: false
            schemas:
              global:
                - "SCHEMA1"
                - "SCHEMA2"
  
  ##############################
  #####  URL configuration  ####
  ##############################
  gapwalk.post.script.mediatype.json: false
  
  ########################################
  #####  CBLQDA parameters  ####
  ########################################
  gapwalk.cobol.cblqda.enabled: false
  ----
  ```
+ Use variable length files with LISTCAT commands

  ```
  [**/*.*]
  encoding=IBM930
  reencoding=false
  
  [global]
  listcat.variablelengthpreprocessor.enabled=true
  listcat.variablelengthpreprocessor.type=rdw
  # use "rdw" if your .listcat file contains a set of records (RDW)
  # use "bdw" if your .listcat file contains a set of blocks (bdw)
  ```
+ Provide Null Byte Indicator Value in LOAD/UNLOAD utility

  ```
  # Unload properties 
  # For date/time: if use database configuration is enabled, formats are ignored
  # For nbi; use hexadecimal syntax to specify the byte value
  # - When the value is null in database : the value dumped to the file is filled by low value characters and the NBI is
  # equal to the byte 6F (the ? character)
  # - When the value is not null in database and the column is nullable: the NBI is equal to the byte 00 (low value) and NOT
  # equal to the byte 40 (space)
  unload:
    sqlCodePointShift: 0
    nbi:
      whenNull: "6F"
      whenNotNull: "00"
    useDatabaseConfiguration: false
    format:
      date: MM/dd/yyyy
      time: HH.mm.ss
      timestamp: yyyy-MM-dd-HH.mm.ss.SSSSSS
  ```

## Available properties for the main application
<a name="ba-runtime-key-value-main"></a>

This table provides an exhaustive view of key/values parameters.

**Note**  
If you are migrating to version 5.1.0 or later and using bluesam with default openWarmUp behavior:  
The default value of `bluesam.openWarmUp` has changed from `true` to `false`
To maintain existing behavior, you must explicitly set `bluesam.openWarmUp=true`


| Key | Type | Default value | Description | Release version | 
| --- | --- | --- | --- | --- | 
| `blockSizeDefault` | number | 32760 | The default block size to be used for BDW bytes. |  | 
| `blu4iv.dataaccess.useOldDaoDesign` | boolean | false | A global flag that determines if the application is to use the old DAO architecture or the new. This is dependent on whether the DAO's were generated using old or new design. |  | 
| `blu4iv.userspace.batchThreshold` | int | 1 | Specifies the number of update or set operations on a userspace after which the userspace is persisted in an external data repository. | 5.75.0 | 
| `blu4iv.userspace.pageSize` | int | 4096 | Specifies the page size which is used to allocate storage for user spaces. The size of the user space at any given time is always a multiple of this number specified. | 4.10.0 | 
| `blu4iv.userspace.redis.*` | Supported Redis properties |  | Specifies configuration properties for the user spaces redis store, see [Available Redis cache properties in AWS Transform for mainframe Runtime](ba-runtime-redis-configuration.md). | 4.10.0 | 
| `blu4iv.userspace.store-type` | string | memory | Specifies the store type that is used for user space registry. Supported values are memory and redis. If no store type is provided, memory is used by default. | 4.10.0 | 
| `bluesam.bluesamStatusPollingInterval` | number | 1000 | Specifies time (in millisecond) to wait between each iteration when polling bluesam status to check online activities. | 4.5.0 | 
| `bluesam.cache` | string |  | If not set, the Blusam cache will not be used. Possible values (cache implementations) are ehcache and redis ([Redis cache properties](ba-runtime-redis-configuration.md#ba-runtime-redis-caches-properties)). |  | 
| `bluesam.checkBluesamStatus` | boolean | false | Specifies whether or not to check bluesam dataset status before accessing it. | 4.5.0 | 
| `bluesam.datasetPrefetchWindowSize` | string[] |  | Specifies per-dataset prefetch window size overrides. Each entry format: `"datasetName:size"`. If a dataset is not listed, it falls back to the global `bluesam.prefetchWindowSize` value.<br />**Note:**<br />- Do not add spaces around the colon separator.<br />- Dataset names containing `\|` are supported (uses last colon as delimiter).<br />- Wrap entries in double quotes or ensure no spaces in the entry.<br />- Example: `"fileset1\|MYFILE:10000"` |  | 
| `bluesam.disabled` | boolean | false | Whether to disable Blusam entirely. |  | 
| `bluesam.externalDdlManagement` | boolean | false | When enabled, BlueSAM will not auto-create tables and instead adopts externally managed tables by registering metadata only. |  | 
| `bluesam.fileList` | string[] |  | Specifies the list of bluesam dataset to be cached during open.<br />**Note:**<br />**- This parameter is only effective when `bluesam.openWarmUp` is set to `false`.** | 5.1.0 | 
| `bluesam.fileLoading.commitInterval` | number | 100000 | The bluesam commit interval. |  | 
| `bluesam.maxBluesamDisablingThreadpoolSize` | number | 10 | Specifies maximum threadpool size used to disable bluesam datasets for batch processing. | 4.5.0 | 
| `bluesam.maxBluesamStatusPollingRetry` | number | 3 | Specifies maximum number of retries when polling bluesam status is failing. | 4.5.0 | 
| `bluesam.metadataWarmUpFileList` | string[] |  | Specifies the list of bluesam datasets whose index metadata will be pre-loaded into a permanent in-memory cache at application startup.<br />**Note:**<br />- Indexes are loaded on ApplicationReadyEvent and persist for the full application lifecycle.<br />- Only effective for large datasets. |  | 
| `bluesam.openWarmUp` | boolean | false | Specifies whether to cache any bluesam datasets during open.<br />**Warning: Breaking Change in version 5.1.0**<br />**- Default value changed from `true` to `false`.** | 5.1.0 | 
| `bluesam.prefetchWindowMultiples` | int | 5 | Specifies the multiplier for prefetch window size to determine maximum prefetch window capacity. The maximum capacity is calculated as `prefetchWindowSize × prefetchWindowMultiples`. This property is only effective when using Redis cache. |  | 
| `bluesam.prefetchWindowSize` | int | 1000 | Specifies the number of records to prefetch and cache in memory for Redis cache optimization. This property is only effective when using Redis cache. |  | 
| `bluesam.redis.batchClearSize` | int | 1000 | Batch size for Redis cache clear operations when `bluesam.redis.enableBatchClear` is enabled. |  | 
| `bluesam.redis.clearStrategy` | string | DEFAULT | Specifies the strategy for cache clear operations.<br />`DEFAULT` uses the Spring `RedisCache.clear()` method.<br />`REDISSON` uses the Redisson `unlinkByPattern` method, which is cluster-safe and avoids out-of-memory errors.<br />`REDISSON_BATCHED` uses a Redisson SCAN operation with batched expire calls, which gives you maximum control over the Redis load. |  | 
| `bluesam.redis.deleteAllBatchSize` | int | 1500 | Batch size for Redis deleteAll operations to optimize performance when working with large datasets. |  | 
| `bluesam.redis.enableBatchClear` | boolean | false | Enable batch processing for Redis cache clear operations when working with large datasets. |  | 
| `bluesam.redis.readBatchSize` | int | 1500 | Batch size for Redis cache read operations (bulk read from cache by IDs). |  | 
| `bluesam.sizesCleanUpThreshold` | int | 1000 | Maximum number of entries retained in the internal offset-tracking map per data set for large data sets (LargeKSDS, LargeESDS) during concurrent multi-threaded writes. When the map exceeds this threshold, it is trimmed to the 10 most recent entries to prevent heap exhaustion while preserving enough entries to avoid NullPointerException from concurrent thread access. Reduce this value if heap pressure is observed during high-volume large dataset bulk loads. |  | 
| `bluesam.warmUpMetadataCacheLimit` | long | 0 | Maximum number of index entries allowed in the metadata warm-up cache. Set to 0 for unlimited.<br />**Note:**<br />- This is a global limit across all datasets configured in `bluesam.metadataWarmUpFileList`.<br />- When the limit is reached, additional indexes are skipped with a warning log. |  | 
| `cacheMetadata` | boolean | true | Specifies whether to cache database metadata. |  | 
| `card.encoding` | string | CP1145 | Card encoding: to be used with`useControlMVariable`. |  | 
| `check-groovy-file` | boolean | true | Specifies whether to check groovy files content before registering. |  | 
| `checkinputfilesize` | boolean | false | Specifies whether to release a check if the file size is a multiple of record size. |  | 
| `cl.configuration.context.encoding` | string | CP297 | The encoding of CL files. Expects a valid encoding`CP1047`,`IBM930`,`ASCII`,`UTF-8`... Default value is`CP297` |  | 
| `cl.zonedMode` | string | EBCDIC\_STRICT | The mode for encoding or decoding control language (CL) commands. Allowed values are`EBCDIC_STRICT` /`EBCDIC_MODIFIED` /`AS400`. |  | 
| `clcommand.rtvmbrd.hasHeader` | string | true | Specify if the files contain headers that should not be included when counting the rows. |  | 
| `cleanTempFilesDirectoryAtStartup` | boolean | true | Specifies whether to purge the contents of the temporary files folder at application startup. |  | 
| `context.preconstruct.enable` | boolean | false | Specifies whether to activate pre construction of program context. |  | 
| `context.preconstruct.frequencyInMillis` | number | 100 | The interval between each run of the task that adjusts the size of the pool. |  | 
| `context.preconstruct.minInstances` | number | 2 | The number of instances that will be created the first time a context is needed. |  | 
| `context.preconstruct.parallelism` | number | 5 | The number of threads used to produce the missing instances in the queue when the adjustment task runs. |  | 
| `database.cursor.overflow.allowed` | boolean | true | Specifies whether to allow the cursor overflow. Set to`true` to perform a next call on the cursor whatever its position. Set to`false` to check whether the cursor is at the last position before performing a next call on cursor. Only enable if cursor is SCROLLABLE (SENSITIVE or INSENSITIVE). |  | 
| `database.cursor.raise.already.opened.error` | boolean | false | Specifies whether to enable raising SQLCODE error 502 when an already opened cursor is opening. |  | 
| `databaseStatistics` | boolean | false | Specifies whether to allow SQL builders to collect and display statistics information. |  | 
| `dataSimplifier.byteRangeBoundsCheck` | boolean | false | When set to true, it ensures that no ByteRange is created with improper values. The default is false. |  | 
| `dataSimplifier.cacheDefaultValues` | boolean | false | When set to true, enables per-instance caching of computed default-value byte patterns in `RecordEntity`, `ElementaryRange`, and `RangeType` subclasses. The default is false. |  | 
| `dataSimplifier.doubleFloatingType` | string | IEEE\_754 | The double floating type is the format used to encode and decode a floating-point number. Allowed values are `IEEE_754` / `HFP`(for Hexadecimal Floating Point format). Default value is `IEEE_754`. | 4.7.0 | 
| `dataSimplifier.numproc` | string | PFD | numproc compiler specification. Allowed values are `PFD`/`NOPFD`/`MIG`/. Default is `PFD`. |  | 
| `dataSimplifier.onInvalidNumericData` | string | reject | How to react when decoding invalid numeric data. Allowed values are`reject` /`toleratespaces` /`toleratespaceslowvalues` /`toleratemost`. Default is`reject`. |  | 
| `dataSimplifier.zeroInvalidBcdNibbles` | boolean | true | When set to true, bytes containing invalid BCD nibbles (hex digits `A`-`F` in digit positions) are treated as `00` during packed decimal decode. The default is true. |  | 
| `datasource.bluesamDs` \+ -`driver-class-name` \+ -`url` \+ -`username` \+ -`password` \+ -`type` | Standard spring datasource with subkeys |  | Contains the connection information for the Blusam database. Alternately, use of AWS secrets is strongly encouraged, as explained in [Blusam database](ba-runtime-config-app-secrets.md#blusam-database). |  | 
| `datasource.jicsDs` \+ -`driver-class-name` \+ -`url` \+ -`username` \+ -`password` \+ -`type` | Standard spring datasource with subkeys |  | Contains the connection information for the Jics database. Alternately, use of AWS secrets is strongly encouraged, as explained in [JICS database](ba-runtime-config-app-secrets.md#jics-database). |  | 
| `dateTimeFormat` | string | ISO | The dateTimeFormat describes how to spill database date time timestamp type into data simplifier entities. Allowed values are`ISO` /`EUR` /`EUR` /`USA` /`LOCAL` |  | 
| `dbDateFormat` | string | yyyy-MM-dd | The db target date format. |  | 
| `dbTimeFormat` | string | HH:mm:ss | The db target time format. |  | 
| `dbTimestampFormat` | string | yyyy-MM-dd HH:mm:ss.SSSSSS | The db target timestamp format. |  | 
| `defaultKeepExistingFiles` | boolean | false | Specifies whether to set the dataset default previous value. |  | 
| `disposition.checkexistence` | boolean | false | Specifies whether to release a check on file existence for Dataset with DISP SHR or OLD. |  | 
| `enableActivePgmIdCache` | boolean | false | Specifies whether to enable active program ID local cache. Use carefully this feature because JICS resources can be shared amongst programs and users. Those resources can be changed externally by any administrators and the local cache put in place might be invalidated. |  | 
| `encoding` | string | ASCII | The encoding used in projects (not in groovy files). Expects a valid encoding`CP1047`,`IBM930`,`ASCII`,`UTF-8`... |  | 
| `externalSort.threshold` | datasize (example: 12 MB) |  | The sort threshold: determines when the system should switch from in-memory to external merge sorting using temporary files on the file system. If not specified (default=`null`), the threshold is set to half of the available memory at each new sort task. To estimate the available memory, a call to System.gc() is performed. |  | 
| `fetchSize` | number |  | The fetchSize value for cursors. Use when fetching data using chunks by load/unload utils. |  | 
| `file.stdoutIntoLogger` | boolean | false | Specifies whether to enable writing to logger instead of the default system output stream in the default `SYSPRINT` and `SYSPUNCH` files. |  | 
| `filesDirectory` | string |  | The directory for batches input/output files. |  | 
| `forcedDate` | string |  | Forces the date to the date provided if there is one. |  | 
| `forcedDateMode` | string |  | Specifies the forced date mode. When set to `HYBRID`, the date portion is the configured forced date but the time portion reflects the actual system time. Applies only if `forcedDate` is also set. |  | 
| `forceDisableSQLTrimStringType` | boolean | false | Specifies whether to disable trim of all sql string parameters. |  | 
| `forceHR` | boolean | false | Specifies whether to use Human Readable SYSPRINT, either on console or file output. |  | 
| `frozenDate` | boolean | true | Specifies whether to freeze the date. Applies only if`forcedDate` is also set. |  | 
| `gapwalk-application.defaultSuperAdminUserName` | string | `sadmin` | When `gapwalk-application.security` is disabled, specifies the default local super user name. |  | 
| `gapwalk-application.defaultSuperAdminUserPwd` | string | `sadmin` | When `gapwalk-application.security` is disabled, specifies the default local super user password. |  | 
| `gapwalk-application.security` | string | `disabled` | Toggle global security configuration (XSS, CORS, CSRF, OAUTH authentication...). Allowed values are `disabled` and `enabled`. |  | 
| `gapwalk-application.security.allowedOrigins` | string[] | `null` | The list of origins to allow. This option requires `gapwalk-application.identity` to be set to `oauth`. |  | 
| `gapwalk-application.security.blockedURIs` | string[] | null | The list of URIs to block. This option is required when `gapwalk-application.security.filterURIs` is `enabled`. |  | 
| `gapwalk-application.security.claimGroupName` | string | `cognito:groups` | The claim attribute that contains the list of all the groups a user belongs to. Use `cognito:groups` for Amazon Cognito, or any other string for a foreign IdP. |  | 
| `gapwalk-application.security.customAllowedHeaders` | string[] | null | The list of custom headers to allow. This option requires `gapwalk-application.identity` to be set to `oauth`. | 4.8.0 | 
| `gapwalk-application.security.filterURIs` | string | `disabled` | Toggle filtering URIs configuration. Allowed values are `disabled` and `enabled`. |  | 
| `gapwalk-application.security.identity` | string | null | Global authentication method. Recommended value is `oauth`. Allowed values are `json` and `oauth`. This option is required when `gapwalk-application.security` is `enabled`. |  | 
| `gapwalk-application.security.issuerUri` | string | null | The issuer URI of the identity provider (IdP). This option is required when `gapwalk-application.identity` is `oauth`. |  | 
| `gapwalk-application.security.userAttributeName` | string | `username` | The claim attribute name used to identify a user request. Use `username` for Amazon Cognito, `preferred_username` for Keycloak, or any other string for a foreign IdP. |  | 
| `gapwalk.cobol.cblqda.enabled` | boolean | false | Enables a CBLQDA feature that controls QSAM files' dynamic allocation during an OPEN statement. This configuration helps to dynamically allocate temporary files declared in the program, even if the files are not defined in the JCL script. |  | 
| `gapwalk.database.metadata.schema-inclusion.enabled` | boolean | false | Enables a memory optimization feature that control which database schemas are cached by a application. This configuration helps reduce memory footprint while maintaining system stability by intelligently managing schema metadata. It automatically includes some common database system schemas which maybe required for proper operation. | 4.9.0 | 
| `gapwalk.database.metadata.schema-inclusion.schemas.global` | list<String> | null | Defines a list of schemas that should be cached. | 4.9.0 | 
| `gapwalk.database.support.useSavePointToRestoreFail` | boolean | false | Enables transaction recovery in case of failure by using savepoints on insert queries. Enabling this property may impact database performance. You can override this setting for specific queries using the query-to-database mapping configuration. | 4.6.0 | 
| `gapwalk.io.sequential.readBufferSize` | integer | 8192 | Sets the buffer size (in bytes) for `BufferedInputStream` when reading sequential files. Increasing this value reduces the number of I/O read operations, which can improve performance when reading large files from network-attached storage such as Amazon EFS. |  | 
| `gapwalk.line.separator` | string | null | Specifies line separator type in gapwalk. The allowed values are WIN (CRLF) / UNIX (LF) / LINUX (LF). Other values are ignored and System line.sepatator property is used. |  | 
| `gapwalk.post.script.mediatype.json` | boolean | false | Specifies whether the `Content-Type` header of the response from endpoint `/post/script/{scriptId:.+}` is set to `application/json`, depending on the value of a boolean variable. If set to false, the default is `text/plain; charset=utf-8`. |  | 
| `gapwalk.ssl.enabled` | boolean | false | Indicated to set the following `gapwalk.ssl.*` properties to the current JVM system properties if there are not already set at application start. |  | 
| `gapwalk.ssl.keyStore` | string | null | Set the value to the system property `javax.net.ssl.keyStore` if not already setup at application start. |  | 
| `gapwalk.ssl.keyStorePassword` | string | null | Set the value to the system property `javax.net.ssl.keyStorePassword` if not already setup at application start. Alternately, use of AWS secrets is strongly encouraged, as explained in [Secret manager for SSL password settings](ba-runtime-config-app-secrets.md#ba-runtime-ssl-secrets-properties). |  | 
| `gapwalk.ssl.trustStore` | string | null | Set the value to the system property `javax.net.ssl.trustStore` if not already set at application start. |  | 
| `gapwalk.ssl.trustStorePassword` | string | null | Set the value to the system property `javax.net.ssl.trustStorePassword` if not already setup at application start. Alternately, use of AWS secrets is strongly encouraged, as explained in [Secret manager for SSL password settings](ba-runtime-config-app-secrets.md#ba-runtime-ssl-secrets-properties). |  | 
| `gapwalk.ssl.trustStoreType` | string | null | Set the value to the system property `javax.net.ssl.trustStoreType` if not already setup at application start. |  | 
| `gapwalk.zos.sysplexName` | string | null | Specifies the sysplex name value for the emulated CVT (Communications Vector Table). | 5.202.0 | 
| `gapwalk.zos.systemName` | string | null | Specifies the system name value for the emulated CVT (Communications Vector Table). | 5.202.0 | 
| `gdgDirectoryPath` | string | `output/gdg` | GDG directory path is the directory where the gdg files are stored. | 4.6.0 | 
| `ims.messages.extendedSize` | boolean | false | Specifies whether to set the extended size on IMS messages. |  | 
| `ims.programs` | string |  | List of IMS programs to use. Separate each parameter with a semicolon (`;`) and each transaction with a comma (`,`). For example:`PCP008,PCT008;PCP054,PCT054;PCP066,PCT066;PCP068,PCT068;`  |  | 
| `invalidDataTolerence` | boolean | true | Specifies whether invalid data is tolerated for packed type. |  | 
| `jcl.checkpoint.enabled` | boolean | false | Specifies if JCL checkpoint mechanism is enabled to allow job restart. JCL checkpoints are created and saved to the in-memory registry at the start of each step or main program invocation. All the step level checkpoints are persisted at the end of the job, if persistence provider is defined. |  | 
| `jcl.checkpoint.expireTimeout` | number | -1 |  Specifies time duration to retain JCL checkpoints in the persistence provider or in-memory registry. |  | 
| `jcl.checkpoint.expireTimeoutUnit` | string | SECONDS | Specifies time duration unit for the `jcl.checkpoint.expireTimeout` property. Supported enum constant values: java.util.concurrent.TimeUnit. |  | 
| `jcl.checkpoint.provider` | string | null | Specifies JCL checkpoint mechanism persistence provider. Allowed values are `redis`.  |  | 
| `jcl.checkpoint.redis.*` | Supported Redis properties |  |  Specifies configuration properties for JCL checkpoint mechanism's REDIS persistence provider, see [Supported Redis properties](ba-runtime-redis-configuration.md#ba-runtime-redis-supported-properties). |  | 
| `jcl.nullJclEof` | boolean | true | Specifies how null JCL statements (//) are handled during job execution. When true, // terminates the job immediately (EOF mode). When false, // is treated as a null statement and execution continues (IGNORE mode). |  | 
| `jhdb.checkpointPath` | string | file:./setup/ | If`jhdb.checkpointPersistence` is not`none` then this parameter allows you to setup the checkpoint persistence path (checkpoint.dat file storage location), all the checkpoints data contained in the registry are serialized and backed up in a file (checkpoint.dat) located in provided folder. Note that only checkpoint data (scriptId, stepId, database position and checkpoint area) are concerned by this backup. |  | 
| `jhdb.checkpointPersistence` | string | none | The checkpoint persistence mode. Allowed values are`none` /`add` /`end`. Use`add` to persist checkpoints when a new one is created and added to the registry. Use`end` too persist checkpoint at server shutdown. Any other values disable the persistence. Note that each time a new checkpoint is added to the registry, all the existing checkpoints will be serialized and the file will be erased. It is not an append to the existing data in the file. So depending on the number of checkpoints, it can have some effects on performances. |  | 
| `jhdb.configuration.context.encoding` | string | CP297 | The JHDB (Java Hierarchical Database) encoding. Expects a valid encoding string`CP1047`,`IBM930`,`ASCII`,`UTF-8`... |  | 
| `jhdb.identificationCardData` | string |  | Used to hard-code some "operator identification card data" to the MID field designated by the CARD parameter. Blank by default, no input restriction. |  | 
| `jhdb.lterm` | string |  | Allow you to force a common logical terminal ID in the case of an IMS emulation. If not set then sessionId is used. |  | 
| `jhdb.metadata.extrapath` | string | file:./setup/ | A configuration parameter that specifies an extra, runtime-specific root folder for psbs and dbds folders. |  | 
| `jhdb.navigation.cachenexts` | number | 5000 | The cache duration (in milliseconds) used in hierarchical navigation for an RDBMS. |  | 
| `jhdb.optim.cacheRetention` | boolean | false | Specifies whether to retain the node cache across consecutive read operations. When enabled, sequential reads reuse the cache, and only write operations (commit or rollback) clear it. |  | 
| `jhdb.query.limitJoinUsage` | boolean | true | Specifies whether to use the limit join usage parameter on RDBMS graphs. |  | 
| `jhdb.use-db-prefix` | boolean | true | Specifies whether to enable a database prefix in hierarchical navigation for an RDBMS. |  | 
| `jics.data.dataJsonInitLocation` | string |  |  |  | 
| `jics.db.dataScriptLocation` | string |  | Defines the path to SQL scripts used for initializing the JICS database. Accepts a comma-separated list of files and directories, allowing for multiple scripts and folders to be specified. |  | 
| `jics.db.dataTestQueryLocation` | string |  | Location of a sql script containing a single sql query that is expected to return a count of objects (for example: counting number of records in the jics program table). If the count equals 0, database will be loaded using the`jics.db.dataScriptLocation` script, otherwise database load will be skipped. |  | 
| `jics.db.ddlScriptLocation` | string |  | The Jics DDL script location. Allows you to initiate the Jics database schema using a .sql script. Blank by default. For example,`./jics/sql/jics.sql`. |  | 
| `jics.db.schemaTestQueryLocation` | string |  | Location of the sql file that should contain a unique query that returns the number of objects in the jics schema (if any). |  | 
| `jics.initList` | string |  | The initialize JICS list, separated by commas. If present, it defines comma-separated names of lists to activate at Apache Tomcat startup among CICS lists. Example value: `$UUU,DFH$IVPL,PEZ1`. This will cascade to groups contained in those lists and their underlying resource definitions, which will then be visible to the runtime. Empty by default. |  | 
| `jics.jcl.rt.encoding` | string | CP037 | The encoding of the JCL scripts written in the dedicated JICS queue. |  | 
| `jics.jcl.rt.queue` | string | JICS | The name of the queue to which JCL scripts can be written line by line at runtime. |  | 
| `jics.parameters.applid` | string | VELOCITY | The applied to identify application in JICS (at least 4 characters, no max length). |  | 
| `jics.parameters.charset` | string | CP037 | JICS globally used character set. |  | 
| `jics.parameters.cwa.length` | number | 0 | The length of the common work area (CWA). |  | 
| `jics.parameters.datform` | string | MMDDYY | The date form. |  | 
| `jics.parameters.eibtrmid` | string | TERM | The terminal identifier (4 characters maximum, 1 minimum). |  | 
| `jics.parameters.jobname` | string | MJOBNAME | The job name. |  | 
| `jics.parameters.netname` | string | MYNETNAME | The network name (8 characters maximum, 1 minimum). |  | 
| `jics.parameters.opid` | string | XXX | The 3-character operator identification. |  | 
| `jics.parameters.sysid` | string | CICS | The system identification (SYSID). |  | 
| `jics.parameters.sysname` | string | SYSNAME | The AS400 system name (sysname). |  | 
| `jics.parameters.tsqimpl` | string | bluesam | JICS Temporary Storage Queue (TSQ) implementation (allowed values are`bluesam` /`memory` /`redis`) |  | 
| `jics.parameters.userid` | string |  | The user id (8 characters maximum, no minimum). When no value is provided (blank by default) the HTTP session id is used as the user id.  |  | 
| `jics.parameters.username` | string | MYUSERNAME | The username (10 characters maximum, 1 minimum). |  | 
| `jics.queues.sqs.region` | string | eu-west-1 | The AWS Region for Amazon Simple Queue Service, used in JICS. |  | 
| `jics.queues.ts.redis.*` | Supported Redis properties |  | Specifies configuration properties for the JICS TS Queues Redis server, see [Supported Redis properties](ba-runtime-redis-configuration.md#ba-runtime-redis-supported-properties). |  | 
| `jics.redis.*` | Supported Redis properties |  | Specifies configuration properties for the JICS Redis server connection factory, see [Supported Redis properties](ba-runtime-redis-configuration.md#ba-runtime-redis-supported-properties). |  | 
| `jics.runUnitLauncherPool.enable` | boolean | false | Specifies whether to activate the run unit launcher pool in JICS. |  | 
| `jics.runUnitLauncherPool.parallelism` | number | 2 | The number of threads used to produce the missing instances in the queue when the adjustment task runs. |  | 
| `jics.runUnitLauncherPool.size` | number | 20 | The run unit launcher pool size in JICS. |  | 
| `jics.runUnitLauncherPool.validationInterval` | number | 1000 | The interval between each run of the task that adjusts the size of the pool. |  | 
| `jics.spool.smtp.debug` | boolean | false | Specifies the debug mode for the SMTP server. |  | 
| `jics.spool.smtp.hostname` | string | null | Specifies the SMTP server host. Example: `smtp.xxx.com` |  | 
| `jics.spool.smtp.password` | string | null | Specifies the login password of the SMTP server. |  | 
| `jics.spool.smtp.port` | string | null | Specifies the SMTP server port. Example: 25 |  | 
| `jics.spool.smtp.username` | string | null | Specifies the username of the SMTP server. |  | 
| `jics.xa.agent.timeout` | number |  |  |  | 
| `jildb.backend` | string |  | Specifies the database type used in the Jildb backend, for example, Oracle. |  | 
| `jildb.datasource` \+ -`driver-class-name` \+ -`url` \+ -`username` \+ -`password` | Standard spring datasource with subkeys |  | Contains the connection information for the Jics database. |  | 
| `jildb.record-hold-timeout` | int | 10000 | Specifies the wait timeout period, in milliseconds, for the record holding mechanism in Jildb. |  | 
| `job.default.encoding` | string | CP1047 | Specifies the default encoding which is used to initialize the job level storage. For example, switches in BLU4IV application uses this encoding to initialize to zeroes. | 4.9.0 | 
| `listOfMDCUrlParams` | string | `null` | The list of URL parameters to add to the MDC when executing Groovy batch script.  |  | 
| `localDateFormat` | string |  | List of local date formats.Separate each format with`\`. |  | 
| `localTimeFormat` | string |  | List of local time formats. Separate each format with`\` |  | 
| `localTimestampFormat` | string |  | List of local timestamp formats. Separate each format with`\`. |  | 
| `lockTimeout` | number | 500 | The lock timeout, in milliseconds. |  | 
| `logging.config` | Path | classpath:logback-main.xml | Standard key for the reference to the logback configuration file. Other standard logging keys are available too. |  | 
| `mapTransfo.prefixes` | string | &,@,%% | List of prefixes to be used when transforming controlM variables. Each one separated by comma. |  | 
| `mf.runtime.switch.N` | boolean | true | Enables null insertion for MF nature line-sequential files. | 4.4.0 | 
| `mf.runtime.switch.T` | boolean | false | Enables insertion of tab characters in MF nature line-sequential files. | 4.4.0 | 
| `mq.connection.pool.share` | boolean | false | Indicate whether to share or recreate the JMS connection pool with the same Queue Manager. | 4.9.0 | 
| `mq.queues` | string | `sqs` | Specifies which supported queue brocker to use among `sqs` using Amazon SQS, `rabbitmq` using on-prem Rabbit MQ or `jms` using on-prem IBMMQ. |  | 
| `mq.queues.default.syncpoint` | boolean | false | Specifies the default behavior for MQ PUT commands when neither MQPMO\_SYNCPOINT nor MQPMO\_NO\_SYNCPOINT are set. When set to true, it acts as `MQPMO_SYNCPOINT` and messages are NOT directly committed during the PUT command. When set to false, it acts as `MQPMO_NO_SYNCPOINT` and messages are directly committed during the PUT command. |  | 
| `mq.queues.jms.connectionfactory.*` | Supported Atomikos connection factory properties |  | Specifies configuration properties for the JMS MQ connection pool. |  | 
| `mq.queues.jmsMQQueueManagers[N]` |  |  | When `mq.queues` is `jms`, enables to specify an IBM MQ connection list. `mq.queues.jmsMQQueueManagers[0]` for the first connection, `mq.queues.jmsMQQueueManagers[1]` for the second and so on. |  | 
| `mq.queues.jmsMQQueueManagers[N].jmsMQAppName` | string | null | The IBMMQ application name. |  | 
| `mq.queues.jmsMQQueueManagers[N].jmsMQChannel` | string | null | The IBMMQ channel name. |  | 
| `mq.queues.jmsMQQueueManagers[N].jmsMQHost` | string | null | The IBMMQ hostname. |  | 
| `mq.queues.jmsMQQueueManagers[N].jmsMQMaxPoolSize` | number | 0 | The IBMMQ maximum pool size . With 0, an infinite number of physical connections are enabled. |  | 
| `mq.queues.jmsMQQueueManagers[N].jmsMQPassword` | string | null | The IBMMQ user password. Alternately, use of AWS secrets is strongly encouraged, as explained in [Secret manager for IBM MQ password settings](ba-runtime-config-app-secrets.md#ba-runtime-IBMMQ-secrets-properties). |  | 
| `mq.queues.jmsMQQueueManagers[N].jmsMQPort` | number | null | The IBMMQ port. |  | 
| `mq.queues.jmsMQQueueManagers[N].jmsMQQueueManager` | string | null | The IBMMQ queue manager name. |  | 
| `mq.queues.jmsMQQueueManagers[N].jmsMQSSLCipher` | string | null | The IBMMQ SSL cipher suite. An example could be `"*TLS12ORHIGHER"`. Refer to the official documentation [TLS CipherSpecs and CipherSuites in IBM MQ classes for JMS](https://www.ibm.com/docs/en/ibm-mq/9.2?topic=jms-tls-cipherspecs-ciphersuites-in-mq-classes) for more details. |  | 
| `mq.queues.jmsMQQueueManagers[N].jmsMQUserid` | string | null | The IBMMQ user name. |  | 
| `mq.queues.non.jms.client` | boolean | false | Indicate whether target client for sending messages to is non-JMS. Native MQ format will be used for non-JMS client while RFH2 format will be used for JMS. | 4.5.0 | 
| `mq.queues.rabbitMQHost` | string | null | The Rabbit MQ hostname. |  | 
| `mq.queues.rabbitMQPassword` | string | null | The Rabbit MQ password. |  | 
| `mq.queues.rabbitMQPort` | number | null | The Rabbit MQ port. |  | 
| `mq.queues.rabbitMQUsername` | string | null | The Rabbit MQ user. |  | 
| `mq.queues.rabbitMQVirtualHost` | string | null | The Rabbit MQ virtual hostname. |  | 
| `mq.queues.sqs.region` | string | eu-west-3 | The AWS Region for the AWS SQS MQ service. |  | 
| `pgmDateFormat` | string | yyyy-MM-dd | The date time format. |  | 
| `pgmTimeFormat` | string | HH.mm.ss | The time format used for pgm (programs) execution. |  | 
| `pgmTimestampFormat` | string | yyyy-MM-dd-HH.mm.ss.SSSSSS | The timestamp format. |  | 
| `program.timeout` | number | -1 | Specifies a timeout for any program/transaction execution in seconds. After this time, the system will try to interrupt the program. |  | 
| `qtemp.cleanup.threshold.hours` | number | 0 | To specify when`qtemp.dblog` is enabled. The db partition lifetime (in hours). |  | 
| `qtemp.dblog` | boolean | false | Whether to enable QTEMP Database logging. |  | 
| `qtemp.uuid.length` | number | 9 | The QTEMP unique id length. |  | 
| `quartz.scheduler.stand-by-if-error` | boolean | false | Specifies whether to trigger job execution if the job scheduler is in standby mode. If true, When enabled job execution is not triggered. |  | 
| `query.useConcatCondition` | boolean | false | Specifies whether key condition is built by key concatenation or not. |  | 
| `reportOutputPath` | string | `/reports` | The report output path. |  | 
| `returnHttp5xxResponseForFailedSyncJob` | boolean | false | Specifies whether to return HTTP response code of 500 series for unsuccessful synchronized job execution. | 4.10.0 | 
| `rollbackOnRTE` | boolean | false | Specifies whether to rollback implicit run unit transaction on runtime exceptions. |  | 
| `sctThreadLimit` | long | 5 | The thread limit for triggering scripts. |  | 
| `server.servlet.session.timeout` | string | 30m | Specifies the session timeout duration. Examples: `60s` (60 seconds), `4m` (4 minutes), `4h` (4 hours). |  | 
| `server.servlet.session.tracking-modes` | string | cookie | Specifies the session tracking modes to use. Possible values are `url`, `cookie`, `ssl`. Multiple values can be specified separated by commas. Note: When deploying on Tomcat, you need to set `cookies=false` in context.xml because Tomcat takes precedence for tracking mode configuration. |  | 
| `spring.aws.application.credentials` | string | null | Load the AWS credentials from the credential profiles file in JICS. |  | 
| `spring.aws.client.bluesam.locks.redis.secret` | string | null | Specifies the credential secret ARN for Bluesam locks Redis cache, see [AWS Transform for mainframe Runtime secrets](ba-runtime-config-app-secrets.md). |  | 
| `spring.aws.client.bluesam.redis.secret` | string | null | Specifies the credential secret ARN for Bluesam Redis cache, see [AWS Transform for mainframe Runtime secrets](ba-runtime-config-app-secrets.md). |  | 
| `spring.aws.client.jcl.checkpoint.redis.secret` | string | null |  Specifies the credential secret ARN for JCL checkpoint mechanism's Redis persistence provider, see [AWS Transform for mainframe Runtime secrets](ba-runtime-config-app-secrets.md).  |  | 
| `spring.aws.client.jics.queues.ts.redis.secret` | string | null | Specifies the credential secret ARN for JICS TS Queues Redis server, see [AWS Transform for mainframe Runtime secrets](ba-runtime-config-app-secrets.md). |  | 
| `spring.aws.client.jics.redis.secret` | string | null |  Specifies the credential secret ARN for JICS Redis server connection factory, see [AWS Transform for mainframe Runtime secrets](ba-runtime-config-app-secrets.md). |  | 
| `spring.jta.enabled` | boolean | false | Standard key. If the datasource support mode is not static-xa, spring JTA transactions autoconfiguration must be disabled. |  | 
| `spring.session.store-type` | string | none | The session cache for high-availability environments. Possible values are`none` or`redis`. Default is`none`. |  | 
| `sqlCodePointShift` | number |  | Optional. The sql code point shift. Shifts the codepoint for control characters that we might encounter when migrating legacy RDBMS data to a modern RDBMS. For example, you can specify`384` to match Unicode character`\u0180`. |  | 
| `sqlConnectionAutoCommitEnabled` | boolean | true | Enables automatic commit of current connection during connection reset operations. When enabled, automatically commits the current connection before switching to a new datasource connection in non-XA environments to prevent connection instability. When disabled, logs a warning message about potential connection issues during reset operations. | 4.10.0 | 
| `sqlIntegerOverflowAllowed` | boolean | false | Specifies whether to allow the SQL integer overflow, meaning whether placing larger values in the host variable is allowed. |  | 
| `startDefaultJob` | string | `false` | Specify whether to initialize default job at first transaction. |  | 
| `stepFailWhenAbend` | boolean | true | Specifies whether to raise an abend if a step fails or completes execution. |  | 
| `stopExecutionWhenProgNotFound` | boolean | true | Specifies whether to stop running if a program isn't found. If set to`true`, interrupts the run if a program is not found. |  | 
| `system.date.format` | string  | MDY | The system date format DATFMT. | --- | 
| `system.date.separator` | string  | / | The system date separator DATSEP.<br />Possible values are slash (`/`), dash (`–`), period (`.`), comma (`,`) or blank (` `). Value needs to be specified in double quotes `""`. | 5.17.0 | 
| `system.qdecfmt` | string |  |  |  | 
| `taskExecutor.allowCoreThreadTimeOut` | boolean | false | Specifies whether to allow core threads to time out in JCIS. This enables dynamic growing and shrinking even in combination with a non-zero queue (since the max pool size will only grow once the queue is full). |  | 
| `taskExecutor.corePoolSize` | number | 5 | When a transaction in a terminal is initiated via a groovy script, a new thread is created. Use this parameter to setup the core pool size. |  | 
| `taskExecutor.maxPoolSize` | number | 10 | When a transaction in a terminal is initiated via a groovy script, a new thread is created. Use this parameter to setup the max pool size (max number of parallel threads). |  | 
| `taskExecutor.queueCapacity` | number | 50 | When a transaction in a terminal is initiated via a groovy script, a new thread is created. Use this parameter to setup the queue size. (= maximum number of pending transactions when`taskExecutor.maxPoolSize` is reached) |  | 
| `tempFilesDirectory` | string | null | Specifies the name of the folder location of the temporary files that are generated. |  | 
| `tempFolderPattern` | string | null | Specifies a pattern that will be used to dynamically build the name of the temporary folder based on the following predefined and customizable information.<br />HOST: the host name.<br />JOBID: the ID of the job.<br />HASHCODE: the hash code of the job context.<br />TIMESTAMP: the pattern to use when getting the timestamp. Target name of the temporary folder is TMP\_DIR\_{tempFolderPattern}. For example, in the case of the following pattern, the name will start with the job ID and end with the “timestamp”: tempFolderPattern: JOBID,HOST=xxxxx,HASHCODE,TIMESTAMP=yyyymmddhhmmss. If the property `tempFolderPattern` is not added to the YAML file or is empty, the name of the temporary folder will be "TMP\_DIR\_" \+ this.hashCode() (DefaultJobContext). |  | 
| `uppercaseUserInput` | boolean | true | Specifies whether user input must be in uppercase.  |  | 
| `useControlMVariable` | boolean | false | Specifies whether to use control-M specification for variable replacement. |  | 
| `xmlGeneratorPrettyFormat` | boolean | true | Determines the formatting style of the generated XML output within the XmlGenerator class. When set to `true`, the XML output is formatted in a human-readable, indented structure (pretty-printed). When set to `false`, the output is in a compact, single-line format without additional whitespace. | 4.8.0 | 

## Available properties for optional web applications
<a name="ba-runtime-key-value-web"></a>

Depending on your modernized application, you might need to configure one or more optional web applications that represent support for dependencies such as z/OS, AS/400, or IMS/MFS. The following tables contain lists of the available key/value parameters for configuring each optional web application.

### gapwalk-utility-pgm.war
<a name="ba-runtime-key-value-web-utility"></a>

This optional web application contains support for Z/OS utility programs.

This table provides an exhaustive view of key/values parameters for this application.


| Key | Type | Default value | Description | Release version | 
| --- | --- | --- | --- | --- | 
| `convertGraphicDataToFullWidth` |  boolean |  true | Specifies whether to convert graphic data to full-width format. |  | 
| `encoding` |  string |  ASCII |  The encoding used in utility programs. Expects a valid encoding `CP1047`,`IBM930`,`ASCII`,`UTF-8`. |  | 
| `forcedDate` |  string |   |  Forces the date to the date provided if there is one. |  | 
| `forcedDateMode` |  string |  |  Specifies the forced date mode. When set to `HYBRID`, the date portion is the configured forced date but the time portion reflects the actual system time. Applies only if `forcedDate` is also set. |  | 
| `frozenDate` |  boolean |  true |  Specifies whether to freeze the date. Applies only if`forcedDate` is also set. |  | 
| `hasGraphic` |  boolean |  false |  Whether the INFUTILB utility needs to handle GRAPHIC DB2 columns. |  | 
| `idcams.deleteFromAllSubfolders` | boolean | false | Whether the IDCAMS DELETE command should also remove matching files from every sub-folder of the files directory. | 5.155.0 | 
| `idcams.encoding.forced` |  string |  |  The encoding used in IDCAMS utility program. Expects a valid encoding `CP1047`, `IBM930`, `ASCII`, `UTF-8`. | 4.4.0 | 
| `idcams.repro.failOnMissingOutput` | boolean | false | If set to true, IDCAMS REPRO will early fail if an output Blusam dataset, having either SHR or OLD disposition, is missing. | 5.185.0 | 
| `jcl.type` |  string |  mvs |  .jcl file type. Allowed values are`jcl` /`vse`. The IDCAMS utility PRINT/REPRO commands return 4 if the file is empty for non-vse jcl. |  | 
| `load.applyRollback` | boolean | false | Set this parameter to `true` to indicate that you want the service to roll back table changes if it encounters an error while loading data into the database. |  | 
| `load.batchSize` |  number |  0 |  The load utility batch size. |  | 
| `load.format.dbDate` |  string |  yyyy-MM-dd |  The load utility database format to use. |  | 
| `load.format.dbTime` |  string |  HH:mm:ss |  The load utility database time to use. |  | 
| `load.format.localDate` |  string |  dd.MM.yyyy\\dd/MM/yyyy\\yyyy-MM-dd |  The load utility local date format to use. |  | 
| `load.format.localTime` |  string |  HH:mm:ss\\HH.mm.ss |  The load utility local time format to use. |  | 
| `load.sqlCodePointShift` |  number |  0s |  The SQL code pointshift for load utility. Runs the shifting characters process. Required when your target database from DB2 is Postgresql. |  | 
| `logging.config` |  Path |  classpath:logback-utility.xml |  Standard key for the reference to the logback configuration file. Other standard logging keys are available too. |  | 
| `primary.datasource` -`driver-class-name` -`url` -`username` -`password` |  Standard spring datasource with subkeys |   |  Contains the connection information for the application database, if not using JNDI. Must have the same configuration as in the modernized application YAML file.<br /> Alternately, use of AWS secrets is strongly encouraged, as explained in [Client database](ba-runtime-config-app-secrets.md#client-database). |  | 
| `spring.datasource.primary.jndi-name` |  string |  jdbc/primary |  The JNDI name (Java Naming And Directory Interface) for the primary datasource, if using JNDI. |  | 
| `spring.jta.enabled` |  boolean |  false |  Standard key. If the datasource support mode is not static-xa, spring JTA transactions auto configuration must be disabled. |  | 
| `sysPunchEncoding` |  string |  ASCII |  The syspunch encoding character set. Expects a valid encoding`CP1047`,`IBM930`,`ASCII`,`UTF-8`. |  | 
| `systin.encoding` |  string |  ASCII |  The encoding character set of SYSTIN file dataset. Expects a valid encoding`CP1047`,`IBM930`,`ASCII`,`UTF-8`. | 4.5.0 | 
| `treatLargeNumberAsInteger` |  boolean |  false |  Specifies whether to treat large numbers as`Integer`. They are treated as`BigDecimal` by default. |  | 
| `unload.bmc.useInto` |  boolean |  false |  Specifies whether to handle INTO bmc control keyword for unload utility. |  | 
| `unload.chunkSize` |  number |  0 |  Chunk size used for unload utility. |  | 
| `unload.columnFiller` |  string |  space |  The unload utility column filler. |  | 
| `unload.computeRecordSizeIfNull` |  boolean |  false | Determines whether to compute the record size if not specified. If specified, the value remains unchanged. |  | 
| `unload.fetchSize` |  number |  0 |  Allows you to tune the fetch size when handling cursors in the unload utility. |  | 
| `unload.format.date` |  string |  MM/dd/yyyy |  If`unload.useDatabaseConfiguration` is enabled, the date format to use in the unload utility. |  | 
| `unload.format.time` |  string |  HH.mm.ss |  If`unload.useDatabaseConfiguration` is enabled, the time format to use in the unload utility. |  | 
| `unload.format.timestamp` |  string |  yyyy-MM-dd-HH.mm.ss.SSSSSS |  If`unload.useDatabaseConfiguration` is enabled, the timestamp format to use in the unload utility. |  | 
| `unload.nbi.whenNotNull` |  hexadecimal |  00 |  The Null Byte Indicator (NBI) value to add when value from database is not null. |  | 
| `unload.nbi.whenNull` |  hexadecimal |  6F |  The Null Byte Indicator (NBI) value to add when value from database is null. |  | 
| `unload.nbi.writeNullIndicator` |  boolean |  false |  Specifies whether to write out the null indicator in the unload output file. |  | 
| `unload.noPad` |  boolean |  true |  Indicates that variable-length character (VARCHAR) fields are to be unloaded without any padding to the maximum length. | 4.5.0 | 
| `unload.sqlCodePointShift` |  number |  0 |  The SQL code pointshift for unload utility. Runs the shifting characters process. Required when your target database from DB2 is Postgresql. |  | 
| `unload.useDatabaseConfiguration` |  boolean |  false |  Specifies whether to use the date or time configuration from application-main.yml in unload utility.  |  | 
| `unload.varCharIsNull` |  boolean |  false |  Use this parameter in INFTILB program, if set to`true` then all not nullable fields with blank (space) values returns an empty string. |  | 
| `zonedMode` |  string |  EBCDIC\_STRICT |  The mode for encoding or decoding zoned data types. Allowed values are`EBCDIC_STRICT` /`EBCDIC_MODIFIED` /`AS400`. |  | 

### gapwalk-cl-command.war
<a name="ba-runtime-key-value-web-cl"></a>

This optional web application contains support for AS/400 utility programs.

This table provides an exhaustive view of key/values parameters for this application.


| Key | Type | Default value | Description | 
| --- | --- | --- | --- | 
|  `commands-off` |  string |   | List of commands to turn off, separated by comma. Allowed values are`PGM_BASIC`,`RCVMSG`,`SNDRCVF`,`CHGVAR`,`QCLRDTAQ`,`RTVJOBA`,`ADDLFM`,`ADDPFM`,`RCVF`,`OVRDBF`,`DLTOVR`,`CPYF`,`SNDDTAQ`. Useful when you want to disable or overwrite an existing program. `PGM_BASIC` is a specific AWS Transform for mainframe Runtime program designed for debugging purposes. | 
|  `encoding` |  string |  ASCII |  The encoding used in utility programs. Expects a valid encoding`CP1047`,`IBM930`,`ASCII`,`UTF-8`... | 
|  `forcedDate` |  string |   | Forces the date to the date provided if there is one. | 
| `forcedDateMode` |  string |   | Specifies the forced date mode. When set to `HYBRID`, the date portion is the configured forced date but the time portion reflects the actual system time. Applies only if `forcedDate` is also set. | 
|  `logging.config` |  Path |  classpath:logback-utility.xml |  Standard key for the reference to the logback configuration file. Other standard logging keys are available too. | 
|  `primary.datasource` \+ -`driver-class-name` \+ -`url` \+ -`username` \+ -`password` |  Standard spring datasource with subkeys |   |  Contains the connection information for the application database, if not using JNDI. Must have the same configuration as in the modernized application YAML file.<br /> Alternately, use of AWS secrets is strongly encouraged, as explained in [Client database](ba-runtime-config-app-secrets.md#client-database). | 
|  `spring.datasource.primary.jndi-name` |  string |  jdbc/primary |  The JNDI name (Java Naming And Directory Interface) for the primary datasource, if using JNDI.  | 
|  `spring.jta.enabled` |  boolean |  false |  Standard key. If the datasource support mode is not static-xa, spring JTA transactions auto configuration must be disabled. | 
|  `zonedMode` |  string |  EBCDIC\_STRICT |  The mode for encoding or decoding zoned data types. Allowed values are`EBCDIC_STRICT` /`EBCDIC_MODIFIED` /`AS400`. | 

### gapwalk-hierarchical-support.war
<a name="ba-runtime-key-value-web-hierarchical"></a>

This optional web application contains IMS/MFS transaction support.

This table provides an exhaustive view of key/values parameters for this application.


| Key | Type | Default value | Description | 
| --- | --- | --- | --- | 
| `jhdb.backend` | string |  | Jhdb backend type. Expected value is `rdbms` | 
|  `jhdb.checkpointPersistence` |  string |  none |  The checkpoint persistence mode. Allowed values are`none` /`add` /`end`. Use`add` to persist checkpoints when a new one is created and added to the registry. Use`end` too persist checkpoint at server shutdown. Any other values disable the persistence. Note that each time a new checkpoint is added to the registry, all the existing checkpoints will be serialized and the file will be erased. It is not an append to the existing data in the file. So depending on the number of checkpoints, it can have some effects on performances. | 
|  `jhdb.configuration.context.encoding` |  string |   |  The JHDB (Java Hierarchical Database) encoding. Expects a valid encoding string`CP1047`,`IBM930`,`ASCII`,`UTF-8`... | 
| `jhdb.keepParent` | boolean | false | Whether to keep \_parent and \_logicalparent during IMS insertion. When set to true the IMS ISRT call will insert \_parent and \_logicalparent into database columns. | 
| `jhdb.query.timeout` | int | -1 | Specifies a timeout for any jhdb transaction execution in seconds. After this time, the system will try to interrupt the program. No timeout is set if the value is -1 (default). | 
| `jhdb.transaction.scope.programs` | string |  | list of programs to be declared as a whole transaction. Separate each program with a comma (`,`). For example:`PCP008,PCT008` | 
|  `logging.config` |  Path |  classpath:logback-utility.xml |  Standard key for the reference to the logback configuration file. Other standard logging keys are available too. | 
| `metadata.datasource` \+ -`driver-class-name` \+ -`url` \+ -`username` \+ -`password` \+ -`type` | string | Standard spring datasource with subkeys | Contains the metadata information for the jhdb database, including psbs, dbds, connections. Alternately, use of AWS secrets is strongly encouraged. | 
|  `spring.jta.enabled` |  boolean |  false |  Standard key. If the datasource support mode is not static-xa, spring JTA transactions auto configuration must be disabled. | 

### gapwalk-gs21.war
<a name="ba-runtime-key-value-web-gs21"></a>

Use this optional web application to run Fujitsu GS21 platform programs in your AWS Mainframe Modernization environment. Install this application only if your modernized workload includes GS21 programs.

The following table describes the key-value parameters for this application.


| Key | Type | Default value | Description | 
| --- | --- | --- | --- | 
| `aim.sockets.socketConfigurations` | list | None | Configures Application Integration Module (AIM) socket connections. Each entry is a socket server configuration or a socket client configuration.<br />Socket server entry keys: `remote` (connection name), `smqn` (Structured Message Queue Name (SMQN) queue name), `port` (socket port).<br />Socket client entry keys: `remote` (remote server name), `targetName` (target server name), `smqn` (SMQN queue name), `port` (local port), `targetPort` (target port), `targetHost` (target IP). | 
| `datasource.gs21Ds` \+ -`driver-class-name` \+ -`url` \+ -`username` \+ -`password` \+ -`type` | Standard Spring datasource with subkeys | None | Stores the connection information for the GS21 database. We recommend using AWS Secrets Manager for database credentials. For more information, see [Client database](ba-runtime-config-app-secrets.md#client-database). | 
| `taskExecutor` \+ -`corePoolSize` \+ -`maxPoolSize` \+ -`queueCapacity` \+ -`allowCoreThreadTimeOut` | Spring thread pool executor configuration | None | Configures the thread pool executor that spawns AIM processes (such as SMQNs, socket handlers, and message reply handlers). | 

## Available properties for the client application
<a name="ba-runtime-key-value-client"></a>

Your modernized application may require specific property configurations for the client Spring application. These properties initialize beans from classes packaged in runtime JAR files. The `application-profile.yaml` file, where the profile value is set during application generation, allows you to configure these properties. The following table lists the key/value parameters available for configuring the client web application that uses beans from classes packaged in the Gapwalk runtime


| Key | Type | Default value | Description | Release version | 
| --- | --- | --- | --- | --- | 
| `blu4iv.dao.cache.enabled` | boolean | false | Enable the In-memory cache. | 4.8.0 | 
| `blu4iv.dao.cache.enabledHits` | boolean | false | Add the tracking of number of requests to the cache. | 4.8.0 | 
| `blu4iv.dao.cache.entries.fileIds` | string |  | The list of database tables to be cached. | 4.8.0 | 
| `blu4iv.dao.cache.entries.programIds` | string |  | The program's identifiers where the cache should be activated for the specified tables. The cache is available for all sub-programs in the execution stacks. | 4.8.0 | 
| `blu4iv.dao.cache.initMaxResults` | number | 10000 | The size of the cache. | 4.8.0 | 
| `blu4iv.dao.data.max` | number | 10 | The size of the internal cache for input DAO operations. This cache exists at the program level (single instance). | 4.9.0 | 
| `blu4iv.dao.sort.function` | string |  | The sort function name for the blu4iv database. | 4.9.0 | 
| `blu4iv.dao.support` | string | JPA | Specifies the data access implementation to use (JPA or JDBC). | 4.9.0 | 
| `blu4iv.dtaara.library.disable` | boolean | false | Controls the usage of library in the context of data area operations. If set to true, library usage is disabled for data area operations, but this does not affect the usage of QTemp. If set to false, library is considered when performing CRUD operations for data area. | 4.5.0 | 
| `blu4iv.librarylist.enabled` | boolean | false | Enable the use of the library list to resolve a file library. | 4.10.0 | 
| `blu4iv.librarylist.libraries` | string |  | The initial list of libraries ordered from left to right. | 4.10.0 | 

### Configure the In-Memory cache for AS400 applications
<a name="ba-runtime-in-memory-cache-as400"></a>

The in-memory cache feature enables users to cache read-only data within memory, significantly improving performance for data-intensive programs. The cache system optimizes performance in three ways: loading data only on first access, creating data access maps on demand, and storing cached data efficiently near program memory. This design minimizes memory overhead while maximizing speed improvements.

```
###################################################################
# Cache configuration for read operations called from DAO classes #
###################################################################
blu4iv:
 dao:
   cache:
     enabled: true
     enabledHits: true
     initMaxResults: 100000
     entries:
     -
       fileIds: [${TABLEA}]
       programIds: [${PROGRAM1}]
     -
       fileIds: [${TABLEB},${TABLEC}]
       programIds: [${PROGRAM2}]
  librarylist:
         enabled: true
         libraries: ["LIBA","LIBC","LIBE"]
```

## Configure API access logging
<a name="ba-runtime-api-access-logging"></a>

The API access logging feature records detailed information about API requests to BAC, JAC, and Gapwalk applications, helping meet security requirements by tracking who accessed what and when.


| Key | Type | Default value | Description | Release version | 
| --- | --- | --- | --- | --- | 
| `api.logging.enabled` | boolean | false | Enables API access logging for BAC, JAC, and Gapwalk applications. When enabled, logs all API requests with details. | 5.0.0 | 

When enabled, user can provide logback file configuration to log API access logs in chosen place using the logger name `api.access`. The logs can include the following MDC fields:


| MDC Field | Description | 
| --- | --- | 
| `api-context` | Where the API is hosted | 
| `api-date` | The date and time when the API request was made | 
| `api-duration` | How long it took to process the API request (milliseconds) | 
| `api-host` | The source address that the API request came from | 
| `api-method` | The type of HTTP request made (e.g., GET, POST, DELETE, ...) | 
| `api-name` | The endpoint/URI that was accessed | 
| `api-retcode` | The status code returned after the API request completed | 
| `api-scheme` | The transfer protocol used, for example, HTTP or HTTPS. | 
| `api-secure` | The security method used to protect the API call (e.g., OAuth2, Token, Anonymous) | 
| `api-sessionid` | A unique identifier for the user's current login session | 
| `api-user` | The username or identifier of the person making the API request | 

To configure a dedicated log file for API access logs, add the following to your logback configuration:

```
<!-- File appender -->
<appender name="ApiAccessFile" class="ch.qos.logback.core.FileAppender">
    <file>logs/main/main-api-access.log</file>
    <immediateFlush>true</immediateFlush>
    <encoder>
        <pattern>%date %X{api-scheme} %X{api-host} %X{api-method} %X{api-name} - Return code: %X{api-retcode} - Start date: %X{api-date} - Duration: %X{api-duration} ms - User: %X{api-user} - SessionId: %X{api-sessionid} - SecureMethod: %X{api-secure} %n</pattern>
    </encoder>
</appender>

<logger name="api.access" level="info" additivity="false">
    <appender-ref ref="ApiAccessFile" />
    <appender-ref ref="CONSOLE" />
</logger>
```

Sample log output:

```
2025-06-13 22:24:36,174 http 127.0.0.1 GET /bac/api/services/rest/bluesamservice/listDataSet - Return code: 200 - Start date: 06-13-2025 22:24:35.863+0200 - Duration: 308 ms - User: velocity_admin - SessionId:
1X1X1X1X1X1X1X1X1X1X1X1X1X1X1X1X- SecureMethod: Oauth2
```

## Configure Distributed Tracing
<a name="ba-runtime-distributed-tracing"></a>

The distributed tracing feature enables end-to-end request tracking across GapWalk applications by propagating traceId and spanId from HTTP requests, allowing correlation of logs across the entire request lifecycle.


| Key | Type | Default value | Description | Release version | 
| --- | --- | --- | --- | --- | 
| `gapwalk.tracing.enabled` | boolean | false | Enables distributed tracing for GapWalk applications. When enabled, propagates traceId and spanId for batch job execution. |  | 

When enabled, the tracing feature propagates trace context. The logs can include the following MDC fields:


| MDC Field | Description | 
| --- | --- | 
| spanId | Unique identifier for the current operation within the trace | 
| traceId | Unique identifier for the entire request flow across all services and threads | 

To configure distributed tracing, update your logback configuration to include traceId and spanId in the log pattern. Add or update the following property:

```
<property name="DEFAULT_LOG_PATTERN"
        value="%date{yyyy-MM-dd HH:mm:ss} %-15.15contextName %-5.5level [%X{traceId:-},%X{spanId:-}] - %-40.40logger{15} - %msg%n" />
```

Sample log output:

```
2026-02-02 20:00:00 default INFO [6966b3c1dc96c2da73be7e2b6f9f25dc,73be7e2b6f9f25dc] - q.t.s.i.TestJobProcessImpl - Length is: 100
```