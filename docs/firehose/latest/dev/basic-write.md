

# Send data to a Firehose stream
<a name="basic-write"></a>

This section describes how you can use different data sources to send data to your Firehose stream. If you are new to Amazon Data Firehose, take some time to become familiar with the concepts and terminology presented in [What is Amazon Data Firehose?](what-is-this-service.md).

**Note**  
Some AWS services can only send messages and events to a Firehose stream that is in the same Region. If your Firehose stream doesn't appear as an option when you're configuring a target for Amazon CloudWatch Logs, CloudWatch Events, or AWS IoT, verify that your Firehose stream is in the same Region as your other services. For information on service endpoints for each Region, see [Amazon Data Firehose endpoints](https://docs.aws.amazon.com/general/latest/gr/fh.html#fh_region).

You can send data to your Firehose stream from the following data sources.

**Topics**
+ [Configure Kinesis agent to send data](writing-with-agents.md)
+ [Send data with AWS SDK](writing-with-sdk.md)
+ [Send CloudWatch Logs to Firehose](writing-with-cloudwatch-logs.md)
+ [Send CloudWatch Events to Firehose](writing-with-cloudwatch-events.md)
+ [Configure AWS IoT to send data to Firehose](writing-with-iot.md)