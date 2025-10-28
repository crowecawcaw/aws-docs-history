# Ensure correct setup on the upstream

system

You must make sure that the upstream system sets up correctly with your VPC and
pushes content to the correct locations in MediaLive.

###### To set up for a standard channel

Follow this procedure if the MediaLive channel is a [standard channel](plan-redundancy.md "plan-redundancy.md").

1. Provide the operator with this information:
   - The IDs of the VPC, two subnets, and the security groups that the
     Amazon VPC user gave you.
   - The two endpoints (URLs) that MediaLive generated when you created the
     RTP input. These endpoints are the addresses in the blue boxes in
     [the diagram after this
     procedure](setup-rtp-vpc-result.md "setup-rtp-vpc-result.md"). The URLs have private IP addresses and include
     port 5000. For example:

   `10.12.30.44:5000`

   `10.99.39.15:5000`

2. Make sure that the operator sets up properly for a standard channel. They
   must:
   - Set up two output interfaces—one output interface in one of
     the subnets, and set up the other upstream system with one output
     interface in the other subnet. These interfaces are the addresses in
     the purple boxes in [the diagram
     after this procedure](setup-rtp-vpc-result.md "setup-rtp-vpc-result.md").
   - Deliver two sources that are identical in terms of video
     resolution and bitrate.
   - Push to the correct URLs on MediaLive. For example, they must push
     to:

   `10.12.30.131:5000`

   `10.99.39.40:5000`
   - Send over RTP, not UDP. The UDP protocol is not supported for an
     input into MediaLive.

###### To set up for a single-pipeline channel

Follow this procedure if the MediaLive channel is a [single-pipeline channel](plan-redundancy.md "plan-redundancy.md").

1. Provide the operator with this information:
   - The IDs of the VPC, one subnet, and the security groups that the
     Amazon VPC user gave you.
   - Only the first of the two endpoints (URLs) that MediaLive generated
     when you created the RTP input. These endpoints are the addresses in
     the blue boxes in [the diagram
     after this procedure](setup-rtp-vpc-result.md "setup-rtp-vpc-result.md"). The URL has a private IP address
     and includes port 5000. For example:

   `10.12.30.44:5000`

   `10.99.39.15:5000`

2. Make sure that the operator sets up properly for a standard channel. They
   must:
   - Set up one output interface. The interface is the address in one
     of the purple boxes in [the
     diagram after this procedure](setup-rtp-vpc-result.md "setup-rtp-vpc-result.md").
   - Push to the correct URL on MediaLive. For example, they must push
     to:

   `10.12.30.131:5000`

   `10.99.39.40:5000`
   - Send over RTP, not UDP. The UDP protocol is not supported for an
     input into MediaLive.
