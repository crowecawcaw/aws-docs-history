# Use `CreateLogStream` with an AWS SDK or CLI

The following code examples show how to use `CreateLogStream`.

.NET

**SDK for .NET**

###### Note

There's more on GitHub. Find the complete example and learn how to set up and run in the
[AWS Code
Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/dotnetv3/CloudWatchLogs#code-examples "https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/dotnetv3/CloudWatchLogs#code-examples").

```
    using System;
    using System.Threading.Tasks;
    using Amazon.CloudWatchLogs;
    using Amazon.CloudWatchLogs.Model;

    /// <summary>
    /// Shows how to create an Amazon CloudWatch Logs stream for a CloudWatch
    /// log group.
    /// </summary>
    public class CreateLogStream
    {
        public static async Task Main()
        {
            // This client object will be associated with the same AWS Region
            // as the default user on this system. If you need to use a
            // different AWS Region, pass it as a parameter to the client
            // constructor.
            var client = new AmazonCloudWatchLogsClient();
            string logGroupName = "cloudwatchlogs-example-loggroup";
            string logStreamName = "cloudwatchlogs-example-logstream";

            var request = new CreateLogStreamRequest
            {
                LogGroupName = logGroupName,
                LogStreamName = logStreamName,
            };

            var response = await client.CreateLogStreamAsync(request);

            if (response.HttpStatusCode == System.Net.HttpStatusCode.OK)
            {
                Console.WriteLine($"{logStreamName} successfully created for {logGroupName}.");
            }
            else
            {
                Console.WriteLine("Could not create stream.");
            }
        }
    }



```

- For API details, see
  [CreateLogStream](../../../goto/DotNetSDKV3/logs-2014-03-28/CreateLogStream.md "../../../goto/DotNetSDKV3/logs-2014-03-28/CreateLogStream.md")
  in _AWS SDK for .NET API Reference_.

CLI

**AWS CLI**

The following command creates a log stream named `20150601` in the log group `my-logs`:

```
`aws logs create-log-stream --log-group-name `my-logs` --log-stream-name `20150601``

```

- For API details, see
  [CreateLogStream](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/logs/create-log-stream.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/logs/create-log-stream.html")
  in _AWS CLI Command Reference_.

For a complete list of AWS SDK developer guides and code examples, see
[Using CloudWatch Logs with an AWS SDK](sdk-general-information-section.md "sdk-general-information-section.md").
This topic also includes information about getting started and details about previous SDK versions.
