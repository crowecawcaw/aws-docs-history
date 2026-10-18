

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

## Common issues to watch for
<a name="smperf04-issues"></a>
+ Relying solely on server-side logs with no client telemetry.
+ Client telemetry in a system that can't correlate with CDN or origin data.
+ No breakdown by geography or device, so localized issues are invisible.