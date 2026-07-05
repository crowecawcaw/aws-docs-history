After careful consideration, we have made the decision to close new customer access to **AWS Mainframe Modernization self-managed experience**,
effective June 30, 2026. Existing customers can continue to use the service as normal. AWS continues to invest in security and availability improvements for
AWS Mainframe Modernization self-managed experience, but we do not plan to introduce new features. For more information, see [AWS Mainframe Modernization
availability change](mainframe-modernization-availability-change.md "mainframe-modernization-availability-change.md").

**AWS Mainframe Modernization Service (Managed Runtime Environment experience)** is no longer open to new customers. For
capabilities similar to AWS Mainframe Modernization Service (Managed Runtime Environment experience) explore AWS Mainframe Modernization Service (Self-Managed
Experience). Existing customers can continue to use the service as normal. For more information, see [AWS Mainframe Modernization
availability change](mainframe-modernization-availability-change.md "mainframe-modernization-availability-change.md").

# AWS Transform for mainframe runtime Breaking changes - 5.X

The purpose of this document is to list breaking changes in the AWS Transform for mainframe runtime, for 5.X major version releases, starting with version 5.75.0.
Whenever a component applies to a single legacy environment, the corresponding change is tagged with that environment.

The following environments are used:

- z/OS : IBM mainframe series and assimilated, running on z/OS;
- AS400: IBM iSeries midframes;
- GS21 : Fujitsu GS21 environment;
- ALL (or blank): a change that might concern more than one specific environment;

###### Note

A significant amount of changes concern internal usages of classes, in the AWS Transform for mainframe runtime. They should have no impact on existing customer code.

###### Topics

- [Release 5.125.0 - Breaking changes from 5.75.0](#ba-breaking-changes-5.125.0 "#ba-breaking-changes-5.125.0")

## Release 5.125.0 - Breaking changes from 5.75.0

### Component gapwalk-utility-pgm (5.125.0) - z/OS Only

- Class `com.netfective.bluage.gapwalk.utility.sort.service.sum.AbstractSum`:

  - **Bug fix (z/OS)**: Handle SUM field overflow with OPTION OVFLO=RC0 in DFSORT. When OPTION OVFLO=RC0 is set and a SUM field overflows its capacity, the current accumulated record is output and a new accumulation starts with the current record, instead of truncating the value.
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

- Interface `com.netfective.bluage.gapwalk.bluesam.core.storage.MetadataPersistence`:

  - **Performance optimization (z/OS)**: Improve performance and fix on large KSDS dataloader when append mode is enabled. All known implementations of this interface have been adapted accordingly. This interface is internal to the Blu Age runtime, for BluSam support. The existing 3-parameter method now delegates to the new 4-parameter version with false as default. It should not have any impact on existing customer code.
    Added new public method `boolean buildDatasetIndexes(CoreMetadata metadata, int indexingPageSizeInMb, long expectedRecordsCount, boolean isAppendMode);`

- Interface `com.netfective.bluage.gapwalk.bluesam.LargeKeySequencedDataSet`:

  - **Performance optimization (z/OS)**: Improve performance and fix on large KSDS dataloader when append mode is enabled. All known implementations of this interface, `com.netfective.bluage.gapwalk.bluesam.core.LargeKSDS` and `com.netfective.bluage.gapwalk.bluesam.core.LargeESDS`, have been adapted accordingly. Any class implementing `LargeKeySequencedDataSet` must now implement this new method. For non-append behavior, delegate to the existing 2-parameter version or pass false for `isAppendMode` internally.
    Added new public method `void buildIndexes(int indexingPageSizeInMb, long expectedRecordsCount, boolean isAppendMode);`

### Component gapwalk-bluesam-services-pgsql (5.125.0) - z/OS Only

- Interface `com.amazonaws.bluage.gapwalk.bluesam.services.util.large.ReadWorker`:

  - **Performance optimization (z/OS)**: Improve performance and fix on large KSDS dataloader when append mode is enabled. The only known implementation, `com.amazonaws.bluage.gapwalk.bluesam.services.pgsql.util.PgsqlReadWorker`, has been adapted accordingly. Any class implementing `ReadWorker` must now implement these 3 methods.
    Added new public method `DataSource getDataSource();`

Added new public method `boolean isMultiSchemaEnabled();`

Added new public method `String getFileType();`
