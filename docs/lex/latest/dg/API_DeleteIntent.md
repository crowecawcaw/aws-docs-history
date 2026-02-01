End of support notice: On September 15, 2025, AWS
will discontinue support for Amazon Lex V1. After September 15, 2025, you will
no longer be able to access the Amazon Lex V1 console or Amazon Lex V1 resources. If you are using Amazon Lex V2, refer to the [Amazon Lex V2 guide](../../../lexv2/latest/dg/what-is.md "../../../lexv2/latest/dg/what-is.md") instead.
.

# DeleteIntent

Deletes all versions of the intent, including the
`$LATEST` version. To delete a specific version of the
intent, use the [DeleteIntentVersion](API_DeleteIntentVersion.md "API_DeleteIntentVersion.md") operation.

You can delete a version of an intent only if it is not
referenced. To delete an intent that is referred to in one or more bots
(see [Amazon Lex: How It Works](how-it-works.md "how-it-works.md")), you must remove those references
first.

###### Note

If you get the `ResourceInUseException` exception, it
provides an example reference that shows where the intent is referenced.
To remove the reference to the intent, either update the bot or delete
it. If you get the same exception when you attempt to delete the intent
again, repeat until the intent has no references and the call to
`DeleteIntent` is successful.

This operation requires permission for the
`lex:DeleteIntent` action.

## Request Syntax

```
DELETE /intents/`name` HTTP/1.1

```

## URI Request Parameters

The request uses the following URI parameters.

**[name](#API_DeleteIntent_RequestSyntax "#API_DeleteIntent_RequestSyntax")**

The name of the intent. The name is case sensitive.

Length Constraints: Minimum length of 1. Maximum length of 100.

Pattern: `^([A-Za-z]_?)+$`

Required: Yes

## Request Body

The request does not have a request body.

## Response Syntax

```
HTTP/1.1 204

```

## Response Elements

If the action is successful, the service sends back an HTTP 204 response with an empty HTTP body.

## Errors

**BadRequestException**

The request is not well formed. For example, a value is invalid or
a required field is missing. Check the field values, and try
again.

HTTP Status Code: 400

**ConflictException**

There was a conflict processing the request. Try your request
again.

HTTP Status Code: 409

**InternalFailureException**

An internal Amazon Lex error occurred. Try your request again.

HTTP Status Code: 500

**LimitExceededException**

The request exceeded a limit. Try your request again.

HTTP Status Code: 429

**NotFoundException**

The resource specified in the request was not found. Check the
resource and try again.

HTTP Status Code: 404

**ResourceInUseException**

The resource that you are attempting to delete is referred to by
another resource. Use this information to remove references to the
resource that you are trying to delete.

The body of the exception contains a JSON object that describes the
resource.

`{ "resourceType": BOT | BOTALIAS | BOTCHANNEL |
 INTENT,`

`"resourceReference": {`

`"name": *string*, "version":
 *string* } }`

**exampleReference**

Describes the resource that refers to the resource that you are
attempting to delete. This object is returned as part of the
`ResourceInUseException` exception.

HTTP Status Code: 400

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/lex-models-2017-04-19/DeleteIntent.md "../../../goto/cli2/lex-models-2017-04-19/DeleteIntent.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/lex-models-2017-04-19/DeleteIntent.md "../../../goto/DotNetSDKV4/lex-models-2017-04-19/DeleteIntent.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/lex-models-2017-04-19/DeleteIntent.md "../../../goto/SdkForCpp/lex-models-2017-04-19/DeleteIntent.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/lex-models-2017-04-19/DeleteIntent.md "../../../goto/SdkForGoV2/lex-models-2017-04-19/DeleteIntent.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/lex-models-2017-04-19/DeleteIntent.md "../../../goto/SdkForJavaV2/lex-models-2017-04-19/DeleteIntent.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/lex-models-2017-04-19/DeleteIntent.md "../../../goto/SdkForJavaScriptV3/lex-models-2017-04-19/DeleteIntent.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/lex-models-2017-04-19/DeleteIntent.md "../../../goto/SdkForKotlin/lex-models-2017-04-19/DeleteIntent.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/lex-models-2017-04-19/DeleteIntent.md "../../../goto/SdkForPHPV3/lex-models-2017-04-19/DeleteIntent.md")
- [AWS SDK for Python](../../../goto/boto3/lex-models-2017-04-19/DeleteIntent.md "../../../goto/boto3/lex-models-2017-04-19/DeleteIntent.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/lex-models-2017-04-19/DeleteIntent.md "../../../goto/SdkForRubyV3/lex-models-2017-04-19/DeleteIntent.md")
