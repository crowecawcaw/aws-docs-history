

**AWS Mainframe Modernization self-managed experience** is no longer open to new customers. For capabilities similar to AWS Mainframe Modernization self-managed experience, explore capabilities from vendor-direct offerings and from AWS Transform. Existing customers can continue to use the service as normal. For more information, see [AWS Mainframe Modernization availability change](https://docs.aws.amazon.com/m2/latest/userguide/mainframe-modernization-availability-change.html). 

**AWS Mainframe Modernization Service (Managed Runtime Environment experience)** is no longer open to new customers. For capabilities similar to AWS Mainframe Modernization Service (Managed Runtime Environment experience) explore AWS Mainframe Modernization Service (Self-Managed Experience). Existing customers can continue to use the service as normal. For more information, see [AWS Mainframe Modernization availability change](https://docs.aws.amazon.com/m2/latest/userguide/mainframe-modernization-availability-change.html). 

# AWS Transform for mainframe runtime Breaking changes - 5.X
<a name="ba-breaking-changes"></a>

The purpose of this document is to list breaking changes in the AWS Transform for mainframe runtime, for 5.X major version releases, starting with version 5.75.0. Whenever a component applies to a single legacy environment, the corresponding change is tagged with that environment.

The following environments are used:
+ z/OS : IBM mainframe series and assimilated, running on z/OS;
+ AS400: IBM iSeries midframes;
+ GS21 : Fujitsu GS21 environment;
+ ALL (or blank): a change that might concern more than one specific environment;

**Note**  
A significant amount of changes concern internal usages of classes, in the AWS Transform for mainframe runtime. They should have no impact on existing customer code.

**Topics**
+ [Release 5.274.0 - Breaking changes from 5.194.0](#ba-breaking-changes-5.274.0)
+ [Release 5.125.0 - Breaking changes from 5.75.0](#ba-breaking-changes-5.125.0)

## Release 5.274.0 - Breaking changes from 5.194.0
<a name="ba-breaking-changes-5.274.0"></a>

### Generated-code signature changes
<a name="ba-breaking-changes-5.274.0-generated-code-signatures"></a>

These methods are emitted directly into generated modernized-application code by the transformation engine, so a re-transformation binds against the new signature. There are three.
+ **`InputDeviceHelper.writeInto(...)` — third parameter type changed**
  + File: `velocity-framework/GapWalk-Runtime-Legacy-Statements/src/main/java/com/netfective/bluage/gapwalk/runtime/statements/InputDeviceHelper.java`
  + Why it matters: The generator emits `InputDeviceHelper.writeInto(...)` calls into generated code for COBOL ACCEPT ... FROM CONSOLE, passing a writable field slice as the third argument. Re-transformed applications bind to the new `RecordAdaptable` parameter.

  Before

  ```
  void writeInto(ExecutionContext executionContext, Context context, RangeReference rangeReference)
  ```

  After

  ```
  void writeInto(ExecutionContext executionContext, Context context, RecordAdaptable recordAdaptable)
  ```
+ **`DataUtils.formatBytes(RangeReference, RangeReference)` — return type changed**
  + File: `velocity-framework/GapWalk-DataSimplifier/src/main/java/com/netfective/bluage/gapwalk/datasimplifier/utils/DataUtils.java`
  + Why it matters: The generator emits `DataUtils.formatBytes(...)` into generated code and now consumes the returned `int` as the length argument of a generated `SequentialFile.write(record, int)` call (GS21 print-mode VARYING-without-DEPENDING-ON write path). Re-transformed applications depend on the new `int` return.

  Before

  ```
  public static void formatBytes(RangeReference source, RangeReference target)
  ```

  After

  ```
  public static int formatBytes(RangeReference source, RangeReference target)
  ```
+ **`Blu4UserSpace.withTransferSize(...)` — parameter type widened**
  + File: `velocity-framework/gapwalk-runtime-userspace-support/src/main/java/com/netfective/bluage/gapwalk/userspace/support/data/Blu4UserSpace.java`
  + Why it matters: Two generators emit `withTransferSize(<field reference>)` for the AS/400 QUSCRTUS (Create User Space) API, binding the reference overload. The erased method descriptor changed from `(ElementaryRangeReference)` to `(RangeReference)`, so pre-built customer artifacts that call the old descriptor require recompilation. Source is compatible on re-transformation (the new body still handles an `ElementaryRangeReference` argument).

  Before

  ```
  public Blu4UserSpace withTransferSize(ElementaryRangeReference transferSize)
  ```

  After

  ```
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

  ```
  public void addRecord(byte[] record)
  ```

  After

  ```
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