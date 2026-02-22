# Use AWS Ground Station Configs

_Configs_ are resources that AWS Ground Station uses to define the parameters for
each aspect of your contact. Add the configs you want to a mission profile, and then that
mission profile will be used when executing the contact. You can define several different
types of configs. The configs can be grouped into three categories:

- Tracking configs
- Dataflow configs
- Telemetry configs

A _TrackingConfig_ is the only type of tracking config. It's used to
configure the autotrack setting of the antenna during a contact, and is required in a
mission profile.

The configs that can be used in a mission profile dataflow can be thought
of as dataflow nodes that each represent an AWS Ground Station managed resource that can send or receive
data. A mission profile requires at least one pair of these configs, with one representing a
source of data, and one representing a destination. These configs are summarized in the
following table.

| Config name                      | Dataflow source/destination |
| -------------------------------- | --------------------------- |
| AntennaDownlinkConfig            | Source                      |
| AntennaDownlinkDemodDecodeConfig | Source                      |
| UplinkEchoConfig                 | Source                      |
| S3RecordingConfig                | Destination                 |
| AntennaUplinkConfig              | Destination                 |
| DataflowEndpointConfig           | Source and/or Destination   |

A _TelemetrySinkConfig_ is the only type of telemetry config. It's used to
configure where telemetry data will be delivered during a contact, and is optional
in a mission profile. When included, AWS Ground Station streams near real-time telemetry to your
account during the execution of your contacts.

See the following documentation for more information about how to perform operations on configs using CloudFormation, the AWS Command Line Interface, or the AWS Ground Station API.
Links to documentation for specific config types are also provided below.

- [AWS::GroundStation::Config CloudFormation resource type](../../../AWSCloudFormation/latest/UserGuide/aws-resource-groundstation-config.md "../../../AWSCloudFormation/latest/UserGuide/aws-resource-groundstation-config.md")
- [Config AWS CLI reference](../../../cli/latest/reference/groundstation/create-config.md "../../../cli/latest/reference/groundstation/create-config.md")
- [Config API reference](../APIReference/API_CreateConfig.md "../APIReference/API_CreateConfig.md")

## Tracking Config

You can use tracking configs in the mission profile to determine whether autotrack should be enabled during your contacts.
This config has a single parameter: `autotrack`. The `autotrack` parameter can have the following values:

- `REQUIRED` - Autotrack is required for your contacts.
- `PREFERRED` - Autotrack is preferred for contacts, but contacts can still be executed without autotrack.
- `REMOVED` - No autotrack should be used for your contacts.

AWS Ground Station will utilize programmatic tracking which will point based on your ephemeris when autotrack is not used. Please reference [Understand how AWS Ground Station uses ephemerides](ephemeris.md "ephemeris.md") for details about how ephemeris is constructed.

Autotrack will use program tracking until the expected signal is found. Once that occurs, it will continue to track based on the strength of the signal.

See the following documentation for more information about how to perform operations on tracking configs using CloudFormation, the AWS Command Line Interface, or the AWS Ground Station API.

- [AWS::GroundStation::Config TrackingConfig CloudFormation property](../../../AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-config-trackingconfig.md "../../../AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-config-trackingconfig.md")
- [Config AWS CLI reference](../../../cli/latest/reference/groundstation/create-config.md "../../../cli/latest/reference/groundstation/create-config.md") (see the `trackingConfig -> (structure)` section)
- [TrackingConfig API reference](../APIReference/API_TrackingConfig.md "../APIReference/API_TrackingConfig.md")

## Antenna Downlink Config

You can use antenna downlink configs to configure the antenna for downlink during your contact.
They consist of a spectrum config that specifies the frequency, bandwidth,
and polarization that should be used during your downlink contact.

This config represents a source node in a dataflow. It is responsible for digitizing radio frequency data. Data streamed from this node will follow the Signal Data/IP Format. For more detailed information on how to construct dataflows with this config, see [Work with dataflows](dataflows.md "dataflows.md")

