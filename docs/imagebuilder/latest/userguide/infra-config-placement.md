# Instance placement and tenancy

Use placement settings to control where Image Builder launches your build and test
instances. By default, Amazon EC2 instances run on shared tenancy hardware, which
means multiple AWS accounts might share the same physical server. You can
change the tenancy to run on single-tenant hardware or a Dedicated Host. You
can also pin instances to a specific Availability Zone.

For the placement field names, their valid values, and constraints, see
[Placement](../APIReference/API_Placement.md "../APIReference/API_Placement.md") in the
_EC2 Image Builder API Reference_.

###### Note

Mac instances require a Dedicated Host. Set `tenancy` to
`host` for macOS images. If your Dedicated Host has
auto-placement enabled and you don't specify a `hostId` or
`hostResourceGroupArn`, Amazon EC2 finds an available host for you.
For more information, see [Auto-placement](../../../AWSEC2/latest/UserGuide/dedicated-hosts-understanding.md#dedicated-hosts-auto-placement "../../../AWSEC2/latest/UserGuide/dedicated-hosts-understanding.md#dedicated-hosts-auto-placement") in the
_Amazon EC2 User Guide_.
