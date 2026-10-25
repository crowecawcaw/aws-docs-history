

# Configuring resolved IP validation on the firewall policy
<a name="route53-resolved-ip-validation-policy-setting"></a>

Set resolved IP validation on the firewall policy. For where this fits among the other policy settings, see [Firewall policy settings in AWS Network Firewall](firewall-policy-settings.md). For the API structure, see [Route53ResolvedIPValidation](https://docs.aws.amazon.com/network-firewall/latest/APIReference/API_Route53ResolvedIPValidation.html) in the *AWS Network Firewall API Reference*.

Use these settings to control which connections the firewall validates and what happens when validation fails. Resolved IP validation has the following settings:
+ **Action** (required) – The enforcement mode for connections that fail resolved IP validation. Valid values: `ALERT` \| `DROP` \| `REJECT`. `ALERT` tags the matching connection in the firewall's flow logs without blocking it, and requires that you enable logging. `DROP` silently blocks the connection. `REJECT` blocks the connection and sends a TCP reset to the client. Reject applies to TCP. Network Firewall drops non-TCP traffic.
+ **DNS Firewall rule group ID** (required) – The ID of the Amazon Route 53 Resolver DNS Firewall rule group whose associated VPCs' resolutions Network Firewall uses for validation. Associate this rule group with the VPCs that send traffic to the firewall. The ID must match the pattern `rslvr-frg-<id>`, and must exist and be accessible from your account.

  Changing this value swaps the DNS Firewall rule group association and is processed asynchronously. While a swap is in progress, further changes to resolved IP validation are rejected until the policy returns to the `ACTIVE` state.
+ **DNS expiry exception policy** (required) – The action to take when a recorded resolution has expired from the resolved IP cache but the firewall still sees traffic to that IP address. Valid values: `CONTINUE` \| `DROP` \| `REJECT`. `CONTINUE` treats the expired resolution as still valid. `DROP` silently blocks the connection. `REJECT` blocks the connection and sends a TCP reset.

  Resolved IP validation keeps a resolution in the resolved IP cache for longer than the DNS record's time to live (TTL), so a short TTL alone doesn't cause connections to fail.
+ **Source IP ranges** (optional) – The client source IP address ranges whose connections are validated. Specify up to 100 IPv4 or IPv6 addresses or CIDR ranges. If you don't specify any ranges, validation applies to the firewall's VPC CIDR ranges.

  This scope applies to the policy-level check only. Stateful rules that use the `AWS_ROUTE_53_RESOLVED_DOMAIN` target type or the `aws_route_53_resolved_domain` keyword still evaluate their destinations regardless of this setting.
+ **Bypass destination validation IP ranges** (optional) – Destination IP address ranges that are exempt from the policy-level check. Specify up to 100 IPv4 or IPv6 addresses or CIDR ranges.

  This exemption applies only to the policy-level check. Stateful rules that use the `AWS_ROUTE_53_RESOLVED_DOMAIN` target type or the `aws_route_53_resolved_domain` keyword still evaluate connections to these destinations.

Removing resolved IP validation from the policy tears down the DNS Firewall rule group association, and the feature stops applying.