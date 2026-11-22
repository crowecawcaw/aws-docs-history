

# How TLS inspection resets connections

To inspect a connection, Network Firewall terminates the SSL/TLS session from the client and establishes a new session to the server. This TLS proxy runs at the TLS layer, before and around the stateful rules engine. When the proxy can't establish or validate a session, it resets the connection at the TLS layer, independently of your firewall rules, your IPS rules, and the firewall default action.

**Important**  
These resets happen with both a Classic and a Next Generation policy, and in both enforce mode and monitor mode. Because the TLS proxy performs them—not the rules engine—monitor mode doesn't prevent them. For how these resets appear and behave in monitor mode, see [TLS inspection in monitor mode](tls-inspection-policy-v2-monitor-mode.md).

The only explanation for these resets is in the `tls_error.error_message` field of the TLS log. The alert log doesn't record the reason. Turn on TLS logging to see these messages. For the log format and example entries, see [Logging for TLS inspection in AWS Network Firewall](tls-inspection-logging.md).

Where a reset falls in relation to the rules engine determines whether it can appear in the alert log at all:
+ Network Firewall checks the *syntax* of the server name indication (SNI) before the rules engine evaluates the connection. A connection that fails this check—the first two conditions that follow—is reset before any rule or the firewall default action sees it, so it produces no alert log entry.
+ Network Firewall validates the server's certificate and completes the server-side handshake after the firewall's TLS gate has admitted the flow. A reset from these later conditions—the last two that follow—happens after the rules engine has already evaluated the connection.

**The client hello has no server name**  
When the client hello in the TLS handshake carries no SNI, or an empty SNI, Network Firewall can't determine the destination server name and resets the connection. The TLS log message is `Server name is not found in client hello.` Traffic that uses the TLS 1.3 Encrypted SNI or Encrypted Client Hello extensions is reset for this reason, because the server name isn't visible to the firewall.

**The server name is present but not valid**  
When the client hello includes an SNI that isn't a valid hostname, Network Firewall resets the connection. The TLS log message is `Server name {{sni}} in client hello is NOT valid.`

To be valid, a server name must be 3 to 255 characters long and formed as a hostname of dot-separated labels, where each label uses only letters, digits, and hyphens. Network Firewall resets the connection for a server name that:
+ Ends in a trailing dot, such as `example.com.`
+ Is a single label with no dot, such as `localhost`
+ Contains an underscore
+ Contains a wildcard character (`*`)
+ Contains non-ASCII or Unicode characters. Use the Punycode form of an internationalized domain name instead.

**The server name doesn't match the server's certificate**  
Network Firewall resets the connection when the SNI doesn't match the names in the server's certificate—its subject alternative names (SAN) or common name (CN)—including when the SNI is a subdomain that the certificate doesn't cover. The TLS log message is `SNI: {{sni}} Match Failed to server certificate names: {{names}}`, where {{names}} lists the names that the certificate does cover. A well-formed, real-looking server name is still reset when the certificate that the server presents doesn't cover it.

**The handshake to the server or client fails**  
Network Firewall resets the connection when the TLS handshake to the server—or to the client—fails. The TLS log message is `Error in connection to Server: {{reason}}.` or `Error in connection to Client: {{reason}}.`, where {{reason}} is one of the following:
+ `Certificate verification failed`
+ `Certificate is expired`
+ `Bad certificate`
+ `TLS certificate has unknown ca`
+ `Wrong version number`
+ `No supported application protocol`
+ `Invalid ALPN protocol`

**Note**  
Some handshake failures are reset without any customer TLS log record. For example, a TLS version or cipher mismatch that surfaces as a handshake-failure alert, or a server that presents no certificate, resets the connection but doesn't produce a TLS log entry. When a connection is reset and no TLS log entry explains it, a handshake incompatibility of this kind is a likely cause.

Certificate revocation checking can also close or reset an outbound connection, independently of your rules and in monitor mode. That cause is recorded in the `revocation_check` field of the TLS log rather than in `tls_error.error_message`. For more information, see [Checking certificate revocation status](tls-inspection-certificate-requirements.md#tls-inspection-check-certificate-revocation-status).