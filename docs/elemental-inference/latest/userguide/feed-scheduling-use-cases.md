

# Use cases for feed scheduling
<a name="feed-scheduling-use-cases"></a>

Use feed scheduling to change settings that are specific to Elemental Inference. For example:
+ **Switch games for event clipping** – Before the game, attach the game's fixture to an event clipping output so that clips are aligned to the correct game. For information about fixtures, see [Step 1: Find your game](create-feed-outputs.md#event-clip-find-game).
+ **Enable an output for a time window** – Enable a smart crop output when a game starts, and disable it when the game ends. The rest of the feed isn't affected.

You don't need a schedule action to stop all inference between events. A feed uses resources only while it receives media. To stop inference, stop sending media to the feed, for example by stopping the AWS Elemental MediaLive (MediaLive) channel. The feed becomes idle automatically.