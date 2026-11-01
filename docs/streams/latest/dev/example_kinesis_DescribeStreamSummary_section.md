

# Use `DescribeStreamSummary` with an AWS SDK or CLI
<a name="example_kinesis_DescribeStreamSummary_section"></a>

The following code examples show how to use `DescribeStreamSummary`.

Action examples are code excerpts from larger programs and must be run in context. You can see this action in context in the following code example: 
+  [Learn the basics](example_kinesis_Scenario_GettingStarted_section.md) 

------
#### [ CLI ]

**AWS CLI**  
**To describe a data stream summary**  
The following `describe-stream-summary` example provides a summarized description (without the shard list) of the specified data stream.  

```
aws kinesis describe-stream-summary \
    --stream-name {{samplestream}}
```
Output:  

```
{
    "StreamDescriptionSummary": {
        "StreamName": "samplestream",
        "StreamARN": "arn:aws:kinesis:us-west-2:123456789012:stream/samplestream",
        "StreamStatus": "ACTIVE",
        "RetentionPeriodHours": 48,
        "StreamCreationTimestamp": 1572297168.0,
        "EnhancedMonitoring": [
            {
                "ShardLevelMetrics": []
            }
        ],
        "EncryptionType": "NONE",
        "OpenShardCount": 3,
        "ConsumerCount": 0
    }
}
```
For more information, see [Creating and Managing Streams](https://docs.aws.amazon.com/streams/latest/dev/working-with-streams.html) in the *Amazon Kinesis Data Streams Developer Guide*.  
+  For API details, see [DescribeStreamSummary](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/kinesis/describe-stream-summary.html) in *AWS CLI Command Reference*. 

------
#### [ Python ]

**SDK for Python (Boto3)**  
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/python/example_code/kinesis#code-examples). 

```
    def describe_stream_summary(self, stream_name):
        """
        Provides a summarized description of a Kinesis data stream.

        :param stream_name: The name of the stream to describe.
        :return: A dictionary containing the stream description summary.
        """
        try:
            response = self.kinesis_client.describe_stream_summary(
                StreamName=stream_name
            )
            summary = response.get("StreamDescriptionSummary", dict())
            logger.info(
                "Described stream summary for '%s'. Status: %s.",
                stream_name,
                summary.get("StreamStatus", "UNKNOWN"),
            )
            return summary
        except ClientError as err:
            if err.response["Error"]["Code"] == "ResourceNotFoundException":
                logger.error(
                    "Stream '%s' not found. Verify the stream name.", stream_name
                )
            raise
```
+  For API details, see [DescribeStreamSummary](https://docs.aws.amazon.com/goto/boto3/kinesis-2013-12-02/DescribeStreamSummary) in *AWS SDK for Python (Boto3) API Reference*. 

------

For a complete list of AWS SDK developer guides and code examples, see [Using this service with an AWS SDK](sdk-general-information-section.md). This topic also includes information about getting started and details about previous SDK versions.