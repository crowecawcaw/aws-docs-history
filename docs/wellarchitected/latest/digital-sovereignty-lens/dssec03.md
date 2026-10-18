

# Sovereignty control verification
<a name="dssec03"></a>

 Claiming sovereignty compliance is different from proving it. Sovereignty controls must be verifiable through automated analysis rather than relying solely on manual audits or periodic reviews. Automated reasoning, network reachability analysis, and configuration validation provide mathematical or evidence-based assurance that policies enforce the jurisdictional boundaries they are designed to protect. 

 This capability covers the use of proactive and detective controls to validate that access policies, network paths, and resource configurations meet sovereignty baselines before and after deployment. 


|  DSSEC03: How do you prove your sovereignty controls are effective?  | 
| --- | 
| [DSSEC03-BP01 Validate policy effectiveness through automated analysis](dssec03-bp01.md) | 
| [DSSEC03-BP02 Verify network security posture through automated analysis](dssec03-bp02.md) | 
| [DSSEC03-BP03 Validate resource configurations for sovereignty compliance](dssec03-bp03.md) | 

## Capability intent
<a name="capability-intent-2"></a>
+  Access policies are validated through automated reasoning to confirm they enforce intended jurisdictional boundaries, rather than relying on manual policy review alone. 
+  Network paths are analyzed to verify they don't cross sovereign boundaries, and reachability findings are resolved before workloads go live. 
+  Resource configurations are evaluated against sovereignty baselines both before provisioning (proactive) and after deployment (detective), so the intended controls match what is actually deployed. 
+  Verification results produce audit-ready evidence that demonstrates control effectiveness to regulators without separate manual evidence collection. 
+  New resources are blocked from provisioning when they violate sovereignty baselines, moving enforcement earlier in the deployment lifecycle. 

## Common issues to watch for
<a name="common-issues-to-watch-for-2"></a>
+  Policies that appear correct on inspection but contain implicit allows or overly broad conditions that automated reasoning would catch. 
+  Network reachability analysis scoped only to individual VPCs, missing cross-account peering or transit gateway paths that cross jurisdictional boundaries. 
+  Proactive controls deployed without detective controls as a backstop, so resources that bypass the proactive layer (for example, through console actions) go undetected. 
+  Verification results that are not actionable because findings lack context on which sovereignty requirement is violated and what remediation is needed. 
+  Automated analysis that runs on a schedule rather than on change events, creating windows where noncompliant configurations exist undetected between analysis runs. 