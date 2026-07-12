# Troubleshoot audio quality issues in Connect Customer

Audio quality issues—choppy or robotic audio, echo, delay, one-way audio, humming, or
dead air—can originate anywhere along the call path. This page is the starting point for
diagnosing them. It helps you narrow down _where_ in the path the problem
occurs, then directs you to the specialized topic that resolves it.

###### Call disconnects

This page covers audio _quality_. If calls are dropping or
disconnecting rather than sounding bad, see [Troubleshoot call disconnects by using DisconnectDetails in the contact record](troubleshoot-call-disconnects.md "troubleshoot-call-disconnects.md").

###### Intended audience

This guide assumes you are an IT administrator with experience investigating network,
telephony, and workstation issues, and that you can access data in a Connect Customer contact
record.

## Before you begin: gather this information

Collect the following for the affected calls before you start. You need it to
investigate and, if necessary, to open a case with AWS Support.

- **Description of the symptom**—what the audio
  sounds like (choppy, robotic, echo, one-way, humming, dead air, delay) and whose
  voice is affected. You use this in Step 1.
- **Instance Amazon Resource Name (ARN)**—see [Find your Connect Customer instance ID or ARN](find-instance-arn.md "find-instance-arn.md").
- **ContactId** of each affected call (provide 3–5
  examples, none older than 24 hours).
- **Time of occurrence**, including time zone
  (record in Coordinated Universal Time (UTC) where possible).
- **Call recording** for each example.

If you can't obtain a recording directly, ask the agent or customer to review one and
confirm:

- Whose audio is degraded—the **agent** or the
  **end-customer**.
- Whether the reported degradation is **actually
  audible** in the recording.

###### Prerequisites

Before troubleshooting, make sure of the basics: the agent workstation meets the [minimum hardware requirements](ccp-agent-hardware.md "ccp-agent-hardware.md") and the agent
uses a [supported browser](connect-supported-browsers.md "connect-supported-browsers.md").

## Step 1: Identify the symptom

Use the symptom to jump to the most likely cause. If your symptom isn't listed, or
you're not sure, continue to Step 2.

