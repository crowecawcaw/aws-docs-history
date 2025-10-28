# AssociateTagOptionWithResource

Associate the specified TagOption with the specified portfolio or product.

## Request Syntax

```
{
   "ResourceId": "`string`",
   "TagOptionId": "`string`"
}
```

## Request Parameters

The request accepts the following data in JSON format.

**[ResourceId](#API_AssociateTagOptionWithResource_RequestSyntax "#API_AssociateTagOptionWithResource_RequestSyntax")**

The resource identifier.

Type: String

Required: Yes

**[TagOptionId](#API_AssociateTagOptionWithResource_RequestSyntax "#API_AssociateTagOptionWithResource_RequestSyntax")**

The TagOption identifier.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 100.

Required: Yes

## Response Elements

If the action is successful, the service sends back an HTTP 200 response with an empty HTTP body.

## Errors

**DuplicateResourceException**

The specified resource is a duplicate.

HTTP Status Code: 400

**InvalidParametersException**

One or more parameters provided to the operation are not valid.

HTTP Status Code: 400

**InvalidStateException**

An attempt was made to modify a resource that is in a state that is not valid.
Check your resources to ensure that they are in valid states before retrying the operation.

HTTP Status Code: 400

**LimitExceededException**

The current limits of the service would have been exceeded by this operation. Decrease your
resource use or increase your service limits and retry the operation.

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

- [AWS Command Line Interface V2](../../../goto/cli2/servicecatalog-2015-12-10/AssociateTagOptionWithResource.md "../../../goto/cli2/servicecatalog-2015-12-10/AssociateTagOptionWithResource.md")
- [AWS SDK for .NET](../../../goto/DotNetSDKV3/servicecatalog-2015-12-10/AssociateTagOptionWithResource.md "../../../goto/DotNetSDKV3/servicecatalog-2015-12-10/AssociateTagOptionWithResource.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/servicecatalog-2015-12-10/AssociateTagOptionWithResource.md "../../../goto/SdkForCpp/servicecatalog-2015-12-10/AssociateTagOptionWithResource.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/servicecatalog-2015-12-10/AssociateTagOptionWithResource.md "../../../goto/SdkForGoV2/servicecatalog-2015-12-10/AssociateTagOptionWithResource.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/servicecatalog-2015-12-10/AssociateTagOptionWithResource.md "../../../goto/SdkForJavaV2/servicecatalog-2015-12-10/AssociateTagOptionWithResource.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/servicecatalog-2015-12-10/AssociateTagOptionWithResource.md "../../../goto/SdkForJavaScriptV3/servicecatalog-2015-12-10/AssociateTagOptionWithResource.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/servicecatalog-2015-12-10/AssociateTagOptionWithResource.md "../../../goto/SdkForKotlin/servicecatalog-2015-12-10/AssociateTagOptionWithResource.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/servicecatalog-2015-12-10/AssociateTagOptionWithResource.md "../../../goto/SdkForPHPV3/servicecatalog-2015-12-10/AssociateTagOptionWithResource.md")
- [AWS SDK for Python](../../../goto/boto3/servicecatalog-2015-12-10/AssociateTagOptionWithResource.md "../../../goto/boto3/servicecatalog-2015-12-10/AssociateTagOptionWithResource.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/servicecatalog-2015-12-10/AssociateTagOptionWithResource.md "../../../goto/SdkForRubyV3/servicecatalog-2015-12-10/AssociateTagOptionWithResource.md")
