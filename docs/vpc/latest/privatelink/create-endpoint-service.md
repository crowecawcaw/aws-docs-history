

# Create a service powered by AWS PrivateLink
<a name="create-endpoint-service"></a>

You can create your own service powered by AWS PrivateLink, known as an *endpoint service*. You are the service provider, and the AWS principals that create connections to your service are the service consumers.

Endpoint services require either a Network Load Balancer or a Gateway Load Balancer. The load balancer receives requests from service consumers and routes them to your service. In this case, you'll create an endpoint service using a Network Load Balancer. For more information about creating an endpoint service using a Gateway Load Balancer, see [Access virtual appliances](vpce-gateway-load-balancer.md).

**Topics**
+ [Considerations](#considerations-endpoint-services)
+ [Prerequisites](#prerequisites-endpoint-services)
+ [Create an endpoint service](#create-endpoint-service-nlb)
+ [Make your endpoint service available to service consumers](#share-endpoint-service)
+ [Connect to an endpoint service as the service consumer](#connect-to-endpoint-service)

## Considerations
<a name="considerations-endpoint-services"></a>
+ An endpoint service is available in the Region where you created it. Consumers can access your service from other Regions if you enable [cross-Region access](privatelink-share-your-services.md#endpoint-service-cross-region), or if they use VPC peering or a transit gateway.
+ When service consumers retrieve information about an endpoint service, they can see only the Availability Zones that they have in common with the service provider. When the service provider and service consumer are in different accounts, an Availability Zone name, such as `us-east-1a`, might be mapped to a different physical Availability Zone in each AWS account. You can use AZ IDs to consistently identify the Availability Zones for your service. For more information, see [AZ IDs](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/using-regions-availability-zones.html#az-ids) in the *Amazon EC2 User Guide*.
+ When service consumers send traffic to a service through an interface endpoint, the source IP addresses provided to the application are the private IP addresses of the load balancer nodes, not the IP addresses of the service consumers. If you enable proxy protocol on the load balancer, you can obtain the addresses of the service consumers and the IDs of the interface endpoints from the proxy protocol header. For more information, see [Proxy protocol](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/load-balancer-target-groups.html#proxy-protocol) in the *User Guide for Network Load Balancers*.
+ A Network Load Balancer can be associated with a single endpoint service, but an endpoint service can be associated with multiple Network Load Balancers.
+ If an endpoint service is associated with multiple Network Load Balancers, each endpoint network interface is associated with one load balancer. When the first connection from an endpoint network interface is initiated, we select one of the Network Load Balancers in the same Availability Zone as the endpoint network interface at random. All subsequent connection requests from this endpoint network interface use the selected load balancer. We recommend that you use the same listener and target group configuration for all load balancers for an endpoint service, so that consumers can use the endpoint service successfully no matter which load balancer is chosen.
+ There are quotas on your AWS PrivateLink resources. For more information, see [AWS PrivateLink quotas](vpc-limits-endpoints.md).

## Prerequisites
<a name="prerequisites-endpoint-services"></a>
+ Create a VPC for your endpoint service with at least one subnet in each Availability Zone in which the service should be available.
+ To enable service consumers to create IPv6 interface VPC endpoints for your endpoint service, the VPC and subnets must have associated IPv6 CIDR blocks.
+ Create a Network Load Balancer in your VPC. Select one subnet per Availability Zone in which the service should be available to service consumers. For low latency and fault tolerance, we recommend that you make your service available in at least two Availability Zones in the Region.
+ If your Network Load Balancer has a security group, it must allow inbound traffic from the IP addresses of the clients. Alternatively, you can turn off evaluation of inbound security group rules for traffic through AWS PrivateLink. For more information, see [Security groups](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/load-balancer-security-groups.html) in the *User Guide for Network Load Balancers*.
+ To enable your endpoint service to accept IPv6 requests, its Network Load Balancers must use the dualstack IP address type. The targets do not need to support IPv6 traffic. For more information, see [IP address type](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/network-load-balancers.html#ip-address-type) in the *User Guide for Network Load Balancers*.

  If you process source IP addresses from the proxy protocol version 2 header, verify that you can process IPv6 addresses.
+ Launch instances in each Availability Zone in which the service should be available and register them with a load balancer target group. If you do not launch instances in all enabled Availability Zones, you can enable cross-zone load balancing to support service consumers that use zonal DNS hostnames to access the service. Regional data transfer charges apply when you enable cross-zone load balancing. For more information, see [Cross-zone load balancing](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/network-load-balancers.html#cross-zone-load-balancing) in the *User Guide for Network Load Balancers*.

## Create an endpoint service
<a name="create-endpoint-service-nlb"></a>

Use the following procedure to create an endpoint service using a Network Load Balancer.

**To create an endpoint service using the console**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, choose **Endpoint services**.

1. Choose **Create endpoint service**.

1. For **Load balancer type**, choose **Network**.

1. For **Available load balancers**, select the Network Load Balancers to associate with the endpoint service. To see the Availability Zones that are enabled for the load balancer you selected, see **Details of selected load balancers**, **Included Availability Zones**. Your endpoint service will be available in these Availability Zones.

1. (Optional) To make your endpoint service available from Regions other than the Region where it is hosted, select the Regions from **Service Regions**. For more information, see [Cross-Region access](privatelink-share-your-services.md#endpoint-service-cross-region).

1. For **Require acceptance for endpoint**, select **Acceptance required** to require that connection requests to your endpoint service are accepted manually. Otherwise, these requests are accepted automatically.

1. For **Enable private DNS name**, select **Associate a private DNS name with the service** to associate a private DNS name that service consumers can use to access your service, and then enter the private DNS name. Otherwise, service consumers can use the endpoint-specific DNS name provided by AWS. Before service consumers can use the private DNS name, the service provider must verify that they own the domain. For more information, see [Manage DNS names](manage-dns-names.md).

1. For **Supported IP address types**, do one of the following:
   + Select **IPv4** – Enable the endpoint service to accept IPv4 requests.
   + Select **IPv6** – Enable the endpoint service to accept IPv6 requests.
   + Select **IPv4** and **IPv6** – Enable the endpoint service to accept both IPv4 and IPv6 requests.

1. (Optional) To add a tag, choose **Add new tag** and enter the tag key and the tag value.

1. Choose **Create**.

**To create an endpoint service using the command line**
+ [create-vpc-endpoint-service-configuration](https://docs.aws.amazon.com/cli/latest/reference/ec2/create-vpc-endpoint-service-configuration.html) (AWS CLI)
+ [New-EC2VpcEndpointServiceConfiguration](https://docs.aws.amazon.com/powershell/latest/reference/items/New-EC2VpcEndpointServiceConfiguration.html) (Tools for Windows PowerShell)

## Make your endpoint service available to service consumers
<a name="share-endpoint-service"></a>

AWS principals can connect to your endpoint service privately by creating an interface VPC endpoint. Service providers must do the following to make their services available to service consumers.
+ Add permissions that allow each service consumer to connect to your endpoint service. For more information, see [Manage permissions](configure-endpoint-service.md#add-remove-permissions).
+ Provide the service consumer with the name of your service and the supported Availability Zones so that they can create an interface endpoint to connect to your service. For more information, see [Connect to an endpoint service as the service consumer](#connect-to-endpoint-service).
+ Accept the endpoint connection request from the service consumer. For more information, see [Accept or reject connection requests](configure-endpoint-service.md#accept-reject-connection-requests).

## Connect to an endpoint service as the service consumer
<a name="connect-to-endpoint-service"></a>

A service consumer uses the following procedure to create an interface endpoint to connect to your endpoint service.

**To create an interface endpoint using the console**

1. Open the Amazon VPC console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/).

1. In the navigation pane, choose **Endpoints**.

1. Choose **Create endpoint**.

1. For **Type**, choose **Endpoint services that use NLBs and GWLBs**.

1. For **Service name**, enter the name of the service (for example, `com.amazonaws.vpce.us-east-1.vpce-svc-0e123abc123198abc`), and then choose **Verify service**.

1. (Optional) To connect to an endpoint service that is available in a Region other than the endpoint Region, select **Service Region**, **Enable Cross Region endpoint**, and then select the Region. For more information, see [Cross-Region access](privatelink-share-your-services.md#endpoint-service-cross-region).

1. For **VPC**, select the VPC from which you'll access the endpoint service.

1. For **Subnets**, select the subnets in which to create endpoint network interfaces.

1. For **IP address type**, choose from the following options:
   + **IPv4** – Assign IPv4 addresses to the endpoint network interfaces. This option is supported only if all selected subnets have IPv4 address ranges and the endpoint service accepts IPv4 requests.
   + **IPv6** – Assign IPv6 addresses to the endpoint network interfaces. This option is supported only if all selected subnets are IPv6 only subnets and the endpoint service accepts IPv6 requests.
   + **Dualstack** – Assign both IPv4 and IPv6 addresses to the endpoint network interfaces. This option is supported only if all selected subnets have both IPv4 and IPv6 address ranges and the endpoint service accepts both IPv4 and IPv6 requests.

1. For **DNS record IP type**, choose from the following options:
   + **IPv4** – Create A records for the private, Regional, and zonal DNS names. The IP address type must be **IPv4** or **Dualstack**.
   + **IPv6** – Create AAAA records for the private, Regional, and zonal DNS names. The IP address type must be **IPv6** or **Dualstack**.
   + **Dualstack** – Create A and AAAA records for the private, Regional, and zonal DNS names. The IP address type must be **Dualstack**.
   + **Service defined** – Create A records for the private, Regional, and zonal DNS names and AAAA records for the Regional and zonal DNS names. The IP address type must be **Dualstack**.

1. For **Security group**, select the security groups to associate with the endpoint network interfaces.

1. Choose **Create endpoint**.

**To create an interface endpoint using the command line**
+ [create-vpc-endpoint](https://docs.aws.amazon.com/cli/latest/reference/ec2/create-vpc-endpoint.html) (AWS CLI)
+ [New-EC2VpcEndpoint](https://docs.aws.amazon.com/powershell/latest/reference/items/New-EC2VpcEndpoint.html) (Tools for Windows PowerShell)