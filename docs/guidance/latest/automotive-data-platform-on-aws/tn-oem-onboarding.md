# OEM Onboarding

Adding a new OEM cloud-to-cloud integration requires no changes to the normalization pipeline code. The entire process is configuration-driven — you create a transform manifest that maps the OEM’s proprietary signal names and units to the canonical schema, build a connector that authenticates to the OEM’s API, and the existing Flink processor handles the rest.

## Step 1: Understand the OEM’s API

Before building the integration, you need to understand how the OEM exposes telemetry data. Work with the OEM’s developer program to obtain:

- **API documentation** — REST endpoints, authentication flow, rate limits, and data formats
- **Sample telemetry payload** — A real or representative JSON response showing the signal names, nesting structure, and units the OEM uses
- **Data dictionary** — What each field means, what units it uses, and how frequently it updates
- **Authentication details** — OAuth 2.0 token endpoint, client credentials grant type, scopes, and any partner enrollment requirements

Some OEMs expose REST APIs that you poll on a schedule. Others push data to your endpoint via WebSocket or webhook. The connector pattern you choose depends on which model the OEM supports.

## Step 2: Create the transform manifest

The transform manifest is a JSON file that tells the OEMTelemetryProcessor how to extract and convert each signal from the OEM’s payload into the canonical format. There are three ways to create one:

**Option A: Auto-generate from sample data (recommended)** — Upload a sample OEM telemetry payload to the Data Processing API. The API analyzes the JSON structure, matches fields against the signal catalog, and generates a validated manifest automatically.

```
curl -X POST https://{data-processing-api}/oem-transforms/generate \
  -H "Content-Type: application/json" \
  -d '{
    "oem_name": "acme-motors",
    "sample_data": { ... raw OEM JSON ... }
  }'
```

The API returns a generated manifest with detected field mappings and validation warnings for any fields that don’t match the signal catalog. Review the output, adjust any mappings, then upload:

```
curl -X POST https://{data-processing-api}/manifests \
  -H "Content-Type: application/json" \
  -d '{
    "name": "acme-motors-transform.json",
    "manifest": { ... generated manifest ... }
  }'
```

The upload endpoint validates the manifest structure before writing to S3.

**Option B: OEM Integration Wizard (Fleet Manager UI)** — Platform admins can use the visual wizard in the Fleet Manager console under Data Processing → Transform Manifests → Add Integration. The wizard walks through a multi-step flow:

1. **Connection setup** — Enter the OEM name and select the connection type:

| Connection Type          | Description                                                          | Infrastructure                                       |
| ------------------------ | -------------------------------------------------------------------- | ---------------------------------------------------- |
| REST API (Polling)       | Poll OEM REST endpoints on a schedule (for example, every 5 minutes) | AWS Lambda + Amazon EventBridge                      |
| Streaming (gRPC/Pub-Sub) | Receive data via gRPC stream or pub-sub feed from the OEM            | Amazon ECS Fargate                                   |
| WebSocket (Push)         | OEM pushes telemetry to your WebSocket endpoint in real time         | Amazon ECS Fargate + Application Load Balancer + TLS |
| MQTT                     | OEM publishes to an MQTT broker topic                                | AWS IoT Core                                         |

Then select the data encoding format: JSON, Protocol Buffers (Protobuf), Apache Avro, or Raw/Custom. 2. **Authentication** — Configure how the connector authenticates to the OEM’s API:

    * **OAuth 2.0** — Token endpoint, client ID, client secret, resource ID, and tenant. Credentials are stored in AWS Secrets Manager.
    * **API Key** — Static key passed as a header.
    * **Basic Auth** — Username and password.

3. **Sample data** — Paste a sample telemetry JSON payload from the OEM’s API, an optional sample event payload, and an optional data dictionary. For Protobuf-encoded OEMs, upload the `.proto` schema file instead.
4. **Signal mapping** — The wizard calls the Data Processing API to auto-detect field mappings between the OEM’s payload and the signal catalog. Each detected mapping shows the OEM field name, the matched canonical field, and the suggested unit conversion. You can review, adjust, or add mappings before proceeding.
5. **Deploy** — The wizard generates the transform manifest, uploads it to Amazon S3, and registers the data source configuration. The OEMTelemetryProcessor picks up the new manifest automatically — no Flink restart required.

**Option C: Manual creation** — Write the manifest JSON by hand and upload directly to S3:

```
aws s3 cp acme-motors-transform.json \
  s3://{manifests-bucket}/transforms/acme-motors-transform.json
```

Regardless of which option you use, each mapping specifies:

- **source_signal** — The OEM’s field name (for human reference)
- **cms_field** — The canonical `json_field` from the signal catalog (for example, `speed`, `odometer`, `lat`)
- **source_path** — A JSONPath-like expression to extract the value from the OEM’s nested JSON structure
- **unit_conversion** — An optional conversion function to apply (for example, `mps_to_mph` if the OEM reports speed in meters per second)
- **data_type** — The expected output type (`float`, `boolean`, `string`)

