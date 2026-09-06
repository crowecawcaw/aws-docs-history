

AWS App Runner will no longer be open to new customers starting April 30, 2026. If you would like to use App Runner, sign up prior to that date. Existing customers can continue to use the service as normal. For more information, see [AWS App Runner availability change](https://docs.aws.amazon.com/apprunner/latest/dg/apprunner-availability-change.html).

# Release: App Runner expands support for IPv6 compatibility on August 27, 2025
<a name="release-2025-08-27-ipv6-full-support-release"></a>

AWS App Runner expands support for IPv6 compatibility.

**Release date:** August 27, 2025

## Changes
<a name="release-2025-08-27-ipv6-full-support-release.changes"></a>

This release expands IPv6 support for AWS App Runner services by providing the dual-stack configuration option. Previously, App Runner support for IPv6 only included incoming traffic through public endpoints.

Starting with this release, you can use the *dualstack* option to configure incoming and outgoing network traffic to support IPv6 through both public and private endpoints. With this new release App Runner defaults outgoing public traffic to dual stack when you create a new service or when you deploy an update to an existing service.

For more information about how to manage dual-stack support for your App Runner service, see [Networking with App Runner](https://docs.aws.amazon.com/apprunner/latest/dg/network.html) in the *AWS App Runner Developer Guide*.