

# Update the IP address types for your Gateway Load Balancer
<a name="load-balancer-ip-address-type"></a>

You can configure your Gateway Load Balancer so that application servers can access your load balancer using IPv4 addresses only, or using both IPv4 and IPv6 addresses (dualstack). The load balancer communicates with targets based on the IP address type of the target group. For more information, see [IP address type](gateway-load-balancers.md#ip-address-type).

**To update the IP address type using the console**

1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/).

1. On the navigation pane, under **Load Balancing**, choose **Load Balancers**.

1. Select the load balancer.

1. Choose **Actions**, **Edit IP address type**.

1. For **IP address type**, choose **ipv4** to support IPv4 addresses only or **dualstack** to support both IPv4 and IPv6 addresses.

1. Choose **Save**.

**To update the IP address type using the AWS CLI**  
Use the [set-ip-address-type](https://docs.aws.amazon.com/cli/latest/reference/elbv2/set-ip-address-type.html) command.