The manifest also defines how to extract the vehicle identifier from the OEM’s payload and how to parse timestamps.

```
{
  "manifest_version": "1.0.0",
  "source_name": "acme-motors",
  "vehicle_id_extraction": {
    "strategy": "json_path",
    "path": "vehicleIdentifier"
  },
  "timestamp_field": "recordedAt",
  "timestamp_format": "iso8601",
  "signal_mappings": [
    {
      "source_signal": "VEHICLE_SPEED",
      "cms_field": "speed",
      "source_path": "metrics.speedKph",
      "unit_conversion": "kph_to_mph",
      "data_type": "float"
    },
    {
      "source_signal": "MILEAGE",
      "cms_field": "odometer",
      "source_path": "metrics.odometerKm",
      "unit_conversion": "km_to_miles",
      "data_type": "float"
    },
    {
      "source_signal": "GPS_LAT",
      "cms_field": "lat",
      "source_path": "location.latitude",
      "data_type": "float"
    },
    {
      "source_signal": "GPS_LNG",
      "cms_field": "lng",
      "source_path": "location.longitude",
      "data_type": "float"
    },
    {
      "source_signal": "ENGINE_ON",
      "cms_field": "ignitionOn",
      "source_path": "status.engineRunning",
      "data_type": "boolean"
    }
  ]
}
```

Upload the manifest to Amazon S3:

```
aws s3 cp acme-motors-transform.json \
  s3://{manifests-bucket}/transforms/acme-motors-transform.json
```

The `OEMTelemetryProcessor` loads manifests from S3 at startup and caches them. When a message arrives with `oem_source: "acme-motors"`, the processor selects this manifest and applies the mappings.

## Step 3: Store credentials

Store the OEM’s OAuth 2.0 credentials in AWS Secrets Manager:

```
aws secretsmanager create-secret \
  --name cms/oem/acme-motors \
  --secret-string '{
    "tokenEndpoint": "https://api.acme-motors.com/oauth/token",
    "clientId": "<client-id>",
    "clientSecret": "<client-secret>",
    "scope": "vehicle.telemetry.read"
  }'
```

The connector Lambda or Fargate task reads these credentials at runtime to authenticate with the OEM’s API.

## Step 4: Build the connector

The connector is responsible for authenticating to the OEM’s cloud API, fetching telemetry data, and writing the raw payload to the `cms-telemetry-oem` Kafka topic. Choose the pattern that matches the OEM’s API model:

**REST polling connector** — For OEMs that expose request/response APIs. Deploy an AWS Lambda function triggered by Amazon EventBridge on a schedule (for example, every 5 minutes). The Lambda authenticates via OAuth 2.0, calls the OEM’s REST endpoints, and writes each response as a message to Kafka with the `oem_source` field set.

**Streaming connector (gRPC/Pub-Sub)** — For OEMs that provide a gRPC stream or pub-sub feed. Deploy an Amazon ECS Fargate task that maintains a persistent connection to the OEM’s streaming endpoint, receives incoming data, and writes each message to Kafka.

**WebSocket connector** — For OEMs that push telemetry to your endpoint via WebSocket. Deploy an Amazon ECS Fargate task behind an Application Load Balancer with TLS termination. The OEM connects to your public endpoint and pushes data in real time. The task receives each message and writes it to Kafka.

**MQTT connector** — For OEMs that publish to an MQTT broker. Configure an AWS IoT Core rule on the OEM’s topic pattern that routes messages to the `cms-telemetry-oem` Kafka topic via the existing MSK VPC destination. This requires no custom code — only an IoT rule definition.

In both cases, the connector writes the raw OEM JSON to Kafka without any transformation. The `oem_source` field is the only required addition — it tells the OEMTelemetryProcessor which transform manifest to use:

```
{
  "oem_source": "acme-motors",
  "vehicleIdentifier": "ACME-V-12345",
  "recordedAt": "2026-03-19T14:30:00Z",
  "metrics": {
    "speedKph": 105.3,
    "odometerKm": 72841.2
  },
  "location": {
    "latitude": 47.6062,
    "longitude": -122.3321
  },
  "status": {
    "engineRunning": true
  }
}
```

## Step 5: Deploy and validate

After deploying the connector, verify the end-to-end flow:

1. Confirm the connector is writing to the `cms-telemetry-oem` Kafka topic
2. Check the OEMTelemetryProcessor logs to verify it loaded the transform manifest and is producing normalized output to `cms-telemetry-preprocessed`
3. Query the REST API for a vehicle from the new OEM — the response should include normalized signals with canonical field names and units
4. Verify the vehicle appears on the Fleet Manager map if GPS coordinates are mapped

No Flink restart is required. The OEMTelemetryProcessor detects new manifests in S3 and loads them automatically.
