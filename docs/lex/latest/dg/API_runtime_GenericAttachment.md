End of support notice: On September 15, 2025, AWS
will discontinue support for Amazon Lex V1. After September 15, 2025, you will
no longer be able to access the Amazon Lex V1 console or Amazon Lex V1 resources. If you are using Amazon Lex V2, refer to the [Amazon Lex V2 guide](../../../lexv2/latest/dg/what-is.md "../../../lexv2/latest/dg/what-is.md") instead.
.

# GenericAttachment

Represents an option rendered to the user when a prompt is shown. It
could be an image, a button, a link, or text.

## Contents

**attachmentLinkUrl**

The URL of an attachment to the response card.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 2048.

Required: No

**buttons**

The list of options to show to the user.

Type: Array of [Button](API_runtime_Button.md "API_runtime_Button.md") objects

Array Members: Minimum number of 0 items. Maximum number of 5 items.

Required: No

**imageUrl**

The URL of an image that is displayed to the user.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 2048.

Required: No

**subTitle**

The subtitle shown below the title.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 80.

Required: No

**title**

The title of the option.

Type: String

Length Constraints: Minimum length of 1. Maximum length of 80.

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/runtime.lex-2016-11-28/GenericAttachment.md "../../../goto/SdkForCpp/runtime.lex-2016-11-28/GenericAttachment.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/runtime.lex-2016-11-28/GenericAttachment.md "../../../goto/SdkForJavaV2/runtime.lex-2016-11-28/GenericAttachment.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/runtime.lex-2016-11-28/GenericAttachment.md "../../../goto/SdkForRubyV3/runtime.lex-2016-11-28/GenericAttachment.md")
