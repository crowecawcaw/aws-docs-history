

**AWS Mainframe Modernization self-managed experience** is no longer open to new customers. For capabilities similar to AWS Mainframe Modernization self-managed experience, explore capabilities from vendor-direct offerings and from AWS Transform. Existing customers can continue to use the service as normal. For more information, see [AWS Mainframe Modernization availability change](https://docs.aws.amazon.com/m2/latest/userguide/mainframe-modernization-availability-change.html). 

**AWS Mainframe Modernization Service (Managed Runtime Environment experience)** is no longer open to new customers. For capabilities similar to AWS Mainframe Modernization Service (Managed Runtime Environment experience) explore AWS Mainframe Modernization Service (Self-Managed Experience). Existing customers can continue to use the service as normal. For more information, see [AWS Mainframe Modernization availability change](https://docs.aws.amazon.com/m2/latest/userguide/mainframe-modernization-availability-change.html). 

# AWS Transform for mainframe runtime Breaking changes - 5.X

The purpose of this document is to list breaking changes in the AWS Transform for mainframe runtime, for 5.X major version releases, starting with version 5.75.0. Whenever a component applies to a single legacy environment, the corresponding change is tagged with that environment.

The following environments are used:
+ z/OS : IBM mainframe series and assimilated, running on z/OS;
+ AS400: IBM iSeries midframes;
+ GS21 : Fujitsu GS21 environment;
+ ALL (or blank): a change that might concern more than one specific environment;

**Note**  
A significant amount of changes concern internal usages of classes, in the AWS Transform for mainframe runtime. They should have no impact on existing customer code.

**Topics**
+ [Release 5.323.0 - Breaking changes from 5.274.0](#ba-breaking-changes-5.323.0)
+ [Release 5.274.0 - Breaking changes from 5.194.0](#ba-breaking-changes-5.274.0)
+ [Release 5.125.0 - Breaking changes from 5.75.0](#ba-breaking-changes-5.125.0)

## Release 5.323.0 - Breaking changes from 5.274.0
<a name="ba-breaking-changes-5.323.0"></a>

### Runtime API signature changes
<a name="ba-breaking-changes-5.323.0-generated-code-signatures"></a>

To keep your custom code compiling, update calls to the following public runtime signatures. This release keeps no overload with the old signature, and the runtime and the generated code already use the new signatures:
+ **`PreparedStatementSupport.describePreparedStatement(...)` — parameter type widened**
  + Files: `velocity-framework/GapWalk-Runtime/src/main/java/com/netfective/bluage/gapwalk/rt/db/PreparedStatementSupport.java` (interface) and `velocity-framework/GapWalk-Runtime-Database-Support/src/main/java/com/netfective/bluage/gapwalk/database/support/query/PreparedStatementSupportImpl.java` (implementation).
  + Why it matters: This release widens the parameter to its supertype `RangeReference`. Callers stay source-compatible, but you must recompile them. Classes that implement or override the old signature no longer compile.

  Before

  ```java
  public void describePreparedStatement(RecordEntity sqlda)
  ```

  After

  ```java
  public void describePreparedStatement(RangeReference sqlda)
  ```
+ **`ElasticSQLDA` constructor and `setValue(...)` — parameters changed**
  + File: `velocity-framework/GapWalk-Runtime-Database-Support/src/main/java/com/netfective/bluage/gapwalk/database/support/ElasticSQLDA.java`.
  + Why it matters: The constructor now takes the SQLCA and the `ISqlda` interface. `setValue` now reads the value from a `ResultSet` column and declares `SQLException`, so callers must handle it.

  Before

  ```java
  public ElasticSQLDA(SQLDA sqlda, ExecutionContext executionContext)
  public void setValue(int idSQLVAR, byte[] value)
  ```

  After

  ```java
  public ElasticSQLDA(ISqlca sqlca, ISqlda sqlda, ExecutionContext executionContext)
  public void setValue(int idSQLVAR, ResultSet resultSet, int columnIndex) throws SQLException
  ```
+ **`Blu4ivTableManager.lock(...)`, `unlock(...)`, `close(...)` — parameter added (AS400)**
  + File: `velocity-framework/gapwalk-runtime-blu4iv-support/src/main/java/com/netfective/bluage/gapwalk/rt/blu4iv/dao/Blu4ivTableManager.java`.
  + Why it matters: Record locking now takes commitment control into account. Each method has a new trailing `underCommitmentControl` parameter.

  Before

  ```java
  public boolean lock(String fileId, IRecordObject ro)
  public boolean unlock(IRecordObject ro, String fileId)
  public int close(EOpenMode openMode, String fileId, String partitionName)
  ```

  After

  ```java
  public boolean lock(String fileId, IRecordObject ro, boolean underCommitmentControl)
  public boolean unlock(IRecordObject ro, String fileId, boolean underCommitmentControl)
  public int close(EOpenMode openMode, String fileId, String partitionName, boolean underCommitmentControl)
  ```
+ **`EnterBuilder.from(...)` — parameter type changed (z/OS)**
  + File: `velocity-framework/GapWalk-Jics/src/main/java/com/netfective/bluage/gapwalk/rt/jics/io/EnterBuilder.java`.
  + Why it matters: This release widens the parameter to its supertype `RecordAdaptable`. Callers stay source-compatible, but you must recompile them. Subclasses that override the old signature with `@Override` no longer compile.

  Before

  ```java
  public EnterBuilder from(RangeReference from)
  ```

  After

  ```java
  public EnterBuilder from(RecordAdaptable from)
  ```
+ **`BluesamRedisCache` and `BluesamRedisCacheProvider` constructors — parameter added**
  + Files: `velocity-framework/gapwalk-bluesam/gapwalk-bluesam-redis/src/main/java/com/netfective/bluage/gapwalk/bluesam/redis/BluesamRedisCache.java` and `BluesamRedisCacheProvider.java` in the same folder.
  + Why it matters: The 12-argument `BluesamRedisCache` constructor and the 13-argument `BluesamRedisCacheProvider` constructor now take a trailing `boolean scopedClearEnabled`. A 14-argument `BluesamRedisCache` variant adds `boolean orderedTracking`. The 8-, 9-, and 10-argument `BluesamRedisCache` constructors and the 8-, 10-, and 12-argument `BluesamRedisCacheProvider` constructors are unchanged.

  Before

  ```java
  public BluesamRedisCache(Cache cache, RedisTemplate<Object, Object> template, RedissonClient redissonClient,
      BluesamRedisCodec bluesamRedisCodec, long pageSizeInBytes, long timeToLiveMillis, boolean useAsyncBatch,
      boolean useBatchInMemoryAtomic, int deleteAllBatchSize, int readBatchSize, ClearStrategy clearStrategy,
      int clearBatchSize)
  
  public BluesamRedisCacheProvider(CacheManager cacheManager, RedisTemplate<Object, Object> template,
      RedissonClient redissonClient, BluesamRedisCodec bluesamRedisCodec, long pageSizeInBytes, long timeToLiveMillis,
      boolean useAsyncBatch, boolean useBatchInMemoryAtomic, int deleteAllBatchSize, int readBatchSize,
      ClearStrategy clearStrategy, int clearBatchSize, int indexCacheMaxCount)
  ```

  After

  ```java
  public BluesamRedisCache(Cache cache, RedisTemplate<Object, Object> template, RedissonClient redissonClient,
      BluesamRedisCodec bluesamRedisCodec, long pageSizeInBytes, long timeToLiveMillis, boolean useAsyncBatch,
      boolean useBatchInMemoryAtomic, int deleteAllBatchSize, int readBatchSize, ClearStrategy clearStrategy,
      int clearBatchSize, boolean scopedClearEnabled)
  
  public BluesamRedisCacheProvider(CacheManager cacheManager, RedisTemplate<Object, Object> template,
      RedissonClient redissonClient, BluesamRedisCodec bluesamRedisCodec, long pageSizeInBytes, long timeToLiveMillis,
      boolean useAsyncBatch, boolean useBatchInMemoryAtomic, int deleteAllBatchSize, int readBatchSize,
      ClearStrategy clearStrategy, int clearBatchSize, int indexCacheMaxCount, boolean scopedClearEnabled)
  ```
+ **Sort utility formatters `HexConvertFormatter`, `JfyFormatter`, `JfyUtils.justifyField(...)` — parameters changed (z/OS)**
  + Folder: `velocity-framework/GapWalk-Utility-Pgm/src/main/java/com/netfective/bluage/gapwalk/utility/sort/service/external/format/subformatter/`.
  + Why it matters: `HexConvertFormatter` now takes the charset. The JFY (justify) formatter and its helper were reworked to support the JFY options, so their parameter lists changed.

  Before

  ```java
  public HexConvertFormatter(int inputIndex, int length, int outputIndex)
  
  public JfyFormatter(int inputIndex, int inputLength, String shiftCond, String leadCond, String trailCond,
      String preblankCond, Charset charset)
  
  public static byte[] justifyField(byte[] record, int fieldStart, int fieldLength, String shift, byte[] trail,
      byte[] lead, Charset charset)
  ```

  After

  ```java
  public HexConvertFormatter(int inputIndex, int length, int outputIndex, Charset charset)
  
  public JfyFormatter(int outputIndex, int inputIndex, int inputLength, Map<String, String> options, Charset charset)
  
  public static byte[] justifyField(byte[] field, boolean right, int outputLength, byte[] lead, byte[] trail,
      Set<Byte> preblank, byte space)
  ```

### Removed public members
<a name="ba-breaking-changes-5.323.0-removed-members"></a>

This release removes the following public methods, with no replacement:
+ `com.netfective.bluage.gapwalk.utility.sort.TranscodeTool#extractTypeBloc(List<String> lines)` (z/OS). The RECORD TYPE now comes from the catalog.
+ `com.netfective.bluage.gapwalk.utility.sort.service.external.ExternalSort#getTypeBloc()` and `#setTypeBloc(String)` (z/OS).
+ `com.netfective.bluage.gapwalk.utility.sort.service.external.ExternalSortTasklet#getTypeBloc()` and `#setTypeBloc(String)` (z/OS).
+ `com.netfective.bluage.gapwalk.utility.sort.service.external.format.Printer#setColFormat(String)` and `#setColLenght(int)` (z/OS). `setCol(boolean)` is kept.
+ `com.netfective.bluage.gapwalk.bluesam.concurrent.locks.BluesamBlocksRegistry#syncDatasetLocksRegistry(String datasetName)` (z/OS). `syncRecordLocksRegistry(String, Long)` is kept.
+ `com.netfective.bluage.gapwalk.database.support.mappers.RowMapperHelper#handleLengthOverflowAndIndicatorVariable(Configuration, int, ElementaryRangeReference, RangeReference, int, SqlcaVersion)`.

### Removed public types
<a name="ba-breaking-changes-5.323.0-removed-types"></a>

This release removes the GS21 program `EMSGN`, with no replacement. The following types of `velocity-framework/GapWalk-Gs21` no longer exist:
+ `com.netfective.bluage.gapwalk.gs21.program.emsgn.Emsgn`
+ `com.netfective.bluage.gapwalk.gs21.program.emsgn.EmsgnConfiguration` (bean `EmsgnContextConfiguration`)
+ `com.netfective.bluage.gapwalk.gs21.program.emsgn.EmsgnContext`

### New abstract members in public interfaces and abstract classes
<a name="ba-breaking-changes-5.323.0-interface-additions"></a>

If your class implements or extends one of these types directly, you must implement the new member. This release adapts all known implementations in the runtime.
+ Interface `com.netfective.bluage.gapwalk.rt.db.metadata.IDatabaseMetadata` (z/OS): added `boolean hasPrimaryKey(String schemaName, String tableName);`
+ Interface `com.netfective.bluage.gapwalk.rt.call.MainProgramRunner`: added `MainProgramRunner withDefaultReturnCode(int returnCode);`
+ Interface `com.netfective.bluage.gapwalk.rt.jics.resources.File` (z/OS): added `String getDefinedDsName();`
+ Interface `com.netfective.bluage.gapwalk.datasimplifier.entity.ElementaryRangeReference`: added `void setSizeError(boolean sizeError);`
+ Abstract class `com.netfective.bluage.gapwalk.utility.dsnutilb.CopyTask` (z/OS): added `protected abstract void dumpQueryToFile(String query, String copyDdn) throws SQLException, IOException;`

### Configuration-property changes
<a name="ba-breaking-changes-5.323.0-configuration-properties"></a>

This release doesn't rename or remove any existing configuration property. It adds the following properties, which are on by default and change existing behavior. To keep the 5.274.0 behavior, you set them to `false`.
+ **`bluesam.applyDependingOnRecordLength` (default `true`) (z/OS)**
  + Impact: Runtime · Behavior change (Blusam files declared with RECORD VARYING DEPENDING ON).
  + Change: For a file declared with RECORD VARYING DEPENDING ON, the runtime now writes and rewrites each ESDS or KSDS record with the length held by its DEPENDING ON field. Previously, it used the full record length. A DEPENDING ON value outside the range from 1 to the maximum record length is a record size error (FILE STATUS 44).
  + Action: To write records with their full length, as in 5.274.0, set `bluesam.applyDependingOnRecordLength: false`.
+ **`bluesam.redis.scopedClearEnabled` (default `true`)**
  + Impact: Runtime · Action required for rolling deployments that share a Redis cache.
  + Change: With the Blusam Redis cache, a dataset DELETE/REUSE or EMPTY now evicts only the keys that the dataset tracks, instead of scanning the whole Redis keyspace. At startup, one node of the fleet indexes the keys already present in Redis, once.
  + Why it matters: Nodes that run 5.274.0 write cache keys without tracking them. While such nodes share the Redis instance with 5.323.0 nodes, a scoped clear skips their keys. As a result, nodes can read stale records.
  + Action: Use the same value on every node that shares the Redis instance. During a rolling deployment, set `bluesam.redis.scopedClearEnabled: false` until no node runs an older version, and then enable it on all nodes.

## Release 5.274.0 - Breaking changes from 5.194.0
<a name="ba-breaking-changes-5.274.0"></a>

### Generated-code signature changes
<a name="ba-breaking-changes-5.274.0-generated-code-signatures"></a>

These methods are emitted directly into generated modernized-application code by the transformation engine, so a re-transformation binds against the new signature. There are three.
+ **`InputDeviceHelper.writeInto(...)` — third parameter type changed**
  + File: `velocity-framework/GapWalk-Runtime-Legacy-Statements/src/main/java/com/netfective/bluage/gapwalk/runtime/statements/InputDeviceHelper.java`
  + Why it matters: The generator emits `InputDeviceHelper.writeInto(...)` calls into generated code for COBOL ACCEPT ... FROM CONSOLE, passing a writable field slice as the third argument. Re-transformed applications bind to the new `RecordAdaptable` parameter.

  Before

  ```java
  void writeInto(ExecutionContext executionContext, Context context, RangeReference rangeReference)
  ```

  After

  ```java
  void writeInto(ExecutionContext executionContext, Context context, RecordAdaptable recordAdaptable)
  ```
+ **`DataUtils.formatBytes(RangeReference, RangeReference)` — return type changed**
  + File: `velocity-framework/GapWalk-DataSimplifier/src/main/java/com/netfective/bluage/gapwalk/datasimplifier/utils/DataUtils.java`
  + Why it matters: The generator emits `DataUtils.formatBytes(...)` into generated code and now consumes the returned `int` as the length argument of a generated `SequentialFile.write(record, int)` call (GS21 print-mode VARYING-without-DEPENDING-ON write path). Re-transformed applications depend on the new `int` return.

  Before

  ```java
  public static void formatBytes(RangeReference source, RangeReference target)
  ```

  After

  ```java
  public static int formatBytes(RangeReference source, RangeReference target)
  ```
+ **`Blu4UserSpace.withTransferSize(...)` — parameter type widened**
  + File: `velocity-framework/gapwalk-runtime-userspace-support/src/main/java/com/netfective/bluage/gapwalk/userspace/support/data/Blu4UserSpace.java`
  + Why it matters: Two generators emit `withTransferSize(<field reference>)` for the AS/400 QUSCRTUS (Create User Space) API, binding the reference overload. The erased method descriptor changed from `(ElementaryRangeReference)` to `(RangeReference)`, so pre-built customer artifacts that call the old descriptor require recompilation. Source is compatible on re-transformation (the new body still handles an `ElementaryRangeReference` argument).

  Before

  ```java
  public Blu4UserSpace withTransferSize(ElementaryRangeReference transferSize)
  ```

  After

  ```java
  public Blu4UserSpace withTransferSize(RangeReference transferSize)
  ```

### Configuration-property changes
<a name="ba-breaking-changes-5.274.0-configuration-properties"></a>

None. No existing transform, generation, or runtime configuration property was renamed, removed, or had its default value changed. All property changes in the release are net-new, opt-in keys whose defaults preserve prior behavior.

### Dependency / deployment changes
<a name="ba-breaking-changes-5.274.0-dependency-deployment"></a>
+ **RabbitMQ client is no longer bundled**
  + Impact: Runtime · Action required (RabbitMQ users only)
  + Change: The `com.rabbitmq:amqp-client` library was unbundled from the runtime (to clear a CVE and a GPL-2.0 license gate). RabbitMQ is now accessed through reflection behind the runtime's messaging interfaces.
  + Why it matters: A deployment that uses a RabbitMQ broker (`ims.messages`, `jics.queues`, `dataqueue.queues`, or `blu4ivmq.queues.broker = rabbitmq`) will fail at runtime (`RabbitMQUnavailableException`) because the jar is absent. The default internal queueing is unaffected. This is a classpath change only — the customer-facing messaging interfaces (`MqQueueingConsumer`, `JicsQueueingConsumer`, the IMS message-queue base) did not change.
  + Action: RabbitMQ users must supply a CVE-free `amqp-client` jar (5.35.0 or later) on the runtime classpath, the same way Oracle and IBM MQ drivers are provided.

## Release 5.125.0 - Breaking changes from 5.75.0
<a name="ba-breaking-changes-5.125.0"></a>

### Component gapwalk-utility-pgm (5.125.0) - z/OS Only
<a name="ba-breaking-changes-5.125.0-gapwalk-utility-pgm"></a>
+ Class `com.netfective.bluage.gapwalk.utility.sort.service.sum.AbstractSum`:
  + **Bug fix (z/OS)**: Handle SUM field overflow with OPTION OVFLO=RC0 in DFSORT. When OPTION OVFLO=RC0 is set and a SUM field overflows its capacity, the current accumulated record is output and a new accumulation starts with the current record, instead of truncating the value.

  Method `addRecord(byte[])` return type changed from `void` to `boolean`. Returns true if records were added, false if overflow occurred and OPTION OVFLO=RC0 was set (records not added). Any custom code overriding or calling this method may need to be updated accordingly.

  Before

  ```java
  public void addRecord(byte[] record)
  ```

  After

  ```java
  public boolean addRecord(byte[] record)
  ```

### Component gapwalk-bluesam-core (5.125.0) - z/OS Only
<a name="ba-breaking-changes-5.125.0-gapwalk-bluesam-core"></a>
+ Interface `com.netfective.bluage.gapwalk.bluesam.core.storage.MetadataPersistence`:
  + **Performance optimization (z/OS)**: Improve performance and fix on large KSDS dataloader when append mode is enabled. All known implementations of this interface have been adapted accordingly. This interface is internal to the Blu Age runtime, for BluSam support. The existing 3-parameter method now delegates to the new 4-parameter version with false as default. It should not have any impact on existing customer code.

  Added new public method `boolean buildDatasetIndexes(CoreMetadata metadata, int indexingPageSizeInMb, long expectedRecordsCount, boolean isAppendMode);`
+ Interface `com.netfective.bluage.gapwalk.bluesam.LargeKeySequencedDataSet`:
  + **Performance optimization (z/OS)**: Improve performance and fix on large KSDS dataloader when append mode is enabled. All known implementations of this interface, `com.netfective.bluage.gapwalk.bluesam.core.LargeKSDS` and `com.netfective.bluage.gapwalk.bluesam.core.LargeESDS`, have been adapted accordingly. Any class implementing `LargeKeySequencedDataSet` must now implement this new method. For non-append behavior, delegate to the existing 2-parameter version or pass false for `isAppendMode` internally.

  Added new public method `void buildIndexes(int indexingPageSizeInMb, long expectedRecordsCount, boolean isAppendMode);`

### Component gapwalk-bluesam-services-pgsql (5.125.0) - z/OS Only
<a name="ba-breaking-changes-5.125.0-gapwalk-bluesam-services-pgsql"></a>
+ Interface `com.amazonaws.bluage.gapwalk.bluesam.services.util.large.ReadWorker`:
  + **Performance optimization (z/OS)**: Improve performance and fix on large KSDS dataloader when append mode is enabled. The only known implementation, `com.amazonaws.bluage.gapwalk.bluesam.services.pgsql.util.PgsqlReadWorker`, has been adapted accordingly. Any class implementing `ReadWorker` must now implement these 3 methods.

  Added new public method `DataSource getDataSource();`

  Added new public method `boolean isMultiSchemaEnabled();`

  Added new public method `String getFileType();`