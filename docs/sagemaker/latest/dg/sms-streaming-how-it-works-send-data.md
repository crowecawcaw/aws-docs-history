# Send data to a streaming labeling job

You can optionally submit input data to a streaming labeling job one time when you
create the labeling job using an input manifest file. Once the labeling job has
started and the state is `InProgress`, you can submit new data objects to
your labeling job in real time using your Amazon SNS input topic and Amazon S3 event
notifications.

**Submit Data Objects When you Start
the Labeling Job (One Time):**

- **Use an Input Manifest File** – You can
  optionally specify an input manifest file Amazon S3 URI in
  `ManifestS3Uri` when you create the streaming labeling job.
  Ground Truth sends each data object in the manifest file to workers for labeling as
  soon as the labeling job starts. To learn more, see [Create a Manifest File (Optional)](sms-streaming-manifest.md "sms-streaming-manifest.md").

After you submit a request to create the streaming labeling job, its status
will be `Initializing`. Once the labeling job is active, the state
changes to `InProgress` and you can start using the real-time options
to submit additional data objects for labeling.
**Submit Data Objects in Real
Time:**

- **Send data objects using Amazon SNS messages**
  – You can send Ground Truth new data objects to label by sending an Amazon SNS
  message. You will send this message to an Amazon SNS input topic that you create and
  specify when you create your streaming labeling job. For more information, see
  [Send data objects using Amazon SNS](#sms-streaming-how-it-works-sns "#sms-streaming-how-it-works-sns").
- **Send data objects by placing them in an Amazon S3
  bucket** – Each time you add a new data object to an
  Amazon S3 bucket, you can prompt Ground Truth to process that object for labeling. To do
  this, you add an event notification to the bucket so that it notifies your
  Amazon SNS input topic each time a new object is added to (or _created
  in_) that bucket. For more information, see [Send data objects using Amazon S3](#sms-streaming-how-it-works-s3 "#sms-streaming-how-it-works-s3"). This option is not
  available for text-based labeling jobs such as text classification and named
  entity recognition.

###### Important

If you use the Amazon S3 configuration, do not use the same Amazon S3 location for
your input data configuration and your output data. You specify the S3
prefix for your output data when you create a labeling job.

## Send data objects using Amazon SNS

You can send data objects to your streaming labeling job using Amazon Simple Notification Service
(Amazon SNS). Amazon SNS is a web service that coordinates and manages the delivery of
messages to and from _endpoints_ (for example, an email
address or AWS Lambda function). An Amazon SNS _topic_ acts as a
communication channel between two or more endpoints. You use Amazon SNS to send, or
_publish_, new data objects to the topic specified in the
[`CreateLabelingJob`](../APIReference/API_CreateLabelingJob.md "../APIReference/API_CreateLabelingJob.md") parameter
`SnsTopicArn` in `InputConfig`. The format of these
messages is the same as a single line from an [input manifest file](sms-data-input.md "sms-data-input.md").

For example, you may send a piece of text to an active text classification
labeling job by publishing it to your input topic. The message that you publish
may look similar to the following:

```
{"source": "Lorem ipsum dolor sit amet"}
```

To send a new image object to an image classification labeling job, your message
may look similar to the following:

```
{"source-ref": "s3://`amzn-s3-demo-bucket`/example-image.jpg"}
```

###### Note

You can also include custom deduplication IDs and deduplication keys in your
Amazon SNS messages. To learn more, see [Duplicate message handling](sms-streaming-impotency.md "sms-streaming-impotency.md").

When Ground Truth creates your streaming labeling job, it subscribes to your Amazon SNS
input topic.

## Send data objects using Amazon S3

You can send one or more new data objects to a streaming labeling job by
placing them in an Amazon S3 bucket that is configured with an Amazon SNS event
notification. You can set up an event to notify your Amazon SNS input topic anytime a
new object is created in your bucket. You must specify this same Amazon SNS input
topic in the [`CreateLabelingJob`](../APIReference/API_CreateLabelingJob.md "../APIReference/API_CreateLabelingJob.md") parameter
`SnsTopicArn` in `InputConfig`.

Anytime you configure an Amazon S3 bucket to send notifications to Amazon SNS,
Ground Truth will publish a test event, `"s3:TestEvent"`, to ensure
that the topic exists and that the owner of the Amazon S3 bucket specified
has permission to publish to the specified topic. It is recommended that
you set up your Amazon S3 connection with Amazon SNS before starting a streaming
labeling job. If you do not, this test event may register as a data
object and be sent to Ground Truth for labeling.

###### Important

If you use the Amazon S3 configuration, do not use the same Amazon S3 location for
your input data configuration and your output data. You specify the S3
prefix for your output data when you create a labeling job.

For image-based labeling jobs, Ground Truth requires all S3 buckets to have a
CORS policy attached. To learn more, see [CORS Requirement for Input Image Data](sms-cors-update.md "sms-cors-update.md").

Once you have configured your Amazon S3 bucket and created your labeling job, you can
add objects to your bucket and Ground Truth either sends that object to workers or places
it on your Amazon SQS queue.

To learn more, see [Creating Amazon S3 based bucket event notifications based of the Amazon SNS defined in your labeling job](sms-streaming-s3-setup.md "sms-streaming-s3-setup.md").

###### Important

This option is not available for text-based labeling jobs such as text
classification and named entity recognition.
