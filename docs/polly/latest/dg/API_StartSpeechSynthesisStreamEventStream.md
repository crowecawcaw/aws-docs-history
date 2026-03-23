# StartSpeechSynthesisStreamEventStream

Outbound event stream that contains synthesized audio data and stream status events.

## Contents

**AudioEvent**

An audio event containing synthesized speech.

Type: [AudioEvent](API_AudioEvent.md "API_AudioEvent.md") object

Required: No

**ServiceFailureException**

An unknown condition has caused a service failure.

Type: Exception

HTTP Status Code: 500

Required: No

**ServiceQuotaExceededException**

An exception indicating a service quota would be exceeded.

Type: Exception

HTTP Status Code: 402

Required: No

**StreamClosedEvent**

An event, with summary information, indicating the stream has closed.

Type: [StreamClosedEvent](API_StreamClosedEvent.md "API_StreamClosedEvent.md") object

Required: No

**ThrottlingException**

An exception indicating the request was throttled.

Type: Exception

HTTP Status Code: 400

Required: No

**ValidationException**

An exception indicating the input failed validation.

Type: Exception

HTTP Status Code: 400

Required: No

## See Also

For more information about using this API in one of the language-specific AWS SDKs, see the following:

- [AWS SDK for C++](../../../goto/SdkForCpp/polly-2016-06-10/StartSpeechSynthesisStreamEventStream.md "../../../goto/SdkForCpp/polly-2016-06-10/StartSpeechSynthesisStreamEventStream.md")
- [AWS SDK for Java V2](../../../goto/SdkForJavaV2/polly-2016-06-10/StartSpeechSynthesisStreamEventStream.md "../../../goto/SdkForJavaV2/polly-2016-06-10/StartSpeechSynthesisStreamEventStream.md")
- [AWS SDK for Ruby V3](../../../goto/SdkForRubyV3/polly-2016-06-10/StartSpeechSynthesisStreamEventStream.md "../../../goto/SdkForRubyV3/polly-2016-06-10/StartSpeechSynthesisStreamEventStream.md")
