# TextEvent

Contains text content to be synthesized into speech.

## Contents

**Text**

The text content to synthesize. If you specify `ssml` as the
`TextType`, follow the SSML format for the input text.

Type: String

Required: Yes

**FlushStreamConfiguration**

Configuration for controlling when synthesized audio flushes to the output stream.

Type: [FlushStreamConfiguration](API_FlushStreamConfiguration.md "API_FlushStreamConfiguration.md") object

Required: No

**TextType**

Specifies whether the input text is plain text or SSML. Default: plain text.

Type: String

Valid Values: `ssml | text`

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/polly-2016-06-10/TextEvent.md "../../../goto/SdkForCpp/polly-2016-06-10/TextEvent.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/polly-2016-06-10/TextEvent.md "../../../goto/SdkForJavaV2/polly-2016-06-10/TextEvent.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/polly-2016-06-10/TextEvent.md "../../../goto/SdkForRubyV3/polly-2016-06-10/TextEvent.md")
