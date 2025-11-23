# Tutorial: Bring your IP addresses to IPAM

The tutorials in this section walk you through the process of bringing public IP address space to AWS and managing the space with IPAM.

Managing public IP address space with IPAM has the following benefits:

- **Improves public IP addresses utilization across your
  organization**: You can use IPAM to share IP address space across AWS
  accounts. Without using IPAM, you cannot share your public IP space across AWS
  Organizations accounts.
- **Simplifies the process of bringing public IP space to AWS**:
  You can use IPAM to onboard public IP address space once, and then use IPAM to
  distribute your public IPs across Regions to resources like EC2 instances and [application load balancers](../../../elasticloadbalancing/latest/application/load-balancer-ip-pools.md "../../../elasticloadbalancing/latest/application/load-balancer-ip-pools.md"). Without IPAM, you have to onboard your
  public IPs for each AWS Region.

###### Contents

- [Verify domain
  control](tutorials-byoip-ipam-domain-verification-methods.md "tutorials-byoip-ipam-domain-verification-methods.md")
- [Bring your own IP to IPAM using both the AWS Management Console and the AWS CLI](tutorials-byoip-ipam-console-intro.md "tutorials-byoip-ipam-console-intro.md")
- [Bring your own IP CIDR to IPAM using only the AWS CLI](tutorials-byoip-ipam-cli-only-intro.md "tutorials-byoip-ipam-cli-only-intro.md")
- [Bring your own IP to CloudFront using IPAM](tutorials-byoip-cloudfront.md "tutorials-byoip-cloudfront.md")
