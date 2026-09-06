

# Work with telemetry
<a name="telemetry"></a>

 AWS Ground Station telemetry delivers near real-time metrics from AWS Ground Station antennas during your satellite contacts. You can use telemetry data to monitor contact performance, detect anomalies, and make informed decisions about your satellite communications. 

**Topics**
+ [How telemetry works](#telemetry.how-it-works)
+ [Available telemetry types](#telemetry.telemetry-types)
+ [Regional availability](#telemetry.regional-availability)
+ [Set up telemetry](telemetry.setup.md)
+ [Understand telemetry data](telemetry.understanding-data.md)

## How telemetry works
<a name="telemetry.how-it-works"></a>

 To use telemetry, you configure a *TelemetrySinkConfig* that specifies where AWS Ground Station should deliver telemetry data. You then add this config to your mission profile using the `telemetrySinkConfigArn` field. During contacts that use a telemetry-enabled mission profile, AWS Ground Station streams telemetry data to your account. 

 The telemetry delivery process works as follows: 

1.  You create a Kinesis Data Streams stream in your AWS account to receive telemetry data. The stream must be created in the same account and region from which you schedule your contacts. 

1.  You create an IAM role that grants AWS Ground Station permission to write data to your stream. 

1.  You create a TelemetrySinkConfig that references your stream and IAM role. 

1.  You add the TelemetrySinkConfig to your mission profile. 

1.  You list and reserve contacts using the new telemetry-enabled mission profile. 

1.  During contacts using this mission profile, AWS Ground Station streams telemetry data to your Kinesis Data Streams stream in near real-time. 

1.  You consume and process the telemetry data from your stream using AWS services or your own applications. 

## Available telemetry types
<a name="telemetry.telemetry-types"></a>

 AWS Ground Station provides the following telemetry types during contacts: 

**Note**  
AWS Ground Station is working on expanding the number of supported telemetry types

Pointing telemetry  
 Provides information about antenna pointing direction during satellite contacts. This telemetry type is always sent during a contact and includes actual and commanded azimuth and elevation angles. For more information, see [Pointing telemetry](telemetry.understanding-data.md#telemetry.understanding-data.pointing). 

Tracking telemetry  
 Provides information about antenna tracking status and tracking errors. This telemetry type is sent when autotracking is enabled in your tracking config. For more information, see [Tracking telemetry](telemetry.understanding-data.md#telemetry.understanding-data.tracking). 

## Regional availability
<a name="telemetry.regional-availability"></a>

 Telemetry is available in all AWS Regions where AWS Ground Station operates. During contact execution, telemetry will be delivered from the AWS Ground Station antenna to the region you scheduled your contact from, providing cross-region support. 

 For a complete list of AWS Ground Station Regions and ground station locations, see [AWS Ground Station Locations](aws-ground-station-antenna-locations.md). 