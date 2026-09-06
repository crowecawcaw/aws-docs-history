

AWS App Runner is no longer open to new customers. Existing customers can continue to use the service as normal. For more information, see [AWS App Runner availability change](https://docs.aws.amazon.com/apprunner/latest/dg/apprunner-availability-change.html).

# Terminology
<a name="network-terms"></a>

In order to know how to customize your network traffic to suit your needs, let’s understand the following terms that are used in this chapter.

## General Terms
<a name="network-terms.general"></a>

To know what is needed to associate with an Amazon Virtual Private Cloud (VPC), let’s understand the following terms:
+  *VPC*: An *Amazon VPC* is a logically isolated virtual network that gives you complete control over your virtual networking environment, including resource placement, connectivity, and security. It is a virtual network that closely resembles a traditional network that you'd operate in your own data center. 
+  *VPC interface endpoint*: *VPC interface endpoint*, an AWS PrivateLink resource, connects a VPC to an endpoint service. Create a VPC interface endpoint to send traffic to endpoint services that use a Network Load Balancer to distribute traffic. Traffic destined for the endpoint service is resolved using DNS. 
+  *Regions*: Each *Region* is a separate geographic area where you can host an App Runner service. 
+  *Availability Zones*: An *Availability Zone* is an isolated location within an AWS Region. It is one or more discrete data centers with redundant power, networking, and connectivity. Availability Zones help you to make production applications highly available, fault tolerant, and scalable. 
+  *Subnets*: A *subnet* is a range of IP addresses in your VPC. A subnet must reside in a single Availability Zone. You can launch an AWS resource into a specified subnet. Use a public subnet for resources that must be connected to the internet, and a private subnet for resources that won't be connected to the internet. 
+  *Security groups*: A *security group* controls the traffic that is allowed to reach and leave the resources that it is associated with. Security groups provide an additional layer of security to protect the AWS resources in each subnet, giving you more control over your network traffic. When you create a VPC, it comes with a default security group. You can create additional security groups for each VPC. You can associate a security group only with resources within the VPC for which it is created. 
+  *Dual-stack*: A *dual-stack* is an address type that supports network traffic from both IPv4 and IPv6 endpoints. 

## Term specific to configuring outgoing traffic
<a name="network-terms.egress"></a>

VPC Connector

A *VPC Connector* is an App Runner resource that enables App Runner service to access applications that run in a private Amazon VPC. 

## Terms specific to configuring incoming traffic
<a name="network-terms.ingress"></a>

To know how you can make your services privately accessible only from within an Amazon VPC, let’s understand the following terms:
+  *VPC Ingress Connection*: *VPC Ingress Connection* is an App Runner resource that provides an App Runner endpoint for incoming traffic. App Runner assigns the VPC Ingress Connection resource behind the scenes when you choose **Private endpoint** on the App Runner console for your incoming traffic. The VPC Ingress Connection resource connects your App Runner service to the VPC interface endpoint of the Amazon VPC. 
**Note**  
 If you are using App Runner API, the VPC Ingress Connection resource is not automatically created. 
+  *Private endpoint*: *Private endpoint* is an App Runner console option that you select to configure the incoming network traffic to be accessible from only within an Amazon VPC. 