

# Scanning AWS Lambda functions with Amazon Inspector
<a name="scanning-lambda"></a>

 Amazon Inspector support for AWS Lambda functions and layers provides continuous automated security vulnerability assessments. Amazon Inspector offers two types of Lambda function scanning: 

**[Amazon Inspector Lambda standard scanning](https://docs.aws.amazon.com/inspector/latest/user/scanning_resources_lambda_exclude_functions.html)**  
 This scan type is the default Lambda scan type. It scans application dependencies in Lambda functions and layers for [package vulnerabilities](findings-types.md#findings-types-package). 

**[Amazon Inspector Lambda code scanning](https://docs.aws.amazon.com/inspector/latest/user/scanning_resources_lambda_code.html)**  
 This scan type scans custom application code in your Lambda functions and layers for [code vulnerabilities](findings-types.md#findings-types-code). You can activate Lambda standard scanning or Lambda standard scanning with Lambda code scanning. 

 If you want to activate Lambda code scanning, you must activate Lambda standard scanning first. For more information, see [Activating a scan type](https://docs.aws.amazon.com/inspector/latest/user/activate-scans.html). 

 When you activate Lambda function scanning, Amazon Inspector creates the following service-linked channels in your account: `cloudtrail:CreateServiceLinkedChannel` and `cloudtrail:DeleteServiceLinkedChannel`. Amazon Inspector manages these channels and uses them to monitor CloudTrail events for scans. The channels allow you to view CloudTrail events in your account as if you had a trail in CloudTrail. We recommend creating your own trail in CloudTrail to manage events in your account. For information about how to view these channels, see [Viewing service-linked channels](https://docs.aws.amazon.com/awscloudtrail/latest/userguide/cloudtrail-service-linked-channels.html) in the *AWS CloudTrail User Guide*. 

**Note**  
 Amazon Inspector does not support scanning [Lambda functions encrypted with customer managed keys](https://docs.aws.amazon.com/lambda/latest/dg/security-encryption-at-rest.html). This applies to Lambda standard scanning and Lambda code scanning. 

## Scan behaviors for Lambda function scanning
<a name="lambda-scan-behavior"></a>

Upon activation, Amazon Inspector scans all Lambda functions invoked or updated in the last 90 days in your account. Amazon Inspector initiates vulnerability scans of Lambda functions in the following situations:
+ As soon as Amazon Inspector discovers an existing Lambda function.
+ When you deploy a new Lambda function to the Lambda service.
+ When you deploy an update to the application code or dependencies of an existing Lambda function or its layers.
+ Whenever Amazon Inspector adds a new common vulnerabilities and exposures (CVE) item to its database, and that CVE is relevant to your function.

Amazon Inspector monitors each Lambda function throughout its lifetime until it's either deleted or excluded from scanning.

You can check when a Lambda function was last checked for vulnerabilities from the **Lambda functions** tab on the **Account management** page or by using the [ListCoverage](https://docs.aws.amazon.com/inspector/v2/APIReference/API_ListCoverage.html) API. Amazon Inspector updates the **Last scanned at** field for a Lambda function in response to the following events:
+ When Amazon Inspector completes an initial scan of a Lambda function.
+ When a Lambda function is updated.
+ When Amazon Inspector re-scans a Lambda function because a new CVE item impacting that function was added to the Amazon Inspector database.

## Supported runtimes and eligible functions
<a name="supported-functions"></a>

Amazon Inspector supports different runtimes for Lambda standard scanning and Lambda code scanning. For a list of supported runtimes for each scan type, see [Supported runtimes: Amazon Inspector Lambda standard scanning](supported.md#supported-programming-languages-lambda-standard) and [Supported runtimes: Amazon Inspector Lambda code scanning](supported.md#supported-programming-languages-lambda-code).

In addition to having a supported runtime, a Lambda function needs to meet the following criteria to be eligible for Amazon Inspector scans:
+ The function has been invoked or updated in the last 90 days.
+ The function is marked `$LATEST`.
+ The function isn't excluded from scans by tags.

**Note**  
Lambda functions that haven't been invoked or modified in the last 90 days are automatically excluded from scans. Amazon Inspector will resume scanning an automatically excluded function if it is invoked again or if changes are made to the Lambda function code.