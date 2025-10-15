# Debugging and troubleshooting S3 Object Lambda

###### Note

Amazon S3 Object Lambda will no longer be open to new customers starting on November 7th, 2025. If you would like to use the service, please sign up prior to November 7th, 2025. For capabilities similar to S3 Object Lambda, learn more here - [Amazon S3 Object Lambda availability change](amazons3-ol-change.md "amazons3-ol-change.md").

Requests to Amazon S3 Object Lambda access points might result in a new error response when something goes
 wrong with the Lambda function invocation or execution. These errors follow the same format
 as standard Amazon S3 errors. For information about S3 Object Lambda errors, see [S3 Object Lambda Error
 Code List](../API/ErrorResponses.md#S3ObjectLambdaErrorCodeList "../API/ErrorResponses.md#S3ObjectLambdaErrorCodeList") in the *Amazon Simple Storage Service API Reference*.

For more information about general Lambda function debugging, see [Monitoring and troubleshooting Lambda
 applications](https://docs.aws.amazon.com/lambda/latest/dg/lambda-monitoring.html  "https://docs.aws.amazon.com/lambda/latest/dg/lambda-monitoring.html ") in the *AWS Lambda Developer Guide*.

For information about standard Amazon S3 errors, see [Error Responses](../API/ErrorResponses.md "../API/ErrorResponses.md") in the
 *Amazon Simple Storage Service API Reference*.

You can enable request metrics in Amazon CloudWatch for your Object Lambda Access Points. These metrics help you
 monitor the operational performance of your access point. You can enable request metrics during or
 after creation of your Object Lambda Access Point. For more information, see [S3 Object Lambda request metrics in
 CloudWatch](metrics-dimensions.md#olap-cloudwatch-metrics "metrics-dimensions.md#olap-cloudwatch-metrics").

To get more granular logging about requests made to your Object Lambda Access Points, you can enable
 AWS CloudTrail data events. For more information, see [Logging data events for
 trails](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.html "https://docs.aws.amazon.com/awscloudtrail/latest/userguide/logging-data-events-with-cloudtrail.html") in the *AWS CloudTrail User Guide*.
