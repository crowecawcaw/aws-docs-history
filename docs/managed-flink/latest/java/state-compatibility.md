# State compatibility guide for Flink 2.2 upgrades

When upgrading from Flink 1.x to Flink 2.2, state compatibility issues may prevent your
application from restoring from snapshots. This guide helps you identify potential
compatibility issues and provides migration strategies.

## Understanding state compatibility changes

Amazon Managed Service for Apache Flink 2.2 introduces several serialization changes that affect state
compatibility. The following are the major ones:

- **Kryo Version Upgrade**: Apache Flink 2.2
  upgrades the bundled Kryo serializer from version 2 to version 5. Because Kryo
  v5 uses a different binary encoding format than Kryo v2, any operator state that
  was serialized via Kryo in a Flink 1.x savepoint cannot be restored in Flink
  2.2.
- **Java Collections Serialization**: In Flink
  1.x, Java collections (such as `HashMap`, `ArrayList`,
  and `HashSet`) within POJOs were serialized using Kryo. Flink 2.2
  introduces collection-specific optimized serializers that are incompatible with
  the Kryo-serialized state from 1.x. Applications using Java collections with
  POJO or Kryo serializers in 1.x cannot restore this state in Flink 2.2.
  See Flink [documentation](https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/dev/datastream/fault-tolerance/serialization/types_serialization/ "https://nightlies.apache.org/flink/flink-docs-release-2.2/docs/dev/datastream/fault-tolerance/serialization/types_serialization/") for more details on data types and serialization.
- **Kinesis Connector Compatibility**: The Kinesis
  Data Streams (KDS) connector version lower than 5.0 maintains state that is not
  compatible with the Flink 2.2 Kinesis connector version 6.0. You must migrate
  to connector version 5.0 or greater before your upgrade.

## Serialization compatibility reference

Review all state declarations in your application and match serialization types to the
table below. If any state type is incompatible, see the
[State migration](#state-compat-migration "#state-compat-migration")
section before proceeding with your upgrade.

Serialization compatibility reference| Serialization Type | Compatible? | Details |
| --- | --- | --- |
| Avro (`SpecificRecord`, `GenericRecord`) | Yes | Uses its own binary format independent of Kryo. Ensure you are using<br>Flink's native Avro type information, not Avro registered as a Kryo<br>serializer. |
| Protobuf | Yes | Uses its own binary encoding independent of Kryo. Verify schema<br>changes follow backward-compatible evolution rules. |
| POJOs without collections | Yes | Handled by Flink's POJO serializer — but only if the class meets all<br>POJO criteria: public class, public no-arg constructor, all fields<br>either public or accessible via getters/setters, and all field types<br>themselves serializable by Flink. A POJO that violates any of these<br>silently falls back to Kryo and becomes incompatible. |
| Custom TypeSerializers | Yes | Compatible only if your serializer does not delegate to Kryo<br>internally. |
| SQL and Table API state | Yes (with caveat) | Uses Flink's internal serializers. However, Apache Flink does not<br>guarantee state compatibility between major versions for Table API<br>applications. Test in a non-production environment first. |
| POJOs with Java collections (`HashMap`,<br>`ArrayList`, `HashSet`) | No | In Flink 1.x, collections within POJOs were serialized via Kryo v2.<br>Flink 2.2 introduces dedicated collection serializers whose binary<br>format is incompatible with the Kryo v2 format. |
| Scala case classes | No | Serialized via Kryo in Flink 1.x. The Kryo v2 to v5 upgrade changes<br>the binary format. |
| Java records | No | Typically fall back to Kryo serialization in Flink 1.x. Verify by<br>testing with `disableGenericTypes()`. |
| Third-party library types | No | Types without a registered custom serializer fall back to Kryo. The<br>Kryo v2 to v5 binary format change breaks compatibility. |
| Any type using Kryo fallback | No | If Flink cannot handle a type with a built-in or registered<br>serializer, it falls back to Kryo. All Kryo-serialized state from 1.x<br>is incompatible with 2.2. |

## Diagnostic methods

You can either identify state compatibility issues proactively by looking at
application logs or inspecting logs after the [UpdateApplication API](../apiv2/API_UpdateApplication.md "../apiv2/API_UpdateApplication.md") operation.

**Identify Kryo fallback in your application**

You can use the following regex pattern in your logs to identify Kryo fallback in
your application:

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

If the upgrade fails using the UpdateApplication API, the following exceptions might signal
that you are encountering serializer-based state incompatibility:

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

- Review all state declarations in your application
- Check for POJOs with collections (`HashMap`,
  `ArrayList`, `HashSet`)
- Verify serialization methods for each state type
- Create a prod replica application and test state compatibility using
  UpdateApplication API on this replica
- If state is incompatible, select a strategy from
  [State migration](#state-compat-migration "#state-compat-migration")
- Enable auto-rollback in your production Flink application
  configuration

## State migration

**Rebuild complete state**

Best for applications where state can be rebuilt from source data.

If your application can rebuild state from source data:

1. Stop the Flink 1.x application
2. Upgrade to Flink 2.x with updated code
3. Start with `SKIP_RESTORE_FROM_SNAPSHOT`
4. Allow application to rebuild state

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

1. **Always use Avro or Protobuf for complex
   state** — These provide schema evolution and are
   Kryo-independent
2. **Avoid collections in POJOs** — Use
   Flink's native `ListState` and `MapState`
   instead
3. **Test state restoration locally** —
   Before production upgrade, test with actual snapshots
4. **Take snapshots frequently** —
   Especially before major version upgrades
5. **Enable auto-rollback** — Configure
   your MSF application to automatically rollback on failure
6. **Document your state types** — Maintain
   documentation of all state types and their serialization
   methods
7. **Monitor checkpoint sizes** — Growing
   checkpoint sizes may indicate serialization issues

## Next steps

**Plan your upgrade**: See
[Upgrading to Flink 2.2: Complete guide](flink-2-2-upgrade-guide.md "flink-2-2-upgrade-guide.md").

For questions or issues during migration, see the [Troubleshoot Managed Service for Apache Flink](troubleshooting.md "troubleshooting.md") or contact AWS Support.
