

AWS App Runner will no longer be open to new customers starting April 30, 2026. If you would like to use App Runner, sign up prior to that date. Existing customers can continue to use the service as normal. For more information, see [AWS App Runner availability change](https://docs.aws.amazon.com/apprunner/latest/dg/apprunner-availability-change.html).

# Release: App Runner adds dual stack support for incoming network traffic on November 02, 2023
<a name="release-2023-11-02-dual-stack"></a>

AWS App Runner now adds dual stack support for incoming traffic through public endpoints.

**Release date:** November 02, 2023

## Changes
<a name="release-2023-11-02-dual-stack.changes"></a>

AWS App Runner now offers the ability to receive *incoming IPv6 traffic* through *public endpoint* by adding the *dual stack* support. With dual stack your service has the flexibility to receive network traffic originating from both IPv4 and IPv6 endpoints, simultaneously. You're no longer restricted to downgrade your incoming IPv6 internet traffic to IPv4 to allow it to flow through your App Runner public endpoints.

**Note**  
Currently, any network traffic originating from IPv6 endpoint cannot be received by App Runner services hosted in an Amazon Virtual Private Cloud (Amazon VPC). For all App Runner *private services* only *IPv4 traffic* is supported. For all *outgoing traffic* also only *IPv4* is supported. 

For more information about how to enable dual stack for your App Runner service, see [Enabling dual stack for public incoming traffic](https://docs.aws.amazon.com/apprunner/latest/dg/network-dual-stack.html) in the *AWS App Runner Developer Guide*. 