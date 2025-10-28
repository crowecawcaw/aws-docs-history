# ResourceChange

Information about a resource change that will occur when a plan is executed.

## Contents

**Action**

The change action.

Type: String

Valid Values: `ADD | MODIFY | REMOVE`

Required: No

**Details**

Information about the resource changes.

Type: Array of [ResourceChangeDetail](API_ResourceChangeDetail.md "API_ResourceChangeDetail.md") objects

Required: No

**LogicalResourceId**

The ID of the resource, as defined in the AWS CloudFormation template.

Type: String

Required: No

**PhysicalResourceId**

The ID of the resource, if it was already created.

Type: String

Required: No

**Replacement**

If the change type is `Modify`, indicates whether the existing resource
is deleted and replaced with a new one.

Type: String

Valid Values: `TRUE | FALSE | CONDITIONAL`

Required: No

**ResourceType**

The type of resource.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 256.

Required: No

**Scope**

The change scope.

Type: Array of strings

Valid Values: `PROPERTIES | METADATA | CREATIONPOLICY | UPDATEPOLICY | DELETIONPOLICY | TAGS`

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/servicecatalog-2015-12-10/ResourceChange.md "../../../goto/SdkForCpp/servicecatalog-2015-12-10/ResourceChange.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/servicecatalog-2015-12-10/ResourceChange.md "../../../goto/SdkForJavaV2/servicecatalog-2015-12-10/ResourceChange.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/servicecatalog-2015-12-10/ResourceChange.md "../../../goto/SdkForRubyV3/servicecatalog-2015-12-10/ResourceChange.md")
