# Configuring router and firewall

rules for Amazon Route 53 health checks

When Route 53 checks the health of an endpoint, it sends an HTTP, HTTPS, or TCP
request to the IP address and port that you specified when you created the health
check. For a health check to succeed, your router and firewall rules must allow
inbound traffic from the IP addresses that the Route 53 health checkers use.

For the current list of IP addresses for Route 53 health checkers, for Route 53 name
servers, and for other AWS services, see [IP address ranges of Amazon Route 53 servers](route-53-ip-addresses.md "route-53-ip-addresses.md").

In Amazon EC2, security groups act as firewalls. For more information, see [Amazon EC2 security groups](../../../AWSEC2/latest/UserGuide/using-network-security.md "../../../AWSEC2/latest/UserGuide/using-network-security.md") in
the _Amazon EC2 User Guide_.To configure your security groups to allow
Route 53 health checks, you can either allow inbound traffic from each IP address
range, or you can use an AWS-managed prefix list.

To use the AWS-managed prefix list, modify your security group to allow inbound traffic
from `com.amazonaws.<region>.route53-healthchecks`, where the
`<region>` is the AWS Region of your Amazon EC2 instance or resource.
If you are using Route 53 health checks to check IPv6 endpoints, you should also allow
inbound traffic from
`com.amazonaws.<region>.ipv6.route53-healthchecks`.

For more information about AWS-managed prefix lists, see [Work with AWS-managed prefix lists](../../../vpc/latest/userguide/working-with-aws-managed-prefix-lists.md "../../../vpc/latest/userguide/working-with-aws-managed-prefix-lists.md") in the _Amazon VPC User Guide_.

###### Important

When you add IP addresses to a list of allowed IP addresses, add all the IP addresses in
the CIDR range for each AWS Region that you specified when you created health
checks, as well as the Global CIDR range. You might see that health check
requests come from just one IP address in a Region. However, that IP address can
change at any time to another of the IP addresses for that Region.

If you want to make sure that you include both the current and older health
checker IP addresses, add ALL /26 and /18 IP address ranges to the allow list.
For a complete list, see [AWS IP address ranges](../../../general/latest/gr/aws-ip-ranges.md "../../../general/latest/gr/aws-ip-ranges.md")
in the _AWS General Reference_.

When you add the AWS-managed prefix list to your inbound security group, it automatically adds
all necessary ranges.
