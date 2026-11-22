

# Securely operate your workload

 Security foundations are the organization-wide decisions and controls that every workload builds on. They set how accounts are structured, how control objectives are defined and enforced, and how teams operate securely across the whole lifecycle of a workload, from design and build through running it and improving it. 

 Operating securely depends more on consistency than on individual effort. A governance approach guides decisions the same way every time, so control objectives are met without relying solely on the judgment of the person doing the work. Reusing shared capabilities and expressing controls as code makes that consistency repeatable, and it lets an organization improve security across many workloads at once rather than one at a time. 

 This capability covers establishing that foundation: separating workloads, defining and validating control objectives, reducing the security surface a team has to manage, automating the controls every workload inherits, modeling threats, and keeping current with new threats and capabilities. It does not cover the specific identity, network, data protection, or detection controls that the later capabilities address. 


|  SEC01: How do you securely operate your workload?  | 
| --- | 
|  [SEC01-BP01 Separate workloads using accounts](sec01-bp01.md)  | 
|  [SEC01-BP02 Identify and validate control objectives](sec01-bp02.md)  | 
|  [SEC01-BP03 Stay up to date with security threats and recommendations](sec01-bp03.md)  | 
|  [SEC01-BP04 Reduce security management scope](sec01-bp04.md)  | 
|  [SEC01-BP05 Automate deployment of standard security controls](sec01-bp05.md)  | 
|  [SEC01-BP06 Identify threats and prioritize mitigations using a threat model](sec01-bp06.md)  | 
|  [SEC01-BP07 Evaluate and implement new security services and features regularly](sec01-bp07.md)  | 

## Capability intent
<a name="sec01-intent"></a>
+  Workloads run within a governed account structure that isolates environments and limits the scope of impact of a failure or unauthorized access. 
+  Control objectives are derived from compliance obligations and the organization's threat model, and their effectiveness is validated continuously rather than assumed. 
+  Threats to each workload are identified during design and revisited as the workload changes, and mitigations are prioritized against them. 
+  Standard security controls are defined once, deployed consistently as code, and inherited by every new workload and account. 
+  Teams invest security effort only where it is specific to their workload, and reuse shared capabilities and managed services everywhere else. 
+  The organization tracks emerging threats and the AWS service roadmap, and folds relevant improvements into its controls on a regular cadence. 

## Common issues to watch for
<a name="sec01-issues"></a>
+  Unrelated workloads and environments share one account, so a single misconfiguration or unauthorized access reaches far beyond the resource that caused it. 
+  Control objectives exist as documents but are never validated in the running environment, so posture is assumed rather than known. 
+  Standard controls are applied manually for each workload, so they drift apart and coverage depends on who set the account up. 
+  Teams rebuild logging, identity, and detection for every workload instead of consuming shared capability, multiplying both effort and inconsistency. 
+  Threat models are written once at launch and never revisited, so they no longer reflect the workload or the threats it now faces. 
+  New security services are picked up opportunistically by individuals rather than evaluated and rolled out through a repeatable mechanism. 