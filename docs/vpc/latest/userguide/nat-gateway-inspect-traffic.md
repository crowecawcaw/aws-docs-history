

# Inspect traffic from NAT gateways
<a name="nat-gateway-inspect-traffic"></a>

You can attach Network Firewall Proxy to your NAT Gateway to inspect and filter traffic on your NAT Gateway. This security control allows you to prevent data leaks outside your trusted perimeter and blocks any undesired inbound response.

## How it works
<a name="nat-gateway-proxy-how-it-works"></a>

When creating a Network Firewall Proxy, you're required to select an existing NAT Gateway to attach the Proxy on. Once created, the Proxy:
+ The Proxy comes with a fully qualified domain name and you need to set set your applications to send http and https connect requests to the Proxy. The proxy first filters the domain name in the connect request based on the rules entered by the customer. If allowed by the customer, the proxy then makes a DNS query to get the IP address of the domain. It then established TCP connection with the end destination. Based on whether TLS decryption is enabled, the proxy then filters the TLS connection on the IP address and header attributes and only established a TLS connection with the destination if the IP and header attributes (including the header action and the url path) are allowed by the policies.
+ The appliance inspects and filters the traffic.
+ Allowed traffic continues to the destination (in the internet or on-prem environment or another VPC).

## Attaching appliances
<a name="nat-gateway-attaching-appliances"></a>

Appliances are attached to NAT Gateways through AWS Network Firewall. For steps on creating and attaching appliances, see the [Network Firewall Proxy Developer Guide](https://docs.aws.amazon.com/network-firewall/latest/developerguide/network-firewall-proxy-developer-guide.html).

## Viewing attached appliances
<a name="nat-gateway-viewing-attached-appliances"></a>

To view appliances attached to your NAT Gateway, use the [describe-nat-gateways](https://docs.aws.amazon.com/cli/latest/reference/ec2/describe-nat-gateways.html) command:

```
aws ec2 describe-nat-gateways --nat-gateway-ids nat-1234567890abcdef0
```

The response includes an `AttachedAppliances` field showing:
+ **Type** – The appliance type (e.g., `network-firewall-proxy`)
+ **ApplianceArn** – The ARN of the attached appliance
+ **AttachmentState** – Current attachment status (`attached`, `detaching`, `detached`, `attach_failed`, `detach_failed`)
+ **ModificationState** – Current modification status (`modifying`, `completed`, `failed`)
+ **VpcEndpointId** – The VPC endpoint ID used to route traffic from application VPCs to the proxy for inspection and filtering
+ **FailureCode** – The failure code if the appliance attachment or modification operation failed
+ **FailureMessage** – A descriptive message explaining the failure if the appliance attachment or modification operation failed