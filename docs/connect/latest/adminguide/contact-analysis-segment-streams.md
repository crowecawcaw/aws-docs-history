# Access Contact Lens

analytics for voice and chat contacts using Amazon Kinesis Data Streams

Contact analysis segment streams enable you to access Contact Lens
analytics in for voice and chat contacts. Streaming overcomes the scaling
limitations of existing [call and chat analytics
APIs](contact-lens-api.md "contact-lens-api.md"). For voice contacts, it also provides access to a data segment
called `Utterance` that allows you to access partial transcripts. This
enables you to meet ultra-low latency requirements to assist agents on live calls.

This section explains how to integrate with Amazon Kinesis Data Streams for streaming.

Through streaming, you can receive the following event types:

- STARTED events published at the beginning of a contact analysis
  session.
- SEGMENTS events published during the contact analysis sessions. These
  events contain a list of segments with analyzed information.
- COMPLETED or FAILED events published at the end of a contact analysis
  session.

###### Contents

- [Enable
  contact analysis segment streams](enable-contact-analysis-segment-streams.md "enable-contact-analysis-segment-streams.md")
- [Voice: Data model for conversational analytics segment streams](real-time-contact-analysis-segment-streams-data-model.md "real-time-contact-analysis-segment-streams-data-model.md")
- [Chat: Data model for conversational analytics segment streams](chat-real-time-contact-analysis-segment-streams-data-model.md "chat-real-time-contact-analysis-segment-streams-data-model.md")
- [Voice: Sample conversational analytics segment stream](sample-real-time-contact-analysis-segment-stream.md "sample-real-time-contact-analysis-segment-stream.md")
- [Chat:
  Sample conversational analytics segment stream](chat-sample-real-time-contact-analysis-segment-stream.md "chat-sample-real-time-contact-analysis-segment-stream.md")
