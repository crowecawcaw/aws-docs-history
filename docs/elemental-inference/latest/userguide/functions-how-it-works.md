

# How functions work
<a name="functions-how-it-works"></a>

Functions involve two resources.

The function  
An account-level resource, independent of any feed. It holds the **target** (an Amazon Bedrock model, or passthrough) and one or two **expressions** written in JSONata: a *request expression* that builds the request, and an optional *response expression* that picks the parts of the result you want to keep. One function can be attached to many feeds.

The function output on a feed  
A function does nothing until you attach it to a feed as an output, the same way you add a smart crop or subtitling output. The output holds the ARN of the function, the **trigger** that decides how often the function runs, and the settings for the media that the function reads. The **name** that you give the output is the name you pass to `GetMetadata` to read the results.  
A feed with an enabled function output must also have an enabled smart crop, event clipping, smart subtitles, or contextual metadata output.

At runtime, each time the trigger fires, Elemental Inference does the following:

1. Gathers the media and metadata for that window – for example, decodes video frames, remuxes a short video clip, or collects the transcript.

1. Evaluates your request expression to build the request body.

1. For a model target, assumes the feed's access role and calls `InvokeModel` in your account. For a passthrough target, skips this step.

1. Evaluates your response expression against the result. Without a response expression, the result is stored as it is.

1. Writes the value to the feed's metadata timeline, under the name of the function output, at the presentation timestamp (PTS) of the window.

**Note**  
You never encode media into an expression yourself. Elemental Inference supplies the media as context, and substitutes the encoded media into the request after your expression has been evaluated. For more information, see [Placing media in the request](functions-expressions-media.md).

Only successful runs produce metadata. If the decoded media is too large for the request, the model rejects the request, the model call times out, or the expression breaks a guardrail, Elemental Inference logs the cause and the window produces no metadata item. There is no partial or error-shaped item on the timeline. For more information about where those log entries appear, see [Troubleshooting functions](functions-troubleshooting.md).