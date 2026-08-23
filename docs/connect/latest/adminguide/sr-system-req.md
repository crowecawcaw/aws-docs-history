# System and network requirements for screen recording in Connect Customer

This topic provides the system requirements for using screen recording, and describes
the detailed dataflow it uses in each platform.

## System requirements

Here are the minimum system requirements for agent devices to perform screen
recording. You'll need to scope additional memory, bandwidth, and CPU for the
operating system and anything else running on the device to avoid resource
contention.

- CPU: 2.0 GHz (4 cores or 4 vCPU recommended)
- Memory: 4 GB
- Network: 600 Kbps

### Supported operating systems

- 64-bit Windows 10 and 11 based on the x86-64 architecture
- Chrome OS version 140 or higher enrolled in a Google Enterprise
  Domain

###### Note

When Windows multi-session configuration is enabled allowing multiple agents
to use a single Windows host, make sure that the agent's workstation has the
recommended resource availability for each concurrent session.

## Network requirements

### URLs to add to your firewall allow list

To ensure smooth screen recording functionality, add the following URL
patterns to your allow list.

#### Client App authentication

`https://your-connect-instance-alias.my.connect.aws/taps/client/auth`

#### Screen recording upload (from CCP)

We recommend the wildcard
`connect-recording-staging-*.s3.dualstack.your-region-name.amazonaws.com`

