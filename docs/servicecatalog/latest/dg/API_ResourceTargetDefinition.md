# ResourceTargetDefinition

Information about a change to a resource attribute.

## Contents

**Attribute**

The attribute to be changed.

Type: String

Valid Values: `PROPERTIES | METADATA | CREATIONPOLICY | UPDATEPOLICY | DELETIONPOLICY | TAGS`

Required: No

**Name**

If the attribute is `Properties`, the value is the name of the property.
Otherwise, the value is null.

Type: String

Required: No

**RequiresRecreation**

If the attribute is `Properties`, indicates whether a change to this property
causes the resource to be re-created.

Type: String

Valid Values: `NEVER | CONDITIONALLY | ALWAYS`

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/servicecatalog-2015-12-10/ResourceTargetDefinition.md "../../../goto/SdkForCpp/servicecatalog-2015-12-10/ResourceTargetDefinition.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/servicecatalog-2015-12-10/ResourceTargetDefinition.md "../../../goto/SdkForJavaV2/servicecatalog-2015-12-10/ResourceTargetDefinition.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/servicecatalog-2015-12-10/ResourceTargetDefinition.md "../../../goto/SdkForRubyV3/servicecatalog-2015-12-10/ResourceTargetDefinition.md")
