# Create an inspection system as a Gateway Load Balancer endpoint service

You can create your own service powered by AWS PrivateLink, known as an _endpoint service_.
You are the service provider, and the AWS principals that create connections to your service are the
service consumers.

Endpoint services require either a Network Load Balancer or a Gateway Load Balancer. In this case, you'll create an endpoint service
using a Gateway Load Balancer. For more information about creating an endpoint service using a Network Load Balancer, see [Create an endpoint service](create-endpoint-service.md "create-endpoint-service.md").

###### Contents

- [Considerations](#considerations-gateway-load-balancer-endpoint-service "#considerations-gateway-load-balancer-endpoint-service")
- [Prerequisites](#prerequisites-gateway-load-balancer-endpoint-service "#prerequisites-gateway-load-balancer-endpoint-service")
- [Create the endpoint service](#create-endpoint-service-glb "#create-endpoint-service-glb")
- [Make your endpoint service available](#share-gateway-load-balancerendpoint-service "#share-gateway-load-balancerendpoint-service")

## Considerations

- An endpoint service is available in the Region where you created it.
- When service consumers retrieve information about an endpoint service, they can
  see only the Availability Zones that they have in common with the service provider.
  When the service provider and service consumer are in different accounts, an
  Availability Zone name, such as `us-east-1a`, might be mapped to a
  different physical Availability Zone in each AWS account. You can use AZ IDs
  to consistently identify the Availability Zones for your service. For more information,
  see [AZ IDs](../../../AWSEC2/latest/UserGuide/using-regions-availability-zones.md#az-ids "../../../AWSEC2/latest/UserGuide/using-regions-availability-zones.md#az-ids")
  in the _Amazon EC2 User Guide_.
- There are quotas on your AWS PrivateLink resources. For more information, see
  [AWS PrivateLink quotas](vpc-limits-endpoints.md "vpc-limits-endpoints.md").

## Prerequisites

- Create a service provider VPC with at least two subnets in the Availability Zone
  in which the service should be available. One subnet is for the security appliance
  instances and the other is for the Gateway Load Balancer.
- Create a Gateway Load Balancer in your service provider VPC. If you plan to enable IPv6 support on
  your endpoint service, you must enable dualstack support on your Gateway Load Balancer. For more
  information, see [Getting started with
  Gateway Load Balancers](../../../elasticloadbalancing/latest/gateway/getting-started.md "../../../elasticloadbalancing/latest/gateway/getting-started.md").
- Launch security appliances in the service provider VPC and register them with
  a load balancer target group.

## Create the endpoint service

Use the following procedure to create an endpoint service using a Gateway Load Balancer.

###### To create an endpoint service using the console

1. Open the Amazon VPC console at
   [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
2. In the navigation pane, choose **Endpoint services**.
3. Choose **Create endpoint service**.
4. For **Load balancer type**, choose
   **Gateway**.
5. For **Available load balancers**, select your Gateway Load Balancer.
6. For **Require acceptance for endpoint**, select
   **Acceptance required** to require that connection requests to your
   endpoint service are accepted manually. Otherwise, they are accepted
   automatically.
7. For **Supported IP address types**, do one of the following:
   - Select **IPv4** – Enable the endpoint service to accept
     IPv4 requests.
   - Select **IPv6** – Enable the endpoint service to accept
     IPv6 requests.
   - Select **IPv4** and **IPv6** – Enable the
     endpoint service to accept both IPv4 and IPv6 requests.

8. (Optional) To add a tag, choose **Add new tag** and
   enter the tag key and the tag value.
9. Choose **Create**.

###### To create an endpoint service using the command line

- [create-vpc-endpoint-service-configuration](../../../cli/latest/reference/ec2/create-vpc-endpoint-service-configuration.md "../../../cli/latest/reference/ec2/create-vpc-endpoint-service-configuration.md") (AWS CLI)
- [New-EC2VpcEndpointServiceConfiguration](../../../powershell/latest/reference/items/New-EC2VpcEndpointServiceConfiguration.md "../../../powershell/latest/reference/items/New-EC2VpcEndpointServiceConfiguration.md") (Tools for Windows PowerShell)

## Make your endpoint service available

Service providers must do the following to make their services available to service
consumers.

- Add permissions that allow each service consumer to connect to your endpoint
  service. For more information, see [Manage permissions](configure-endpoint-service.md#add-remove-permissions "configure-endpoint-service.md#add-remove-permissions").
- Provide the service consumer with the name of your service and the supported
  Availability Zones so that they can create an interface endpoint to connect to
  your service. For more information, see the procedure below.
- Accept the endpoint connection request from the service consumer. For more
  information see [Accept or reject connection requests](configure-endpoint-service.md#accept-reject-connection-requests "configure-endpoint-service.md#accept-reject-connection-requests").

AWS principals can connect to your endpoint service privately by creating a Gateway Load Balancer endpoint.
For more information, see [Create a Gateway Load Balancer endpoint](gateway-load-balancer-endpoints.md "gateway-load-balancer-endpoints.md").
