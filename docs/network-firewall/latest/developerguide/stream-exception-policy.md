

# Stream exception policy options in your AWS Network Firewall firewall policy

The firewall policy's stream exception policy setting determines how Network Firewall handles traffic when a network connection breaks midstream. Network connections can break due to disruptions in external networks or within the firewall itself. A stream exception policy presents the following options:
+ **Drop** – Network Firewall fails closed and drops all subsequent traffic going to the firewall. If you create a firewall policy with the API or AWS CLI and don't specify a stream exception policy, Network Firewall uses **Drop**.
+ **Reject** – Network Firewall fails closed and drops all subsequent traffic going to the firewall. Network Firewall also sends a TCP reject packet back to your client so that the client can immediately establish a new session. Network Firewall has context about the new session and applies rules to the subsequent traffic.
+ **Continue** – Network Firewall continues to apply rules to the subsequent traffic without context from traffic before the break. This impacts the behavior of rules that depend on this context. For example, if you have a stateful rule to drop HTTP traffic, Network Firewall won't match the traffic for this rule because the service won't have the context from session initialization defining the application layer protocol as HTTP. However, this behavior is rule dependent—a TCP-layer rule using a `flow:stateless` rule would still match, as would the `aws:drop_strict` default action.
**Note**  
The **Continue** option is available only for Classic Network Firewall policies. Next Generation policies support only **Drop** and **Reject**. For information about the policy types, see [AWS Network Firewall firewall policy versions](firewall-policy-versions.md).

**Note**  
When you create a firewall policy in the console, the console pre-selects **Reject**.