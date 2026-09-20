

# Access conversational analytics for voice and chat contacts using Amazon Kinesis Data Streams
<a name="contact-analysis-segment-streams"></a>

With contact analysis segment streams, you can access conversational analytics for voice and chat contacts. Streaming overcomes the scaling limitations of existing [call and chat analytics APIs](contact-lens-api.md). For voice contacts, it also provides access to a data segment called `Utterance` that you can use to access partial transcripts. This helps you meet ultra-low latency requirements to assist agents on live calls. 

This section explains how to integrate with Amazon Kinesis Data Streams for streaming.

Through streaming, you can receive the following event types: 
+ STARTED events published at the beginning of a contact analysis session.
+ SEGMENTS events published during the contact analysis sessions. These events contain a list of segments with analyzed information.
+ COMPLETED or FAILED events published at the end of a contact analysis session.

**Topics**
+ [Enable contact analysis segment streams to analyze conversational analytics conversations](enable-contact-analysis-segment-streams.md)
+ [Data model for conversational analytics segment streams to analyze voice contacts in conversational analytics](real-time-contact-analysis-segment-streams-data-model.md)
+ [Data model for conversational analytics segment streams to analyze chats in conversational analytics](chat-real-time-contact-analysis-segment-streams-data-model.md)
+ [Sample conversational analytics segment streams to analyze calls using conversational analytics](sample-real-time-contact-analysis-segment-stream.md)
+ [Sample conversational analytics streams to analyze chats in conversational analytics](chat-sample-real-time-contact-analysis-segment-stream.md)