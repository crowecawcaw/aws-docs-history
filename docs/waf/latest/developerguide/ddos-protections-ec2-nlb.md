**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console.
For more details, see [Working with the updated console experience](working-with-console.md "working-with-console.md").

# Protecting Amazon EC2 instances and Network Load Balancers with Shield Advanced

This page explains how to use AWS Shield Advanced protections for Amazon EC2 instances and Network Load Balancers.

You can protect Amazon EC2 instances and Network Load Balancers by first attaching these resources to Elastic IP
addresses, and then protecting the Elastic IP addresses in Shield Advanced.

When you protect Elastic IP addresses, Shield Advanced identifies and protects the resources that
they're attached to. Shield Advanced automatically identifies the type of resource that's
attached to an Elastic IP address and applies the appropriate detections and mitigations
for that resource. This includes configuring network ACLs that are specific to the
Elastic IP address. For more information about using Elastic IP addresses with your
AWS resources, see the following guides: [Amazon Elastic Compute Cloud documentation](../../../ec2.md "../../../ec2.md") or
[Elastic Load Balancing documentation](../../../elasticloadbalancing.md "../../../elasticloadbalancing.md").

During an attack,
Shield Advanced automatically deploys your network ACLs to the border of the AWS network.
When your network ACLs are at the border of the network, Shield Advanced can provide
protection against larger DDoS events. Typically, network ACLs are applied near your
Amazon EC2 instances within your Amazon VPC. The network ACL can mitigate attacks only as large as
your Amazon VPC and instance can handle. For example, if the network interface attached to your Amazon EC2
instance can process up to 10 Gbps, then volumes over 10 Gbps will slow down and possibly block
traffic to that instance. During an attack, Shield Advanced promotes your network ACL to the
AWS border, which can process multiple terabytes of traffic. Your network ACL is able
to provide protection for your resource well beyond your network's typical capacity. For
more information about network ACLs, see [Network
ACLs](../../../AmazonVPC/latest/UserGuide/VPC_ACLs.md "../../../AmazonVPC/latest/UserGuide/VPC_ACLs.md").

Some scaling tools, like AWS Elastic Beanstalk, don't let you automatically attach an Elastic IP
address to a Network Load Balancer. For those cases, you need to manually attach the Elastic IP
address.
