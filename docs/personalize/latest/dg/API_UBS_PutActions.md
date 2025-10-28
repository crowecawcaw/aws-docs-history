# PutActions

Adds one or more actions to an Actions dataset. For more information see
[Importing actions individually](importing-actions.md "importing-actions.md").

## Request Syntax

```
POST /actions HTTP/1.1
Content-type: application/json

{
   "actions": [
      {
         "actionId": "`string`",
         "properties": "`string`"
      }
   ],
   "datasetArn": "`string`"
}
```

## URI Request Parameters

The request does not use any URI parameters.

## Request Body

The request accepts the following data in JSON format.

**[actions](#API_UBS_PutActions_RequestSyntax "#API_UBS_PutActions_RequestSyntax")**

A list of action data.

Type: Array of [Action](API_UBS_Action.md "API_UBS_Action.md") objects

Array Members: Minimum number of 1 item. Maximum number of 10 items.

Required: Yes

**[datasetArn](#API_UBS_PutActions_RequestSyntax "#API_UBS_PutActions_RequestSyntax")**

The Amazon Resource Name (ARN) of the Actions dataset you are adding the action or actions to.

Type: String

Length Constraints: Maximum length of 256.

Pattern: `arn:([a-z\d-]+):personalize:.*:.*:.+`

Required: Yes

## Response Syntax

```
HTTP/1.1 200

```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors

**InvalidInputException**

Provide a valid value for the field or parameter.

HTTP Status Code: 400

**ResourceInUseException**

The specified resource is in use.

HTTP Status Code: 409

**ResourceNotFoundException**

Could not find the specified resource.

HTTP Status Code: 404

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/personalize-events-2018-03-22/PutActions.md "../../../goto/cli2/personalize-events-2018-03-22/PutActions.md")
- [AWS SDK for .NET](../../../goto/DotNetSDKV3/personalize-events-2018-03-22/PutActions.md "../../../goto/DotNetSDKV3/personalize-events-2018-03-22/PutActions.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/personalize-events-2018-03-22/PutActions.md "../../../goto/SdkForCpp/personalize-events-2018-03-22/PutActions.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/personalize-events-2018-03-22/PutActions.md "../../../goto/SdkForGoV2/personalize-events-2018-03-22/PutActions.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/personalize-events-2018-03-22/PutActions.md "../../../goto/SdkForJavaV2/personalize-events-2018-03-22/PutActions.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/personalize-events-2018-03-22/PutActions.md "../../../goto/SdkForJavaScriptV3/personalize-events-2018-03-22/PutActions.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/personalize-events-2018-03-22/PutActions.md "../../../goto/SdkForKotlin/personalize-events-2018-03-22/PutActions.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/personalize-events-2018-03-22/PutActions.md "../../../goto/SdkForPHPV3/personalize-events-2018-03-22/PutActions.md")
- [AWS SDK for Python](../../../goto/boto3/personalize-events-2018-03-22/PutActions.md "../../../goto/boto3/personalize-events-2018-03-22/PutActions.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/personalize-events-2018-03-22/PutActions.md "../../../goto/SdkForRubyV3/personalize-events-2018-03-22/PutActions.md")
