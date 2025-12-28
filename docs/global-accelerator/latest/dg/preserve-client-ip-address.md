# Preserve client IP addresses in AWS Global Accelerator

Your options for preserving and accessing the client IP address for AWS Global Accelerator depend on the endpoints that
you've set up with your accelerator. When client IP address preservation is enabled, the source IP address of the
original client is preserved for packets that arrive at the load balancer.

Endpoints on custom routing accelerators always have the client IP address preserved. There are three types of endpoints for
standard accelerators that can preserve the source IP address of the
client in incoming packets: Application Load Balancers, Amazon EC2 instances, and Network Load Balancers with security groups. There are requirements and
limitations for specific resources that you add as endpoint with client IP address
preservation. For more information, see [Transition endpoints with client IP address preservation](about-endpoints.md "about-endpoints.md").

Note that Global Accelerator does not support client IP address preservation for the following endpoint types:

- Network Load Balancers without security groups
- Elastic IP addresses
  For details about endpoint requirements, see [Requirements for resources you add as accelerator endpoints](about-endpoints-caveats.md "about-endpoints-caveats.md").

###### Contents

- [Guidelines and restrictions](preserve-client-ip-address.md "preserve-client-ip-address.md")
- [Requirements for client IP address preservation](about-endpoints.md "about-endpoints.md")
- [How the client IP address is preserved](preserve-client-ip-address.md "preserve-client-ip-address.md")
- [Benefits of
  client IP address preservation](preserve-client-ip-address.md "preserve-client-ip-address.md")
- [Best practices for ENIs and security](best-practices-aga.md "best-practices-aga.md")
- [Transition endpoints](about-endpoints.md "about-endpoints.md")
