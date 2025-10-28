# Request setup on the VPC

An Amazon VPC user must set up the VPC, and identify subnets and security groups that
both the upstream system and MediaLive will use.

###### To set up the VPC

1.  Provide the Amazon VPC user with the following guidelines.
    - Guideline for the subnets – Request two subnets. You need
      two subnets because a CDI input is always a [standard-class input](class-channel-input.md "class-channel-input.md"), even
      if your channel is a single-pipeline channel. For information about
      input classes, see [Choosing the channel class and input
      class](class-channel-input.md "class-channel-input.md").

    These rules apply:

        + The two subnets must be in different Availability
         Zones.
        + Each subnet must have a private CIDR block (a range of IP
         addresses).
        + Each subnet must have at least two unused addresses in
         that block—one for the upstream system and one for the
         CDI input.
        + Any other VPC-based sources (source B) that you create for
         use in the same channel as this CDI source (source A) must
         be in subnets that are in the same Availability Zones as
         source A. The two subnets of the source B can be different
         from the source A, but the Availability Zones of those two
         subnets must be the same as the Availability Zones of source
         A.

    - Guideline for the security group – the security groups or
      groups for each subnet must follow these rules:
      - The combined inbound rules of the security groups must
        allow inbound traffic from the IP addresses of the upstream
        system that is in that subnet.
      - The subnet must have an EFA-enabled security group. To
        create this type of security group and for information about
        its rules, see the [Amazon
        Elastic Compute Cloud User Guide](../../../AWSEC2/latest/UserGuide/efa-start.md "../../../AWSEC2/latest/UserGuide/efa-start.md").

2.  After the Amazon VPC user has performed the setup, obtain the following
    information:
    - The ID of the VPC. For example: `vpc-3f139646`
    - The IDs of the two subnets. For example, one subnet might have
      this ID: `subnet-1122aabb`

    - The IDs of the security groups for the subnet or subnets. For
      example: `sg-51530134`
