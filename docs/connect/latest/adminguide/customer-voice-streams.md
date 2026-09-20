

# Set up live media streaming of customer audio in Connect Customer
<a name="customer-voice-streams"></a>

In Connect Customer, you can capture customer audio during an interaction with your contact center by sending the audio to a Kinesis video stream. Depending on your settings, audio can be captured for the entire interaction—until the interaction with the agent is complete—or only one direction: 
+ What the customer hears, including what the agent says and system prompts.
+ What the customer says, including when they are on hold.

The customer audio streams also include interactions with an Amazon Lex bot, if you're using one in your flow. 

**Topics**
+ [Plan for live media streaming from Connect Customer to Kinesis Video Streams](plan-live-media-streams.md)
+ [Enable live media streaming in your Connect Customer instance](enable-live-media-streams.md)
+ [Develop live media streaming in Connect Customer](access-media-stream-data.md)
+ [Example flow for testing live media streaming in Connect Customer](use-media-streams-blocks.md)
+ [Contact attributes for live media streaming in Kinesis Video Streams](media-streaming-attributes.md)