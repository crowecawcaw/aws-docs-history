# Item

Represents item metadata added to an Items dataset using the
`PutItems` API. For more information see
[Importing items individually](importing-items.md "importing-items.md").

## Contents

**itemId**

The ID associated with the item.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 256.

Required: Yes

**properties**

A string map of item-specific metadata. Each element in the map consists of a key-value pair.
For example, `{"numberOfRatings": "12"}`.

The keys use camel case names that match the fields in the schema for the Items
dataset. In the previous example, the `numberOfRatings` matches the
'NUMBER_OF_RATINGS' field defined in the Items schema. For categorical string data, to include multiple categories for a single item,
separate each category with a pipe separator (`|`). For example, `\"Horror|Action\"`.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 32000.

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/personalize-events-2018-03-22/Item.md "../../../goto/SdkForCpp/personalize-events-2018-03-22/Item.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/personalize-events-2018-03-22/Item.md "../../../goto/SdkForJavaV2/personalize-events-2018-03-22/Item.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/personalize-events-2018-03-22/Item.md "../../../goto/SdkForRubyV3/personalize-events-2018-03-22/Item.md")
