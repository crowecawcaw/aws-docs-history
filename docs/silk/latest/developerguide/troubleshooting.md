# Troubleshooting: Determining the client's IP address

By default, and when it's efficient, Amazon Silk routes requests through a remote proxy server
in the Amazon cloud. Thus, the source IP for a request may be that of the remote proxy, and
not of the originating client.

## Obtaining the Client IP Address

When Amazon Silk does not route requests through a remote proxy server, the source IP address
of the request can be obtained as it normally would be on any HTTP request.

When browsing is routed through a remote proxy, the source IP address of the end client
is supplied in the X-Forwarded-For request header. Note that different requests from a
single end user may be routed through different cloud servers. In other words, a website may
receive a series of requests from different source IP addresses but with the same
X-Forwarded-For header.

Additionally, a single Amazon Silk cloud server can support multiple end users. This means
that a website may see requests with the same source IP address but different
X-Forwarded-For headers.
