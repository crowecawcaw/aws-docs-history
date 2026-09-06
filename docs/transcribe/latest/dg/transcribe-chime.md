

# Transcribing your Amazon Chime calls in real time
<a name="transcribe-chime"></a>

Amazon Transcribe is integrated with the Amazon Chime SDK, facilitating real-time transcriptions of your Amazon Chime calls.

When you request a transcription using the Amazon Chime SDK API, Amazon Chime begins streaming audio to Amazon Transcribe and continues to do so for the duration of the call.

The Amazon Chime SDK uses its 'active talker' algorithm to select the top two active talkers, and then sends their audio to Amazon Transcribe as two separate channels via a single stream. Meeting participants receive user-attributed transcriptions via Amazon Chime SDK data messages. You can view delivery examples in the *[Amazon Chime SDK Developer Guide](https://docs.aws.amazon.com/chime-sdk/latest/dg/delivery-examples.html)*.

The data flow of an Amazon Chime transcription is depicted in the following diagram:

![Data flow schematic for Amazon Chime SDK transcriptions.](http://docs.aws.amazon.com/transcribe/latest/dg/images/chime-transcribe-architecture.png)


For additional information and detailed instructions on how to set up real-time Amazon Chime transcriptions, refer to [Using Amazon Chime SDK live transcription](https://docs.aws.amazon.com/chime-sdk/latest/dg/meeting-transcription.html) in the *Amazon Chime SDK Developer Guide*. For API operations, refer to the [*Amazon Chime SDK API Reference*](https://docs.aws.amazon.com/chime-sdk/latest/APIReference/API_meeting-chime_StartMeetingTranscription.html).

**Dive deeper with the AWS Machine Learning Blog**  
To learn more about improving accuracy with real-time transcriptions, see:  
[Amazon Chime SDK meetings now support live transcription with Amazon Transcribe and Amazon Transcribe Medical](https://aws.amazon.com/about-aws/whats-new/2021/08/amazon-chime-sdk-amazon-transcribe-amazon-transcribe-medical/)
[Amazon Chime SDK for Telemedicine Solution](https://aws.amazon.com/blogs/industries/chime-sdk-for-telemedicine-solution/)