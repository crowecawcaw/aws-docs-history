# Preparing the upstream and downstream systems in a workflow

As the first stage in planning the workflow, you must set up the upstream and downstream
systems.

###### Important

This procedure describes planning the workflow starting from the
output and then working back to the input. This is the most effective way
to plan a workflow.

###### To plan the workflow

1. Identify the output groups that you need to produce, based on the
   systems that are downstream of MediaLive. See [Identify the output group types for the
   downstream system](identify-downstream-system.md "identify-downstream-system.md").
2. Identify the requirements for the video and audio encodes that you
   will include in each output group. See [Identify the encode
   requirements for the output groups](identify-dss-video-audio.md "identify-dss-video-audio.md").
3. Decide on the channel class—decide if you want to create a
   standard channel that supports redundancy or a single-pipeline channel
   that doesn't support redundancy. See [Identify resiliency requirements](plan-redundancy.md "plan-redundancy.md").
4. Assess the source content to make sure it's compatible with MediaLive
   and with the outputs that you need to create. For example, make sure
   that the source content has a video codec that MediaLive supports. See [Assess the upstream system](evaluate-upstream-system.md "evaluate-upstream-system.md") .

After you have performed these four steps, you know whether MediaLive
can handle your transcoding request. 5. Collect identifiers for the source content. For example, ask the
operator at the upstream system for the identifiers for the different
audio languages that you want to extract from the content. See [Collect information about the source content](planning-content-extract.md "planning-content-extract.md"). 6. Coordinate with the downstream system or systems to provide a
destination for the output groups that MediaLive will produce. See [Coordinate with downstream systems](setting-up-downstream-system.md "setting-up-downstream-system.md").
