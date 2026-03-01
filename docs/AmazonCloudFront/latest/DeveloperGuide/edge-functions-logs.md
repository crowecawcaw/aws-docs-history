# Edge function logs

You can use Amazon CloudWatch Logs to get logs for your edge functions, both [Lambda@Edge](lambda-at-the-edge.md "lambda-at-the-edge.md") and [CloudFront Functions](cloudfront-functions.md "cloudfront-functions.md"). You can access the logs by using the CloudWatch console or the CloudWatch Logs
API.

###### Important

We recommend that you use the logs to understand the nature of the requests for your
content, not as a complete accounting of all requests. CloudFront delivers edge function logs
on a best-effort basis. The log entry for a particular request might be delivered long
after the request was actually processed and, in rare cases, a log entry might not be
delivered at all. When a log entry is omitted from edge function logs, the number of
entries in the edge function logs won't match the usage that appears in the AWS
billing and usage reports.

###### Topics

- [Lambda@Edge logs](#lambda-at-edge-logs "#lambda-at-edge-logs")
- [CloudFront Functions logs](#cloudfront-function-logs "#cloudfront-function-logs")

## Lambda@Edge logs

Lambda@Edge automatically sends function logs to CloudWatch Logs, creating log streams in the
AWS Regions where the functions are invoked. When you create or modify a function in
AWS Lambda, you can either use the default CloudWatch log group name or customize it.

- The default log group name is
  `/aws/lambda/`<FunctionName>`where`<FunctionName>`` is the name that
you specified when you created the function. When sending logs to CloudWatch,
Lambda@Edge will automatically add the `us-east-1` prefix to the
function name, so that the log group name is
`/aws/lambda/us-east-1.`<FunctionName>``.
  This prefix corresponds to the AWS Region where the function was created. This
  prefix remains part of the log group name, even in other Regions where the
  function is invoked.
- If you specify a custom log group name, such as
  `/`MyLogGroup``, Lambda@Edge won't
  add the Region prefix. The log group name remains the same across all other
  Regions where the function is invoked.

###### Note

If you create a custom log group and specify the same name as the default
`/aws/lambda/`<FunctionName>``,
 Lambda@Edge adds the `us-east-1` prefix to the function name.

In addition to customizing the log group name, Lambda@Edge functions support JSON and
plain text log formats, and log-level filtering. For more information , see [Configuring advance logging controls for Lambda function](../../../lambda/latest/dg/monitoring-cloudwatchlogs-advanced.md "../../../lambda/latest/dg/monitoring-cloudwatchlogs-advanced.md") in the
_AWS Lambda Developer Guide_.

###### Note

Lambda@Edge throttles logs based on the request volume and the size of logs.

You must review CloudWatch log files in the correct Region to see your Lambda@Edge function
log files. To see the Regions where your Lambda@Edge function is running, view graphs of
metrics for the function in the CloudFront console. Metrics are displayed for each Region. On
the same page, you can choose a Region and then view log files for that Region to
investigate issues.

To learn more about how to use CloudWatch Logs with Lambda@Edge functions, see the following
topics:

- For more information about viewing graphs in the
  **Monitoring** section of the CloudFront console, see [Monitor CloudFront metrics with Amazon CloudWatch](monitoring-using-cloudwatch.md "monitoring-using-cloudwatch.md").
- For information about the permissions required to send data to CloudWatch Logs, see
  [Set up IAM permissions and roles for Lambda@Edge](lambda-edge-permissions.md "lambda-edge-permissions.md").
- For information about adding logging to a Lambda@Edge function, see [AWS Lambda
  function logging in Node.js](../../../lambda/latest/dg/nodejs-logging.md "../../../lambda/latest/dg/nodejs-logging.md") or [AWS Lambda
  function logging in Python](../../../lambda/latest/dg/python-logging.md "../../../lambda/latest/dg/python-logging.md") in the
  _AWS Lambda Developer Guide_.
- For information about CloudWatch Logs quotas (formerly known as limits), see [CloudWatch Logs quotas](../../../AmazonCloudWatch/latest/logs/cloudwatch_limits_cwl.md "../../../AmazonCloudWatch/latest/logs/cloudwatch_limits_cwl.md") in the
  _Amazon CloudWatch Logs User Guide_.

## CloudFront Functions logs

If a CloudFront function's code contains `console.log()` statements,
CloudFront Functions automatically sends these log lines to CloudWatch Logs. If there are no
`console.log()` statements, nothing is sent to CloudWatch Logs.

CloudFront Functions always creates log streams in the US East (N. Virginia) Region
(`us-east-1`), no matter which edge location ran the function.
The log stream
name is in the format
`YYYY/M/D/`UUID``.

The log group name uses the following format:

- For CloudFront Functions at the cache behavior level, the format is
  `/aws/cloudfront/function/`<FunctionName>``
- For CloudFront Functions at the distribution level (Connection Functions), the
  format is
  `/aws/cloudfront/connection-function/`<FunctionName>``

The
`<FunctionName>`
is the name that you gave to the function when you created it.
.

###### Example Viewer requests

The following shows an example log message sent to CloudWatch Logs. Each line begins with an
ID that uniquely identifies a CloudFront request. The message begins with a
`START` line that includes the CloudFront distribution ID, and ends with an
`END` line. Between the `START` and `END` lines
are the log lines generated by `console.log()` statements in the
function.

```
U7b4hR_RaxMADupvKAvr8_m9gsGXvioUggLV5Oyq-vmAtH8HADpjhw== START DistributionID: E3E5D42GADAXZZ
U7b4hR_RaxMADupvKAvr8_m9gsGXvioUggLV5Oyq-vmAtH8HADpjhw== Example function log output
U7b4hR_RaxMADupvKAvr8_m9gsGXvioUggLV5Oyq-vmAtH8HADpjhw== END
```

###### Example Connection requests

The following shows an example log message sent to CloudWatch Logs. Each line begins with an
ID that uniquely identifies a CloudFront request. The message begins with a
`START` line that includes the CloudFront distribution ID, and ends with an
`END` line. Between the `START` and `END` lines
are the log lines generated by `console.log()` statements in the
function.

```
U7b4hR_RaxMADupvKAvr8_m9gsGXvioUggLV5Oyq-vmAtH8HADpjhw== START DistributionID: E3E5D42GADA123
U7b4hR_RaxMADupvKAvr8_m9gsGXvioUggLV5Oyq-vmAtH8HADpjhw== 1.2.3.4
U7b4hR_RaxMADupvKAvr8_m9gsGXvioUggLV5Oyq-vmAtH8HADpjhw== END
```

###### Note

CloudFront Functions sends logs to CloudWatch only for functions in the `LIVE`
stage that run in response to production requests and responses. When you [test a function](test-function.md "test-function.md"), CloudFront doesn't send any logs to
CloudWatch. The test output contains information about errors, compute utilization, and
function logs (`console.log()` statements), but this information isn't
sent to CloudWatch.

CloudFront Functions uses an AWS Identity and Access Management (IAM) [service-linked role](../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-linked-role "../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-linked-role") to send logs to CloudWatch Logs in your
account. A service-linked role is an IAM role that is linked directly to an
AWS service. Service-linked roles are predefined by the service and include all of the
permissions that the service requires to call other AWS services for you.
CloudFront Functions uses the **AWSServiceRoleForCloudFrontLogger** service-linked role. For more
information about this role, see [Service-linked roles for Lambda@Edge](lambda-edge-permissions.md#using-service-linked-roles-lambda-edge "lambda-edge-permissions.md#using-service-linked-roles-lambda-edge") (Lambda@Edge uses the same service-linked role).

When a function fails with a validation error or an execution error, the information
is logged in [standard logs](AccessLogs.md "AccessLogs.md") and [real-time access logs](real-time-logs.md "real-time-logs.md"). For specific information about the
error, see the `x-edge-result-type`,
`x-edge-response-result-type`, and `x-edge-detailed-result-type`
fields.