If your downlink use case requires demodulation or decoding, see the [Antenna Downlink Demod
Decode Config](#how-it-works.config-antenna-downlink-demod-decode "#how-it-works.config-antenna-downlink-demod-decode") .

See the following documentation for more information about how to perform operations on antenna downlink configs using CloudFormation, the AWS Command Line Interface, or the AWS Ground Station API.

- [AWS::GroundStation::Config AntennaDownlinkConfig CloudFormation property](../../../AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-config-antennadownlinkconfig.md "../../../AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-config-antennadownlinkconfig.md")
- [Config AWS CLI reference](../../../cli/latest/reference/groundstation/create-config.md "../../../cli/latest/reference/groundstation/create-config.md") (see the `antennaDownlinkConfig -> (structure)` section)
- [AntennaDownlinkConfig API reference](../APIReference/API_AntennaDownlinkConfig.md "../APIReference/API_AntennaDownlinkConfig.md")

## Antenna Downlink Demod

Decode Config

Antenna downlink demod decode configs are a more complex and customizable config type that you
can use to execute downlink contacts with demodulation and/or decoding. If you're interested
in executing these types of contacts, please open an AWS Support ticket through the
[AWS Support Center Console](https://console.aws.amazon.com/support "https://console.aws.amazon.com/support"). We'll help you define the right config and mission
profile for your use case.

This config represents a source node in a dataflow. It is responsible for digitizing radio
frequency data and performing the demodulation and decoding as specified. Data streamed from
this node will follow the Demodulated/Decoded Data/IP Format. For more detailed information on
how to construct dataflows with this config, see
[Work with dataflows](dataflows.md "dataflows.md")

See the following documentation for more information about how to perform operations on antenna
downlink demod decode configs using CloudFormation, the AWS Command Line Interface, or the AWS Ground Station API.

- [AWS::GroundStation::Config AntennaDownlinkDemodDecodeConfig CloudFormation property](../../../AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-config-antennadownlinkdemoddecodeconfig.md "../../../AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-config-antennadownlinkdemoddecodeconfig.md")
- [Config AWS CLI reference](../../../cli/latest/reference/groundstation/create-config.md "../../../cli/latest/reference/groundstation/create-config.md")
  (see the `antennaDownlinkDemodDecodeConfig -> (structure)` section)
- [AntennaDownlinkDemodDecodeConfig API reference](../APIReference/API_AntennaDownlinkDemodDecodeConfig.md "../APIReference/API_AntennaDownlinkDemodDecodeConfig.md")

## Antenna Uplink Config

You can use antenna uplink configs to configure the antenna for uplink during your contact.
They consist of a spectrum config with frequency, polarization, and target effective isotropic radiated power (EIRP).
For information about how to configure a contact for uplink loopback, see [Antenna Uplink Echo Config](#how-it-works.config-antenna-uplink-echo "#how-it-works.config-antenna-uplink-echo").

This config represents a destination node in a dataflow. It will convert the provided digitized radio frequency data signal into an analog signal and emit it for your satellite to receive. Data streamed to this node is expected to meet the Signal Data/IP Format. For more detailed information on how to construct dataflows with this config, see [Work with dataflows](dataflows.md "dataflows.md")

See the following documentation for more information about how to perform operations on antenna uplink configs using CloudFormation, the AWS Command Line Interface, or the AWS Ground Station API.

- [AWS::GroundStation::Config AntennaUplinkConfig CloudFormation property](../../../AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-config-antennauplinkconfig.md "../../../AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-config-antennauplinkconfig.md")
- [Config AWS CLI reference](../../../cli/latest/reference/groundstation/create-config.md "../../../cli/latest/reference/groundstation/create-config.md") (see the `antennaUplinkConfig -> (structure)` section)
- [AntennaUplinkConfig API reference](../APIReference/API_AntennaUplinkConfig.md "../APIReference/API_AntennaUplinkConfig.md")

## Antenna Uplink Echo Config

Uplink echo configs tell the antenna how to execute an uplink echo. An uplink echo can be used
to validate commands sent to your spacecraft, and perform other advanced tasks. This is
achieved by recording the actual signal transmitted by the AWS Ground Station antenna (i.e. the uplink).
This echoes the signal sent by the antenna back to your dataflow endpoint and should match the
transmitted signal. An uplink echo config contains the ARN of an uplink config. The antenna
uses the parameters from the uplink config pointed to by the ARN when executing an uplink echo.

This config represents a source node in a dataflow. Data streamed from this node will
meet the Signal Data/IP Format. For more detailed information on how to construct dataflows
with this config, see [Work with dataflows](dataflows.md "dataflows.md")

See the following documentation for more information about how to perform operations on uplink
echo configs using CloudFormation, the AWS Command Line Interface, or the AWS Ground Station API.

- [AWS::GroundStation::Config UplinkEchoConfig CloudFormation property](../../../AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-config-uplinkechoconfig.md "../../../AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-config-uplinkechoconfig.md")
- [Config AWS CLI reference](../../../cli/latest/reference/groundstation/create-config.md "../../../cli/latest/reference/groundstation/create-config.md") (see the `uplinkEchoConfig -> (structure)` section)
- [UplinkEchoConfig API reference](../APIReference/API_UplinkEchoConfig.md "../APIReference/API_UplinkEchoConfig.md")

## Dataflow Endpoint Config

###### Note

Dataflow endpoint configs are only used for data delivery to Amazon EC2 and are not used for data
delivery to Amazon S3.

You can use dataflow endpoint configs to specify which dataflow endpoint in a
[dataflow endpoint group](how-it-works.md "how-it-works.md") from which
or to which you want data to flow during a contact. The two parameters of a dataflow endpoint
config specify the name and region of the dataflow endpoint. When reserving a contact, AWS Ground Station
analyzes the [mission profile](how-it-works-mission-profile.md "how-it-works-mission-profile.md") you specified
and attempts to find a dataflow endpoint _group_ within the AWS Region
that contains all of the dataflow _endpoints_ specified by the dataflow
endpoint _configs_ contained in your mission profile. If a suitable
dataflow endpoint _group_ is found, the contact status will become
SCHEDULED, otherwise it will become FAILED_TO_SCHEDULE. For more information about the
possible statuses of a contact, see
[AWS Ground Station contact statuses](contacts.md#contact-statuses "contacts.md#contact-statuses").

The `dataflowEndpointName` property of a dataflow endpoint config specifies which
dataflow endpoint in a dataflow endpoint group to which or from which data will flow during a
contact.

The `dataflowEndpointRegion` property specifies which region the dataflow endpoint
resides in. If a region is specified in your dataflow endpoint config, AWS Ground Station looks for a
dataflow endpoint in the region specified. If no region is specified, AWS Ground Station will default to
the contact's ground station region. A contact is considered a cross region data delivery
contact if your dataflow endpoint's region is not the same as the contact's ground station
region. See [Work with dataflows](dataflows.md "dataflows.md") for more information on
cross-region dataflows.

See [Use AWS Ground Station Dataflow endpoint groups](how-it-works.md "how-it-works.md")
for tips on how different naming schemes for your dataflows can benefit your use case.

For more detailed information on how to construct dataflows with this config, see
[Work with dataflows](dataflows.md "dataflows.md")

See the following documentation for more information about how to perform operations on
dataflow endpoint configs using CloudFormation, the AWS Command Line Interface, or the AWS Ground Station API.

- [AWS::GroundStation::Config DataflowEndpointConfig CloudFormation property](../../../AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-config-dataflowendpointconfig.md "../../../AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-config-dataflowendpointconfig.md")
- [Config AWS CLI reference](../../../cli/latest/reference/groundstation/create-config.md "../../../cli/latest/reference/groundstation/create-config.md") (see the `dataflowEndpointConfig -> (structure)` section)
- [DataflowEndpointConfig API reference](../APIReference/API_DataflowEndpointConfig.md "../APIReference/API_DataflowEndpointConfig.md")

## Amazon S3 Recording Config

###### Note

Amazon S3 recording configs are only used for data delivery to Amazon S3 and are not used for data delivery to Amazon EC2.

This config represents a destination node in a dataflow. This node will encapsulate
incoming data from the dataflow's source node into pcap data. For more detailed information
on how to construct dataflows with this config, see
[Work with dataflows](dataflows.md "dataflows.md")

You can use S3 recording configs to specify an Amazon S3 bucket to which you want downlinked data
delivered along with the naming convention used. The following specifies restrictions and
details about these parameters:

- The Amazon S3 bucket's name must begin with `aws-groundstation` .
- The IAM role must have a trust policy that allows the
  `groundstation.amazonaws.com` service principal to assume the role.
  See the [Example Trust Policy](#s3-trust-policy-example "#s3-trust-policy-example") section below
  for an example. During config creation the config resource id does not exist,
  the trust policy must use an asterisk (`*`) in place of
  `your-config-id` and can be updated after creation with the
  config resource id.

For more information on how to update a role's trust policy, see
[Managing IAM roles](../../../IAM/latest/UserGuide/id_roles_manage.md "../../../IAM/latest/UserGuide/id_roles_manage.md") in the IAM User Guide.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "Service": "groundstation.amazonaws.com"
 },
 "Action": "sts:AssumeRole",
 "Condition": {
 "StringEquals": {
 "aws:SourceAccount": "`999999999999`"
 },
 "ArnLike": {
 "aws:SourceArn": "arn:aws:groundstation:`us-east-1`:`999999999999`:config/s3-recording/`your-config-id`"
 }
 }
 }
 ]
}`

```

- The IAM role must have an IAM policy that allows the role to perform the
  `s3:GetBucketLocation` action on the bucket and `s3:PutObject`
  action on the bucket's objects. If the Amazon S3 bucket has a bucket policy, then the bucket
  policy must also allow the IAM role to perform these actions. See the
  [Example Role Policy](#s3-role-policy-example "#s3-role-policy-example") section below for an
  example.

For more information on how to update or attach a role policy, see
[Managing IAM policies](../../../IAM/latest/UserGuide/access_policies_manage.md "../../../IAM/latest/UserGuide/access_policies_manage.md") in the IAM User Guide.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "s3:GetBucketLocation"
 ],
 "Resource": [
 "arn:aws:s3:::`your-bucket-name`"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "s3:PutObject"
 ],
 "Resource": [
 "arn:aws:s3:::`your-bucket-name`/*"
 ]
 }
 ]
}`

```

