# ListADAssessments

Retrieves a list of directory assessments for the specified directory or all
assessments in your account. Use this operation to monitor assessment status and manage
multiple assessments.

## Request Syntax

```
{
   "DirectoryId": "`string`",
   "Limit": `number`,
   "NextToken": "`string`"
}
```

## Request Parameters

The request accepts the following data in JSON format.

**[DirectoryId](#API_ListADAssessments_RequestSyntax "#API_ListADAssessments_RequestSyntax")**

The identifier of the directory for which to list assessments. If not specified, all
assessments in your account are returned.

Type: String

Pattern: `^d-[0-9a-f]{10}$`

Required: No

**[Limit](#API_ListADAssessments_RequestSyntax "#API_ListADAssessments_RequestSyntax")**

The maximum number of assessment summaries to return.

Type: Integer

Valid Range: Minimum value of 1. Maximum value of 100.

Required: No

**[NextToken](#API_ListADAssessments_RequestSyntax "#API_ListADAssessments_RequestSyntax")**

The pagination token from a previous request to [ListADAssessments](API_ListADAssessments.md "API_ListADAssessments.md").
Pass null if this is the first request.

Type: String

Required: No

## Response Syntax

```
{
   "Assessments": [
      {
         "AssessmentId": "***string***",
         "CustomerDnsIps": [ "***string***" ],
         "DirectoryId": "***string***",
         "DnsName": "***string***",
         "LastUpdateDateTime": ***number***,
         "ReportType": "***string***",
         "StartTime": ***number***,
         "Status": "***string***"
      }
   ],
   "NextToken": "***string***"
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[Assessments](#API_ListADAssessments_ResponseSyntax "#API_ListADAssessments_ResponseSyntax")**

A list of assessment summaries containing basic information about each directory
assessment.

Type: Array of [AssessmentSummary](API_AssessmentSummary.md "API_AssessmentSummary.md") objects

**[NextToken](#API_ListADAssessments_ResponseSyntax "#API_ListADAssessments_ResponseSyntax")**

If not null, more results are available. Pass this value for the
`NextToken` parameter in a subsequent request to retrieve the next set of
items.

Type: String

## Errors

For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").

**ClientException**

A client exception has occurred.

**Message**

The descriptive message for the exception.

**RequestId**

The AWS request identifier.

HTTP Status Code: 400

**DirectoryDoesNotExistException**

The specified directory does not exist in the system.

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

This example illustrates one usage of ListADAssessments.

```
POST / HTTP/1.1
Host: ds.us-west-2.amazonaws.com
Accept-Encoding: identity
Content-Length: 75
X-Amz-Target: DirectoryService_20150416.ListADAssessments
X-Amz-Date: 20231212T212029Z
User-Agent: aws-cli/2.0.0 Python/3.8.0 Linux/5.4.0 botocore/2.0.0
Content-Type: application/x-amz-json-1.1
Authorization: AWS4-HMAC-SHA256
 Credential=AKIAI7E3BYXS3example/20231212/us-west-2/ds/aws4_request,
 SignedHeaders=content-type;host;x-amz-date;x-amz-target,
 Signature=e3b0c44298fc1c149afbf4c8996fb92427ae41e4649b934ca495991b7852b855

{
    "DirectoryId": "d-926example"
}
```

### Example Response

This example illustrates one usage of ListADAssessments.

```
HTTP/1.1 200 OK
x-amzn-RequestId: cfc1cbc8-c0b0-11e6-aa44-41d91ee57463
Content-Type: application/x-amz-json-1.1
Content-Length: 524
Date: Mon, 12 Dec 2023 21:20:31 GMT

{
    "Assessments": [{
            "AssessmentId": "da-1234567890example1",
            "DirectoryId": "d-926example",
            "DnsName": "ad.example.com",
            "StartTime": "2025-06-15T23:21:49.074000-04:00",
            "LastUpdateDateTime": "2025-06-16T16:42:54.861000-04:00",
            "Status": "SUCCESS",
            "CustomerDnsIps": [
                "10.24.34.100",
                "10.24.34.200"
            ],
            "ReportType": "SYSTEM"
        },
        {
            "AssessmentId": "da-09876543210example2",
            "DirectoryId": "d-926example",
            "DnsName": "ad.example.com",
            "StartTime": "2025-06-10T14:28:54.934000-04:00",
            "LastUpdateDateTime": "2025-06-10T14:55:52.197000-04:00",
            "Status": "FAILED",
            "CustomerDnsIps": [
                "10.24.34.100",
                "10.24.34.200"
            ],
            "ReportType": "CUSTOMER"
        }
    ]
}
```

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/ds-2015-04-16/ListADAssessments.md "../../../goto/cli2/ds-2015-04-16/ListADAssessments.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/ds-2015-04-16/ListADAssessments.md "../../../goto/DotNetSDKV4/ds-2015-04-16/ListADAssessments.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/ds-2015-04-16/ListADAssessments.md "../../../goto/SdkForCpp/ds-2015-04-16/ListADAssessments.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/ds-2015-04-16/ListADAssessments.md "../../../goto/SdkForGoV2/ds-2015-04-16/ListADAssessments.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/ds-2015-04-16/ListADAssessments.md "../../../goto/SdkForJavaV2/ds-2015-04-16/ListADAssessments.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/ds-2015-04-16/ListADAssessments.md "../../../goto/SdkForJavaScriptV3/ds-2015-04-16/ListADAssessments.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/ds-2015-04-16/ListADAssessments.md "../../../goto/SdkForKotlin/ds-2015-04-16/ListADAssessments.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/ds-2015-04-16/ListADAssessments.md "../../../goto/SdkForPHPV3/ds-2015-04-16/ListADAssessments.md")
- [AWS SDK for Python](../../../goto/boto3/ds-2015-04-16/ListADAssessments.md "../../../goto/boto3/ds-2015-04-16/ListADAssessments.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/ds-2015-04-16/ListADAssessments.md "../../../goto/SdkForRubyV3/ds-2015-04-16/ListADAssessments.md")
