

# Using functions with AWS Elemental MediaLive

When AWS Elemental MediaLive is the source of your media, you set up the function on the Elemental Inference side and give MediaLive only the ARN of the feed. MediaLive has no function settings: its **AWS Elemental Inference** section covers event clipping, smart crop, smart subtitles, and contextual metadata, and MediaLive neither creates nor reads function outputs.

The following table shows that division of work.


| Where | What you do | 
| --- | --- | 
| In Elemental Inference | Create the function. Create the feed, or reuse the channel's existing feed. Set the access role. Add the function output, plus any smart subtitles, contextual metadata, or event clipping output that the function reads from. | 
| In MediaLive | Point the channel at the feed. Deliver the source stream. | 
| In your application | Read the results with GetMetadata on the feed's data endpoint. | 

**Topics**
+ [Setting up with the MediaLive console](functions-medialive-console.md)
+ [Setting up with the MediaLive API or CLI](functions-medialive-cli.md)
+ [Considerations for functions with MediaLive](functions-medialive-notes.md)