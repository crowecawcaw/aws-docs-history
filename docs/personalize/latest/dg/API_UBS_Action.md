# Action

Represents action metadata added to an Action dataset using the
`PutActions` API. For more information see
[Importing actions individually](importing-actions.md "importing-actions.md").

## Contents

**actionId**

The ID associated with the action.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 256.

Required: Yes

**properties**

A string map of action-specific metadata. Each element in the map consists of a key-value pair.
For example, `{"value": "100"}`.

The keys use camel case names that match the fields in the schema for the Actions
dataset. In the previous example, the `value` matches the
'VALUE' field defined in the Actions schema. For categorical string data, to include multiple categories for a single action,
separate each category with a pipe separator (`|`). For example, `\"Deluxe|Premium\"`.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 32000.

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/personalize-events-2018-03-22/Action.md "../../../goto/SdkForCpp/personalize-events-2018-03-22/Action.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/personalize-events-2018-03-22/Action.md "../../../goto/SdkForJavaV2/personalize-events-2018-03-22/Action.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/personalize-events-2018-03-22/Action.md "../../../goto/SdkForRubyV3/personalize-events-2018-03-22/Action.md")
