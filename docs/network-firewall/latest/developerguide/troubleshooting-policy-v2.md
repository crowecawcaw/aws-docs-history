

# Troubleshooting Next Generation policies in AWS Network Firewall

Use the information here to help you diagnose common issues that you might encounter when working with Next Generation policies in Network Firewall. For information about Next Generation policies, see [Next Generation policies](firewall-policies-v2.md).

## My traffic is being dropped and I didn't configure a deny rule
<a name="troubleshoot-policy-v2-traffic-dropped-no-deny"></a>

The firewall engine in a Next Generation policy is drop by default. Traffic that isn't explicitly accepted is handled by the policy's firewall default action, which is **Drop** unless you change it. To allow traffic, author firewall rules that accept it. For more information, see [Firewall default action](firewall-policy-v2-default-action.md) and [Working with firewall rule groups in AWS Network Firewall](firewall-rule-groups.md).

To confirm whether the firewall default action is responsible, check the `FirewallDefaultActionApplied` CloudWatch metric. A nonzero value means that traffic is reaching the default action because it didn't match any firewall rule. For more information, see [AWS Network Firewall metrics in Amazon CloudWatch](monitoring-cloudwatch.md).

## My TLS-inspected traffic is blocked even though I wrote an allow rule for the domain
<a name="troubleshoot-policy-v2-tls-blocked-with-allow"></a>

Allowing a TLS-inspected domain through the firewall engine requires two firewall rules: a TLS rule—an `accept:flow` or `accept:tx` rule at the TLS `client_hello` hook—that matches the SNI, and an HTTP rule that matches the `Host` header. The TLS rule allows the connection past the TLS handshake stage; the HTTP rule allows the decrypted request. Under a **Drop** or **Reject** default action, if either rule is missing the traffic falls through to the default action at that stage and is dropped—so a TLS rule without its paired HTTP rule still results in a block at the decrypted request stage. Author both rules for the domain. For more information, see [How rules are evaluated for TLS-inspected traffic](tls-inspection-policy-v2-tls-gate.md) and [Authoring a TLS rule and an HTTP rule for each allowed domain](tls-inspection-policy-v2-two-rules.md).

## My TLS-inspected connections are reset right after the ClientHello
<a name="troubleshoot-policy-v2-tls-reset-after-clienthello"></a>

The client receives a TCP reset immediately after it sends its TLS ClientHello—for example, `curl` reports `Recv failure: Connection reset by peer`. No ServerHello arrives, and the server is never contacted.

Under a **Drop** or **Reject** default action, this means no firewall rule allowed the website name at the TLS handshake stage: no `accept:flow` or `accept:tx` rule at the TLS `client_hello` hook matched the connection's SNI, so the connection was blocked at that stage. A block by the default action is recorded in your alert logs, tagged with the TLS hook.

To fix it, add a firewall rule that allows the website name—an `accept:flow` or `accept:tx` rule at the TLS `client_hello` hook that matches the SNI—together with the paired HTTP rule for the decrypted request. For more information, see [How rules are evaluated for TLS-inspected traffic](tls-inspection-policy-v2-tls-gate.md) and [Authoring a TLS rule and an HTTP rule for each allowed domain](tls-inspection-policy-v2-two-rules.md).

## My firewall rule at a later hook never matches
<a name="troubleshoot-policy-v2-rule-at-later-hook-never-matches"></a>

By default, the firewall engine is drop by default, so a connection reaches a rule's hook only if it was accepted at every earlier hook. (You can change this with the firewall default action, but **Drop** is the default.) If a rule at a later hook never matches, the connection is probably being blocked before it reaches that hook. Set accept prior hooks to true on the rule so that Network Firewall accepts the earlier hooks for you, or author accept rules for the earlier hooks yourself. For more information, see [Accepting prior hooks automatically](firewall-rule-groups-accept-prior-hooks.md).

To see exactly where a connection is getting to and what it matches, put the policy in monitor mode and review your logs. In monitor mode, nothing is blocked and every rule match and default action generates an alert log entry, so you can trace the connection through the hooks and see whether it's matching a drop or reject rule or falling through to the firewall default action. For more information, see [Policy mode: enforce and monitor](firewall-policy-v2-policy-mode.md) and [Logging for a Next Generation policy in AWS Network Firewall](logging-policy-v2.md).

## I turned on monitor mode but traffic isn't being blocked
<a name="troubleshoot-policy-v2-monitor-mode-not-blocking"></a>

This is expected behavior. In monitor mode, both engines evaluate traffic and generate log records, but no traffic is dropped or rejected. To enforce your rules, change the policy mode to enforce. For more information, see [Policy mode: enforce and monitor](firewall-policy-v2-policy-mode.md). A few kinds of block still happen in monitor mode, such as TLS-layer resets, TLS inspection certificate revocation checks, and Route 53 Resolved IP validation. For more information, see [I'm in monitor mode but some traffic is still being blocked](#troubleshoot-policy-v2-monitor-mode-still-blocking).

## I'm in monitor mode but some traffic is still being blocked
<a name="troubleshoot-policy-v2-monitor-mode-still-blocking"></a>

In monitor mode, a Next Generation policy doesn't drop or reject traffic based on your rules, the firewall default action, or the stream exception policy. The exceptions are the following, which still block or reset connections even in monitor mode:
+ TLS-layer resets—a missing or invalid Server Name Indication (SNI), an SNI that doesn't match the server's certificate, or a failed handshake. Network Firewall resets these connections at the TLS layer regardless of the policy mode.
+ TLS inspection certificate revocation checks whose action for a revoked certificate or an unknown status is **Drop** or **Reject**. Network Firewall still blocks connections to servers whose certificates are revoked, or whose revocation status can't be determined. An unknown status includes revocation checks that fail or time out.
+ Route 53 Resolved IP validation, which still applies its configured action and DNS expiry exception policy in monitor mode.

For more information about how policy mode affects traffic, see [Policy mode: enforce and monitor](firewall-policy-v2-policy-mode.md).

If you see blocked traffic while a policy is in monitor mode, check your TLS inspection revocation-check logs and metrics to see whether revocation checks are the cause. For more information, see [Logging for TLS inspection in AWS Network Firewall](tls-inspection-logging.md).