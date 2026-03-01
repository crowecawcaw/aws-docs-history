# Debugging and troubleshooting S3 Object Lambda

###### Note

As of November 7th, 2025, S3 Object Lambda is available only to existing customers that are currently using the service as well as to select AWS Partner Network (APN) partners. For capabilities similar to S3 Object Lambda, learn more here - [Amazon S3 Object Lambda availability change](amazons3-ol-change.md "amazons3-ol-change.md").

Requests to Amazon S3 Object Lambda access points might result in a new error response when something goes
wrong with the Lambda function invocation or execution. These errors follow the same format
as standard Amazon S3 errors. For information about S3 Object Lambda errors, see [S3 Object Lambda Error
Code List](../API/ErrorResponses.md#S3ObjectLambdaErrorCodeList "../API/ErrorResponses.md#S3ObjectLambdaErrorCodeList") in the _Amazon Simple Storage Service API Reference_.

For more information about general Lambda function debugging, see [Monitoring and troubleshooting Lambda
applications](../../../lambda/latest/dg/lambda-monitoring.md "../../../lambda/latest/dg/lambda-monitoring.md") in the _AWS Lambda Developer Guide_.

For information about standard Amazon S3 errors, see [Error Responses](../API/ErrorResponses.md "../API/ErrorResponses.md") in the
_Amazon Simple Storage Service API Reference_.

You can enable request metrics in Amazon CloudWatch for your Object Lambda Access Points. These metrics help you
monitor the operational performance of your access point. You can enable request metrics during or
after creation of your Object Lambda Access Point. For more information, see [S3 Object Lambda request metrics in CloudWatch](metrics-dimensions.md#olap-cloudwatch-metrics "metrics-dimensions.md#olap-cloudwatch-metrics").

To get more granular logging about requests made to your Object Lambda Access Points, you can enable
AWS CloudTrail data events. For more information, see [Logging data events for
trails](../../../awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.md "../../../awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.md") in the _AWS CloudTrail User Guide_.
