# Work with telemetry

AWS Ground Station telemetry delivers near real-time metrics from AWS Ground Station antennas
during your satellite contacts. You can use telemetry data to monitor contact
performance, detect anomalies, and make informed decisions about your satellite communications.

## How telemetry works

To use telemetry, you configure a _TelemetrySinkConfig_ that
specifies where AWS Ground Station should deliver telemetry data. You then add this config to
your mission profile using the `telemetrySinkConfigArn` field.
During contacts that use a telemetry-enabled mission profile, AWS Ground Station streams telemetry
data to your account.

The telemetry delivery process works as follows:

1. You create a Kinesis Data Streams stream in your AWS account to receive telemetry data. The
   stream must be created in the same account and region from which you
   schedule your contacts.
2. You create an IAM role that grants AWS Ground Station permission to write data to your stream.
3. You create a TelemetrySinkConfig that references your stream and IAM role.
4. You add the TelemetrySinkConfig to your mission profile.
5. You list and reserve contacts using the new telemetry-enabled mission profile.
6. During contacts using this mission profile, AWS Ground Station streams telemetry data to your
   Kinesis Data Streams stream in near real-time.
7. You consume and process the telemetry data from your stream using AWS services
   or your own applications.

## Available telemetry types

AWS Ground Station provides the following telemetry types during contacts:

###### Note

AWS Ground Station is working on expanding the number of supported telemetry types

Pointing telemetry

Provides information about antenna pointing direction during satellite contacts.
This telemetry type is always sent during a contact and includes actual and
commanded azimuth and elevation angles. For more information, see
[Pointing telemetry](telemetry.md#telemetry.understanding-data.pointing "telemetry.md#telemetry.understanding-data.pointing").

Tracking telemetry

Provides information about antenna tracking status and tracking errors. This
telemetry type is sent when autotracking is enabled in your tracking config.
For more information, see
[Tracking telemetry](telemetry.md#telemetry.understanding-data.tracking "telemetry.md#telemetry.understanding-data.tracking").

## Regional availability

Telemetry is available in all AWS Regions where AWS Ground Station operates. During contact execution,
telemetry will be delivered from the AWS Ground Station antenna to the region you scheduled your contact
from, providing cross-region support.

For a complete list of AWS Ground Station Regions and ground station locations, see
[AWS Ground Station Locations](aws-ground-station-antenna-locations.md "aws-ground-station-antenna-locations.md").

###### Topics

- [Set up telemetry](telemetry.md "telemetry.md")
- [Understand telemetry data](telemetry.md "telemetry.md")
