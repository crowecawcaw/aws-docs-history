

# Release: Elastic Beanstalk supports IPv6 in dualstack configuration for Application and Network Load Balancers on September 9, 2025
<a name="release-2025-09-09-ipv6-dualstack-lb"></a>

AWS Elastic Beanstalk adds support for IPv6 network protocol with dual stack configuration for Application and Network Load Balancers.

**Release date:** September 9, 2025

## Changes
<a name="release-2025-09-09-ipv6-dualstack-lb.changes"></a>

Elastic Beanstalk now offers support for your environment to serve both IPv4 and IPv6 protocols by providing the dual-stack configuration option for Application and Network Load Balancers. Elastic Beanstalk will automatically configure your load balancer with dual-stack support when you set the `aws:elbv2:loadbalancer` namespace option `IpAddressType` to *dualstack*.

This feature is available in all AWS Regions where Elastic Beanstalk is supported.

For more information, see [ Configuring dual-stack Elastic Beanstalk load balancers](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/environments-cfg-elbv2-ipv6-dualstack.html) in the *AWS Elastic Beanstalk Developer Guide*.