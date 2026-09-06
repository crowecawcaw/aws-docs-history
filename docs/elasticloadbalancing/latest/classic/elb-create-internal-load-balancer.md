

# Create an internal Classic Load Balancer
<a name="elb-create-internal-load-balancer"></a>

You can create an internal load balancer to distribute traffic to your EC2 instances from clients with access to the VPC for the load balancer.

**Topics**
+ [Prerequisites](#create-internal-lb-prereq)
+ [Create an internal load balancer using the console](#create-internal-lb)
+ [Create an internal load balancer using the AWS CLI](#create-internal-lb-cli)

## Prerequisites
<a name="create-internal-lb-prereq"></a>
+ If you have not yet created a VPC for your load balancer, you must create it before you get started. For more information, see [Recommendations for your VPC](elb-backend-instances.md#set-up-ec2).
+ Launch the EC2 instances that you plan to register with your internal load balancer. Ensure that you launch them in private subnets in the VPC intended for the load balancer.

## Create an internal load balancer using the console
<a name="create-internal-lb"></a>

Use the following procedure to create your internal Classic Load Balancer. Provide basic configuration information for your load balancer, such as a name and scheme. Then provide information about your network, and the listener that routes traffic to your instances..

**To create an internal Classic Load Balancer using the console**

1. Open the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/).

1. On the navigation bar, choose a Region for your load balancer. Be sure to select the same Region that you selected for your EC2 instances.

1. On the navigation pane, under **Load Balancing**, choose **Load Balancers**.

1. Choose **Create Load Balancer**.

1. Expand the **Classic Load Balancer** section, then choose **Create**.

1. **Basic configuration**

   1. For **Load balancer name**, type a name for your load balancer.

      The name of your Classic Load Balancer must be unique within your set of Classic Load Balancers for the Region, can have a maximum of 32 characters, can contain only alphanumeric characters and hyphens, and must not begin or end with a hyphen.

   1. For **Scheme**, select **Internal**.

1. **Network mapping**

   1. For **VPC**, select the same VPC that you selected for your instances.

   1. For **Mappings**, first select an Availability Zone, then choose a subnet from its available subnets. You can only select one subnet per Availability Zone. To improve the availability of your load balancer, select more than one Availability Zone and subnet.

1. For **Security groups**, select an existing security group that is configured to allow the required HTTP traffic on port 80. Or you can create a new security group if your application uses different protocols and ports.

1. **Listeners and routing**

   1. For **Listener**, ensure the protocol is `HTTP` and the port is `80`.

   1. For **Instance**, ensure the protocol is `HTTP` and the port is `80`.

1. **Health checks**

   1. For **Ping Protocol**, the default is `HTTP`.

   1. For **Ping Port**, the default is `80`.

   1. For **Ping Path**, the default is `/`.

   1. For **Advanced health check settings**, use the default values or enter values specific to your application.

1. **Instances**

   1. Select **Add instances**, to bring up the instance selection screen.

   1. Under **Available instances**, you can select from the current instances that are available to the load balancer, based on the network settings selected before.

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

## Create an internal load balancer using the AWS CLI
<a name="create-internal-lb-cli"></a>

By default, Elastic Load Balancing creates an internet-facing load balancer. Use the following procedure to create an internal load balancer and register your EC2 instances with the newly created internal load balancer.

**To create an internal load balancer**

1. Use the [create-load-balancer](https://docs.aws.amazon.com/cli/latest/reference/elb/create-load-balancer.html) command with the `--scheme` option set to `internal`, as follows:

   ```
   aws elb create-load-balancer --load-balancer-name {{my-internal-loadbalancer}} --listeners Protocol=HTTP,LoadBalancerPort=80,InstanceProtocol=HTTP,InstancePort=80
    --subnets {{subnet-4e05f721}} --scheme internal --security-groups {{sg-b9ffedd5}}
   ```

   The following is an example response. Note that the name indicates that this is an internal load balancer.

   ```
   {
       "DNSName": "internal-my-internal-loadbalancer-786501203.us-west-2.elb.amazonaws.com"
   }
   ```

1. Use the following [register-instances-with-load-balancer](https://docs.aws.amazon.com/cli/latest/reference/elb/register-instances-with-load-balancer.html) command to add instances:

   ```
   aws elb register-instances-with-load-balancer --load-balancer-name {{my-internal-loadbalancer}} --instances {{i-4f8cf126 i-0bb7ca62}}
   ```

   The following is an example response:

   ```
   {
       "Instances": [
           {
               "InstanceId": "i-4f8cf126"
           },
           {
               "InstanceId": "i-0bb7ca62"
           }
       ]
   }
   ```

1. (Optional) Use the following [describe-load-balancers](https://docs.aws.amazon.com/cli/latest/reference/elb/describe-load-balancers.html) command to verify the internal load balancer: 

   ```
   aws elb describe-load-balancers --load-balancer-name {{my-internal-loadbalancer}}
   ```

   The response includes the `DNSName` and `Scheme` fields, which indicate that this is an internal load balancer.

   ```
   {
       "LoadBalancerDescriptions": [
           {
               ...
               "DNSName": "internal-my-internal-loadbalancer-1234567890.us-west-2.elb.amazonaws.com", 
               "SecurityGroups": [
                   "sg-b9ffedd5"
               ], 
               "Policies": {
                   "LBCookieStickinessPolicies": [], 
                   "AppCookieStickinessPolicies": [], 
                   "OtherPolicies": []
               }, 
               "LoadBalancerName": "my-internal-loadbalancer", 
               "CreatedTime": "2014-05-22T20:32:19.920Z", 
               "AvailabilityZones": [
                   "us-west-2a"
               ], 
               "Scheme": "internal",
               ...
           }
       ]
   }
   ```