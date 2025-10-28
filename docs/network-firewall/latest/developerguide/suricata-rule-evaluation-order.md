# Managing evaluation order for Suricata compatible rules in AWS Network Firewall

You can configure and manage the evaluation order of the rules in your Suricata compatible stateful rule groups.

All of your stateful rule groups are provided to the rule engine as
Suricata compatible strings. Suricata can evaluate stateful rule groups
by using the default rule group ordering method, or you can set an
exact order using the _strict_ ordering method. We recommend that you use strict order because it lets you specify the exact order that you'd like the stateful engine to evaluation your rules. The settings for your
rule groups must match the settings for the firewall policy that they belong to.

## Action order

If your firewall policy is set up to use action order rule group ordering, the action order by which
Suricata evaluates stateful rules is determined by the following settings, listed in order of precedence:

1. The Suricata `action` specification. This takes highest precedence.

Actions are processed in the following order:

    1. `pass`
    2. `drop`
    3. `reject`
    4. `alert`

###### Note

If a packet within a flow matches a rule containing `pass` action, then Suricata doesn't scan the other packets in that flow and it passes the unscanned packets.

For more information about the action specification, see
[Suricata.yaml: Action-order](https://docs.suricata.io/en/suricata-7.0.8/configuration/suricata-yaml.html?highlight=action+order#action-order "https://docs.suricata.io/en/suricata-7.0.8/configuration/suricata-yaml.html?highlight=action+order#action-order")
in the [Suricata User Guide](https://docs.suricata.io/en/suricata-7.0.8/index.html "https://docs.suricata.io/en/suricata-7.0.8/index.html"). 2. The Suricata `priority` keyword. Within a specific action group, you can use the priority
setting to indicate the processing order. By default, Suricata processes from the lowest
numbered priority setting on up. The `priority` keyword has a mandatory
numeric value ranging from 1 to 65535. Note that the `priority` keyword is only valid using
the default action order.

For more information about priority, see
[Suricata.yaml: Action-order](https://docs.suricata.io/en/suricata-7.0.8/rules/meta.html?highlight=priority#priority "https://docs.suricata.io/en/suricata-7.0.8/rules/meta.html?highlight=priority#priority")
in the [Suricata User Guide](https://docs.suricata.io/en/suricata-7.0.8/index.html "https://docs.suricata.io/en/suricata-7.0.8/index.html").

For example, Suricata evaluates all `pass` rules before
evaluating any `drop`, `reject`, or `alert` rules by default,
regardless of the value of priority settings. Within all `pass` rules, if priority keywords are present,
Suricata orders the processing according to them.

The protocol layer does not impact the rule evaluation order by default. If you
want to avoid matching against lower-level protocol packets before
higher-level application protocols can be identified, consider using
the `flow` keyword in your rules. This is needed because,
for example, a TCP rule might match on the first packet of a TCP
handshake before the stateful engine can identify the application
protocol. For information about the `flow` keyword, see
[Flow Keywords](https://docs.suricata.io/en/suricata-7.0.8/rules/flow-keywords.html "https://docs.suricata.io/en/suricata-7.0.8/rules/flow-keywords.html").

For examples of default rule order management, see [Stateful rules examples: manage rule evaluation order](suricata-examples.md#suricata-example-rule-ordering "suricata-examples.md#suricata-example-rule-ordering").

For additional information about evaluation order for stateful rules, see the following topics in the [Suricata User Guide](https://docs.suricata.io/en/suricata-7.0.8/ "https://docs.suricata.io/en/suricata-7.0.8/"):

- [Suricata.yaml: Action-order](https://docs.suricata.io/en/suricata-7.0.8/configuration/suricata-yaml.html?highlight=action%20order#action-order "https://docs.suricata.io/en/suricata-7.0.8/configuration/suricata-yaml.html?highlight=action%20order#action-order")
- [Meta Keywords: priority](https://docs.suricata.io/en/suricata-7.0.8/rules/meta.html?highlight=priority#priority "https://docs.suricata.io/en/suricata-7.0.8/rules/meta.html?highlight=priority#priority")

## Strict evaluation order

If your firewall policy is set up to use strict ordering,
Network Firewall allows you the option to manually set a
_strict_ rule group order. With
strict ordering, the rule groups are evaluated by order of
priority, starting from the lowest number, and the rules in
each rule group are processed in the order in which they're
defined.

When configuring these actions, consider the following caveats:

1. For drop actions, you can choose either none or only one drop action.
2. For alert actions, you can choose none, one alert action, or **Alert all** plus any of the other two alert actions.
3. Some combinations of actions are invalid. If either **Drop established** or **Alert established** is selected, you cannot select **Application Layer drop established** or **Application Layer alert established**, and vice versa.
4. When you choose **Strict** for your rule order, you can choose one or more **Default actions**.
   Note that this does not refer to default action rule ordering, but rather, to the default actions that Network Firewall takes
   when following your strict, or exact, rule ordering.

The default actions are as follows:

If you have rules that match application layer data, such as those that evaluate HTTP headers, a default drop action might trigger earlier than you want. This can happen when the data that your rules match against spans multiple packets, because a default drop action can apply to a single packet. For this case, don't choose any default drop action and instead use drop rules that are specific to the application layer.

_Choose none or one. You can't choose more than one._

- **Drop all** – Drops all packets.
- **Drop established** – Drops only the packets that are in established connections from client to server.
  This allows the layer 3 and 4 connection establishment packets that are needed for the upper-layer connections to be established,
  while dropping the packets for connections that are already established. This allows application-layer _pass_
  rules to be written in a default-deny setup without the need to write additional rules to allow the lower-layer
  handshaking parts of the underlying protocols. Packets from established connections from the server to the client are passed to allow return traffic from established connections back to the client.

Choose this option when using strict order for your own domain list rule groups because Network Firewall requires an established connection in order to evaluate whether to pass or drop the packets for domain lists.

For other protocols, such as UDP, Network Firewall considers the connection established only after seeing traffic from both sides of the connection. For connectionless protocols, such as UDP and ICMP, the `drop` established action drops all packets. You must write specific rules to allow these packets as needed.

- **Application Layer drop established** – Drops server-initiated banner packets and packets in established connections.
  It also provides enhanced support for segmented application layer traffic through the following behaviors:
  - Allows segmented TLS client hello packets until a `TLS.SNI` field is detected, then applies rules based on SNI.
  - Allows segmented HTTPS request packets until the `HTTP.HOST` field is detected, then applies rules based on host

###### About the application layer drop established action

When you select the application layer drop established option, the firewall drops connections that have banner packets.
After a connection is established, if the firewall sees a packet that no explicit pass rule allows,
the firewall drops that packet and all subsequent packets in the connection. This behavior affects TCP flow control packets that occur after the TCP handshake
but before a pass rule applies.

Examples of TCP flow control packets that can result in such drops include:

- TCP window updates from either client or server, if seen immediately after the TCP handshake.
- TCP keep-alives from either client or server, if seen immediately after the TCP handshake.
- TCP resets from either client or server, if seen immediately after the TCP handshake.
  To allow these packets in your environment you can add custom pass rules in a stateful rule group, for example:

To allow TCP window packets:

```
pass tcp any any -> any any (msg:"Allow all TCP Window Updates from server to client"; tcp.flags:A; dsize:0; window:!0; flow:established, to_client; sid:1000001;)
pass tcp any any -> any any (msg:"Allow all TCP Window Updates from client to server"; tcp.flags:A; dsize:0; window:!0; flow:established, to_server; sid:1000002;)
```

To allow TCP keep-alives (will pass all ACKs):

```
pass tcp any any -> any any (msg:"Allow TCP keep alives - all acks - from server to client"; tcp.flags:A; dsize:0; flow:established, to_client; sid:1000003;)
pass tcp any any -> any any (msg:"Allow TCP keep alives - all acks - from client to server"; tcp.flags:A; dsize:0; flow:established, to_server; sid:1000004;)
```

To allow TCP resets:

```
pass tcp any any -> any any (msg:"Allow TCP resets from server to client"; tcp.flags:+R; dsize:0; flow:established, to_client; sid:1000005;)
pass tcp any any -> any any (msg:"Allow TCP resets from client to server"; tcp.flags:+R; dsize:0; flow:established, to_server; sid:1000006;)
```

_Choose none, one, or all._

- **Alert all** - Logs an `ALERT` message on all packets. This does not drop packets, but alerts you
  to what would be dropped if you were to choose **Drop all**.
- **Alert established** - Logs an `ALERT` message on only the packets that are in established
  connections. This does not drop packets, but alerts you to what would be dropped if you were to choose
  **Drop established**.
- **Application Layer alert established** – Logs an `ALERT` message on only the packets that are in
  established connections, with enhanced support for segmented application layer traffic.

###### Tip

You can use these logged messages to better understand the impact that the Application Layer Drop Established action has on firewall behavior.
For more information about logging network traffic, see [Logging network traffic from AWS Network Firewall](firewall-logging.md "firewall-logging.md").
