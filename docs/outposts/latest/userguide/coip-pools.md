

# Create a CoIP pool
<a name="coip-pools"></a>

You can provide IP address ranges to facilitate communication between your on-premises network and instances in your VPC. For more information, see [Customer-owned IP addresses](routing.md#ip-addressing).

Customer-owned IP pools are available for local gateway route tables in CoIP mode.

Use the following procedure to create a CoIP pool.

------
#### [ Console ]

**To create a CoIP pool using the console**

1. Open the AWS Outposts console at [https://console.aws.amazon.com/outposts/](https://console.aws.amazon.com/outposts/home).

1. To change the AWS Region, use the Region selector in the upper-right corner of the page.

1. On the navigation pane, choose **Local gateway route tables**.

1. Choose the route table. 

1. Choose the **CoIP pools** tab in the details pane, and then choose **Create CoIP pool**.

1. (Optional) For **Name**, enter a name for your CoIP pool.

1. Choose **Add new CIDR** and enter a range of customer-owned IP addresses.

1. (Optional) To add a CIDR block, choose **Add new CIDR** and enter a range of customer-owned IP addresses.

1. Choose **Create CoIP pool**.

------
#### [ AWS CLI ]

**To create a CoIP pool using the AWS CLI**

1. Use the [create-coip-pool](https://docs.aws.amazon.com/cli/latest/reference/ec2/create-coip-pool.html) command to create a pool of CoIP addresses for the specified local gateway route table.

   ```
   aws ec2 create-coip-pool --local-gateway-route-table-id {{lgw-rtb-abcdefg1234567890}}
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

1. Use the [create-coip-cidr](https://docs.aws.amazon.com/cli/latest/reference/ec2/create-coip-cidr.html) command to create a range of CoIP addresses in the specified CoIP pool.

   ```
   aws ec2 create-coip-cidr --cidr 15.0.0.0/24 --coip-pool-id {{ipv4pool-coip-1234567890abcdefg}}
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

------

After you create a CoIP pool, use the following procedure to assign an address to your instance.

------
#### [ Console ]

**To assign a CoIP address to an instance using the console**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, choose **Elastic IPs**.

1. Choose **Allocate Elastic IP address**.

1. For **Network Border Group**, select the location from which the IP address is advertised.

1. For **Public IPv4 address pool**, choose **Customer owned IPv4 address pool**.

1. For **Customer owned IPv4 address pool**, select the pool that you configured.

1. Choose **Allocate**.

1. Select the Elastic IP address, and choose **Actions**, **Associate Elastic IP address**.

1. Select the instance from **Instance**, and then choose **Associate**.

------
#### [ AWS CLI ]

**To assign a CoIP address to an instance using the AWS CLI**

1. Use the [describe-coip-pools](https://docs.aws.amazon.com/cli/latest/reference/ec2/describe-coip-pools.html) command to retrieve information about your customer-owned address pools.

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

1. Use the [allocate-address](https://docs.aws.amazon.com/cli/latest/reference/ec2/allocate-address.html) command to allocate an Elastic IP address. Use the pool ID returned in the previous step.

   ```
   aws ec2 allocate-address--address {{192.0.2.128}} --customer-owned-ipv4-pool {{ipv4pool-coip-0abcdef0123456789}}
   ```

   The following is example output.

   ```
   {
       "CustomerOwnedIp": "192.0.2.128",
       "AllocationId": "eipalloc-02463d08ceEXAMPLE",
       "CustomerOwnedIpv4Pool": "ipv4pool-coip-0abcdef0123456789",
   }
   ```

1. Use the [associate-address](https://docs.aws.amazon.com/cli/latest/reference/ec2/associate-address.html) command to associate the Elastic IP address with the Outpost instance. Use the allocation ID returned in the previous step.

   ```
   aws ec2 associate-address --allocation-id {{eipalloc-02463d08ceEXAMPLE}} --network-interface-id {{eni-1a2b3c4d}}
   ```

   The following is example output.

   ```
   {
       "AssociationId": "eipassoc-02463d08ceEXAMPLE",
   }
   ```

------