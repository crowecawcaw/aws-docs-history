

# State compatibility guide for Flink 2.2 upgrades
<a name="state-compatibility"></a>

When upgrading from Flink 1.x to Flink 2.2, state compatibility issues may prevent your application from restoring from snapshots. This guide helps you identify potential compatibility issues and provides migration strategies.

## Understanding state compatibility changes
<a name="state-compat-understanding"></a>

Amazon Managed Service for Apache Flink 2.2 introduces several serialization changes that affect state compatibility. The following are the major ones:
+ **Kryo Version Upgrade**: Apache Flink 2.2 upgrades the bundled Kryo serializer from version 2 to version 5. Because Kryo v5 uses a different binary encoding format than Kryo v2, any operator state that was serialized via Kryo in a Flink 1.x savepoint cannot be restored in Flink 2.2.
+ **Java Collections Serialization**: In Flink 1.x, Java collections (such as `HashMap`, `ArrayList`, and `HashSet`) within POJOs were serialized using Kryo. Flink 2.2 introduces collection-specific optimized serializers that are incompatible with the Kryo-serialized state from 1.x. Applications using Java collections with POJO or Kryo serializers in 1.x cannot restore this state in Flink 2.2. See Flink [documentation](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/dev/datastream/fault-tolerance/serialization/types_serialization/) for more details on data types and serialization.
+ **Kinesis Connector Compatibility**: The Kinesis Data Streams (KDS) connector version lower than 5.0 maintains state that is not compatible with the Flink 2.2 Kinesis connector version 6.0. You must migrate to connector version 5.0 or greater before your upgrade.

## Serialization compatibility reference
<a name="state-compat-reference"></a>

