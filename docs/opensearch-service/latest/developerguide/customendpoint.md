# Creating a custom endpoint for Amazon OpenSearch Service

Creating a custom endpoint for your Amazon OpenSearch Service domain makes it easier for you to refer to
your OpenSearch and OpenSearch Dashboards URLs. You can include your company's branding or just
use a shorter, easier-to-remember endpoint than the standard one.

If you ever need to switch to a new domain, just update your DNS to point to the new URL
and continue using the same endpoint as before.

You secure custom endpoints by either generating a certificate in AWS Certificate Manager (ACM) or
importing one of your own.

## Custom endpoints for new domains

You can enable a custom endpoint for a new OpenSearch Service domain using the OpenSearch Service console, AWS CLI,
or configuration API.

###### To customize your endpoint (console)

1. From the OpenSearch Service console, choose **Create domain**
   and provide a name for the domain.
2. Under **Custom endpoint**, select **Enable custom endpoint**.
3. For **Custom hostname**, enter your preferred
   custom endpoint hostname. The hostname should be a fully qualified domain name
   (FQDN), such as www.yourdomain.com or example.yourdomain.com.

###### Note

If you don't have a [wildcard
certificate](https://en.wikipedia.org/wiki/Wildcard_certificate "https://en.wikipedia.org/wiki/Wildcard_certificate") you must obtain a new certificate for your custom
endpoint's subdomains. 4. For **AWS certificate**, choose the SSL
certificate to use for your domain. If no certificates are available, you can
import one into ACM or use ACM to provision one. For more information, see
[Issuing and
Managing Certificates](../../../acm/latest/userguide/gs.md "../../../acm/latest/userguide/gs.md") in the _AWS
Certificate Manager User Guide_.

###### Note

The certificate must have the custom endpoint name and be in the same
account as your OpenSearch Service domain. The certificate status should be ISSUED.

    * Follow the rest of the steps to create your domain and choose
     **Create**.
    * Select the domain when it's finished processing to view your custom
     endpoint.To use the CLI or configuration API, use the `CreateDomain` and

`UpdateDomainConfig` operations. For more information, see the
[AWS CLI Command Reference](../../../cli/latest/reference.md "../../../cli/latest/reference.md") and [Amazon OpenSearch Service API
Reference](../APIReference/Welcome.md "../APIReference/Welcome.md").

## Custom endpoints for existing

domains

To add a custom endpoint to an existing OpenSearch Service domain, choose **Edit** and perform steps 2–4 above.

## CNAME mapping

After you enable a custom endpoint for your OpenSearch Service domain, you can create a CNAME
mapping in Amazon Route 53 (or your preferred DNS service provider). Creating a CNAME mapping
will enable you to route traffic to your custom endpoint and its subdomains. Without
this mapping, you won't be able to route traffic to your custom endpoint. For steps to
create this mapping in Route 53, see [Configuring DNS
routing for a new domain](../../../Route53/latest/DeveloperGuide/dns-configuring-new-domain.md "../../../Route53/latest/DeveloperGuide/dns-configuring-new-domain.md") and [Creating a new hosted zone for a subdomain](../../../Route53/latest/DeveloperGuide/dns-routing-traffic-for-subdomains.md#dns-routing-traffic-for-subdomains-creating-hosted-zone "../../../Route53/latest/DeveloperGuide/dns-routing-traffic-for-subdomains.md#dns-routing-traffic-for-subdomains-creating-hosted-zone"). For other providers, consult
their documentation.

Create a CNAME record that points the custom endpoint to the automatically generated
domain endpoint. If your domain is dual stack, you can point your CNAME record to either
of the two service generated endpoints. The dual stack capabilty of your custom endpoint
depends on the service generated endpoint that you point the CNAME record to. The custom
endpoint hostname is the _name_ of the CNAME record, and the domain
endpoint hostname is the _value_ of the CNAME record.

If you use [SAML authentication for OpenSearch
Dashboards](saml.md "saml.md"), you must update your IdP with the new SSO URL.

You can use Amazon Route 53 to create an alias record type to point your domain's custom
endpoint to a dual stack search endpoint. To create an alias record type, you must
configure your domain to use the dual stack IP address type. You can do this using the
Route 53 API.

To create an alias record type using the Route 53 API, specify the alias target of your
domain. You can find the alias target of your domain in the **Hosted Zone (dual
stack)** field in the custom endpoint section of the OpenSearch Service console or by
using the `DescribeDomain` API and copying the value of the
`DomainEndpointV2HostedZoneId`.
