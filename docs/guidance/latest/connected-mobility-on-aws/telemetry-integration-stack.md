# Telemetry ingestion

The telemetry ingestion layer connects IoT Core to the MSK cluster.

## IoT Rules

Rules route telemetry messages to MSK topics.

**Telemetry rule:**

```
SELECT * FROM 'cms/telemetry/+'
```

**Action:** Send to MSK topic `cms-telemetry`

**FleetWise telemetry rule:**

```
SELECT encode(*, 'base64') AS data, topic(4) AS thingName, timestamp() AS ts
FROM 'cms/fleetwise/vehicles/+/signals'
```

**Action:** Send to MSK topic `fw-telemetry-raw` and S3 backup bucket

**FleetWise checkin rule:**

```
SELECT encode(*, 'base64') AS data, topic(4) AS thingName, timestamp() AS ts
FROM 'cms/fleetwise/vehicles/+/checkins'
```

**Action:** Send to MSK topic `fw-checkin`

The FleetWise IoT rules use `topic(4)` to extract the vehicle VIN from the MQTT topic path and `encode(*, 'base64')` to preserve the binary protobuf payload for downstream Flink processing.

**VPC destination:**

- VPC: InfrastructureStack VPC
- Subnets: Private subnets
- Security group: Allows traffic to MSK

## Message transformation

IoT Rules can transform messages before sending to MSK:

```
SELECT
  vin,
  timestamp() as serverTimestamp,
  * as payload
FROM 'cms/telemetry/+'
```
