This guide provides documentation for Wickr Enterprise. If you're using
AWS Wickr, see [AWS Wickr
Administration Guide](../adminguide/what-is-wickr.md "../adminguide/what-is-wickr.md") or [AWS Wickr
User Guide](../userguide/what-is-wickr.md "../userguide/what-is-wickr.md").

# Calling settings

- **Require Calling Nodes**: When this setting is enabled, Wickr’s
  calling services are only deployed on Kubernetes Nodes with the label
  `role=calling`. Disable this setting to deploy Calling and Messaging services on the
  same nodes, or for single node deployments.

You will generally also want to disable the calling TCP Proxy when this setting is
disabled, because the TCP Proxy service runs on port 443.

- **Enable TCP Proxy**: This setting controls whether or not the service
  for TCP fallback mode on calls is deployed. Disable this setting if you have other services
  running on 443/tcp or do not require TCP fallback mode for calls. This must be enabled for
  deployments planning to use Wickr Open Access.
- **Automatically discover server public IP addresses**: When this setting
  is enabled, the calling services will discover their public IP address by making HTTPS requests
  to [https://ipv4.icanhazip.com/](https://ipv4.icanhazip.com/ "https://ipv4.icanhazip.com/") and [https://ipv6.icanhazip.com/](https://ipv6.icanhazip.com/ "https://ipv6.icanhazip.com/").
  When disabled, you must enable the “Use host primary IP address for Calling traffic” or
  “Hostname override” setting otherwise the calling services will fail to start.
- **Use host primary IP address for Calling traffic**: Use the primary IP
  address of the Kubernetes nodes for calling services. This implies that all Wickr clients are
  able to connect to your Kubernetes nodes on the primary IP address of the node, as presented in
  `status.hostIP` from the [Downward
  API](https://kubernetes.io/docs/concepts/workloads/pods/downward-api/ "https://kubernetes.io/docs/concepts/workloads/pods/downward-api/").
- **Hostname override**: Provide a hostname or IP address to return as the
  connectivity point for Calling services. This setting should only be used when running a single
  calling server, because the same value is returned for all replicas of the service. When a
  hostname override is set and the “use host primary IP address” setting is enabled, the host
  primary IP address setting takes precedence.
- **Calling Host Network Enabled**: By default, calling pods use the nodes'
  host network for connectivity. Disable this to expose a NodePort service for calling traffic.
  If calling ingress is enabled, make sure that an appropriate service is configured to allow
  ingress traffic. This must be disabled for STIG compliance.
