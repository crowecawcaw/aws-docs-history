# Endpoints for standard accelerators in AWS Global Accelerator

Endpoints for standard accelerators in AWS Global Accelerator can be Network Load Balancers, Application Load Balancers, Amazon EC2 instances, or Elastic IP addresses.
In AWS Global Accelerator, static IP addresses serve as a single point of contact for clients, and, with a standard accelerator, Global Accelerator
distributes incoming traffic across healthy endpoints. Global Accelerator directs traffic to endpoints by
using the port (or port range) that you specify for the listener that the endpoint group for
the endpoint belongs to.

Each endpoint group can have multiple endpoints. You can add each endpoint to multiple endpoint
groups, but the endpoint groups must be associated with different listeners. A resource must be valid
and active when you add it as an endpoint.

###### Important

Accelerators that you configure as dual-stack (that is, accelerators that you want to support
IPv4 and IPv6) require that you add only endpoints that also
support dual-stack. Network Load Balancers, Application Load Balancers, and Amazon EC2 instances can be added as dual-stack endpoints.

Global Accelerator continually monitors the health of all endpoints that are included in a standard endpoint group. It
routes traffic only to the active endpoints that are healthy. If Global Accelerator doesn’t have any healthy endpoints
to route traffic to, it routes traffic to all endpoints in the AWS Region.

###### Contents

- [Requirements for resources you add as accelerator endpoints](about-endpoints-caveats.md "about-endpoints-caveats.md")
- [Add a standard endpoint](about-endpoints-adding-endpoints.md "about-endpoints-adding-endpoints.md")
- [Edit a standard endpoint](about-endpoints-adding-endpoints-edit.md "about-endpoints-adding-endpoints-edit.md")
- [Remove a standard endpoint](about-endpoints-adding-endpoints-remove.md "about-endpoints-adding-endpoints-remove.md")
- [How endpoint weights work to manage traffic volume](about-endpoints-endpoint-weights.md "about-endpoints-endpoint-weights.md")
- [How failover works for unhealthy endpoints](about-endpoints-endpoint-weights.md "about-endpoints-endpoint-weights.md")
- [How to avoid connection collisions that result in TCP connection time delays](about-endpoints.md "about-endpoints.md")
