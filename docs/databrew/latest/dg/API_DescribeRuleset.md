# DescribeRuleset

Retrieves detailed information about the ruleset.

## Request Syntax

```
GET /rulesets/`name` HTTP/1.1

```

## URI Request Parameters

The request uses the following URI parameters.

**[name](#API_DescribeRuleset_RequestSyntax "#API_DescribeRuleset_RequestSyntax")**

The name of the ruleset to be described.

Length Constraints: Minimum length of 1. Maximum length of 255.

Required: Yes

## Request Body

The request does not have a request body.

## Response Syntax

```
HTTP/1.1 200
Content-type: application/json

{
   "CreateDate": ***number***,
   "CreatedBy": "***string***",
   "Description": "***string***",
   "LastModifiedBy": "***string***",
   "LastModifiedDate": ***number***,
   "Name": "***string***",
   "ResourceArn": "***string***",
   "Rules": [
      {
         "CheckExpression": "***string***",
         "ColumnSelectors": [
            {
               "Name": "***string***",
               "Regex": "***string***"
            }
         ],
         "Disabled": ***boolean***,
         "Name": "***string***",
         "SubstitutionMap": {
            "***string***" : "***string***"
         },
         "Threshold": {
            "Type": "***string***",
            "Unit": "***string***",
            "Value": ***number***
         }
      }
   ],
   "Tags": {
      "***string***" : "***string***"
   },
   "TargetArn": "***string***"
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[Name](#API_DescribeRuleset_ResponseSyntax "#API_DescribeRuleset_ResponseSyntax")**

The name of the ruleset.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 255.

**[CreateDate](#API_DescribeRuleset_ResponseSyntax "#API_DescribeRuleset_ResponseSyntax")**

The date and time that the ruleset was created.

Type: Timestamp

**[CreatedBy](#API_DescribeRuleset_ResponseSyntax "#API_DescribeRuleset_ResponseSyntax")**

The Amazon Resource Name (ARN) of the user who created the ruleset.

Type: String

**[Description](#API_DescribeRuleset_ResponseSyntax "#API_DescribeRuleset_ResponseSyntax")**

The description of the ruleset.

Type: String

Length Constraints: Maximum length of 1024.

**[LastModifiedBy](#API_DescribeRuleset_ResponseSyntax "#API_DescribeRuleset_ResponseSyntax")**

The Amazon Resource Name (ARN) of the user who last modified the ruleset.

Type: String

**[LastModifiedDate](#API_DescribeRuleset_ResponseSyntax "#API_DescribeRuleset_ResponseSyntax")**

The modification date and time of the ruleset.

Type: Timestamp

**[ResourceArn](#API_DescribeRuleset_ResponseSyntax "#API_DescribeRuleset_ResponseSyntax")**

The Amazon Resource Name (ARN) for the ruleset.

Type: String

Length Constraints: Minimum length of 20. Maximum length of 2048.

**[Rules](#API_DescribeRuleset_ResponseSyntax "#API_DescribeRuleset_ResponseSyntax")**

A list of rules that are defined with the ruleset. A rule includes one
or more checks to be validated on a DataBrew dataset.

Type: Array of [Rule](API_Rule.md "API_Rule.md") objects

Array Members: Minimum number of 1 item.

**[Tags](#API_DescribeRuleset_ResponseSyntax "#API_DescribeRuleset_ResponseSyntax")**

Metadata tags that have been applied to the ruleset.

Type: String to string map

Map Entries: Maximum number of 200 items.

Key Length Constraints: Minimum length of 1. Maximum length of 128.

Value Length Constraints: Maximum length of 256.

**[TargetArn](#API_DescribeRuleset_ResponseSyntax "#API_DescribeRuleset_ResponseSyntax")**

The Amazon Resource Name (ARN) of a resource (dataset) that the ruleset is
associated with.

Type: String

Length Constraints: Minimum length of 20. Maximum length of 2048.

## Errors

For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").

**ResourceNotFoundException**

One or more resources can't be found.

HTTP Status Code: 404

**ValidationException**

The input parameters for this request failed validation.

HTTP Status Code: 400

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/databrew-2017-07-25/DescribeRuleset.md "../../../goto/cli2/databrew-2017-07-25/DescribeRuleset.md")
- [AWS SDK for .NET](../../../goto/DotNetSDKV3/databrew-2017-07-25/DescribeRuleset.md "../../../goto/DotNetSDKV3/databrew-2017-07-25/DescribeRuleset.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/databrew-2017-07-25/DescribeRuleset.md "../../../goto/SdkForCpp/databrew-2017-07-25/DescribeRuleset.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/databrew-2017-07-25/DescribeRuleset.md "../../../goto/SdkForGoV2/databrew-2017-07-25/DescribeRuleset.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/databrew-2017-07-25/DescribeRuleset.md "../../../goto/SdkForJavaV2/databrew-2017-07-25/DescribeRuleset.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/databrew-2017-07-25/DescribeRuleset.md "../../../goto/SdkForJavaScriptV3/databrew-2017-07-25/DescribeRuleset.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/databrew-2017-07-25/DescribeRuleset.md "../../../goto/SdkForKotlin/databrew-2017-07-25/DescribeRuleset.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/databrew-2017-07-25/DescribeRuleset.md "../../../goto/SdkForPHPV3/databrew-2017-07-25/DescribeRuleset.md")
- [AWS SDK for Python](../../../goto/boto3/databrew-2017-07-25/DescribeRuleset.md "../../../goto/boto3/databrew-2017-07-25/DescribeRuleset.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/databrew-2017-07-25/DescribeRuleset.md "../../../goto/SdkForRubyV3/databrew-2017-07-25/DescribeRuleset.md")
