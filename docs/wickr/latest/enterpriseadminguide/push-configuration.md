This guide provides documentation for Wickr Enterprise. If you're using AWS Wickr, see [AWS Wickr
Administration Guide](../adminguide/what-is-wickr.md "../adminguide/what-is-wickr.md").

# Push configuration

The **Push Configuration** section has available options for proxy or
intermediary networking devices. This can also be used to obfuscate the infrastructure by forcing
users to connect to proxies which then forward traffic to the Messaging/App server.

###### Note

Push configuration entries supersede any connection information in a config file or
deeplink.

- **Messaging Domains:** Domains and IP addresses accepting client
  connections.
- **Voice & Video Domains:** Domains and IP addresses accepting client
  calls.
- **Certificate Pinning:** Accepts only authorized pinned certificates for
  authentication of client-server connections.
- **SSL Certificates:** The SSL certificate used during installation is
  here automatically.
  We recommend using intermediate certificates instead of a leaf.
