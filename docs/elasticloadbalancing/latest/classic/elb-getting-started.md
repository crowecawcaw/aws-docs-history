# Create an internet-facing Classic Load Balancer

When you create a load balancer, you configure listeners, configure health checks,
and register back-end instances. You configure a listener by specifying a protocol and
a port for front-end (client to load balancer) connections, and a protocol and a port
for back-end (load balancer to back-end instances) connections. You can configure multiple
listeners for your load balancer.

This tutorial provides a hands-on introduction to Classic Load Balancers through the AWS Management Console,
a web-based interface. You'll create a load balancer that receives
public HTTP traffic and sends it to your EC2 instances.

To create a load balancer with an HTTPS listener, see
[Create a Classic Load Balancer with an HTTPS listener](elb-create-https-ssl-load-balancer.md "elb-create-https-ssl-load-balancer.md").

###### Tasks

- [Before you begin](#getting-started-prerequisites "#getting-started-prerequisites")
- [Create a Classic Load Balancer using the AWS Management Console](#console-steps "#console-steps")

## Before you begin

- Create a virtual private cloud (VPC). For more information, see
  [Recommendations for your VPC](elb-backend-instances.md#set-up-ec2 "elb-backend-instances.md#set-up-ec2").
- Launch the EC2 instances that you plan to register with your load balancer. Ensure that
  the security groups for these instances allow HTTP access on port 80.
- Install a web server, such as Apache or Internet Information Services (IIS), on each
  instance, enter its DNS name into the address field of an internet-connected web browser,
  and verify that the browser displays the default page of the server.

## Create a Classic Load Balancer using the AWS Management Console

Use the following procedure to create your Classic Load Balancer. Provide basic configuration information
for your load balancer, such as a name and scheme. Then provide information about your network,
and the listener that routes traffic to your instances.

###### To create a Classic Load Balancer using the console

1. Open the Amazon EC2 console at
   [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
2. On the navigation bar, choose a Region for your load balancer. Be sure to select
   the same Region that you selected for your EC2 instances.
3. On the navigation pane, under **Load Balancing**, choose
   **Load Balancers**.
4. Choose **Create Load Balancer**.
5. Expand the **Classic Load Balancer** section, then choose **Create**.
6. **Basic configuration**
   1. For **Load balancer name**, type a name for your load
      balancer.

   The name of your Classic Load Balancer must be unique within your set of Classic Load Balancers for the
   Region, can have a maximum of 32 characters, can contain only alphanumeric
   characters and hyphens, and must not begin or end with a hyphen. 2. For **Scheme**, select **Internet-facing**.

7. **Network mapping**
   1. For **VPC**, select the same VPC that you selected for your
      instances.
   2. For **Mappings**, first select an Availability Zone, then choose a
      public subnet from its available subnets. You can only select one subnet per Availability Zone.
      To improve the availability of your load balancer, select more than one Availability Zone and subnet.

8. **Security groups**
   1. For **Security groups**, select an existing security group that is
      configured to allow the required HTTP traffic on port 80.

9. **Listeners and routing**
   1. For **Listener**, ensure the protocol is `HTTP` and the port
      is `80`.
   2. For **Instance**, ensure the protocol is `HTTP` and the port
      is `80`.

10. **Health checks**
    1. For **Ping Protocol**, ensure the protocol is `HTTP`.
    2. For **Ping Port**, ensure the port is `80`.
    3. For **Ping Path**, ensure the path is `/`.
    4. For **Advanced health check settings**, use the default values.

11. **Instances**
    1. Select **Add instances**, to bring up the instance selection screen.
    2. Under **Available instances**, you can select from the current instances
       that are available to the load balancer, based on the current network settings.
    3. After you're satisfied with your selections, select **Confirm** to add the
       instances to be registered to the load balancer.

12. **Attributes**
    1. For **Enable cross-zone load balancing**, **Enable
       connection draining**, and **Timeout (draining interval)**
       keep the default values.

13. **Load balancer tags (optional)**
    1. The **Key** field is required.
    2. The **Value** field is optional.
    3. To add another tag, select **Add new tag** then input your values into the
       **Key** field, and optionally the **Value**
       field.
    4. To remove an existing tag, select **Remove** next to the tag you want to remove.

14. **Summary and creation**
    1. If you need to change any settings, select **Edit** next to the setting
       needing to be changed.
    2. After you're satisfied with all the settings shown in the summary, select **Create
       load balancer** to begin creation of your load balancer.
    3. On the final creation page, select **View load balancer** to view your load balancer in the Amazon EC2 console.

15. **Verify**
    1. Select your new load balancer.
    2. On the **Target instances** tab, check the **Health status** column. After
       at least one of your EC2 instances is **In-service**, you can test your load balancer.
    3. In the **Details** section, copy the load balancers **DNS name**,
       which would look similar to `my-load-balancer-1234567890.us-east-1.elb.amazonaws.com`.
    4. Paste your load balancers **DNS name** into the address field of a public internet
       connected web browser. If your load balancer is functioning correctly, you will see the default page
       of your server.

16. **Delete (optional)**
    1. If you have a CNAME record for your domain that points to your load balancer, point it to a new location
       and wait for the DNS change to take effect before deleting your load balancer.
    2. Open the Amazon EC2 console at
       [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/ "https://console.aws.amazon.com/ec2/").
    3. Select the load balancer.
    4. Choose **Actions**, **Delete load balancer**.
    5. When prompted for confirmation, type `confirm` then select **Delete**.
    6. After you delete a load balancer, the EC2 instances that were registered with the load balancer continue
       to run. You will be billed for each partial or full hour that they continue running. When you no longer
       need an EC2 instance, you can stop or terminate it to prevent incurring additional charges.
