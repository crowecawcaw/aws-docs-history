# Identify Amazon ECS optimization opportunities using application trace data

Amazon ECS integrates with AWS Distro for OpenTelemetry to collect trace data from your
application. Amazon ECS uses an AWS Distro for OpenTelemetry sidecar container to collect and
route trace data to AWS X-Ray. For more information, see [Setting up AWS Distro for
OpenTelemetry Collector in Amazon ECS](https://aws-otel.github.io/docs/setup/ecs "https://aws-otel.github.io/docs/setup/ecs"). You can then use AWS X-Ray to identify errors
and exceptions, analyze performance bottlenecks and response times.

For the AWS Distro for OpenTelemetry Collector to send trace data to AWS X-Ray, your
application must be configured to create the trace data. For more information, see [Instrumenting your application for AWS X-Ray](../../../xray/latest/devguide/xray-instrumenting-your-app.md "../../../xray/latest/devguide/xray-instrumenting-your-app.md") in the _AWS X-Ray
Developer Guide_.

## Required IAM permissions for AWS Distro for

OpenTelemetry integration with AWS X-Ray

The Amazon ECS integration with AWS Distro for OpenTelemetry requires that you create a
task role and specify the role in your task definition. We recommend that you configure
the AWS Distro for OpenTelemetry sidecar to route container logs to CloudWatch Logs.

###### Important

If you also collect application metrics using the AWS Distro for OpenTelemetry
integration, ensure your task IAM role also contains the permissions necessary for
that integration. For more information, see [Correlate Amazon ECS application performance using application
metrics](metrics-data.md "metrics-data.md").

After you create the role, create a policy with the following permissions, and then attach it to the role.

- `logs:PutLogEvents`
- `logs:CreateLogGroup`
- `logs:CreateLogStream`
- `logs:DescribeLogStreams`
- `logs:DescribeLogGroups`
- `logs:PutRetentionPolicy`
- `xray:PutTraceSegments`
- `xray:PutTelemetryRecords`
- `xray:GetSamplingRules`
- `xray:GetSamplingTargets`
- `xray:GetSamplingStatisticSummaries`
- `ssm:GetParameters`
