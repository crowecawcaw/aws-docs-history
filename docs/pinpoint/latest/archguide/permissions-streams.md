**End of support notice:** On October
30, 2026, AWS will end support for Amazon Pinpoint. After October 30, 2026, you will no
longer be able to access the Amazon Pinpoint console or Amazon Pinpoint resources (endpoints,
segments, campaigns, journeys, and analytics). For more information, see [Amazon Pinpoint end of
support](../../../console/pinpoint/migration-guide.md "../../../console/pinpoint/migration-guide.md"). **Note:** APIs related to SMS, voice,
mobile push, OTP, and phone number validate are not impacted by this change and are
supported by AWS End User Messaging.

# IAM role for streaming events to Kinesis

Amazon Pinpoint can automatically send _app usage data_, or
_event data_, from your app to an Amazon Kinesis data stream or Amazon Data Firehose
delivery stream in your AWS account. Before Amazon Pinpoint can begin streaming the event data,
you must delegate the required permissions to Amazon Pinpoint.

If you use the console to set up event streaming, Amazon Pinpoint will automatically create an
AWS Identity and Access Management (IAM) role with the required permissions. For more information, see [Streaming Amazon Pinpoint events to
Kinesis](../userguide/analytics-streaming-kinesis.md "../userguide/analytics-streaming-kinesis.md") in the _Amazon Pinpoint User Guide_.

If you want to create the role manually, attach the following policies to the role:

- A permissions policy that allows Amazon Pinpoint to send event data to your
  stream.
- A trust policy that allows Amazon Pinpoint to assume the role.
  After you create the role, you can configure Amazon Pinpoint to send events to your stream
  automatically. For more information, see [Streaming Amazon Pinpoint events to
  Kinesis](../developerguide/event-streams.md "../developerguide/event-streams.md") in the _Amazon Pinpoint Developer Guide_.

## Permissions policies

To allow Amazon Pinpoint to send event data to your stream, attach one of the following
policies to the role.

### Amazon Kinesis Data Streams

The following policy allows Amazon Pinpoint to send event data to a Kinesis stream.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": {
 "Action": [
 "kinesis:PutRecords",
 "kinesis:DescribeStream"
 ],
 "Effect": "Allow",
 "Resource": [
 "arn:aws:kinesis:`us-east-1`:`111122223333`:stream/`stream-name`"
 ]
 }
}`

```

### Amazon Data Firehose

The following policy allows Amazon Pinpoint to send event data to a Firehose delivery
stream.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": {
 "Effect": "Allow",
 "Action": [
 "firehose:PutRecordBatch",
 "firehose:DescribeDeliveryStream"
 ],
 "Resource": [
 "arn:aws:firehose:`us-east-1`:`111122223333`:deliverystream/`delivery-stream-name`"
 ]
 }
}`

```

## Trust policy

To allow Amazon Pinpoint to assume the IAM role and perform the actions allowed by the
permissions policy, attach the following trust policy to the role:

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Principal": {
 "Service": "pinpoint.amazonaws.com"
 },
 "Action": "sts:AssumeRole"
 }
 ]
}`

```

## Creating the IAM role (AWS CLI)

Complete the following steps to create the IAM role by using the AWS Command Line Interface (AWS CLI).
To learn how to create the role by using the Amazon Pinpoint console, see [Streaming Amazon Pinpoint events to Kinesis](../userguide/analytics-streaming-kinesis.md#analytics-streaming-kinesis-setup "../userguide/analytics-streaming-kinesis.md#analytics-streaming-kinesis-setup") in the
_Amazon Pinpoint User Guide_.

If you haven't installed the AWS CLI, see [Installing the AWS CLI](../../../cli/latest/userguide/cli-chap-getting-set-up.md "../../../cli/latest/userguide/cli-chap-getting-set-up.md") in the
_AWS Command Line Interface User Guide_.

###### To create the IAM role by using the AWS CLI

1. Create a JSON file that contains the trust policy for your role, and save the
   file locally. You can copy the trust policy provided in this topic.
2. Use the [`create-role`](../../../cli/latest/reference/iam/create-role.md "../../../cli/latest/reference/iam/create-role.md") command to create the role and attach
   the trust policy:

```
aws iam create-role --role-name `PinpointEventStreamRole` --assume-role-policy-document file://`PinpointEventStreamTrustPolicy`.json
```

Following the `file://` prefix, specify the path to the JSON file
that contains the trust policy.

After you run this command, the AWS CLI prints the following output in your
terminal: 3. Create a JSON file that contains the permissions policy for your role, and
save the file locally. You can copy one of the policies provided in the [Permissions policies](#permissions-streams-permissionspolicies "#permissions-streams-permissionspolicies") section of this
topic. 4. Use the [`put-role-policy`](../../../cli/latest/reference/iam/put-role-policy.md "../../../cli/latest/reference/iam/put-role-policy.md") command to attach the permissions
policy to the role:

```
aws iam put-role-policy --role-name `PinpointEventStreamRole` --policy-name `PinpointEventStreamPermissionsPolicy` --policy-document file://`PinpointEventStreamPermissionsPolicy`.json
```

Following the `file://` prefix, specify the path to the JSON file
that contains the permissions policy.
