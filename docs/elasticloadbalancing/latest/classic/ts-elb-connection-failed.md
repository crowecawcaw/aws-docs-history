# Troubleshoot a Classic Load Balancer: Client connectivity

## Clients cannot connect to an internet-facing

load balancer

If the load balancer is not responding to requests, check for the following
issues:

**Your internet-facing load balancer is attached to a private subnet**

You must specify public subnets for your load balancer. A public subnet
has a route to the internet gateway for your virtual private cloud
(VPC).

**A security group or network ACL does not allow traffic**

The security group for the load balancer and any network ACLs for the load
balancer subnets must allow inbound traffic from the clients and outbound
traffic to the clients on the listener ports. For more information, see [Configure security groups for your Classic Load Balancer](elb-vpc-security-groups.md "elb-vpc-security-groups.md").

## Requests sent to a custom domain aren't received by the load balancer

If the load balancer is not receiving requests sent to a custom domain, check for the following issues:

**The custom domain name does not resolve to the load balancer IP address**

- Confirm what IP address the custom domain name resolves to using a command line interface.
  - Linux, macOS, or Unix – You can use the `dig` command within Terminal. Ex.`dig example.com`
  - Windows – You can use the `nslookup` command within Command Prompt. Ex.`nslookup example.com`

- Confirm what IP address the load balancers DNS name resolves to using a command line interface.
- Compare the results of the two outputs. The IP addresses need to match.

## HTTPS requests sent to the load balancer return "NET::ERR_CERT_COMMON_NAME_INVALID"

If HTTPS requests are receiving `NET::ERR_CERT_COMMON_NAME_INVALID` from the load balancer, check the following possible causes:

- The domain name used in the HTTPS request does not match the alternate name specified in the listeners associated ACM certificate.
- The load balancers default DNS name is being used. The default DNS name cannot be used to
  make HTTPS requests as a public certificate cannot be requested for the `*.amazonaws.com` domain.
