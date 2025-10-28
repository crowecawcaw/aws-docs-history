# Set up AWS Elemental MediaConnect

A MediaConnect user must set up MediaConnect with flows to deliver source content to
MediaLive.

###### To set up flows for a standard channel

1. Provide the MediaConnect user with this information:
   - Information about the provider of the source content.
   - The AWS Region for the channel that you that will create. The
     AWS Elemental MediaConnect flows and the MediaLive channel (and input) must be in the
     same Region.

   If the flows and the MediaLive channel aren't in the same Region, then
   the MediaConnect operator will have to set up a distribution to move the
   source content to the same Region as the MediaLive input.

2. Discuss with the MediaConnect user whether you need new flows:
   - You need new flows if the source content doesn't yet have flows in
     MediaConnect.
   - You can reuse existing flows so long as you follow these
     rules:
     - Each flow doesn't exceed its maximum output
       bandwidth.
     - Each flow doesn't exceed its maximum number of outputs
       from the flow. (MediaLive automatically creates an output on
       each flow after you create the input in the next step, [Create a MediaConnect input](setup-input-emx.md "setup-input-emx.md").)

3. If you decide you need new flows, ask the MediaConnect user to create two flows.
   - They should assign flow names that are identical except for a
     suffix. For example, `sports_event_A` and
     `sports_event_B`. These suffixes will help
     you, the MediaLive user, to match the flows to the input pipelines in
     MediaLive.
   - They should set up each flow in a different Availability Zone. (If
     the flows are in the same Availability Zone then you, the MediaLive
     user, won't be able to create the MediaLive inputs.)
   - They should speak to the service provider about the
     following:
     - To determine how to complete the source information for
       each flow.
     - To make sure that the service provider delivers two
       sources.
     - To make sure that the two sources have identical video
       resolution and bitrate.

   - They should not create outputs or entitlements.

4. Obtain the following information from the MediaConnect user:
   - The ARNs for the flows. For example:

   `arn:aws:mediaconnect:us-west-1:111122223333:flow:1bgf67:sports_event_A`

   `arn:aws:mediaconnect:us-west-1:111122223333:flow:9pmlk76:sports_event_B`

   Note that the ARNs include the flow names as the last portion.

###### To set up flows for a single-pipeline channel

1. Provide the MediaConnect user with this information:
   - Information about the provider of the source content.
   - The AWS Region for the channel that you will create. The
     AWS Elemental MediaConnect flow and the MediaLive channel (and input) must be in the same
     Region.

   If the flow and the MediaLive channel aren't in the same Region, then
   the MediaConnect operator will have to set up a distribution to move the
   source content to the same Region as the MediaLive input.

2. Discuss with the MediaConnect user whether you need a new flow:
   - You need a new flow if the source content doesn't yet have a flow
     in MediaConnect.
   - You can reuse an existing flow so long as you follow these
     rules:
     - The flow doesn't exceed its maximum output
       bandwidth.
     - The flow doesn't exceed its maximum number of outputs from
       the flow. (MediaLive automatically creates an output on the flow
       after you create the input in the next step, [Create a MediaConnect input](setup-input-emx.md "setup-input-emx.md").)

3. If you decide you need a new flow, ask the MediaConnect user to create one flow.
   - They should speak to the service provider to determine how to
     complete the source information for the flow.
   - They should not create an output or entitlement.

4. Obtain the ARN for the flow from the MediaConnect user. For example:

`arn:aws:mediaconnect:us-west-1:111122223333:flow:1bgf67:sports_event_A`

Note that the ARN includes the flow name as the last portion.
