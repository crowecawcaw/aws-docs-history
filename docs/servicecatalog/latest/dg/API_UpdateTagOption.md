# UpdateTagOption

Updates the specified TagOption.

## Request Syntax

```
{
   "Active": `boolean`,
   "Id": "`string`",
   "Value": "`string`"
}
```

## Request Parameters

The request accepts the following data in JSON format.

**[Active](#API_UpdateTagOption_RequestSyntax "#API_UpdateTagOption_RequestSyntax")**

The updated active state.

Type: Boolean

Required: No

**[Id](#API_UpdateTagOption_RequestSyntax "#API_UpdateTagOption_RequestSyntax")**

The TagOption identifier.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 100.

Required: Yes

**[Value](#API_UpdateTagOption_RequestSyntax "#API_UpdateTagOption_RequestSyntax")**

The updated value.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 256.

Pattern: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`

Required: No

## Response Syntax

```
{
   "TagOptionDetail": {
      "Active": ***boolean***,
      "Id": "***string***",
      "Key": "***string***",
      "Owner": "***string***",
      "Value": "***string***"
   }
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[TagOptionDetail](#API_UpdateTagOption_ResponseSyntax "#API_UpdateTagOption_ResponseSyntax")**

Information about the TagOption.

Type: [TagOptionDetail](API_TagOptionDetail.md "API_TagOptionDetail.md") object

## Errors

**DuplicateResourceException**

The specified resource is a duplicate.

HTTP Status Code: 400

**InvalidParametersException**

One or more parameters provided to the operation are not valid.

HTTP Status Code: 400

**ResourceNotFoundException**

The specified resource was not found.

HTTP Status Code: 400

**TagOptionNotMigratedException**

An operation requiring TagOptions failed because the TagOptions migration process has
not been performed for this account. Use the AWS Management Console to perform the migration
process before retrying the operation.

HTTP Status Code: 400

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/servicecatalog-2015-12-10/UpdateTagOption.md "../../../goto/cli2/servicecatalog-2015-12-10/UpdateTagOption.md")
- [AWS SDK for .NET](../../../goto/DotNetSDKV3/servicecatalog-2015-12-10/UpdateTagOption.md "../../../goto/DotNetSDKV3/servicecatalog-2015-12-10/UpdateTagOption.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/servicecatalog-2015-12-10/UpdateTagOption.md "../../../goto/SdkForCpp/servicecatalog-2015-12-10/UpdateTagOption.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/servicecatalog-2015-12-10/UpdateTagOption.md "../../../goto/SdkForGoV2/servicecatalog-2015-12-10/UpdateTagOption.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/servicecatalog-2015-12-10/UpdateTagOption.md "../../../goto/SdkForJavaV2/servicecatalog-2015-12-10/UpdateTagOption.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/servicecatalog-2015-12-10/UpdateTagOption.md "../../../goto/SdkForJavaScriptV3/servicecatalog-2015-12-10/UpdateTagOption.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/servicecatalog-2015-12-10/UpdateTagOption.md "../../../goto/SdkForKotlin/servicecatalog-2015-12-10/UpdateTagOption.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/servicecatalog-2015-12-10/UpdateTagOption.md "../../../goto/SdkForPHPV3/servicecatalog-2015-12-10/UpdateTagOption.md")
- [AWS SDK for Python](../../../goto/boto3/servicecatalog-2015-12-10/UpdateTagOption.md "../../../goto/boto3/servicecatalog-2015-12-10/UpdateTagOption.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/servicecatalog-2015-12-10/UpdateTagOption.md "../../../goto/SdkForRubyV3/servicecatalog-2015-12-10/UpdateTagOption.md")
