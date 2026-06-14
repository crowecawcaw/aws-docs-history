# Troubleshoot agent screen recording issues

## Troubleshoot screen recording failures on Chrome 147 or Edge 147 and later

Starting with Chrome version 147 and Edge version 147, Chromium-based
browsers enforce Local Network Access (LNA) restrictions on WebSocket
connections. This blocks the local WebSocket connection between the Contact
Control Panel and the Connect Customer Client Application, causing screen recordings to fail. Affected
recordings cannot be recovered.

**Symptoms**

- Screen recording does not start for agents using Chrome 147+
  or Edge 147+.
- Screen recording works correctly on older browser versions or
  when using a browser that does not enforce LNA
  restrictions.
- The shared worker logs show:
  `IPC connection terminated with status code
1006`

  - Note: this could also mean the Connect Customer Client Application is not
    installed or not running on the agent machine.

- The shared worker or CCP logs show:
  `ERR_BLOCKED_BY_LOCAL_NETWORK_ACCESS_CHECKS`

**Confirm the issue**

To confirm whether an agent is affected by this issue, temporarily
disable the LNA check on a single impacted workstation:

- **Chrome**: Navigate to
  `chrome://flags/#local-network-access-check`
  and set the flag to "Disabled", then restart Chrome.
- **Edge**: Navigate to
  `edge://flags/#local-network-access-check`
  and set the flag to "Disabled", then restart Edge.

If screen recording resumes after disabling the flag, this confirms
the issue is caused by LNA enforcement.

**Resolution**

Deploy the **LoopbackNetworkAllowedForUrls**
enterprise policy to pre-grant loopback network access permission for your
Contact Control Panel domain. Configure this policy with your Connect Customer
Contact Control Panel URL. Example policy value:
`[*.]my.connect.aws`

- For Google Chrome, see [LoopbackNetworkAllowedForUrls](https://chromeenterprise.google/policies/#LoopbackNetworkAllowedForUrls "https://chromeenterprise.google/policies/#LoopbackNetworkAllowedForUrls") in the Chrome
  enterprise policy documentation.
- For Microsoft Edge, see [LoopbackNetworkAllowedForUrls](https://learn.microsoft.com/en-us/deployedge/microsoft-edge-browser-policies/loopbacknetworkallowedforurls "https://learn.microsoft.com/en-us/deployedge/microsoft-edge-browser-policies/loopbacknetworkallowedforurls") in the Edge
  enterprise policy documentation.

For additional troubleshooting steps, including how to collect log files
from the Connect Customer Client Application and shared worker, see
[Download the Connect Customer Client Application log
files for troubleshooting](troubleshoot-sr.md "troubleshoot-sr.md").
