# DeleteTagOption

Deletes the specified TagOption.

You cannot delete a TagOption if it is associated with a product or portfolio.

## Request Syntax

```
{
   "Id": "`string`"
}
```

## Request Parameters

The request accepts the following data in JSON format.

**[Id](#API_DeleteTagOption_RequestSyntax "#API_DeleteTagOption_RequestSyntax")**

The TagOption identifier.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 100.

Required: Yes

## Response Elements

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors

**ResourceInUseException**

A resource that is currently in use. Ensure that the resource is not in use and retry the operation.

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

- [AWS Command Line Interface V2](../../../goto/cli2/servicecatalog-2015-12-10/DeleteTagOption.md "../../../goto/cli2/servicecatalog-2015-12-10/DeleteTagOption.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/servicecatalog-2015-12-10/DeleteTagOption.md "../../../goto/DotNetSDKV4/servicecatalog-2015-12-10/DeleteTagOption.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/servicecatalog-2015-12-10/DeleteTagOption.md "../../../goto/SdkForCpp/servicecatalog-2015-12-10/DeleteTagOption.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/servicecatalog-2015-12-10/DeleteTagOption.md "../../../goto/SdkForGoV2/servicecatalog-2015-12-10/DeleteTagOption.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/servicecatalog-2015-12-10/DeleteTagOption.md "../../../goto/SdkForJavaV2/servicecatalog-2015-12-10/DeleteTagOption.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/servicecatalog-2015-12-10/DeleteTagOption.md "../../../goto/SdkForJavaScriptV3/servicecatalog-2015-12-10/DeleteTagOption.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/servicecatalog-2015-12-10/DeleteTagOption.md "../../../goto/SdkForKotlin/servicecatalog-2015-12-10/DeleteTagOption.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/servicecatalog-2015-12-10/DeleteTagOption.md "../../../goto/SdkForPHPV3/servicecatalog-2015-12-10/DeleteTagOption.md")
- [AWS SDK for Python](../../../goto/boto3/servicecatalog-2015-12-10/DeleteTagOption.md "../../../goto/boto3/servicecatalog-2015-12-10/DeleteTagOption.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/servicecatalog-2015-12-10/DeleteTagOption.md "../../../goto/SdkForRubyV3/servicecatalog-2015-12-10/DeleteTagOption.md")
