

# Telemetry ingestion
<a name="telemetry-integration-stack"></a>

The telemetry ingestion layer connects IoT Core to the MSK cluster.

## IoT Rules
<a name="iot-rules"></a>

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

 **Command response rule (JSON):** 

```
SELECT * FROM 'cms/commands/+/response'
```

 **Action:** Invoke Command Response Handler Lambda. Processes JSON command responses from MQTT Direct simulators.

 **Command response rule (FWE protobuf):** 

```
SELECT encode(*, 'base64') AS b64_payload, topic(3) AS vehicleId
FROM 'cms/commands/things/+/executions/+/response/protobuf'
```

 **Action:** Invoke Command Response Handler Lambda. The rule base64-encodes the binary protobuf payload and extracts the VIN from `topic(3)`. The Lambda decodes the `CommandResponse` protobuf and maps the FWE status enum to a string status (SUCCEEDED, FAILED, TIMEOUT).

 **VPC destination:** 
+ VPC: InfrastructureStack VPC
+ Subnets: Private subnets
+ Security group: Allows traffic to MSK

## Message transformation
<a name="message-transformation"></a>

IoT Rules can transform messages before sending to MSK:

```
SELECT
  vin,
  timestamp() as serverTimestamp,
  * as payload
FROM 'cms/telemetry/+'
```