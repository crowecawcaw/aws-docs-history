

# Requirements for Elemental Inference
<a name="requirements-for-inference"></a>

Your organization might implement [AWS Elemental Inference features](elemental-inference.md) in a channel. Users who configure the channel to use these features need permissions to work with feeds. 
+ Users need permissions to work with feeds. Users need these permissions even though they are using the MediaLive console or API to set up the feeds and to associate the channel with the feed. 
+ Users need permissions to let MediaLive perform setup on a feed after the channel has been created or modified. The setup involves associating the channel with the feed. MediaLive uses IAM forward access sessions (FAS) to send and retrieve.


| Permissions | Service name in IAM | Actions | 
| --- | --- | --- | 
| When configuring a channel, so that MediaLive can work with the Elemental Inference feed. | Elemental Inference | CreateFeed`DeleteFeed`<br />`GetFeed`<br />`ListFeeds`<br />`UpdateFeed` | 
| After configuration of a channel, so that MediaLive can use FAS to associate the channel with the Elemental Inference feed. | Elemental Inference | `AssociateFeed`<br />`DisassociateFeed`<br />`GetFeed` | 