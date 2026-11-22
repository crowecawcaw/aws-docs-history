

# Protecting compute

 Compute resources run the code behind a workload, and each type carries its own risk. An instance, a container, and a function differ in how they are built, accessed, and replaced, but the strategies that keep them secure are shared: reduce the attack surface, know and fix what is vulnerable, limit who can touch a running resource, and confirm that only approved software runs. 

 Protection that lasts depends on the lifecycle of a resource, not a single moment. What a resource is built from, how it is changed after launch, and how quickly a newly disclosed flaw is addressed matter more than any one control applied once. Immutable patterns, where a resource is replaced from a fresh image rather than modified in place, remove whole classes of drift and reduce the window of exposure. 

 This capability covers building compute from a known secure baseline, verifying the integrity and provenance of software before it runs, finding and remediating vulnerabilities by workload risk, reducing manual management and interactive access, and automating these protections so they hold at scale. It does not cover the network, identity, or data protection controls that other capabilities address. 


|  SEC06: How do you protect your compute resources?  | 
| --- | 
|  [SEC06-BP01 Perform vulnerability management](sec06-bp01.md)  | 
|  [SEC06-BP02 Provision compute from hardened images](sec06-bp02.md)  | 
|  [SEC06-BP03 Reduce manual management and interactive access](sec06-bp03.md)  | 
|  [SEC06-BP04 Validate software integrity](sec06-bp04.md)  | 
|  [SEC06-BP05 Automate compute protection](sec06-bp05.md)  | 

## Capability intent
<a name="sec06-intent"></a>
+  Compute resources launch from hardened baselines configured to a recognized standard, carrying only what the workload needs. 
+  Only software with verified integrity and provenance runs, because artifacts are checked against publisher signatures and internally built code is signed and verified before it executes. 
+  Vulnerabilities are found continuously across the pipeline and running environments, and remediation is prioritized by data sensitivity, exposure, and business impact rather than raw severity alone. 
+  Resources are managed through automation rather than interactive login, and direct access is reserved for logged, emergency-only sessions. 
+  Immutable replacement is the default response to change, so resources are rebuilt from updated images instead of patched in place wherever the component allows it. 
+  Scanning, patching, verification, and remediation run automatically, with a manual override that lets operators pause a control while requirements change. 

## Common issues to watch for
<a name="sec06-issues"></a>
+  Compute launches from generic base images with unused packages, services, and open ports left in place, widening the attack surface before any workload runs. 
+  Integrity checks rely on a hash alone, which proves a file is unchanged but says nothing about its source, so altered artifacts with matching published hashes pass verification. 
+  Vulnerabilities are treated as equally urgent by severity score, so remediation effort ignores the data sensitivity and exposure that determine real risk to the workload. 
+  Operators reach running resources interactively over SSH or RDP as routine, keeping a remote-access port open and inviting manual error and shared credentials. 
+  Resources are patched in place indefinitely rather than replaced from updated images, and approved exceptions are never revisited, so drift accumulates and unpatched paths remain long after the reason for the exception has passed. 
+  Automated remediation runs with no override, so it reverts a legitimate change and fights the operators who need to make it. 