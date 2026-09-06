

# Viewing features using the AWS CLI
<a name="smart-crop-cli-view"></a>

To view information about Elemental Inference features, use `get-feed` to obtain this information:
+ The ARN of a feed.
+ The ARN of the MediaLive channel that is associated with the feed. This value is in `associatedResourceName`.
+ The data endpoint of the feed. The feed receives media data at this endpoint and returns the resulting metadata to this endpoint. 
+ A list of the outputs that belong to the feed. Each output is of type `GetOutput`.
+ The status of each output is captured in each `GetOutput`. The output is either `ENABLED` or `DISABLED`. When MediaLive is managing feeds, outputs will always `ENABLED`. (MediaLive doesn't ever disable a feed output that is no longer set up for Elemental Inference features. Instead, it simply deletes it.)

  You can change the status of an output to disable the related feature. For information, see [Disabling some Elemental Inference features in a channel](smart-crop-disable-some.md) or [Disabling all Elemental Inference features in a channel](smart-crop-disable-all.md).
+ The status of the feed. You can't change the status of a feed. The service controls the status. 

  The following statuses are most interesting when you are using MediaLive to work with Elemental Inference features:
  + `ACTIVE` means that the feed is associated with the channel.
  + `DELETED` means that MediaLive has deleted the channel. After a short period \*\*how long?, the status will always change to `ARCHIVED`. There is no way to change the status of a feed that is `DELETED` or `ARCHIVED`. If you reenable Elemental Inference features in a channel, MediaLive will create a new feed that has a new ID.