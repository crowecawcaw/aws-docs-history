

# Key concepts for a NAT/Proxy firewall

Firewall capability  
The way that a firewall handles traffic. You choose either **routed firewall** or **NAT/Proxy firewall** when you create the firewall. You can't change the capability of an existing firewall.

Explicit proxy  
Clients send HTTP and HTTPS proxy requests (HTTP `CONNECT`) directly to the firewall's proxy hostname, instead of having their traffic steered to the firewall by VPC route tables. The firewall inspects each request against the firewall policy and connects to allowed destinations on the client's behalf. Clients don't need route table changes, only proxy settings such as the `http_proxy` and `https_proxy` environment variables.

Proxy hostname  
The fully qualified domain name that clients use to reach the explicit proxy. Each NAT/Proxy firewall has one proxy hostname, which is the same in every Availability Zone and every VPC where the firewall has an endpoint. By default, the hostname has the format `proxy-{{id}}.nfw.{{region}}.amazonaws.com`. You can use a custom hostname instead. For information about using a custom proxy hostname, see [Using a custom proxy hostname and certificate](nfw-proxy-custom-hostname.md).

Proxy listeners  
The ports that the explicit proxy accepts requests on. A firewall can have one HTTP listener and one HTTPS listener. The defaults are port 3128 for HTTP and port 8443 for HTTPS.

NAT gateway and firewall endpoint per Availability Zone  
In each Availability Zone that the firewall runs in, Network Firewall creates exactly one NAT gateway in a NAT subnet and exactly one firewall endpoint in a separate firewall endpoint subnet. Traffic that enters through an Availability Zone's firewall endpoint leaves through that Availability Zone's NAT gateway. The NAT gateways are resources in your account.

Non-proxy traffic  
Traffic that reaches the firewall endpoint through your VPC route tables and isn't addressed to a proxy listener. By default, after a NAT/Proxy firewall inspects non-proxy traffic, it sends the traffic out through the NAT gateway. You can choose instead to return non-proxy traffic to the firewall endpoint without address translation.