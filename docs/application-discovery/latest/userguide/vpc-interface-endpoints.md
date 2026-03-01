AWS Application Discovery Service is no longer open to new customers. Alternatively, use AWS Transform which provides similar capabilities. For more information, see [AWS Application Discovery Service availability change](application-discovery-service-availability-change.md "application-discovery-service-availability-change.md").

# Access AWS Application Discovery Service using an interface endpoint (AWS PrivateLink)

You can use AWS PrivateLink to create a private connection between your VPC and
AWS Application Discovery Service. You can access Application Discovery Service as if it were in your VPC, without the use of an
internet gateway, NAT device, VPN connection, or Direct Connect connection. Instances in your VPC
don't need public IP addresses to access Application Discovery Service.

You establish this private connection by creating an _interface
endpoint_, powered by AWS PrivateLink. We create an endpoint network interface
in each subnet that you enable for the interface endpoint. These are requester-managed
network interfaces that serve as the entry point for traffic destined for Application Discovery Service.

For more information, see [Access AWS services
through AWS PrivateLink](../../../vpc/latest/privatelink/privatelink-access-aws-services.md "../../../vpc/latest/privatelink/privatelink-access-aws-services.md") in the
_AWS PrivateLink Guide_.

## Considerations for Application Discovery Service

Before you set up an interface endpoint for Application Discovery Service, review [Access an AWS service using an interface VPC endpoint](../../../vpc/latest/privatelink/create-interface-endpoint.md#considerations-interface-endpoints "../../../vpc/latest/privatelink/create-interface-endpoint.md#considerations-interface-endpoints") in the
_AWS PrivateLink Guide_.

Application Discovery Service supports two interfaces: One for making calls to all of its API actions, and
a second one for the Agentless Collector and AWS Application Discovery Agent to send discovery
data.

## Create an interface endpoint

You can create an interface endpoint using either the Amazon VPC console or the AWS Command Line Interface
(AWS CLI). For more information, see [Access an AWS service using an interface VPC endpoint](../../../vpc/latest/privatelink/create-interface-endpoint.md#create-interface-endpoint-aws "../../../vpc/latest/privatelink/create-interface-endpoint.md#create-interface-endpoint-aws") in the
_AWS PrivateLink Guide_.

For Application Discovery Service
Create an interface endpoint for Application Discovery Service using the following service
name:

```
com.amazonaws.`region`.discovery
```

If you enable private DNS for the interface endpoint, you can make API
requests to Application Discovery Service using its default Regional DNS name. For example,
`discovery.us-east-1.amazonaws.com`.

For Agentless Collector and AWS Application Discovery Agent
Create an interface endpoint using the following service name:

```
com.amazonaws.`region`.arsenal-discovery
```

If you enable private DNS for the interface endpoint, you can make API
requests to Application Discovery Arsenal using its default Regional DNS
name. For example,
`arsenal-discovery.us-east-1.amazonaws.com`.

## Create an endpoint policy for your interface endpoint

An endpoint policy is an IAM resource that you can attach to an interface endpoint.
The default endpoint policy allows full access to an AWS service through the interface
endpoint. To control the access allowed to an AWS service from your VPC, attach a
custom endpoint policy to the interface endpoint.

An endpoint policy specifies the following information:

- The principals that can perform actions (AWS accounts, IAM users, and
  IAM roles).
- The actions that can be performed.

For more information, see [Control access to services using endpoint policies](../../../vpc/latest/privatelink/vpc-endpoints-access.md "../../../vpc/latest/privatelink/vpc-endpoints-access.md") in the
_AWS PrivateLink Guide_.

###### Example: VPC endpoint policies

The following is an example of a custom endpoint policy. When you attach this
policy to your interface endpoint, it grants access to the listed actions for all
principals on all resources.

Example policy for Application Discovery Service

```
{
   "Statement": [
      {
         "Principal": "*",
         "Effect": "Allow",
         "Action": [
            "discovery:`action-1`",
            "discovery:`action-2`",
            "discovery:`action-3`"
         ],
         "Resource":"*"
      }
   ]
}
```

Example policy for the Agentless Collector and
AWS Application Discovery Agent

```
{
   "Statement": [
      {
         "Principal": "*",
         "Effect": "Allow",
         "Action": [
            "arsenal:RegisterOnPremisesAgent"
         ],
         "Resource":"*"
      }
   ]
}
```

## Using the VPC endpoint for the Agentless Collector and AWS Application Discovery Agent

The Agentless Collector and AWS Application Discovery Agent don't support configurable
endpoints. Instead, use the private DNS feature for the `arsenal-discovery`
Amazon VPC endpoint.

- Set up the Direct Connect route table to route private AWS IP addresses to the VPC.
  For example, destination = 10.0.0.0/8 and target = local. For this setup you
  need at least routing for the `arsenal-discovery` Amazon VPC endpoint
  private IP addresses to the VPC.
- Use the `arsenal-discovery` Amazon VPC endpoint private DNS feature
  because the Agentless Collector doesn't support configurable Arsenal
  endpoints.
- Set up the `arsenal-discovery` Amazon VPC endpoint in a private subnet
  with the same VPC to which you are routing the Direct Connect traffic.
- Set up the `arsenal-discovery` Amazon VPC endpoint with a security group
  that enables inbound traffic from within the VPC (for example,
  10.0.0.0/8).
- Set up an Amazon Route 53 inbound resolver to route DNS resolution for the
  `arsenal-discovery` Amazon VPC endpoint private DNS name, which will
  resolve to the private IP of the VPC endpoint. If you don't do that, the
  collector will perform DNS resolution by using the on-premises resolver and will
  use the public Arsenal endpoint, and traffic will not go through the VPC.
- If you have all public traffic disabled, the auto-update feature will fail.
  That is because the Agentless Collector retrieves updates by sending
  requests to the Amazon ECR endpoint. To get the auto-update feature working without
  sending requests over the public internet, set up a VPC endpoint for the Amazon ECR
  service and enable the private DNS feature for this endpoint.
