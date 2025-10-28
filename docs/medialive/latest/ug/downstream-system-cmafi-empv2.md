# Obtain destination for a CMAF Ingest

output group

1. Decide if you need two destination URLs for the output:
   - You need two destinations in a [standard channel](plan-redundancy.md "plan-redundancy.md").
   - You need one destination in a single-pipeline channel.

2. Obtain the one or two URLs from the MediaPackage operator. The MediaPackage terminology for
   the URL is _input endpoint_. Make sure that you
   obtain the URLs (which start with `https://`), not the channel name
   (which starts with `arn`).

Note that you don't use user credentials to send to CMAF Ingest to
MediaPackage.
**Example**

Two URLs look like this example:

`https://mz82o4-1.ingest.hnycui.mediapackagev2.us-west-2.amazonaws.com/in/v1/curling-channel-group/1/curling-channel/`

`https://mz82o4-2.ingest.hnycui.mediapackagev2.us-west-2.amazonaws.com/in/v1/curling-channel-group/1/curling-channel/`

Note the following:

- The `v1/` near the end of the URL is the version of the MediaPackage
  destination URL schema, it doesn't refer to MediaPackage v1.
- `curling-channel-group/` is the name of the channel group that the
  MediaPackage operator created.
- `curling-channel/` is the name of the MediaPackage channel that the MediaPackage
  operator created. It isn't the name of the MediaLive channel.
- The only difference in the two URLs is the `-1` and `-2`
  before
  `.ingest`.
