# HLS output group to MediaStore

Follow this procedure if you [determined](identify-downstream-system.md "identify-downstream-system.md") that you will create an HLS output group, with AWS Elemental MediaStore as
the destination. You and the operator of the downstream system must agree about the
destination for the output of the HLS output group

###### To arrange setup of the destination

1. Decide if you need two destinations for the output:
   - You need two destinations in a [standard channel](plan-redundancy.md "plan-redundancy.md").
   - You need one destination in a single-pipeline channel.

2. We recommend that you design the full path of the destination. See [Design the path for the
   output destination](hls-destinations-design-step.md "hls-destinations-design-step.md").

If you have two destinations, the destination paths must be different from
each other in some way. At least one of the portions of one path must be
different from the other. It is acceptable for all the portions to be
different. 3. Ask the MediaStore user to create any containers that don't already exist. 4. Obtain the data endpoint for the container or containers. For example:

`https://a23f.data.mediastore.us-west-2.amazonaws.com`

`https://fe30.data.mediastore.us-west-2.amazonaws.com`

You need the data endpoints. You don't need the container name.
Note that you don't need user credentials to send to MediaStore containers. MediaLive has
permission to write to the MediaStore container via the trusted entity. Someone in your
organization should have already set up these permissions. For more information, see
[Access requirements for the trusted entity](trusted-entity-requirements.md "trusted-entity-requirements.md").
