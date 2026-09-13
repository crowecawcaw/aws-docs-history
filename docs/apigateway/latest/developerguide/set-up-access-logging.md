

# Access logging for REST APIs
<a name="set-up-access-logging"></a>

In access logging, you log who has accessed your API and how the caller accessed the API. You can create your own log group or choose an existing log group. To specify the access details, you select [`$context`](api-gateway-variables-for-access-logging.md) variables, a log format, and a log group destination.

## Access log formats
<a name="apigateway-cloudwatch-log-formats"></a>

The access log format must include at least `$context.requestId` or `$context.extendedRequestId`. As a best practice, include both in your log format.

**`$context.requestId`**  
This logs the value in the `x-amzn-RequestId` header. Clients can override the value in the `x-amzn-RequestId` header with a value in the format of a universally unique identifier (UUID). API Gateway returns this request ID in the `x-amzn-RequestId` response header. API Gateway replaces overridden request IDs that aren't in the format of a UUID with `{{UUID}}_REPLACED_INVALID_REQUEST_ID` in your access logs.

**`$context.extendedRequestId`**  
The extendedRequestID is a unique ID that API Gateway generates. API Gateway returns this request ID in the `x-amz-apigw-id` response header. An API caller can't provide or override this request ID. You might need to provide this value to AWS Support to help troubleshoot your API. For more information, see [Variables for access logging for API Gateway](api-gateway-variables-for-access-logging.md).

Choose a log format that is also adopted by your analytic backend, such as [Common Log Format](https://httpd.apache.org/docs/current/logs.html#common) (CLF), JSON, XML, or CSV. You can then feed the access logs to it directly to have your metrics computed and rendered. To define the log format, set the log group ARN on the [accessLogSettings/destinationArn](https://docs.aws.amazon.com/apigateway/latest/api/API_Stage.html#destinationArn) property on the [stage](https://docs.aws.amazon.com/apigateway/latest/api/API_Stage.html). You can obtain a log group ARN in the CloudWatch console. To define the access log format, set a chosen format on the [accessLogSetting/format](https://docs.aws.amazon.com/apigateway/latest/api/API_Stage.html#format) property on the [stage](https://docs.aws.amazon.com/apigateway/latest/api/API_Stage.html).

Examples of some commonly used access log formats are shown in the API Gateway console and are listed as follows.
+ `CLF` ([Common Log Format](https://httpd.apache.org/docs/current/logs.html#common)):

  ```
  $context.identity.sourceIp $context.identity.caller $context.identity.user [$context.requestTime]"$context.httpMethod $context.resourcePath $context.protocol" $context.status $context.responseLength $context.requestId $context.extendedRequestId
  ```
+ `JSON`:

  ```
  { "requestId":"$context.requestId", "extendedRequestId":"$context.extendedRequestId","ip": "$context.identity.sourceIp", "caller":"$context.identity.caller", "user":"$context.identity.user", "requestTime":"$context.requestTime", "httpMethod":"$context.httpMethod", "resourcePath":"$context.resourcePath", "status":"$context.status", "protocol":"$context.protocol", "responseLength":"$context.responseLength" }
  ```
+ `XML`:

  ```
  <request id="$context.requestId"> <extendedRequestId>$context.extendedRequestId</extendedRequestId> <ip>$context.identity.sourceIp</ip> <caller>$context.identity.caller</caller> <user>$context.identity.user</user> <requestTime>$context.requestTime</requestTime> <httpMethod>$context.httpMethod</httpMethod> <resourcePath>$context.resourcePath</resourcePath> <status>$context.status</status> <protocol>$context.protocol</protocol> <responseLength>$context.responseLength</responseLength> </request>
  ```
+ `CSV` (comma-separated values):

  ```
  $context.identity.sourceIp,$context.identity.caller,$context.identity.user,$context.requestTime,$context.httpMethod,$context.resourcePath,$context.protocol,$context.status,$context.responseLength,$context.requestId,$context.extendedRequestId
  ```

## Set up access logging using the API Gateway console
<a name="set-up-access-logging-using-console"></a>

Before you set up access logging, deploy the API to a stage and configure [an appropriate CloudWatch Logs role](set-up-logging.md#set-up-access-logging-permissions) ARN for your account.

1. Sign in to the API Gateway console at [https://console.aws.amazon.com/apigateway](https://console.aws.amazon.com/apigateway).

1. In the main navigation pane, choose **APIs**, and then do one of the following:

   1. Choose an existing API, and then choose a stage.

   1. Create an API, and then deploy it to a stage.

1. In the main navigation pane, choose **Stages**.

1. In the **Logs and tracing** section, choose **Edit**.

1. Turn on **Custom access logging**.

1. For **Access log destination ARN**, enter the ARN of a log group. The ARN format is `arn:aws:logs:{{{region}}}:{{{account-id}}}:log-group:{{log-group-name}}`.

1. For **Log Format**, enter a log format. You can choose **CLF**, **JSON**, **XML**, or **CSV**. To learn more about example log formats, see [Access log formats](#apigateway-cloudwatch-log-formats).

1. Choose **Save changes**.

API Gateway is now ready to log requests to your API. You don't need to redeploy the API when you update the stage settings, logs, or stage variables.

## Set up access logging using CloudFormation
<a name="set-up-access-logging-using-cloudformation"></a>

Use the following example CloudFormation template to create a Amazon CloudWatch Logs log group and configure access logging for a stage. To enable CloudWatch Logs, you must grant API Gateway permission to read and write logs to CloudWatch for your account. To learn more, see [Associate account with IAM role](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-apigateway-account.html#aws-resource-apigateway-account--examples) in the *AWS CloudFormation User Guide*.

```
  TestStage:
    Type: AWS::ApiGateway::Stage
    Properties:
      StageName: test
      RestApiId: !Ref MyAPI
      DeploymentId: !Ref Deployment
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