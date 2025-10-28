# Configuring network firewalls for the RFDK

##

###### Important

On November 7, 2025, AWS Thinkbox Deadline 10 will enter maintenance mode. We recommend exploring [AWS Deadline Cloud](https://aws.amazon.com/deadline-cloud/ "https://aws.amazon.com/deadline-cloud/") for render management. For questions, contact [support@awsthinkbox.zendesk.com](mailto:support@awsthinkbox.zendesk.com "mailto:support@awsthinkbox.zendesk.com") or refer to the [Maintenance Mode FAQ](https://docs.thinkboxsoftware.com/products/deadline/latest/1_User%20Manual/manual/maintenance-mode-faq.html "https://docs.thinkboxsoftware.com/products/deadline/latest/1_User%20Manual/manual/maintenance-mode-faq.html").

A firewall is a network (virtual) device that governs a network or host. It is used to restrict only specific traffic from entering or exiting the firewall. Firewalls are typically
configured with rules that indicate whether traffic directed to/from a specific network address/port is allowed or blocked.

It is recommended that firewalls are used, and that they are configured to restrict traffic to the minimum required access for the render farm to function properly. Doing
this can reduce the risk of malicious network activity.

AWS provides multiple levels of network firewalls described in the sections below.

## Network access control lists (ACLs)

[Network ACLs](../../../vpc/latest/userguide/vpc-network-acls.md "../../../vpc/latest/userguide/vpc-network-acls.md") are firewalls that govern a VPC subnet. It is recommended that you use Network ACLs that are
scoped to restrict traffic to enter/exit a VPC subnet to only the traffic that is required for normal operation of your render farm. Determining the Network ACL rules requires an
understanding of the software that is running on the instances within the subnets and what network connectivity they require outside of the subnet.

Refer to the [Security best practices for your VPC](../../../vpc/latest/userguide/vpc-security-best-practices.md "../../../vpc/latest/userguide/vpc-security-best-practices.md") for more details.

## Security groups

[Security Groups](../../../AWSEC2/latest/UserGuide/ec2-security-groups.md "../../../AWSEC2/latest/UserGuide/ec2-security-groups.md") are firewalls that govern one or more instance(s). They are used to restrict network
traffic between the instance(s) within the security group and outside peers.
