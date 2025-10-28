# Configure logging for HTTP APIs in API Gateway

You can turn on logging to write logs to CloudWatch Logs. You can use [logging variables](http-api-logging-variables.md "http-api-logging-variables.md") to customize the
content of your logs.

To improve your security posture, we recommend that you write logs to CloudWatch Logs for all stages of your HTTP API.
You might need to do this to comply with various compliance frameworks. For more information, see [Amazon API Gateway controls](../../../securityhub/latest/userguide/apigateway-controls.md "../../../securityhub/latest/userguide/apigateway-controls.md") in
the _AWS Security Hub User Guide_.

To turn on logging for an HTTP API, you must do the following.

1. Ensure that your user has the required permissions to activate logging.
2. Create a CloudWatch Logs log group.
3. Provide the ARN of the CloudWatch Logs log group for a stage of your API.

## Permissions to activate logging

To turn on logging for an API, your user must have the following permissions.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "logs:DescribeLogGroups",
 "logs:DescribeLogStreams",
 "logs:GetLogEvents",
 "logs:FilterLogEvents"
 ],
 "Resource": "arn:aws:logs:`us-east-2`:`123456789012`:log-group:*"
 },
 {
 "Effect": "Allow",
 "Action": [
 "logs:CreateLogDelivery",
 "logs:PutResourcePolicy",
 "logs:UpdateLogDelivery",
 "logs:DeleteLogDelivery",
 "logs:CreateLogGroup",
 "logs:DescribeResourcePolicies",
 "logs:GetLogDelivery",
 "logs:ListLogDeliveries"
 ],
 "Resource": "*"
 }
 ]
}`

```

## Create a log group and activate logging for HTTP APIs

You can create a log group and activate access logging using the AWS Management Console or the AWS CLI.

AWS Management Console

1. Create a log group.

To learn how to create a log group using the console, see [Create a Log Group in Amazon CloudWatch Logs User Guide](../../../AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.md "../../../AmazonCloudWatch/latest/logs/Working-with-log-groups-and-streams.md"). 2. Sign in to the API Gateway console at [https://console.aws.amazon.com/apigateway](https://console.aws.amazon.com/apigateway "https://console.aws.amazon.com/apigateway"). 3. Choose an HTTP API. 4. Under the **Monitor** tab in the primary navigation panel, choose **Logging**. 5. Select a stage to activate logging and choose **Select**. 6. Choose **Edit** to activate access logging. 7. Turn on **Access logging**, enter a CloudWatch Logs, and select a log format. 8. Choose **Save**.

AWS CLI
The following [create-log-group](../../../cli/latest/reference/logs/create-log-group.md "../../../cli/latest/reference/logs/create-log-group.md") command creates a log group:

```
aws logs create-log-group --log-group-name `my-log-group`
```

You need the Amazon Resource Name (ARN) for your log group to turn on logging. The ARN format is
arn:aws:logs:`region`:`account-id`:log-group:`log-group-name`.

The following [update-stage](../../../cli/latest/reference/apigatewayv2/update-stage.md "../../../cli/latest/reference/apigatewayv2/update-stage.md") command turns on logging for the `$default` stage of an HTTP API:

```
aws apigatewayv2 update-stage --api-id `abcdef` \
    --stage-name '`$default`' \
    --access-log-settings '{"DestinationArn": "arn:aws:logs:`region`:`account-id`:log-group:`log-group-name`", "Format": "$context.identity.sourceIp - - [$context.requestTime] \"$context.httpMethod $context.routeKey $context.protocol\" $context.status $context.responseLength $context.requestId"}'
```

## Example log formats

Examples of some common access log formats are available in the API Gateway console and are
listed as follows.

- `CLF` ([Common Log
  Format](https://httpd.apache.org/docs/current/logs.html#common "https://httpd.apache.org/docs/current/logs.html#common")):

```
$context.identity.sourceIp - - [$context.requestTime] "$context.httpMethod $context.routeKey $context.protocol" $context.status $context.responseLength $context.requestId $context.extendedRequestId
```

- `JSON`:

```
{ "requestId":"$context.requestId", "ip": "$context.identity.sourceIp", "requestTime":"$context.requestTime", "httpMethod":"$context.httpMethod","routeKey":"$context.routeKey", "status":"$context.status","protocol":"$context.protocol", "responseLength":"$context.responseLength", "extendedRequestId": "$context.extendedRequestId" }
```

- `XML`:

```
<request id="$context.requestId"> <ip>$context.identity.sourceIp</ip> <requestTime>$context.requestTime</requestTime> <httpMethod>$context.httpMethod</httpMethod> <routeKey>$context.routeKey</routeKey> <status>$context.status</status> <protocol>$context.protocol</protocol> <responseLength>$context.responseLength</responseLength> <extendedRequestId>$context.extendedRequestId</extendedRequestId> </request>
```

- `CSV` (comma-separated values):

```
$context.identity.sourceIp,$context.requestTime,$context.httpMethod,$context.routeKey,$context.protocol,$context.status,$context.responseLength,$context.requestId,$context.extendedRequestId
```
