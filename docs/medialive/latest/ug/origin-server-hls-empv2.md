# HLS output group to MediaPackage v2

Follow this procedure if you [determined](dss-compare-elemental-services.md#hls-choosing-hls-vs-emp "dss-compare-elemental-services.md#hls-choosing-hls-vs-emp") that you will create an HLS output group, and will send to
MediaPackage v2. You and the operator of the downstream system must agree about the
destination for the output of the HLS output group.

###### To arrange setup of the destination

1. Ask the MediaPackage user to create one channel on MediaPackage. Even if the MediaLive
   channel is a [standard channel](plan-redundancy.md "plan-redundancy.md") (with
   two pipelines), you need only one MediaPackage channel.
2. Obtain the two URLs (input endpoints is the MediaPackage terminology) for the
   channel. The two URLs for a channel look like this:

`https://mz82o4-1.ingest.hnycui.mediapackagev2.us-west-2.amazonaws.com/in/v1/live-sports/1/curling/index`

`https://mz82o4-2.ingest.hnycui.mediapackagev2.us-west-2.amazonaws.com/in/v1/live-sports/2/curling/index`

The two URLs are slightly different, as shown in the examples
above.

Make sure that you obtain the URLs (which start with
`https://`), not the channel name (which starts with
`arn`).

Note that you don't use user credentials in order to send to MediaPackage
v2.
