

# Rules that Elemental Inference checks when you attach a function
<a name="functions-attach-rules"></a>

Elemental Inference rejects an attachment that it can't run, at the time you save the feed rather than at the time the function would first fire. The following table lists the rules.


| Rule | Why | 
| --- | --- | 
| The function must exist, and must be in the same account as the feed. | A feed can't reference a function in another account. | 
| A function with a model target requires the feed to have an access role. | Elemental Inference assumes that role to invoke the model. A passthrough function needs none. | 
| A function that reads media.transcript must use fixedInterval, and must name an enabled smart subtitles output on this feed. | The transcript comes from that output. The transcript isn't available on the boundary triggers. | 
| A function that reads media.contextual must use perScene or perShot. A perScene trigger, and a function that reads media.contextual on perShot, must name an enabled contextual metadata output on this feed. | The scene boundaries and the contextual classification come from that output, and the classification is available only on those triggers. | 
| A function that reads media.clip must use perClip or fixedInterval. A perClip trigger, and a function that reads media.clip on fixedInterval, must name an enabled event clipping output on this feed. | The clips come from that output. | 
| The frames and video that the attachment would send must fit one model request. | Reduce the frame count, the fragment count, or both. | 
| The number of enabled function outputs must be within the per-feed quota. | See [Quotas and limits for functions](functions-quotas.md). | 
| A feed with an enabled function output must also have an enabled smart crop, event clipping, smart subtitles, or contextual metadata output. | A function runs alongside the features of a feed, not on its own. Disable the function output, or enable one of those outputs. | 

For the errors these rules produce and what to do about them, see [Errors when you create or update](functions-troubleshooting-validation.md).