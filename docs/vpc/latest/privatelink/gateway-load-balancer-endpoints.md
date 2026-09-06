

# Access an inspection system using a Gateway Load Balancer endpoint
<a name="gateway-load-balancer-endpoints"></a>

You can create a Gateway Load Balancer endpoint to connect to [endpoint services](concepts.md#concepts-endpoint-services) powered by AWS PrivateLink.

For each subnet that you specify from your VPC, we create an endpoint network interface in the subnet and assign it a private IP address from the subnet address range. An endpoint network interface is a requester-managed network interface; you can view it in your AWS account, but you can't manage it yourself.

You are billed for hourly usage and data processing charges. For more information, see [Gateway Load Balancer endpoint pricing](https://aws.amazon.com/privatelink/pricing/#Gateway_Load_Balancer_Endpoint_pricing).

**Topics**
+ [Considerations](#considerations-gateway-load-balancer-endpoints)
+ [Prerequisites](#prerequisites-gateway-load-balancer-endpoints)
+ [Create the endpoint](#create-gateway-load-balancer-endpoint)
+ [Configure routing](#configure-routing-gateway-load-balancer-endpoint)
+ [Manage tags](#add-remove-gateway-load-balancer-endpoint-tags)
+ [Delete a Gateway Load Balancer endpoint](#delete-gateway-load-balancer-endpoint)

## Considerations
<a name="considerations-gateway-load-balancer-endpoints"></a>
+ You can choose only one Availability Zone in the service consumer VPC. You can't change this subnet later on. To use a Gateway Load Balancer endpoint in a different subnet, you must create a new Gateway Load Balancer endpoint.
+ You can create a single Gateway Load Balancer endpoint per Availability Zone per service, and you must select the Availability Zone that the Gateway Load Balancer supports. When the service provider and service consumer are in different accounts, an Availability Zone name, such as `us-east-1a`, might be mapped to a different physical Availability Zone in each AWS account. You can use AZ IDs to consistently identify the Availability Zones for your service. For more information, see [AZ IDs](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-regions-availability-zones.html#az-ids) in the *Amazon EC2 User Guide*.
+ Before you can use the endpoint service the service provider must accept the connection requests. The service can't initiate requests to resources in your VPC through the VPC endpoint. The endpoint only returns responses to traffic that was initiated by resources in your VPC.
+ Each Gateway Load Balancer endpoint can support a bandwidth of up to 10 Gbps per Availability Zone and automatically scales up to 100 Gbps.
+ If an endpoint service is associated with multiple Gateway Load Balancers, a Gateway Load Balancer endpoint establishes a connection with only one load balancer per Availability Zone.
+ To keep traffic within the same Availability Zone, we recommend that you create a Gateway Load Balancer endpoint in each Availability Zone to which you'll send traffic.
+ Network Load Balancer client IP preservation is not supported when traffic is routed through a Gateway Load Balancer endpoint, even if the target is in the same VPC as the Network Load Balancer.
+ If the application servers and the Gateway Load Balancer endpoint are in the same subnet, the NACL rules are evaluated for traffic from the application servers to the Gateway Load Balancer endpoint.
+ If you use a Gateway Load Balancer with an egress-only internet gateway, the IPv6 traffic is dropped. Instead, use an internet gateway and inbound firewall rules.
+ There are quotas on your AWS PrivateLink resources. For more information, see [AWS PrivateLink quotas](vpc-limits-endpoints.md).

## Prerequisites
<a name="prerequisites-gateway-load-balancer-endpoints"></a>
+ Create a service consumer VPC with at least two subnets in the Availability Zone from which you'll access the service. One subnet is for the application servers and the other is for the Gateway Load Balancer endpoint.
+ To verify which Availability Zones are supported by the endpoint service, describe the endpoint service using the console or the [describe-vpc-endpoint-services](https://docs.aws.amazon.com/cli/latest/reference/ec2/describe-vpc-endpoint-services.html) command.
+ If your resources are in a subnet with a network ACL, verify that the network ACL allows traffic between the endpoint network interfaces and the resources in the VPC.

## Create the endpoint
<a name="create-gateway-load-balancer-endpoint"></a>

Use the following procedure to create a Gateway Load Balancer endpoint that connects to the endpoint service for the inspection system.

**To create a Gateway Load Balancer endpoint using the console**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, choose **Endpoints**.

1. Choose **Create endpoint**.

1. For **Type**, choose **Endpoint services that use NLBs and GWLBs**.

1. For **Service name**, enter the name of the service, and then choose **Verify service**.

1. For **VPC**, select the VPC from which you'll access the endpoint service.

1. For **Subnets**, select one subnet in which to create an endpoint network interface.

1. For **IP address type**, choose from the following options:
   + **IPv4** – Assign IPv4 addresses to the endpoint network interface. This option is supported only if the selected subnet has an IPv4 address range.
   + **IPv6** – Assign IPv6 addresses to the endpoint network interface. This option is supported only if the selected subnet is an IPv6 only subnet.
   + **Dualstack** – Assign both IPv4 and IPv6 addresses to the endpoint network interface. This option is supported only if the selected subnet has both IPv4 and IPv6 address ranges.

1. (Optional) To add a tag, choose **Add new tag** and enter the tag key and the tag value.

1. Choose **Create endpoint**. The initial status is `pending acceptance`.

**To create a Gateway Load Balancer endpoint using the command line**
+ [create-vpc-endpoint](https://docs.aws.amazon.com/cli/latest/reference/ec2/create-vpc-endpoint.html) (AWS CLI)
+ [New-EC2VpcEndpoint](https://docs.aws.amazon.com/powershell/latest/reference/items/New-EC2VpcEndpoint.html) (Tools for Windows PowerShell)

## Configure routing
<a name="configure-routing-gateway-load-balancer-endpoint"></a>

Use the following procedure to configure route tables for the service consumer VPC. This enables the security appliances to perform security inspection for inbound traffic that's destined for the application servers. For more information, see [Routing](vpce-gateway-load-balancer.md#gateway-load-balancer-endpoints-routing).

**To configure routing using the console**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, choose **Route Tables**.

1. Select the route table for the internet gateway and do the following:

   1. Choose **Actions**, **Edit routes**.

   1. If you support IPv4, choose **Add route**. For **Destination**, enter the IPv4 CIDR block of the subnet for the application servers. For **Target**, select the VPC endpoint.

   1. If you support IPv6, choose **Add route**. For **Destination**, enter the IPv6 CIDR block of the subnet for the application servers. For **Target**, select the VPC endpoint.

   1. Choose **Save changes**.

1. Select the route table for the subnet with the application servers and do the following:

   1. Choose **Actions**, **Edit routes**.

   1. If you support IPv4, choose **Add route**. For **Destination**, enter **0.0.0.0/0**. For **Target**, select the VPC endpoint.

   1. If you support IPv6, choose **Add route**. For **Destination**, enter **::/0**. For **Target**, select the VPC endpoint.

   1. Choose **Save changes**.

1. Select the route table for the subnet with the Gateway Load Balancer endpoint, and do the following:

   1. Choose **Actions**, **Edit routes**.

   1. If you support IPv4, choose **Add route**. For **Destination**, enter **0.0.0.0/0**. For **Target**, select the internet gateway.

   1. If you support IPv6, choose **Add route**. For **Destination**, enter **::/0**. For **Target**, select the internet gateway.

   1. Choose **Save changes**.

**To configure routing using the command line**
+ [create-route](https://docs.aws.amazon.com/cli/latest/reference/ec2/create-route.html) (AWS CLI)
+ [New-EC2Route](https://docs.aws.amazon.com/powershell/latest/reference/items/New-EC2Route.html) (Tools for Windows PowerShell)

## Manage tags
<a name="add-remove-gateway-load-balancer-endpoint-tags"></a>

You can tag your Gateway Load Balancer endpoint to help you identify it or categorize it according to your organization's needs.

**To manage tags using the console**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, choose **Endpoints**.

1. Select the interface endpoint.

1. Choose **Actions**, **Manage tags**.

1. For each tag to add choose **Add new tag** and enter the tag key and tag value.

1. To remove a tag, choose **Remove** to the right of the tag key and value.

1. Choose **Save**.

**To manage tags using the command line**
+ [create-tags](https://docs.aws.amazon.com/cli/latest/reference/ec2/create-tags.html) and [delete-tags](https://docs.aws.amazon.com/cli/latest/reference/ec2/delete-tags.html) (AWS CLI)
+ [New-EC2Tag](https://docs.aws.amazon.com/powershell/latest/reference/items/New-EC2Tag.html) and [Remove-EC2Tag](https://docs.aws.amazon.com/powershell/latest/reference/items/Remove-EC2Tag.html) (Tools for Windows PowerShell)

## Delete a Gateway Load Balancer endpoint
<a name="delete-gateway-load-balancer-endpoint"></a>

When you are finished with an endpoint, you can delete it. Deleting a Gateway Load Balancer endpoint also deletes the endpoint network interfaces. You can't delete a Gateway Load Balancer endpoint if there are routes in your route tables that point to the endpoint.

**To delete a Gateway Load Balancer endpoint**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, choose **Endpoints** and select your endpoint.

1. Choose **Actions**, **Delete Endpoint**. 

1. In the confirmation screen, choose **Yes, Delete**.

**To delete a Gateway Load Balancer endpoint**
+ [delete-vpc-endpoints](https://docs.aws.amazon.com/cli/latest/reference/ec2/delete-vpc-endpoints.html) (AWS CLI)
+ [Remove-EC2VpcEndpoint](https://docs.aws.amazon.com/powershell/latest/reference/items/Remove-EC2VpcEndpoint.html) (AWS Tools for Windows PowerShell)