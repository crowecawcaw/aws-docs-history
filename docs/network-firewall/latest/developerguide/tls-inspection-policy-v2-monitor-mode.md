

# TLS inspection in monitor mode
<a name="tls-inspection-policy-v2-monitor-mode"></a>

Monitor mode changes only how the firewall rules, the IPS rules, and the firewall default action are *enforced*. In monitor mode, none of them drop or reject traffic—each records what it would have done instead. Monitor mode doesn't change the TLS proxy. For how monitor mode affects the engines, see [Policy mode: enforce and monitor](firewall-policy-v2-policy-mode.md).

As a result, a connection can be reset in monitor mode even though monitor mode doesn't block traffic. The reset comes from the TLS layer, not the rules engine:
+ Every TLS-layer reset in [How TLS inspection resets connections](tls-inspection-connection-resets.md)—a missing or invalid SNI, a server name that doesn't match the certificate, or a failed handshake—still resets the connection in monitor mode.
+ Certificate revocation checking still closes a connection when its action is **Drop**, and still resets a connection when its action is **Reject**, in monitor mode. For more information, see [Checking certificate revocation status](tls-inspection-certificate-requirements.md#tls-inspection-check-certificate-revocation-status).

**What your logs show**  
Monitor mode changes what a reset looks like in your logs, depending on where the reset happens relative to the rules engine:
+ **A reset from SNI syntax**—a missing or invalid server name—happens before the rules engine evaluates the connection, so there's no alert log entry for it in any mode. The TLS log is the only evidence.
+ **A reset after the TLS gate admits the flow**—a certificate-name mismatch, a handshake failure, or a revocation action—happens after the rules engine has evaluated the connection. In monitor mode, the alert log shows the default accept trail (`accept:hook,alert`) with the offending server name, which makes the connection look accepted even though the TLS proxy then reset it. Always consult the TLS log for the real reason.

**Note**  
When traffic is unexpectedly reset under TLS inspection, check the TLS log first. The `tls_error.error_message` field or the `revocation_check` field carries the reason. The alert log might not show it, and in monitor mode the alert log can misleadingly show the connection as accepted. For the TLS log format, see [Logging for TLS inspection in AWS Network Firewall](tls-inspection-logging.md).