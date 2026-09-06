

# Quotas and constraints
<a name="quotas-and-constraints"></a>

## Supported and unsupported features
<a name="supported-unsupported-features"></a>

The following table lists the features available in the current release of inbound external links with custom domains and features that are planned or not yet supported. For general RTB Fabric service quotas, see Quotas for RTB Fabric.


| Feature | Status | Notes | 
| --- | --- | --- | 
| HTTP and HTTPS ingress | Supported | The gateway accepts both HTTP and HTTPS traffic on your custom domain. TLS certificate configuration is required only for HTTPS. | 
| Host exact match | Supported | Case-insensitive comparison. Port is stripped before matching (RFC 7230). | 
| Host wildcard match | Supported | RFC 6125 single-level subdomain matching. \*.example.com matches bid.example.com but not a.b.example.com. | 
| Path exact match | Supported | Byte-for-byte comparison of the request path. | 
| Path prefix match | Supported | Segment-boundary aware. /api matches /api/v1 but does not match /api2. | 
| Query string equals match | Supported | URL-decoded key-value comparison. One queryStringEquals condition per rule. | 
| Query string exists match | Supported | URL-decoded key presence check. One queryStringExists condition per rule. | 
| Composite rules | Supported | AND logic across all conditions within a single rule. All specified conditions must match. | 
| Global priority ordering | Supported | Rules across all links are flattened and evaluated in ascending priority order. First match wins. | 
| Customer TLS certificates | Supported | Provisioned through ACM. Private key decrypted securely within the VPC. | 
| Service TLS certificates | Supported | ECDSA and RSA. Used as fallback when no customer certificate matches the SNI hostname. | 
| SNI-based certificate selection | Supported | Fast exact hostname lookup, then wildcard pattern iteration. | 
| TLS 1.2 and TLS 1.3 | Supported | Session resumption supported across gateway hosts via shared session ticket keys. | 
| DNS-based traffic migration | Supported | Route 53 weighted routing for gradual cutover. See Migrating traffic to inbound external links with custom domains. | 
| Path regex match | Not supported | Deferred. Track feature request with your RTB Fabric account team. | 
| Multiple query parameter conditions per rule | Not supported | Each rule supports one query condition: either queryStringEquals or queryStringExists, but not both. Use multiple rules with appropriate priorities to match on additional parameters. | 
| Catch-all / default routing rules | Not supported | The control plane requires at least one condition per rule. A rule with no conditions cannot be created. | 
| HTTP/2 upstream | Not supported | Requests are forwarded to your bidder over HTTP/1.1 only. | 
| Mutual TLS (mTLS) | Not supported | Client certificate authentication is not available for inbound external links with custom domains. | 
| WebSocket upgrade | Not supported | WebSocket connections are not supported through the gateway. | 
| Response header injection | Not supported | The gateway does not add, modify, or remove response headers. | 
| Request/response body transformation | Not supported | Request and response bodies are passed through unmodified. | 
| Custom domain operational metrics | Not supported | The rule executor and certificate resolver do not emit metrics distinguishing customer certificate from service certificate resolution, rule match counts, or rule evaluation latency. Use gateway-level logs for debugging. | 

## Service quotas
<a name="service-quotas"></a>

The following dimensions are subject to service quotas. Quotas are enforced by the control plane. For current quota values and instructions on requesting increases, see Quotas for RTB Fabric.


| Dimension | Description | 
| --- | --- | 
| Routing rules per link | Maximum number of routing rules that can be created on a single link via the CreateLinkRoutingRule API. | 
| Routing rules per gateway | Maximum total number of routing rules across all links on a single gateway. | 
| Customer certificates per gateway | Maximum number of customer certificates associated with a single gateway via the AssociateCertificate API. | 
| SANs per certificate | Maximum number of subject alternative names (SANs) on a single ACM certificate used with inbound external links with custom domains. | 

**Note**  
If you need a quota increase for any of these dimensions, contact your RTB Fabric account team.

## Regional constraints
<a name="regional-constraints"></a>

Inbound external links with custom domains operate within the following regional boundaries:
+ **Gateway scope.** Each gateway is provisioned per customer, per region. A gateway in `us-east-1` serves only traffic entering that region.
+ **DNS records.** Create region-specific CNAME records that point to each region's gateway endpoint. There is no global gateway endpoint.
+ **Certificate scope.** Certificates and their associated private keys are stored and decrypted within the region where the gateway is deployed. A certificate provisioned for a `us-east-1` gateway is not available in `eu-west-1`.
+ **Routing rule scope.** Routing rules are configured per gateway. Rules defined for one region do not apply to another region's gateway, even for the same link ID.
+ **Independent configuration.** Changes to a gateway's certificates, routing rules, or link associations in one region have no effect on other regions.

## Performance characteristics
<a name="performance-characteristics"></a>

Inbound external links with custom domains add minimal overhead to request processing. Rule evaluation and certificate resolution are designed to operate within the latency constraints of real-time bidding workloads.

For information about end-to-end bid-request latency, QPS capacity limits, and connection pooling characteristics, contact your RTB Fabric account team. For information about health check behavior, see [Health checks for Managed Endpoints](health-checks-for-managed-endpoints.md).