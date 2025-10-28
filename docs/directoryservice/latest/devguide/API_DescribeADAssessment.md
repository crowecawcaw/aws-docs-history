# DescribeADAssessment

Retrieves detailed information about a directory assessment, including its current
status, validation results, and configuration details. Use this operation to monitor
assessment progress and review results.

## Request Syntax

```
{
   "AssessmentId": "`string`"
}
```

## Request Parameters

The request accepts the following data in JSON format.

**[AssessmentId](#API_DescribeADAssessment_RequestSyntax "#API_DescribeADAssessment_RequestSyntax")**

The identifier of the directory assessment to describe.

Type: String

Pattern: `^da-[0-9a-f]{18}$`

Required: Yes

## Response Syntax

```
{
   "Assessment": {
      "AssessmentId": "***string***",
      "CustomerDnsIps": [ "***string***" ],
      "DirectoryId": "***string***",
      "DnsName": "***string***",
      "LastUpdateDateTime": ***number***,
      "ReportType": "***string***",
      "SecurityGroupIds": [ "***string***" ],
      "SelfManagedInstanceIds": [ "***string***" ],
      "StartTime": ***number***,
      "Status": "***string***",
      "StatusCode": "***string***",
      "StatusReason": "***string***",
      "SubnetIds": [ "***string***" ],
      "Version": "***string***",
      "VpcId": "***string***"
   },
   "AssessmentReports": [
      {
         "DomainControllerIp": "***string***",
         "Validations": [
            {
               "Category": "***string***",
               "LastUpdateDateTime": ***number***,
               "Name": "***string***",
               "StartTime": ***number***,
               "Status": "***string***",
               "StatusCode": "***string***",
               "StatusReason": "***string***"
            }
         ]
      }
   ]
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[Assessment](#API_DescribeADAssessment_ResponseSyntax "#API_DescribeADAssessment_ResponseSyntax")**

Detailed information about the self-managed instance settings (IDs and DNS
IPs).

Type: [Assessment](API_Assessment.md "API_Assessment.md") object

**[AssessmentReports](#API_DescribeADAssessment_ResponseSyntax "#API_DescribeADAssessment_ResponseSyntax")**

A list of assessment reports containing validation results for each domain controller
and test category. Each report includes specific validation details and outcomes.

Type: Array of [AssessmentReport](API_AssessmentReport.md "API_AssessmentReport.md") objects

## Errors

For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").

**ClientException**

A client exception has occurred.

**Message**

The descriptive message for the exception.

**RequestId**

The AWS request identifier.

HTTP Status Code: 400

**EntityDoesNotExistException**

The specified entity could not be found.

**Message**

The descriptive message for the exception.

**RequestId**

The AWS request identifier.

HTTP Status Code: 400

**InvalidParameterException**

One or more parameters are not valid.

**Message**

The descriptive message for the exception.

**RequestId**

The AWS request identifier.

HTTP Status Code: 400

**ServiceException**

An exception has occurred in AWS Directory Service.

**Message**

The descriptive message for the exception.

**RequestId**

The AWS request identifier.

HTTP Status Code: 500

**UnsupportedOperationException**

The operation is not supported.

**Message**

The descriptive message for the exception.

**RequestId**

The AWS request identifier.

HTTP Status Code: 400

## Examples

The following examples are formatted for legibility.

### Example Request

This example illustrates one usage of DescribeADAssessment.

```
POST / HTTP/1.1
Host: ds.us-west-2.amazonaws.com
Accept-Encoding: identity
Content-Length: 45
X-Amz-Target: DirectoryService_20150416.DescribeADAssessment
X-Amz-Date: 20231212T212029Z
User-Agent: aws-cli/2.0.0 Python/3.8.0 Linux/5.4.0 botocore/2.0.0
Content-Type: application/x-amz-json-1.1
Authorization: AWS4-HMAC-SHA256
 Credential=AKIAIOSFODNN7EXAMPLE/20231212/us-west-2/ds/aws4_request,
 SignedHeaders=content-type;host;x-amz-date;x-amz-target,
 Signature=e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855

{
    "AssessmentId": "da-1234567890example1"
}
```

### Example Response

This example illustrates one usage of DescribeADAssessment.

```
HTTP/1.1 200 OK
x-amzn-RequestId: cfc1cbc8-c0b0-11e6-aa44-41d91ee57463
Content-Type: application/x-amz-json-1.1
Content-Length: 892
Date: Mon, 12 Dec 2023 21:20:31 GMT

{
    "Assessment": {
        "AssessmentId": "da-1234567890example1",
        "DnsName": "ad.example.com",
        "StartTime": "2025-06-10T14:28:54.934000-04:00",
        "LastUpdateDateTime": "2025-06-10T14:55:52.197000-04:00",
        "Status": "SUCCESS",
        "CustomerDnsIps": [
            "10.24.34.100",
            "10.24.34.200"
        ]
        "VpcId": "vpc-0e1051example5f2a",
        "SubnetIds": [
            "subnet-0fee0examplee9604",
            "subnet-076dbexample5ed88"
        ],
        "SelfManagedInstanceIds": [
            "i-10243410",
            "i-10243420"
        ],
        "ReportType": "CUSTOMER",
        "Version": "v1"
    },
    "AssessmentReports": [
        {
            "DomainControllerIp": "10.24.34.100",
            "Validations": [
                {
                    "Category": "preValidationTests",
                    "Name": "testDnsIpMatch",
                    "Status": "SUCCESS",
                    "StartTime": "2025-06-10T14:30:00.374000-04:00",
                    "LastUpdateDateTime": "2025-06-10T14:30:35.400000-04:00"
                },
                    . . .
            ]
        },
        {
            "DomainControllerIp": "10.24.34.200",
            "Validations": [
                {
                    "Category": "preValidationTests",
                    "Name": "testDnsIpMatch",
                    "Status": "SUCCESS",
                    "StartTime": "2025-06-10T14:30:00.374000-04:00",
                    "LastUpdateDateTime": "2025-06-10T14:30:35.446000-04:00"
                },
                    . . .
            ]
        }
    ]
}
```

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/ds-2015-04-16/DescribeADAssessment.md "../../../goto/cli2/ds-2015-04-16/DescribeADAssessment.md")
- [AWS SDK for .NET](../../../goto/DotNetSDKV3/ds-2015-04-16/DescribeADAssessment.md "../../../goto/DotNetSDKV3/ds-2015-04-16/DescribeADAssessment.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/ds-2015-04-16/DescribeADAssessment.md "../../../goto/SdkForCpp/ds-2015-04-16/DescribeADAssessment.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/ds-2015-04-16/DescribeADAssessment.md "../../../goto/SdkForGoV2/ds-2015-04-16/DescribeADAssessment.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/ds-2015-04-16/DescribeADAssessment.md "../../../goto/SdkForJavaV2/ds-2015-04-16/DescribeADAssessment.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/ds-2015-04-16/DescribeADAssessment.md "../../../goto/SdkForJavaScriptV3/ds-2015-04-16/DescribeADAssessment.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/ds-2015-04-16/DescribeADAssessment.md "../../../goto/SdkForKotlin/ds-2015-04-16/DescribeADAssessment.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/ds-2015-04-16/DescribeADAssessment.md "../../../goto/SdkForPHPV3/ds-2015-04-16/DescribeADAssessment.md")
- [AWS SDK for Python](../../../goto/boto3/ds-2015-04-16/DescribeADAssessment.md "../../../goto/boto3/ds-2015-04-16/DescribeADAssessment.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/ds-2015-04-16/DescribeADAssessment.md "../../../goto/SdkForRubyV3/ds-2015-04-16/DescribeADAssessment.md")
