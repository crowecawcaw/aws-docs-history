

# Use your BYOIP address range in Amazon EC2
<a name="byoip-working-with"></a>

You can view and use the IPv4 and IPv6 address ranges that you've provisioned in your account. For more information, see [Onboard your address range for use in Amazon EC2](byoip-onboard.md).

## IPv4 address ranges
<a name="byoip-work-with-ipv4"></a>

You can create an Elastic IP address from your IPv4 address pool and use it with your AWS resources, such as EC2 instances, NAT gateways, and Network Load Balancers.

To view information about the IPv4 address pools that you've provisioned in your account, use the following [describe-public-ipv4-pools](https://docs.aws.amazon.com/cli/latest/reference/ec2/describe-public-ipv4-pools.html) command.

```
aws ec2 describe-public-ipv4-pools --region {{us-east-1}}
```

To create an Elastic IP address from your IPv4 address pool, use the [allocate-address](https://docs.aws.amazon.com/cli/latest/reference/ec2/allocate-address.html) command. You can use the `--public-ipv4-pool` option to specify the ID of the address pool returned by `describe-byoip-cidrs`. Or you can use the `--address` option to specify an address from the address range that you provisioned.

## IPv6 address ranges
<a name="byoip-work-with-ipv6"></a>

To view information about the IPv6 address pools that you've provisioned in your account, use the following [describe-ipv6-pools](https://docs.aws.amazon.com/cli/latest/reference/ec2/describe-ipv6-pools.html) command.

```
aws ec2 describe-ipv6-pools --region {{us-east-1}}
```

To create a VPC and specify an IPv6 CIDR from your IPv6 address pool, use the following [create-vpc](https://docs.aws.amazon.com/cli/latest/reference/ec2/create-vpc.html) command. To let Amazon choose the IPv6 CIDR from your IPv6 address pool, omit the `--ipv6-cidr-block` option.

```
aws ec2 create-vpc --cidr-block {{10.0.0.0/16}} --ipv6-cidr-block {{ipv6-cidr}} --ipv6-pool {{pool-id}} --region {{us-east-1}}
```

To associate an IPv6 CIDR block from your IPv6 address pool with a VPC, use the following [associate-vpc-cidr-block](https://docs.aws.amazon.com/cli/latest/reference/ec2/associate-vpc-cidr-block.html) command. To let Amazon choose the IPv6 CIDR from your IPv6 address pool, omit the `--ipv6-cidr-block` option.

```
aws ec2 associate-vpc-cidr-block --vpc-id {{vpc-123456789abc123ab}} --ipv6-cidr-block {{ipv6-cidr}} --ipv6-pool {{pool-id}} --region {{us-east-1}}
```

To view your VPCs and the associated IPv6 address pool information, use the [describe-vpcs](https://docs.aws.amazon.com/cli/latest/reference/ec2/describe-vpcs.html) command. To view information about associated IPv6 CIDR blocks from a specific IPv6 address pool, use the following [get-associated-ipv6-pool-cidrs](https://docs.aws.amazon.com/cli/latest/reference/ec2/get-associated-ipv6-pool-cidrs.html) command.

```
aws ec2 get-associated-ipv6-pool-cidrs --pool-id {{pool-id}} --region {{us-east-1}}
```

If you disassociate the IPv6 CIDR block from your VPC, it's released back into your IPv6 address pool.