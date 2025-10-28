# Ensure correct setup on the upstream

system

After you create the CDI input, you must make sure that the operator at the
upstream system sets up correctly with your VPC, and that they push content to the
correct locations in MediaLive.

###### To set up for a standard channel

If the planned channel is a [standard
channel](plan-redundancy.md "plan-redundancy.md"), you must ensure that the operator at the upstream system
provides two sources.

1. Provide the operator with this information:
   - The IDs of the VPC, two subnets, and the security groups that the
     Amazon VPC user gave you in [step
     1](setup-vpc-cdi-vpc.md "setup-vpc-cdi-vpc.md").
   - The two endpoints (URLs) that MediaLive generated when you created the
     CDI input. These endpoints are the addresses in the blue boxes in
     [the diagram after this
     procedure](setup-result-cdi-vpc.md "setup-result-cdi-vpc.md"). These URLs each have a private IP address from
     the subnet range, and they specify port 5000. For example:

   `10.30.30.33:5000`

   `10.40.40.44:5000`

2. Make sure that the operator sets up properly for a standard channel. They
   must do the following:
   - Set up two output interfaces. Set up one upstream system with one
     output interface in one of the subnets, and set up the other
     upstream system with one output interface in the other subnet. These
     interfaces are the addresses in the purple boxes in [the diagram after this
     procedure](setup-result-cdi-vpc.md "setup-result-cdi-vpc.md").
   - Make sure that the two content sources are identical in terms of
     video resolution and bitrate.
   - Push to the correct URLs on MediaLive. For example, they must push
     to:

   `10.30.30.33:5000`

   `10.40.40.44:5000`

###### To set up for a single-pipeline channel

- There will be one upstream system that sends content to only one of
  the subnets in the VPC.
- The content will flow from the VPC to one of the endpoints on the
  input. The other endpoint will never be used.
- MediaLive will ingest the single source content.

1. Provide the operator with this information:
   - The IDs of the VPC, one of the subnets, and all of the security
     groups that the Amazon VPC user gave you.
   - Only the first of the two endpoints (URLs) that MediaLive generated
     when you created the CDI input. These endpoints are the addresses in
     the blue box in [the diagram
     after this procedure](setup-result-cdi-vpc.md "setup-result-cdi-vpc.md"). The URL has a private IP address
     from the subnet range, and it specifies port 5000.

   `10.30.30.33:5000`

2. Make sure that the operator sets up properly for a single-pipeline
   channel. They must:
   - Set up one upstream system.
   - Set up one output interfaces. The interface is the address in one
     of the purple boxes in [the
     diagram after this procedure](setup-result-cdi-vpc.md "setup-result-cdi-vpc.md").
   - Push to the correct URL on MediaLive. For example, they must push
     to:

   `10.30.30.33:5000`
