# Release: App Runner expands support for IPv6 compatibility on

August 27, 2025

AWS App Runner expands support for IPv6 compatibility.

**Release date:** August 27, 2025

## Changes

This release expands IPv6 support for AWS App Runner services by providing the dual-stack
configuration option. Previously, App Runner support for IPv6 only included incoming traffic
through public endpoints.

Starting with this release, you can use the _dualstack_
option to configure incoming and outgoing network traffic to support IPv6 through both public
and private endpoints. With this new release App Runner defaults outgoing public traffic to dual
stack when you create a new service or when you deploy an update to an existing service.

For more information about how to manage dual-stack support for your App Runner service, see
[Networking with
App Runner](../dg/network.md "../dg/network.md") in the _AWS App Runner Developer Guide_.
