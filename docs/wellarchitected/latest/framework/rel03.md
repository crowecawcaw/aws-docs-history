

# Design your workload service architecture

 How you divide a workload into services shapes how it fails, scales, and changes over time. A monolith packages all functionality into one deployable unit. A service-oriented architecture (SOA) splits functionality into coarse services aligned to business functions, and a microservices architecture pushes those boundaries finer so each service owns a single capability. Smaller services can differentiate the availability each one needs and focus investment where it matters most, but they turn the workload into a distributed system with its own coordination and failure costs. 

 This capability covers how an organization designs the service architecture of a workload for reliability: choosing a segmentation level deliberately, drawing service boundaries along business domains, and defining machine-readable contracts between services. Together these decisions let components scale, recover, and release on their own, and they contain a failure within one part of the workload rather than letting it spread across the whole. 


|  REL03: How do you design your workload service architecture?  | 
| --- | 
|  [REL03-BP01 Choose how to segment your workload](rel03-bp01.md)  | 
|  [REL03-BP02 Build services focused on specific business domains and functionality](rel03-bp02.md)  | 
|  [REL03-BP03 Provide service contracts per API](rel03-bp03.md)  | 

## Capability intent
<a name="rel03-intent"></a>
+  A workload is divided into components whose boundaries match reliability requirements, team ownership, and tolerance for operational overhead. 
+  Service boundaries follow business domains, so each service owns a coherent capability and sets its own reliability requirements. 
+  Components are as loosely coupled and stateless as their function allows, so they scale and recover independently. 
+  Every API exposes a documented, machine-readable contract with a versioning strategy, so producers and consumers change without breaking each other. 
+  The architecture can evolve toward finer segmentation as adoption grows, rather than requiring a full rewrite. 

## Common issues to watch for
<a name="rel03-issues"></a>
+  Teams build a monolith with no internal modularity, leaving no path to decompose it as the workload grows. 
+  Services grow so interdependent that one failure cascades across all of them, recreating a monolith's fragility with the added cost of distribution. 
+  Teams adopt microservices for a product racing to first launch, paying distributed-system costs before they are needed. 
+  Boundaries follow technical layers such as user interface or database, so a single business change spreads across many teams. 
+  A shared domain library couples services together, so a change for one domain forces changes and redeployments in others. 
+  APIs ship without typed schemas or a versioning strategy, so consumers must update in lockstep and integration errors appear only in production. 