# ResourceChangeDetail

Information about a change to a resource attribute.

## Contents

**CausingEntity**

The ID of the entity that caused the change.

Type: String

Required: No

**Evaluation**

For static evaluations, the value of the resource attribute will change and the new value is known.
For dynamic evaluations, the value might change, and any new value will be determined when the plan is updated.

Type: String

Valid Values: `STATIC | DYNAMIC`

Required: No

**Target**

Information about the resource attribute to be modified.

Type: [ResourceTargetDefinition](API_ResourceTargetDefinition.md "API_ResourceTargetDefinition.md") object

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/servicecatalog-2015-12-10/ResourceChangeDetail.md "../../../goto/SdkForCpp/servicecatalog-2015-12-10/ResourceChangeDetail.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/servicecatalog-2015-12-10/ResourceChangeDetail.md "../../../goto/SdkForJavaV2/servicecatalog-2015-12-10/ResourceChangeDetail.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/servicecatalog-2015-12-10/ResourceChangeDetail.md "../../../goto/SdkForRubyV3/servicecatalog-2015-12-10/ResourceChangeDetail.md")
