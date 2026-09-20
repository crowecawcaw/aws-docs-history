

# Security foundations
<a name="dssec01"></a>

 Sovereign workloads carry regulatory obligations that span data residency, jurisdictional access, and continuous compliance. These obligations are easier to meet when security and sovereignty controls are part of the architecture from initial deployment rather than added later. A security foundation supplies automated guardrails, standardized baselines, and pre-configured compliance frameworks, so teams can deploy new workloads without rebuilding controls each time. 

 This capability covers multi-account landing zone architecture, digital sovereignty controls, data perimeters, and layered security patterns that enforce sovereignty requirements across the network, identity, data, and application layers. 


|  DSSEC01: How do you build secure foundations aligned with sovereignty requirements?  | 
| --- | 
| [DSSEC01-BP01 Establish secure foundations aligned with regulatory requirements](dssec01-bp01.md) | 

## Capability intent
<a name="capability-intent"></a>
+  Security, compliance, and sovereignty controls are embedded in the architecture from initial deployment, not retrofitted after workloads are running. 
+  Automated guardrails enforce data residency and jurisdictional access boundaries across all accounts and workloads without manual intervention. 
+  Landing zone configurations codify regulatory requirements into repeatable infrastructure as code, so new accounts inherit sovereignty controls by default. 
+  Data perimeters combine identity-based, network-based, and resource-based controls to prevent unauthorized cross-boundary access at multiple layers. 
+  Compliance monitoring runs continuously and produces audit-ready evidence without separate manual collection efforts. 

## Maturity levels
<a name="maturity-levels"></a>

 These levels summarize what each stage of maturity looks like for this capability as a whole. 


|  Level  |  Name  |  What it looks like  | 
| --- | --- | --- | 
|  1  |  Initial  |  Security controls are applied manually and inconsistently across accounts. Teams configure sovereignty controls on a per-workload basis with no standardized baseline. Compliance evidence is collected manually before audits.  | 
|  2  |  Emerging  |  A landing zone is established with basic organizational unit structure and some preventive controls. Data residency controls exist but are not uniformly applied across all workloads. Compliance monitoring covers some resources but gaps remain.  | 
|  3  |  Defined  |  Landing zone configurations are codified as infrastructure as code with digital sovereignty controls enabled across organizational units. Data perimeters enforce jurisdictional boundaries through service control policies and resource policies. Compliance baselines are documented and monitored continuously.  | 
|  4  |  Proactive  |  Guardrails are tested against regulatory changes before enforcement dates. New accounts and workloads automatically inherit sovereignty controls through landing zone automation. Data perimeter effectiveness is validated through automated reasoning tools.  | 
|  5  |  Optimized  |  Security foundations evolve ahead of regulatory requirements. Control effectiveness is measured through automated assurance and feeds back into baseline refinement. Regional implementations are benchmarked against each other and converge toward a unified, auditable standard.  | 

## Common issues to watch for
<a name="common-issues-to-watch-for"></a>
+  Security controls added after workloads are already running. The gap between deployment and compliance then persists until the next audit cycle. 
+  Landing zone accelerators deployed with default configurations that do not account for jurisdiction-specific sovereignty requirements, which gives a false sense of compliance. 