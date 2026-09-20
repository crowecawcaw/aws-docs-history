

# Access control within sovereign boundaries
<a name="dssec02"></a>

 A single control layer isn't sufficient to protect sovereign data. Network controls alone can't enforce identity rules, and identity controls alone can't account for network paths. To protect data within its sovereign boundary, you need layered preventive controls that verify identity, constrain network paths, and restrict resource-level access in proportion to data sensitivity and jurisdictional requirements. 

 This capability covers data perimeters that combine IAM conditions, resource-based policies, service control policies, VPC endpoint policies, and network controls to enforce jurisdictional boundaries and block unauthorized access before it occurs. 


|  DSSEC02: How do you control access to data within sovereign boundaries?  | 
| --- | 
| [DSSEC02-BP01 Protect data through layered access controls within sovereign boundaries](dssec02-bp01.md) | 

## Capability intent
<a name="capability-intent-1"></a>
+  Data remains accessible only to authorized identities operating within designated sovereign boundaries, and every access path is auditable. 
+  Network-centric and identity-centric controls operate as layered preventive boundaries rather than relying on detection after access has already occurred. 
+  Operator access is constrained to approved jurisdictions and approved roles, with access patterns recorded for regulatory demonstration. 
+  Cross-service and cross-Region data flows are explicitly mapped and controlled rather than implicitly permitted. 
+  Access control policies are expressed declaratively and validated through automated analysis, so teams rely less on manual review. 

## Maturity levels
<a name="maturity-levels-1"></a>

 These levels summarize what each stage of maturity looks like for this capability as a whole. 


|  Level  |  Name  |  What it looks like  | 
| --- | --- | --- | 
|  1  |  Initial  |  Access controls rely on individual IAM policies without coordination across layers. No formal data perimeter exists. Cross-Region data flows are not explicitly mapped or restricted.  | 
|  2  |  Emerging  |  Basic service control policies restrict actions at the organizational unit level. Some VPC endpoint policies are in place, but coverage is inconsistent. Operator access constraints exist but are not systematically enforced.  | 
|  3  |  Defined  |  A formal data perimeter combines identity-based, network-based, and resource-based controls. Policies are codified and applied consistently across accounts. Operator access is restricted to approved jurisdictions through condition keys and network controls.  | 
|  4  |  Proactive  |  Access policies are validated through automated reasoning to confirm they enforce intended boundaries. New services and data flows are assessed against the data perimeter model before deployment. Exceptions are time-bound and logged.  | 
|  5  |  Optimized  |  Data perimeter effectiveness is continuously measured and refined. Policy changes are tested in isolated environments before promotion. Access patterns are analyzed to identify unused permissions and tighten controls proactively.  | 

## Common issues to watch for
<a name="common-issues-to-watch-for-1"></a>
+  Relying on a single control layer (for example, only detective controls) to identify violations rather than applying preventive controls that stop violations before they occur. 
+  Cross-service data flows that traverse Region boundaries without explicit mapping, which opens unintentional sovereignty gaps. 
+  VPC endpoint policies that allow all principals by default, which negates the boundary enforcement the endpoint was meant to provide. 
+  Operator access paths that bypass data perimeter controls through break-glass mechanisms that lack proper logging and time-bound constraints. 
+  Access control reviews conducted only at deployment time, so policy drift and permission accumulation over the workload lifecycle go unnoticed. 