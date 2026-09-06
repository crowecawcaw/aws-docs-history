

# Instance placement and tenancy
<a name="infra-config-placement"></a>

Use placement settings to control where Image Builder launches your build and test instances. By default, Amazon EC2 instances run on shared tenancy hardware, which means multiple AWS accounts might share the same physical server. You can change the tenancy to run on single-tenant hardware or a Dedicated Host. You can also pin instances to a specific Availability Zone.

For the placement field names, their valid values, and constraints, see [Placement](https://docs.aws.amazon.com/imagebuilder/latest/APIReference/API_Placement.html) in the *EC2 Image Builder API Reference*.

**Note**  
Mac instances require a Dedicated Host. Set `tenancy` to `host` for macOS images. If your Dedicated Host has auto-placement enabled and you don't specify a `hostId` or `hostResourceGroupArn`, Amazon EC2 finds an available host for you. For more information, see [Auto-placement](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/dedicated-hosts-understanding.html#dedicated-hosts-auto-placement) in the *Amazon EC2 User Guide*.