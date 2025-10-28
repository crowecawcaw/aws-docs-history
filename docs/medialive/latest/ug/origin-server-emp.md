# Coordinate with the MediaPackage operator

You and the operator of the AWS Elemental MediaPackage service must agree about the destination for the
output of your MediaPackage output group.

Note that you can send to AWS Elemental MediaPackage by creating a MediaPackage output group, or by
creating an HLS output group. See [Choosing between the HLS output group and
MediaPackage output group](dss-compare-elemental-services.md#hls-choosing-hls-vs-emp "dss-compare-elemental-services.md#hls-choosing-hls-vs-emp") for a
description of the differences. This section describes the first option.

###### To arrange setup of the destination

1. Ask the MediaPackage user to create one channel. Even if the MediaLive channel is a [standard channel](plan-redundancy.md "plan-redundancy.md") (with two pipelines), you
   need only one MediaPackage channel.
2. Obtain the ID of the MediaPackage channel. For example, `curlinglive`. The
   channel ID is case sensitive.
   Note that you don't need user credentials to send a MediaPackage output group to
   MediaPackage. MediaLive has permission to write to MediaPackage via the trusted entity. Someone in your
   organization should have already set up these permissions. For more information, see
   [Access requirements for the trusted entity](trusted-entity-requirements.md "trusted-entity-requirements.md").
