

# Working with IPS rule groups in AWS Network Firewall

An *IPS rule group* holds the threat detection and prevention rules that the IPS engine evaluates. You author IPS rules as raw Suricata compatible rule strings, using the same syntax and semantics as the stateful rules in a Classic Network Firewall policy. For information about writing Suricata compatible rules, see [Working with stateful rule groups in AWS Network Firewall](stateful-rule-groups-ips.md).

Because IPS rules use the same Suricata compatible syntax as Classic Network Firewall stateful rules, the stateful rule examples in [Examples of stateful rules for Network Firewall](suricata-examples.md) apply to IPS rules as well. An IPS rule group also supports rule variables and the same IP set references as a Classic Network Firewall stateful rule group—an IP set reference can point to an Amazon Virtual Private Cloud managed prefix list, a resource group, an address list, or a container association. A rule group can reference up to 5 IP set references (prefix lists, resource groups, or address lists) or up to 30 container associations, and you can't mix the two types in the same rule group. For more information about IP set references, see [IP set references in Suricata compatible AWS Network Firewall rule groups](rule-groups-ip-set-references.md). The limitations and caveats for Suricata compatible stateful rules apply to IPS rules; see [Limitations and caveats for stateful rules in AWS Network Firewall](suricata-limitations-caveats.md).

The following examples show IPS rules for common threat-prevention tasks. Unlike firewall rules, IPS rules don't use hooks or carrier rules—they inspect the traffic that the firewall engine has already accepted, using standard Suricata compatible syntax.

**Example Block deprecated TLS versions**  
This rule drops any connection that negotiates TLS 1.0 or TLS 1.1, enforcing a minimum TLS version across all traffic that reaches the IPS engine. The negotiated version is known only from the server's `ServerHello`, so the rule inspects the server-to-client direction (`$EXTERNAL_NET any -> $HOME_NET any` with `flow:established,to_client`). A rule written in the client-to-server direction would match the version the client offered instead of the version the connection negotiates.  

```
drop tls $EXTERNAL_NET any -> $HOME_NET any (msg:"Deprecated TLS version blocked"; flow:established,to_client; ssl_version:tls1.0,tls1.1; sid:100; rev:1;)
```

**Example Block a known-bad destination by TLS SNI**  
This rule drops a connection whose TLS server name indication matches a domain you want to block, such as a known command-and-control domain. Use a denylist of specific domains in the IPS engine, and rely on the firewall engine's allow list for the general egress posture.  

```
drop tls $HOME_NET any -> $EXTERNAL_NET any (msg:"Blocked SNI"; tls.sni; content:"bad.example.com"; endswith; nocase; sid:101; rev:1;)
```

**Example Block an HTTP host**  
This rule drops an HTTP request whose `Host` header matches a domain you want to block. It applies to cleartext HTTP; to inspect HTTPS, attach a TLS inspection configuration to the policy.  

```
drop http $HOME_NET any -> $EXTERNAL_NET any (msg:"Blocked HTTP host"; http.host; content:"bad.example.com"; endswith; sid:102; rev:1;)
```

In your logs, an alert from the IPS engine carries `engine: td` (threat detection), which distinguishes it from a firewall engine alert (`engine: fw`). For more information about reading Network Firewall logs, see [Logging and monitoring in AWS Network Firewall](logging-monitoring.md).

SIDs that you use in rules you embed directly in a policy must be unique across all of the policy's embedded rules, including embedded IPS rules and embedded firewall rules. For more information, see [Signature ID uniqueness](firewall-policy-v2-sid-uniqueness.md).