

# Bypassing the IPS engine for accepted traffic
<a name="firewall-rule-ips-bypass"></a>

By default, traffic that the firewall engine accepts advances to the IPS engine for threat inspection. You can configure an accept rule to also bypass the IPS engine, so that the accepted connection goes straight to its destination without IPS inspection. The most common reason to do this is to exempt specific trusted traffic that would otherwise trigger a false positive in your IPS rules—for example, a known-good application whose traffic matches a signature that isn't relevant to it. Apply a bypass only to traffic that you have independently determined is trusted.

**Important**  
Bypassing the IPS engine means the matched traffic receives no threat inspection from your IPS section rules—and also none from the AWS managed rule groups in the IPS section, including the Active Threat Defense and threat signature rule groups. The console adds the Active Threat Defense managed rule group to a Next Generation policy by default, so a bypass skips it too. In other words, the entire IPS engine is bypassed for the matched traffic. Apply an IPS bypass only to traffic that you have independently determined is trusted. The IPS bypass is the secondary `pass` action, and it's valid only at the `flow` or `packet` scope.

You set the bypass on a modeled rule with the `BypassIPSEnabled` setting. In a raw rule string, the bypass is a secondary `pass` action that you chain to the rule's primary `accept` action, in the form `{{accept}}:{{scope}},pass:{{scope}}`. The `pass` action is only ever a secondary action—there's no standalone `pass` verb in the firewall engine.

**Note**  
The visual rule builder in the console doesn't provide a control for the IPS bypass. To bypass the IPS engine, either set `BypassIPSEnabled` through the API, or author the rule as a rule string that chains the secondary `pass` action to the primary `accept` action—for example, `accept:flow,pass:flow`. You can enter such a rule string in the console when you author the rule group from a rule string rather than with the visual rule builder.

The bypass `pass` must use the same scope as the primary `accept`, and only the `flow` and `packet` scopes are valid for a bypass. A rule that pairs a bypass with an `accept:tx` or `accept:hook` primary is rejected when you create or update the rule group, because the transaction and hook scopes can't carry a flow-level or packet-level bypass. Use `accept:flow,pass:flow` to bypass the IPS engine for the rest of the connection, or `accept:packet,pass:packet` to bypass it for the current packet.

**Example Accepting a connection and bypassing the IPS engine**  
The following rule accepts TCP traffic to port 443 at the flow scope and sends the accepted connection straight to its destination, skipping the IPS engine:  

```
accept:flow,pass:flow tcp:all $HOME_NET any -> $EXTERNAL_NET 443 (sid:1001;)
```
You can combine the bypass with alerting. The following rule bypasses the IPS engine and also generates an alert log for the matched traffic:  

```
accept:flow,pass:flow,alert tcp:all $HOME_NET any -> $EXTERNAL_NET 443 (sid:1002;)
```