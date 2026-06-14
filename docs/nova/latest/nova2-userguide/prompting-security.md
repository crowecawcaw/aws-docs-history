# Security use cases

This guide provides best practices for prompting Nova 2 Lite to perform
security operations tasks focused on analysis use cases. It covers an example of converting a threat intelligence
report into a structured hunt plan for a Security Operations Center (SOC) team.
Nova 2 Lite is not designed to generate malicious code or perform offensive
security operations. The prompting techniques shown here produce structured,
repeatable output that integrates into existing security workflows.

## Key principles

- Assign the model a specific security role (threat hunter, security engineer)
  to focus its output
- Define the output structure explicitly — sections, tables, and formats the
  model must follow
- Include rules that prevent hallucination of indicators, techniques, or
  vulnerabilities not present in the input
- Use iterative refinement to adapt output to your environment, tooling,
  and constraints

## Threat intelligence hunt planner

This prompt template converts a threat intelligence report into a structured
hunt plan. The model maps adversary behaviors to
[MITRE ATT&CK](https://attack.mitre.org/ "https://attack.mitre.org/"), a public
knowledge base of adversary tactics and techniques used as a common vocabulary in
threat intelligence. It then generates huntable hypotheses, identifies which techniques are
not huntable through Security Information and Event Management (SIEM) telemetry,
and produces a consolidated log source checklist. The output is SIEM-agnostic by
default. Analysts can request detection queries for a specific platform (SPL, KQL,
Sigma) as a follow-up.

The model assumes the threat intelligence report has already been vetted for
relevance by your team and does not perform its own applicability assessment.

**Recommended model configuration:**
Nova 2 Lite with medium reasoning.

Use the following system prompt to configure the model for threat intelligence
analysis.

```
IMPORTANT: Write all output as readable markdown. Do not wrap the entire
response in a code block. Use fenced code blocks only inside the Telemetry
Requirements section if needed.

You are a senior threat hunter supporting a SOC team. Your role is to convert
threat intelligence reports into actionable hunt plans focused on identifying
adversary tradecraft.

The intelligence you receive has already been vetted for relevance. Do not
assess whether the threat applies — it does. Focus entirely on
operationalizing the tradecraft described.

Your output has three sections, in this order:

MITRE ATT&CK MAPPING
- Map every adversary behavior in the report to ATT&CK techniques and
  sub-techniques
- Present as a table: Technique ID | Name | Tactic | How used (one sentence,
  specific to the report)
- Do not map techniques not described or clearly implied in the report
- In the "How used" column, describe the behavior without reproducing specific
  domain, IP, or hash values. Refer to indicators generically rather than by
  value.

HUNT HYPOTHESES

Assessment
- State whether the report provides sufficient operational detail to support
  actionable hunting
- If the report defers IOCs or technical details to a separate document, name
  that document and note that indicator-based hunts require it

Not Huntable via SIEM
- A technique is not huntable if detecting it requires telemetry that the
  target device class does not realistically forward to a SIEM, or if
  detection requires decrypting encrypted payloads or inspecting raw packet
  captures. Connection metadata (IPs, ports, timing, volume, TLS certificate
  fields) is available without decryption and counts as huntable telemetry.
- List every mapped technique that cannot be hunted using logs a SIEM
  realistically ingests — one entry per technique with a one-line reason
- Each entry must include the technique ID and name
- Only list techniques that appear in your MITRE ATT&CK MAPPING table above.
  Do not introduce new techniques in this section

Huntable Hypotheses
- For each remaining technique, generate a hypothesis with:
  - Statement: What you are looking for, stated as a testable proposition
  - Data required: The specific log source and event type needed, realistic
    for where the technique executes
  - Rationale: Why this activity would indicate the threat, and what
    distinguishes it from normal operations
  - Priority: High / Medium / Low
    - High: Technique is central to the adversary's objective AND detection
      signal is specific (low false-positive rate against the described
      behavior).
    - Medium: Technique is supporting or post-compromise, OR detection signal
      requires correlation with other events to be reliable.
    - Low: Technique is incidental, or detection signal overlaps heavily with
      benign activity and requires tuning per environment.
  - Specific indicators: Reference the location of relevant indicators in the
    source report. Do not reproduce hash, IP, or domain values. The analyst
    will retrieve exact values from the source report.
- Reference the ATT&CK technique ID in each hypothesis

TELEMETRY REQUIREMENTS
- Consolidate all required log sources across every huntable hypothesis into
  a single checklist
- Every telemetry entry must reference a technique ID from the Huntable
  Hypotheses section. Do not add sources that support no listed hypothesis.
- Format each entry as: [ ] Log source (event type) — needed for — technique
  IDs and what it detects
- All items unchecked — the analyst determines what is available, not you
- Flag high-value telemetry: sources that enable hunting for multiple
  techniques from this threat

RULES
- Do not invent techniques, indicators, behaviors, numeric thresholds, port
  numbers, byte sizes, time windows, or tuning values. If a threshold is
  needed in a hypothesis, phrase it as a variable ("volume exceeding
  baseline", "repeated connections") and leave tuning to the analyst.
- Do not invent log source names. Use only telemetry that applies to the
  device class where the technique executes
- Do not reference figures, tables, or sections by number unless they appear
  in the report you are analyzing. If you cannot verify a specific figure
  reference, describe the indicator location generically ("see IOC table")
  or omit the reference.
- If the report is vague about a technique, note the ambiguity
- Every technique in the MITRE ATT&CK MAPPING table must appear in exactly
  one of "Not Huntable via SIEM" or "Huntable Hypotheses". Verify before
  finalizing.
- Do not invent ATT&CK technique IDs. If unsure of the correct ID for a
  described behavior, use the parent technique ID or omit the mapping rather
  than guess.
- Do not generate a hypothesis you would not act on. Label it NOT HUNTABLE
  VIA SIEM instead.
- Keep output tight — no filler, no preamble, no restating the report back
  to the analyst

EXAMPLE (classification reasoning)
- T1190 Exploit Public-Facing Application → Huntable. Inbound connections
  and HTTP request metadata to exposed services are visible in WAF, reverse
  proxy, and edge firewall logs.
- T1003.001 OS Credential Dumping: LSASS Memory → Not Huntable via SIEM
  without EDR. Requires process access telemetry (Sysmon Event 10, EDR
  process handle events); standard Windows Security logs do not capture it
  reliably.
- T1016 System Network Configuration Discovery → Not Huntable via SIEM on
  most endpoints. On-host enumeration (ipconfig, route) produces no network
  artifact; detection requires command-line logging that is often not
  forwarded.
- T1110.003 Password Spraying → Huntable. Authentication logs show
  low-volume failed logons across many accounts from a single source,
  distinguishable from single-account brute force.
- T1070.004 File Deletion on a network appliance → Not Huntable via SIEM.
  Executes on an embedded device (router/firewall) that forwards syslog and
  connection metadata only; host-level file, process, auditd, and
  iptables-change events are not available to the SIEM even though equivalent
  logs exist on servers.
- T1486 Data Encrypted for Impact → Huntable. File modification events and
  mass-rename patterns appear in file server audit logs and EDR file
  telemetry.
```

The following example demonstrates the full output structure. The input is a
short vendor blog post summary. Longer reports produce more extensive plans.

`User:`

```
Our threat intel team flagged this report as relevant to us.
Generate a hunt plan.
"A New Sandworm Malware Cyclops Blink Replaces VPN Filter.pdf"
```

`Assistant:`

```
## MITRE ATT&CK MAPPING

| Technique ID | Name | Tactic | How used |
|--------------|------|--------|----------|
| **T1133** | External Remote Services | Initial Access | Actors deploy modified device firmware images by exploiting an externally-available management service. |
| **T1059.004** | Command and Scripting Interpreter: Unix Shell | Execution | Cyclops Blink executes downloaded files using the Linux API (Unix shell). |
| **T1542.001** | Pre-OS Boot: System Firmware | Persistence | The malware is embedded in a modified device firmware image to survive reboots. |
| **T1037.004** | Boot or Logon Initialization Scripts: RC Scripts | Persistence | Cyclops Blink runs at device startup via a tweaked RC script. |
| **T1562.004** | Impair Defenses: Disable or Modify System Firewall | Defense Evasion | The malware alters the Linux firewall to permit C2 traffic. |
| **T1036.005** | Masquerading: Match Legitimate Name or Location | Defense Evasion | Cyclops Blink masquerades as a Linux kernel thread process. |
| **T1082** | System Information Discovery | Discovery | The malware regularly queries and beacons device information to its C2 server. |
| **T1090** | Proxy | Command and Control | C2 traffic can be routed through a proxy to hide the source. |
| **T1132.002** | Data Encoding: Non-Standard Encoding | Command and Control | Command messages use a custom binary scheme to encode data. |
| **T1008** | Fallback Channels | Command and Control | The malware selects a C2 server from lists of IPv4 addresses and ports. |
| **T1071.001** | Application Layer Protocol: Web Protocols | Command and Control | Files are downloaded and commands issued over HTTP/HTTPS. |
| **T1573.002** | Encrypted Channel: Asymmetric Cryptography | Command and Control | C2 messages are individually encrypted (AES-256-CBC) and sent under TLS. |
| **T1571** | Non-Standard Port | Command and Control | C2 uses ports that are not typical for HTTP/HTTPS traffic. |
| **T1041** | Exfiltration Over C2 Channel | Exfiltration | The malware can upload files to a C2 server. |

---

## HUNT HYPOTHESES

### Assessment
The advisory provides sufficient tactical detail (e.g., C2 protocols,
persistence mechanisms, and traffic patterns) to build generic detection
logic. However, indicator-of-compromise (IOC) values (specific IPs, domains,
hashes) are **deferred to the accompanying Cyclops Blink malware analysis
report**; indicator-based hunts therefore require that report.

### Not Huntable via SIEM
- **T1059.004 - Command and Scripting Interpreter: Unix Shell** - Requires
  process-level execution telemetry from the network device, which is not
  forwarded to a typical SIEM.
- **T1542.001 - Pre-OS Boot: System Firmware** - Detection needs firmware
  image analysis; not available via standard logs.
- **T1037.004 - Boot or Logon Initialization Scripts: RC Scripts** - Relies
  on boot-time script execution logs that most SIEMs do not collect from
  network appliances.
- **T1562.004 - Impair Defenses: Disable or Modify System Firewall** -
  Requires firewall-rule-change audit data that is generally not forwarded
  from WatchGuard devices.
- **T1036.005 - Masquerading: Match Legitimate Name or Location** - Needs
  process-identity details that are not exported to SIEM from the device.

### Huntable Hypotheses

| ATT&CK ID | Statement | Data required | Rationale | Priority | Specific indicators |
|-----------|-----------|---------------|-----------|----------|----------------------|
| **T1133** | Unexpected inbound connections to a device's remote-management interface from external IPs. | WatchGuard firewall logs (management-interface connection events). | Cyclops Blink is delivered via exploitation of open remote-management services; inbound connections that bypass the allowed management-access list are a clear sign of initial-access activity. | **High** | See Cyclops Blink malware analysis report - IOC table for affected management ports. |
| **T1082** | Periodic outbound HTTPS requests from a network device to a small set of domains/IPs with low-volume payloads. | Outbound NetFlow/Zeek logs, DNS query logs, TLS handshake logs (SNI, certificate fields). | The malware beacons device information on a regular schedule; repetitive, low-data-size HTTPS calls to the same endpoints stand out from normal device behavior. | **High** | See Cyclops Blink malware analysis report - beacon frequency and target domains. |
| **T1090** | Use of an intermediate proxy server for outbound C2 traffic from infected devices. | Proxy server access logs (e.g., Squid, Bluecoat) showing requests originating from WatchGuard IPs. | Proxy usage is a common evasion tactic; seeing known-good device IPs proxying to unusual destinations suggests C2 redirection. | **Medium** | See Cyclops Blink malware analysis report - proxy-config examples. |
| **T1132.002** | Outbound HTTP/HTTPS requests containing high-entropy binary data that does not match normal application payloads. | Proxy or Zeek HTTP(S) payload logs (or network TAP packet captures) with entropy analysis. | The custom binary encoding of C2 messages produces high-entropy byte streams; anomalous binary content in otherwise legitimate-looking web requests can indicate command encoding. | **Medium** | See Cyclops Blink malware analysis report - sample encoded command payloads. |
| **T1008** | Rapid switching of destination IP/port pairs for outbound connections from the same device within a short time window. | NetFlow/Zeek flow records (source-IP, destination-IP, destination-port, timestamps). | Fallback-channel logic causes the malware to rotate C2 endpoints; frequent IP/port changes from a single device are suspicious. | **Medium** | See Cyclops Blink malware analysis report - list of C2 IP/port pairs. |
| **T1071.001** | Outbound HTTP/HTTPS traffic to domains that resolve to Tor hidden services or to IPs known to host .onion exit nodes. | DNS resolution logs, NetFlow/Zeek logs, and optional Tor exit-node list cross-reference. | Cyclops Blink can use Tor for C2 reachability; traffic to .onion-associated domains or IPs is a strong indicator of hidden-service communication. | **High** | See Cyclops Blink malware analysis report - known C2 domains and Tor hidden-service names. |
| **T1573.002** | Outbound TLS handshakes from a network device that present self-signed certificates or certificates signed by an untrusted CA. | TLS handshake logs (e.g., from firewall/proxy) capturing certificate subject, issuer, serial, and public-key fingerprint. | The malware generates individually-signed TLS certificates for each C2 session; seeing unexpected self-signed or mistrust-CA certificates from a device is a red flag. | **High** | See Cyclops Blink malware analysis report - sample certificate details. |
| **T1571** | Outbound connections from a WatchGuard device to destination ports outside the conventional web ports on a regular basis. | NetFlow/Zeek flow logs (source-IP, destination-port). | Using non-standard ports evades typical port-filtering; repeated connections to atypical ports from network equipment warrants investigation. | **Medium** | See Cyclops Blink malware analysis report - list of non-standard C2 ports. |
| **T1041** | Large outbound data transfers to a known C2 IP that do not match normal device backup or update patterns. | NetFlow/Zeek volume statistics, proxy transfer logs, or firewall byte-count logs. | The ability to exfiltrate files is part of the malware's C2 capabilities; bulk data pushes to C2 endpoints deviate from normal device behavior. | **Medium** | See Cyclops Blink malware analysis report - typical exfiltration sizes and destinations. |

---

## TELEMETRY REQUIREMENTS

| [ ] Log source (event type) — needed for — technique IDs and what it detects |
|----------------------------------------------------------------------------|
| **[ ] WatchGuard firewall logs (management-interface connection events)** — needed for — **T1133** (inbound remote-management exploitation) |
| **[ ] WatchGuard firewall/NetFlow logs (outbound connection metadata)** — needed for — **T1082**, **T1008**, **T1571**, **T1041** (beacon timing, fallback-channel switching, non-standard ports, exfiltration volume) |
| **[ ] DNS query logs** — needed for — **T1082**, **T1071.001** (domain resolution for C2, Tor hidden-service lookup) |
| **[ ] Proxy server access logs (Squid/Bluecoat)** — needed for — **T1090**, **T1132.002**, **T1071.001**, **T1573.002**, **T1041** (proxy usage, payload inspection, TLS handshake, large transfers) |
| **[ ] TLS handshake / certificate logs (firewall or proxy)** — needed for — **T1573.002**, **T1071.001** (certificate fields, SNI, self-signed cert detection) |
| **[ ] Zeek/NetFlow L7 payload logs (binary entropy, HTTP(S) body)** — needed for — **T1132.002** (non-standard encoding detection) |
| **[ ] WatchGuard syslog (device-level audit messages)** — needed for — **T1133** (optional context on management-interface events) |

*High-value telemetry (enabling multiple techniques):*
- **WatchGuard firewall logs** - cover inbound remote-management (T1133), outbound beaconing (T1082), fallback-channel switching (T1008), non-standard ports (T1571), and exfiltration volume (T1041).
- **Proxy logs + TLS handshake logs** - together support proxy usage (T1090), web-protocol C2 (T1071.001), encrypted-channel detection (T1573.002), and payload-encoding analysis (T1132.002).
- **NetFlow/Zeek flow data** - provide the backbone for timing, IP/port rotation, and volume-based exfiltration across many C2 techniques.
```

### Iterative refinement

After the initial output, use follow-up prompts to extend or adapt the
plan.

- **Extend the plan:**

  - "Add an executive summary"
  - "Add response and containment guidance"
  - "Write detection queries for [SIEM platform]"

- **Refine based on your environment:**

  - "We don't have DNS logging, remove those hypotheses and focus on proxy
    and endpoint telemetry"
  - "Our partner org runs Sentinel, give me the detections in KQL so we
    can share"

The model revises the plan based on updated context.

### Considerations

The following considerations apply when using this prompt to generate hunt
plans from threat intelligence reports.

- **Verify technical identifiers.** Large language
  models can generate inaccurate technical specifics. Verify these values against
  authoritative sources before acting on them.
- **Validate telemetry requirements against your
  environment.** The model proposes log sources based on the techniques
  described in the report, not on the telemetry your organization collects. Treat
  the telemetry checklist as a set of requirements to evaluate, not an inventory
  of available data.
- **Assess the quality of the source report.** The
  hunt plan reflects the content of the input report. If the source intelligence is
  incomplete, inaccurate, or ambiguous, the output inherits those limitations. The
  model does not validate the accuracy of the report.
- **Use hunt plans as input to detection
  engineering.** Hunt plans are hypotheses for analysts to validate, tune,
  and operationalize. They are not finished detection rules.
- **Mitigate prompt injection risk.** Threat
  intelligence reports provided as input can contain instructions intended to
  manipulate the model. Treat the report as untrusted data rather than as trusted
  instructions. For more information, see
  [Prompt injection](../../../bedrock/latest/userguide/prompt-injection.md "../../../bedrock/latest/userguide/prompt-injection.md").
