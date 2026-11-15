

# Stream exception policy for Next Generation policies
<a name="stream-exception-policy-v2"></a>

A Next Generation policy supports only the **Drop** and **Reject** stream exception policy options; **Reject** is both the default and the recommended value. It doesn't support **Continue** as a configurable value.

**Reject** is recommended so that a client receives a TCP reset and can immediately establish a new connection, instead of a silent timeout.

In monitor mode, Network Firewall doesn't apply your stream exception policy—it uses **Continue** so that mid-stream connections aren't dropped or rejected. Your configured **Drop** or **Reject** value is saved and applies again when you switch the policy to enforce mode. For more information about monitor mode, see [Policy mode: enforce and monitor](firewall-policy-v2-policy-mode.md).