# Using Elastic Beanstalk with VPC endpoints

This topic explains the benefits that a VPC endpoint can offer your Elastic Beanstalk application. It
also provides instructions to create an interface VPC endpoint to an Elastic Beanstalk service.

A VPC endpoint enables you to privately connect your VPC to supported AWS services and VPC
endpoint services powered by AWS PrivateLink, without requiring an internet gateway, NAT device,
VPN connection, or AWS Direct Connect connection.

Instances in your VPC don't require public IP addresses to communicate with resources in the
service. Traffic between your VPC and the other service doesn't leave the Amazon network. For
complete information about VPC endpoints, see [VPC
Endpoints](../../../vpc/latest/userguide/vpc-endpoints.md "../../../vpc/latest/userguide/vpc-endpoints.md") in the _Amazon VPC User Guide_.

AWS Elastic Beanstalk supports AWS PrivateLink, which provides private connectivity to the Elastic Beanstalk service
and eliminates exposure of traffic to the public internet. To enable your application to send
requests to Elastic Beanstalk using AWS PrivateLink, you configure a type of VPC endpoint known as an
_interface VPC endpoint_ (interface endpoint). For more information, see
[Interface VPC Endpoints (AWS PrivateLink)](../../../vpc/latest/userguide/vpce-interface.md "../../../vpc/latest/userguide/vpce-interface.md")
in the _Amazon VPC User Guide_.

###### Note

Elastic Beanstalk supports AWS PrivateLink and interface VPC endpoints in a limited number of
AWS Regions. We're working to extend support to more AWS Regions in the near
future.

## IPv6 support with dual-stack configuration

Elastic Beanstalk supports incoming traffic over IPv4 and IPv6. This section describes the public
endpoints that support both IPv4 and IPv6 and also explains how to configure your Elastic Beanstalk VPC
endpoints to support dual-stack traffic.

###### Public endpoints

The Elastic Beanstalk service has two sets of endpoints that consists of the older IPv4 endpoints
and the more recent endpoints with dual-stack capability. Both sets of endpoints follow
AWS naming standards:

- **IPv4** endpoints use the domain
  `amazonaws.com` – format for general service endpoint:
  `elasticbeanstalk.`region`.amazonaws.com`
- **Dual-stack** endpoints use the domain
  `api.aws` – format for general service endpoint::
  `elasticbeanstalk.`region`.api.aws`

