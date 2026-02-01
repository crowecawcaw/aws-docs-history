# DeleteADAssessment

Deletes a directory assessment and all associated data. This operation permanently
removes the assessment results, validation reports, and configuration
information.

You cannot delete system-initiated assessments. You can delete customer-created
assessments even if they are in progress.

## Request Syntax

```
{
   "AssessmentId": "`string`"
}
```

## Request Parameters

The request accepts the following data in JSON format.

**[AssessmentId](#API_DeleteADAssessment_RequestSyntax "#API_DeleteADAssessment_RequestSyntax")**

The unique identifier of the directory assessment to delete.

Type: String

Pattern: `^da-[0-9a-f]{18}$`

Required: Yes

## Response Syntax

```
{
   "AssessmentId": "***string***"
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[AssessmentId](#API_DeleteADAssessment_ResponseSyntax "#API_DeleteADAssessment_ResponseSyntax")**

The unique identifier of the deleted directory assessment.

Type: String

Pattern: `^da-[0-9a-f]{18}$`

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

This example illustrates one usage of DeleteADAssessment.

```
POST / HTTP/1.1
Host: ds.us-west-2.amazonaws.com
Accept-Encoding: identity
Content-Length: 45
X-Amz-Target: DirectoryService_20150416.DeleteADAssessment
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

This example illustrates one usage of DeleteADAssessment.

```
HTTP/1.1 200 OK
x-amzn-RequestId: cfc1cbc8-c0b0-11e6-aa44-41d91ee57463
Content-Type: application/x-amz-json-1.1
Content-Length: 45
Date: Mon, 12 Dec 2023 21:20:31 GMT

{
   "AssessmentId": "da-1234567890example1"
}
```

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/ds-2015-04-16/DeleteADAssessment.md "../../../goto/cli2/ds-2015-04-16/DeleteADAssessment.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/ds-2015-04-16/DeleteADAssessment.md "../../../goto/DotNetSDKV4/ds-2015-04-16/DeleteADAssessment.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/ds-2015-04-16/DeleteADAssessment.md "../../../goto/SdkForCpp/ds-2015-04-16/DeleteADAssessment.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/ds-2015-04-16/DeleteADAssessment.md "../../../goto/SdkForGoV2/ds-2015-04-16/DeleteADAssessment.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/ds-2015-04-16/DeleteADAssessment.md "../../../goto/SdkForJavaV2/ds-2015-04-16/DeleteADAssessment.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/ds-2015-04-16/DeleteADAssessment.md "../../../goto/SdkForJavaScriptV3/ds-2015-04-16/DeleteADAssessment.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/ds-2015-04-16/DeleteADAssessment.md "../../../goto/SdkForKotlin/ds-2015-04-16/DeleteADAssessment.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/ds-2015-04-16/DeleteADAssessment.md "../../../goto/SdkForPHPV3/ds-2015-04-16/DeleteADAssessment.md")
- [AWS SDK for Python](../../../goto/boto3/ds-2015-04-16/DeleteADAssessment.md "../../../goto/boto3/ds-2015-04-16/DeleteADAssessment.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/ds-2015-04-16/DeleteADAssessment.md "../../../goto/SdkForRubyV3/ds-2015-04-16/DeleteADAssessment.md")
