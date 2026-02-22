# Understand telemetry data

Telemetry data is delivered as Base64-encoded JSON records to your Kinesis Data Streams stream.
Each record contains information collected during your satellite contact, including metadata
about the contact and the sampled telemetry measurements.

## Data format overview

Each telemetry record contains the following components:

Telemetry type and version

Identifies the specific type of telemetry data and its schema version. This allows
you to parse different telemetry types appropriately. For more information about
schema versioning, see
[Schema versioning and evolution](#telemetry.understanding-data.schema-evolution "#telemetry.understanding-data.schema-evolution").

Scope ID

A unique identifier for the scope of the telemetry. This
allows you to correlate telemetry data with specific contacts.

Metadata

Contextual information about the telemetry.

Data

The sampled telemetry measurements specific to the telemetry type.

**Partition key**

Telemetry records are delivered to your Kinesis Data Streams stream with a partition key in the format:

```
SCOPE#`scopeId`#TELEMETRY_ID#`telemetryId`#TELEMETRY_VERSION#`telemetryVersion`
```

This partition key ensures that all telemetry of a given type for a single contact is delivered to the
same shard within your Kinesis Data Streams stream, providing best effort ordering for that contact's telemetry stream.

## Pointing telemetry

Pointing telemetry provides information about antenna pointing direction during satellite
contacts. This telemetry type is always sent during a contact.

**Data fields**

sampleTimestamp

Time when the telemetry data was sampled, in ISO-8601 format in UTC with millisecond
precision.

azimuth

Actual azimuth angle of the antenna in degrees.

elevation

Actual elevation angle of the antenna in degrees.

commandedAzimuth

Commanded azimuth angle in degrees. This is the target azimuth angle the antenna
is attempting to achieve.

commandedElevation

Commanded elevation angle in degrees. This is the target elevation angle the antenna
is attempting to achieve.

###### Note

The actual antenna position may differ from the commanded position due to
physical limitations or mechanical delays during the contact.

**Metadata fields**

groundStation

Name of the ground station (for example, "Ohio 1").

satelliteId

Identifier of the satellite resource in AWS Ground Station.

contactId

Identifier of the contact.

**Example JSON**

```
{
  "telemetryTypeAndVersion": "POINTING#1.0.0",
  "telemetryType": "POINTING",
  "telemetryVersion": "1.0.0",
  "scopeId": "12345678-1234-1234-1234-123456789012",
  "metadata": {
    "groundStation": "Ohio 1",
    "satelliteId": "87654321-4321-4321-4321-210987654321",
    "contactId": "12345678-1234-1234-1234-123456789012"
  },
  "data": {
    "sampleTimestamp": "2025-12-08T12:00:00.123Z",
    "azimuth": 180.5,
    "elevation": 45.2,
    "commandedAzimuth": 180.0,
    "commandedElevation": 45.0
  }
}
```

## Tracking telemetry

Tracking telemetry provides information about antenna tracking status and tracking errors.
This telemetry type is sent when autotracking is enabled in your tracking config and when
the antenna is actively using autotrack.

###### Note

If the `autotrack` parameter in your TrackingConfig is set to
`REMOVED`, no tracking telemetry will be delivered. For more information
about tracking configs, see
[Tracking Config](how-it-works.md#how-it-works.config-tracking "how-it-works.md#how-it-works.config-tracking").

**Data fields**

sampleTimestamp

Time when the telemetry data was sampled, in ISO-8601 format in UTC with millisecond
precision.

trackingStatus

Current tracking status of the antenna. Possible values include `TRACKING`,
`ACQUIRING`, and `MASKED`.

trackingErrorAzimuth

Tracking error in the azimuth axis, measured in degrees.

trackingErrorElevation

Tracking error in the elevation axis, measured in degrees.

###### Note

The tracking error values represent adjustments from the ephemeris-based program track
that AWS Ground Station applies during autotracking to maximize signal strength.

**Metadata fields**

Tracking telemetry includes the same metadata fields as pointing telemetry:
`groundStation`, `satelliteId`, and `contactId`.

**Example JSON**

```
{
  "telemetryTypeAndVersion": "TRACKING#1.0.0",
  "telemetryType": "TRACKING",
  "telemetryVersion": "1.0.0",
  "scopeId": "12345678-1234-1234-1234-123456789012",
  "metadata": {
    "groundStation": "Ohio 1",
    "satelliteId": "87654321-4321-4321-4321-210987654321",
    "contactId": "12345678-1234-1234-1234-123456789012"
  },
  "data": {
    "sampleTimestamp": "2025-12-08T12:00:00.123Z",
    "trackingStatus": "TRACKING",
    "trackingErrorAzimuth": 0.2,
    "trackingErrorElevation": 0.1
  }
}
```

## Reading data from Kinesis Data Streams stream

Telemetry data is delivered to your Kinesis Data Streams stream and can be consumed using standard stream
consumption patterns. When reading data from your stream, keep the following considerations
in mind.

**Base64 decoding**

Data in Kinesis Data Streams stream is Base64-encoded. You must decode the data before parsing it as JSON.
For more information, see
[Working with Amazon Kinesis Data Streams](../../../streams/latest/dev/working-with-streams.md "../../../streams/latest/dev/working-with-streams.md").

**Using the Kinesis Data Viewer**

For quick access to your telemetry data, the Kinesis Data Streams stream console offers a Data Viewer feature.
When using this feature:

- Telemetry delivery can occur to any shard within your stream.
- The default starting position reads from the latest records in the shard.
- You may need to adjust the selected shard and use the "At timestamp" starting
  position to view received records.

**Using the Kinesis Client Library**

The Kinesis Client Library (KCL) manages many of the complexities associated with consuming data
from Kinesis Data Streams stream, including shard management, checkpointing, and load balancing. We recommend
using KCL for production telemetry consumption applications.

For more information, see
[Developing Consumers
Using the Kinesis Client Library](../../../streams/latest/dev/kcl.md "../../../streams/latest/dev/kcl.md").

**Best practices for consumption**

- **Minimize latency** - Use Enhanced Fan-Out to read
  from Kinesis Data Streams stream with dedicated throughput and lower latency compared to polling. For
  more information, see
  [Developing Enhanced Fan-Out Consumers](../../../streams/latest/dev/enhanced-consumers.md "../../../streams/latest/dev/enhanced-consumers.md").
- **Dedicated stream** - Use a dedicated Kinesis Data Streams stream for
  your AWS Ground Station telemetry integration. Sharing a stream with other applications can
  cause write throughput saturation and telemetry delivery failures.
- **On-demand capacity** - Deploy your Kinesis Data Streams stream in
  on-demand provisioning mode to allow automatic scaling of shards based on throughput.
- **Monitor throughput** - Monitor your stream for
  throttling using CloudWatch metrics. For more information, see
  [Monitoring Amazon Kinesis Data Streams](../../../streams/latest/dev/monitoring-with-cloudwatch.md "../../../streams/latest/dev/monitoring-with-cloudwatch.md").

## Schema versioning and evolution

Telemetry schemas are versioned to support evolution over time. The
`telemetryVersion` field in each record indicates the schema version.

**Handling schema changes**

- New telemetry types may be introduced in the future.
- Existing telemetry types may receive new versions with breaking changes.
- Your applications should be tolerant of unknown telemetry types and versions.
- Parse the `telemetryTypeAndVersion`, `telemetryType`,
  and `telemetryVersion` fields to determine how to process each record.

We recommend implementing version-aware payload serialization that can handle multiple schema
versions gracefully, allowing your applications to continue functioning when new versions
are introduced.
