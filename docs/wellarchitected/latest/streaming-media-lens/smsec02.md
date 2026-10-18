

# Detection
<a name="smsec02"></a>

Viewer access patterns provide a data source for identifying unauthorized access. A combination of client and infrastructure logging baselines expected behavior and alerts on deviations.


| SMSEC02: How do you monitor access to your media distribution workload? | 
| --- | 
| [SMSEC02-BP01 Monitor for fraudulent access attempts](smsec02-bp01.md) | 

## Capability intent
<a name="smsec02-intent"></a>
+ Access patterns are logged and analyzed for anomalies.
+ Fraudulent or unauthorized access attempts are detected through automated monitoring.
+ Risk scoring is applied to sessions based on behavior signals.

## Common issues to watch for
<a name="smsec02-issues"></a>
+ No access logging or anomaly detection on content requests.
+ Logs collected but never analyzed for geographic or volume anomalies.
+ No post-authentication behavior monitoring for credential sharing.