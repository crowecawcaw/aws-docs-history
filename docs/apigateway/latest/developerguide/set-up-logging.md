# Set up CloudWatch logging for REST APIs in API Gateway

To help debug issues related to request execution or client access to your API, you can
enable Amazon CloudWatch Logs to log API calls. For more information about CloudWatch, see [Monitor REST API execution with Amazon CloudWatch metrics](monitoring-cloudwatch.md "monitoring-cloudwatch.md").

## CloudWatch log formats for API Gateway

There are two types of API logging in CloudWatch: execution logging and access logging. In
execution logging, API Gateway manages the CloudWatch Logs. The process includes creating log groups and
log streams, and reporting to the log streams any caller's requests and responses.

The logged data includes errors or execution traces (such as request or response parameter values or
payloads), data used by Lambda authorizers (formerly known as custom authorizers), whether API keys are required,
whether usage plans are enabled, and other information. API Gateway redacts authorization headers, API key values, and similar
sensitive request parameters from the logged data.

To improve your security posture, we recommend that you use execution logging at the `ERROR` or
`INFO` level. You might need to do this to comply with various compliance frameworks. For more information, see [Amazon API Gateway controls](../../../securityhub/latest/userguide/apigateway-controls.md "../../../securityhub/latest/userguide/apigateway-controls.md")
in the _AWS Security Hub User Guide_.

When you deploy an API, API Gateway creates a log group and log streams under the log group. The log group is named
following the `API-Gateway-Execution-Logs_{rest-api-id}/{stage_name}` format. Within each log group,
the logs are further divided into log streams, which are ordered by **Last Event Time** as logged
data is reported.

In access logging, you, as an API developer, want to log who has accessed your API and how the caller accessed
the API. You can create your own log group or choose an existing log group that could be managed by API Gateway. To
specify the access details, you select [$context](api-gateway-variables-for-access-logging.md "api-gateway-variables-for-access-logging.md")
variables, a log format, and a log group destination.

The access log
format must include at least `$context.requestId` or `$context.extendedRequestId`. As a best
practice, include `$context.requestId` and `$context.extendedRequestId` in your log format.

**`$context.requestId`**

This logs the value in the `x-amzn-RequestId` header. Clients can override
the value in the `x-amzn-RequestId` header with a value in the format of a universally unique
identifier (UUID). API Gateway returns this request ID in the `x-amzn-RequestId` response header. API Gateway
replaces overridden request IDs that aren't in the format of a UUID with
``UUID`\_REPLACED_INVALID_REQUEST_ID` in your access logs.

**`$context.extendedRequestId`**

The extendedRequestID is a unique ID that API Gateway generates. API Gateway returns this request ID in the
`x-amz-apigw-id` response header. An API caller can't provide or override this request ID. You might need to provide this value to AWS Support to help
troubleshoot your API. For more information, see
[Variables for access logging for API Gateway](api-gateway-variables-for-access-logging.md "api-gateway-variables-for-access-logging.md").

