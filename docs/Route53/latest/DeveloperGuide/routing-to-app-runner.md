# Routing traffic to an AWS App Runner service

AWS App Runner is a fully managed service that makes it easy for developers to deploy
containerized web applications and APIs at scale and with no prior infrastructure
experience required. Start with your source code or a container image. App Runner builds and
deploys the web application automatically, load balances traffic with encryption, scales
to meet your traffic needs, and makes it easy for your services to communicate with
other AWS services and applications that run in a private Amazon VPC. With App Runner, rather
than thinking about servers or scaling, you have more time to focus on your
applications. For more information, see [What is AWS App Runner](../../../apprunner/latest/dg/what-is-apprunner.md "../../../apprunner/latest/dg/what-is-apprunner.md") in the
_AWS App Runner Developer Guide._

###### Important

Amazon Route 53 currently supports alias records for AWS App Runner services that are created after August
1, 2022.

To route domain traffic to an App Runner Service, use Amazon Route 53 to create an
[alias record](resource-record-sets-choosing-alias-non-alias.md "resource-record-sets-choosing-alias-non-alias.md")
that points to your App Runner service. An alias record is a Route 53 extension to DNS. It's
similar to a CNAME record, except you can create an alias record both for the root
domain, such as example.com, and for subdomains, such as www.example.com
(http://www.example.com/). You can create only CNAME records for subdomains.

###### Note

Route 53 doesn't charge for alias queries to App Runner service or other AWS
resources.

## Prerequisites

To get started, you need the following:

- An App Runner service. For information about creating an App Runner service, see
  [Getting started with
  App Runner](../../../apprunner/latest/dg/getting-started.md "../../../apprunner/latest/dg/getting-started.md").
- A registered domain name. You can use Amazon Route 53 as your domain registrar,
  or you can use a different registrar.
- Route 53 as the DNS service for the domain. If you register your domain name
  by using Route 53, we automatically configure Route 53 as the DNS service for the
  domain.

For information about using Route 53 as the DNS service provider for your
domain, see [Making Amazon Route 53 the DNS service for an existing domain](MigratingDNS.md "MigratingDNS.md").

- Associated the custom domain to your App Runner service. For more information,
  see [Managing custom
  domain names for App Runner](../../../apprunner/latest/dg/manage-custom-domains.md "../../../apprunner/latest/dg/manage-custom-domains.md").
- Configure the certificate validation record returned by App Runner to you Route 53
  hosted zone to start the domain validation process. For more information,
  see [DNS validation in the
  AWS Certificate Manager](../../../acm/latest/userguide/dns-validation.md "../../../acm/latest/userguide/dns-validation.md") in the _AWS Certificate Manager User
  Guide._

## Configuring Amazon Route 53 to route

traffic to an App Runner service

To configure Amazon Route 53 to route traffic to an App Runner service, perform the following
procedure.

###### To route traffic to an App Runner

service

1. Open the Route 53 console at
   [https://console.aws.amazon.com/route53/](https://console.aws.amazon.com/route53/ "https://console.aws.amazon.com/route53/").
2. In the navigation pane, choose **Hosted zones**.
3. Choose the name of the hosted zone that matches the name of the domain
   that you want to route traffic for.
4. Choose **Create record**.
5. Specify the following values:

**Routing policy**

Choose the applicable routing policy. For more information,
see [Choosing a routing policy](routing-policy.md "routing-policy.md").

**Record name**

Enter the domain name that you want to use to route traffic to
your App Runner service. The default value is the name of the hosted
zone.

For example, if the name of the hosted zone is example.com and
you want to use acme.example.com to route traffic to your App Runner
service, enter **acme**.

**Value/Route traffic to**

Choose **Alias to App Runner Service**, then choose
the AWS Region. Choose the domain name of the environment that
you want to route traffic to.

**Record type**

Accept the default value, **A – IPv4
address**.

**Evaluate target health**

Choose **No**. For information about
evaluating target health, see [Evaluate target
health](resource-record-sets-values-alias.md#rrsets-values-alias-evaluate-target-health "resource-record-sets-values-alias.md#rrsets-values-alias-evaluate-target-health"). 6. Choose **Create records**.

Changes generally propagate to all Route 53 servers within 60 seconds. When
propagation is done, you'll be able to route traffic to your App Runner service by
using the name of the alias record that you created in this procedure.
