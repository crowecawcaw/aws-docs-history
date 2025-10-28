# Enabling restricted internet browsing for Amazon WorkSpaces Secure Browser

The recommended network setup of a WorkSpaces Secure Browser portal is to use private subnets with NAT
gateway, so that the portal can browse both public internet and private content. For more
information, see [Enabling unrestricted internet browsing for Amazon WorkSpaces Secure Browser
(recommended)](unrestricted-internet-browsing.md "unrestricted-internet-browsing.md"). However, you might be
required to control outbound communication from a WorkSpaces Secure Browser portal to the internet by using a
web proxy. For example, if you use a web proxy as the gateway to the internet, you can
implement preventive security controls, such as domain allow-listing and content
filtering. This can also reduce bandwidth usage and improve network performance by caching
frequently accessed resources, such as web pages or software updates locally. For some use
cases, you might have private content that is only accessible by using a web proxy.

You might already be familiar with configuring proxy settings on managed devices, or
on the image of your virtual environments. But this poses challenges if you aren’t in
control of the device (for example, when users are on devices not owned or managed by the
enterprise), or if you need to manage the image for your virtual environment. With WorkSpaces Secure Browser,
you can set proxy settings using Chrome’s policies built into the web browser. You can do
this by setting up an HTTP outbound proxy for WorkSpaces Secure Browser.

This solution is based on a recommended outbound VPC proxy setup. The proxy solution
is based on the open source HTTP proxy [Squid](http://www.squid-cache.org/ "http://www.squid-cache.org/"). Then, it uses WorkSpaces Secure Browser browser settings to configure WorkSpaces Secure Browser portal to
connect to the proxy endpoint. For more information, see [How to set up an outbound VPC proxy with domain whitelisting and content
filtering](https://aws.amazon.com/blogs/security/how-to-set-up-an-outbound-vpc-proxy-with-domain-whitelisting-and-content-filtering/ "https://aws.amazon.com/blogs/security/how-to-set-up-an-outbound-vpc-proxy-with-domain-whitelisting-and-content-filtering/").

This solution provides you with the following benefits:

- An outbound proxy that includes a group of auto-scaling Amazon EC2 instances, hosted by
  a network load balancer. Proxy instances live in a public subnet, and each of them is
  attached with an Elastic IP, so they can have access to the internet.
- A WorkSpaces Secure Browser portal deployed to private subnets. You don’t need to configure NAT
  gateway to enable internet access. Instead, you configure your browser policy, so all
  internet traffic goes through the outbound proxy. If you want to use your own proxy,
  the WorkSpaces Secure Browser portal setup will be similar.

###### Topics

- [Restricted internet browsing architecture for Amazon WorkSpaces Secure Browser](restricted-architecture.md "restricted-architecture.md")
- [Restricted internet browsing prerequisites for Amazon WorkSpaces Secure Browser](restricted-prerequisites.md "restricted-prerequisites.md")
- [HTTP outbound proxy for Amazon WorkSpaces Secure Browser](restricted-setup.md "restricted-setup.md")
- [Troubleshooting restricted internet browsing for Amazon WorkSpaces Secure Browser](restricted-troubleshooting.md "restricted-troubleshooting.md")
