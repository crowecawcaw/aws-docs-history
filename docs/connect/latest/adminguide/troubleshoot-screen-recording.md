

# Troubleshoot agent screen recording issues
<a name="troubleshoot-screen-recording"></a>

## Troubleshoot screen recording failures caused by browser Local Network Access restrictions
<a name="troubleshoot-sr-lna"></a>

Modern browsers enforce Local Network Access (LNA) restrictions on WebSocket connections. This blocks the local WebSocket connection between the Contact Control Panel and the Connect Customer Client Application, causing screen recordings to fail. Affected recordings cannot be recovered. These restrictions apply to Chrome version 147 and later, Edge version 147 and later, and Firefox version 154 and later.

**Symptoms**
+ Screen recording does not start for agents using Chrome 147\+, Edge 147\+, or Firefox 154\+.
+ Screen recording works correctly on older browser versions or when using a browser that does not enforce LNA restrictions.
+ The shared worker logs show: `IPC connection terminated with status code 1006 (translated to failure code {{X}})`. The translated failure code indicates the cause:
  + Failure code `802` definitively indicates the connection was blocked by browser LNA restrictions. This failure code is currently available only on Chrome and Edge; on Firefox, LNA-blocked connections report failure code 1006.
  + Failure code `1006` indicates the cause could not be determined. This could be LNA restrictions or the Connect Customer Client Application not being installed or not running on the agent machine.
+ On Chrome and Edge, the shared worker or CCP logs show: `ERR_BLOCKED_BY_LOCAL_NETWORK_ACCESS_CHECKS`. Firefox does not emit this specific error string.

**Confirm the issue**

To confirm whether an agent is affected by this issue, temporarily disable the LNA check on a single impacted workstation:
+ **Chrome**: Navigate to `chrome://flags/#local-network-access-check` and set the flag to "Disabled", then restart Chrome.
+ **Edge**: Navigate to `edge://flags/#local-network-access-check` and set the flag to "Disabled", then restart Edge.
+ **Firefox**: Navigate to `about:config`, set `network.lna.websocket.enabled` to `false`, then restart Firefox.

If screen recording resumes after disabling the check, this confirms the issue is caused by LNA enforcement.

**Resolution**

Deploy the browser enterprise policy that pre-grants local network access for your Contact Control Panel domain, so agents are not blocked or prompted:
+ **Chrome and Edge**: Deploy the **LoopbackNetworkAllowedForUrls** policy. See [LoopbackNetworkAllowedForUrls](https://chromeenterprise.google/policies/#LoopbackNetworkAllowedForUrls) (Chrome) and [LoopbackNetworkAllowedForUrls](https://learn.microsoft.com/en-us/deployedge/microsoft-edge-browser-policies/loopbacknetworkallowedforurls) (Edge).
+ **Firefox**: Deploy the **LocalNetworkAccess** policy and add the loopback address `127.0.0.1` to **SkipDomains**. See [LocalNetworkAccess](https://firefox-admin-docs.mozilla.org/reference/policies/localnetworkaccess/).

For configuration examples and Windows registry commands, see [Browser enterprise policy for local network access](sr-system-req.md#browser-enterprise-policy).

For additional troubleshooting steps, including how to collect log files from the Connect Customer Client Application and shared worker, see [Download the Connect Customer Client Application log files for troubleshooting](troubleshoot-sr.md).

## Related information
<a name="troubleshoot-screen-recording-related"></a>

For help with rule-based redaction issues, see [Troubleshoot rule-based redaction](troubleshoot-sr.md#troubleshoot-rule-based-redaction).