

# Valid combinations and constraints for firewall rules

A firewall rule combines an action and scope, a protocol and hook, a source and destination, and a set of matching keywords. Not every combination is valid: the action limits the scopes you can use, the hook limits the keywords you can match, and some keywords match only at one specific point in a connection. Network Firewall validates these combinations when you create or update a rule group, and rejects a rule group that contains an invalid rule, identifying the rule by its SID. This section describes the constraints so that you can author rules that validate the first time.

A firewall rule in rule-string form has the following shape. The constraints in this section apply the same way to modeled rules, because Network Firewall compiles each modeled rule into one rule string of this form.

```
{{action}}:{{scope}} {{protocol}}:{{hook}} {{source}} {{source-port}} -> {{destination}} {{destination-port}} ({{keywords}}; sid:{{N}};)
```

The firewall engine is built on Suricata's firewall mode. For further reading on the underlying actions, action scopes, rule hooks, and connection states that these constraints are based on, see [Firewall design](https://docs.suricata.io/en/suricata-8.0.3/firewall/firewall-design.html) in the [Suricata User Guide](https://docs.suricata.io/en/suricata-8.0.3/index.html). For the complete list of hooks that each protocol exposes and the keywords valid at each one, see the same documentation and the `--list-app-layer-hooks` output for the Suricata version that Network Firewall runs.