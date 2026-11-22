

# Failure, recovery, and capacity management

 Advertising systems operate at the intersection of owned infrastructure and external partner dependencies (DSPs, SSPs, measurement providers, and CDN origins). A failure in any layer, whether an internal component, an external partner, or a data store, translates directly into lost auction revenue or measurement gaps. This capability addresses how you detect, contain, and recover from failures across all three dimensions: proactive DR readiness, defensive architecture against external failures, and data recovery within regulatory constraints. 


|  ADVREL04: How do you manage failures, maintain availability during partner outages, and recover data within your recovery objectives?  | 
| --- | 
| [ADVREL04-BP01 Create disaster recovery (DR) runbooks, and regularly test documented backup and restoration processes](advrel04-bp01.md) | 
| [ADVREL04-BP02 Architect defensively against failures](advrel04-bp02.md) | 
| [ADVREL04-BP03 Monitor and manage partner SLAs against actuals](advrel04-bp03.md) | 
| [ADVREL04-BP04 Design your workloads to withstand failures of individual components](advrel04-bp04.md) | 
| [ADVREL04-BP05 Back up data in multiple locations with consideration for regulatory requirements](advrel04-bp05.md) | 

## Capability intent
<a name="advrel04-capability-intent"></a>
+  Disaster recovery runbooks are documented, regularly tested with SSP/DSP partner coordination, and validated against realistic failure conditions using [AWS Fault Injection Service](https://aws.amazon.com/fis/). 
+  Your advertising system continues operating when external partners experience failures, using circuit breakers, retries, and fallbacks that help avoid cascading impact across the auction pipeline. 
+  Partner SLAs are monitored against actuals with [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) custom metrics, and SLA degradation triggers automated protective actions before revenue impact. 
+  Individual component failures (compute, databases, and caches) are absorbed by cell-based architectures with distributed resources across Availability Zones. 
+  Data is backed up in multiple locations with backup strategies aligned to per-tier RTO/RPO objectives and with consideration for privacy regulations governing advertising audience data. 

## Common issues to watch for
<a name="advrel04-common-issues-to-watch-for"></a>
+  Never testing backup restoration, discovering that backups are corrupt or incomplete during an actual disaster. 
+  DR runbooks that describe the desired end-state but not the step-by-step procedure, making them unusable under pressure. 
+  External partner failures cascading into auction failures because of missing circuit breakers or fallback behavior. 
+  Relying on internet-based connections for critical partner integrations without [AWS Direct Connect](https://aws.amazon.com/directconnect/) or [AWS PrivateLink](https://aws.amazon.com/privatelink/) alternatives. 
+  No fallback behavior when external data providers (DMPs, audience platforms) are unavailable, so bids proceed with no targeting data or are abandoned entirely. 
+  Not considering privacy regulations when planning cross-region data replication for backup. EU user data may not be replicated to non-EU regions. 
+  Over-provisioning backup solutions beyond what RPO/RTO requirements justify, inflating costs without proportional recovery benefit. 