| Symptom                                                                                                                   | Most likely area                                                    | Where to go                                                                                                                                                                                                                                                                                                               |
| ------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| No audio ("dead air") on the **first call after a<br>Windows 11 reboot**                                                  | Workstation (network interface card/services)                       | [CCP audio issues on first call after system reboot when using Windows 11](common-ccp-issues.md#ccp-windows-11-audio-issues-after-reboot "common-ccp-issues.md#ccp-windows-11-audio-issues-after-reboot")                                                                                                                 |
| No audio in *_both directions_<br>• (neither<br>party can hear the other), not after a reboot                             | Contact Control Panel (CCP) setup, microphone access, or ports      | [Contact Control Panel (CCP) Issues](common-ccp-issues.md "common-ccp-issues.md"), [How do I troubleshoot stopped audio during calls in my Amazon<br>Connect CCP? (AWS re:Post)](https://repost.aws/knowledge-center/connect-call-audio-not-working "https://repost.aws/knowledge-center/connect-call-audio-not-working") |
| One party can't hear the other (one-way audio)                                                                            | Exclusive mic/speaker control, or network address translation (NAT) | [One-way audio from customers](common-ccp-issues.md#ccp-oneway-issues "common-ccp-issues.md#ccp-oneway-issues"), [Troubleshoot your network for call quality and disconnect problems](network-ts.md "network-ts.md")                                                                                                      |
| Persistent *_humming_<br>• in the agent's<br>audio                                                                        | Headset/browser sample-rate mismatch                                | [Humming sound in the agent's audio device: Verify the headset and browser sample rates](verify-sample-rate.md "verify-sample-rate.md")                                                                                                                                                                                   |
| Missed calls / "Microphone is not accessible" / "Initialization<br>Failed" / Web Real-Time Communication (WebRTC) timeout | CCP setup, permissions, or ports                                    | [Contact Control Panel (CCP) Issues](common-ccp-issues.md "common-ccp-issues.md")                                                                                                                                                                                                                                         |
| Echo (agent hears their own voice)                                                                                        | Mic/speaker feedback                                                | [Troubleshoot an agent's workstation for call quality and disconnect problems](agent-ts.md "agent-ts.md")                                                                                                                                                                                                                 |
| Choppy/broken, delayed, or distorted/robotic audio                                                                        | Network or workstation                                              | Continue to Step 2                                                                                                                                                                                                                                                                                                        |

## Step 2: Determine the scope

The number of affected agents changes where you look first.

- **A single agent**—focus on that agent's
  **workstation** (Step 5, workstation path) and
  headset.
- **Multiple agents in the same location or
  hierarchy**—suspect a **local
  network** issue (router, internet service provider (ISP), or local area network (LAN)) or a software or OS update pushed to
  those machines.
- **Agents across multiple locations (remote and
  in-office)**—suspect an **organization-level** network change or a browser/OS
  auto-update.

Use [AgentHierarchyGroups](ctr-data-model.md#ctr-AgentHierarchyGroups "ctr-data-model.md#ctr-AgentHierarchyGroups") and [DeviceInfo](ctr-data-model.md#ctr-deviceinfo "ctr-data-model.md#ctr-deviceinfo")
from the contact record to identify the impacted population. For more information about impact
analysis, see [Troubleshoot audio quality issues by using QualityMetrics in the contact record](sop-audio-qa.md "sop-audio-qa.md").

###### Tip

If the issue started on a specific date for all affected agents, check for network
infrastructure changes, browser auto-updates, or OS patches pushed on that
date.

## Step 3: Localize the problem using the call path

When agents use the Contact Control Panel (CCP), calls traverse this path:

**(1) Headset → (2) Agent device/CCP → (3) Agent network → (4)
Connect Customer → (5) Telephony network → (6) End-customer device**

Connect Customer records each call at point (4), so the recording captures the audio exactly as
it arrived at Connect Customer. The recording is a dividing line. If the degradation **is audible** in the recording, the audio had already degraded
**before** it reached Connect Customer (paths 1–3). If the
recording **sounds clean** but a participant reported bad
audio, the degradation occurred **after** point 4, on the
path to the listener.

Use the following table to pair what you observe with the conclusion and where to go
next.

| Whose audio is degraded                                               | Degradation *_is_<br>• in the<br>recording                                                                                                        | Degradation is *_not_<br>• in the<br>recording                                                                                             |
| --------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------ |
| *_Agent_<br>• (the agent's voice, as heard<br>by the customer)        | The audio degraded before reaching Connect Customer—headset, device, or<br>agent network (1, 2, and 3). Go to Step 4.                             | Audio reached Connect Customer cleanly but customer heard degradation —<br>telephony network or end-customer side (5 and 6). Go to Step 6. |
| *_End-customer_<br>• (the customer's voice,<br>as heard by the agent) | The audio degraded before reaching Connect Customer on the inbound side —<br>telephony network or end-customer device (5 and 6). Go to Step<br>6. | Audio reached Connect Customer cleanly but agent heard degradation—agent<br>network, device, or headset (1, 2, and 3). Go to Step 4.       |

###### Multi-party and conference calls

For conference or multi-party calls, apply this recording-localization logic per
leg (per ContactId), not to the call as a whole.

###### No recording available

If you can't determine the affected path from the recording—or no recording is
available—continue to Step 4 to pull the metrics, which can localize the issue
independently.

## Step 4: Collect diagnostic data (agent-side, paths 1, 2, and 3)

Run these in order. Each links to its full procedure.

1. **Endpoint Test Utility**—from the affected
   agent's machine, validate WebRTC support, media-device access, per-Region
   latency (target **under 300 ms**), and required
   ports. Download the JSON results. See [Validate connectivity to Connect Customer with the Endpoint Test Utility](check-connectivity-tool.md "check-connectivity-tool.md").
2. **QualityMetrics from the contact record**—call
   [DescribeContact](../APIReference/API_DescribeContact.md "../APIReference/API_DescribeContact.md") and review:

   - **`QualityScore`** (1.00 =
     poor, 5.00 = excellent) for a quick read.
   - **`PotentialQualityIssues`**:
     `HighPacketLoss`, `HighJitterBuffer`, or
     `HighRoundTripTime`. An empty list means no issue was
     detected. See [Troubleshoot audio quality issues by using QualityMetrics in the contact record](sop-audio-qa.md "sop-audio-qa.md").

3. **CCP logs**—if available, download them and
   open them in the CCP Log Parser. Check for ERROR-level entries and WebRTC
   metrics during the affected call: `PacketLoss`,
   `JitterBufferMillis` (> 30 ms is abnormal),
   `RoundTripTime` (> 300 ms is abnormal). See [Download and review Connect Customer Contact Control Panel (CCP) logs](download-ccp-logs.md "download-ccp-logs.md").
4. **Amazon CloudWatch**—check whether
   `ToInstancePacketLossRate` exceeded **20%** during the time of the issue. For more information about checking this metric,
   see [Troubleshoot Amazon Connect audio quality issues (AWS
   re:Post)](https://repost.aws/knowledge-center/connect-audio-quality-issues "https://repost.aws/knowledge-center/connect-audio-quality-issues"). Audio quality can degrade at packet loss rates well below
   20%; this threshold indicates a severe issue requiring immediate network team
   engagement.

Then branch on what you found:

- **Abnormal metrics found** → treat as a
  **network** issue (Step 5, network
  path).
- **No abnormal metrics** → treat as a **workstation** issue (Step 5, workstation path).

## Step 5: Resolve agent-side issues

### Network (path 3)

Abnormal `PacketLoss`, `JitterBuffer`,
`RoundTripTime`, or a high `ToInstancePacketLossRate`
point to the agent network. Check:

- **Virtual private network (VPN)**—does the issue reproduce without
  VPN (direct connection)? If VPN is required, is split-tunneling enabled for
  real-time traffic?
- **Wi-Fi vs. wired**—does it reproduce on a
  wired connection?
- **Firewall/proxy/NAT**—is UDP 3478 (media),
  TCP 443, and websocket traffic allowed? Use static NAT with keep-alives
  where possible.
- **Bandwidth contention**—are large file
  transfers or bandwidth-heavy apps running concurrently?
- **Distance to Region**—is the agent far
  from the AWS Region of the instance? (Correlates with high
  `RoundTripTime`.)

Full procedure: [Troubleshoot your network for call quality and disconnect problems](network-ts.md "network-ts.md"). For more information about metric interpretation, see [Troubleshoot audio quality issues by using QualityMetrics in the contact record](sop-audio-qa.md "sop-audio-qa.md").

### Workstation (paths 1/2)

No abnormal network metrics points to the headset, device, or software.
Check:

- **Headset**—wired vs. wireless; does a
  wired headset resolve it? Confirm it meets the [minimum headset requirements](ccp-agent-hardware.md#ccp-agent-headset "ccp-agent-hardware.md#ccp-agent-headset").
- **Audio Enhancement**—if enabled, does
  disabling it resolve the issue? Note these constraints:

  - **Voice Isolation must only be used with a
    wired headset.** For wireless or mixed setups, use
    **Noise Suppression**
    instead.
  - Audio Enhancement requires a **4-core CPU / 4
    vCPU minimum**.
  - **Audio Enhancement is not supported when using
    Connect Customer audio optimization (WebRTC redirection); it is supported
    with VDI local-browser access.** If both Audio
    Enhancement and Connect Customer audio optimization are configured, that
    conflict is a likely cause. See [Enable Audio Enhancement for agents in Connect Customer](audio-enhancement.md "audio-enhancement.md").

- **Humming**—verify headset/browser sample
  rate is 48000. See [Humming sound in the agent's audio device: Verify the headset and browser sample rates](verify-sample-rate.md "verify-sample-rate.md").
- **Browser or OS**—check for recent updates;
  does rolling back to the last working version resolve it? Confirm a [supported browser](connect-supported-browsers.md "connect-supported-browsers.md").
- **Virtual desktop infrastructure (VDI)**—for Citrix, WorkSpaces, or
  Omnissa, make sure that WebRTC redirection is configured through the
  `VDIPlatform` parameter. See [Use the agent workspace to optimize audio for Citrix, Amazon WorkSpaces, and Omnissa cloud desktops](optimize-audio-cdd.md "optimize-audio-cdd.md").
- **Exclusive device control**—check whether
  another application has taken exclusive control of the mic/speaker. See
  [One-way audio from customers](common-ccp-issues.md#ccp-oneway-issues "common-ccp-issues.md#ccp-oneway-issues").
- **Custom CCP**—if you use a custom CCP,
  does the issue reproduce on the default CCP?
- **Windows 11 first call after reboot**—if
  audio fails only on the first call after a reboot, apply the service
  startup-type fix (qWAVE, ndisuio.sys, dmwAppushSvc, SstpSvc, RasMan). See
  [CCP audio issues on first call after system reboot when using Windows 11](common-ccp-issues.md#ccp-windows-11-audio-issues-after-reboot "common-ccp-issues.md#ccp-windows-11-audio-issues-after-reboot").

Full procedure: [Troubleshoot an agent's workstation for call quality and disconnect problems](agent-ts.md "agent-ts.md") and [Improve call quality on agent workstations in Amazon Connect contact centers
(Prescriptive Guidance)](../../../prescriptive-guidance/latest/patterns/improve-call-quality-on-agent-workstations-in-amazon-connect-contact-centers.md "../../../prescriptive-guidance/latest/patterns/improve-call-quality-on-agent-workstations-in-amazon-connect-contact-centers.md").

## Step 6: Resolve end-customer/telephony issues (paths 4/5/6)

When the degradation is on the end-customer/telephony side, you can't fix it on the
agent workstation. Try to isolate the source before opening a case:

- **Change the calling environment**—have the
  end-customer try a different device, network, or carrier.
- **Check for a common factor**—does the issue
  correlate with a specific carrier, direct inward dial (DID) number, or geographic region? If
  it correlates with a particular country or number type, confirm that country's
  coverage and any known telephony restrictions in the [Amazon Connect Telecoms Coverage guide](https://d1v2gagwb6hfe1.cloudfront.net/Amazon_Connect_Telecoms_Coverage.pdf "https://d1v2gagwb6hfe1.cloudfront.net/Amazon_Connect_Telecoms_Coverage.pdf") on the Amazon Connect website.
- **Check for call forwarding**—is another system
  forwarding calls to Connect Customer? If so, does the issue occur on direct dials to Connect Customer
  without forwarding?
- **Test multiple numbers**—try multiple
  destination and source numbers to see whether the issue follows a particular
  number.

If the issue persists across these changes, open a case with AWS Support.

## Step 7: Before you contact AWS Support

If the issue persists after troubleshooting, [open a case](open-case-troubleshoot-audio.md "open-case-troubleshoot-audio.md") with **3–5 examples no older than 24 hours**, and include:

- Instance ARN and a description of the symptom (whose voice, and how—choppy,
  no audio, echo, and so on).
- ContactIds, timestamps (UTC), and contact-record snapshots.
- Call recordings attached to the case.
- For end-customer issues: the end-customer phone number (last 4 digits might be
  masked) and the Connect Customer phone number.
- Test results: browsers tested, networks tested, alternate-machine test,
  **Endpoint Test Utility JSON export**, and your
  **observations after running Ping and
  MTR**.
- Agent environment details: VPN/firewall/VDI configuration, headset type, and
  Audio Enhancement mode.
- CCP type (default vs. custom) and the downloaded CCP logs for the affected
  calls.
- Frequency of the issue and the date/time it started (UTC).

###### Download CCP logs immediately after affected calls

CCP logs persist only within the current browser session. If the agent closes or refreshes
the CCP tab, the browser discards the logs—download them as soon as possible after an affected
call.