The endpoints for _service health_ and _FIPS_ have different host names, but they follow the same domain
name pattern. For a list of endpoints see [Elastic Beanstalk service
endpoints](../../../general/latest/gr/elasticbeanstalk.md#elasticbeanstalk_region "../../../general/latest/gr/elasticbeanstalk.md#elasticbeanstalk_region") in the _Amazon Web Services General Reference_.

###### Requests to Elastic Beanstalk

When you send requests to the Elastic Beanstalk service with the [AWS CLI](../../../cli/latest/reference/elasticbeanstalk.md "../../../cli/latest/reference/elasticbeanstalk.md") or the [AWS SDK](https://aws.amazon.com/developer/tools/ "https://aws.amazon.com/developer/tools/") you can specify an IPv4 endpoint or a dual-stack
endpoint. The AWS CLI and AWS SDK use the IPv4-only endpoints by default if an endpoint URL
isn't specified.

The following example demonstrates the AWS CLI sending a request to a dual-stack
endpoint:

```
aws elasticbeanstalk list-available-solution-stacks \
    --endpoint-url "``https://elasticbeanstalk.us-east-1.api.aws``"
```

The following example demonstrates the AWS Python SDK sending a request to a dual-stack
endpoint:

```
import boto3

dual_stack_eb_client = boto3.client(
    service_name='`elasticbeanstalk`',
    region_name='``us-east-1'``,
    endpoint_url='``https://elasticbeanstalk.us-east-1.api.aws``';
)

print(dual_stack_eb_client.list_available_solution_stacks())
```

###### VPC endpoints for dual-stack IPs

To configure your Elastic Beanstalk VPC endpoints to support dual-stack traffic, specify
**dualstack** for the **IP address type** parameter of
the VPC endpoint. You can specify this field via the [AWS CLI](../../../cli/latest/reference/elasticbeanstalk.md "../../../cli/latest/reference/elasticbeanstalk.md"), the [AWS SDK](https://aws.amazon.com/developer/tools/ "https://aws.amazon.com/developer/tools/"), or the AWS PrivateLink console. For instructions
to do so in the AWS PrivateLink console, see [Create a VPC endpoint](../../../vpc/latest/privatelink/create-interface-endpoint.md "../../../vpc/latest/privatelink/create-interface-endpoint.md")
in the _AWS PrivateLink Guide_.

###### Note

You must specify the **IP address type** of the VPC endpoint as either
**IPv4** or **dualstack**. At this time Elastic Beanstalk VPC
endpoints don't support an **IP address type** of
**IPv6**, which would indicate IPv6-only support. The
**dualstack** option allows for both the IPv4 and IPv6 internet
protocols.

The following example demonstrates how to create a dual-stack VPC endpoint with the
AWS CLI:

```
aws ec2 create-vpc-endpoint \
    --vpc-id "``vpc-example``"
    --service-name "``com.amazonaws.us-east-1.elasticbeanstalk``"
    --ip-address-type "`dualstack`"
```

## Setting up a VPC endpoint for Elastic Beanstalk

To create the interface VPC endpoint for the Elastic Beanstalk service in your VPC, follow the [Creating an Interface
Endpoint](../../../vpc/latest/userguide/vpce-interface.md#create-interface-endpoint "../../../vpc/latest/userguide/vpce-interface.md#create-interface-endpoint") procedure.

- For **Service Name**, choose
  **com.amazonaws.`region`.elasticbeanstalk**.
- For **IP address type**, choose either **IPv4** or
  **Dualstack**. At this time Elastic Beanstalk VPC endpoints don't support an
  **IP address type** of **IPv6**, which would indicate
  IPv6-only support. The **Dualstack** option allows for both the IPv4 and
  IPv6 internet protocols.

If your VPC is configured with public internet access, your application can still access
Elastic Beanstalk over the internet using either the
`elasticbeanstalk.`region`.amazonaws.com` or the
`elasticbeanstalk.`region`.api.aws` public endpoint.
You can prevent this by ensuring that **Enable DNS name** is enabled during
endpoint creation (true by default). This adds a DNS entry in your VPC that maps the public
service endpoint to the interface VPC endpoint.

## Setting up a VPC endpoint for enhanced health

If you enabled [enhanced health reporting](health-enhanced.md "health-enhanced.md") for your
environment, you can configure enhanced health information to be sent over AWS PrivateLink too.
Enhanced health information is sent by the `healthd` daemon, an Elastic Beanstalk component on
your environment instances, to a separate Elastic Beanstalk enhanced health service. To create an
interface VPC endpoint for this service in your VPC, follow the [Creating an Interface
Endpoint](../../../vpc/latest/userguide/vpce-interface.md#create-interface-endpoint "../../../vpc/latest/userguide/vpce-interface.md#create-interface-endpoint") procedure.

- For **Service Name**, choose
  **com.amazonaws.`region`.elasticbeanstalk-health**.
- For **IP address type**, choose either **IPv4** or
  **Dualstack**. At this time Elastic Beanstalk VPC endpoints don't support an
  **IP address type** of **IPv6**, which would indicate
  IPv6-only support. The **Dualstack** option allows for both the IPv4 and
  IPv6 internet protocols.

###### Important

The `healthd` daemon sends enhanced health information to the public endpoint
`elasticbeanstalk-health.`region`.amazonaws.com` or
`elasticbeanstalk-health.`region`.api.aws`. If your
VPC is configured with public internet access, and **Enable DNS name** is
disabled for the VPC endpoint, enhanced health information travels through the public
internet. This is probably not your intention when you set up an enhanced health VPC
endpoint. Ensure that **Enable DNS name** is enabled (true by
default).

## Using VPC endpoints in a private VPC

A private VPC, or a private subnet in a VPC, has no public internet access. You might want
to run your Elastic Beanstalk environment in a [private VPC](vpc.md#services-vpc-private "vpc.md#services-vpc-private") and
configure interface VPC endpoints for enhanced security. In this case, be aware that your
environment might try to connect to the internet for other reasons in addition to contacting
the Elastic Beanstalk service. To learn more about running an environment in a private VPC, see [Running an Elastic Beanstalk environment in a private VPC](vpc.md#services-vpc-private-beanstalk "vpc.md#services-vpc-private-beanstalk").
