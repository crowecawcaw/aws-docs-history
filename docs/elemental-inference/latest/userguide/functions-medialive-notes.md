

# Considerations for functions with MediaLive
+ **Every enabled output counts against the feed's output quotas**, whichever service created it. By default, a feed can have five enabled outputs. At most two of them can be function outputs. A channel that already uses event clipping and smart subtitles is using two of the five. An `update-feed` call or channel save that goes over a quota fails. For more information, see [AWS Elemental Inference function quotas](functions-quotas.md).
+ **A feed that MediaLive created already exists**. If you enabled Elemental Inference features from the MediaLive console first, the channel has a feed named after itself. Add the access role and the function output to that feed rather than creating a second one, because a channel can be associated with only one feed.
+ **Disabling a function output doesn't stop MediaLive**. The channel keeps sending media to the feed for as long as `FeedArn` is set. Only the function's runs, and their model charges in your account, stop.

Functions work the same way on a feed that has no MediaLive channel: create the function, create the feed with the function output and the access role, associate the resource that represents your source, and deliver media to the feed's data endpoint with `PutMedia`. For more information, see [Step C: Deliver the source media](deliver-source.md).