

# Using custom domains with inbound external links
<a name="using-custom-domains-ext-inbound-links"></a>

**Topics**
+ [Overview](#custom-domain-overview)
+ [Inbound external links with custom domains concepts](custom-domain-concepts.md)
+ [Prerequisites](custom-domain-prerequisites.md)
+ [Getting started with inbound external links with custom domains](get-started-custom-domain.md)
+ [Configuring routing rules](configure-routing-rule.md)
+ [Manage TLS certificates](manage-tls-certificates.md)
+ [Migrating traffic to inbound external links with custom domains](migrating-traffic-to-custom-domain.md)
+ [Quotas and constraints](quotas-and-constraints.md)
+ [Monitoring and logging](monitoring-and-logging.md)
+ [Troubleshooting inbound external links with custom domains](troubleshooting-custom-domain-ingress.md)

## Overview
<a name="custom-domain-overview"></a>

### What is inbound external links with custom domains?
<a name="custom-domain-what-is"></a>

Inbound external links with custom domains let you route traffic through AWS RTB Fabric while preserving your existing public endpoints. Adtech partners send bid requests to your domain (for example, `east-bid.dsp.example.com`), and RTB Fabric processes the request without requiring any URL change on the demand-side platform.

Without inbound external links with custom domains, adopting RTB Fabric requires partners to update their endpoint URLs to point to Fabric-managed domains. For many customers, this is not feasible: demand-side platforms (DSPs) and supply-side platforms (SSPs) have hardcoded URLs in their bidding configurations, and changing them requires coordination across multiple external organizations. Inbound external links with custom domains remove this requirement entirely.

### Benefits
<a name="custom-domain-benefits"></a>

Inbound external links with custom domains provide the following benefits:
+ **Preserve existing URLs** — Partners continue sending bid requests to the same endpoints they already use. No URL changes are required on the demand side.
+ **DNS-based migration** — Migrate traffic by updating a CNAME record. Use weighted DNS routing to shift traffic gradually, or cut over instantly.
+ **Zero-downtime cutover** — Because the migration is DNS-driven, there is no interruption to live bid traffic during the transition.
+ **Customer-managed TLS** — The gateway supports both HTTP and HTTPS. For HTTPS, you provide your own TLS certificates through ACM, and RTB Fabric terminates TLS using your certificate.
+ **Full request fidelity** — The host header, request path, query string, and request body are preserved exactly as sent by the partner.

### How inbound external links with custom domains works
<a name="custom-domain-how-it-works"></a>

The following sequence describes the end-to-end flow when a partner sends a bid request to your custom domain:

1. **DNS resolution** - The partner's DNS resolver looks up your custom domain (for example, `east-bid.dsp.example.com`). Your DNS record contains a CNAME that points to a regional RTB Fabric Gateway endpoint. DNS resolves to the IP address of the gateway in the target region.

1. **TLS termination (HTTPS only)** - If the partner connects over HTTPS, the gateway inspects the Server Name Indication (SNI) extension in the TLS ClientHello to determine which certificate to present. The certificate resolver first checks for an exact hostname match in the customer certificate store, then checks for a wildcard hostname match. If no customer certificate matches, the resolver falls back to a service certificate selected based on the client's supported signature schemes. The certificate's private key is decrypted within the VPC. If the partner connects over HTTP, this step is skipped.

1. **Link ID resolution** - After connection establishment, the gateway determines which link should process the request. The gateway evaluates three extraction methods in order: URL-based extraction, host header extraction, and rule-based routing. For custom domain traffic, the first two methods typically do not match because the URL does not contain a Fabric link ID. Rule-based routing evaluates the routing rules that you define. Rules are flattened across all links, sorted by priority (ascending), and the first matching rule determines the link ID.

1. **Module flow execution** - The gateway executes the link's configured module flow. This includes fraud detection, identity resolution, geo-enrichment, and ISV modules as defined in your link configuration. The original host header, request path, and query string are preserved throughout the flow.

1. **Delivery to your bidder** - The gateway delivers the processed request to your bidder running in your VPC via cross-account network interface. Your bidder receives the request with the original host, path, query string, and body intact.

**Note**  
Inbound external links with custom domains use the same module flow and delivery mechanism as standard RTB Fabric links. The differences are in steps 2 and 3: for HTTPS traffic, TLS terminates using your certificate, and link ID resolution uses routing rules instead of URL-based extraction. For HTTP traffic, only link ID resolution (step 3) differs from the standard flow.

**Important**  
Routing rules and certificate resolution use different matching semantics. Be aware of these differences when configuring HTTPS inbound external links with custom domains:  
Routing rules use case-insensitive host matching and RFC 6125 single-label wildcard matching (`*.example.com` matches `bid.example.com` but not `a.b.example.com`).
Certificate resolution uses case-sensitive host matching and suffix-based wildcard matching (`*.example.com` may match `a.b.example.com`).