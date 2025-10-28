# CreateProvisionedProductPlan

Creates a plan.

A plan includes the list of resources to be
created (when provisioning a new product) or modified (when updating a provisioned product)
when the plan is executed.

You can create one plan for each provisioned product. To create a plan for an existing
provisioned product, the product status must be AVAILABLE or TAINTED.

To view the resource changes in the change set, use [DescribeProvisionedProductPlan](API_DescribeProvisionedProductPlan.md "API_DescribeProvisionedProductPlan.md").
To create or modify the provisioned product, use [ExecuteProvisionedProductPlan](API_ExecuteProvisionedProductPlan.md "API_ExecuteProvisionedProductPlan.md").

## Request Syntax

```
{
   "AcceptLanguage": "`string`",
   "IdempotencyToken": "`string`",
   "NotificationArns": [ "`string`" ],
   "PathId": "`string`",
   "PlanName": "`string`",
   "PlanType": "`string`",
   "ProductId": "`string`",
   "ProvisionedProductName": "`string`",
   "ProvisioningArtifactId": "`string`",
   "ProvisioningParameters": [
      {
         "Key": "`string`",
         "UsePreviousValue": `boolean`,
         "Value": "`string`"
      }
   ],
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

**[AcceptLanguage](#API_CreateProvisionedProductPlan_RequestSyntax "#API_CreateProvisionedProductPlan_RequestSyntax")**

The language code.

- `jp` - Japanese
- `zh` - Chinese

Type: String

Length Constraints: Maximum length of 100.

Required: No

**[IdempotencyToken](#API_CreateProvisionedProductPlan_RequestSyntax "#API_CreateProvisionedProductPlan_RequestSyntax")**

A unique identifier that you provide to ensure idempotency. If multiple requests differ only by the idempotency token,
the same response is returned for each repeated request.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 128.

Pattern: `[a-zA-Z0-9][a-zA-Z0-9_-]*`

Required: Yes

**[NotificationArns](#API_CreateProvisionedProductPlan_RequestSyntax "#API_CreateProvisionedProductPlan_RequestSyntax")**

Passed to AWS CloudFormation. The SNS topic ARNs to which to publish stack-related
events.

Type: Array of strings

Array Members: Maximum number of 5 items.

Length Constraints: Minimum length of 1. Maximum length of 1224.

Pattern: `arn:[a-z0-9-\.]{1,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[^/].{0,1023}`

Required: No

**[PathId](#API_CreateProvisionedProductPlan_RequestSyntax "#API_CreateProvisionedProductPlan_RequestSyntax")**

The path identifier of the product. This value is optional if the product
has a default path, and required if the product has more than one path.
To list the paths for a product, use [ListLaunchPaths](API_ListLaunchPaths.md "API_ListLaunchPaths.md").

Type: String

Length Constraints: Minimum length of 1. Maximum length of 100.

Pattern: `^[a-zA-Z0-9_\-]*`

Required: No

**[PlanName](#API_CreateProvisionedProductPlan_RequestSyntax "#API_CreateProvisionedProductPlan_RequestSyntax")**

The name of the plan.

Type: String

Required: Yes

**[PlanType](#API_CreateProvisionedProductPlan_RequestSyntax "#API_CreateProvisionedProductPlan_RequestSyntax")**

The plan type.

Type: String

Valid Values: `CLOUDFORMATION`

Required: Yes

**[ProductId](#API_CreateProvisionedProductPlan_RequestSyntax "#API_CreateProvisionedProductPlan_RequestSyntax")**

The product identifier.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 100.

Pattern: `^[a-zA-Z0-9_\-]*`

Required: Yes

**[ProvisionedProductName](#API_CreateProvisionedProductPlan_RequestSyntax "#API_CreateProvisionedProductPlan_RequestSyntax")**

A user-friendly name for the provisioned product. This value must be
unique for the AWS account and cannot be updated after the product is provisioned.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 128.

Pattern: `[a-zA-Z0-9][a-zA-Z0-9._-]*`

Required: Yes

**[ProvisioningArtifactId](#API_CreateProvisionedProductPlan_RequestSyntax "#API_CreateProvisionedProductPlan_RequestSyntax")**

The identifier of the provisioning artifact.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 100.

Pattern: `^[a-zA-Z0-9_\-]*`

Required: Yes

**[ProvisioningParameters](#API_CreateProvisionedProductPlan_RequestSyntax "#API_CreateProvisionedProductPlan_RequestSyntax")**

Parameters specified by the administrator that are required for provisioning the
product.

Type: Array of [UpdateProvisioningParameter](API_UpdateProvisioningParameter.md "API_UpdateProvisioningParameter.md") objects

Required: No

**[Tags](#API_CreateProvisionedProductPlan_RequestSyntax "#API_CreateProvisionedProductPlan_RequestSyntax")**

One or more tags.

If the plan is for an existing provisioned product, the product must have a `RESOURCE_UPDATE` constraint with `TagUpdatesOnProvisionedProduct` set to `ALLOWED` to allow tag updates.

Type: Array of [Tag](API_Tag.md "API_Tag.md") objects

Array Members: Maximum number of 50 items.

Required: No

## Response Syntax

```
{
   "PlanId": "***string***",
   "PlanName": "***string***",
   "ProvisionedProductName": "***string***",
   "ProvisioningArtifactId": "***string***",
   "ProvisionProductId": "***string***"
}
```

## Response Elements

If the action is successful, the service sends back an HTTP 200 response.

The following data is returned in JSON format by the service.

**[PlanId](#API_CreateProvisionedProductPlan_ResponseSyntax "#API_CreateProvisionedProductPlan_ResponseSyntax")**

The plan identifier.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 100.

Pattern: `^[a-zA-Z0-9_\-]*`

**[PlanName](#API_CreateProvisionedProductPlan_ResponseSyntax "#API_CreateProvisionedProductPlan_ResponseSyntax")**

The name of the plan.

Type: String

**[ProvisionedProductName](#API_CreateProvisionedProductPlan_ResponseSyntax "#API_CreateProvisionedProductPlan_ResponseSyntax")**

The user-friendly name of the provisioned product.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 128.

Pattern: `[a-zA-Z0-9][a-zA-Z0-9._-]*`

**[ProvisioningArtifactId](#API_CreateProvisionedProductPlan_ResponseSyntax "#API_CreateProvisionedProductPlan_ResponseSyntax")**

The identifier of the provisioning artifact.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 100.

Pattern: `^[a-zA-Z0-9_\-]*`

**[ProvisionProductId](#API_CreateProvisionedProductPlan_ResponseSyntax "#API_CreateProvisionedProductPlan_ResponseSyntax")**

The product identifier.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 100.

Pattern: `^[a-zA-Z0-9_\-]*`

## Errors

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

- [AWS Command Line Interface V2](../../../goto/cli2/servicecatalog-2015-12-10/CreateProvisionedProductPlan.md "../../../goto/cli2/servicecatalog-2015-12-10/CreateProvisionedProductPlan.md")
- [AWS SDK for .NET](../../../goto/DotNetSDKV3/servicecatalog-2015-12-10/CreateProvisionedProductPlan.md "../../../goto/DotNetSDKV3/servicecatalog-2015-12-10/CreateProvisionedProductPlan.md")
- [AWS SDK for C++](../../../goto/SdkForCpp/servicecatalog-2015-12-10/CreateProvisionedProductPlan.md "../../../goto/SdkForCpp/servicecatalog-2015-12-10/CreateProvisionedProductPlan.md")
- [AWS SDK for Go v2](../../../goto/SdkForGoV2/servicecatalog-2015-12-10/CreateProvisionedProductPlan.md "../../../goto/SdkForGoV2/servicecatalog-2015-12-10/CreateProvisionedProductPlan.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/servicecatalog-2015-12-10/CreateProvisionedProductPlan.md "../../../goto/SdkForJavaV2/servicecatalog-2015-12-10/CreateProvisionedProductPlan.md")
- [AWS SDK for JavaScript V3](../../../goto/SdkForJavaScriptV3/servicecatalog-2015-12-10/CreateProvisionedProductPlan.md "../../../goto/SdkForJavaScriptV3/servicecatalog-2015-12-10/CreateProvisionedProductPlan.md")
- [AWS SDK for Kotlin](../../../goto/SdkForKotlin/servicecatalog-2015-12-10/CreateProvisionedProductPlan.md "../../../goto/SdkForKotlin/servicecatalog-2015-12-10/CreateProvisionedProductPlan.md")
- [AWS SDK for PHP V3](../../../goto/SdkForPHPV3/servicecatalog-2015-12-10/CreateProvisionedProductPlan.md "../../../goto/SdkForPHPV3/servicecatalog-2015-12-10/CreateProvisionedProductPlan.md")
- [AWS SDK for Python](../../../goto/boto3/servicecatalog-2015-12-10/CreateProvisionedProductPlan.md "../../../goto/boto3/servicecatalog-2015-12-10/CreateProvisionedProductPlan.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/servicecatalog-2015-12-10/CreateProvisionedProductPlan.md "../../../goto/SdkForRubyV3/servicecatalog-2015-12-10/CreateProvisionedProductPlan.md")
