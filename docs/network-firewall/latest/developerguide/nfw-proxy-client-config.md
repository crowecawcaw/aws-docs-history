

# Configuring workloads to use the proxy

To send traffic through the explicit proxy, configure your applications' proxy settings to use the firewall's proxy hostname on a listener port. Clients that use the explicit proxy don't need route table changes. To inspect traffic that doesn't use the explicit proxy, update your VPC route tables to send that traffic to the firewall endpoint in the same Availability Zone. For information about configuring route tables, see [VPC route table configuration for AWS Network Firewall](vpc-config-route-tables.md).

You can find the proxy hostname in the console, on the firewall's details page, in the **Endpoints and identity** section. The hostname appears after the firewall is ready. In the API, the hostname is in the `DnsName` field of each Availability Zone's attachment in the `DescribeFirewall` response.

## Setting proxy environment variables
<a name="nfw-proxy-env-vars"></a>

On Linux, set the following environment variables:

```bash
export http_proxy="http://{{PROXY_HOSTNAME}}:{{HTTP_PORT}}"
export https_proxy="https://{{PROXY_HOSTNAME}}:{{HTTPS_PORT}}"
export no_proxy="169.254.169.254,localhost"
```

For example, for a firewall with the proxy hostname `proxy-0123456789abcdef0.nfw.us-west-2.amazonaws.com` and the default listener ports:

```bash
export http_proxy="http://proxy-0123456789abcdef0.nfw.us-west-2.amazonaws.com:3128"
export https_proxy="https://proxy-0123456789abcdef0.nfw.us-west-2.amazonaws.com:8443"
export no_proxy="169.254.169.254,localhost"
```

The `no_proxy` setting keeps requests to the instance metadata service and to the local host from going through the proxy.

## Hostname resolution
<a name="nfw-proxy-hostname-resolution"></a>

Network Firewall creates Route 53 private hosted zones so that the proxy hostname resolves in the firewall's VPC and in any VPC with a VPC endpoint association for the firewall. You don't need to configure DNS.
+ The hostname resolves to the firewall endpoint in the client's own Availability Zone, so traffic stays in that Availability Zone and leaves through its NAT gateway.
+ The hostname doesn't resolve in Availability Zones that the firewall doesn't run in, and there's no failover to another Availability Zone.
+ The DNS records have a time to live (TTL) of 60 seconds. After you remove an Availability Zone, clients might use a cached answer for up to about a minute.
+ Clients must use the VPC's Route 53 Resolver, which is the default for Amazon EC2 instances.

## HTTP and HTTPS listeners
<a name="nfw-proxy-listeners"></a>

The listener type determines how clients establish the initial connection to the proxy. A firewall can have at most one HTTP listener and one HTTPS listener, on different ports from 1 through 65535. It must have at least one listener.


| Listener type | Client connection | Certificate | Use case | 
| --- | --- | --- | --- | 
| HTTP (default port 3128) | The client sends HTTP CONNECT in plaintext to the proxy port. | None | Simpler setup. The proxy request is unencrypted between the client and the firewall. | 
| HTTPS (default port 8443) | The client establishes TLS with the proxy before it sends CONNECT. | A public certificate that Network Firewall manages for the default hostname, or your ACM certificate for a custom hostname | Encrypts the proxy connection between the client and the firewall. | 