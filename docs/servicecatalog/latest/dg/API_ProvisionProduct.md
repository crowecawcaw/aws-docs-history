# ProvisionProduct

Provisions the specified product.

A provisioned product is a resourced instance
of a product.
For example,
provisioning a product
that's based
on an AWS CloudFormation template
launches an AWS CloudFormation stack and its underlying resources.
You can check the status
of this request
using [DescribeRecord](API_DescribeRecord.md "API_DescribeRecord.md").

If the request contains a tag key
with an empty list
of values,
there's a tag conflict
for that key.
Don't include conflicted keys
as tags,
or this will cause the error "Parameter validation failed: Missing required parameter in Tags[*N*]:_Value_".

###### Note

When provisioning a product
that's been added
to a portfolio,
you must grant your user, group, or role access
to the portfolio.
For more information,
see [Granting users access](../adminguide/catalogs_portfolios_users.md "../adminguide/catalogs_portfolios_users.md")
in the _Service Catalog User Guide_.

## Request Syntax

```
{
   "AcceptLanguage": "`string`",
   "NotificationArns": [ "`string`" ],
   "PathId": "`string`",
   "PathName": "`string`",
   "ProductId": "`string`",
   "ProductName": "`string`",
   "ProvisionedProductName": "`string`",
   "ProvisioningArtifactId": "`string`",
   "ProvisioningArtifactName": "`string`",
   "ProvisioningParameters": [
      {
         "Key": "`string`",
         "Value": "`string`"
      }
   ],
   "ProvisioningPreferences": {
      "StackSetAccounts": [ "`string`" ],
      "StackSetFailureToleranceCount": `number`,
      "StackSetFailureTolerancePercentage": `number`,
      "StackSetMaxConcurrencyCount": `number`,
      "StackSetMaxConcurrencyPercentage": `number`,
      "StackSetRegions": [ "`string`" ]
   },
   "ProvisionToken": "`string`",
   "Tags": [
      {
         "Key": "`string`",
         "Value": "`string`"
      }
   ]
}
```

## Request Parameters

The request accepts the following data in JSON format.

