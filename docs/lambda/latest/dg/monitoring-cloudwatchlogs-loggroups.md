# Configuring CloudWatch log groups

By default, CloudWatch automatically creates a log group named `/aws/lambda/<function name>` for your function when it's first invoked. To configure your function to send logs to an existing log group,
or to create a new log group for your function, you can use the Lambda console or the AWS CLI. You can also configure custom log groups using the [CreateFunction](../api/API_CreateFunction.md "../api/API_CreateFunction.md") and [UpdateFunctionConfiguration](../api/API_UpdateFunctionConfiguration.md "../api/API_UpdateFunctionConfiguration.md")
Lambda API commands and the AWS Serverless Application Model (AWS SAM) AWS::Serverless::Function resource.

You can configure multiple Lambda functions to send logs to the same CloudWatch log group. For example, you could use a single log group to store logs for all of the Lambda functions that make up a particular application. When
you use a custom log group for a Lambda function, the log streams Lambda creates include the function name and function version. This ensures that
the mapping between log messages and functions is preserved, even if you use the same log group for multiple functions.

The log stream naming format for custom log groups follows this convention:

```
YYYY/MM/DD/<function_name>[<function_version>][<execution_environment_GUID>]
```

Note that when configuring a custom log group, the name you select for your log group must follow the [CloudWatch Logs naming rules](../../../AmazonCloudWatchLogs/latest/APIReference/API_CreateLogGroup.md "../../../AmazonCloudWatchLogs/latest/APIReference/API_CreateLogGroup.md").
Additionally, custom log group names mustn't begin with the string `aws/`. If you create a custom log group beginning with `aws/`,
Lambda won't be able to create the log group. As a result of this, your function's logs won't be sent to CloudWatch.

###### To change a function’s log group (console)

1. Open the [Functions page](https://console.aws.amazon.com/lambda/home#/functions "https://console.aws.amazon.com/lambda/home#/functions") of the Lambda console.
2. Choose a function.
3. On the function configuration page, choose **Monitoring and operations tools**.
4. In the **Logging configuration** pane, choose **Edit**.
5. In the **Logging group** pane, for **CloudWatch log group**, choose **Custom**.
6. Under **Custom log group**, enter the name of the CloudWatch log group you want your function to send logs to. If you enter the
   name of an existing log group, then your function will use that group. If no log group exists with the name that you enter, then Lambda will
   create a new log group for your function with that name.

###### To change a function's log group (AWS CLI)

- To change the log group of an existing function, use the [update-function-configuration](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/update-function-configuration.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/update-function-configuration.html") command.

```
`aws lambda update-function-configuration \
 --function-name myFunction \
 --logging-config LogGroup=myLogGroup`
```

###### To specify a custom log group when you create a function (AWS CLI)

- To specify a custom log group when you create a new Lambda function using the AWS CLI, use the `--logging-config` option. The following example command creates a Node.js Lambda function that sends logs to a log group named `myLogGroup`.

```
`aws lambda create-function \
 --function-name myFunction \
 --runtime nodejs22.x \
 --handler index.handler \
 --zip-file fileb://function.zip \
 --role arn:aws:iam::123456789012:role/LambdaRole \
 --logging-config LogGroup=myLogGroup`
```

## Execution role permissions

For your function to send logs to CloudWatch Logs, it must have the [logs:PutLogEvents](../../../AmazonCloudWatchLogs/latest/APIReference/API_PutLogEvents.md "../../../AmazonCloudWatchLogs/latest/APIReference/API_PutLogEvents.md") permission.
When you configure your function's log group using the Lambda console, Lambda will add this permission to the role under the following conditions:

- The service destination is set to CloudWatch Logs
- Your function's execution role doesn't have permissions to upload logs to CloudWatch Logs (the default destination)

###### Note

Lambda does not add any Put permission for Amazon S3 or Firehose log destinations.

When Lambda adds this permission, it gives the function permission to send logs to any CloudWatch Logs log group.

To prevent Lambda from automatically updating the function's execution role and edit it manually instead, expand **Permissions** and uncheck **Add required permissions**.

When you configure your function's log group using the AWS CLI, Lambda won't automatically add the `logs:PutLogEvents` permission. Add the
permission to your function's execution role if it doesn't already have it. This permission is included in the
[AWSLambdaBasicExecutionRole](https://console.aws.amazon.com/iam/home#/policies/arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole$jsonEditor "https://console.aws.amazon.com/iam/home#/policies/arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole$jsonEditor")
managed policy.
