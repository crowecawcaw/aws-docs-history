

# Troubleshooting a NAT/Proxy firewall in AWS Network Firewall

Use the information here to help you diagnose common issues with NAT/Proxy firewalls. For information about this capability, see [NAT/Proxy firewall in AWS Network Firewall](nfw-proxy.md).

## The firewall shows a failed status after you create it
<a name="troubleshoot-nfw-proxy-create-failed"></a>

If Network Firewall can't create the NAT gateway in an Availability Zone, that Availability Zone's firewall endpoint shows a failed status, and the whole firewall shows a failed status, even if other Availability Zones are ready. The status message includes the error that Amazon EC2 returned. Common causes include the following:
+ Your account reached its NAT gateway or Elastic IP address quota.
+ An Elastic IP address is already associated with another resource.
+ A private IP address isn't available in the NAT subnet, or isn't in the NAT subnet's IPv4 CIDR block.
+ The caller doesn't have the required Amazon EC2 permissions, or the caller's credentials expired during the operation. For information about the required permissions, see [Permissions for a NAT/Proxy firewall](nfw-proxy-permissions.md).

To recover, resolve the cause, delete the firewall, and create it again. When you delete a firewall that failed to create, Network Firewall deletes the NAT gateways that it created for that firewall. For information about viewing status messages, see [Troubleshooting firewall endpoint failures in AWS Network Firewall](firewall-troubleshooting-endpoint-failures.md).

## An Availability Zone that you added shows a failed status
<a name="troubleshoot-nfw-proxy-az-failed"></a>

When you add an Availability Zone to an existing firewall and Network Firewall can't create its NAT gateway, only that Availability Zone shows a failed status. The firewall's other Availability Zones keep working. To recover, remove the Availability Zone, resolve the cause from the status message, and add the Availability Zone again. For information about adding and removing Availability Zones, see [Removing an Availability Zone](nfw-proxy-managing.md#nfw-proxy-removing-az) and [Adding an Availability Zone](nfw-proxy-managing.md#nfw-proxy-adding-az).

## You can't remove an Availability Zone
<a name="troubleshoot-nfw-proxy-remove-az-blocked"></a>

If a VPC endpoint association exists for the firewall in the Availability Zone, the request to remove the Availability Zone fails with a `ResourceReverseReferencesNotEmptyException` error that lists the associations. Delete those VPC endpoint associations, and then try again. Associations in other Availability Zones don't block the request.

You also can't remove the firewall's last Availability Zone. To remove it, delete the firewall.

## Clients can't resolve or reach the proxy hostname
<a name="troubleshoot-nfw-proxy-hostname"></a>

Check the following:
+ The firewall status is `READY`. The proxy hostname appears after the firewall is ready.
+ The client is in an Availability Zone that the firewall runs in. The hostname doesn't resolve in other Availability Zones.
+ The client uses the VPC's Route 53 Resolver.
+ The client is in the firewall's VPC or in a VPC with a VPC endpoint association for the firewall in the same Availability Zone.
+ The client's proxy settings use a listener port that the firewall has, with the matching scheme (`http://` for the HTTP listener, `https://` for the HTTPS listener).

## Errors with a custom hostname or certificate
<a name="troubleshoot-nfw-proxy-custom-hostname"></a>

The following errors can occur when you create a firewall with a custom hostname and certificate:
+ `ProxySettings.DomainName is required when ProxySettings.CertificateArn is provided.` – Specify both the hostname and the certificate, or neither.
+ The certificate must name a certificate in the same account and Region as the firewall – Use an ACM certificate from the firewall's account and AWS Region.
+ The domain name isn't valid, or uses the reserved `proxy-{{id}}.nfw.{{region}}.amazonaws.com` format – Use a fully qualified domain name with at least two labels and no wildcard.
+ The request fails with a parameter that names your domain as invalid – Check that the certificate's subject alternative names cover the hostname.

When you update the proxy listeners of a firewall that uses a custom hostname, include the same `CertificateArn` and `DomainName` in the `UpdateProxySettings` request. You can't change or remove them after you create the firewall.

If the HTTPS listener stops accepting connections, check that the certificate is still valid in ACM and that your clients trust its certificate authority. Network Firewall doesn't report an unusable certificate in the firewall's status.

For information about using a custom proxy hostname, see [Using a custom proxy hostname and certificate](nfw-proxy-custom-hostname.md).

## Preventing domain spoofing with a NAT/Proxy firewall
<a name="troubleshoot-nfw-proxy-domain-spoofing"></a>

A NAT/Proxy firewall's users can prevent domain spoofing on their proxied traffic in several ways. The following approaches describe the options.

For proxied traffic, the firewall generates DNS requests to the Route 53 DNS resolver in the VPC of the NAT gateway for the domain name in the CONNECT header. All DNS requests flow through the stateful inspection engine, so you can add DNS and mDNS rules that block requests to a known bad domain name to prevent DNS spoofing. You can also use a DNS pass rule for the domains that you want to allow, as in the following example, together with a default drop action, to prevent spoofing.

```
pass dns any any -> 169.254.169.253 [53,5353] (msg:"Allow dns.google"; dns.query; content:"dns.google"; nocase; sid:9900102;)
pass mdns any any -> 169.254.169.253 [53,5353] (msg:"Allow dns.google on mdns"; mdns.queries.rrname; content:"dns.google"; nocase; sid:9900203;)
```

You can also use the AWS Network Firewall IP validation feature to block domain spoofing. Add a rule with the `aws_route_53_resolved_domain` keyword, as in the following example, together with a default drop action, to prevent spoofing for an SNI.

```
pass tls $HOME_NET any -> $EXTERNAL_NET any (tls.sni; content:"good.com"; nocase; startswith; endswith; aws_route_53_resolved_domain:"good.com"; flow:to_server, established; sid:5;)
pass http $HOME_NET any -> $EXTERNAL_NET any (http.host; content:"good.com"; nocase; startswith; endswith; aws_route_53_resolved_domain:"good.com"; flow:to_server, established; sid:6;)
```

**Note**  
To use the proxy and the IP validation feature together, add 169.254.169.253 to the bypass destination validation IP ranges in your Network Firewall IP validation configuration, so that DNS queries that originate from the proxy can reach the Route 53 resolvers.

For more information, see [Resolved IP validation in AWS Network Firewall](route53-resolved-ip-validation.md).

You can also prevent domain spoofing by enabling TLS inspection for your proxied traffic. With TLS inspection, the firewall verifies the server certificate against public certificate authorities, so the SNI can't be spoofed. For more information, see [Inspecting SSL/TLS traffic with TLS inspection configurations in AWS Network Firewall](tls-inspection-configurations.md).