

# Set up application logging in Managed Service for Apache Flink
<a name="cloudwatch-logs"></a>

By adding an Amazon CloudWatch logging option to your Managed Service for Apache Flink application, you can monitor for application events or configuration problems.

This topic describes how to configure your application to write application events to a CloudWatch Logs stream. A CloudWatch logging option is a collection of application settings and permissions that your application uses to configure the way it writes application events to CloudWatch Logs. You can add and configure a CloudWatch logging option using either the AWS Management Console or the AWS Command Line Interface (AWS CLI).

Note the following about adding a CloudWatch logging option to your application:
+ When you add a CloudWatch logging option using the console, Managed Service for Apache Flink creates the CloudWatch log group and log stream for you and adds the permissions your application needs to write to the log stream. 
+ When you add a CloudWatch logging option using the API, you must also create the application's log group and log stream, and add the permissions your application needs to write to the log stream.

## Set up CloudWatch logging using the console
<a name="cloudwatch-logs-console"></a>

When you enable CloudWatch logging for your application in the console, a CloudWatch log group and log stream is created for you. Also, your application's permissions policy is updated with permissions to write to the stream. 

Managed Service for Apache Flink creates a log group named using the following convention, where {{ApplicationName}} is your application's name.

```
/aws/kinesis-analytics/{{ApplicationName}}
```

Managed Service for Apache Flink creates a log stream in the new log group with the following name.

```
kinesis-analytics-log-stream
```