- The prefix will be used when naming the S3 data object. You can specify optional keys for
  substitution, these values will be replaced with the corresponding information from your
  contact details. For example, a prefix of `{satellite_id}/{year}/{month}/{day}`
  will be replaced and would result with an output like `fake_satellite_id/2021/01/10`

_Optional keys for substitution_: `{satellite_id}` | `{config-name}` | `{config-id}` | `{year}` | `{month}` | `{day}` |

See the following documentation for more information about how to perform operations on S3
recording configs using CloudFormation, the AWS Command Line Interface, or the AWS Ground Station API.

- [AWS::GroundStation::Config S3RecordingConfig CloudFormation property](../../../AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-config-s3recordingconfig.md "../../../AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-config-s3recordingconfig.md")
- [Config AWS CLI reference](../../../cli/latest/reference/groundstation/create-config.md "../../../cli/latest/reference/groundstation/create-config.md") (see the `s3RecordingConfig -> (structure)` section)
- [S3RecordingConfig API reference](../APIReference/API_S3RecordingConfig.md "../APIReference/API_S3RecordingConfig.md")

## Telemetry Sink Config

You can use telemetry sink configs to specify where you want telemetry
data delivered during satellite contacts. A telemetry sink config is optional and is
added to your mission profile to schedule telemetry-enabled contacts. The following specifies
restrictions and details about these parameters:

