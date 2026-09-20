

# Infrastructure access
<a name="dssec05"></a>

 Controlling how and from where operators access infrastructure is a core sovereignty concern. Operator access introduces risk when access paths span jurisdictions, when privileges persist beyond immediate need, or when regional teams lack the authority and tooling to operate independently. Sovereign workloads require access models that verify identity, validate access location through layered controls, enforce just-in-time privileges, and reduce interactive access through automation. 

 This capability covers operator access controls, jurisdictional access constraints, and the empowerment of regional teams to operate within their own jurisdictions without dependency on centralized access paths. 


|  DSSEC05: How do you secure infrastructure access while enabling regional operations?  | 
| --- | 
| [DSSEC05-BP01 Control operator access to infrastructure from approved locations](dssec05-bp01.md) | 
| [DSSEC05-BP02 Empower regional teams](dssec05-bp02.md) | 

## Capability intent
<a name="capability-intent-4"></a>
+  Operator access to infrastructure is constrained to approved locations and validated through layered identity and network controls. 
+  Privileges are granted just-in-time and scoped to the minimum necessary for each operation, with time-bound expiration. 
+  Interactive access to production systems is minimized through automation, reducing both risk surface and dependency on individual operators. 
+  Regional teams possess the authority, tooling, and training to operate their jurisdictions independently without requiring access from centralized or foreign locations. 
+  All operator access is logged with sufficient context (identity, source location, time, and scope) to support forensic review and regulatory reporting. 

## Maturity levels
<a name="maturity-levels-4"></a>

 These levels summarize what each stage of maturity looks like for this capability as a whole. 


|  Level  |  Name  |  What it looks like  | 
| --- | --- | --- | 
|  1  |  Initial  |  Operators use standing credentials with broad permissions. Access location isn't validated or constrained. Regional teams depend on centralized operations for infrastructure changes.  | 
|  2  |  Emerging  |  Multi-factor authentication is required for infrastructure access. Some jurisdictional constraints exist through network-level controls, but they are not comprehensive. Regional teams have partial operational capability but escalate frequently.  | 
|  3  |  Defined  |  Just-in-time access is implemented with time-bound sessions and approval workflows. Access is constrained to approved locations through IP-based conditions and network controls. Regional teams operate independently for routine tasks with clear escalation paths for exceptions.  | 
|  4  |  Proactive  |  Automation handles the majority of operational tasks, reducing the need for interactive access. Access patterns are analyzed to identify unused privileges and tighten constraints. Regional teams are fully self-sufficient with local tooling, documentation, and trained personnel.  | 
|  5  |  Optimized  |  Interactive access is the exception, reserved for break-glass scenarios with enhanced logging and post-event review. Access models evolve based on usage data and threat intelligence. Regional operational independence is validated through exercises and measured against defined capability targets.  | 

## Common issues to watch for
<a name="common-issues-to-watch-for-4"></a>
+  Standing administrator credentials that persist across sessions, creating a permanent attack surface and violating least-privilege principles. 
+  Jurisdictional access constraints enforced only at the network level without corresponding identity conditions, allowing authenticated operators from non-approved locations to access systems through VPN or direct connections. 
+  Regional teams that lack sufficient authority or tooling to operate independently, creating bottlenecks where all changes must route through a central team in another jurisdiction. 
+  Automation pipelines that run with broad permissions and are not subject to the same jurisdictional constraints applied to human operators. 