# Release: Elastic Beanstalk supports IPv6 in dualstack configuration for Application and Network Load Balancers on September 9, 2025

AWS Elastic Beanstalk adds support for IPv6 network protocol with dual stack configuration for Application and Network Load Balancers.

**Release date:** September 9, 2025

## Changes

Elastic Beanstalk now offers support for your environment to serve both IPv4 and IPv6 protocols by
providing the dual-stack configuration option for Application and Network Load Balancers.
Elastic Beanstalk will automatically configure your load balancer with dual-stack support when you set the
`aws:elbv2:loadbalancer` namespace option `IpAddressType` to
_dualstack_.

This feature is available in all AWS Regions where Elastic Beanstalk is supported.

For more information, see [Configuring dual-stack Elastic Beanstalk load balancers](../dg/environments-cfg-elbv2-ipv6-dualstack.md "../dg/environments-cfg-elbv2-ipv6-dualstack.md") in the _AWS Elastic Beanstalk Developer Guide_.
