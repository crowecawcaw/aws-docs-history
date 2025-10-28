For similar capabilities to Amazon Timestream for LiveAnalytics, consider Amazon Timestream for InfluxDB. It offers simplified
data ingestion and single-digit millisecond query response times for real-time analytics. Learn more [here](timestream-for-influxdb.md "timestream-for-influxdb.md").

# AWS Lambda

You can create Lambda functions that interact with Timestream for LiveAnalytics. For example, you can create a
Lambda function that runs at regular intervals to execute a query on Timestream and send an
SNS notification based on the query results satisfying one or more criteria. To learn more
about Lambda, see the [AWS
Lambda documentation](../../../lambda/latest/dg/welcome.md "../../../lambda/latest/dg/welcome.md").

###### Topics

- [Build AWS Lambda functions using Amazon Timestream for LiveAnalytics with
  Python](#Lambda.w-python "#Lambda.w-python")
- [Build AWS Lambda functions using Amazon Timestream for LiveAnalytics with
  JavaScript](#Lambda.w-js "#Lambda.w-js")
- [Build AWS Lambda functions using Amazon Timestream for LiveAnalytics with Go](#Lambda.w-go "#Lambda.w-go")
- [Build AWS Lambda functions using Amazon Timestream for LiveAnalytics with
  C#](#Lambda.w-c-sharp "#Lambda.w-c-sharp")

## Build AWS Lambda functions using Amazon Timestream for LiveAnalytics with

Python

To build AWS Lambda functions using Amazon Timestream for LiveAnalytics with Python, follow the steps
below.

1. Create an IAM role for Lambda to assume that will grant the required
   permissions to access the Timestream Service, as outlined in [Provide Timestream for LiveAnalytics access](accessing.md#getting-started.prereqs.iam-user "accessing.md#getting-started.prereqs.iam-user").
2. Edit the trust relationship of the IAM role to add Lambda service. You can use
   the commands below to update an existing role so that AWS Lambda can assume
   it:
   1. Create the trust policy document:

   ```
   cat > Lambda-Role-Trust-Policy.json << EOF
   {
     "Version": "2012-10-17",
     "Statement": [
       {
         "Effect": "Allow",
         "Principal": {
           "Service": [
             "lambda.amazonaws.com"
           ]
         },
         "Action": "sts:AssumeRole"
       }
     ]
   }
   EOF
   ```

   2. Update the role from previous step with the trust document

   ```
   aws iam update-assume-role-policy --role-name <name_of_the_role_from_step_1> --policy-document file://Lambda-Role-Trust-Policy.json
   ```

Related references are at [TimestreamWrite](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/timestream-write.html "https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/timestream-write.html") and [TimestreamQuery](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/timestream-query.html "https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/timestream-query.html").

## Build AWS Lambda functions using Amazon Timestream for LiveAnalytics with

JavaScript

To build AWS Lambda functions using Amazon Timestream for LiveAnalytics with JavaScript, follow the instructions
outlined [here](../../../lambda/latest/dg/nodejs-package.md#nodejs-package-dependencies "../../../lambda/latest/dg/nodejs-package.md#nodejs-package-dependencies").

Related references are at [Timestream Write Client - AWS SDK for JavaScript v3](../../../AWSJavaScriptSDK/v3/latest/clients/client-timestream-write/index.md "../../../AWSJavaScriptSDK/v3/latest/clients/client-timestream-write/index.md") and [Timestream Query Client - AWS SDK for JavaScript v3](../../../AWSJavaScriptSDK/v3/latest/clients/client-timestream-query/index.md "../../../AWSJavaScriptSDK/v3/latest/clients/client-timestream-query/index.md").

## Build AWS Lambda functions using Amazon Timestream for LiveAnalytics with Go

To build AWS Lambda functions using Amazon Timestream for LiveAnalytics with Go, follow the instructions outlined
[here](../../../lambda/latest/dg/golang-package.md "../../../lambda/latest/dg/golang-package.md").

Related references are at [timestreamwrite](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/timestreamwrite "https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/timestreamwrite") and [timestreamquery](https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/timestreamquery "https://pkg.go.dev/github.com/aws/aws-sdk-go-v2/service/timestreamquery").

## Build AWS Lambda functions using Amazon Timestream for LiveAnalytics with

C#

To build AWS Lambda functions using Amazon Timestream for LiveAnalytics with C#, follow the instructions outlined
[here](../../../lambda/latest/dg/csharp-package.md "../../../lambda/latest/dg/csharp-package.md").

Related references are at [Amazon.TimestreamWrite](../../../sdkfornet/v3/apidocs/items/TimestreamWrite/NTimestreamWrite.md "../../../sdkfornet/v3/apidocs/items/TimestreamWrite/NTimestreamWrite.md") and [Amazon.TimestreamQuery](../../../sdkfornet/v3/apidocs/items/TimestreamQuery/NTimestreamQuery.md "../../../sdkfornet/v3/apidocs/items/TimestreamQuery/NTimestreamQuery.md").