Choose a log format that is also adopted by your analytic backend, such as [Common Log Format](https://httpd.apache.org/docs/current/logs.html#common "https://httpd.apache.org/docs/current/logs.html#common")
(CLF), JSON, XML, or CSV. You can then feed the access logs to it directly to have your
metrics computed and rendered. To define the log format, set the log group ARN on the
[accessLogSettings/destinationArn](../api/API_Stage.md#destinationArn "../api/API_Stage.md#destinationArn") property on the [stage](../api/API_Stage.md "../api/API_Stage.md"). You can obtain a log group ARN in
the CloudWatch console. To define the access log format, set a chosen format on the [accessLogSetting/format](../api/API_Stage.md#format "../api/API_Stage.md#format") property
on the [stage](../api/API_Stage.md "../api/API_Stage.md").

Examples of some commonly used access log formats are shown in the API Gateway console and
are listed as follows.

- `CLF` ([Common Log
  Format](https://httpd.apache.org/docs/current/logs.html#common "https://httpd.apache.org/docs/current/logs.html#common")):

```
$context.identity.sourceIp $context.identity.caller $context.identity.user [$context.requestTime]"$context.httpMethod $context.resourcePath $context.protocol" $context.status $context.responseLength $context.requestId $context.extendedRequestId
```

- `JSON`:

```
{ "requestId":"$context.requestId", "extendedRequestId":"$context.extendedRequestId","ip": "$context.identity.sourceIp", "caller":"$context.identity.caller", "user":"$context.identity.user", "requestTime":"$context.requestTime", "httpMethod":"$context.httpMethod", "resourcePath":"$context.resourcePath", "status":"$context.status", "protocol":"$context.protocol", "responseLength":"$context.responseLength" }
```

- `XML`:

```
<request id="$context.requestId"> <extendedRequestId>$context.extendedRequestId</extendedRequestId> <ip>$context.identity.sourceIp</ip> <caller>$context.identity.caller</caller> <user>$context.identity.user</user> <requestTime>$context.requestTime</requestTime> <httpMethod>$context.httpMethod</httpMethod> <resourcePath>$context.resourcePath</resourcePath> <status>$context.status</status> <protocol>$context.protocol</protocol> <responseLength>$context.responseLength</responseLength> </request>
```

- `CSV` (comma-separated values):

```
$context.identity.sourceIp,$context.identity.caller,$context.identity.user,$context.requestTime,$context.httpMethod,$context.resourcePath,$context.protocol,$context.status,$context.responseLength,$context.requestId,$context.extendedRequestId
```

## Permissions for CloudWatch logging

To enable CloudWatch Logs, you must grant API Gateway permission to read and write logs to CloudWatch for
your account. The [AmazonAPIGatewayPushToCloudWatchLogs](../../../aws-managed-policy/latest/reference/AmazonAPIGatewayPushToCloudWatchLogs.md "../../../aws-managed-policy/latest/reference/AmazonAPIGatewayPushToCloudWatchLogs.md") has all the required permissions.

###### Note

API Gateway calls AWS Security Token Service in order to assume the IAM role, so make sure that AWS STS
is enabled for the Region. For more information, see [Managing AWS
STS in an AWS Region](../../../IAM/latest/UserGuide/id_credentials_temp_enable-regions.md "../../../IAM/latest/UserGuide/id_credentials_temp_enable-regions.md").

To grant these permissions to your account, create an IAM role with
`apigateway.amazonaws.com` as its trusted entity, attach the preceding
policy to the IAM role, and set the IAM role ARN on the [cloudWatchRoleArn](../api/API_UpdateAccount.md#cloudWatchRoleArn "../api/API_UpdateAccount.md#cloudWatchRoleArn")
property on your [Account](../api/API_GetAccount.md "../api/API_GetAccount.md"). You must
set the [cloudWatchRoleArn](../api/API_UpdateAccount.md#cloudWatchRoleArn "../api/API_UpdateAccount.md#cloudWatchRoleArn") property separately for each AWS Region in which you
want to enable CloudWatch Logs.

If you receive an error when setting the IAM role ARN, check your AWS Security Token Service account
settings to make sure that AWS STS is enabled in the Region that you're using. For more
information about enabling AWS STS, see [Managing AWS STS in an AWS Region](../../../IAM/latest/UserGuide/id_credentials_temp_enable-regions.md#sts-regions-activate-deactivate "../../../IAM/latest/UserGuide/id_credentials_temp_enable-regions.md#sts-regions-activate-deactivate") in the
_IAM User Guide_.

## Set up CloudWatch API logging using the

API Gateway console

To set up CloudWatch API logging, you must have deployed the API to a stage. You must also have
configured [an appropriate CloudWatch Logs
role](#set-up-access-logging-permissions "#set-up-access-logging-permissions") ARN for your account.

1. Sign in to the API Gateway console at [https://console.aws.amazon.com/apigateway](https://console.aws.amazon.com/apigateway "https://console.aws.amazon.com/apigateway").
2. On the main navigation pane, choose **Settings**, and then under
   **Logging**, choose **Edit**.
3. For **CloudWatch log role ARN**, enter an ARN of an IAM role with appropriate
   permissions. You need to do this once for each AWS account that creates APIs using API Gateway.
4. In the main navigation pane, choose **APIs**, and then do one of the following:
   1. Choose an existing API, and then choose a stage.
   2. Create an API, and then deploy it to a stage.

5. In the main navigation pane, choose **Stages**.
6. In the **Logs and tracing** section, choose
   **Edit**.
7. To enable execution logging:
   1. Select a logging level from the **CloudWatch Logs** dropdown menu. The logging levels are the following:
      - Off – Logging is not turned on for this stage.
      - Errors only – Logging is enabled for errors only.
      - Errors and info logs – Logging is enabled for all events.

   2. (Optional) Select **Data tracing** to turn on data trace logging for your stage.
      This can be useful to troubleshoot APIs, but can result in logging sensitive data.

   ###### Note

   We recommend that
   you don't use **Data tracing** for production APIs. 3. (Optional) Select **Detailed
   metrics** to turn on detailed CloudWatch metrics.For more information about CloudWatch metrics, see [Monitor REST API execution with Amazon CloudWatch metrics](monitoring-cloudwatch.md "monitoring-cloudwatch.md").

8. To enable access logging:
   1. Turn on
      **Custom access logging**.
   2. For **Access log destination ARN**, enter the ARN of a log group. The ARN format is
      `arn:aws:logs:`{region}`:`{account-id}`:log-group:`log-group-name``.
   3. For **Log Format**, enter a log format. You can choose
      **CLF**, **JSON**, **XML**, or
      **CSV**. To learn more about example log formats, see [CloudWatch log formats for API Gateway](#apigateway-cloudwatch-log-formats "#apigateway-cloudwatch-log-formats").

9. Choose **Save changes**.

###### Note

You can enable execution logging and access logging independently of each
other.

API Gateway is now ready to log requests to your API. You don't need to redeploy the API
when you update the stage settings, logs, or stage variables.

## Set up CloudWatch API logging using CloudFormation

Use the following example CloudFormation template to create an Amazon CloudWatch Logs log group and configure execution and access
logging for a stage. To enable CloudWatch Logs, you must grant API Gateway permission to read and write logs to CloudWatch for your
account. To learn more, see [Associate account with IAM role](../../../AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-account.md#aws-resource-apigateway-account--examples "../../../AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-account.md#aws-resource-apigateway-account--examples") in the _AWS CloudFormation User Guide_.

```
  TestStage:
    Type: AWS::ApiGateway::Stage
    Properties:
      StageName: test
      RestApiId: !Ref MyAPI
      DeploymentId: !Ref Deployment
      Description: "test stage description"
      MethodSettings:
        - ResourcePath: "/*"
          HttpMethod: "*"
          LoggingLevel: INFO
      AccessLogSetting:
        DestinationArn: !GetAtt MyLogGroup.Arn
        Format: $context.extendedRequestId $context.identity.sourceIp $context.identity.caller $context.identity.user [$context.requestTime] "$context.httpMethod $context.resourcePath $context.protocol" $context.status $context.responseLength $context.requestId
  MyLogGroup:
    Type: AWS::Logs::LogGroup
    Properties:
      LogGroupName: !Join
        - '-'
        - - !Ref MyAPI
          - access-logs

```