**[AcceptLanguage](#API_ProvisionProduct_RequestSyntax "#API_ProvisionProduct_RequestSyntax")**

The language code.

- `jp` - Japanese
- `zh` - Chinese

Type: String

Length Constraints: Maximum length of 100.

Required: No

**[NotificationArns](#API_ProvisionProduct_RequestSyntax "#API_ProvisionProduct_RequestSyntax")**

Passed to AWS CloudFormation. The SNS topic ARNs to which to publish stack-related
events.

Type: Array of strings

Array Members: Maximum number of 5 items.

Length Constraints: Minimum length of 1. Maximum length of 1224.

Pattern: `arn:[a-z0-9-\.]{1,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[^/].{0,1023}`

Required: No

**[PathId](#API_ProvisionProduct_RequestSyntax "#API_ProvisionProduct_RequestSyntax")**

The path identifier of the product. This value is optional if the product
has a default path, and required if the product has more than one path.
To list the paths for a product, use [ListLaunchPaths](API_ListLaunchPaths.md "API_ListLaunchPaths.md"). You must provide the name or ID, but not both.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 100.

Pattern: `^[a-zA-Z0-9_\-]*`

Required: No

**[PathName](#API_ProvisionProduct_RequestSyntax "#API_ProvisionProduct_RequestSyntax")**

The name of the path. You must provide the name or ID, but not both.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 100.

Required: No

**[ProductId](#API_ProvisionProduct_RequestSyntax "#API_ProvisionProduct_RequestSyntax")**

The product identifier. You must provide the name or ID, but not both.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 100.

Pattern: `^[a-zA-Z0-9_\-]*`

Required: No

**[ProductName](#API_ProvisionProduct_RequestSyntax "#API_ProvisionProduct_RequestSyntax")**

The name of the product. You must provide the name or ID, but not both.

Type: String

Length Constraints: Maximum length of 8191.

Required: No

**[ProvisionedProductName](#API_ProvisionProduct_RequestSyntax "#API_ProvisionProduct_RequestSyntax")**

A user-friendly name for the provisioned product. This value must be
unique for the AWS account and cannot be updated after the product is provisioned.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 128.

Pattern: `[a-zA-Z0-9][a-zA-Z0-9._-]*`

Required: Yes

**[ProvisioningArtifactId](#API_ProvisionProduct_RequestSyntax "#API_ProvisionProduct_RequestSyntax")**

The identifier of the provisioning artifact. You must provide the name or ID, but not both.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 100.

Pattern: `^[a-zA-Z0-9_\-]*`

Required: No

**[ProvisioningArtifactName](#API_ProvisionProduct_RequestSyntax "#API_ProvisionProduct_RequestSyntax")**

The name of the provisioning artifact. You must provide the name or ID, but not both.

Type: String

Length Constraints: Maximum length of 8192.

Required: No

**[ProvisioningParameters](#API_ProvisionProduct_RequestSyntax "#API_ProvisionProduct_RequestSyntax")**

Parameters specified by the administrator that are required for provisioning the
product.

Type: Array of [ProvisioningParameter](API_ProvisioningParameter.md "API_ProvisioningParameter.md") objects

Required: No

**[ProvisioningPreferences](#API_ProvisionProduct_RequestSyntax "#API_ProvisionProduct_RequestSyntax")**

An object that contains information about the provisioning preferences for a stack set.

Type: [ProvisioningPreferences](API_ProvisioningPreferences.md "API_ProvisioningPreferences.md") object

Required: No

**[ProvisionToken](#API_ProvisionProduct_RequestSyntax "#API_ProvisionProduct_RequestSyntax")**

An idempotency token that uniquely identifies the provisioning request.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 128.

Pattern: `[a-zA-Z0-9][a-zA-Z0-9_-]*`

Required: Yes

**[Tags](#API_ProvisionProduct_RequestSyntax "#API_ProvisionProduct_RequestSyntax")**

One or more tags.

Type: Array of [Tag](API_Tag.md "API_Tag.md") objects

Array Members: Maximum number of 50 items.

Required: No

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

**[RecordDetail](#API_ProvisionProduct_ResponseSyntax "#API_ProvisionProduct_ResponseSyntax")**

Information about the result of provisioning the product.

Type: [RecordDetail](API_RecordDetail.md "API_RecordDetail.md") object

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

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS Command Line Interface V2](../../../goto/cli2/servicecatalog-2015-12-10/ProvisionProduct.md "../../../goto/cli2/servicecatalog-2015-12-10/ProvisionProduct.md")
- [AWS SDK for .NET](../../../goto/DotNetSDKV3/servicecatalog-2015-12-10/ProvisionProduct.md "../../../goto/DotNetSDKV3/servicecatalog-2015-12-10/ProvisionProduct.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/servicecatalog-2015-12-10/ProvisionProduct.md "../../../goto/SdkForCpp/servicecatalog-2015-12-10/ProvisionProduct.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/servicecatalog-2015-12-10/ProvisionProduct.md "../../../goto/SdkForGoV2/servicecatalog-2015-12-10/ProvisionProduct.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/servicecatalog-2015-12-10/ProvisionProduct.md "../../../goto/SdkForJavaV2/servicecatalog-2015-12-10/ProvisionProduct.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/servicecatalog-2015-12-10/ProvisionProduct.md "../../../goto/SdkForJavaScriptV3/servicecatalog-2015-12-10/ProvisionProduct.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/servicecatalog-2015-12-10/ProvisionProduct.md "../../../goto/SdkForKotlin/servicecatalog-2015-12-10/ProvisionProduct.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/servicecatalog-2015-12-10/ProvisionProduct.md "../../../goto/SdkForPHPV3/servicecatalog-2015-12-10/ProvisionProduct.md")
- [AWS SDK for Python](../../../goto/boto3/servicecatalog-2015-12-10/ProvisionProduct.md "../../../goto/boto3/servicecatalog-2015-12-10/ProvisionProduct.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/servicecatalog-2015-12-10/ProvisionProduct.md "../../../goto/SdkForRubyV3/servicecatalog-2015-12-10/ProvisionProduct.md")
