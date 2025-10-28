# Generating audience-specific

manifests

To retrieve a manifest for a particular audience, use the
`aws.mediatailor.channel.audienceId` query parameter. This query parameter may
be dynamically appended by your CDN or added through a call to your content or
customer-management system. You must maintain the association of a given playback session
to an `audienceId` outside of MediaTailor. This will retrieve an audience-specific manifest
with any alternate media defined for that audience in place of default content. It is
important that once a manifest is requested for a particular audience that the player always
requests the manifest with that same audience ID or there could be playback errors.

If a request is made for an audience that does not exist on the channel, MediaTailor returns a
404 error.

###### Example Getting a manifest for an audience

`https:// prefix>.channel-assembly.mediatailor.us-west-2.amazonaws.com/v1/channel/ExampleChannel/index_dash.mpd?aws.mediatailor.channel.`audienceId`=Seattle`
