

# Security and compliance

 A strong security posture combines preventive, proactive, detective, and reactive controls so issues are blocked where they can be, caught before they are deployed, detected in running resources, and remediated when they appear. Security and compliance at the foundation level sets up emergency access, standardized log and telemetry destinations, auditable inventory, threat detection, vulnerability management, dedicated security tooling, forensic readiness, shift-left compliance checks, and organization-wide encryption and key management. This capability covers the best practices that protect your organization's resources and let security teams prevent, detect, and respond to events effectively. 


|  FND05: How do you detect, respond to, and remediate security threats and compliance violations?  | 
| --- | 
|  [FND05-BP01 Shift compliance checks left with proactive controls](fnd05-bp01.md)  | 
|  [FND05-BP02 Establish emergency access mechanisms](fnd05-bp02.md)  | 
|  [FND05-BP03 Configure audit logging of cloud operations](fnd05-bp03.md)  | 
|  [FND05-BP04 Configure standardized locations for logs, traces, and metrics](fnd05-bp04.md)  | 
|  [FND05-BP05 Maintain an auditable cloud inventory record](fnd05-bp05.md)  | 
|  [FND05-BP06 Remediate non-compliant resources](fnd05-bp06.md)  | 
|  [FND05-BP07 Implement threat detection mechanisms](fnd05-bp07.md)  | 
|  [FND05-BP08 Employ vulnerability and patch management controls](fnd05-bp08.md)  | 
|  [FND05-BP09 Establish security tooling for investigating incidents](fnd05-bp09.md)  | 
|  [FND05-BP10 Prepare forensic capabilities](fnd05-bp10.md)  | 
|  [FND05-BP11 Establish encryption and key management standards](fnd05-bp11.md)  | 

## Capability intent
<a name="fnd05-intent"></a>
+  Security services operate from dedicated security tooling and forensics accounts separated from workloads, provisioned ahead of any incident so the team is not assembling capability under pressure. 
+  Audit logs, traces, metrics, and resource inventory are captured in standardized, centrally owned, immutable locations that support correlation, investigation, compliance evidence, and point-in-time reconstruction. 
+  Compliance rules are codified once and enforced as close to the source of change as possible — in pipelines, at provisioning time, and in the provisioning service itself — so non-compliant resources are blocked before they exist wherever practical. 
+  Continuous threat detection, vulnerability scanning, and compliance checks run at organization scale, and findings flow into owned, prioritized response and remediation workflows rather than sitting unattended. 
+  Emergency access works independently of the primary identity path, is tightly monitored for misuse, and is exercised often enough to be trusted during a real failure. 
+  Encryption keys, secrets, and certificates are managed through central services with documented ownership, rotation, and cross-account sharing patterns that workloads consume instead of reinventing. 

## Common issues to watch for
<a name="fnd05-issues"></a>
+  Emergency access processes that depend on the same identity provider they are meant to work around, leaving administrators locked out of the environment at the moment they most need access. 
+  Logs, traces, and inventory split across accounts with inconsistent retention and access controls, so incident investigations stall and compliance evidence is assembled by hand each time. 
+  A compliance program built almost entirely on detective tooling, where every misconfiguration becomes a ticket, a remediation action, and a communication exercise rather than being prevented at provisioning time. 
+  Threat detection, vulnerability scanning, and compliance services enabled without clear ownership, severity thresholds, or remediation SLAs, producing alert fatigue and ageing backlogs rather than action. 
+  Security tooling mixed into a general admin account and forensics capabilities designed during an active incident, which weakens chain of custody and wastes time that should be spent on containment. 
+  Encryption keys, secrets, and certificates created per workload with no central inventory, per-Region keys used for cross-Region replicated data, and credentials stored in environment variables, so failovers break and rotation requires redeployment. 