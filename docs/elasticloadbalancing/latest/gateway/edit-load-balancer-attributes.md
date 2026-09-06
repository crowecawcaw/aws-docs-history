

# Edit attributes for your Gateway Load Balancer
<a name="edit-load-balancer-attributes"></a>

After you create a Gateway Load Balancer, you can edit its load balancer attributes.

**Topics**
+ [Deletion protection](#deletion-protection)
+ [Cross-zone load balancing](#cross-zone-load-balancing)

## Deletion protection
<a name="deletion-protection"></a>

To prevent your Gateway Load Balancer from being deleted accidentally, you can enable deletion protection. By default, deletion protection is disabled.

If you enable deletion protection for your Gateway Load Balancer, you must disable it before you can delete the Gateway Load Balancer.

**To enable deletion protection using the console**

1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/).

1. In the navigation pane, under **Load Balancing**, choose **Load Balancers**.

1. Select the Gateway Load Balancer.

1. Choose **Actions**, **Edit attributes**.

1. On the **Edit load balancer attributes** page, select **Enable** for **Delete Protection**, and then choose **Save**.

**To disable deletion protection using the console**

1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/).

1. In the navigation pane, under **Load Balancing**, choose **Load Balancers**.

1. Select the Gateway Load Balancer.

1. Choose **Actions**, **Edit attributes**.

1. On the **Edit load balancer attributes** page, clear **Enable** for **Delete Protection**, and then choose **Save**.

**To enable or disable deletion protection using the AWS CLI**  
Use the [modify-load-balancer-attributes](https://docs.aws.amazon.com/cli/latest/reference/elbv2/modify-load-balancer-attributes.html) command with the `deletion_protection.enabled` attribute.

## Cross-zone load balancing
<a name="cross-zone-load-balancing"></a>

By default, each load balancer node distributes traffic across the registered targets in its Availability Zone only. If you enable cross-zone load balancing, each Gateway Load Balancer node distributes traffic across the registered targets in all enabled Availability Zones. For more information, see [Cross-zone load balancing](https://docs.aws.amazon.com/elasticloadbalancing/latest/userguide/how-elastic-load-balancing-works.html#cross-zone-load-balancing) in the *Elastic Load Balancing User Guide*.

**To enable cross-zone load balancing using the console**

1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/).

1. In the navigation pane, under **Load Balancing**, choose **Load Balancers**.

1. Select the Gateway Load Balancer.

1. Choose **Actions**, **Edit attributes**.

1. On the **Edit load balancer attributes** page, select **Enable** for **Cross-Zone Load Balancing**, and then choose **Save**.

**To enable cross-zone load balancing using the AWS CLI**  
Use the [modify-load-balancer-attributes](https://docs.aws.amazon.com/cli/latest/reference/elbv2/modify-load-balancer-attributes.html) command with the `load_balancing.cross_zone.enabled` attribute.