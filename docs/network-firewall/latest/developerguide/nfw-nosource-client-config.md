# Configuring workloads for the proxy

You can direct HTTP and HTTPS traffic from your workloads to the firewall's proxy listener. The firewall receives HTTP CONNECT requests, evaluates the requested domain against your security rules, and establishes connections to allowed destinations on behalf of the client.

## Setting proxy environment variables

Configure your workloads to use the firewall's hostname as their HTTP/HTTPS proxy.

###### Linux

Set the following environment variables:

```
export http_proxy="http://FIREWALL_HOSTNAME:HTTP_PORT"
export https_proxy="https://FIREWALL_HOSTNAME:HTTPS_PORT"
export no_proxy="169.254.169.254,localhost"
```

For example, with a firewall FQDN of `my-firewall.us-east-1.nfw.amazonaws.com` listening on ports 3128 (HTTP) and 8080 (HTTPS):

```
export http_proxy="http://my-firewall.us-east-1.nfw.amazonaws.com:3128"
export https_proxy="https://my-firewall.us-east-1.nfw.amazonaws.com:8080"
export no_proxy="169.254.169.254,localhost"
```

## Hostname resolution

When you create a VPC endpoint association, Network Firewall automatically creates private hosted zones in the associated VPCs. These hosted zones resolve the firewall's hostname to the local VPC endpoint IP address.

You do not need to configure DNS manually. Resolution is handled automatically.

## HTTP and HTTPS listeners

Your firewall's proxy settings define one or more listeners with a port and type (HTTP or HTTPS). The listener type determines how clients establish the initial connection to the proxy.

| Listener type | Client connection                                            | Certificate                                                              | Use case                                                                |
| ------------- | ------------------------------------------------------------ | ------------------------------------------------------------------------ | ----------------------------------------------------------------------- |
| HTTP          | Client sends HTTP CONNECT in plaintext to the proxy port     | None required                                                            | Simpler setup; proxy request is unencrypted between client and firewall |
| HTTPS         | Client establishes TLS with the proxy before sending CONNECT | Amazon public certificate (ACM-signed, trusted by standard trust stores) | Encrypts the proxy connection between client and firewall               |
