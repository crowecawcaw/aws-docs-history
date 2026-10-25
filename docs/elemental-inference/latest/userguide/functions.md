

# Using functions in Elemental Inference
<a name="functions"></a>

The other Elemental Inference features — smart crop, event clipping, smart subtitles, and contextual metadata — produce a fixed set of metadata. For information about configuring them, see [Configuring each feature](create-feed-outputs.md). A *function* lets you add your own analysis to the same feed, and read the result from the same metadata timeline.

You define a function once, in your own account, and attach it to any number of feeds in that account. On each attachment you choose how often the function runs. Elemental Inference gathers the media and metadata that your function asks for, builds a request from your instructions, optionally sends that request to a model in *your* Amazon Bedrock account, shapes the result, and writes it to the feed's metadata timeline next to the native metadata. You retrieve it with the same `GetMetadata` operation that you already use.

A function can do one of two things with the request it builds:
+ **Invoke a model** – the request goes to an Amazon Bedrock model that you choose. The model runs in your account under a role that you control, so the model choice, the model access grants, the throughput quotas, and the charges are all yours.
+ **Invoke nothing** – a *passthrough* function sends the request nowhere. It reshapes the metadata that Elemental Inference already produced into your own schema, at no model cost. Use it when you want the existing metadata in a different shape rather than a new analysis.

Functions do not affect the rest of the feed. If a function fails, the feed's other outputs continue normally and the timeline has no function metadata for that window.

**Topics**
+ [How functions work](functions-how-it-works.md)
+ [What a function can read](functions-context.md)
+ [Triggers](functions-triggers.md)
+ [Costs and throughput](functions-costs.md)
+ [Prerequisites for functions](functions-prerequisites.md)
+ [Creating a function](functions-create.md)
+ [Attaching a function to a feed](functions-attach.md)
+ [Reading function results](functions-metadata.md)
+ [Writing function expressions](functions-expressions.md)
+ [JSONata reference for functions](functions-jsonata.md)
+ [Example functions](functions-examples.md)
+ [Managing existing functions](functions-managing.md)
+ [Using functions with AWS Elemental MediaLive](functions-medialive.md)
+ [Quotas and limits for functions](functions-quotas.md)
+ [Troubleshooting functions](functions-troubleshooting.md)