Review all state declarations in your application and match serialization types to the table below. If any state type is incompatible, see the [State migration](#state-compat-migration) section before proceeding with your upgrade.


**Serialization compatibility reference**  

| Serialization Type | Compatible? | Details | 
| --- | --- | --- | 
| Avro (SpecificRecord, GenericRecord) | Yes | Uses its own binary format independent of Kryo. Ensure you are using Flink's native Avro type information, not Avro registered as a Kryo serializer. | 
| Protobuf | Yes | Uses its own binary encoding independent of Kryo. Verify schema changes follow backward-compatible evolution rules. | 
| POJOs without collections | Yes | Handled by Flink's POJO serializer — but only if the class meets all POJO criteria: public class, public no-arg constructor, all fields either public or accessible via getters/setters, and all field types themselves serializable by Flink. A POJO that violates any of these silently falls back to Kryo and becomes incompatible. | 
| Custom TypeSerializers | Yes | Compatible only if your serializer does not delegate to Kryo internally. | 
| SQL and Table API state | Yes (with caveat) | Uses Flink's internal serializers. However, Apache Flink does not guarantee state compatibility between major versions for Table API applications. Test in a non-production environment first. | 
| POJOs with Java collections (HashMap, ArrayList, HashSet) | No | In Flink 1.x, collections within POJOs were serialized via Kryo v2. Flink 2.2 introduces dedicated collection serializers whose binary format is incompatible with the Kryo v2 format. | 
| Scala case classes | No | Serialized via Kryo in Flink 1.x. The Kryo v2 to v5 upgrade changes the binary format. | 
| Java records | No | Typically fall back to Kryo serialization in Flink 1.x. Verify by testing with disableGenericTypes(). | 
| Third-party library types | No | Types without a registered custom serializer fall back to Kryo. The Kryo v2 to v5 binary format change breaks compatibility. | 
| Any type using Kryo fallback | No | If Flink cannot handle a type with a built-in or registered serializer, it falls back to Kryo. All Kryo-serialized state from 1.x is incompatible with 2.2. | 

## Diagnostic methods
<a name="state-compat-diagnostics"></a>

You can either identify state compatibility issues proactively by looking at application logs or inspecting logs after the [UpdateApplication API](https://docs.aws.amazon.com/managed-flink/latest/apiv2/API_UpdateApplication.html) operation.

**Identify Kryo fallback in your application**

You can use the following regex pattern in your logs to identify Kryo fallback in your application:

```
Class class (?<className>[^\s]+) cannot be used as a POJO type
```

Sample log:

```
Class class org.apache.flink.streaming.connectors.kinesis.model.SequenceNumber
cannot be used as a POJO type because not all fields are valid POJO fields,
and must be processed as GenericType. Please read the Flink documentation on
"Data Types & Serialization" for details of the effect on performance and
schema evolution.
```

If the upgrade fails using the UpdateApplication API, the following exceptions might signal that you are encountering serializer-based state incompatibility:

**IndexOutOfBoundsException**

```
Caused by: java.lang.IndexOutOfBoundsException: Index 116 out of bounds for length 1
    at java.base/jdk.internal.util.Preconditions.outOfBounds(Unknown Source)
    at java.base/jdk.internal.util.Preconditions.outOfBoundsCheckIndex(Unknown Source)
    at java.base/jdk.internal.util.Preconditions.checkIndex(Unknown Source)
    at java.base/java.util.Objects.checkIndex(Unknown Source)
    at java.base/java.util.ArrayList.get(Unknown Source)
    at com.esotericsoftware.kryo.util.MapReferenceResolver.getReadObject(MapReferenceResolver.java:77)
    at com.esotericsoftware.kryo.Kryo.readReferenceOrNull(Kryo.java:923)
    ... 23 more
```

**StateMigrationException (POJOSerializer)**

```
Caused by: org.apache.flink.util.StateMigrationException: The new state serializer
(org.apache.flink.api.java.typeutils.runtime.PojoSerializer@8bf85b5d) must not be
incompatible with the old state serializer
(org.apache.flink.api.java.typeutils.runtime.PojoSerializer@3282ee3).
```

## Pre-upgrade checklist
<a name="state-compat-checklist"></a>
+ Review all state declarations in your application
+ Check for POJOs with collections (`HashMap`, `ArrayList`, `HashSet`)
+ Verify serialization methods for each state type
+ Create a prod replica application and test state compatibility using UpdateApplication API on this replica
+ If state is incompatible, select a strategy from [State migration](#state-compat-migration)
+ Enable auto-rollback in your production Flink application configuration

## State migration
<a name="state-compat-migration"></a>

**Rebuild complete state**

Best for applications where state can be rebuilt from source data.

If your application can rebuild state from source data:

1. Stop the Flink 1.x application

1. Upgrade to Flink 2.x with updated code

1. Start with `SKIP_RESTORE_FROM_SNAPSHOT`

1. Allow application to rebuild state

```
aws kinesisanalyticsv2 start-application \
    --application-name MyApplication \
    --run-configuration '{
        "ApplicationRestoreConfiguration": {
            "ApplicationRestoreType": "SKIP_RESTORE_FROM_SNAPSHOT"
        }
    }'
```

## Best practices
<a name="state-compat-best-practices"></a>

1. **Always use Avro or Protobuf for complex state** — These provide schema evolution and are Kryo-independent

1. **Avoid collections in POJOs** — Use Flink's native `ListState` and `MapState` instead

1. **Test state restoration locally** — Before production upgrade, test with actual snapshots

1. **Take snapshots frequently** — Especially before major version upgrades

1. **Enable auto-rollback** — Configure your MSF application to automatically rollback on failure

1. **Document your state types** — Maintain documentation of all state types and their serialization methods

1. **Monitor checkpoint sizes** — Growing checkpoint sizes may indicate serialization issues

## Next steps
<a name="state-compat-next-steps"></a>

**Plan your upgrade**: See [Upgrading to Flink 2.2: Complete guide](flink-2-2-upgrade-guide.md).

For questions or issues during migration, see the [Troubleshoot Managed Service for Apache Flink](troubleshooting.md) or contact AWS Support.