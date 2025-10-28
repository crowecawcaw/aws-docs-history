End of support notice: On May 20, 2026, AWS
will end support for AWS SimSpace Weaver. After May 20, 2026, you will
no longer be able to access the SimSpace Weaver console or SimSpace Weaver resources.
For more information, see [AWS SimSpace Weaver end of support](simspaceweaver-end-of-support.md "simspaceweaver-end-of-support.md").

# Working with service quotas

This section describes how to work with the service quotas for SimSpace Weaver. **Quotas**
are also called **limits**. For a list of service quotas, see
[SimSpace Weaver endpoints and quotas](service-quotas.md "service-quotas.md"). The APIs
in this section are from the set of **app APIs**. App APIs
are a different than the service APIs. The app APIs are part of the SimSpace Weaver app SDK.
You can find the documentation for the app APIs in the app SDK folder on your local
system:

```
`sdk-folder`\SimSpaceWeaverAppSdk-`sdk-version`\documentation\index.html
```

###### Topics

- [Get the limits for an app](#working-with_quotas_get-app-limits "#working-with_quotas_get-app-limits")
- [Get the amount of resources used by an app](#working-with_quotas_get-app-resources "#working-with_quotas_get-app-resources")
- [Reset metrics](#working-with_quotas_reset-metrics "#working-with_quotas_reset-metrics")
- [Exceeding a limit](#working-with_quotas_exceed-limit "#working-with_quotas_exceed-limit")
- [Running out of memory](#working-with_quotas_out-of-memory "#working-with_quotas_out-of-memory")
- [Best practices](#working-with_quotas_best-practices "#working-with_quotas_best-practices")

## Get the limits for an app

You can use the RuntimeLimits app API to
query the limits for an app.

```
Result<Limit> RuntimeLimit(Application& app, LimitType type)
```

###### Parameters

**Application& app**

A reference to the app.

**LimitType type**

An enum with the following limit types:

```
enum LimitType {
    Unset = 0,
    EntitiesPerPartition = 1,
    RemoteEntityTransfers = 2,
    LocalEntityTransfers = 3
};

```

The following example queries the entity count limit.

```
WEAVERRUNTIME_TRY(auto entity_limit,
    **Api::RuntimeLimit(m\_app, Api::LimitType::EntitiesPerPartition)**)
Log::Info("Entity count limit", entity_limit.value);

```

## Get the amount of resources used by an app

You can call the RuntimeMetrics app API to get the amount of resources used by an app:

```
Result<std::reference_wrapper<const AppRuntimeMetrics>> RuntimeMetrics(Application& app) noexcept
```

###### Parameters

**Application& app**

A reference to the app.

The API returns a reference to a struct that contains the metrics. A counter metric
holds a running total value and only increases. A gauge metric holds a value that can
increase or decrease. The application runtime updates a counter whenever an event increases
the value. The runtime only updates the gauges when you call the API. SimSpace Weaver
guarantees that the reference is valid for the lifetime of the app. Repeat calls to the API
won't change the reference.

```
struct AppRuntimeMetrics {
    uint64_t total_committed_ticks_gauge,

    uint32_t active_entity_gauge,
    uint32_t ticks_since_reset_counter,

    uint32_t load_field_counter,
    uint32_t store_field_counter,

    uint32_t created_entity_counter,
    uint32_t deleted_entity_counter,

    uint32_t entered_entity_counter,
    uint32_t exited_entity_counter,

    uint32_t rejected_incoming_transfer_counter,
    uint32_t rejected_outgoing_transfer_counter
}

```

## Reset metrics

The ResetRuntimeMetrics app API
resets the values in the `AppRuntimeMetrics` struct.

```
Result<void> ResetRuntimeMetrics(Application& app) noexcept
```

The following example demonstrates how you can call ResetRuntimeMetrics
in your app.

```
if (ticks_since_last_report > 100)
{
    auto metrics = WEAVERRUNTIME_EXPECT(Api::RuntimeMetrics(m_app));
    Log::Info(metrics);

    ticks_since_last_report = 0;

    WEAVERRUNTIME_EXPECT(**Api::ResetRuntimeMetrics(m\_app)**);
}

```

## Exceeding a limit

An app API call that exceeds a limit will return an
`ErrorCode::CapacityExceeded`, except for entity transfers. SimSpace Weaver
handles entity transfers asynchronously as part of **Commit**
and BeginUpdate app API operations, so there
isn't a specific operation that returns an error if a transfer fails because of the entity
transfer limit. To detect transfer failures, you can compare the current values of
`rejected_incoming_transfer_counter` and `rejected_outgoing_transfer_counter`
(in the `AppRuntimeMetrics` struct) with their previous values.
Rejected entities won't be in the partition, but the app can still simulate them.

## Running out of memory

SimSpace Weaver uses a garbage collector process to clean up and release freed memory.
It's possible to write data faster than the garbage collector can release memory. If this
happens, write operations might exceed the app's reserved memory limit. SimSpace Weaver
will return an internal error with a message that contains `OutOfMemory`
(and additional details). For more information, see [Spread writes across time](#working-with_quotas_best-practices_spread-writes "#working-with_quotas_best-practices_spread-writes").

## Best practices

The following best practices are general guidelines for designing your apps to avoid
exceeding limits. They might not apply to your specific app design.

### Monitor frequently and slow down

You should monitor your metrics frequently and slow down operations that are close to
reaching a limit.

### Avoid

exceeding subscription limits and transfer limits

If possible, design your simulation to reduce the number of remote
subscriptions and entity transfers. You can use
placement groups to place multiple partitions on the same worker and reduce
the need for remote entity transfers between workers.

### Spread writes across time

The number and size of updates in a tick can have a significant impact on the time
and memory required to commit a transaction. Large memory requirements can cause the
application runtime to run out of memory. You can spread writes across time to lower the
average total size of updates per tick. This can help improve performance and avoid exceeding
limits. We recommend that you don't write more than an average of 12 MB on each tick or 1.5 KB
for each entity.
