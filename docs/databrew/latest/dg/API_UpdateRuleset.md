# UpdateRuleset

Updates specified ruleset.

## Request Syntax

```
PUT /rulesets/`name` HTTP/1.1
Content-type: application/json

{
   "Description": "`string`",
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
   ]
}
```

## URI Request Parameters

The request uses the following URI parameters.

**[name](#API_UpdateRuleset_RequestSyntax "#API_UpdateRuleset_RequestSyntax")**

The name of the ruleset to be updated.

Length Constraints: Minimum length of 1. Maximum length of 255.

Required: Yes

## Request Body

The request accepts the following data in JSON format.

**[Rules](#API_UpdateRuleset_RequestSyntax "#API_UpdateRuleset_RequestSyntax")**

A list of rules that are defined with the ruleset. A rule includes one or more
checks to be validated on a DataBrew dataset.

Type: Array of [Rule](API_Rule.md "API_Rule.md") objects

Array Members: Minimum number of 1 item.

Required: Yes

**[Description](#API_UpdateRuleset_RequestSyntax "#API_UpdateRuleset_RequestSyntax")**

The description of the ruleset.

Type: String

Length Constraints: Maximum length of 1024.

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

**[Name](#API_UpdateRuleset_ResponseSyntax "#API_UpdateRuleset_ResponseSyntax")**

The name of the updated ruleset.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 255.

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

- [AWS Command Line Interface V2](../../../goto/cli2/databrew-2017-07-25/UpdateRuleset.md "../../../goto/cli2/databrew-2017-07-25/UpdateRuleset.md")
- [AWS SDK for .NET](../../../goto/DotNetSDKV3/databrew-2017-07-25/UpdateRuleset.md "../../../goto/DotNetSDKV3/databrew-2017-07-25/UpdateRuleset.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/databrew-2017-07-25/UpdateRuleset.md "../../../goto/SdkForCpp/databrew-2017-07-25/UpdateRuleset.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/databrew-2017-07-25/UpdateRuleset.md "../../../goto/SdkForGoV2/databrew-2017-07-25/UpdateRuleset.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/databrew-2017-07-25/UpdateRuleset.md "../../../goto/SdkForJavaV2/databrew-2017-07-25/UpdateRuleset.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/databrew-2017-07-25/UpdateRuleset.md "../../../goto/SdkForJavaScriptV3/databrew-2017-07-25/UpdateRuleset.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/databrew-2017-07-25/UpdateRuleset.md "../../../goto/SdkForKotlin/databrew-2017-07-25/UpdateRuleset.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/databrew-2017-07-25/UpdateRuleset.md "../../../goto/SdkForPHPV3/databrew-2017-07-25/UpdateRuleset.md")
- [AWS SDK for Python](../../../goto/boto3/databrew-2017-07-25/UpdateRuleset.md "../../../goto/boto3/databrew-2017-07-25/UpdateRuleset.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/databrew-2017-07-25/UpdateRuleset.md "../../../goto/SdkForRubyV3/databrew-2017-07-25/UpdateRuleset.md")
