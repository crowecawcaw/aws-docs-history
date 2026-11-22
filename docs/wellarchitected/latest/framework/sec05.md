

# Protecting networks

 Network protection is how a workload controls which components can reach each other and what traffic is allowed to cross between them. It complements identity and access controls as part of a defense-in-depth strategy: identity decides who can call an action, and the network decides which components can communicate at all. A flat network where every resource can reach every other resource offers no containment, so a single point of unauthorized access exposes everything behind it. 

 Effective network protection treats the network as a set of boundaries rather than a single perimeter. Components are grouped by their function, the sensitivity of the data they handle, and how they behave, and controls are placed at each boundary so only authorized flows pass. Traffic is inspected against expected patterns, and protections tighten as traffic moves closer to sensitive data. Because these controls span many accounts and change over time, they are most reliable when they are expressed as code and deployed through automation rather than configured manually. 


|  SEC05: How do you protect your network resources?  | 
| --- | 
|  [SEC05-BP01 Create network layers](sec05-bp01.md)  | 
|  [SEC05-BP02 Control traffic flow within your network layers](sec05-bp02.md)  | 
|  [SEC05-BP03 Implement inspection-based protection](sec05-bp03.md)  | 
|  [SEC05-BP04 Automate network protection](sec05-bp04.md)  | 

## Capability intent
<a name="sec05-intent"></a>
+  Workload components are grouped into isolated network layers that reflect their function, data sensitivity, and behavior, with control points at every boundary. 
+  Internet-facing components are separated from internal ones, so someone who reaches a public entry point cannot move freely toward sensitive systems. 
+  Only the flows a workload actually needs are permitted, in both directions, applying least privilege to network paths within and between layers. 
+  Traffic crossing between layers is inspected against explicit rules, current threat intelligence, and a baseline of normal behavior, with protection tightening near the most sensitive data. 
+  Network protections are defined as version-controlled templates, validated before deployment, and rolled out consistently across accounts through automated pipelines. 
+  Ownership of controls is divided deliberately between central and workload teams, so protection stays both standardized and responsive to workload-specific needs. 

## Common issues to watch for
<a name="sec05-issues"></a>
+  Resources share a single flat network with no internal boundaries, so unauthorized access to one component gives a clear path to every other component. 
+  Internal components are exposed directly to the internet because no boundary separates public entry points from private resources. 
+  Controls are applied only at the perimeter of a layer while internal flows go unrestricted, on the assumption that any traffic already inside is trusted. 
+  Controls cover ingress but not egress, so a component under unauthorized control can still send data out or reach an external command channel unhindered. 
+  Traffic is filtered only by port and protocol, so unauthorized traffic reuses permitted paths to blend in, and without a baseline of normal traffic those anomalies go unnoticed. 
+  Network protections are configured manually for each workload, so they drift apart across environments and unintended changes weaken protection without anyone noticing. 