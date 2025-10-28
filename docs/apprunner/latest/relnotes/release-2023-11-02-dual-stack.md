# Release: App Runner adds dual stack support for incoming network traffic on November 02, 2023

AWS App Runner now adds dual stack support for incoming traffic through public endpoints.

**Release date:** November 02, 2023

## Changes

AWS App Runner now offers the ability to receive _incoming IPv6 traffic_ through _public endpoint_ by adding the
_dual stack_ support.
With dual stack your service has the flexibility to receive network traffic originating from both IPv4 and IPv6
endpoints, simultaneously. You're no longer restricted to downgrade your incoming IPv6 internet traffic to IPv4 to allow it to flow through your App Runner public endpoints.

###### Note

Currently, any network traffic originating from IPv6 endpoint cannot be received by App Runner services hosted in an Amazon Virtual Private Cloud (Amazon VPC). For all App Runner
_private services_ only _IPv4 traffic_ is supported. For all _outgoing traffic_ also only _IPv4_ is supported.

For more information about how to enable dual stack for your App Runner service, see [Enabling dual stack
for public incoming traffic](../dg/network-dual-stack.md "../dg/network-dual-stack.md") in the _AWS App Runner Developer Guide_.
