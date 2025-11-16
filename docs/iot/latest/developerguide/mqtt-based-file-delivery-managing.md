# Managing a stream in the AWS Cloud

AWS IoT provides AWS SDK and AWS CLI commands that you can use to manage a stream in the AWS Cloud. You
can use these commands to do the following:

- Create a stream.
  [CLI](../../../cli/latest/reference/iot/create-stream.md "../../../cli/latest/reference/iot/create-stream.md") /
  [SDK](../apireference/API_CreateStream.md "../apireference/API_CreateStream.md")
- Describe a stream to get its information.
  [CLI](../../../cli/latest/reference/iot/describe-stream.md "../../../cli/latest/reference/iot/describe-stream.md") /
  [SDK](../apireference/API_DescribeStream.md "../apireference/API_DescribeStream.md")
- List streams in your AWS account.
  [CLI](../../../cli/latest/reference/iot/list-streams.md "../../../cli/latest/reference/iot/list-streams.md") /
  [SDK](../apireference/API_ListStreams.md "../apireference/API_ListStreams.md")
- Update the file list or stream description in a stream.
  [CLI](../../../cli/latest/reference/iot/update-stream.md "../../../cli/latest/reference/iot/update-stream.md") /
  [SDK](../apireference/API_UpdateStream.md "../apireference/API_UpdateStream.md")
- Delete a
  stream.
  [CLI](../../../cli/latest/reference/iot/delete-stream.md "../../../cli/latest/reference/iot/delete-stream.md") /
  [SDK](../apireference/API_DeleteStream.md "../apireference/API_DeleteStream.md")

###### Note

At this time, streams are not visible in the AWS Management Console. You must use the AWS CLI or
AWS SDK to manage a stream in AWS IoT. Also, [Embedded C
SDK](https://github.com/aws/aws-iot-device-sdk-embedded-C "https://github.com/aws/aws-iot-device-sdk-embedded-C") is the only SDK that supports MQTT-based file transfers.

Before you use AWS IoT MQTT-based file delivery from your devices, you must ensure the
following conditions are met for your devices as shown in the next sections:

- A policy reflecting the correct permissions required for transmitting data via
  MQTT.
- Your device can connect to the AWS IoT Device Gateway.
- A policy statement stating you can tag resources. If `CreateStream`
  is called with tags, then `iot:TagResource` is required.
  Before you use AWS IoT MQTT-based file delivery from your devices, you must follow the steps in the
  next sections to make sure that your devices are properly authorized and can connect to the AWS IoT
  Device Gateway.

## Grant permissions to your devices

You can follow the steps in [Create an AWS IoT
policy](create-iot-resources.md#create-iot-policy "create-iot-resources.md#create-iot-policy") to create a device policy or use an existing device policy. Attach the policy to the
certificates associated with your devices and add the following permissions to the device policy.

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "iot:Connect"
 ],
 "Resource": [
 "arn:aws:iot:`us-east-1`:`123456789012`:client/${iot:Connection.Thing.ThingName}"
 ]
 },
 {
 "Effect": "Allow",
 "Action": [
 "iot:Receive",
 "iot:Publish"
 ],
 "Resource": [
 "arn:aws:iot:`us-east-1`:`123456789012`:topic/$aws/things/${iot:Connection.Thing.ThingName}/streams/*"
 ]
 },
 {
 "Effect": "Allow",
 "Action": "iot:Subscribe",
 "Resource": [
 "arn:aws:iot:`us-east-1`:`123456789012`:topicfilter/$aws/things/${iot:Connection.Thing.ThingName}/streams/*"
 ]
 }
 ]
}`

```

## Connect your devices to AWS IoT

Devices that use AWS IoT MQTT-based file delivery are required to connect with AWS IoT. AWS IoT
MQTT-based file delivery integrates with AWS IoT in the AWS Cloud, so your devices should directly connect to
[the endpoint
of the AWS IoT Data Plane](../apireference/Welcome.md#Welcome_AWS_IoT_Data_Plane "../apireference/Welcome.md#Welcome_AWS_IoT_Data_Plane").

###### Note

The endpoint of the AWS IoT data plane is specific to the AWS account and Region. You must use the
endpoint for the AWS account and the Region in which your devices are registered in AWS IoT.

See [Connect to AWS IoT Core](connect-to-iot.md "connect-to-iot.md") for more information.

## TagResource Usage

The `CreateStream` API action creates a stream for delivering one or
more large files in chunks over MQTT.

A successful `CreateStream` API call requires the following
permissions:

- `iot:CreateStream`
- `iot:TagResource` (if `CreateStream` is with
  tags)

The policy supporting those two permissions is shown below:

```
`{
 "Version":"2012-10-17",
 "Statement": {
 "Action": [
 "iot:CreateStream",
 "iot:TagResource"
 ],
 "Effect": "Allow",
 "Resource": "arn:aws:iot:us-east-1:`123456789012`:stream/streamId"
 }
}`

```

The `iot:TagResource` policy statement action is required to ensure a
user can't create or update a tag on a resource without the proper permissions.
Without the specifc policy statement action of `iot:TagResource`, the
`CreateStream` API call will return an
`AccessDeniedException` if the request comes with tags.

For more information, refer to the following links:

- [CreateStream](../apireference/API_CreateStream.md "../apireference/API_CreateStream.md")
- [TagResource](../apireference/API_TagResource.md "../apireference/API_TagResource.md")
- [Tag](../apireference/API_Tag.md "../apireference/API_Tag.md")
