

# Transit gateway connection between Local Zones
<a name="local-zones-connectivity-transit-gateway-lzs"></a>

A transit gateway can be used to connect one Local Zone to another within the same parent Region. For more information about transit gateways, see [Connect your VPC to other VPCs and networks using a transit gateway](https://docs.aws.amazon.com/vpc/latest/userguide/extend-tgw.html) in the *Amazon VPC User Guide*.

A transit gateway connection between Local Zones is useful when you have workloads in different Local Zones and also require network connectivity between them.

The following diagram shows the transit gateway connection between two Local Zones in the same Region.

![An AWS Region with two VPCs. Each VPC contains an Availability Zone and a Local Zone. Each zone has a private subnet. A transit gateway connection facilitates traffic between the two Local Zones.](http://docs.aws.amazon.com/local-zones/latest/ug/images/local-zones-same-region.png)


**Considerations**
+ You must create a transit gateway attachment in the parent zone.
+ You can't connect a Local Zone to another Local Zone or Outpost that is within the same VPC.

**Parent zone**  
You can use the AWS Global View console or the command line interface to get the parent zone details for a Local Zone.

------
#### [ AWS Global View console ]

**To get the parent zone details for a Local Zone**

1. Sign in to the [AWS Global View console](https://console.aws.amazon.com/ec2globalview/home#RegionsAndZones).

1. From the navigation pane, choose **Regions and Zones**.

1. Choose the **Local Zones** tab.

1. Find the Local Zone.

1. Scroll to see the **Parent Zone name** and **Parent Zone ID** for the Local Zone.

------
#### [ AWS CLI ]

**To get the parent zone details for a Local Zone**  
Use the [describe-availability-zones](https://docs.aws.amazon.com/cli/latest/reference/ec2/describe-availability-zones.html) command. The following example uses a Local Zone in Los Angeles.

```
aws ec2 describe-availability-zones \
  --zone-names {{us-west-2-lax-1a}} \
  --query 'AvailabilityZones[0].ParentZoneName' \
  --region {{us-west-2}} \
  --output text
```

------