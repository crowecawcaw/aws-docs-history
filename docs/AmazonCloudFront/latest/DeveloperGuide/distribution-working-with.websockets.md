# Use WebSockets with CloudFront distributions

Amazon CloudFront supports using WebSocket, a TCP-based protocol that is useful when you need
long-lived bidirectional connections between clients and servers. A persistent
connection is often a requirement with real-time applications. The scenarios in which
you might use WebSockets include social chat platforms, online collaboration workspaces,
multi-player gaming, and services that provide real-time data feeds like financial
trading platforms. Data over a WebSocket connection can flow in both directions for
full-duplex communication.

WebSocket functionality is automatically enabled to work with any distribution. To use
WebSockets, configure one of the following in the cache behavior that's attached to your
distribution:

- Forward all viewer request headers to your origin. You can use the [AllViewer managed origin
  request policy](using-managed-origin-request-policies.md#managed-origin-request-policy-all-viewer "using-managed-origin-request-policies.md#managed-origin-request-policy-all-viewer").
- Specifically forward the `Sec-WebSocket-Key` and
  `Sec-WebSocket-Version` request headers in your origin request
  policy.

## How the WebSocket protocol works

The WebSocket protocol is an independent, TCP-based protocol that allows you to
avoid some of the overhead—and potentially increased latency—of
HTTP.

To establish a WebSocket connection, the client sends a regular HTTP request that
uses HTTP's upgrade semantics to change the protocol. The server can then complete
the handshake. The WebSocket connection remains open and either the client or server
can send data frames to each other without having to establish new connections each
time.

By default, the WebSocket protocol uses port 80 for regular WebSocket connections
and port 443 for WebSocket connections over TLS. The options that you choose for
your CloudFront [Viewer protocol policy](DownloadDistValuesCacheBehavior.md#DownloadDistValuesViewerProtocolPolicy "DownloadDistValuesCacheBehavior.md#DownloadDistValuesViewerProtocolPolicy") and [Protocol (custom origins only)](DownloadDistValuesOrigin.md#DownloadDistValuesOriginProtocolPolicy "DownloadDistValuesOrigin.md#DownloadDistValuesOriginProtocolPolicy") apply to WebSocket
connections and also HTTP traffic.

## WebSocket requirements

WebSocket requests must comply with [RFC 6455](https://datatracker.ietf.org/doc/html/rfc6455 "https://datatracker.ietf.org/doc/html/rfc6455") in the
following standard formats.

###### Example Sample client request

```
GET /chat HTTP/1.1
Host: server.example.com
Upgrade: websocket
Connection: Upgrade
Sec-WebSocket-Key: dGhlIHNhbXBsZSBub25jZQ==
Origin: https://example.com
Sec-WebSocket-Protocol: chat, superchat
Sec-WebSocket-Version: 13
```

###### Example Sample server response

```
HTTP/1.1 101 Switching Protocols
Upgrade: websocket
Connection: Upgrade
Sec-WebSocket-Accept: s3pPLMBiTxaQ9kYGzzhZRbK+xOo=
Sec-WebSocket-Protocol: chat

```

If the WebSocket connection is disconnected by the client or server, or by a
network disruption, client applications are expected to re-initiate the connection
with the server.

## Recommended WebSocket headers

To avoid unexpected compression-related issues when using WebSockets, we recommend
that you include the following headers in an [origin request
policy](origin-request-create-origin-request-policy.md "origin-request-create-origin-request-policy.md"):

- `Sec-WebSocket-Key`
- `Sec-WebSocket-Version`
- `Sec-WebSocket-Protocol`
- `Sec-WebSocket-Accept`
- `Sec-WebSocket-Extensions`

###### Note

Currently, CloudFront only supports WebSocket connections over the HTTP/1.1
protocol.
