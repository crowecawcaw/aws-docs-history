

# Creating a health check source

The following procedure describes how to create a health check source by using the Route 53 console.<a name="health-check-sources-creating-proc"></a>

**To create a health check source**

1. Sign in to the AWS Management Console and open the Route 53 console at [https://console.aws.amazon.com/route53/](https://console.aws.amazon.com/route53/).

1. In the navigation pane, choose **Health checks**. Then choose the **Health check sources** tab.

1. Choose **Create health check source**.

1. (Optional) For **Name**, enter a name.

1. For **Region**, choose the AWS Region of the VPC. Private endpoint health checks that use this source run from this Region. The status, CloudWatch metrics, and alarms for these health checks also appear in this Region, even when you set your console to a different Region.

1. For **VPC**, choose the VPC that can reach your private endpoints. Route 53 filters the list by the Region that you selected.

1. Under **Subnet configurations**, choose three Availability Zones. For each one, choose a subnet and one or more security groups (up to 10).
**Note**  
In US West (N. California), which has two Availability Zones, choose two subnets.

1. Choose **Create health check source**.

**Note**  
You can't change the network configuration of a health check source after you create it. To change it, create a new source.

A health check source can take a few minutes to provision. Wait until its status is **Available** before you use it in a health check.

You can also start creating a health check source while you create a private endpoint health check. In the **Health check source** field, choose **Create health check source** to open the create page in a new tab. For more information, see [Values that you specify when you create or update a private endpoint health check](health-checks-creating-values.md#health-checks-creating-values-private-endpoint).