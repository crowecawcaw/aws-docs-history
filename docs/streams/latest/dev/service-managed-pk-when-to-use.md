

# When to use service-managed record distribution
<a name="service-managed-pk-when-to-use"></a>

Use service-managed record distribution for stateless streaming workloads where record ordering is not required:
+ Log aggregation
+ Metrics collection
+ IoT telemetry
+ Clickstream analytics

Continue using customer-managed partition keys for stateful workloads that require ordering guarantees:
+ Database change data capture (CDC) where updates to the same row must be processed sequentially
+ Financial transaction processing where account-level ordering is required
+ Session-based analytics where all events from a user session must be processed together
+ Any application where business logic depends on processing related records in the order they were produced