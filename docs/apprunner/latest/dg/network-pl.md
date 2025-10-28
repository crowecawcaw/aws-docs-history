# Enabling Private endpoint for incoming traffic

By default when you create an AWS App Runner service, the service is accessible over the internet.
However, you can also make your App Runner service private and only accessible from within an
Amazon Virtual Private Cloud (Amazon VPC).

With your App Runner service private, you have complete control over incoming traffic, adding an
additional layer of security. This is helpful in a variety of use cases, including running
internal APIs, corporate web applications, or applications that are still in development that
require a greater level of privacy and security, or have the need to meet specific compliance
requirements.

###### Note

If your App Runner application requires source IP/CIDR incoming traffic control rules, you must use security group rules for private endpoints instead of [WAF web ACLs](waf.md "waf.md"). This is because we currently don’t support forwarding request source IP data to App Runner private services associated with
WAF. As a result, source IP rules for App Runner private services that are associated with WAF web ACLs do not adhere to IP based rules.

To learn more about infrastructure security and security groups, including best practices, see the following topics in the
_Amazon VPC User Guide_: [Control
network traffic](../../../vpc/latest/userguide/infrastructure-security.md#control-network-traffic "../../../vpc/latest/userguide/infrastructure-security.md#control-network-traffic") and [Control traffic to your AWS resources using
security groups](../../../vpc/latest/userguide/vpc-security-groups.md "../../../vpc/latest/userguide/vpc-security-groups.md").

When your App Runner service is private, you can access your service from within an Amazon VPC. An
internet gateway, NAT device, or VPN connection isn’t required.

###### Note

App Runner supports IPv4 and dual-stack, (both IPv4 and IPv6), for both incoming traffic and
outgoing traffic.

## Considerations

- Before you set up a VPC interface endpoint for App Runner, review [Considerations](../../../vpc/latest/privatelink/create-interface-endpoint.md#considerations-interface-endpoints "../../../vpc/latest/privatelink/create-interface-endpoint.md#considerations-interface-endpoints") in the _AWS PrivateLink Guide_.
- VPC endpoint policies are not supported for App Runner. By default, full access to App Runner is
  allowed through the VPC interface endpoint. Alternatively, you can associate a security
  group with the endpoint network interfaces to control traffic to App Runner through the VPC
  interface endpoint.
- If your App Runner application requires source IP/CIDR incoming traffic control rules, you must use security group rules for private endpoints instead of [WAF web ACLs](waf.md "waf.md"). This is because we currently don’t support forwarding request source IP data to App Runner private services associated with
  WAF. As a result, source IP rules for App Runner private services that are associated with WAF web ACLs do not adhere to IP based rules.
- After you enable a Private endpoint, your service is only accessible from your VPC,
  and can’t be accessed from the internet.
- For higher availability, it's recommended that you select at least two subnets across
  Availability Zone different for the VPC interface endpoint. We don’t recommend using only
  one subnet.
- If you're choosing the dual stack option for the IP address type, ensure your subnets can support dual-stack traffic.
- You can use the same VPC interface endpoint to access multiple App Runner services in a
  VPC.

For information on the terms used in this section, see [Terminology](network-terms.md "network-terms.md").

## Permissions

The following is the list of permissions required to enable **Private
endpoint**:

- ec2:CreateTags
- ec2:CreateVpcEndpoint
- ec2:ModifyVpcEndpoint
- ec2:DeleteVpcEndpoints
- ec2:DescribeSubnets
- ec2:DescribeVpcEndpoints
- ec2:DescribeVpcs

## VPC interface endpoint

A VPC interface endpoint is an _AWS PrivateLink_ resource that connects
an Amazon VPC to an endpoint service. You can specify which Amazon VPC you would like your App Runner service
to be accessible in by passing a VPC interface endpoint. To create a VPC interface endpoint
specify the following:

- The Amazon VPC to enable the connectivity.
- Add Security groups. By default, a security group is assigned to VPC interface
  endpoint. You can choose to associate a custom security group to bring further control to
  incoming network traffic.
- Add subnets. To ensure higher availability, it is recommended to select at least two
  subnets for each Availability Zone from which you’ll access the App Runner service. A network
  interface endpoint is created in each subnet that you enable for the VPC interface
  endpoint. These are requester-managed network interfaces that serve as the entry point for
  traffic destined for App Runner. A requester-managed network interface is a network interface
  that an AWS service creates in your VPC on your behalf.
- If you are using the API, add the App Runner VPC interface endpoint
  `Servicename`. For example,

```
com.amazonaws.`region`.apprunner.requests
```

You can create a VPC interface endpoint using one of the following AWS services:

- App Runner console. For more information, see [Manage
  Private endpoint](network-pl-manage.md "network-pl-manage.md").
- Amazon VPC console or API, and AWS Command Line Interface (AWS CLI). For more information, see [Access AWS services
  through AWS PrivateLink](../../../vpc/latest/privatelink/privatelink-access-aws-services.md "../../../vpc/latest/privatelink/privatelink-access-aws-services.md") in the _AWS PrivateLink Guide_.

###### Note

You’re charged for each VPC interface endpoint that you use based on [AWS PrivateLink Pricing](https://aws.amazon.com/privatelink/pricing/ "https://aws.amazon.com/privatelink/pricing/").
Therefore, for better cost efficiency, you can use the same VPC interface endpoint to access
multiple App Runner services within a VPC. However, for better isolation, consider associating a
different VPC interface endpoint for each of your App Runner services.

## VPC Ingress Connection

A _VPC Ingress Connection_ is an App Runner resource that specifies an App Runner
endpoint for incoming traffic. App Runner assigns the VPC Ingress Connection resource behind the
scenes when you choose **Private endpoint** on the App Runner console for your
incoming traffic. Choose this option to only allow traffic from an Amazon VPC to access your App Runner
service. The VPC Ingress Connection resource connects your App Runner service to the VPC interface
endpoint of the Amazon VPC. You can create a VPC Ingress Connection resource only if you are using
the API operations to configure the network settings for incoming traffic. For more
information how to create VPC Ingress Connection resource, see [CreateVpcIngressConnection](../api/API_CreateVpcIngressConnection.md "../api/API_CreateVpcIngressConnection.md") in the _AWS App Runner API Reference_.

###### Note

One VPC Ingress Connection resource of the App Runner can connect to one VPC interface
endpoint of the Amazon VPC. Also, you can only create one VPC Ingress Connection resource for
each App Runner service.

## Private endpoint

Private endpoint is an App Runner console option that you can choose if you only want to receive
incoming traffic from an Amazon VPC. Choosing the **Private endpoint** option on
the App Runner console provides you with the option to connect your service to a VPC by configuring
its _VPC interface endpoint_. Behind the scenes, App Runner assigns a VPC Ingress
Connection resource to the VPC interface endpoint that you configure.

## Summary

Make your service private by only allowing traffic from an Amazon VPC to access your App Runner
service. To achieve this, you create a VPC interface endpoint for the selected Amazon VPC using
either App Runner or Amazon VPC. On the App Runner console, you create a VPC interface endpoint when you enable
the **Private endpoint** for the **Incoming traffic**. App Runner
then automatically creates a _VPC Ingress Connection_ resource and connects
to the VPC interface endpoint and your App Runner service. This creates a private service connection
that ensures that only traffic from the selected VPC can access your App Runner service.
