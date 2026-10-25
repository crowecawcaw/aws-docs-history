

# Attaching a function to a feed
<a name="functions-attach"></a>

You attach a function to a feed by adding a *function output* to the feed, in the same way that you add an output for any other feature. The output holds the following.


| Field | Required | Description | 
| --- | --- | --- | 
| name | Yes | The name of the output. This is the name you pass to GetMetadata to read results, so choose something stable and meaningful. | 
| functionArn | Yes | The ARN of the function to run. The function must exist in the same account as the feed. | 
| trigger | Yes | Exactly one of fixedInterval, perShot, perScene, or perClip. See [Triggers](functions-triggers.md). | 
| trigger.fixedInterval.intervalSeconds | With fixedInterval | 1 through 60 seconds of content. | 
| frameSettings.frameSampling | With frameSettings | mode is FIRST, UNIFORM, or LAST: frames from the start, spaced evenly, or from the end. count is the number of frames, 1 through 64, in every mode. Applies to a function that reads media.frames. Default: UNIFORM, 1 frame. | 
| frameSettings.frameSize | No | widthPixels, 1 through 1280, and heightPixels, 1 through 720. Both are required. Elemental Inference resizes each sampled frame to exactly this size, so a size off the 16:9 aspect ratio stretches the frame. Smaller frames let one request carry more of them. Default: frames keep their native 1280 x 720 size. | 
| videoSettings.fragmentSampling | With videoSettings | mode is FIRST, UNIFORM, or LAST. count is the number of fragments, 1 through 16, in every mode. Applies to a function that reads media.video. Default: FIRST, 1 fragment. | 
| subtitlingSettings.outputName | For transcript functions | The name of an enabled smart subtitles output on this feed, to source media.transcript from. | 
| contextualMetadataSettings.outputName | For perScene, and for contextual functions on perShot | The name of an enabled contextual metadata output on this feed. | 
| clippingSettings.outputName | For perClip, and for clip functions on fixedInterval | The name of an enabled event clipping output on this feed. | 

Settings for context that the function doesn't read are ignored rather than rejected, so you can leave them out.

**Note**  
Sampling controls cost as much as it controls quality. Each frame and each fragment is part of the request that the model is charged for. Two frames are often enough to answer "what is on screen"; 20 frames of a one-second window are mostly the same picture.

**Topics**
+ [Attaching a function using the console](functions-attach-console.md)
+ [Attaching a function using the CLI](functions-attach-cli.md)
+ [Rules that Elemental Inference checks when you attach a function](functions-attach-rules.md)