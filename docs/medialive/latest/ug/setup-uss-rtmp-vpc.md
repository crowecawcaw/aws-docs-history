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
     RTMP input. These endpoints are the addresses in the blue boxes in
     [the diagram after this
     procedure](setup-rtmp-vpc-result.md "setup-rtmp-vpc-result.md"). The URL has a private IP address and includes
     port 1935. For example:

   `10.12.30.131:1935/live/curling`

   `10.99.39.40:1935/live/curling`

2. Make sure that the operator sets up properly for a standard channel. They
   must do the following:
   - Set up two separate upstream systems. They can't set up one
     upstream system with two output interfaces because you, the MediaLive
     user, will lose the redundancy that you want to achieve with a
     standard channel (with two independent pipelines).
   - Set up two output interfaces—one output interface in one of
     the subnets, and set up the other upstream system with one output
     interface in the other subnet. These interfaces are the addresses in
     the purple boxes in [the
     diagram after this procedure](setup-rtmp-vpc-result.md "setup-rtmp-vpc-result.md").
   - Make sure that the two content sources are identical in terms of
     video resolution and bitrate.
   - Push to the correct URLs on MediaLive, and use the agreed application
     name and instance name. For example, they must push to:

   `10.12.30.131:1935/live/curling`

   `10.99.39.40:1935/live/curling`

###### To set up for a single-pipeline channel

Follow this procedure if the MediaLive channel is a [single-pipeline channel](plan-redundancy.md "plan-redundancy.md").

1. Provide the operator with this information:
   - The IDs of the VPC, one subnet, and the security groups that the
     Amazon VPC user gave you.
   - Only the first of the two endpoints (URLs) that MediaLive generated
     when you created the RTMP input. These endpoints are the addresses
     in the blue boxes in [the
     diagram after this procedure](setup-rtmp-vpc-result.md "setup-rtmp-vpc-result.md"). The URL has a private IP
     address and includes port 1935. For example:

   `10.12.30.131:1935/live/curling`

2. Make sure that the operator sets up properly for a single-pipeline
   channel. They must do the following:
   - Set up one upstream system.
   - Set up one output interface. The interface is the address in one
     of the purple boxes in [the
     diagram after this procedure](setup-rtmp-vpc-result.md "setup-rtmp-vpc-result.md").
   - Push to the correct URL on MediaLive. For example, they must push
     to:

   `10.12.30.131:1935/live/curling`
