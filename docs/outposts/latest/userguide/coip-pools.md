# Create a CoIP pool

You can provide IP address ranges to facilitate communication between your on-premises
network and instances in your VPC. For more information, see [Customer-owned IP addresses](routing.md#ip-addressing "routing.md#ip-addressing").

Customer-owned IP pools are available for local gateway route tables in CoIP mode.

Use the following procedure to create a CoIP pool.

Console

###### To create a CoIP pool using the console

1. Open the AWS Outposts console at [https://console.aws.amazon.com/outposts/](https://console.aws.amazon.com/outposts/home "https://console.aws.amazon.com/outposts/home").
2. To change the AWS Region, use the Region selector in the upper-right corner of
   the page.
3. On the navigation pane, choose **Local gateway route
   tables**.
4. Choose the route table.
5. Choose the **CoIP pools** tab in the details pane, and then
   choose **Create CoIP pool**.
6. (Optional) For **Name**, enter a name for your CoIP
   pool.
7. Choose **Add new CIDR** and enter a range of customer-owned IP
   addresses.
8. (Optional) To add a CIDR block, choose **Add new CIDR** and
   enter a range of customer-owned IP addresses.
9. Choose **Create CoIP pool**.

AWS CLI

###### To create a CoIP pool using the AWS CLI

1. Use the [create-coip-pool](../../../cli/latest/reference/ec2/create-coip-pool.md "../../../cli/latest/reference/ec2/create-coip-pool.md") command to create a pool of CoIP addresses for the
   specified local gateway route table.

```
aws ec2 create-coip-pool --local-gateway-route-table-id `lgw-rtb-abcdefg1234567890`
```

The following is example output.

```
{
    "CoipPool": {
        "PoolId": "ipv4pool-coip-1234567890abcdefg",
        "LocalGatewayRouteTableId": "lgw-rtb-abcdefg1234567890",
        "PoolArn": "arn:aws:ec2:us-west-2:123456789012:coip-pool/ipv4pool-coip-1234567890abcdefg"
    }
}
```

2. Use the [create-coip-cidr](../../../cli/latest/reference/ec2/create-coip-cidr.md "../../../cli/latest/reference/ec2/create-coip-cidr.md") command to create a range of CoIP addresses in the
   specified CoIP pool.

```
aws ec2 create-coip-cidr --cidr 15.0.0.0/24 --coip-pool-id `ipv4pool-coip-1234567890abcdefg`
```

The following is example output.

```
{
    "CoipCidr": {
        "Cidr": "15.0.0.0/24",
        "CoipPoolId": "ipv4pool-coip-1234567890abcdefg",
        "LocalGatewayRouteTableId": "lgw-rtb-abcdefg1234567890"
    }
}
```

After you create a CoIP pool, use the following procedure to assign an address to your
instance.

Console

###### To assign a CoIP address to an instance using the console

1. Open the Amazon VPC console at
   [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
2. In the navigation pane, choose **Elastic IPs**.
3. Choose **Allocate Elastic IP address**.
4. For **Network Border Group**, select the location from which
   the IP address is advertised.
5. For **Public IPv4 address pool**, choose **Customer
   owned IPv4 address pool**.
6. For **Customer owned IPv4 address pool**, select the pool that
   you configured.
7. Choose **Allocate**.
8. Select the Elastic IP address, and choose **Actions**,
   **Associate Elastic IP address**.
9. Select the instance from **Instance**, and then choose
   **Associate**.

AWS CLI

###### To assign a CoIP address to an instance using the AWS CLI

1. Use the [describe-coip-pools](../../../cli/latest/reference/ec2/describe-coip-pools.md "../../../cli/latest/reference/ec2/describe-coip-pools.md") command to retrieve information about your
   customer-owned address pools.

```
aws ec2 describe-coip-pools
```

The following is example output.

```
{
    "CoipPools": [
        {
            "PoolId": "ipv4pool-coip-0abcdef0123456789",
            "PoolCidrs":  [
                "192.168.0.0/16"
            ],
            "LocalGatewayRouteTableId": "lgw-rtb-0abcdef0123456789"
        }
    ]
}
```

2. Use the [allocate-address](../../../cli/latest/reference/ec2/allocate-address.md "../../../cli/latest/reference/ec2/allocate-address.md") command to allocate an Elastic IP address. Use the pool
   ID returned in the previous step.

```
aws ec2 allocate-address--address `192.0.2.128` --customer-owned-ipv4-pool `ipv4pool-coip-0abcdef0123456789`
```

The following is example output.

```
{
    "CustomerOwnedIp": "192.0.2.128",
    "AllocationId": "eipalloc-02463d08ceEXAMPLE",
    "CustomerOwnedIpv4Pool": "ipv4pool-coip-0abcdef0123456789",
}
```

3. Use the [associate-address](../../../cli/latest/reference/ec2/associate-address.md "../../../cli/latest/reference/ec2/associate-address.md") command to associate the Elastic IP address with the
   Outpost instance. Use the allocation ID returned in the previous step.

```
aws ec2 associate-address --allocation-id `eipalloc-02463d08ceEXAMPLE` --network-interface-id `eni-1a2b3c4d`
```

The following is example output.

```
{
    "AssociationId": "eipassoc-02463d08ceEXAMPLE",
}
```
