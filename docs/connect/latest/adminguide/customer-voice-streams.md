

# Set up live media streaming of customer audio in Connect Customer
<a name="customer-voice-streams"></a>

In Connect Customer, you can capture customer audio during an interaction with your contact center by sending the audio to a Kinesis video stream. Depending on your settings, audio can be captured for the entire interaction—until the interaction with the agent is complete—or only one direction: 
+ What the customer hears, including what the agent says and system prompts.
+ What the customer says, including when they are on hold.

The customer audio streams also include interactions with an Amazon Lex bot, if you're using one in your flow. 

**Topics**
+ [Plan for live media streaming](plan-live-media-streams.md)
+ [Enable live media streaming](enable-live-media-streams.md)
+ [Access Kinesis Video Streams Data](access-media-stream-data.md)
+ [Test live media streaming](use-media-streams-blocks.md)
+ [Contact attributes for live media streaming](media-streaming-attributes.md)