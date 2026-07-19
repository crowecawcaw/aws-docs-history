# Log-level filtering for capacity provider system logs

Lambda can filter your capacity provider's system logs so that only logs of a certain detail level or lower are sent to CloudWatch Logs. You can choose between the following log levels.

| Log level           | Usage                                                                                 |
| ------------------- | ------------------------------------------------------------------------------------- |
| DEBUG (most detail) | Detailed information for system debugging                                             |
| INFO                | Messages that record the normal operation of the capacity provider                    |
| WARN (least detail) | Messages about potential errors that might lead to unexpected behavior if unaddressed |

When you select a log level, Lambda sends logs at that level and lower. For example, if you set a capacity provider's system log level to INFO, Lambda doesn't send log outputs at the DEBUG level.

By default, Lambda sets the system log level to INFO. To receive more detailed logs, set the level to DEBUG. To receive fewer logs, set the level to WARN. To see a list of the log levels that Lambda maps different system log events to, see [Capacity provider system log event reference](lambda-managed-instances-monitoring-system-log-events.md "lambda-managed-instances-monitoring-system-log-events.md").

## Configuring the system log level

To configure the system log level for your capacity provider, you can use the Lambda console or the AWS Command Line Interface (AWS CLI). You can also configure the system log level using the `CreateCapacityProvider` and `UpdateCapacityProvider` Lambda API commands.

###### To configure the system log level (console)

1. Open the [Capacity providers page](https://console.aws.amazon.com/lambda/home#/capacity-providers "https://console.aws.amazon.com/lambda/home#/capacity-providers") of the Lambda console.
2. Choose a capacity provider.
3. Choose **Additional configuration**.
4. In the **Logging configuration** section, choose **Edit**.
5. Select your desired **System log level** for your capacity provider.
6. Choose **Save**.

###### To set the system log level when creating a capacity provider (AWS CLI)

- To configure the system log level when you create a new capacity provider, use the `--telemetry-config` option in the [create-capacity-provider](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/create-capacity-provider.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/create-capacity-provider.html") command. Set `SystemLogLevel` to one of `DEBUG`, `INFO`, or `WARN`.

```
`aws lambda create-capacity-provider \
 --capacity-provider-name my-capacity-provider \
 --vpc-config SubnetIds=subnet-12345,subnet-67890,SecurityGroupIds=sg-12345 \
 --permissions-config CapacityProviderOperatorRoleArn=arn:aws:iam::123456789012:role/MyOperatorRole \
 --telemetry-config LoggingConfig={SystemLogLevel=DEBUG}`
```

###### To update the system log level of an existing capacity provider (AWS CLI)

- To change the system log level of an existing capacity provider, use the [update-capacity-provider](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/update-capacity-provider.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/lambda/update-capacity-provider.html") command.

```
`aws lambda update-capacity-provider \
 --capacity-provider-name my-capacity-provider \
 --telemetry-config LoggingConfig={SystemLogLevel=WARN}`
```
