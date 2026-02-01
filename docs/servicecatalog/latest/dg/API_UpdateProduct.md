# UpdateProduct

Updates the specified product.

## Request Syntax

```
{
   "AcceptLanguage": "`string`",
   "AddTags": [
      {
         "Key": "`string`",
         "Value": "`string`"
      }
   ],
   "Description": "`string`",
   "Distributor": "`string`",
   "Id": "`string`",
   "Name": "`string`",
   "Owner": "`string`",
   "RemoveTags": [ "`string`" ],
   "SourceConnection": {
      "ConnectionParameters": {
         "CodeStar": {
            "ArtifactPath": "`string`",
            "Branch": "`string`",
            "ConnectionArn": "`string`",
            "Repository": "`string`"
         }
      },
      "Type": "`string`"
   },
   "SupportDescription": "`string`",
   "SupportEmail": "`string`",
   "SupportUrl": "`string`"
}
```

## Request Parameters

The request accepts the following data in JSON format.

**[AcceptLanguage](#API_UpdateProduct_RequestSyntax "#API_UpdateProduct_RequestSyntax")**

The language code.

- `jp` - Japanese
- `zh` - Chinese

Type: String

Length Constraints: Maximum length of 100.

Required: No

**[AddTags](#API_UpdateProduct_RequestSyntax "#API_UpdateProduct_RequestSyntax")**

The tags to add to the product.

Type: Array of [Tag](API_Tag.md "API_Tag.md") objects

Array Members: Maximum number of 20 items.

Required: No

**[Description](#API_UpdateProduct_RequestSyntax "#API_UpdateProduct_RequestSyntax")**

The updated description of the product.

Type: String

Length Constraints: Maximum length of 8191.

Required: No

**[Distributor](#API_UpdateProduct_RequestSyntax "#API_UpdateProduct_RequestSyntax")**

The updated distributor of the product.

Type: String

Length Constraints: Maximum length of 8191.

Required: No

**[Id](#API_UpdateProduct_RequestSyntax "#API_UpdateProduct_RequestSyntax")**

The product identifier.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 100.

Pattern: `^[a-zA-Z0-9_\-]*`

Required: Yes

**[Name](#API_UpdateProduct_RequestSyntax "#API_UpdateProduct_RequestSyntax")**

The updated product name.

Type: String

Length Constraints: Maximum length of 8191.

Required: No

**[Owner](#API_UpdateProduct_RequestSyntax "#API_UpdateProduct_RequestSyntax")**

The updated owner of the product.

Type: String

Length Constraints: Maximum length of 8191.

Required: No

**[RemoveTags](#API_UpdateProduct_RequestSyntax "#API_UpdateProduct_RequestSyntax")**

The tags to remove from the product.

Type: Array of strings

Length Constraints: Minimum length of 1. Maximum length of 128.

Pattern: `^([\p{L}\p{Z}\p{N}_.:/=+\-@]*)$`

Required: No

**[SourceConnection](#API_UpdateProduct_RequestSyntax "#API_UpdateProduct_RequestSyntax")**

Specifies connection details for the updated product and syncs the product to the connection source
artifact. This automatically manages the product's artifacts based on changes to the source.
The `SourceConnection` parameter consists of the following sub-fields.

- `Type`
- `ConnectionParamters`

Type: [SourceConnection](API_SourceConnection.md "API_SourceConnection.md") object

Required: No

**[SupportDescription](#API_UpdateProduct_RequestSyntax "#API_UpdateProduct_RequestSyntax")**

The updated support description for the product.

Type: String

Length Constraints: Maximum length of 8191.

Required: No

**[SupportEmail](#API_UpdateProduct_RequestSyntax "#API_UpdateProduct_RequestSyntax")**

The updated support email for the product.

Type: String

Length Constraints: Maximum length of 254.

Required: No

**[SupportUrl](#API_UpdateProduct_RequestSyntax "#API_UpdateProduct_RequestSyntax")**

The updated support URL for the product.

Type: String

Length Constraints: Maximum length of 2083.

Required: No

## Response Syntax

```
{
   "ProductViewDetail": {
      "CreatedTime": ***number***,
      "ProductARN": "***string***",
      "ProductViewSummary": {
         "Distributor": "***string***",
         "HasDefaultPath": ***boolean***,
         "Id": "***string***",
         "Name": "***string***",
         "Owner": "***string***",
         "ProductId": "***string***",
         "ShortDescription": "***string***",
         "SupportDescription": "***string***",
         "SupportEmail": "***string***",
         "SupportUrl": "***string***",
         "Type": "***string***"
      },
      "SourceConnection": {
         "ConnectionParameters": {
            "CodeStar": {
               "ArtifactPath": "***string***",
               "Branch": "***string***",
               "ConnectionArn": "***string***",
               "Repository": "***string***"
            }
         },
         "LastSync": {
            "LastSuccessfulSyncProvisioningArtifactId": "***string***",
            "LastSuccessfulSyncTime": ***number***,
            "LastSyncStatus": "***string***",
            "LastSyncStatusMessage": "***string***",
            "LastSyncTime": ***number***
         },
         "Type": "***string***"
      },
      "Status": "***string***"
   },
   "Tags": [
      {
         "Key": "***string***",
         "Value": "***string***"
      }
   ]
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[ProductViewDetail](#API_UpdateProduct_ResponseSyntax "#API_UpdateProduct_ResponseSyntax")**

Information about the product view.

Type: [ProductViewDetail](API_ProductViewDetail.md "API_ProductViewDetail.md") object

**[Tags](#API_UpdateProduct_ResponseSyntax "#API_UpdateProduct_ResponseSyntax")**

Information about the tags associated with the product.

Type: Array of [Tag](API_Tag.md "API_Tag.md") objects

Array Members: Maximum number of 50 items.

## Errors

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

- [AWS Command Line Interface V2](../../../goto/cli2/servicecatalog-2015-12-10/UpdateProduct.md "../../../goto/cli2/servicecatalog-2015-12-10/UpdateProduct.md")
- [AWS SDK for .NET V4](../../../goto/DotNetSDKV4/servicecatalog-2015-12-10/UpdateProduct.md "../../../goto/DotNetSDKV4/servicecatalog-2015-12-10/UpdateProduct.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/servicecatalog-2015-12-10/UpdateProduct.md "../../../goto/SdkForCpp/servicecatalog-2015-12-10/UpdateProduct.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/servicecatalog-2015-12-10/UpdateProduct.md "../../../goto/SdkForGoV2/servicecatalog-2015-12-10/UpdateProduct.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/servicecatalog-2015-12-10/UpdateProduct.md "../../../goto/SdkForJavaV2/servicecatalog-2015-12-10/UpdateProduct.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/servicecatalog-2015-12-10/UpdateProduct.md "../../../goto/SdkForJavaScriptV3/servicecatalog-2015-12-10/UpdateProduct.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/servicecatalog-2015-12-10/UpdateProduct.md "../../../goto/SdkForKotlin/servicecatalog-2015-12-10/UpdateProduct.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/servicecatalog-2015-12-10/UpdateProduct.md "../../../goto/SdkForPHPV3/servicecatalog-2015-12-10/UpdateProduct.md")
- [AWS SDK for Python](../../../goto/boto3/servicecatalog-2015-12-10/UpdateProduct.md "../../../goto/boto3/servicecatalog-2015-12-10/UpdateProduct.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/servicecatalog-2015-12-10/UpdateProduct.md "../../../goto/SdkForRubyV3/servicecatalog-2015-12-10/UpdateProduct.md")
