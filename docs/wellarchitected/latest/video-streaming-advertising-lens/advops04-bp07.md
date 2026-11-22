

# ADVOPS04-BP07 Standardize incident response and escalation procedures across linear playout and digital ad serving

 Establish a unified incident response framework with consistent classification, escalation, and remediation procedures that apply across linear broadcast playout and digital ad serving infrastructure. Use automated detection, tiered escalation, and runbook automation to minimize MTTR across converged operations. 

 **Desired outcome:** 
+  All ad operations incidents (whether a playout server failure causing dead air, a programmatic bid stream interruption, or an SSAI stitch failure) follow a single, well-documented response process. 
+  Teams respond with consistent urgency, clear ownership, and pre-approved actions. 
+  Post-incident analysis drives ongoing improvement across both linear and digital domains. 

 **Common anti-patterns:** 
+  Maintaining separate incident management processes for linear NOC and digital ad ops teams, which results in inconsistent severity classification and delayed communication when incidents span both domains. 
+  Not conducting post-incident analysis that drives runbook improvement across both linear and digital domains, which means that you miss opportunities to reduce the recurrence of cross-channel failure modes. 
+  Relying solely on manual detection of delivery failures rather than automated alerting from real-time monitoring. 

 **Benefits of establishing this best practice:** 
+  A unified incident response framework reduces MTTD and MTTR while minimizing unplanned business disruption. 
+  Clear escalation paths with pre-approved actions expedite decision-making and reduce MTTR. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 Linear TV and digital advertising teams have historically operated separate incident management infrastructure. Linear Network-on-Chip (NOC) uses broadcast-oriented tools and processes, and digital ad ops uses web-oriented ones. This split creates coordination overhead when incidents require a fast response. A SSAI stitch failure that affects both the linear simulcast and the OTT streaming delivery requires both teams to coordinate. They have no shared tools or classification criteria and no pre-defined escalation paths. 

 AWS Systems Manager Incident Manager automatically creates incidents from CloudWatch alarms or EventBridge events. It centralizes management, organizes relevant AWS resource information, and initiates predefined response plans. Integrate linear playout alarms (MediaLive) and digital ad serving alarms (Prebid Server, ADS) into a single Incident Manager instance. From one place, you manage incidents across both domains. 

 Use an impact matrix to classify incidents across both domains. Score each incident by audience scope (individual viewer, content segment, channel, and all channels) and revenue impact per minute (low <$X/min, medium X–Y/min, and high >$Y/min). 

 Build a library of runbooks over time and progressively automate them. Playbooks identify root causes, and runbooks mitigate them. AWS Systems Manager Incident Manager can populate runbook parameter values from incident context when an incident starts. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Deploy AWS Systems Manager OpsCenter and Incident Manager as unified systems:** Configure automated incident creation from CloudWatch alarms monitoring both linear playout health (MediaLive active alerts, scheduling engine health) and digital ad serving metrics (Prebid bid density, ADS response rates, SSAI stitch failure rates). Define response plans in Incident Manager that include contacts from both linear NOC and digital ad ops, with on-call schedules that cover both domains. 

1.  **Define a unified incident severity classification matrix:** Create a severity matrix using two dimensions: affected audience scope (one viewer, one content segment, one channel, all channels) and revenue impact per minute ($0–$100, $100–$1000, >$1000). Map combinations to Sev1–Sev4. Validate the matrix with both linear NOC and digital ad ops leadership before publication. Document the specific measurement method for each severity criterion to avoid subjective classification. 

1.  **Create response plans with pre-approved actions per severity level:** For each severity level, document: escalation timing (Sev1: immediate, Sev2: 5 minutes, Sev3: 30 minutes), notification channels (PagerDuty, Slack, and phone bridges), pre-approved actions (Sev1 incident commander can activate disaster recovery without further approval), and reporting cadence (Sev1: status update every 15 minutes to stakeholders). Pre-approved actions remove the approval chain that slows high-severity incident response. 

1.  **Implement automated Systems Manager Automation runbooks for common scenarios:** Create SSM Automation documents for: failover to backup playout (MediaLive input failover), restart ad decision services (ECS task restart), switch to fallback creative pool (update ADS configuration to use default creative), and route traffic to secondary region (Route 53 health check failover). Configure Incident Manager to automatically invoke the appropriate runbook based on incident type, with manual confirmation required for high-impact actions. 

1.  **Conduct post-incident analysis within 48 hours and drive cross-domain improvement:** Define a post-incident analysis process for both linear and digital incidents. Within 48 hours of resolution, produce an analysis document asking whether you could improve time to detection, whether metrics and alarms need updates, whether you could improve time to diagnosis, and whether runbook or playbook steps should be added or improved. Share completed analyses across both linear and digital teams and track the completion rate of improvement actions as an operational health metric. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [ADVOPS04-BP01 Create runbooks for the most common operational events and incidents that can impact your advertising workload](advops04-bp01.md) 

 **Related documents:** 
+  [AWS Systems Manager OpsCenter documentation](https://docs.aws.amazon.com/systems-manager/latest/userguide/OpsCenter.html) 
+  [AWS Systems Manager Incident Manager](https://docs.aws.amazon.com/incident-manager/latest/userguide/what-is-incident-manager.html) 

 **Related services:** 
+  [AWS Systems Manager](https://aws.amazon.com/systems-manager/) 
+  [Amazon EventBridge](https://aws.amazon.com/eventbridge/) 
+  [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) 