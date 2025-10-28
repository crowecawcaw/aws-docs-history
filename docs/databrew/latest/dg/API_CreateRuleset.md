# CreateRuleset

Creates a new ruleset that can be used in a profile job to validate
the data quality of a dataset.

## Request Syntax

```
POST /rulesets HTTP/1.1
Content-type: application/json

{
   "Description": "`string`",
   "Name": "`string`",
   "Rules": [
      {
         "CheckExpression": "`string`",
         "ColumnSelectors": [
            {
               "Name": "`string`",
               "Regex": "`string`"
            }
         ],
         "Disabled": `boolean`,
         "Name": "`string`",
         "SubstitutionMap": {
            "`string`" : "`string`"
         },
         "Threshold": {
            "Type": "`string`",
            "Unit": "`string`",
            "Value": `number`
         }
      }
   ],
   "Tags": {
      "`string`" : "`string`"
   },
   "TargetArn": "`string`"
}
```

## URI Request Parameters

The request does not use any URI parameters.

## Request Body

The request accepts the following data in JSON format.

**[Name](#API_CreateRuleset_RequestSyntax "#API_CreateRuleset_RequestSyntax")**

The name of the ruleset to be created. Valid characters are alphanumeric
(A-Z, a-z, 0-9), hyphen (-), period (.), and space.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 255.

Required: Yes

**[Rules](#API_CreateRuleset_RequestSyntax "#API_CreateRuleset_RequestSyntax")**

A list of rules that are defined with the ruleset. A rule includes
one or more checks to be validated on a DataBrew dataset.

Type: Array of [Rule](API_Rule.md "API_Rule.md") objects

Array Members: Minimum number of 1 item.

Required: Yes

**[TargetArn](#API_CreateRuleset_RequestSyntax "#API_CreateRuleset_RequestSyntax")**

The Amazon Resource Name (ARN) of a resource (dataset) that the
ruleset is associated with.

Type: String

Length Constraints: Minimum length of 20. Maximum length of 2048.

Required: Yes

**[Description](#API_CreateRuleset_RequestSyntax "#API_CreateRuleset_RequestSyntax")**

The description of the ruleset.

Type: String

Length Constraints: Maximum length of 1024.

Required: No

**[Tags](#API_CreateRuleset_RequestSyntax "#API_CreateRuleset_RequestSyntax")**

Metadata tags to apply to the ruleset.

Type: String to string map

Map Entries: Maximum number of 200 items.

Key Length Constraints: Minimum length of 1. Maximum length of 128.

Value Length Constraints: Maximum length of 256.

Required: No

## Response Syntax

```
HTTP/1.1 200
Content-type: application/json

{
   "Name": "***string***"
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[Name](#API_CreateRuleset_ResponseSyntax "#API_CreateRuleset_ResponseSyntax")**

The unique name of the created ruleset.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 255.

## Errors

For information about the errors that are common to all actions, see [Common Errors](CommonErrors.md "CommonErrors.md").

**ConflictException**

Updating or deleting a resource can cause an inconsistent state.

HTTP Status Code: 409

**ServiceQuotaExceededException**

A service quota is exceeded.

HTTP Status Code: 402

**ValidationException**

The input parameters for this request failed validation.

HTTP Status Code: 400

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/databrew-2017-07-25/CreateRuleset.md "../../../goto/cli2/databrew-2017-07-25/CreateRuleset.md")
- [AWS SDK for .NET](../../../goto/DotNetSDKV3/databrew-2017-07-25/CreateRuleset.md "../../../goto/DotNetSDKV3/databrew-2017-07-25/CreateRuleset.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/databrew-2017-07-25/CreateRuleset.md "../../../goto/SdkForCpp/databrew-2017-07-25/CreateRuleset.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/databrew-2017-07-25/CreateRuleset.md "../../../goto/SdkForGoV2/databrew-2017-07-25/CreateRuleset.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/databrew-2017-07-25/CreateRuleset.md "../../../goto/SdkForJavaV2/databrew-2017-07-25/CreateRuleset.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/databrew-2017-07-25/CreateRuleset.md "../../../goto/SdkForJavaScriptV3/databrew-2017-07-25/CreateRuleset.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/databrew-2017-07-25/CreateRuleset.md "../../../goto/SdkForKotlin/databrew-2017-07-25/CreateRuleset.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/databrew-2017-07-25/CreateRuleset.md "../../../goto/SdkForPHPV3/databrew-2017-07-25/CreateRuleset.md")
- [AWS SDK for Python](../../../goto/boto3/databrew-2017-07-25/CreateRuleset.md "../../../goto/boto3/databrew-2017-07-25/CreateRuleset.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/databrew-2017-07-25/CreateRuleset.md "../../../goto/SdkForRubyV3/databrew-2017-07-25/CreateRuleset.md")
