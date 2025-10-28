# ImportAsProvisionedProduct

Requests the import of a resource as an AWS Service Catalog provisioned product
that is associated to an AWS Service Catalog product and provisioning artifact.
Once imported, all supported governance actions are supported on the provisioned product.

Resource import only supports AWS CloudFormation stack ARNs. AWS CloudFormation StackSets,
and non-root nested stacks, are not supported.

The AWS CloudFormation stack must have one
of the following statuses
to be imported: `CREATE_COMPLETE`, `UPDATE_COMPLETE`,
`UPDATE_ROLLBACK_COMPLETE`, `IMPORT_COMPLETE`, and
`IMPORT_ROLLBACK_COMPLETE`.

Import of the resource requires that the AWS CloudFormation stack template matches
the associated AWS Service Catalog product provisioning artifact.

###### Note

When you import an existing AWS CloudFormation stack
into a portfolio, AWS Service Catalog does not apply the product's associated constraints
during the import process. AWS Service Catalog applies the constraints
after you call `UpdateProvisionedProduct` for the provisioned product.

The user or role that performs this operation must have the `cloudformation:GetTemplate`
and `cloudformation:DescribeStacks` IAM policy permissions.

You can only import one provisioned product at a time. The product's AWS CloudFormation stack must have the
`IMPORT_COMPLETE` status before you import another.

## Request Syntax

```
{
   "AcceptLanguage": "`string`",
   "IdempotencyToken": "`string`",
   "PhysicalId": "`string`",
   "ProductId": "`string`",
   "ProvisionedProductName": "`string`",
   "ProvisioningArtifactId": "`string`"
}
```

## Request Parameters

The request accepts the following data in JSON format.

**[AcceptLanguage](#API_ImportAsProvisionedProduct_RequestSyntax "#API_ImportAsProvisionedProduct_RequestSyntax")**

The language code.

- `jp` - Japanese
- `zh` - Chinese

Type: String

Length Constraints: Maximum length of 100.

Required: No

**[IdempotencyToken](#API_ImportAsProvisionedProduct_RequestSyntax "#API_ImportAsProvisionedProduct_RequestSyntax")**

A unique identifier that you provide to ensure idempotency. If multiple requests differ only by the idempotency token,
the same response is returned for each repeated request.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 128.

Pattern: `[a-zA-Z0-9][a-zA-Z0-9_-]*`

Required: Yes

**[PhysicalId](#API_ImportAsProvisionedProduct_RequestSyntax "#API_ImportAsProvisionedProduct_RequestSyntax")**

The unique identifier of the resource to be imported. It only currently supports
AWS CloudFormation stack IDs.

Type: String

Required: Yes

**[ProductId](#API_ImportAsProvisionedProduct_RequestSyntax "#API_ImportAsProvisionedProduct_RequestSyntax")**

The product identifier.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 100.

Pattern: `^[a-zA-Z0-9_\-]*`

Required: Yes

**[ProvisionedProductName](#API_ImportAsProvisionedProduct_RequestSyntax "#API_ImportAsProvisionedProduct_RequestSyntax")**

The user-friendly name of the provisioned product. The value must be unique for the AWS account.
The name cannot be updated after the product is provisioned.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 128.

Pattern: `[a-zA-Z0-9][a-zA-Z0-9._-]*`

Required: Yes

**[ProvisioningArtifactId](#API_ImportAsProvisionedProduct_RequestSyntax "#API_ImportAsProvisionedProduct_RequestSyntax")**

The identifier of the provisioning artifact.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 100.

Pattern: `^[a-zA-Z0-9_\-]*`

Required: Yes

## Response Syntax

```
{
   "RecordDetail": {
      "CreatedTime": ***number***,
      "LaunchRoleArn": "***string***",
      "PathId": "***string***",
      "ProductId": "***string***",
      "ProvisionedProductId": "***string***",
      "ProvisionedProductName": "***string***",
      "ProvisionedProductType": "***string***",
      "ProvisioningArtifactId": "***string***",
      "RecordErrors": [
         {
            "Code": "***string***",
            "Description": "***string***"
         }
      ],
      "RecordId": "***string***",
      "RecordTags": [
         {
            "Key": "***string***",
            "Value": "***string***"
         }
      ],
      "RecordType": "***string***",
      "Status": "***string***",
      "UpdatedTime": ***number***
   }
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[RecordDetail](#API_ImportAsProvisionedProduct_ResponseSyntax "#API_ImportAsProvisionedProduct_ResponseSyntax")**

Information about a request operation.

Type: [RecordDetail](API_RecordDetail.md "API_RecordDetail.md") object

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

**ResourceNotFoundException**

The specified resource was not found.

HTTP Status Code: 400

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/servicecatalog-2015-12-10/ImportAsProvisionedProduct.md "../../../goto/cli2/servicecatalog-2015-12-10/ImportAsProvisionedProduct.md")
- [AWS SDK for .NET](../../../goto/DotNetSDKV3/servicecatalog-2015-12-10/ImportAsProvisionedProduct.md "../../../goto/DotNetSDKV3/servicecatalog-2015-12-10/ImportAsProvisionedProduct.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/servicecatalog-2015-12-10/ImportAsProvisionedProduct.md "../../../goto/SdkForCpp/servicecatalog-2015-12-10/ImportAsProvisionedProduct.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/servicecatalog-2015-12-10/ImportAsProvisionedProduct.md "../../../goto/SdkForGoV2/servicecatalog-2015-12-10/ImportAsProvisionedProduct.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/servicecatalog-2015-12-10/ImportAsProvisionedProduct.md "../../../goto/SdkForJavaV2/servicecatalog-2015-12-10/ImportAsProvisionedProduct.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/servicecatalog-2015-12-10/ImportAsProvisionedProduct.md "../../../goto/SdkForJavaScriptV3/servicecatalog-2015-12-10/ImportAsProvisionedProduct.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/servicecatalog-2015-12-10/ImportAsProvisionedProduct.md "../../../goto/SdkForKotlin/servicecatalog-2015-12-10/ImportAsProvisionedProduct.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/servicecatalog-2015-12-10/ImportAsProvisionedProduct.md "../../../goto/SdkForPHPV3/servicecatalog-2015-12-10/ImportAsProvisionedProduct.md")
- [AWS SDK for Python](../../../goto/boto3/servicecatalog-2015-12-10/ImportAsProvisionedProduct.md "../../../goto/boto3/servicecatalog-2015-12-10/ImportAsProvisionedProduct.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/servicecatalog-2015-12-10/ImportAsProvisionedProduct.md "../../../goto/SdkForRubyV3/servicecatalog-2015-12-10/ImportAsProvisionedProduct.md")
