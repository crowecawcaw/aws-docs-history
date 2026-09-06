

# Trip lifecycle
<a name="trip-lifecycle"></a>

The TripProcessor detects trip boundaries from ignition signal transitions. It does not rely on simulator-provided trip IDs or engine event strings, making it compatible with both MQTT Direct and FleetWise Edge telemetry.

## Detection flow
<a name="trip-detection-flow-platform"></a>

The TripProcessor consumes from the `cms-telemetry-trips` Kafka topic (routed by the EventDrivenTelemetryProcessor) and uses the `ignitionOn` signal to detect trip boundaries:


| Previous Ignition | Current Ignition | Action | 
| --- | --- | --- | 
| OFF (or null) | ON |  **Start trip**: Generate trip ID, create ACTIVE trip in DynamoDB, set active trip in Redis | 
| ON | ON |  **Continue trip**: Accumulate route points and metrics, flush to DynamoDB periodically | 
| ON | OFF |  **End trip**: Update trip status to COMPLETED, calculate final metrics, clear active trip from Redis | 
| OFF | OFF | Ignore (no active trip) | 

## Trip ID generation
<a name="trip-id-generation"></a>

When a new trip starts, the processor generates a trip ID using the pattern:

```
{vehicleId}-{timestamp}-{randomHex}
```

For example: `VEH-0049-1709751600000-fc9567` 

If the incoming telemetry message already contains a `tripId` (from the simulator), the processor uses that value instead. This ensures trip IDs are consistent between the simulator’s intent and the processor’s detection.

## State management
<a name="trip-state-management"></a>

The TripProcessor maintains trip state in three locations:

1.  **In-memory ConcurrentHashMap** — Maps `vehicleId` → `tripId` for the currently active trip. This is the primary lookup, avoiding DynamoDB reads on every message. Uses `putIfAbsent` to prevent race conditions when multiple messages arrive simultaneously for the same vehicle.

1.  **Redis** — The active trip ID is written to `vehicle:{vehicleId}:activeTrip` on trip start and deleted on trip end. This allows the TelemetryProcessor (a separate Flink application) to tag telemetry records with the correct `tripId` without querying DynamoDB. The FWTelemetryProcessor also reads this cache to tag FleetWise telemetry with trip IDs.

1.  **DynamoDB** — The authoritative trip record. Written on trip start (PutItem), updated periodically during the trip (UpdateItem every 5 messages to append route points and update metrics), and finalized on trip end (UpdateItem with COMPLETED status and final metrics).

## Trip DynamoDB record
<a name="trip-dynamodb-record"></a>

A trip record progresses through these states:

 **On trip start (ignition ON):** 

```
{
  "tripId": "VEH-0049-1709751600000-fc9567",
  "vehicleId": "VEH-0049",
  "driverId": "DRV-001",
  "status": "ACTIVE",
  "startTime": 1709751600000,
  "startLocation": {"lat": 40.7128, "lng": -74.0060},
  "route": [{"lat": 40.7128, "lng": -74.0060, "ts": 1709751600000}],
  "maxSpeed": 0,
  "totalDistance": 0,
  "telemetryCount": 1,
  "source": "mqtt_direct"
}
```

 **During trip (periodic flush every 5 messages):** 

The processor uses `UpdateItem` (not `PutItem`) to append route points and update running metrics without overwriting the full record. This eliminates race conditions from concurrent writes.

 **On trip end (ignition OFF):** 

```
{
  "tripId": "VEH-0049-1709751600000-fc9567",
  "vehicleId": "VEH-0049",
  "driverId": "DRV-001",
  "status": "COMPLETED",
  "startTime": 1709751600000,
  "endTime": 1709755200000,
  "startLocation": {"lat": 40.7128, "lng": -74.0060},
  "endLocation": {"lat": 40.7589, "lng": -73.9851},
  "route": [{"lat": 40.7128, "lng": -74.0060, "ts": 1709751600000}, "..."],
  "maxSpeed": 65.5,
  "totalDistance": 12.3,
  "duration": 3600,
  "telemetryCount": 120,
  "source": "mqtt_direct"
}
```

## DynamoDB write optimization
<a name="trip-write-optimization"></a>

The stateful design reduces DynamoDB operations compared to a stateless approach:


| Operation | Stateless (per message) | Stateful (current) | 
| --- | --- | --- | 
| DynamoDB reads | 2-3 (GetItem \+ GSI query) | 0 (in-memory \+ Redis) | 
| DynamoDB writes | 1 PutItem (full record) | 1 UpdateItem every 5 messages | 
| 20-message trip total | \~60 reads \+ 20 writes | 0 reads \+ 5 writes | 

Only the TripProcessor writes to the trips table. The TelemetryProcessor tags telemetry records with `tripId` for querying but does not write to the trips table. This single-writer pattern prevents data clobbering between processors.