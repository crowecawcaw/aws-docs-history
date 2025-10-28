# ProvisionedProductPlanDetails

Information about a plan.

## Contents

**CreatedTime**

The UTC time stamp of the creation time.

Type: Timestamp

Required: No

**NotificationArns**

Passed to AWS CloudFormation. The SNS topic ARNs to which to publish stack-related
events.

Type: Array of strings

Array Members: Maximum number of 5 items.

Length Constraints: Minimum length of 1. Maximum length of 1224.

Pattern: `arn:[a-z0-9-\.]{1,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[a-z0-9-\.]{0,63}:[^/].{0,1023}`

Required: No

**PathId**

The path identifier of the product. This value is optional if the product
has a default path, and required if the product has more than one path.
To list the paths for a product, use [ListLaunchPaths](API_ListLaunchPaths.md "API_ListLaunchPaths.md").

Type: String

Length Constraints: Minimum length of 1. Maximum length of 100.

Pattern: `^[a-zA-Z0-9_\-]*`

Required: No

**PlanId**

The plan identifier.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 100.

Pattern: `^[a-zA-Z0-9_\-]*`

Required: No

**PlanName**

The name of the plan.

Type: String

Required: No

**PlanType**

The plan type.

Type: String

Valid Values: `CLOUDFORMATION`

Required: No

**ProductId**

The product identifier.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 100.

Pattern: `^[a-zA-Z0-9_\-]*`

Required: No

**ProvisioningArtifactId**

The identifier of the provisioning artifact.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 100.

Pattern: `^[a-zA-Z0-9_\-]*`

Required: No

**ProvisioningParameters**

Parameters specified by the administrator that are required for provisioning the
product.

Type: Array of [UpdateProvisioningParameter](API_UpdateProvisioningParameter.md "API_UpdateProvisioningParameter.md") objects

Required: No

**ProvisionProductId**

The product identifier.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 100.

Pattern: `^[a-zA-Z0-9_\-]*`

Required: No

**ProvisionProductName**

The user-friendly name of the provisioned product.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 128.

Pattern: `[a-zA-Z0-9][a-zA-Z0-9._-]*`

Required: No

**Status**

The status.

Type: String

Valid Values: `CREATE_IN_PROGRESS | CREATE_SUCCESS | CREATE_FAILED | EXECUTE_IN_PROGRESS | EXECUTE_SUCCESS | EXECUTE_FAILED`

Required: No

**StatusMessage**

The status message.

Type: String

Pattern: `[\u0009\u000a\u000d\u0020-\uD7FF\uE000-\uFFFD]*`

Required: No

**Tags**

One or more tags.

Type: Array of [Tag](API_Tag.md "API_Tag.md") objects

Array Members: Maximum number of 50 items.

Required: No

**UpdatedTime**

The UTC time stamp when the plan was last updated.

Type: Timestamp

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/servicecatalog-2015-12-10/ProvisionedProductPlanDetails.md "../../../goto/SdkForCpp/servicecatalog-2015-12-10/ProvisionedProductPlanDetails.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/servicecatalog-2015-12-10/ProvisionedProductPlanDetails.md "../../../goto/SdkForJavaV2/servicecatalog-2015-12-10/ProvisionedProductPlanDetails.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/servicecatalog-2015-12-10/ProvisionedProductPlanDetails.md "../../../goto/SdkForRubyV3/servicecatalog-2015-12-10/ProvisionedProductPlanDetails.md")
