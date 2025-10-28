# Routing traffic to an Amazon API Gateway API by using your domain name

You can use Amazon API Gateway to create, publish, maintain, monitor, and secure APIs. You can create
APIs that access AWS services or other web services in addition to data stored in the
AWS Cloud.

The method that you use to route domain traffic to an API Gateway API is the same regardless of whether you created a regional API Gateway endpoint or an
edge-optimized API Gateway endpoint. If you create a private API Gateway endpoint, the process is slightly different.

- **Regional API endpoint**: You create a Route 53 alias record that routes traffic
  to the regional API endpoint.
- **Edge-optimized API endpoint**: You create a Route 53 alias record that routes traffic
  to the edge-optimized API. This causes traffic to be routed to the CloudFront distribution that's associated with the edge-optimized API.
- **Private API endpoint**: You create a Route 53 alias record that routes traffic to
  your private API endpoint using an interface VPC endpoint for API Gateway in a private hosted zone.
  An alias record is a Route 53 extension to DNS that's similar to a CNAME record. For a comparison of alias and CNAME records, see
  [Choosing between alias and non-alias records](resource-record-sets-choosing-alias-non-alias.md "resource-record-sets-choosing-alias-non-alias.md").

###### Note

Route 53 doesn't charge for alias queries to API Gateway APIs or other AWS resources.

###### Topics

