

# Using functions with AWS Elemental MediaLive
<a name="functions-medialive"></a>

When AWS Elemental MediaLive is the source of your media, you set up the function on the Elemental Inference side and give MediaLive only the ARN of the feed. MediaLive has no function settings: its **AWS Elemental Inference** section covers event clipping, smart crop, smart subtitles, and contextual metadata, and MediaLive neither creates nor reads function outputs.

That division of work looks like this.


| Where | What you do | 
| --- | --- | 
| In Elemental Inference | Create the function. Create the feed, or reuse the channel's existing feed. Set the access role. Add the function output, plus any smart subtitles, contextual metadata, or event clipping output that the function reads from. | 
| In MediaLive | Point the channel at the feed, and deliver the source stream. | 
| In your application | Read the results with GetMetadata on the feed's data endpoint. | 

**Topics**
+ [Setting up with the MediaLive console](functions-medialive-console.md)
+ [Setting up with the MediaLive API or CLI](functions-medialive-cli.md)
+ [Points to watch](functions-medialive-notes.md)