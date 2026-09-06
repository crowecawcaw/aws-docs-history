

# Inbound external links with custom domains concepts
<a name="custom-domain-concepts"></a>

This section defines the core concepts you need to understand before configuring inbound external links with custom domains.

## Custom domains
<a name="custom-domain-concept-domains"></a>

A custom domain is a DNS hostname that you own and control, such as `east-bid.dsp.example.com` or `bid.example.com`. In the context of RTB Fabric, a custom domain is any hostname that partners already use to send bid requests to your infrastructure.

When you configure inbound external links with custom domains, you tell RTB Fabric how to handle traffic arriving on your custom domain. This includes defining routing rules that map requests on that domain to a specific link, and optionally providing a TLS certificate for the domain if you use HTTPS.

You can configure multiple custom domains per RTB Fabric gateway. Each custom domain requires at least one routing rule. If you use HTTPS, each custom domain also requires its own TLS certificate (or a wildcard certificate that covers it).

## Links and external inbound links
<a name="custom-domain-concept-links"></a>

A link represents a connection between two entities in RTB Fabric. There are two types:
+ **Standard link** — A connection between two RTB Fabric gateways. Create using the CreateLink API.
+ **External inbound link** — A connection between an external endpoint (such as a partner's bid endpoint) and your responder gateway. Create using the CreateInboundExternalLink API.

Inbound external links with custom domains typically use external inbound links, because traffic originates from partners outside RTB Fabric. Each link is identified by a system-generated `linkId` and belongs to a specific gateway (`gatewayId`).

Links define the processing pipeline for each request through flow modules — an ordered list of modules such as fraud detection, identity resolution, and geo-enrichment. You configure flow modules using the UpdateLinkModuleFlow API. If no flow modules are configured, requests are forwarded directly to your bidder with no intermediate processing.

## Regional gateways
<a name="custom-domain-concept-gateways"></a>

RTB Fabric deploys a dedicated external responder gateway for each customer in each region. Partners reach the correct regional gateway through DNS: you create a CNAME record that points your custom domain to the regional gateway endpoint.

Each regional responder gateway operates independently. If you serve bid traffic in multiple regions, you configure each gateway separately with its own certificates and routing rules. You control regional traffic distribution through your DNS configuration — for example, using latency-based or geolocation-based routing in Amazon Route 53.

**Important**  
Each regional gateway is a dedicated resource scoped to your account. Traffic from your custom domain is never mixed with other customers' traffic at the gateway level.

## Routing rules
<a name="custom-domain-concept-routing"></a>

A routing rule maps an incoming HTTP request to a specific link. Each rule belongs to a single link and contains a set of conditions that the request must satisfy. When a request arrives on a custom domain, the gateway evaluates routing rules to determine which link should process it. Routing rules are configured separately from the link's flow modules — create the link first (via CreateLink or CreateInboundExternalLink), then create routing rules on it using the CreateLinkRoutingRule API.

Each routing rule has the following fields:


| Field | Type | Description | 
| --- | --- | --- | 
| ruleId | String | System-generated unique identifier for the rule. | 
| priority | Integer (1-1000) | Evaluation priority. Lower values take precedence. Must be unique within a link. | 
| conditions | Object | The set of conditions the request must match. All conditions use AND logic. At least one condition is required. | 

The gateway evaluates rules across all links by priority and routes to the first match. If no rule matches, the gateway returns HTTP 404.

## Listener configuration
<a name="custom-domain-concept-listener-config"></a>

A listener configuration defines which protocols an external responder gateway accepts for incoming traffic. By default, a gateway listens on a single protocol (HTTP or HTTPS) as specified by the `protocol` parameter at creation time. With multi-protocol support, you can configure a gateway to accept both HTTP and HTTPS traffic simultaneously using the `listenerConfig` parameter.

The `listenerConfig` contains a `protocols` list that specifies one or two protocols:
+ `["HTTPS"]` — The gateway accepts HTTPS traffic only (default).
+ `["HTTP"]` — The gateway accepts HTTP traffic only.
+ `["HTTP", "HTTPS"]` — The gateway accepts both HTTP and HTTPS traffic.

Multi-protocol support is useful when you need to support partners that send traffic over HTTP while also serving HTTPS traffic with TLS termination. When both protocols are enabled, the gateway provisions listeners for each protocol on the public ingress cluster.

**Note**  
If you enable both HTTP and HTTPS, TLS certificate association and SNI-based certificate resolution apply only to HTTPS connections. HTTP connections bypass TLS termination entirely.

## Certificate resolution
<a name="custom-domain-concept-certificates"></a>

RTB Fabric uses a two-tier certificate resolution strategy to select the correct TLS certificate for each incoming connection.

### Tier 1: Customer certificates (SNI-based)
<a name="custom-domain-cert-tier1"></a>

When a TLS ClientHello includes an SNI hostname, the certificate resolver checks for a matching customer certificate:

1. **Exact match** - The resolver looks up the SNI hostname in the exact hostname index within the customer certificate store.

1. **Wildcard match** - If no exact match is found, the resolver iterates over the wildcard hostname entries, checking each wildcard pattern against the SNI hostname.

Customer certificates are certificates you associate with the gateway using the AssociateCertificate API. RTB Fabric extracts the common name (CN) and subject alternative names (SANs) from your ACM certificate and uses them for SNI-based hostname matching.

**Important**  
Customer certificates are never served as a fallback for non-customer traffic. If a connection's SNI hostname does not match any customer certificate, the resolver proceeds to Tier 2.

### Tier 2: Service certificates (fallback)
<a name="custom-domain-cert-tier2"></a>

If no customer certificate matches (or if the ClientHello does not include an SNI extension), the resolver falls back to a Fabric-managed service certificate. Service certificates are used for standard (non-custom-domain) traffic.

**Warning**  
The following limitations apply to certificate resolution in the current release. Ensure your configuration accounts for these behaviors.  
**Wildcard matching scope** - Wildcard matching in certificate resolution uses suffix-based matching, which can match across multiple DNS labels. For example, a certificate configured with `*.example.com` may match `a.b.example.com` during certificate resolution. This differs from routing rule wildcard matching, which enforces single-label matching per RFC 6125. Do not rely on certificate wildcard matching to enforce subdomain boundaries.
**Case-sensitive hostname lookup** - Hostname comparison in certificate resolution is case-sensitive, while routing rule host matching is case-insensitive. Ensure that the CN and SANs on your ACM certificate use lowercase characters to avoid mismatches with SNI hostnames, which clients typically send in lowercase.