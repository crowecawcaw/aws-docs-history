

# Viewer experience measurement
<a name="smperf04"></a>

Infrastructure monitoring provides only part of the picture. Real user monitoring and client-side metrics are necessary to understand what viewers actually experience and to correlate client-side issues with infrastructure events.


| SMPERF04: How do you monitor viewer experience? | 
| --- | 
| [SMPERF04-BP01 Collect and analyze real user logs and metrics](smperf04-bp01.md) | 

## Capability intent
<a name="smperf04-intent"></a>
+ Client telemetry is collected and correlated with CDN and infrastructure logs.
+ Metrics are broken down by geography, device, ISP, and title.
+ Alerts correlate client-side quality events with infrastructure signals.

## Maturity levels
<a name="smperf04-maturity"></a>


| Level | Name | What it looks like | 
| --- | --- | --- | 
| 1 | Initial | The organization relies on server-side logs only with no client-side telemetry. Viewer issues are reported anecdotally. | 
| 2 | Emerging | Some client telemetry is collected but lives in a separate system with no correlation to CDN or infrastructure data. | 
| 3 | Defined | Client metrics (rebuffering, startup time, bit rate) are collected and can be correlated with CDN logs, broken down by geography and device. | 
| 4 | Proactive | Alerts fire when client-side quality degrades, and dashboards enable drill-down by ISP, device type, and title. | 
| 5 | Optimized | Real-user monitoring drives automated responses, experience scores are tracked per session, and client-side signals feed back into delivery and encoding decisions. | 

## Common issues to watch for
<a name="smperf04-issues"></a>
+ Relying solely on server-side logs with no client telemetry.
+ Client telemetry in a system that can't correlate with CDN or origin data.
+ No breakdown by geography or device, so localized issues are invisible.