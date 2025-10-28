Amazon Managed Service for Apache Flink (Amazon MSF) was previously known as Amazon Kinesis Data Analytics for Apache Flink.

# Create an application using Apache Beam

In this exercise, you create a Managed Service for Apache Flink application that transforms data using
[Apache Beam](https://beam.apache.org/ "https://beam.apache.org/"). Apache Beam is a programming
model for processing streaming data. For information about using Apache Beam with Managed Service for Apache Flink, see
[Use Apache Beam with Managed Service for Apache Flink
applications](how-creating-apps-beam.md "how-creating-apps-beam.md").

###### Note

To set up required prerequisites for this exercise, first complete the [Tutorial: Get started using the DataStream API
in Managed Service for Apache Flink](getting-started.md "getting-started.md") exercise.

###### This topic contains the following sections:

- [Create dependent resources](#examples-beam-resources "#examples-beam-resources")
- [Write sample records to the input stream](#examples-beam-write "#examples-beam-write")
- [Download and examine the application code](#examples-beam-download "#examples-beam-download")
- [Compile the application code](#examples-beam-compile "#examples-beam-compile")
- [Upload the Apache Flink streaming Java code](#examples-beam-upload "#examples-beam-upload")
- [Create and run the Managed Service for Apache Flink application](#examples-beam-create-run "#examples-beam-create-run")
- [Clean up AWS resources](#examples-beam-cleanup "#examples-beam-cleanup")
- [Next steps](#examples-beam-nextsteps "#examples-beam-nextsteps")

## Create dependent resources

Before you create a Managed Service for Apache Flink application for this exercise, you create the following dependent resources:

- Two Kinesis data streams (`ExampleInputStream` and
  `ExampleOutputStream`)
- An Amazon S3 bucket to store the application's code (`ka-app-code-`<username>``)

You can create the Kinesis streams and Amazon S3 bucket using the console. For instructions for
creating these resources, see the following topics:

- [Creating and Updating Data
  Streams](../../../kinesis/latest/dev/amazon-kinesis-streams.md "../../../kinesis/latest/dev/amazon-kinesis-streams.md") in the _Amazon Kinesis Data Streams Developer Guide_. Name your data
  streams `ExampleInputStream` and `ExampleOutputStream`.
- [How Do I Create an S3 Bucket?](../../../AmazonS3/latest/userguide/create-bucket.md "../../../AmazonS3/latest/userguide/create-bucket.md") in the
  _Amazon Simple Storage Service User Guide_. Give the Amazon S3 bucket a globally unique name by appending your
  login name, such as `ka-app-code-`<username>``.

## Write sample records to the input stream

In this section, you use a Python script to write random strings to the stream for
the application to process.

###### Note

This section requires the [AWS SDK for Python (Boto)](https://aws.amazon.com/developers/getting-started/python/ "https://aws.amazon.com/developers/getting-started/python/").

1. Create a file named `ping.py` with the following
   contents:

```
import json
import boto3
import random

kinesis = boto3.client('kinesis')

while True:
        data = random.choice(['ping', 'telnet', 'ftp', 'tracert', 'netstat'])
        print(data)
        kinesis.put_record(
                StreamName="ExampleInputStream",
                Data=data,
                PartitionKey="partitionkey")

```

2. Run the `ping.py` script:

```
$ python ping.py
```

Keep the script running while completing the rest of the tutorial.

## Download and examine the application code

The Java application code for this example is available from GitHub. To download
the application code, do the following:

1. Install the Git client if you haven't already. For more information, see [Installing
   Git](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git "https://git-scm.com/book/en/v2/Getting-Started-Installing-Git").
2. Clone the remote repository with the following command:

```
git clone https://github.com/aws-samples/amazon-kinesis-data-analytics-examples.git
```

3. Navigate to the `amazon-kinesis-data-analytics-java-examples/Beam` directory.

The application code is located in the `BasicBeamStreamingJob.java` file. Note the following
about the application code:

- The application uses the Apache Beam [ParDo](https://beam.apache.org/releases/javadoc/2.0.0/org/apache/beam/sdk/transforms/ParDo.html "https://beam.apache.org/releases/javadoc/2.0.0/org/apache/beam/sdk/transforms/ParDo.html")
  to process incoming records by invoking a custom transform function called `PingPongFn`.

The code to invoke the `PingPongFn` function is as follows:

```
.apply("Pong transform",
    ParDo.of(new PingPongFn())
```

- Managed Service for Apache Flink applications that use Apache Beam require the following components. If you don't include
  these components and versions in your `pom.xml`, your application loads the incorrect
  versions from the environment dependencies, and since the versions do not match, your application crashes at runtime.

```
<jackson.version>**2.10.2**</jackson.version>
...
<dependency>
    <groupId>com.fasterxml.jackson.module</groupId>
    <artifactId>jackson-module-jaxb-annotations</artifactId>
    <version>2.10.2</version>
</dependency>
```

- The `PingPongFn` transform function passes the input data into the output
  stream, unless the input data is **ping**, in which case it emits the
  string **pong\n** to the output stream.

The code of the transform function is as follows:

```
    private static class PingPongFn extends DoFn<KinesisRecord, byte[]> {
    private static final Logger LOG = LoggerFactory.getLogger(PingPongFn.class);

    @ProcessElement
    public void processElement(ProcessContext c) {
        String content = new String(c.element().getDataAsBytes(), StandardCharsets.UTF_8);
        if (content.trim().equalsIgnoreCase("ping")) {
            LOG.info("Ponged!");
            c.output("pong\n".getBytes(StandardCharsets.UTF_8));
        } else {
            LOG.info("No action for: " + content);
            c.output(c.element().getDataAsBytes());
        }
    }
}
```

## Compile the application code

To compile the application, do the following:

1. Install Java and Maven if you haven't already. For more information, see [Complete the required
   prerequisites](getting-started.md#setting-up-prerequisites "getting-started.md#setting-up-prerequisites") in the [Tutorial: Get started using the DataStream API
   in Managed Service for Apache Flink](getting-started.md "getting-started.md")
   tutorial.
2. Compile the application with the following command:

```
mvn package -Dflink.version=1.15.2 -Dflink.version.minor=1.8
```

###### Note

The provided source code relies on libraries from Java 11.

Compiling the application creates the application JAR file (`target/basic-beam-app-1.0.jar`).

## Upload the Apache Flink streaming Java code

In this section, you
upload your application code to the Amazon S3 bucket you created in the [Create dependent resources](#examples-beam-resources "#examples-beam-resources") section.

1. In the Amazon S3 console, choose the **ka-app-code-`<username>`** bucket,
   and choose **Upload**.
2. In the **Select files** step, choose **Add
   files**. Navigate to the
   `basic-beam-app-1.0.jar` file that you created
   in the previous step.
3. You don't need to change any of the settings for the object, so choose **Upload**.

Your application code is now stored in an Amazon S3 bucket where your application can
access it.

## Create and run the Managed Service for Apache Flink application

Follow these steps to create, configure, update, and run the application using
the console.

### Create the

Application

1. Sign in to the AWS Management Console, and open the Amazon MSF console at https://console.aws.amazon.com/flink.
2. On the Managed Service for Apache Flink dashboard, choose **Create analytics
   application**.
3. On the **Managed Service for Apache Flink - Create application**
   page, provide the application details as follows:
   - For **Application name**, enter
     `MyApplication`.
   - For **Runtime**, choose **Apache Flink**.

   ###### Note

   Apache Beam is not presently compatible with Apache Flink version 1.19 or later.
   - Select **Apache Flink version 1.15** from the version pulldown.

4. For **Access permissions**, choose
   **Create / update IAM role
   `kinesis-analytics-MyApplication-us-west-2`**.
5. Choose **Create application**.

###### Note

When you create a Managed Service for Apache Flink application using the console, you have the
option of having an IAM role and policy created for your application.
Your application uses this role and policy to access its dependent
resources. These IAM resources are named using your application name
and Region as follows:

- Policy:
  `kinesis-analytics-service-`MyApplication`-`us-west-2``
- Role:
  `kinesis-analytics-MyApplication-`us-west-2``

### Edit the IAM policy

Edit the IAM policy to add permissions to access the Kinesis data
streams.

1. Open the IAM console at
   [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. Choose **Policies**. Choose the
   **`kinesis-analytics-service-MyApplication-us-west-2`**
   policy that the console created for you in the previous section.
3. On the **Summary** page, choose **Edit
   policy**. Choose the **JSON**
   tab.
4. Add the highlighted section of the following policy example to the
   policy. Replace the sample account IDs
   (`012345678901`) with your account
   ID.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "ReadCode",
 "Effect": "Allow",
 "Action": [
 "s3:GetObject",
 "logs:DescribeLogGroups",
 "s3:GetObjectVersion"
 ],
 "Resource": [
 "arn:aws:logs:us-west-2:`012345678901`:log-group:*",
 "arn:aws:s3:::ka-app-code-`<username>`/basic-beam-app-1.0.jar"
 ]
 },
 {
 "Sid": "DescribeLogStreams",
 "Effect": "Allow",
 "Action": "logs:DescribeLogStreams",
 "Resource": "arn:aws:logs:us-west-2:`012345678901`:log-group:/aws/kinesis-analytics/MyApplication:log-stream:*"
 },
 {
 "Sid": "PutLogEvents",
 "Effect": "Allow",
 "Action": "logs:PutLogEvents",
 "Resource": "arn:aws:logs:us-west-2:`012345678901`:log-group:/aws/kinesis-analytics/MyApplication:log-stream:kinesis-analytics-log-stream"
 },
 {
 "Sid": "ListCloudwatchLogGroups",
 "Effect": "Allow",
 "Action": [
 "logs:DescribeLogGroups"
 ],
 "Resource": [
 "arn:aws:logs:us-west-2:`012345678901`:log-group:*"
 ]
 }`,
 {
 "Sid": "ReadInputStream",
 "Effect": "Allow",
 "Action": "kinesis:*",
 "Resource": "arn:aws:kinesis:us-west-2:`012345678901`:stream/ExampleInputStream"
 },
 {
 "Sid": "WriteOutputStream",
 "Effect": "Allow",
 "Action": "kinesis:*",
 "Resource": "arn:aws:kinesis:us-west-2:`012345678901`:stream/ExampleOutputStream"
 }`
 ]
}`

```

### Configure the application

1. On the **MyApplication** page, choose
   **Configure**.
2. On the **Configure application** page, provide
   the **Code location**:
   - For **Amazon S3 bucket**, enter
     `ka-app-code-`<username>``.
   - For **Path to Amazon S3 object**, enter
     `basic-beam-app-1.0.jar`.

3. Under **Access to application resources**, for
   **Access permissions**, choose **Create
   / update IAM role
   `kinesis-analytics-MyApplication-us-west-2`**.
4. Enter the following:

| Group ID                    | Key                | Value                 |
| --------------------------- | ------------------ | --------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `BeamApplicationProperties` | `InputStreamName`  | `ExampleInputStream`  |
| `BeamApplicationProperties` | `OutputStreamName` | `ExampleOutputStream` |
| `BeamApplicationProperties` | `AwsRegion`        | `us-west-2`           | 5. Under **Monitoring**, ensure that the **Monitoring metrics level** is set to **Application**. 6. For **CloudWatch logging**, select the **Enable** check box. 7. Choose **Update**. ###### Note When you choose to enable CloudWatch logging, Managed Service for Apache Flink creates a log group and log stream for you. The names of these resources are as follows: <br>• Log group: `/aws/kinesis-analytics/MyApplication` <br>• Log stream: `kinesis-analytics-log-stream` This log stream is used to monitor the application. This is not the same log stream that the application uses to send results. ### Run the application The Flink job graph can be viewed by running the application, opening the Apache Flink dashboard, and choosing the desired Flink job. You can check the Managed Service for Apache Flink metrics on the CloudWatch console to verify that the application is working. ## Clean up AWS resources This section includes procedures for cleaning up AWS resources created in the Tumbling Window tutorial. ###### This topic contains the following sections: <br>• [Delete your Managed Service for Apache Flink application](#examples-beam-cleanup-app "#examples-beam-cleanup-app") <br>• [Delete your Kinesis data streams](#examples-beam-cleanup-stream "#examples-beam-cleanup-stream") <br>• [Delete your Amazon S3 object and bucket](#examples-beam-cleanup-s3 "#examples-beam-cleanup-s3") <br>• [Delete your IAM resources](#examples-beam-cleanup-iam "#examples-beam-cleanup-iam") <br>• [Delete your CloudWatch resources](#examples-beam-cleanup-cw "#examples-beam-cleanup-cw") ### Delete your Managed Service for Apache Flink application 1. Sign in to the AWS Management Console, and open the Amazon MSF console at https://console.aws.amazon.com/flink. 2. in the Managed Service for Apache Flink panel, choose **MyApplication**. 3. In the application's page, choose **Delete** and then confirm the deletion. ### Delete your Kinesis data streams 1. Open the Kinesis console at [https://console.aws.amazon.com/kinesis](https://console.aws.amazon.com/kinesis "https://console.aws.amazon.com/kinesis"). 2. In the Kinesis Data Streams panel, choose **ExampleInputStream**. 3. In the **ExampleInputStream** page, choose **Delete Kinesis Stream** and then confirm the deletion. 4. In the **Kinesis streams** page, choose the **ExampleOutputStream**, choose **Actions**, choose **Delete**, and then confirm the deletion. ### Delete your Amazon S3 object and bucket 1. Open the Amazon S3 console at [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/"). 2. Choose the **ka-app-code-`<username>` bucket.** 3. Choose **Delete** and then enter the bucket name to confirm deletion. ### Delete your IAM resources 1. Open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/"). 2. In the navigation bar, choose **Policies**. 3. In the filter control, enter **kinesis**. 4. Choose the **kinesis-analytics-service-MyApplication-us-west-2** policy. 5. Choose **Policy Actions** and then choose **Delete**. 6. In the navigation bar, choose **Roles**. 7. Choose the **kinesis-analytics-MyApplication-us-west-2** role. 8. Choose **Delete role** and then confirm the deletion. ### Delete your CloudWatch resources 1. Open the CloudWatch console at [https://console.aws.amazon.com/cloudwatch/](https://console.aws.amazon.com/cloudwatch/ "https://console.aws.amazon.com/cloudwatch/"). 2. In the navigation bar, choose **Logs**. 3. Choose the **/aws/kinesis-analytics/MyApplication** log group. 4. Choose **Delete Log Group** and then confirm the deletion. ## Next steps Now that you've created and run a basic Managed Service for Apache Flink application that transforms data using Apache Beam, see the following application for an example of a more advanced Managed Service for Apache Flink solution. <br>• **[Beam on Managed Service for Apache Flink Streaming Workshop](https://streaming-analytics.workshop.aws/beam-on-kda/ "https://streaming-analytics.workshop.aws/beam-on-kda/")**: In this workshop, we explore an end to end example that combines batch and streaming aspects in one uniform Apache Beam pipeline. |
