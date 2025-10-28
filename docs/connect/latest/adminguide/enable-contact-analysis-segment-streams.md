# Enable contact

analysis segment streams to analyze Contact Lens
conversations

Contact analysis segment streams are not enabled by default. This topic
explains how to enable them.

## Step 1: Create a Kinesis

stream

Create the data stream on the same account and Region where your Amazon Connect
instance resides. For instructions, see [Step 1: Create a Data Stream](../../../streams/latest/dev/tutorial-stock-data-kplkcl-create-stream.md "../../../streams/latest/dev/tutorial-stock-data-kplkcl-create-stream.md") in the
_Amazon Kinesis Data Streams Developer Guide_.

###### Tip

We recommend creating a separate stream for each type of data. While
it's possible to use the same stream for contact analysis segment
streams, agent events, and contact records, it is much easier to manage
and get data from the stream when you use a separate stream for each
one. For more information, see the [Amazon Kinesis Data Streams Developer Guide](../../../streams/latest/dev/introduction.md "../../../streams/latest/dev/introduction.md").

## Step 2: Set up server-side

encryption for the Kinesis stream (optional but recommended)

There are several ways you can do this.

- Option 1: Use the Kinesis AWS managed key
  (`aws/kinesis`). This works with no additional setup from
  you.
- Option 2: Use the same customer managed key for call recordings, chat
  transcripts, or exported reports in your Amazon Connect instance.

Enable encryption, and use a customer managed key for call recordings, chat
transcripts, or exported reports in your Amazon Connect instance. Then choose
the same KMS key for your Kinesis data stream. This key already has
the permission (grant) required to be used.

- Option 3: Use a different customer managed key.

Use an existing customer managed key or create a new one and add required
permissions for Amazon Connect role to use the key. To add permissions using
AWS KMS grants, see the following example:

```
aws kms create-grant \
    --key-id `your key ID` \
    --grantee-principal arn:aws:iam::`your AWS account ID`:role/aws-service-role/connect.amazonaws.com/AWSServiceRoleForAmazonConnect_`11111111111111111111` \
    --operations GenerateDataKey \
    --retiring-principal arn:aws:iam::`your AWS account ID`:role/adminRole
```

Where `grantee-principal` is the ARN of the
service-linked role associated to your Amazon Connect instance. To find the
ARN of the service-linked role, in the Amazon Connect console, go to
**Overview**, **Distribution
settings**, **Service-linked role**.

## Step 3: Associate the Kinesis

stream

Use the Amazon Connect [AssociateInstanceStorageConfig](../APIReference/API_AssociateInstanceStorageConfig.md "../APIReference/API_AssociateInstanceStorageConfig.md") API to associate the following
resource types:

- For voice contacts, use
  `REAL_TIME_CONTACT_ANALYSIS_VOICE_SEGMENTS`
- For chat contacts, use
  `REAL_TIME_CONTACT_ANALYSIS_CHAT_SEGMENTS`

###### Note

`REAL_TIME_CONTACT_ANALYSIS_SEGMENTS` is deprecated, but it
is still supported and applies to voice contacts only. Use
`REAL_TIME_CONTACT_ANALYSIS_VOICE_SEGMENTS` for voice
contacts moving forward.

If you have previously associated a stream with
`REAL_TIME_CONTACT_ANALYSIS_SEGMENTS`, no action is
needed to update the stream to
`REAL_TIME_CONTACT_ANALYSIS_VOICE_SEGMENTS`.

Specify the Kinesis stream where real-time contact analysis segments will be
published. You'll need the instance ID and the Kinesis stream ARN. The
following code shows an example:

```
// Build request
  const request: Connect.Types.AssociateInstanceStorageConfigRequest = {
    InstanceId: 'your Amazon Connect instance ID',
    ResourceType: 'REAL_TIME_CONTACT_ANALYSIS_VOICE_SEGMENTS or REAL_TIME_CONTACT_ANALYSIS_CHAT_SEGMENTS',
    StorageConfig: {
      StorageType: 'KINESIS_STREAM',
      KinesisStreamConfig: {
        StreamArn: 'the ARN of your Kinesis stream',
      },
    }
  };
```

### AWS CLI

The following example is for chat contacts.

###### Tip

If you don't include the AWS Region (`--region`) it
uses the default Region based on the CLI profile.

The `--storage-config` parameter value must not be
include within single quote ('). Otherwise it raises an
error.

```
aws connect associate-instance-storage-config \
--region "us-west-2" \
--instance-id `your Amazon Connect instance ID` \
--resource-type REAL_TIME_CONTACT_ANALYSIS_CHAT_SEGMENTS \
--storage-config StorageType=KINESIS_STREAM,KinesisStreamConfig={StreamArn=`the ARN of your Kinesis stream`}

```

### AWS SDK

The following example is for voice contacts.

```
import { Connect } from 'aws-sdk';

async function associate (): Promise <void> {
  const clientConfig: Connect.ClientConfiguration = {
    region: '`the Region of your Amazon Connect instance`',
  };

  const connect = new Connect(clientConfig);

  // Build request
  const request: Connect.Types.AssociateInstanceStorageConfigRequest = {
    InstanceId: '`your Amazon Connect instance ID`',
    ResourceType: 'REAL_TIME_CONTACT_ANALYSIS_VOICE_SEGMENTS',
    StorageConfig: {
      StorageType: 'KINESIS_STREAM',
      KinesisStreamConfig: {
        StreamArn: '`the ARN of your Kinesis stream`',
      },
    }
  };

  try {
    // Execute request
    const response: Connect.Types.AssociateInstanceStorageConfigResponse = await connect.associateInstanceStorageConfig(request).promise();

    // Process response
    console.log('raw response: ${JSON.stringify(response, null, 2)}');
  } catch (err) {
    console.error('Error calling associateInstanceStorageConfig. err.code: ${err.code},' +
      'err.message: ${err.message}, err.statusCode: ${err.statusCode}, err.retryable: ${err.retryable}');
  }
}

associate().then(r => console.log('`Done`'));
```

## Step 4: Enable

Contact Lens for your Amazon Connect instance

For instructions, see [Enable conversational analytics in
Amazon Connect Contact Lens](enable-analytics.md "enable-analytics.md").

## Step 5 (Optional): Review a

sample segment stream

We recommend you review a [voice](sample-real-time-contact-analysis-segment-stream.md "sample-real-time-contact-analysis-segment-stream.md")
or [chat](chat-sample-real-time-contact-analysis-segment-stream.md "chat-sample-real-time-contact-analysis-segment-stream.md") sample segment stream to familiarize yourself with what it
looks like.
