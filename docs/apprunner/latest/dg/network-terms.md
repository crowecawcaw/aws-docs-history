# Terminology

In order to know how to customize your network traffic to suit your needs, let’s understand the following terms that are used in this chapter.

## General Terms

To know what is needed to associate with an Amazon Virtual Private Cloud (VPC), let’s understand the following terms:

- _VPC_: An _Amazon VPC_ is a logically isolated virtual network that gives you complete control over your virtual networking environment, including resource placement, connectivity, and security. It is a virtual network that closely resembles a traditional network that you'd operate in your own data center.
- _VPC interface endpoint_: _VPC interface endpoint_, an AWS PrivateLink resource, connects a
  VPC to an endpoint service. Create a VPC interface endpoint to send traffic to endpoint services that use a Network Load Balancer to distribute traffic. Traffic destined for the endpoint service is resolved using DNS.
- _Regions_: Each _Region_ is a separate geographic area where you can host an App Runner service.
- _Availability Zones_: An _Availability Zone_ is an isolated location within an AWS Region. It is one or more discrete data centers with redundant power, networking, and connectivity. Availability Zones help you to make production applications highly available, fault tolerant, and scalable.
- _Subnets_: A _subnet_ is a range of IP addresses in your VPC. A subnet must reside in a single Availability
  Zone. You can launch an AWS resource into a specified subnet. Use a public subnet for resources that must be connected to the internet, and a private subnet for resources that won't be connected to the internet.
- _Security groups_: A _security group_ controls the traffic that is allowed to reach and leave the resources that
  it is associated with. Security groups provide an additional layer of security to protect the AWS resources in each subnet, giving you more control
  over your network traffic. When you create a VPC, it comes with a default security group. You can create additional security groups for each VPC. You
  can associate a security group only with resources within the VPC for which it is created.
- _Dual-stack_: A _dual-stack_ is an address type that supports network traffic from both IPv4 and IPv6 endpoints.

## Term specific to configuring outgoing traffic

VPC Connector

A _VPC Connector_ is an App Runner resource that enables App Runner service to access applications that run in a private Amazon VPC.

## Terms specific to configuring incoming traffic

To know how you can make your services privately accessible only from within an Amazon VPC, let’s understand the following terms:

- _VPC Ingress Connection_: _VPC Ingress Connection_ is an App Runner resource that provides an App Runner endpoint for incoming traffic. App Runner assigns the VPC Ingress
  Connection resource behind the scenes when you choose **Private endpoint** on the App Runner console for your
  incoming traffic. The VPC Ingress Connection resource connects your App Runner service to the VPC interface endpoint of the Amazon VPC.

###### Note

If you are using App Runner API, the VPC Ingress Connection resource is not automatically created.

- _Private endpoint_: _Private endpoint_ is an App Runner console option that you select to configure the incoming
  network traffic to be accessible from only within an Amazon VPC.
