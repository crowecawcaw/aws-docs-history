# Access an AWS service using an interface VPC

endpoint

You can create an interface VPC endpoint to connect to services powered by AWS PrivateLink,
including many AWS services. For an overview, see [AWS PrivateLink concepts](concepts.md "concepts.md") and [Access AWS services through
AWS PrivateLink](privatelink-access-aws-services.md "privatelink-access-aws-services.md").

For each subnet that you specify from your VPC, we create an endpoint network interface in
the subnet and assign it a private IP address from the subnet address range. An endpoint
network interface is a requester-managed network interface; you can view it in your
AWS account, but you can't manage it yourself.

You are billed for hourly usage and data processing charges. For more
information, see [Interface endpoint pricing](https://aws.amazon.com/privatelink/pricing/#Interface_Endpoint_pricing "https://aws.amazon.com/privatelink/pricing/#Interface_Endpoint_pricing").

###### Contents

- [Prerequisites](#prerequisites-interface-endpoints "#prerequisites-interface-endpoints")
- [Create a VPC endpoint](#create-interface-endpoint-aws "#create-interface-endpoint-aws")
- [Shared subnets](#interface-endpoint-shared-subnets "#interface-endpoint-shared-subnets")
- [ICMP](#interface-endpoint-icmp "#interface-endpoint-icmp")

## Prerequisites

- Deploy the resources that will access the AWS service in your VPC.
- To use private DNS, you must enable DNS hostnames and DNS resolution for your VPC.
  For more information, see [View
  and update DNS attributes](../userguide/vpc-dns.md#vpc-dns-updating "../userguide/vpc-dns.md#vpc-dns-updating") in the _Amazon VPC User Guide_.
- To enable IPv6 for an interface endpoint, the AWS service must support access over
  IPv6. For more information, see [IP address types](privatelink-access-aws-services.md#aws-service-ip-address-type "privatelink-access-aws-services.md#aws-service-ip-address-type").
- Create a security group for the endpoint network interface that allows the expected
  traffic from the resources in your VPC. For example, to ensure that the AWS CLI can send
  HTTPS requests to the AWS service, the security group must allow inbound HTTPS
  traffic.
- If your resources are in a subnet with a network ACL, verify that the network ACL
  allows traffic between the resources in your VPC and the endpoint network
  interfaces.
- There are quotas on your AWS PrivateLink resources. For more information, see [AWS PrivateLink quotas](vpc-limits-endpoints.md "vpc-limits-endpoints.md").

## Create a VPC endpoint

Use the following procedure to create an interface VPC endpoint that connects to an
AWS service.

###### To create an interface endpoint for an AWS service

1. Open the Amazon VPC console at
   [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/ "https://console.aws.amazon.com/vpc/").
2. In the navigation pane, choose **Endpoints**.
3. Choose **Create endpoint**.
4. For **Type**, choose **AWS services**.
5. For **Service name**, select the service. For more information, see
   [AWS services that integrate with
   AWS PrivateLink](aws-services-privatelink-support.md "aws-services-privatelink-support.md").
6. For **VPC**, select the VPC from which you'll access the
   AWS service.
7. If, in Step 5, you selected the service name for Amazon S3, and if you want to configure
   [private DNS support](vpc-endpoints-s3.md#private-dns-s3 "vpc-endpoints-s3.md#private-dns-s3"), select **Additional
   settings**, **Enable DNS name**. When you make this
   selection, it also automatically selects **Enable private DNS only for inbound
   endpoint**. You can configure private DNS with an inbound Resolver endpoint
   only for interface endpoints for Amazon S3. If you do not have a gateway endpoint for Amazon S3
   and you select **Enable private DNS only for inbound endpoint**, you'll
   receive an error when you attempt the final step in this procedure.

If, in Step 5, you selected the service name for any service other than Amazon S3,
**Additional settings**, **Enable DNS name** is
already selected. We recommend that you keep the default. This ensures that requests
that use the public service endpoints, such as requests made through an AWS SDK,
resolve to your VPC endpoint. 8. For **Subnets**, select the subnets in which to create endpoint
network interfaces. You can select one subnet per Availability Zone. You can't select
multiple subnets from the same Availability Zone. For more information, see [Subnets and Availability Zones](privatelink-access-aws-services.md#aws-service-subnets-zones "privatelink-access-aws-services.md#aws-service-subnets-zones").

By default, we select IP addresses from the subnet IP address ranges and assign them
to the endpoint network interfaces. To choose the IP addresses yourself, select
**Designate IP addresses**. Note that the first four IP addresses and
the last IP address in a subnet CIDR block are reserved for internal use, so you can't
specify them for your endpoint network interfaces. 9. For **IP address type**, choose from the following options:

    * **IPv4** – Assign IPv4 addresses to the endpoint network
     interfaces. This option is supported only if all selected subnets have IPv4 address
     ranges and the service accepts IPv4 requests.
    * **IPv6** – Assign IPv6 addresses to the endpoint network
     interfaces. This option is supported only if all selected subnets are IPv6 only
     subnets and the service accepts IPv6 requests.
    * **Dualstack** – Assign both IPv4 and IPv6 addresses to
     the endpoint network interfaces. This option is supported only if all selected
     subnets have both IPv4 and IPv6 address ranges and the service accepts both IPv4 and
     IPv6 requests.

10. For **Security groups**, select the security groups to associate
    with the endpoint network interfaces. By default, we associate the default security
    group for the VPC.
11. For **Policy**, to allow all operations by all principals on all
    resources over the interface endpoint, select **Full access**. To
    restrict access, select **Custom** and enter a policy. This option is
    available only if the service supports VPC endpoint policies. For more information, see
    [Endpoint policies](vpc-endpoints-access.md "vpc-endpoints-access.md").
12. (Optional) To add a tag, choose **Add new tag** and enter the tag
    key and the tag value.
13. Choose **Create endpoint**.

###### To create an interface endpoint using the command line

- [create-vpc-endpoint](../../../cli/latest/reference/ec2/create-vpc-endpoint.md "../../../cli/latest/reference/ec2/create-vpc-endpoint.md")
  (AWS CLI)
- [New-EC2VpcEndpoint](../../../powershell/latest/reference/items/New-EC2VpcEndpoint.md "../../../powershell/latest/reference/items/New-EC2VpcEndpoint.md")
  (Tools for Windows PowerShell)

## Shared subnets

You can't create, describe, modify, or delete VPC endpoints in subnets that are shared
with you. However, you can use the VPC endpoints in subnets that are shared with you.

## ICMP

Interface endpoints do not respond to **ping** requests. You can use the
**nc** or **nmap** commands instead.