- [Prerequisites](#routing-to-api-gateway-prereqs "#routing-to-api-gateway-prereqs")
- [Configuring Route 53 to route traffic to an API Gateway endpoint](#routing-to-api-gateway-config "#routing-to-api-gateway-config")

## Prerequisites

To get started, you need the following:

- An API Gateway API that has a custom domain name, such as api.example.com that matches the name of
  the Route 53 record that you want to create.

For more information, see the following topics:

    + [Setting up custom domain names for HTTP APIs](../../../apigateway/latest/developerguide/http-api-custom-domain-names.md "../../../apigateway/latest/developerguide/http-api-custom-domain-names.md") in the
     *Amazon API Gateway Developer Guide*.
    + [Setting up custom domain names for REST APIs](../../../apigateway/latest/developerguide/how-to-custom-domains.md "../../../apigateway/latest/developerguide/how-to-custom-domains.md") in the
     *Amazon API Gateway Developer Guide*.
    + [Setting up custom domain names for WebSocket APIs](../../../apigateway/latest/developerguide/websocket-api-custom-domain-names.md "../../../apigateway/latest/developerguide/websocket-api-custom-domain-names.md") in
     the *Amazon API Gateway Developer Guide*.
    + [Custom domain names for private APIs in API Gateway](../../../apigateway/latest/developerguide/apigateway-private-custom-domains.md "../../../apigateway/latest/developerguide/apigateway-private-custom-domains.md") in the
     *Amazon API Gateway Developer Guide*.

- A registered domain name. You can use Amazon Route 53 as your domain registrar or you can use a
  different registrar.
- Route 53 as the DNS service for the domain. If you register your domain name by using Route 53,
  we automatically configure Route 53 as the DNS service for the domain.

For information about using Route 53 as the DNS service provider for your domain, see
[Making Amazon Route 53 the DNS service for an existing domain](MigratingDNS.md "MigratingDNS.md").

## Configuring Route 53 to route traffic to an API Gateway endpoint

To configure Route 53 to route traffic to an API Gateway endpoint, perform the following procedure.

Custom domain names for public APIs
The following procedure describes how to route traffic to an API Gateway endpoint for a custom domain name for public APIs.

###### To route traffic to an API Gateway endpoint

1. If you created the Route 53 hosted zone and the endpoint using the same account, skip to step 2.

If you created the hosted zone and the endpoint using different accounts, get the target domain name for the
custom domain name that you want to use:

    1. Sign in to the AWS Management Console and open
     the API Gateway console at
     [https://console.aws.amazon.com/apigateway/](https://console.aws.amazon.com/apigateway/ "https://console.aws.amazon.com/apigateway/").
    2. In the navigation pane, choose **Custom domain names**.
    3. Select the custom domain name that you want to use and get the value of  **API Gateway
     domain name**.

2. Open the Route 53 console at
   [https://console.aws.amazon.com/route53/](https://console.aws.amazon.com/route53/ "https://console.aws.amazon.com/route53/").
3. In the navigation pane, choose **Hosted zones**.
4. Choose the name of the hosted zone that has the domain name that you want to use to route traffic to your API.
5. Choose **Create record**.
6. Specify the following values:

###### Important

We recommend that you turn on Alias. For domain names that don't use a Route 53 Alias record,
you might encounter issues if you use a VPC with private DNS enabled to invoke a private API.
Private DNS overrides the default DNS resolution behavior within the VPC, which might cause conflicts
with external DNS records.

**Routing policy**

Choose the applicable routing policy. For more information, see [Choosing a routing policy](routing-policy.md "routing-policy.md").

**Record name**

Enter the domain name that you want to use to route traffic to your API.

The API that you want to route traffic to must include a
custom domain name, such as api.example.com that matches the
name of the Route 53 record.

**Alias**

If you are using the **Quick create** record creation method, turn on **Alias**.

**Value/Route traffic to**

Choose **Alias to API Gateway API**, then choose the Region that the endpoint is from.

How you specify the value for **Endpoint** depends on whether you created the hosted zone and the API
using the same AWS account or different accounts:

    * **Same account** – The list of target domain names includes only APIs that
     have a custom domain name that matches the value that you specified for **Record name**. Choose the
     applicable value.
    * **Different accounts** – Enter the value that you got in step 1 of this
     procedure.

**Record type**

Choose **A – IPv4 address**.

**Evaluate target health**

For control over DNS failover, configure custom health checks.
For an example, see [Configure custom health checks for DNS failover](../../../apigateway/latest/developerguide/dns-failover.md "../../../apigateway/latest/developerguide/dns-failover.md") in the _API Gateway user guide_. 7. Choose **Create records**.

Changes generally propagate to all Route 53 servers within 60 seconds. When
propagation is done, you'll be able to route traffic to your API by using
the name of the alias record that you created in this procedure.

Custom domain names for private APIs
The following procedure describes how to route traffic to an API Gateway endpoint for a custom domain name for private APIs.

###### To route traffic to an API Gateway endpoint

1. Open the Route 53 console at
   [https://console.aws.amazon.com/route53/](https://console.aws.amazon.com/route53/ "https://console.aws.amazon.com/route53/").
2. In the navigation pane, choose **Hosted zones**.
3. Choose the name of the private hosted zone that has the domain name that you want to use to route traffic to your API.
4. Choose **Create record**.
5. Specify the following values:

**Routing policy**

Choose the applicable routing policy. For more information, see [Choosing a routing policy](routing-policy.md "routing-policy.md").

**Record name**

Enter the domain name that you want to use to route traffic to your API.

The API that you want to route traffic to must include a
custom domain name, such as api.example.com that matches the
name of the Route 53 record.

**Alias**

Turn on **Alias**.

**Value/Route traffic to**

Choose **Alias to VPC Endpoint**. Choose the Region that the endpoint is from, and then select your VPC endpoint.

**Record type**

If you are using IPv6 for your VPC endpoint, create an AAAA record type. If you are using dualstack for your VPC endpoint, create both an AAAA and an A record type.

**Evaluate target health**

For control over DNS failover, configure custom health checks.
For an example, see [Configure custom health checks for DNS failover](../../../apigateway/latest/developerguide/dns-failover.md "../../../apigateway/latest/developerguide/dns-failover.md") in the _API Gateway user guide_. 6. Choose **Create records**.

Changes generally propagate to all Route 53 servers within 60 seconds. When
propagation is done, you'll be able to route traffic to your API by using
the name of the alias record that you created in this procedure.
