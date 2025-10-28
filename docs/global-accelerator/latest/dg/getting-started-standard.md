#

Getting started with a standard accelerator

This section provides steps for creating a standard accelerator, which routes traffic to an optimal
endpoint.

**Tasks**

- [Before you begin](#getting-started-before-you-begin "#getting-started-before-you-begin")
- [Step 1: Create a standard accelerator](#getting-started-accelerator "#getting-started-accelerator")
- [Step 2: Add listeners](#getting-started-create-listeners "#getting-started-create-listeners")
- [Step 3: Add endpoint groups](#getting-started-add-endpoint-groups "#getting-started-add-endpoint-groups")
- [Step 4: Add endpoints](#getting-started-add-endpoints "#getting-started-add-endpoints")
- [Step 5: Test your accelerator](#getting-started-create-and-test "#getting-started-create-and-test")
- [Step 6 (optional): Delete your accelerator](#getting-started-delete-accelerator "#getting-started-delete-accelerator")

##

Before you begin

Before you create an accelerator, create at least one resource that you can add as an endpoint
to direct traffic to. For example, create one of the following:

- Launch at least one Amazon EC2 instance to add as an endpoint. For more information, see [Create your EC2 resources and launch
  your EC2 instance](../../../AWSEC2/latest/UserGuide/gs-step-one-create-ec2-resources.md "../../../AWSEC2/latest/UserGuide/gs-step-one-create-ec2-resources.md") in the _Amazon EC2 User Guide_.
- Optionally, create one or more Network Load Balancers or Application Load Balancers that include EC2 instances. For more
  information, see [Create a Network Load Balancer](../../../elasticloadbalancing/latest/network/create-network-load-balancer.md "../../../elasticloadbalancing/latest/network/create-network-load-balancer.md")
  in the _User Guide for Network Load Balancers_.

When you create a resource to add to Global Accelerator, be aware of the following:

- When you add an internal Application Load Balancer or an EC2 instance endpoint in Global Accelerator, you enable
  internet traffic to flow directly to and from the endpoint in virtual private clouds (VPCs)
  by targeting it in a private subnet. The VPC that contains the load
  balancer or EC2 instance must have an [internet gateway](../../../vpc/latest/userguide/VPC_Internet_Gateway.md "../../../vpc/latest/userguide/VPC_Internet_Gateway.md")
  attached to it, to indicate that the VPC accepts internet traffic. For more information,
  see [Secure VPC connections in AWS Global Accelerator](secure-vpc-connections.md "secure-vpc-connections.md").
- Global Accelerator requires your router and firewall rules to allow inbound traffic from the IP addresses
  associated with Amazon Route 53 health checkers to complete health checks for EC2 instance or Elastic IP address
  endpoints. You can find information about the IP address ranges associated with Route 53 health
  checkers in [IP address ranges of Amazon Route 53 servers](../../../Route53/latest/DeveloperGuide/route-53-ip-addresses.md "../../../Route53/latest/DeveloperGuide/route-53-ip-addresses.md") in the _Amazon Route 53 Developer Guide_.

##

Step 1: Create a standard accelerator

When you create a standard accelerator, you can choose IPv4 or dual-stack for the static
IP addresses Global Accelerator assigns to your accelerator. Dual-stack supports both IPv4 and IPv6 IP addresses.

## To create an accelerator

1. Open the Global Accelerator console at [https://us-west-2.console.aws.amazon.com/globalaccelerator/home#GlobalAcceleratorHome:](https://us-west-2.console.aws.amazon.com/globalaccelerator/home#GlobalAcceleratorHome: "https://us-west-2.console.aws.amazon.com/globalaccelerator/home#GlobalAcceleratorHome:").
2. Choose **Create accelerator**.
3. Provide a name for your accelerator.
4. For **Accelerator type**, select **Standard**.
5. For **IP address type**, select **IPv4** or **Dual-stack**.
6. Optionally, add one or more tags to help you identify your Global Accelerator resources.
7. Choose **Next**.

## Step 2: Add listeners

Create a listener to process inbound connections from your users to Global Accelerator.

## To create a listener

1. On the **Add listener** page, enter the ports or port ranges that you want to associate with the
   listener. Listeners support ports 1-65535.
2. Choose the protocol or protocols for the ports that you entered.
3. Optionally, choose to enable client affinity. Client affinity for a listener means that Global Accelerator
   ensures that connections from a specific source (client) IP address are always
   routed to the same endpoint. To enable this behavior, in the dropdown list,
   choose **Source IP**.

The default is **None**, which means that client affinity is not enabled and Global Accelerator distributes traffic equally
between the endpoints in the endpoint groups for the listener.

For more information, see [How client affinity works in Global Accelerator](about-listeners-client-affinity.md "about-listeners-client-affinity.md"). 4. Optionally, choose **Add listener** to add an additional listener. 5. When you're finished adding listeners, choose **Next**.

## Step 3: Add endpoint groups

Add one or more endpoint groups, each of which is associated with a specific AWS Region.

## To add an endpoint group

1. On the **Add endpoint groups** page, in the section for a listener,
   choose a **Region** from the dropdown list.
2. Optionally, for **Traffic dial**, enter a number from 0 to 100 to set a
   percentage of traffic for this endpoint group. The percentage is applied only to the traffic
   already directed to this endpoint group, not all listener traffic. By default, the traffic dial
   for an endpoint group is set to 100 (that is, 100%).
3. Optionally, for custom health check values, choose **Configure health
   checks**. When you configure health check settings, Global Accelerator uses the settings for
   health checks for EC2 instance and Elastic IP address endpoints. For Network Load Balancer and Application Load Balancer endpoints,
   Global Accelerator uses the health check settings that you've already configured for the load balancers
   themselves. For more information, see [Ensure health check access for your accelerator](about-endpoint-groups-health-check-options.md "about-endpoint-groups-health-check-options.md").
4. Optionally, choose **Add endpoint group** to add additional endpoint
   groups for this listener or other listeners.
5. Choose **Next**.

## Step 4: Add endpoints

Add one or more endpoints that are associated with specific endpoint groups. This step
isn't required, but no traffic is directed to endpoints in a Region unless the endpoints are
included in an endpoint group.

## To add endpoints

1. On the **Create endpoints** page, in the section for an endpoint, choose an
   **Endpoint**.
2. Optionally, for **Weight**, enter a number from 0 to 255 to set a weight for
   routing traffic to this endpoint. When you add weights to endpoints, you
   configure Global Accelerator to route traffic based on proportions that you specify. By
   default, all endpoints have a weight of 128. For more information, see [How endpoint weights work to manage traffic volume](about-endpoints-endpoint-weights.md "about-endpoints-endpoint-weights.md").
3. Optionally, under **Preserve client IP address**, select **Preserve address**. (For
   some endpoint types, this option is selected and can't be cleared.)
   For more information, see [Preserve client IP addresses in AWS Global Accelerator](preserve-client-ip-address.md "preserve-client-ip-address.md").
4. Optionally, choose **Add endpoint** to add more endpoints.
5. Choose **Next**.

After you choose **Next**, on the Global Accelerator dashboard you'll see a message
that your accelerator is in progress. When the process is finished, the accelerator status in
the dashboard is **Active**.

## Step 5: Test your accelerator

Take steps to test your accelerator to make sure that traffic is being directed to your
endpoints. For example, run a curl command such as the following, substituting one of your
accelerator's static IP addresses, to show the AWS Regions where requests are processed. This
is especially helpful if you set different weights for endpoints or adjust the traffic dial on
endpoint groups.

Run a curl command like the following, substituting one of your accelerator's static IP addresses,
to call the IP address 100 times and then output a count of where each request was processed.

```
for ((i=0;i<100;i++)); do  curl http://198.51.100.0/ >> output.txt; done; cat output.txt | sort | uniq -c ; rm output.txt;
```

If you've adjusted the traffic dial on any endpoint groups, this command can help you confirm
that your accelerator is directing the correct percentages of traffic to different groups. For more
information, see the detailed examples in the following blog post,
[Traffic management with AWS Global Accelerator](https://aws.amazon.com/blogs/networking-and-content-delivery/traffic-management-with-aws-global-accelerator/ "https://aws.amazon.com/blogs/networking-and-content-delivery/traffic-management-with-aws-global-accelerator/").

##

Step 6 (optional): Delete your accelerator

If you created an accelerator as a test or if you're no longer using an accelerator, you can
delete it. On the console, disable the accelerator, and then you can delete it. You don't
have to remove listeners and endpoint groups from the accelerator.

To delete an accelerator by using an API operation instead of the console, you must first
remove all listeners and endpoint groups that are associated with the accelerator as well
as disable it. For more information, see the [DeleteAccelerator](../api/API_DeleteAccelerator.md "../api/API_DeleteAccelerator.md")
operation in the _AWS Global Accelerator API Reference_.

Be aware of the following when you remove endpoints or endpoint groups, or delete an accelerator:

- When you create an accelerator, Global Accelerator provides you with a set of two static IP addresses. The IP addresses are
  assigned to your accelerator for as long as it exists, even if you disable the accelerator and
  it no longer accepts or routes traffic. However, when you _delete_ an accelerator, you lose the
  static IP addresses that are assigned to the accelerator, so you can no longer route traffic by using them.
  As a best practice, ensure that you have permissions in place to avoid inadvertently deleting accelerators.
  You can use IAM policies with Global Accelerator, for example, tag-based permissions, to limit the users who have permissions to delete
  an accelerator. For more information, see [ABAC with Global Accelerator](security_iam_service-with-iam.md#security_iam_service-with-iam-tags "security_iam_service-with-iam.md#security_iam_service-with-iam-tags").
- If you terminate an EC2 instance before you remove it from an endpoint group in Global Accelerator,
  and then you create another instance with the same private IP address, and health checks pass,
  Global Accelerator will route traffic to the new endpoint. If you don't want this to happen, remove the
  EC2 instance from the endpoint group before you terminate the instance.

## To delete an accelerator

1. Open the Global Accelerator console at [https://console.aws.amazon.com/globalaccelerator/home](https://console.aws.amazon.com/globalaccelerator/home "https://console.aws.amazon.com/globalaccelerator/home").
2. Choose the accelerator that you want to delete.
3. Choose **Edit**.
4. Choose **Disable accelerator**, and then choose
   **Save**.
5. Choose the accelerator that you want to delete.
6. Choose **Delete accelerator**.
7. In the confirmation dialog box, choose **Delete**.
