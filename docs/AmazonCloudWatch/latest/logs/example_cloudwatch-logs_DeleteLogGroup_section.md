

# Use `DeleteLogGroup` with an AWS SDK or CLI
<a name="example_cloudwatch-logs_DeleteLogGroup_section"></a>

The following code examples show how to use `DeleteLogGroup`.

Action examples are code excerpts from larger programs and must be run in context. You can see this action in context in the following code examples: 
+  [Configure container service connectivity](example_ecs_ServiceConnect_085_section.md) 
+  [Creating your first serverless function](example_lambda_GettingStarted_019_section.md) 

------
#### [ .NET ]

**SDK for .NET**  
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/dotnetv3/CloudWatchLogs#code-examples). 

```
    using System;
    using System.Threading.Tasks;
    using Amazon.CloudWatchLogs;
    using Amazon.CloudWatchLogs.Model;

    /// <summary>
    /// Uses the Amazon CloudWatch Logs Service to delete an existing
    /// CloudWatch Logs log group.
    /// </summary>
    public class DeleteLogGroup
    {
        public static async Task Main()
        {
            var client = new AmazonCloudWatchLogsClient();
            string logGroupName = "cloudwatchlogs-example-loggroup";

            var request = new DeleteLogGroupRequest
            {
                LogGroupName = logGroupName,
            };

            var response = await client.DeleteLogGroupAsync(request);

            if (response.HttpStatusCode == System.Net.HttpStatusCode.OK)
            {
                Console.WriteLine($"Successfully deleted CloudWatch log group, {logGroupName}.");
            }
        }
    }
```
+  For API details, see [DeleteLogGroup](https://docs.aws.amazon.com/goto/DotNetSDKV3/logs-2014-03-28/DeleteLogGroup) in *AWS SDK for .NET API Reference*. 

------
#### [ CLI ]

**AWS CLI**  
The following command deletes a log group named `my-logs`:  

```
aws logs delete-log-group --log-group-name {{my-logs}}
```
+  For API details, see [DeleteLogGroup](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/logs/delete-log-group.html) in *AWS CLI Command Reference*. 

------
#### [ JavaScript ]

**SDK for JavaScript (v3)**  
 There's more on GitHub. Find the complete example and learn how to set up and run in the [AWS Code Examples Repository](https://github.com/awsdocs/aws-doc-sdk-examples/tree/main/javascriptv3/example_code/cloudwatch-logs#code-examples). 

```
import { DeleteLogGroupCommand } from "@aws-sdk/client-cloudwatch-logs";
import { client } from "../libs/client.js";

const run = async () => {
  const command = new DeleteLogGroupCommand({
    // The name of the log group.
    logGroupName: process.env.CLOUDWATCH_LOGS_LOG_GROUP,
  });

  try {
    return await client.send(command);
  } catch (err) {
    console.error(err);
  }
};

export default run();
```
+  For API details, see [DeleteLogGroup](https://docs.aws.amazon.com/AWSJavaScriptSDK/v3/latest/client/cloudwatch-logs/command/DeleteLogGroupCommand) in *AWS SDK for JavaScript API Reference*. 

------

For a complete list of AWS SDK developer guides and code examples, see [Using CloudWatch Logs with an AWS SDK](sdk-general-information-section.md). This topic also includes information about getting started and details about previous SDK versions.