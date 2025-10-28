# Analyzing a video with the AWS Command Line Interface

You can use the AWS Command Line Interface (AWS CLI) to call Amazon Rekognition Video operations. The design pattern is
the same as using the Amazon Rekognition Video API with the AWS SDK for Java or other AWS SDKs. For more
information, see [Amazon Rekognition Video API overview](video.md#video-api-overview "video.md#video-api-overview"). The following procedures show how to use the AWS CLI to detect labels in a
video.

You start detecting labels in a video by calling `start-label-detection`.
When Amazon Rekognition finishes analyzing the video, the completion status is sent to the Amazon SNS
topic that's specified in the `--notification-channel` parameter of
`start-label-detection`. You can get the completion status by subscribing
an Amazon Simple Queue Service (Amazon SQS) queue to the Amazon SNS topic. You then poll [receive-message](../../../cli/latest/reference/sqs/receive-message.md "../../../cli/latest/reference/sqs/receive-message.md") to get the completion status from the Amazon SQS queue.

When calling `StartLabelDetection`, you can filter your results by
providing filtration arguments to the `LabelsInclusionFilter` and/or
`LabelsExclusionFilter` arguments. For more information, see [Detecting labels in a video](labels-detecting-labels-video.md "labels-detecting-labels-video.md") .

The completion status notification is a JSON structure within the
`receive-message` response. You need to extract the JSON from the
response. For information about the completion status JSON, see [Reference: Video analysis results
notification](video-notification-payload.md "video-notification-payload.md").
If the value of the `Status` field of the completed status JSON is
`SUCCEEDED`, you can get the results of the video analysis request by
calling `get-label-detection`. When calling `GetLabelDetection`,
you can sort and aggregate the returned results using the `SortBy` and
`AggregateBy` arguments.

The following procedures don't include code to poll the Amazon SQS queue. Also, they don't
include code to parse the JSON that's returned from the Amazon SQS queue. For an example in
Java, see [Analyzing a video stored in an Amazon S3
bucket with Java or Python (SDK)](video-analyzing-with-sqs.md "video-analyzing-with-sqs.md").

## Prerequisites

To run this procedure, you need to have the AWS CLI installed. For more information,
see [Getting started with Amazon Rekognition](getting-started.md "getting-started.md"). The AWS
account that you use must have access permissions to the Amazon Rekognition API. For more
information, [Actions Defined by Amazon Rekognition](../../../IAM/latest/UserGuide/list_amazonrekognition.md#amazonrekognition-actions-as-permissions "../../../IAM/latest/UserGuide/list_amazonrekognition.md#amazonrekognition-actions-as-permissions").

###### To configure Amazon Rekognition Video and upload a video

1. Configure user access to Amazon Rekognition Video and configure Amazon Rekognition Video access to Amazon SNS. For
   more information, see [Configuring Amazon Rekognition Video](api-video-roles.md "api-video-roles.md").
2. Upload an MOV or MPEG-4 format video file to your S3 bucket. While developing
   and testing, we suggest using short videos no longer than 30 seconds in
   length.

For instructions, see [Uploading Objects into
Amazon S3](../../../AmazonS3/latest/userguide/UploadingObjectsintoAmazonS3.md "../../../AmazonS3/latest/userguide/UploadingObjectsintoAmazonS3.md") in the _Amazon Simple Storage Service User Guide_.

###### To detect labels in a video

1. Run the following AWS CLI command to start detecting labels in a video.

```
aws rekognition start-label-detection --video '{"S3Object":{"Bucket":"amzn-s3-demo-bucket","Name":"video-name"}}' \
 --notification-channel '{"SNSTopicArn":"TopicARN","RoleArn":"RoleARN"}' \
--region region-name  \
--features GENERAL_LABELS \
--profile profile-name \
--settings "{"GeneralLabels":{"LabelInclusionFilters":["Car"]}}
```

Update the following values:

    * Change `amzn-s3-demo-bucket` and `videofile` to the Amazon S3
     bucket name and file name that you specified in step 2.
    * Change `us-east-1` to the AWS region that you're
     using.
    * Replace the value of `profile_name` in the line that
     creates the Rekognition session with the name of your developer
     profile.
    * Change `TopicARN` to the ARN of the Amazon SNS topic you created
     in step 3 of [Configuring Amazon Rekognition Video](api-video-roles.md "api-video-roles.md").
    * Change `RoleARN` to the ARN of the IAM service role you
     created in step 7 of [Configuring Amazon Rekognition Video](api-video-roles.md "api-video-roles.md").
    * If required, you can specify the `endpoint-url`. The AWS
     CLI should automatically determine the proper endpoint URL based on the
     provided region. However, if you are using an endpoint [from your private VPC](../../../vpc/latest/userguide/what-is-amazon-vpc.md#what-is-privatelink "../../../vpc/latest/userguide/what-is-amazon-vpc.md#what-is-privatelink"), you may need to specify the
     `endpoint-url`. The [AWS Service Endpoints](../../../general/latest/gr/rande.md#regional-endpoints "../../../general/latest/gr/rande.md#regional-endpoints") resource lists the syntax for
     specifying endpoint urls and the names and codes for each region.
    * You can also include filtration criteria in the settings paramter. For
     example, you can use a `LabelsInclusionFilter` or a
     `LabelsExclusionFilter` alongside a list of desired
     values.

If you are accessing the CLI on a Windows device, use double quotes instead
of single quotes and escape the inner double quotes by backslash (i.e. \) to
address any parser errors you may encounter. For an example, see below:

```

aws rekognition start-label-detection --video "{\"S3Object\":{\"Bucket\":\"amzn-s3-demo-bucket",\"Name\":\"video-name\"}}" --notification-channel "{\"SNSTopicArn\":\"TopicARN\",\"RoleArn\":\"RoleARN\"}" \
--region us-east-1 --features GENERAL_LABELS --settings "{\"GeneralLabels\":{\"LabelInclusionFilters\":[\"Car\"]}}" --profile profile-name

```

2. Note the value of `JobId` in the response. The response looks
   similar to the following JSON example.

```
{
    "JobId": "547089ce5b9a8a0e7831afa655f42e5d7b5c838553f1a584bf350ennnnnnnnnn"
}
```

3. Write code to poll the Amazon SQS queue for the completion status JSON (by using
   [receive-message](../../../cli/latest/reference/sqs/receive-message.md "../../../cli/latest/reference/sqs/receive-message.md")).
4. Write code to extract the `Status` field from the completion status
   JSON.
5. If the value of `Status` is `SUCCEEDED`, run the
   following AWS CLI command to show the label detection results.

```
aws rekognition get-label-detection  --job-id `JobId` \
--region `us-east-1` --sort-by TIMESTAMP aggregate-by TIMESTAMPS

```

Update the following values:

    * Change `JobId` to match the job identifier that you noted
     in step 2.
    * Change `Endpoint` and `us-east-1` to the AWS
     endpoint and region that you're using.

The results look similar to the following example JSON:

```
{
    "Labels": [
        {
            "Timestamp": 0,
            "Label": {
                "Confidence": 99.03720092773438,
                "Name": "Speech"
            }
        },
        {
            "Timestamp": 0,
            "Label": {
                "Confidence": 71.6698989868164,
                "Name": "Pumpkin"
            }
        },
        {
            "Timestamp": 0,
            "Label": {
                "Confidence": 71.6698989868164,
                "Name": "Squash"
            }
        },
        {
            "Timestamp": 0,
            "Label": {
                "Confidence": 71.6698989868164,
                "Name": "Vegetable"
            }
        }, .......
```
