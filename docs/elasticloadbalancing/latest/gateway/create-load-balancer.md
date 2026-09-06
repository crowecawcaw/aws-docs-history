

# Create a Gateway Load Balancer
<a name="create-load-balancer"></a>

A Gateway Load Balancer takes requests from clients and distributes them across targets in a target group, such as EC2 instances.

To create a Gateway Load Balancer using the AWS Management Console, complete the following tasks. Alternatively, to create a Gateway Load Balancer using the AWS CLI, see [Getting started using the CLI](getting-started-cli.md).

**Topics**
+ [Prerequisites](#create-load-balancer-prerequisites)
+ [Create the load balancer](#create-load-balancer-steps)
+ [Important next steps](#important-next-steps)

## Prerequisites
<a name="create-load-balancer-prerequisites"></a>

Before you begin, ensure that the virtual private cloud (VPC) for your Gateway Load Balancer has at least one subnet in each Availability Zone where you have targets.

## Create the load balancer
<a name="create-load-balancer-steps"></a>

Use the following procedure to create your Gateway Load Balancer. Provide basic configuration information for your load balancer, such as a name and IP address type. Then provide information about your network, and the listener that routes traffic to your target groups. Gateway Load Balancers require target groups that use the GENEVE protocol.

**To create the load balancer and listener using the console**

1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/).

1. In the navigation pane, under **Load Balancing**, choose **Load Balancers**.

1. Choose **Create load balancer**.

1. Under **Gateway Load Balancer**, choose **Create**.

1. **Basic configuration**

   1. For **Load balancer name**, enter a name for your load balancer. For example, **my-glb**. The name of your Gateway Load Balancer must be unique within your set of load balancers for the Region. It can have a maximum of 32 characters, can contain only alphanumeric characters and hyphens, and must not begin or end with a hyphen.

   1. For **IP address type**, choose **IPv4** to support IPv4 addresses only or **Dualstack** to support both IPv4 and IPv6 addresses.

1. **Network mapping**

   1. For **VPC**, select the service provider VPC.

   1. For **Mappings**, select all of the Availability Zones in which you launched security appliance instances, and the corresponding public subnets.

1. **IP listener routing**

   1. For **Default action**, select the target group to receive traffic. If you don't have a target group, choose **Create target group**. For more information, see [Create a target group](create-target-group.md).

   1. (Optional) Expand **Listener tags** and add the tags that you need.

1. (Optional) Expand **Load balancer tags** and add the tags that you need.

1. Review your configuration, and then choose **Create load balancer**.

## Important next steps
<a name="important-next-steps"></a>

After creating your load balancer, verify that your EC2 instances have passed the initial health check. To test your load balancer, you must create a Gateway Load Balancer endpoint and update your route table to make the Gateway Load Balancer endpoint the next hop. These configurations are set within the Amazon VPC console. For more information, see the [Getting started](getting-started.md) tutorial.