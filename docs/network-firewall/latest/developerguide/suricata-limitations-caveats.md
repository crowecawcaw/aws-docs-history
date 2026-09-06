

# Limitations and caveats for stateful rules in AWS Network Firewall
<a name="suricata-limitations-caveats"></a>

AWS Network Firewall stateful rules are Suricata compatible. Most Suricata rules work without modification with Network Firewall. Your use of Suricata rules with Network Firewall has the restrictions and caveats listed in this section. 

## Suricata features that Network Firewall doesn't support
<a name="suricata-not-supported"></a>

The following Suricata features are not supported by Network Firewall:
+ Datasets. The keywords `dataset` and `datarep` aren't allowed.
+ ENIP/CIP keywords. 
+ File extraction. File keywords aren't allowed. 
+ FTP-data protocol detection.
+ IP reputation. The `iprep` keyword is not allowed. 
+ Lua scripting.
+ Rules actions except for pass, drop, reject, and alert. Pass, drop, reject, and alert are supported. For additional information about stateful rule actions, see [Actions for stateful rules](rule-action.md#rule-action-stateful).
+ SCTP protocol.
+ `xbits` and `hostbits` with host or IP-level tracking (`track ip_src`, `track ip_dst`, or `track ip_pair`).
+ `tag:host`.
+ Thresholding.
+ IKEv2 protocol.
+ IP-in-IP protocol.
+ HTTP/2 overloading.
+ Application drop established (bidirectional) and Application drop established (server-directed only) default rules are incompatible with a session-holding configuration. You can read more at [Managing evaluation order for Suricata compatible rules in AWS Network Firewall.](https://docs.aws.amazon.com/network-firewall/latest/developerguide/suricata-rule-evaluation-order.html)

## Suricata features that Network Firewall supports with caveats
<a name="suricata-supported-with-caveats"></a>

The following Suricata features have caveats for use with Network Firewall:
+ If you want a rule group to use settings for `HOME_NET` and `EXTERNAL_NET` that are different from those that are set for the firewall policy, you must explicitly set both of these variables. 
  + In a firewall policy's variables, you can set a custom value for `HOME_NET`. The default `HOME_NET` setting is the CIDR of the inspection VPC. The policy's `EXTERNAL_NET` setting is always the negation of the policy's `HOME_NET` setting. For example, if the `HOME_NET` is `11.0.0.0`, the `EXTERNAL_NET` is set to `!11.0.0.0`.
  + In a rule group's variables, you can set custom values for both `HOME_NET` and `EXTERNAL_NET`. If you explicitly set rule group variables, those are used. Otherwise, rule group variables inherit their settings from the corresponding policy variables. 

    This means that, if you don't specify the rule group's `EXTERNAL_NET`, it inherits the setting from the policy's `EXTERNAL_NET` setting, regardless of the value of the rule group's `HOME_NET` setting. 

    For example, say you set the rule group's `HOME_NET` to `10.0.0.0`, and the firewall policy's `HOME_NET` to `11.0.0.0`. If you don't set the rule group's `EXTERNAL_NET`, then Network Firewall sets it to `!11.0.0.0`, based on the policy's `HOME_NET` setting. 
+ The AWS Network Firewall stateful inspection engine supports inspecting inner packets for tunneling protocols such as Generic Routing Encapsulation (GRE). If you want to block the tunneled traffic, you can write rules against the tunnel layer itself or against the inner packet. Due to the service inspecting the different layers, you might see flows and alerts for the packets within the tunnel.
+ To create a rule that requires a variable, you must specify the variable in the rule group. Without the required variables, the rule group isn't valid. For an example of a rule group that's configured with variables, see [Stateful rules examples: rule variables](suricata-examples.md#suricata-example-rule-with-variables).
+ In payload keywords, the `pcre` keyword is only allowed with `content`, `tls.sni`, `http.host`, and `dns.query` keywords.
+ The `priority` keyword is not supported for rule groups that evaluate rules using strict evaluation order.
+ When you use a stateful rule with a layer 3 or 4 protocol such as IP or TCP, and you don't include any flow state context, for example `"flow:not_established"`, then Suricata treats this rule as an IP-only rule. Suricata only evaluates IP-only rules for the first packet in each direction of the flow. For example, Suricata will process the following rule as an IP-only rule:

  ```
  pass tcp $HOME_NET any -> [10.0.0.0/8] $HTTPS_PORTS (sid: 44444; rev:2;)
  ```

  However, if the destination IP contains a `!`, then Suricata treats this as per the protocol specified in the rule. Suricata will process the following rule as a TCP rule.

  ```
  pass tcp $HOME_NET any -> [!10.0.0.0/16] $HTTPS_PORTS (sid: 44444; rev:2;)
  ```
+ To match HTTP/2 application traffic under a TLS inspection-enabled configuration, add http2 protocol rules to your rule set in addition to your existing HTTP rules. For example, if you used this rule to match HTTP traffic:

  ```
  drop http $HOME_NET any -> $EXTERNAL_NET any (msg:"example rule"; flow:to_server,established; http.host; content:"example.com"; sid:1; rev:1;)
  ```

  You should add an http2 application rule to your ruleset:

  ```
  drop http $HOME_NET any -> $EXTERNAL_NET any (msg:"example rule"; flow:to_server,established; http.host; content:"example.com"; sid:1; rev:1;)
  drop http2 $HOME_NET any -> $EXTERNAL_NET any (msg:"example rule"; flow:to_server,established; http.request_header; content:"authority|3a 20|example.com"; sid:2; rev:1;)
  ```