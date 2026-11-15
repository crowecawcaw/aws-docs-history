

# Ad measurement and verification reliability
<a name="advrel08"></a>

 Ad measurement and verification reliability requires dependable systems to accurately track, validate, and report advertising performance metrics while accounting for fraud, viewability, and data quality issues. This includes implementing redundant verification methods, maintaining data accuracy across multiple solutions, and verifying consistent measurement capabilities even during system failures or data anomalies. 


|  ADVREL08: How do you maintain the reliability of your ad measurement and verification systems?  | 
| --- | 
| [ADVREL08-BP01 Implement redundant ad verification systems with automated failover mechanisms](advrel08-bp01.md) | 
| [ADVREL08-BP02 Establish reliable data collection and validation pipelines for measurement accuracy](advrel08-bp02.md) | 

## Capability intent
<a name="advrel08-capability-intent"></a>
+  Redundant ad verification systems with automated failover support ongoing measurement capability even when individual verification providers are unavailable. 
+  Reliable data collection and validation pipelines maintain measurement accuracy through processing failures, retries, and reconciliation. 
+  Measurement data is protected against loss with at-least-once delivery guarantees and dead-letter queue processing. 

## Common issues to watch for
<a name="advrel08-common-issues-to-watch-for"></a>
+  Single point of failure in third-party verification provider integrations. 
+  Not processing dead-letter queue messages. Measurement data loss goes undetected. 