If you prefer not to use wildcards, the full list of endpoints is available
at [https://screenrecording.connect.aws/config/connect-recording-endpoint-allowlist.json](https://screenrecording.connect.aws/config/connect-recording-endpoint-allowlist.json "https://screenrecording.connect.aws/config/connect-recording-endpoint-allowlist.json")

This list might be updated in the future. Refer to the
`createDate` field at the top of the file to check for
updates.

#### Browser extension updates (required for rule-based redaction)

If you use [rule-based redaction](rule-based-redaction-screen-recording.md "rule-based-redaction-screen-recording.md"), the agent's browser must be able to
download and update the Connect Customer browser extension. Allow outbound HTTPS to the
following.

We recommend the wildcard
`https://screenrecording.connect.aws/*`, which covers all
current and future extension paths for both browsers.

If you prefer not to use wildcards, allow these specific URLs:

| Browser                          | URL                                                                                                           |
| -------------------------------- | ------------------------------------------------------------------------------------------------------------- |
| Google Chrome and Microsoft Edge | `https://screenrecording.connect.aws/chromeos/amazon-connect-extension/releases/updates.xml`                  |
| Google Chrome and Microsoft Edge | `https://screenrecording.connect.aws/chromeos/amazon-connect-extension/releases/amazon-connect-extension.crx` |
| Mozilla Firefox                  | `https://screenrecording.connect.aws/firefox/amazon-connect-extension/releases/updates.json`                  |
| Mozilla Firefox                  | `https://screenrecording.connect.aws/firefox/amazon-connect-extension/releases/amazon-connect-extension.xpi`  |

For extension identifiers and deployment instructions, see [Deploy the browser
extension](deploy-browser-extension.md "deploy-browser-extension.md").

### Port used for screen recording

The Connect Customer Client Application communicates with the CCP through a local websocket on port 5431
(on Windows) and 35431 (on Chrome OS).

### Sequence diagram

The following sequence diagram shows the network calls between different
components involved in screen recording.

![A sequence diagram shows the network calls between different components involved in screen recording.](images/sequence-diagram.png)

- In Windows, the Connect Customer Client is the combination of the
  Amazon.Connect.Client.Service background process and
  Amazon.Connect.Client.RecordingSession.
- In ChromeOS, the Connect Customer Client is the combination of Isolated Web App
  and Browser extension.

## Browser enterprise policy for local network access

Modern browsers enforce Local Network Access (LNA) restrictions on
WebSocket connections. These restrictions block the local WebSocket
connection between the Contact Control Panel and the Connect Customer Client Application, causing
screen recordings to fail.

For screen recording to work, you must deploy the appropriate browser
enterprise policy to your agents' workstations for each browser they use.
The policy pre-grants the minimal network access for the Contact Control
Panel, so agents are neither blocked nor prompted. Configure the policy
to allow the Contact Control Panel to reach the Connect Customer Client Application over the local
connection; the policy name, the value to configure, and the configuration
examples differ by browser – see the following sections.

### Google Chrome and Microsoft Edge

Starting with Google Chrome version 147 and Microsoft Edge version
147, Chromium-based browsers enforce LNA restrictions on WebSocket
connections.

Deploy the **LoopbackNetworkAllowedForUrls**
enterprise policy. Example policy value:
`[*.]my.connect.aws`

- For Google Chrome, see [LoopbackNetworkAllowedForUrls](https://chromeenterprise.google/policies/#LoopbackNetworkAllowedForUrls "https://chromeenterprise.google/policies/#LoopbackNetworkAllowedForUrls") in the Chrome enterprise
  policy documentation.
- For Microsoft Edge, see [LoopbackNetworkAllowedForUrls](https://learn.microsoft.com/en-us/deployedge/microsoft-edge-browser-policies/loopbacknetworkallowedforurls "https://learn.microsoft.com/en-us/deployedge/microsoft-edge-browser-policies/loopbacknetworkallowedforurls") in the Edge enterprise
  policy documentation.

The following example commands set the registry policy for the domain
`[*.]my.connect.aws` on Windows:

```
reg add "HKLM\SOFTWARE\Policies\Google\Chrome\LoopbackNetworkAllowedForUrls" /v 1 /t REG_SZ /d "[*.]my.connect.aws"
reg add "HKLM\SOFTWARE\Policies\Microsoft\Edge\LoopbackNetworkAllowedForUrls" /v 1 /t REG_SZ /d "[*.]my.connect.aws"
```

For more details on this browser change, see [New permission
prompt for Local Network Access](https://developer.chrome.com/blog/local-network-access "https://developer.chrome.com/blog/local-network-access") in the Chrome developer
documentation.

### Mozilla Firefox

Starting with Mozilla Firefox version 154, Firefox
enforces LNA restrictions on WebSocket connections.

Deploy the **LocalNetworkAccess**
enterprise policy and add the loopback address `127.0.0.1`
to the **SkipDomains** list. On Firefox,
list the loopback address that the Connect Customer Client Application listens on, rather than your
Contact Control Panel domain.

###### Note

This policy permits local network access to the loopback address
from any site, not only from your Contact Control Panel. It is
currently the most restrictive policy that allows screen recording
to work on Firefox; a more narrowly scoped policy that limits the
exemption to your Contact Control Panel is pending a future Firefox
update.

Example `policies.json` configuration:

```
{
  "policies": {
    "LocalNetworkAccess": {
      "Enabled": true,
      "SkipDomains": ["127.0.0.1"],
      "Locked": true
    }
  }
}
```

The following example command sets the equivalent policy through the
Windows registry (GPO):

```
reg add "HKLM\SOFTWARE\Policies\Mozilla\Firefox\LocalNetworkAccess\SkipDomains" /v 1 /t REG_SZ /d "127.0.0.1"
```

For details, see [LocalNetworkAccess](https://firefox-admin-docs.mozilla.org/reference/policies/localnetworkaccess/ "https://firefox-admin-docs.mozilla.org/reference/policies/localnetworkaccess/") in the Firefox enterprise policy
documentation.

## Requirements for rule-based redaction

If you use [Rule-based redaction
for screen recordings](rule-based-redaction-screen-recording.md "rule-based-redaction-screen-recording.md"), agent workstations
must meet the following additional requirements.

- **Browser** – One of the
  following:

  - Google Chrome 120 or later
  - Microsoft Edge 120 or later
  - Mozilla Firefox 120 or later
    Browsers other than Chrome, Edge, and Firefox do not report URLs to the
    Connect Customer Client Application, so URL rules cannot match pages in those browsers. You can still
    match windows in those browsers by using window title rules based on the
    browser's window title.

- **Connect Customer Client Application** – Version 3.0.2 or later.
  See [Connect Customer Client Application](amazon-connect-client-app.md "amazon-connect-client-app.md").
- **Connect Customer browser extension** – Version
  2.1.0 or later. The extension must be installed and enabled on every browser
  that agents use during recorded contacts. See [Deploy the browser
  extension](deploy-browser-extension.md "deploy-browser-extension.md").
- **Local network access policy**
  – If agents use Chrome version 147 or later, Edge version 147
  or later, or Firefox version 154 or later, deploy the browser
  enterprise policy to allow local network access from the Connect Customer CCP
  origin to 127.0.0.1:5431. For details, see
  [Browser enterprise policy for local network access](#browser-enterprise-policy "#browser-enterprise-policy").

Display scaling from 100% through 200% is supported on single-monitor and
multi-monitor workstations.