You set the application monitoring metrics level and monitoring log level using the **Monitoring log level** section of the **Configure application** page. For information about application log levels, see [Control application monitoring levels](#cloudwatch_levels).

## Set up CloudWatch logging using the CLI
<a name="cloudwatch-logs-api"></a>

To add a CloudWatch logging option using the AWS CLI, you complete the following: 
+ Create a CloudWatch log group and log stream.
+ Add a logging option when you create an application by using the [CreateApplication](https://docs.aws.amazon.com/managed-service-for-apache-flink/latest/apiv2/API_CreateApplication.html) action, or add a logging option to an existing application using the [AddApplicationCloudWatchLoggingOption](https://docs.aws.amazon.com/managed-service-for-apache-flink/latest/apiv2/API_AddApplicationCloudWatchLoggingOption.html) action.
+ Add permissions to your application's policy to write to the logs.

### Create a CloudWatch log group and log stream
<a name="cloudwatch-logs-api-create"></a>

You create a CloudWatch log group and stream using either the CloudWatch Logs console or the API. For information about creating a CloudWatch log group and log stream, see [Working with Log Groups and Log Streams](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.html).

### Work with application CloudWatch logging options
<a name="adding_cloudwatch"></a>

Use the following API actions to add a CloudWatch log option to a new or existing application or change a log option for an existing application. For information about how to use a JSON file for input for an API action, see [Managed Service for Apache Flink API example code](api-examples.md).

#### Add a CloudWatch log option when creating an application
<a name="add_cloudwatch_create"></a>

The following example demonstrates how to use the `CreateApplication` action to add a CloudWatch log option when you create an application. In the example, replace {{Amazon Resource Name (ARN) of the CloudWatch Log stream to add to the new application}} with your own information. For more information about the action, see [`CreateApplication`](https://docs.aws.amazon.com/managed-service-for-apache-flink/latest/apiv2/API_CreateApplication.html).

```
{
    "ApplicationName": "test",
    "ApplicationDescription": "test-application-description",
    "RuntimeEnvironment": "FLINK-1_15",
    "ServiceExecutionRole": "arn:aws:iam::123456789123:role/myrole",
    "ApplicationConfiguration": {
        "ApplicationCodeConfiguration": {
            "CodeContent": {
                "S3ContentLocation":{
                              "BucketARN": "arn:aws:s3:::amzn-s3-demo-bucket",
                              "FileKey": "myflink.jar"
                }
            },
            "CodeContentType": "ZIPFILE"
        }
    },
    "CloudWatchLoggingOptions": [{
      "LogStreamARN": "{{<Amazon Resource Name (ARN) of the CloudWatch log stream to add to the new application>}}"
	}]
}
```

#### Add a CloudWatch log option to an existing application
<a name="add_to_existing_app"></a>

The following example demonstrates how to use the `AddApplicationCloudWatchLoggingOption` action to add a CloudWatch log option to an existing application. In the example, replace each {{user input placeholder}} with your own information. For more information about the action, see [`AddApplicationCloudWatchLoggingOption`](https://docs.aws.amazon.com/managed-service-for-apache-flink/latest/apiv2/API_AddApplicationCloudWatchLoggingOption.html).

```
{
   "ApplicationName": "{{<Name of the application to add the log option to>}}",
   "CloudWatchLoggingOption": { 
      "LogStreamARN": "{{<ARN of the log stream to add to the application>}}"
   },
   "CurrentApplicationVersionId": {{<Version of the application to add the log to>}}
}
```

#### Update an existing CloudWatch log option
<a name="update_existing"></a>

The following example demonstrates how to use the `UpdateApplication` action to modify an existing CloudWatch log option. In the example, replace each {{user input placeholder}} with your own information. For more information about the action, see [`UpdateApplication`](https://docs.aws.amazon.com/managed-service-for-apache-flink/latest/apiv2/API_UpdateApplication.html).

```
{
   "ApplicationName": "{{<Name of the application to update the log option for>}}",
   "CloudWatchLoggingOptionUpdates": [ 
         { 
            "CloudWatchLoggingOptionId": "{{<ID of the logging option to modify>}}",
            "LogStreamARNUpdate": "{{<ARN of the new log stream to use>}}"
         }
      ],
   "CurrentApplicationVersionId": {{<ID of the application version to modify>}}
}
```

#### Delete a CloudWatch log option from an application
<a name="delete-log"></a>

The following example demonstrates how to use the `DeleteApplicationCloudWatchLoggingOption` action to delete an existing CloudWatch log option. In the example, replace each {{user input placeholder}} with your own information. For more information about the action, see [`DeleteApplicationCloudWatchLoggingOption`](https://docs.aws.amazon.com/managed-service-for-apache-flink/latest/apiv2/API_DeleteApplicationCloudWatchLoggingOption.html).

```
{
   "ApplicationName": "{{<Name of application to delete log option from>}}",
   "CloudWatchLoggingOptionId": "{{<ID of the application log option to delete>}}",
   "CurrentApplicationVersionId": {{<Version of the application to delete the log option from>}}
}
```

#### Set the application logging level
<a name="cloudwatch-level"></a>

To set the level of application logging, use the [`MonitoringConfiguration`](https://docs.aws.amazon.com/managed-service-for-apache-flink/latest/apiv2/API_MonitoringConfiguration.html) parameter of the [`CreateApplication`](https://docs.aws.amazon.com/managed-service-for-apache-flink/latest/apiv2/API_CreateApplication.html) action or the [`MonitoringConfigurationUpdate`](https://docs.aws.amazon.com/managed-service-for-apache-flink/latest/apiv2/API_MonitoringConfigurationUpdate.html) parameter of the [`UpdateApplication`](https://docs.aws.amazon.com/managed-service-for-apache-flink/latest/apiv2/API_UpdateApplication.html) action. 

For information about application log levels, see [Control application monitoring levels](#cloudwatch_levels).

##### Set the application logging level when creating an application
<a name="cloudwatch-level-create"></a>

The following example request for the [`CreateApplication`](https://docs.aws.amazon.com/managed-service-for-apache-flink/latest/apiv2/API_CreateApplication.html) action sets the application log level to `INFO`.

```
{
   "ApplicationName": "MyApplication",                    
   "ApplicationDescription": "My Application Description",
   "ApplicationConfiguration": {
      "ApplicationCodeConfiguration":{
      "CodeContent":{
        "S3ContentLocation":{
          "BucketARN":"arn:aws:s3:::amzn-s3-demo-bucket",
          "FileKey":"myflink.jar",
          "ObjectVersion":"AbCdEfGhIjKlMnOpQrStUvWxYz12345"
        }
      },
      "CodeContentType":"ZIPFILE"
      },
      "FlinkApplicationConfiguration": 
         "MonitoringConfiguration": { 
            "ConfigurationType": "CUSTOM",
            "LogLevel": "INFO"
         }
      },
   "RuntimeEnvironment": "FLINK-1_15",
   "ServiceExecutionRole": "arn:aws:iam::123456789123:role/myrole"
}
```

##### Update the application logging level
<a name="cloudwatch-level-update"></a>

The following example request for the [`UpdateApplication`](https://docs.aws.amazon.com/managed-service-for-apache-flink/latest/apiv2/API_UpdateApplication.html) action sets the application log level to `INFO`.

```
{
   "ApplicationConfigurationUpdate": {
      "FlinkApplicationConfigurationUpdate": { 
         "MonitoringConfigurationUpdate": { 
            "ConfigurationTypeUpdate": "CUSTOM",
            "LogLevelUpdate": "INFO"
         }
      }
   }
}
```

### Add permissions to write to the CloudWatch log stream
<a name="enable_putlogevents"></a>

Managed Service for Apache Flink needs permissions to write misconfiguration errors to CloudWatch. You can add these permissions to the AWS Identity and Access Management (IAM) role that Managed Service for Apache Flink assumes.

For more information about using an IAM role for Managed Service for Apache Flink, see [Identity and Access Management for Amazon Managed Service for Apache Flink](security-iam.md).

#### Trust policy
<a name="enable_putlogevents_trust_policy"></a>

To grant Managed Service for Apache Flink permissions to assume an IAM role, you can attach the following trust policy to the service execution role.

------
#### [ JSON ]

****  

```
{
  "Version":"2012-10-17",		 	 	 
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "Service": "kinesisanalytics.amazonaws.com"
      },
      "Action": "sts:AssumeRole"
    }
  ]
}
```

------

#### Permissions policy
<a name="enable_putlogevents_permissions_policy"></a>

To grant permissions to an application to write log events to CloudWatch from a Managed Service for Apache Flink resource, you can use the following IAM permissions policy. Provide the correct Amazon Resource Names (ARNs) for your log group and stream.

------
#### [ JSON ]

****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
        {
            "Sid": "Stmt0123456789000",
            "Effect": "Allow",
            "Action": [
                "logs:PutLogEvents",
                "logs:DescribeLogGroups",
                "logs:DescribeLogStreams"
            ],
            "Resource": [
                "arn:aws:logs:us-east-1:123456789012:log-group:my-log-group:log-stream:my-log-stream*",
                "arn:aws:logs:us-east-1:123456789012:log-group:my-log-group:*",
                "arn:aws:logs:us-east-1:123456789012:log-group:*"
            ]
        }
    ]
}
```

------

## Control application monitoring levels
<a name="cloudwatch_levels"></a>

You control the generation of application log messages using the application's *Monitoring Metrics Level* and *Monitoring Log Level*.

The application's monitoring metrics level controls the granularity of log messages. Monitoring metrics levels are defined as follows:
+ **Application**: Metrics are scoped to the entire application.
+ **Task**: Metrics are scoped to each task. For information about tasks, see [Implement application scaling in Managed Service for Apache Flink](how-scaling.md).
+ **Operator**: Metrics are scoped to each operator. For information about operators, see [Transform data using operators in Managed Service for Apache Flink with the DataStream API](how-operators.md).
+ **Parallelism**: Metrics are scoped to application parallelism. You can only set this metrics level using the [ MonitoringConfigurationUpdate](https://docs.aws.amazon.com/managed-flink/latest/apiv2/API_MonitoringConfigurationUpdate.html) parameter of the [ UpdateApplication](https://docs.aws.amazon.com/managed-flink/latest/apiv2/API_UpdateApplication.html) API. You cannot set this metrics level using the console. For information about parallelism, see [Implement application scaling in Managed Service for Apache Flink](how-scaling.md).

The application's monitoring log level controls the verbosity of the application's log. Monitoring log levels are defined as follows:
+ **Error**: Potential catastrophic events of the application.
+ **Warn**: Potentially harmful situations of the application.
+ **Info**: Informational and transient failure events of the application. We recommend that you use this logging level.
+ **Debug**: Fine-grained informational events that are most useful to debug an application. *Note*: Only use this level for temporary debugging purposes. 

## Apply logging best practices
<a name="cloudwatch_bestpractices"></a>

We recommend that your application use the **Info** logging level. We recommend this level to ensure that you see Apache Flink errors, which are logged at the **Info** level rather than the **Error** level.

We recommend that you use the **Debug** level only temporarily while investigating application issues. Switch back to the **Info** level when the issue is resolved. Using the **Debug** logging level will significantly affect your application's performance.

Excessive logging can also significantly impact application performance. We recommend that you do not write a log entry for every record processed, for example. Excessive logging can cause severe bottlenecks in data processing and can lead to back pressure in reading data from the sources.

## Perform logging troubleshooting
<a name="cloudwatch_troubleshooting"></a>

If application logs are not being written to the log stream, verify the following: 
+ Verify that your application's IAM role and policies are correct. Your application's policy needs the following permissions to access your log stream:
  + `logs:PutLogEvents`
  + `logs:DescribeLogGroups`
  + `logs:DescribeLogStreams`

  For more information, see [Add permissions to write to the CloudWatch log stream](#enable_putlogevents).
+ Verify that your application is running. To check your application's status, view your application's page in the console, or use the [DescribeApplication](https://docs.aws.amazon.com/managed-flink/latest/apiv2/API_DescribeApplication.html) or [ListApplications](https://docs.aws.amazon.com/managed-flink/latest/apiv2/API_ListApplications.html) actions.
+ Monitor CloudWatch metrics such as `downtime` to diagnose other application issues. For information about reading CloudWatch metrics, see [Metrics and dimensions in Managed Service for Apache Flink](metrics-dimensions.md).

## Use CloudWatch Logs Insights
<a name="cloudwatch_next"></a>

After you have enabled CloudWatch logging in your application, you can use CloudWatch Logs Insights to analyze your application logs. For more information, see [Analyze logs with CloudWatch Logs Insights](cloudwatch-logs-reading.md).