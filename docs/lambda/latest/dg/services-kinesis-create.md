# Process Amazon Kinesis Data Streams records with Lambda

To process Amazon Kinesis Data Streams records with Lambda, create a Lambda event source mapping. You can map a Lambda function to a standard iterator or enhanced fan-out consumer. For more information, see [Polling and batching streams](with-kinesis.md#kinesis-polling-and-batching "with-kinesis.md#kinesis-polling-and-batching").

## Create an Kinesis event source mapping

To invoke your Lambda function with records from your data stream, create an [event source mapping](invocation-eventsourcemapping.md "invocation-eventsourcemapping.md").
You can create multiple event source mappings to process the same data with multiple Lambda functions, or to process items
from multiple data streams with a single function. When processing items from multiple streams, each batch contains records
from only a single shard or stream.

You can configure event source mappings to process records from a stream in a different AWS account.
To learn more, see [Creating a cross-account event source mapping](#services-kinesis-eventsourcemapping-cross-account "#services-kinesis-eventsourcemapping-cross-account").

Before you create an event source mapping, you need to give your Lambda function permission to read from a Kinesis data stream.
Lambda needs the following permissions to manage resources related to your Kinesis data stream:

- [kinesis:DescribeStream](../api/API_DescribeStream.md "../api/API_DescribeStream.md")
- [kinesis:DescribeStreamSummary](../api/API_DescribeStreamSummary.md "../api/API_DescribeStreamSummary.md")
- [kinesis:GetRecords](../api/API_GetRecords.md "../api/API_GetRecords.md")
- [kinesis:GetShardIterator](../api/API_GetShardIterator.md "../api/API_GetShardIterator.md")
- [kinesis:ListShards](../api/API_ListShards.md "../api/API_ListShards.md")
- [kinesis:SubscribeToShard](../api/API_SubscribeToShard.md "../api/API_SubscribeToShard.md")

The AWS managed policy [AWSLambdaKinesisExecutionRole](../../../aws-managed-policy/latest/reference/AWSLambdaKinesisExecutionRole.md "../../../aws-managed-policy/latest/reference/AWSLambdaKinesisExecutionRole.md")
includes these permissions. Add this managed policy to your function as described in the following procedure.

###### Note

- You don't need the `kinesis:ListStreams` permission to create and manage
  event source mappings for Kinesis. However, if you create an event source mapping in the console and you don't have this permission, you won't be able to select a Kinesis
  stream from a dropdown list and the console will display an error. To create the event source mapping, you'll need to manually enter the Amazon Resource Name (ARN) of your stream.
- Lambda makes `kinesis:GetRecords` and `kinesis:GetShardIterator` API calls when retrying failed invocations.

AWS Management Console

###### To add Kinesis permissions to your function

1. Open the [Functions page](https://console.aws.amazon.com/lambda/home#/functions "https://console.aws.amazon.com/lambda/home#/functions") of the Lambda console
   and select your function.
2. In the **Configuration** tab, select **Permissions**.
3. In the **Execution role** pane, under **Role name**, choose the link to
   your function’s execution role. This link opens the page for that role in the IAM console.
4. In the **Permissions policies** pane, choose **Add permissions**, then
   select **Attach policies**.
5. In the search field, enter `AWSLambdaKinesisExecutionRole`.
6. Select the checkbox next to the policy and choose **Add permission**.

AWS CLI

###### To add Kinesis permissions to your function

- Run the following CLI command to add the `AWSLambdaKinesisExecutionRole` policy to your function’s execution role:

```
`aws iam attach-role-policy \
--role-name `MyFunctionRole` \
--policy-arn arn:aws:iam::aws:policy/service-role/AWSLambdaKinesisExecutionRole`
```

AWS SAM

###### To add Kinesis permissions to your function

- In your function’s definition, add the `Policies` property as shown in the following example:

```
Resources:
  MyFunction:
    Type: AWS::Serverless::Function
    Properties:
      CodeUri: ./my-function/
      Handler: index.handler
      Runtime: nodejs22.x
      Policies:
        - AWSLambdaKinesisExecutionRole
```

After configuring the required permissions, create the event source mapping.

AWS Management Console

###### To create the Kinesis event source mapping

1. Open the [Functions page](https://console.aws.amazon.com/lambda/home#/functions "https://console.aws.amazon.com/lambda/home#/functions") of the Lambda console
   and select your function.
2. In the **Function overview** pane, choose **Add trigger**.
3. Under **Trigger configuration**, for the source, select **Kinesis**.
4. Select the Kinesis stream you want to create the event source mapping for and, optionally, a consumer of your stream.
5. (Optional) edit the **Batch size**, **Starting position**, and **Batch window**
   for your event source mapping.
6. Choose **Add**.

When creating your event source mapping from the console, your IAM role must have the
[kinesis:ListStreams](../api/API_ListStreams.md "../api/API_ListStreams.md") and
[kinesis:ListStreamConsumers](../api/API_ListStreamConsumers.md "../api/API_ListStreamConsumers.md") permissions.

AWS CLI

###### To create the Kinesis event source mapping

- Run the following CLI command to create a Kinesis event source mapping. Choose your own batch size and starting
  position according to your use case.

```
`aws lambda create-event-source-mapping \
--function-name `MyFunction` \
--event-source-arn `arn:aws:kinesis:us-east-2:123456789012:stream/lambda-stream` \
--starting-position `LATEST` \
--batch-size `100``
```

To specify a batching window, add the `--maximum-batching-window-in-seconds` option. For more information about using this and other parameters, see [create-event-source-mapping](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/create-event-source-mapping.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/create-event-source-mapping.html")
in the _AWS CLI Command Reference_.

AWS SAM

###### To create the Kinesis event source mapping

- In your function’s definition, add the `KinesisEvent` property as shown in the following example:

```
Resources:
  MyFunction:
    Type: AWS::Serverless::Function
    Properties:
      CodeUri: ./my-function/
      Handler: index.handler
      Runtime: nodejs22.x
      Policies:
        - AWSLambdaKinesisExecutionRole
      Events:
        KinesisEvent:
          Type: Kinesis
          Properties:
            Stream: !GetAtt MyKinesisStream.Arn
            StartingPosition: LATEST
            BatchSize: 100

  MyKinesisStream:
    Type: AWS::Kinesis::Stream
    Properties:
      ShardCount: 1
```

To learn more about creating an event source mapping for Kinesis Data Streams in AWS SAM, see [Kinesis](../../../serverless-application-model/latest/developerguide/sam-property-function-kinesis.md "../../../serverless-application-model/latest/developerguide/sam-property-function-kinesis.md")
in the _AWS Serverless Application Model Developer Guide_.

## Polling and stream starting position

Be aware that stream polling during event source mapping creation and updates is eventually consistent.

- During event source mapping creation, it may take several minutes to start polling events from the stream.
- During event source mapping updates, it may take several minutes to stop and restart polling events from the stream.

This behavior means that if you specify `LATEST` as the starting position for the stream, the event source mapping could
miss events during creation or updates. To ensure that no events are missed, specify the stream starting position as `TRIM_HORIZON`
or `AT_TIMESTAMP`.

## Creating a cross-account event source mapping

Amazon Kinesis Data Streams supports [resource-based policies](../../../IAM/latest/UserGuide/access_policies_identity-vs-resource.md "../../../IAM/latest/UserGuide/access_policies_identity-vs-resource.md").
Because of this, you can process data ingested into a stream in one AWS account with a Lambda function in another account.

To create an event source mapping for your Lambda function using a Kinesis stream in a different AWS account, you must
configure the stream using a resource-based policy to give your Lambda function permission to read items. To learn how to
configure your stream to allow cross-account access, see [Sharing access with cross-account AWS Lambda functions](../../../streams/latest/dev/resource-based-policy-examples.md#Resource-based-policy-examples-lambda "../../../streams/latest/dev/resource-based-policy-examples.md#Resource-based-policy-examples-lambda")
in the _Amazon Kinesis Streams Developer guide_.

Once you’ve configured your stream with a resource-based policy that gives your Lambda function the required
permissions, create the event source mapping using any of the methods described in the previous section.

If you choose to create your event source mapping using the Lambda console, paste the ARN of your stream directly
into the input field. If you want to specify a consumer for your stream, pasting the ARN of the
consumer automatically populates the stream field.
