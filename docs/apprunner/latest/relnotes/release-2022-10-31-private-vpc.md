

AWS App Runner will no longer be open to new customers starting April 30, 2026. If you would like to use App Runner, sign up prior to that date. Existing customers can continue to use the service as normal. For more information, see [AWS App Runner availability change](https://docs.aws.amazon.com/apprunner/latest/dg/apprunner-availability-change.html).

# Release: App Runner now supports privately accessible services within Amazon VPC on October 31, 2022
<a name="release-2022-10-31-private-vpc"></a>

AWS App Runner now supports private services which enables access to App Runner services from within an Amazon Virtual Private Cloud (Amazon VPC).

**Release date:** October 31, 2022

## Changes
<a name="release-2022-10-31-private-vpc.changes"></a>

AWS App Runner now supports private services. By default, App Runner services are accessible publicly over the internet. Now, with private services, you can restrict network access to your internal websites, APIs, and applications to originate from within your VPC. 

Private services in App Runner leverages AWS PrivateLink Interface VPC Endpoints, which provides highly available and scalable networking technology. You can specify which Amazon VPC you want your App Runner service to be accessible in by passing an Interface VPC Endpoint. You can also add security groups that function as a virtual firewall to your Interface VPC Endpoints to further restrict network traffic. 

For more information, see [Enabling Private endpoint for incoming traffic](https://docs.aws.amazon.com/apprunner/latest/dg/network-pl.html) in the *AWS App Runner Developer Guide*.