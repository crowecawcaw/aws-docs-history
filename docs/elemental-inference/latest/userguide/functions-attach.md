

# Attaching a function to a feed

You attach a function to a feed by adding a *function output* to the feed, in the same way that you add an output for any other feature. The following table lists the fields of a function output.


| Field | Required | Description | 
| --- | --- | --- | 
| name | Yes | The name of the output. This is the name you pass to GetMetadata to read results, so choose something stable and meaningful. | 
| functionArn | Yes | The ARN of the function to run. The function must exist in the same account as the feed. | 
| trigger | Yes | Exactly one of fixedInterval, perShot, perScene, or perClip. For more information, see [Triggers](functions-triggers.md). | 
| trigger.fixedInterval.intervalSeconds | With fixedInterval | 1 through 60 seconds of content. | 
| frameSettings.frameSampling | With frameSettings | mode is FIRST, UNIFORM, or LAST: frames from the start, spaced evenly, or from the end. count is the number of frames, 1 through 64, in every mode. Applies to a function that reads media.frames. Default: UNIFORM, 1 frame. | 
| frameSettings.frameSize | No | widthPixels, 1 through 1280, and heightPixels, 1 through 720. Both are required. Elemental Inference resizes each sampled frame to exactly this size, so a size off the 16:9 aspect ratio stretches the frame. Smaller frames let one request carry more of them. Default: frames keep their native 1280 x 720 size. | 
| subtitlingSettings.outputName | For transcript functions | The name of an enabled smart subtitles output on this feed, to source media.transcript from. | 
| contextualMetadataSettings.outputName | For perScene, and for contextual functions on perShot | The name of an enabled contextual metadata output on this feed. | 
| clippingSettings.outputName | For perClip, and for clip functions on fixedInterval | The name of an enabled event clipping output on this feed. | 

Elemental Inference ignores settings for context that the function doesn't read, rather than rejecting them, so you can leave them out.

**Note**  
Sampling controls cost as much as it controls quality. Each frame is part of the request that the model charges you for. Two frames are often enough to show what is on screen; 20 frames of a one-second window are mostly the same picture.

**Topics**
+ [Attaching a function using the console](functions-attach-console.md)
+ [Attaching a function using the CLI](functions-attach-cli.md)
+ [Rules that Elemental Inference checks when you attach a function](functions-attach-rules.md)