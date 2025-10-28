# Troubleshooting rules in AWS Network Firewall

Use the information here to help you diagnose common issues that you might encounter when working with rules in Network Firewall.

## Rules with the `HOME_NET` variable are not working as expected with managed rule groups

If your firewall is deployed in a centralized inspection VPC the `HOME_NET` variable uses the Classless Inter-Domain Routing (CIDR) ranges of VPC where the firewall is deployed. You can override the `HOME_NET` in your firewall policy to add the CIDR ranges of your application (spoke) VPCs that you want to filter. Once you define the `HOME_NET` variable, Network Firewall maintains that the value of `EXTERNAL_NET` in the rule group is the negation of the `HOME_NET` value that you define at the firewall policy level. Policy variables affect all rule groups that don't already define `HOME_NET`. For more information, see [Firewall policy settings in AWS Network Firewall](firewall-policy-settings.md "firewall-policy-settings.md").

## I created a rule to allow only outbound traffic from `HOME_NET` to `EXTERNAL_NET`, but `EXTERNAL_NET` was also able to initiate a connection back to `HOME_NET`. How do I prevent this from happening?

You have to ensure that your firewall rules are not wide open to allow unintended traffic. The following example ensures that only trusted traffic is allowed to pass through the firewall in Network Firewall.

###### Example 1 - Do not use

In this example, Network Firewall allows TCP traffic from `HOME_NET` to `EXTERNAL_NET`. However, this rule also allows inbound traffic from `EXTERNAL_NET` to `HOME_NET` because `<>` means "any direction."

```
pass tcp $HOME_NET any <> $EXTERNAL_NET any. (msg:“sid1”; sid:1;)
```

###### Example 2 - Do not use

In this example traffic from `HOME_NET` is allowed to initiate TCP connections to `EXTERNAL_NET`, but since the rule is missing the `flow:to_server` keyword, there are scenarios where this rule will also allow `EXTERNAL_NET` to initiate connections to `HOME_NET`.

```
pass tcp $HOME_NET any -> $EXTERNAL_NET any (msg:“sid1”; sid:1;)
```

You should write rules such that only trusted traffic is allowed through the firewall, and only in the direction you intend.

###### Example 3

If combined with the Network Firewall stateful default action **Drop established**, this rule ensures that traffic initiated by clients in `HOME_NET` to servers in `EXTERNAL_NET` is allowed, but clients in `EXTERNAL_NET` cannot initiate a connection to servers in `HOME_NET`.

```
pass tcp $HOME_NET any -> $EXTERNAL_NET 22 (msg:“sid1”; flow:to_server; sid:1;)
```

## I'm using strict ordering, but stateful rules near the bottom of my ruleset appear to be handling traffic before rules near the top of my ruleset

When network connections traverse Network Firewall's stateful rule engine, it will see the lower level protocol being used (for example TCP) before it sees the application layer protocol (for example HTTP). This means that it's possible to have a blanket TCP (layer 4) rule that comes later in the ruleset take action on traffic that an earlier HTTP (layer 7) rule in the ruleset was intended to handle. Example 1 below may accidentally allow unwanted traffic because rule 2 (TCP) will take action on the port 80 traffic before rule 1 (HTTP), since the TCP part of the connection will be seen by the firewall first. Example 2 uses the `flow:to_server;` keyword to ensure that only the intended traffic is allowed and “baddomain.com (http://baddomain.com/)” continues to be blocked.

###### Example 1 - Do not use

```
# Rule 1 is intended to block http traffic to baddomain.com
reject http $HOME_NET any -> $EXTERNAL_NET 80 (http.host; content:"baddomain.com"; startswith; endswith; sid:1;)
# Rule 2 accidently allows the TCP port 80 traffic even before any application protocol is inspected
pass tcp $HOME_NET any -> $EXTERNAL_NET 80 (sid:2;)

```

###### Example 2

```
# Rule 1 blocks http traffic to baddomain.com
reject http $HOME_NET any -> $EXTERNAL_NET 80 (http.host; content:"baddomain.com"; startswith; endswith; sid:1;)
# Rule 2 waits until later in the connection (when the application protocol can also be detected) before allowing it
pass tcp $HOME_NET any -> $EXTERNAL_NET 80 (flow:to_server; sid:2;)
```

## I've configured a drop action rule but traffic still goes through the firewall

The AWS Network Firewall stateful rule engine supports action order, previous known as default order, and strict rule evaluation order. Action rule order dictates that Network Firewall evaluates firewall rules based on a rule action. Network Firewall evaluates rules with a pass first, followed by drop, reject, and alert action rules. The stateful default action for a policy configured to use action order is pass. It's likely that the traffic matched one of the pass rules in your rule group and therefore it was not dropped by Network Firewall. We recommend that you use strict order so that Network Firewall will evaluate the rules in the order in which they are defined. When configuring a policy that uses strict order, configure the stateful default actions as **Drop established** and **Alert established**. For more information about evaluation order, see [Managing evaluation order for Suricata compatible rules in AWS Network Firewall](suricata-rule-evaluation-order.md "suricata-rule-evaluation-order.md").

## I have a rule that is intermittently not matching when I think it should

The AWS Network Firewall stateful rule engine has limits for traffic inspection parameters such as the maximum total size of all network packets it can inspect within a single network flow. If your traffic exceeds these limits, the stateful rule engine will not be able to match the rule. You can make use of keywords such as `stream-event:reassembly_depth_reached;` in your rules to handle these cases or to troubleshoot and diagnose when this happens. Example 1 shows how you might add an alert rule in a strict action order firewall policy to receive alert logs when the tcp reassembly depth limit is reached for a corresponding rule.

###### Example 1

```

# Rule 1 is intended to log when rule 2 cannot match due to hitting the TCP reassembly depth limit
alert tcp $HOME_NET any -> $EXTERNAL_NET 80 (flow:established,to_server; stream-event:reassembly_depth_reached; flowbits: set, stream_reassembly_depth_reached; classtype:protocol-command-decode; sid:1;)
# Rule 2
drop tcp $HOME_NET any -> $EXTERNAL_NET 80 (flow:established, to_server; sid:2;)

```

For information on how the stateful rule engine works, see [Firewall behavior in AWS Network Firewall](firewall-behavior.md "firewall-behavior.md").
