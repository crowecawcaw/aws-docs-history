# ListFrameworks

Returns a list of all frameworks for an AWS account and AWS Region.

## Request Syntax

```
GET /audit/frameworks?MaxResults=`MaxResults`&NextToken=`NextToken` HTTP/1.1

```

## URI Request Parameters

The request uses the following URI parameters.

**[MaxResults](#API_ListFrameworks_RequestSyntax "#API_ListFrameworks_RequestSyntax")**

The number of desired results from 1 to 1000. Optional. If unspecified, the query will
return 1 MB of data.

Valid Range: Minimum value of 1. Maximum value of 1000.

**[NextToken](#API_ListFrameworks_RequestSyntax "#API_ListFrameworks_RequestSyntax")**

An identifier that was returned from the previous call to this operation, which can be
used to return the next set of items in the list.

## Request Body

The request does not have a request body.

## Response Syntax

```
HTTP/1.1 200
Content-type: application/json

{
   "Frameworks": [
      {
         "CreationTime": ***number***,
         "DeploymentStatus": "***string***",
         "FrameworkArn": "***string***",
         "FrameworkDescription": "***string***",
         "FrameworkName": "***string***",
         "NumberOfControls": ***number***
      }
   ],
   "NextToken": "***string***"
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[Frameworks](#API_ListFrameworks_ResponseSyntax "#API_ListFrameworks_ResponseSyntax")**

The frameworks with details for each framework, including the framework name,
Amazon Resource Name (ARN), description, number of controls, creation time, and deployment
status.

Type: Array of [Framework](API_Framework.md "API_Framework.md") objects

**[NextToken](#API_ListFrameworks_ResponseSyntax "#API_ListFrameworks_ResponseSyntax")**

An identifier that was returned from the previous call to this operation, which can be
used to return the next set of items in the list.

Type: String

## Errors

For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").

**InvalidParameterValueException**

Indicates that something is wrong with a parameter's value. For example, the value is
out of range.

**Context**

**Type**

HTTP Status Code: 400

**ServiceUnavailableException**

The request failed due to a temporary failure of the server.

**Context**

**Type**

HTTP Status Code: 500

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/backup-2018-11-15/ListFrameworks.md "../../../goto/cli2/backup-2018-11-15/ListFrameworks.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/backup-2018-11-15/ListFrameworks.md "../../../goto/DotNetSDKV4/backup-2018-11-15/ListFrameworks.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/backup-2018-11-15/ListFrameworks.md "../../../goto/SdkForCpp/backup-2018-11-15/ListFrameworks.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/backup-2018-11-15/ListFrameworks.md "../../../goto/SdkForGoV2/backup-2018-11-15/ListFrameworks.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/backup-2018-11-15/ListFrameworks.md "../../../goto/SdkForJavaV2/backup-2018-11-15/ListFrameworks.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/backup-2018-11-15/ListFrameworks.md "../../../goto/SdkForJavaScriptV3/backup-2018-11-15/ListFrameworks.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/backup-2018-11-15/ListFrameworks.md "../../../goto/SdkForKotlin/backup-2018-11-15/ListFrameworks.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/backup-2018-11-15/ListFrameworks.md "../../../goto/SdkForPHPV3/backup-2018-11-15/ListFrameworks.md")
- [AWS SDK for Python](../../../goto/boto3/backup-2018-11-15/ListFrameworks.md "../../../goto/boto3/backup-2018-11-15/ListFrameworks.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/backup-2018-11-15/ListFrameworks.md "../../../goto/SdkForRubyV3/backup-2018-11-15/ListFrameworks.md")
