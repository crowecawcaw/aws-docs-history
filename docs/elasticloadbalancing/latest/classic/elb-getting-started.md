

# Create an internet-facing Classic Load Balancer
<a name="elb-getting-started"></a>

When you create a load balancer, you configure listeners, configure health checks, and register back-end instances. You configure a listener by specifying a protocol and a port for front-end (client to load balancer) connections, and a protocol and a port for back-end (load balancer to back-end instances) connections. You can configure multiple listeners for your load balancer.

This tutorial provides a hands-on introduction to Classic Load Balancers through the AWS Management Console, a web-based interface. You'll create a load balancer that receives public HTTP traffic and sends it to your EC2 instances.

To create a load balancer with an HTTPS listener, see [Create a Classic Load Balancer with an HTTPS listener](elb-create-https-ssl-load-balancer.md).

**Topics**
+ [Before you begin](#getting-started-prerequisites)
+ [Create a Classic Load Balancer using the AWS Management Console](#console-steps)

## Before you begin
<a name="getting-started-prerequisites"></a>
+ Create a virtual private cloud (VPC). For more information, see [Recommendations for your VPC](elb-backend-instances.md#set-up-ec2).
+ Launch the EC2 instances that you plan to register with your load balancer. Ensure that the security groups for these instances allow HTTP access on port 80.
+ Install a web server, such as Apache or Internet Information Services (IIS), on each instance, enter its DNS name into the address field of an internet-connected web browser, and verify that the browser displays the default page of the server.

## Create a Classic Load Balancer using the AWS Management Console
<a name="console-steps"></a>

Use the following procedure to create your Classic Load Balancer. Provide basic configuration information for your load balancer, such as a name and scheme. Then provide information about your network, and the listener that routes traffic to your instances.

**To create a Classic Load Balancer using the console**

1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/).

1. On the navigation bar, choose a Region for your load balancer. Be sure to select the same Region that you selected for your EC2 instances.

1. On the navigation pane, under **Load Balancing**, choose **Load Balancers**.

1. Choose **Create Load Balancer**.

1. Expand the **Classic Load Balancer** section, then choose **Create**.

1. **Basic configuration**

   1. For **Load balancer name**, type a name for your load balancer.

      The name of your Classic Load Balancer must be unique within your set of Classic Load Balancers for the Region, can have a maximum of 32 characters, can contain only alphanumeric characters and hyphens, and must not begin or end with a hyphen.

   1. For **Scheme**, select **Internet-facing**.

1. **Network mapping**

   1. For **VPC**, select the same VPC that you selected for your instances.

   1. For **Mappings**, first select an Availability Zone, then choose a public subnet from its available subnets. You can only select one subnet per Availability Zone. To improve the availability of your load balancer, select more than one Availability Zone and subnet.

1. **Security groups**

   1. For **Security groups**, select an existing security group that is configured to allow the required HTTP traffic on port 80.

1. **Listeners and routing**

   1. For **Listener**, ensure the protocol is `HTTP` and the port is `80`.

   1. For **Instance**, ensure the protocol is `HTTP` and the port is `80`.

1. **Health checks**

   1. For **Ping Protocol**, ensure the protocol is `HTTP`.

   1. For **Ping Port**, ensure the port is `80`.

   1. For **Ping Path**, ensure the path is `/`.

   1. For **Advanced health check settings**, use the default values.

1. **Instances**

   1. Select **Add instances**, to bring up the instance selection screen.

   1. Under **Available instances**, you can select from the current instances that are available to the load balancer, based on the current network settings.

   1. After you're satisfied with your selections, select **Confirm** to add the instances to be registered to the load balancer.

1. **Attributes**

   1. For **Enable cross-zone load balancing**, **Enable connection draining**, and **Timeout (draining interval)** keep the default values.

1. **Load balancer tags (optional)**

   1. The **Key** field is required.

   1. The **Value** field is optional.

   1. To add another tag, select **Add new tag** then input your values into the **Key** field, and optionally the **Value** field.

   1. To remove an existing tag, select **Remove** next to the tag you want to remove.

1. **Summary and creation**

   1. If you need to change any settings, select **Edit** next to the setting needing to be changed.

   1. After you're satisfied with all the settings shown in the summary, select **Create load balancer** to begin creation of your load balancer.

   1. On the final creation page, select **View load balancer** to view your load balancer in the Amazon EC2 console.

1. **Verify**

   1. Select your new load balancer.

   1. On the **Target instances** tab, check the **Health status** column. After at least one of your EC2 instances is **In-service**, you can test your load balancer.

   1. In the **Details** section, copy the load balancers **DNS name**, which would look similar to `my-load-balancer-1234567890.us-east-1.elb.amazonaws.com`.

   1. Paste your load balancers **DNS name** into the address field of a public internet connected web browser. If your load balancer is functioning correctly, you will see the default page of your server.

1. **Delete (optional)**

   1. If you have a CNAME record for your domain that points to your load balancer, point it to a new location and wait for the DNS change to take effect before deleting your load balancer.

   1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/).

   1. Select the load balancer.

   1. Choose **Actions**, **Delete load balancer**.

   1. When prompted for confirmation, type `confirm` then select **Delete**.

   1. After you delete a load balancer, the EC2 instances that were registered with the load balancer continue to run. You will be billed for each partial or full hour that they continue running. When you no longer need an EC2 instance, you can stop or terminate it to prevent incurring additional charges.