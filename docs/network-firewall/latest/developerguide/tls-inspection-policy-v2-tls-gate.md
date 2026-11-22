

# How rules are evaluated for TLS-inspected traffic

With TLS inspection, Network Firewall decrypts a connection, inspects the requests inside it, and re-encrypts the traffic before sending it on. Because the firewall can see more of each connection, it also checks more of it: an inspected connection must be allowed at every stage it passes through, not only once.

Network Firewall evaluates an inspected connection at three stages, in order. A connection reaches a stage only if it was allowed at the stage before it.


| Stage | What the firewall evaluates | The question your rules answer | 
| --- | --- | --- | 
| 1. Connection | The TCP connection: addresses, ports, and protocol. | Can this client open this connection? | 
| 2. TLS handshake | The server name indication (SNI) that the client requests, such as example.com, before any traffic is decrypted. | Is this website allowed? | 
| 3. Decrypted request | The HTTP request inside the connection—the Host header, URL, method, and headers—over HTTP/1.1 or HTTP/2. | Is this request, to this host, allowed? | 

A rule at an earlier stage never decides a later stage for an inspected connection. For example, an `accept:flow` rule at the connection stage (such as `accept:flow tcp:all`) only gets the connection past stage 1—Network Firewall still evaluates the SNI at stage 2 and the decrypted request at stage 3. This is deliberate: otherwise a single rule that accepted a connection at the network layer would turn off inspection for everything on that port. In the same way, allowing the website name at stage 2 doesn't allow the requests inside the connection at stage 3.

Where none of your rules allow the traffic at a stage, the policy's firewall default action decides what happens there:
+ **Drop** or **Reject** – The connection is blocked at the first stage that has no matching allow rule. To allow a connection the whole way through, author an allow rule at every stage.
+ **Accept** – Traffic is allowed at any stage your rules don't cover. You author rules only for the traffic you want to block.
+ **Alert** – The same as **Accept**, and Network Firewall records an alert log entry each time the default action is applied.

In monitor mode, the policy doesn't block traffic: rules and the default action that would block instead record what they would have done, so you can test a rule set before you enforce it. The stream exception policy also doesn't block in monitor mode (it uses Continue). The exceptions are the TLS-layer resets that the TLS proxy performs independently of the rules engine: a missing or invalid SNI, an SNI that doesn't match the server's certificate, and failed handshakes still reset the connection regardless of policy mode. Certificate revocation checking is also still enforced: if its action for a revoked or unknown-status certificate is Drop or Reject, those connections are still blocked, even in monitor mode. For more information, see [Policy mode: enforce and monitor](firewall-policy-v2-policy-mode.md), [How TLS inspection resets connections](tls-inspection-connection-resets.md), and [TLS inspection in monitor mode](tls-inspection-policy-v2-monitor-mode.md).

Network Firewall closes a blocked connection rather than returning an HTTP error such as `403`. Traffic that the firewall default action blocks appears in your alert logs, tagged with the hook where it was blocked. Traffic that one of your own rules blocks is logged only when that rule turns on alert logging.