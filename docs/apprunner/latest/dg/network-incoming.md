# Setting up networking configurations for incoming traffic

You can configure your service to receive incoming traffic from private or public endpoint.

A **Public Endpoint** is the default configuration. It opens your service
to any incoming traffic from the public internet. It also provides you with the flexibility to
choose between IPv4 or dual-stack (IPv4 and IPv6) address types for your service.

A **Private endpoint** only allows traffic from an Amazon VPC to access your
App Runner service. This is achieved by setting up a VPC interface endpoint, an AWS PrivateLink
resource, for your App Runner service. Thereby, creating a private connection between the Amazon VPC and
your App Runner service. It also provides you with the flexibility to choose between IPv4 or
dual-stack (IPv4 and IPv6) address types for your service.

The following are the topics that are covered as part of setting up your network configurations for incoming traffic:

- How to configure your incoming traffic to make your service privately available only from within an Amazon VPC. For more information, see [Enabling Private endpoint for incoming traffic](network-pl.md "network-pl.md").
- How to configure your service to receive internet traffic from the dual-stack address type.
  For more information, see [Enabling dual stack for public incoming traffic](network-dual-stack.md "network-dual-stack.md").

## Headers

With App Runner you can access the original source IPv4 and IPv6 addresses of the traffic entering your application. The original source IP addresses are
preserved by assigning the `X-Forwarded-For` request header to them. This enables your applications to fetch the original source IP addresses
when needed.

###### Note

If your service is configured to use private endpoint, then `X-Forwarded-For` request header cannot be used to access original source IP
addresses. If used, it retrieves false values.
