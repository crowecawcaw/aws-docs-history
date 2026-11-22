

# Regions and endpoints

With AWS Abuse Signal API, you can use Regional REST endpoints or a global endpoint. Use the endpoint for the Region you want to submit to, or use the global endpoint, which routes your request to a supported Region automatically. Sign with SigV4 (or SigV4a for the global endpoint and multi-Region use), and send JSON over HTTPS.

**Topics**
+ [Supported Regions and endpoints](#regions-endpoints-list)
+ [Global endpoint](#regions-endpoints-global)
+ [AWS PrivateLink access](#regions-endpoints-privatelink)
+ [Transport security](#regions-endpoints-transport)
+ [Choosing SigV4 or SigV4a](#regions-endpoints-signing)

## Supported Regions and endpoints
<a name="regions-endpoints-list"></a>

For the Regions that AWS Abuse Signal API supports and the endpoint to call in each, see [AWS Abuse Signal API endpoints and quotas](https://docs.aws.amazon.com/general/latest/gr/abuse-signal.html) in the *AWS General Reference*.

## Global endpoint
<a name="regions-endpoints-global"></a>

The global endpoint `abuse.global.api.aws` (dual stack) routes each request to a supported Region based on network latency and Regional health. Because any supported Region can serve the request, sign requests to the global endpoint with SigV4a.

**Tip**  
For a resilient integration, use the global endpoint. It automatically routes each request to a healthy supported Region. Your submissions keep succeeding even if a single Region is impaired, and your client needs no failover logic. A report remains trackable no matter which Region served it.

## AWS PrivateLink access
<a name="regions-endpoints-privatelink"></a>

You can reach the API privately from your VPC over AWS PrivateLink using an interface VPC endpoint. Private traffic does not traverse the public internet. AWS PrivateLink uses the same Regional endpoint names as the public path; there is no separate hostname.

For details about AWS PrivateLink access, including how to create interface VPC endpoints and configure VPC endpoint policies, see [AWS Abuse Signal API and interface VPC endpoints (AWS PrivateLink)](vpc-interface-endpoints.md).

## Transport security
<a name="regions-endpoints-transport"></a>
+ All endpoints require HTTPS on port 443.
+ Endpoints enforce a modern TLS security policy (TLS 1.3 capable).

## Choosing SigV4 or SigV4a
<a name="regions-endpoints-signing"></a>

Sign with the `abuse` signing name. Use SigV4 to target a single Region. Use SigV4a when the same signed request must be accepted in more than one Region, for example a client that fails over between Regions or calls the global endpoint. A SigV4a signature covers a set of Regions that you specify when signing, so include every Region that might receive the request.