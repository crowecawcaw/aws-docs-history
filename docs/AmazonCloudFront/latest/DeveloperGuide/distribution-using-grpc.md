# Using gRPC with CloudFront distributions

Amazon CloudFront supports gRPC, an open-source remote procedure call (RPC) framework built on
HTTP/2. gRPC offers bi-directional streaming and binary protocol that buffers payloads,
making it suitable for applications that require low latency communications.

CloudFront receives your gRPC requests and proxies them directly to your origins. You can
use CloudFront to proxy four types of gRPC services:

- Unary RPC
- Server streaming RPC
- Client streaming RPC
- Bi-directional streaming RPC

## How gRPC works in CloudFront

To configure gRPC in CloudFront, set an origin that provides a gRPC service as your
distribution’s origin. You can use origins that provide both non-gRPC and gRPC
services. CloudFront determines if the incoming request is a gRPC request or an HTTP/HTTPS
request based on the `Content-Type` header. If a request’s
`Content-Type` header has value of `application/grpc`, the
request is considered a gRPC request and CloudFront will proxy the request to your
origin.

###### Note

To enable a distribution to handle gRPC requests, include HTTP/2 as one of the
supported HTTP versions, and allow HTTP methods, including `POST`.
Your gRPC origin endpoint must be configured to support HTTPS, as CloudFront only
supports secure (HTTPS-based) gRPC connections. gRPC only supports end-to-end
HTTPS. If you're using a custom origin, verify that your [Protocol](DownloadDistValuesOrigin.md#DownloadDistValuesOriginProtocolPolicy "DownloadDistValuesOrigin.md#DownloadDistValuesOriginProtocolPolicy") settings
support HTTPS.

To enable gRPC support for your distribution, complete the following steps:

1. Update your distribution's cache behavior to allow HTTP methods, including
   the `POST` method.
2. After you select the `POST` method, select the gRPC checkbox
   that appears.
3. Specify **HTTP/2** as one of the supported HTTP versions.

For more information, see the following topics:

- [Allow gRPC requests over HTTP/2](DownloadDistValuesCacheBehavior.md#enable-grpc-distribution "DownloadDistValuesCacheBehavior.md#enable-grpc-distribution")
- [GrpcConfig](../../../cloudfront/latest/APIReference/API_GrpcConfig.md "../../../cloudfront/latest/APIReference/API_GrpcConfig.md") in the
  _Amazon CloudFront API Reference_

Because gRPC is used only for non-cacheable API traffic, your cache configurations
won't affect gRPC requests. You can use an origin request policy to add custom
headers to the gRPC requests that are sent to your gRPC origin. You can use AWS WAF
with CloudFront to manage access to your gRPC distribution, control bots, and protect your
gRPC applications from web exploits. CloudFront gRPC supports [CloudFront Functions](cloudfront-functions.md "cloudfront-functions.md").

In addition to HTTPS status, you will receive grpc-status along with your gRPC
response. For a list of possible values for grpc-status, see [Status codes and
their use in gRPC](https://grpc.github.io/grpc/core/md_doc_statuscodes.html "https://grpc.github.io/grpc/core/md_doc_statuscodes.html").

###### Notes

gRPC doesn't support the following CloudFront features:

- [Custom error
  responses](GeneratingCustomErrorResponses.md "GeneratingCustomErrorResponses.md")
- [Origin failover](high_availability_origin_failover.md "high_availability_origin_failover.md") isn't supported with gRPC, as gRPC uses `POST`
  method. CloudFront fails over to the secondary origin only when the HTTP
  method of the viewer request is `GET`, `HEAD`, or
  `OPTIONS`.
- CloudFront proxies gRPC requests directly to the origin and bypasses the
  Regional Edge Cache (REC). Because gRPC bypasses the REC, gRPC doesn't
  support [Lambda@Edge](lambda-at-the-edge.md "lambda-at-the-edge.md") or [Origin Shield](origin-shield.md "origin-shield.md").
- gRPC doesn't support AWS WAF request body inspection rules. If you
  enabled these rules on the web ACL for a distribution, any request that
  uses gRPC will ignore the request body inspection rules. All other AWS WAF
  rules will still apply. For more information, see [Enable AWS WAF for distributions](WAF-one-click.md "WAF-one-click.md").