- The IAM role must have a trust policy that allows the
  `groundstation.amazonaws.com` service principal to assume the role.
  See the [Example Trust Policy](#telemetry-config-trust-policy-example "#telemetry-config-trust-policy-example") section below
  for an example.

For more information on how to update a role's trust policy, see
[Managing IAM roles](../../../IAM/latest/UserGuide/id_roles_manage.md "../../../IAM/latest/UserGuide/id_roles_manage.md") in the IAM User Guide.

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "Service": "groundstation.amazonaws.com"
      },
      "Action": "sts:AssumeRole"
    }
  ]
}
```

- The IAM role must have an IAM policy that allows the role to perform the
  `kinesis:DescribeStream`, `kinesis:PutRecord`
  and `kinesis:PutRecords` actions on the stream. See the
  [Example Role Policy](#telemetry-config-role-policy-example "#telemetry-config-role-policy-example") section below for an
  example.

For more information on how to update or attach a role policy, see
[Managing IAM policies](../../../IAM/latest/UserGuide/access_policies_manage.md "../../../IAM/latest/UserGuide/access_policies_manage.md") in the IAM User Guide.

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "kinesis:DescribeStream",
        "kinesis:PutRecord",
        "kinesis:PutRecords"
      ],
      "Resource": "arn:aws:kinesis:`us-east-2`:`999999999999`:stream/`your-stream-name`"
    }
  ]
}
```

When you include a telemetry sink config in your mission profile, AWS Ground Station will stream
telemetry data to your account during contacts. For more information
about telemetry types, data format, and setting up the necessary AWS resources, see
[Work with telemetry](telemetry.md "telemetry.md").

See the following documentation for more information about how to perform operations on
telemetry sink configs using CloudFormation, the AWS Command Line Interface, or the AWS Ground Station API.

- [AWS::GroundStation::Config TelemetrySinkConfig CloudFormation property](../../../AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-config-telemetrysinkconfig.md "../../../AWSCloudFormation/latest/UserGuide/aws-properties-groundstation-config-telemetrysinkconfig.md")
- [Config AWS CLI reference](../../../cli/latest/reference/groundstation/create-config.md "../../../cli/latest/reference/groundstation/create-config.md") (see the `telemetrySinkConfig -> (structure)` section)
- [TelemetrySinkConfig API reference](../APIReference/API_TelemetrySinkConfig.md "../APIReference/API_TelemetrySinkConfig.md")
