# Configuring CloudWatch log groups

By default, Lambda creates a log group named `/aws/lambda/capacity-provider/`<capacity-provider-name>`` for your capacity provider. To send logs to a different log group, use the Lambda console, AWS CLI, or the `CreateCapacityProvider` and `UpdateCapacityProvider` API commands.

When you configure a custom log group, the name must follow the [CloudWatch Logs naming rules](../../../AmazonCloudWatchLogs/latest/APIReference/API_CreateLogGroup.md "../../../AmazonCloudWatchLogs/latest/APIReference/API_CreateLogGroup.md"). Additionally, custom log group names must not begin with the string `aws/`. If you create a custom log group beginning with `aws/`, Lambda cannot create the log group, and your capacity provider does not send logs to CloudWatch.

## Log streams

Within the log group, Lambda creates log streams using the following naming format:

```
`<capacity-provider-name>`/managed-instances
```

For example, for a capacity provider named `my-capacity-provider`, the log stream is:

```
my-capacity-provider/managed-instances
```

## Configuring a custom log group

###### To change a capacity provider's log group (console)

1. Open the [Capacity providers page](https://console.aws.amazon.com/lambda/home#/capacity-providers "https://console.aws.amazon.com/lambda/home#/capacity-providers") of the Lambda console.
2. Choose a capacity provider.
3. Choose **Additional configuration**.
4. In the **Logging configuration** section, choose **Edit**.
5. Enter the name of the CloudWatch Logs log group you want your capacity provider to send logs to. If you enter the name of an existing log group, your capacity provider uses that group. If no log group exists with the name you enter, Lambda creates a new log group with that name.
6. Choose **Save**.

###### To change a capacity provider's log group (AWS CLI)

- To change the log group of an existing capacity provider, use the [update-capacity-provider](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/update-capacity-provider.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/update-capacity-provider.html") command.

```
`aws lambda update-capacity-provider \
 --capacity-provider-name my-capacity-provider \
 --telemetry-config LoggingConfig={LogGroup=myLogGroup}`
```

###### To specify a custom log group when you create a capacity provider (AWS CLI)

- To specify a custom log group when you create a new capacity provider, use the `--telemetry-config` option in the [create-capacity-provider](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/create-capacity-provider.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/create-capacity-provider.html") command.

```
`aws lambda create-capacity-provider \
 --capacity-provider-name my-capacity-provider \
 --vpc-config SubnetIds=subnet-12345,subnet-67890,SecurityGroupIds=sg-12345 \
 --permissions-config CapacityProviderOperatorRoleArn=arn:aws:iam::123456789012:role/MyOperatorRole \
 --telemetry-config LoggingConfig={LogGroup=myLogGroup}`
```

## Operator role permissions

For your capacity provider to send logs to CloudWatch Logs, the operator role must have the [logs:PutLogEvents](../../../AmazonCloudWatchLogs/latest/APIReference/API_PutLogEvents.md "../../../AmazonCloudWatchLogs/latest/APIReference/API_PutLogEvents.md") permission. Lambda does not add this permission automatically. If the operator role doesn't already have it, add it before you create the capacity provider. This permission is included in the `AWSLambdaManagedEC2ResourceOperator` managed policy.

For more information about the operator role, see [Lambda operator role for Lambda Managed Instances](lambda-managed-instances-operator-role.md "lambda-managed-instances-operator-role.md").
