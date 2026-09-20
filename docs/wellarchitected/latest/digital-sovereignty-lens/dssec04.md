

# Detection and investigation
<a name="dssec04"></a>

 Sovereign workloads face threats beyond standard cybersecurity concerns. Unauthorized cross-border data transfers, operator access violations, and jurisdictional compliance drift are sovereignty-specific threats that require purpose-built detection capabilities. Standard threat detection must be augmented with jurisdiction-specific intelligence, full telemetry with data residency controls, and detailed logging of operator actions. 

 This capability covers threat detection, sovereignty-specific monitoring, and operator action logging that together enable timely investigation of security events in sovereign workloads. 


|  DSSEC04: How do you detect and investigate security events in sovereign workloads?  | 
| --- | 
| [DSSEC04-BP01 Enhance threat detection through targeted intelligence](dssec04-bp01.md) | 
| [DSSEC04-BP02 Detect sovereignty-specific threats through telemetry and analysis](dssec04-bp02.md) | 
| [DSSEC04-BP03 Establish comprehensive logging and monitoring of operator actions](dssec04-bp03.md) | 

## Capability intent
<a name="capability-intent-3"></a>
+  Threat detection covers both traditional cybersecurity threats and sovereignty-specific threats such as unauthorized cross-border data transfers and operator access violations. 
+  Threat intelligence is enriched with jurisdiction-specific indicators that reflect the regulatory and geopolitical context of each operating region. 
+  Telemetry data is retained within approved jurisdictions and accessible to authorized investigators without violating data residency requirements. 
+  Operator actions are logged with sufficient detail (identity, location, time, and scope) to support forensic investigation and regulatory demonstration. 
+  Detection findings are correlated across data sources to reduce alert fatigue and flag high-confidence sovereignty violations for immediate response. 

## Maturity levels
<a name="maturity-levels-3"></a>

 These levels summarize what each stage of maturity looks like for this capability as a whole. 


|  Level  |  Name  |  What it looks like  | 
| --- | --- | --- | 
|  1  |  Initial  |  Basic threat detection services are enabled with default configurations. Sovereignty-specific threats are not explicitly monitored. Operator actions are logged but not systematically reviewed or correlated.  | 
|  2  |  Emerging  |  Threat detection is configured with custom rules for some sovereignty-specific scenarios. Log data is centralized but retention and residency controls are not fully implemented. Operator access logs exist but lack sufficient context for forensic investigation.  | 
|  3  |  Defined  |  Detection rules explicitly target sovereignty-specific threats alongside cybersecurity threats. Telemetry pipelines enforce data residency for log storage and access. Operator action logging captures identity, location, and scope with sufficient detail for regulatory demonstration.  | 
|  4  |  Proactive  |  Threat intelligence is enriched with jurisdiction-specific indicators and updated as geopolitical conditions change. Detection findings are correlated across sources to surface high-confidence alerts. Investigation workflows are pre-built and tested for sovereignty-specific scenarios.  | 
|  5  |  Optimized  |  Detection effectiveness is measured per jurisdiction and refined based on outcomes. New sovereignty threat patterns are identified through trend analysis and incorporated into detection rules proactively. Investigation timelines are benchmarked against regulatory notification deadlines.  | 

## Common issues to watch for
<a name="common-issues-to-watch-for-3"></a>
+  Threat detection services enabled with default rulesets that don't cover sovereignty-specific threats, creating blind spots for cross-border data exfiltration and operator access violations. 
+  Centralized logging architectures that aggregate telemetry across jurisdictions without access controls, violating data residency requirements for the logs themselves. 
+  Operator action logs that record what was done but not from where or by whom at a sufficient level of detail, making forensic investigation and regulatory reporting incomplete. 
+  Alert volume that overwhelms investigation teams because detection rules lack tuning for sovereignty context, producing false positives from legitimate cross-Region operational activity. 
+  Investigation workflows that require cross-jurisdictional data access to complete, creating a circular dependency when the data residency controls prevent the investigation from proceeding. 