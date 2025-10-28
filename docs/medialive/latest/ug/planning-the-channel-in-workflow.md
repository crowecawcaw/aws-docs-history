# Planning the outputs in the channel

You should plan the AWS Elemental MediaLive channel as the second stage of planning a
transcoding _workflow_. You should have
already performed the first stage of setting up the upstream and downstream
systems, as described in [Preparing the upstream and downstream systems in a workflow](container-planning-uss-dss.md "container-planning-uss-dss.md").

The channel provides the ability to configure for different
characteristics of the outputs, and for including a wide array of video
features. But before you plan these details, you should plan the basic
features for the channel.

###### Note

On the output side, we refer to each video or audio or caption stream, track, or program
as an _encode_.

###### Topics

- [Identify the output encodes](planning-encodes.md "planning-encodes.md")
- [Map the output encodes
  to the sources](channel-map-output-source.md "channel-map-output-source.md")
- [Design the encodes](designing-encodes.md "designing-encodes.md")
