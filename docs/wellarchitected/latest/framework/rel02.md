

# Plan your network topology

 Workloads rarely live in one place. They span multiple cloud environments, both public and private, and often reach back to an existing data center. The network carries every request between users, services, and those environments, so a topology with a single fragile path caps the availability of everything behind it. If the network to a healthy application fails, users cannot reach it, and if the one link between two environments drops, the systems that depend on it stop communicating. 

 This capability covers how an organization plans a network topology for reliability: building highly available connectivity to public endpoints, provisioning redundant paths between private networks in the cloud and on premises, and planning addressing and structure in anticipation of failure and future growth. Plan the topology so that the loss of a single component, path, or location does not sever the connection between users and the workload, or between the workload and the systems it depends on. 


|  REL02: How do you plan your network topology?  | 
| --- | 
|  [REL02-BP01 Use highly available network connectivity for your workload public endpoints](rel02-bp01.md)  | 
|  [REL02-BP02 Provision redundant connectivity between private networks in the cloud and on-premises environments](rel02-bp02.md)  | 

## Capability intent
<a name="rel02-intent"></a>
+  Public endpoints resolve and respond even when a single network component, path, or location fails. 
+  Name resolution runs health checks and returns only healthy endpoints, so traffic moves away from an impaired path without operator action. 
+  Cacheable content is served close to users from edge locations, which lowers origin load and improves reachability. 
+  Connectivity between the cloud and private networks runs over two or more independent paths with diverse physical routes. 
+  Dynamic routing reroutes traffic to a healthy path automatically, and backup paths are sized for the traffic they must carry. 
+  Public endpoints are protected against volumetric and application-layer denial-of-service attacks. 

## Common issues to watch for
<a name="rel02-issues"></a>
+  Teams design a highly available application but leave DNS and network connectivity as single points of failure. 
+  Services are reached by IP address instead of domain name, which defeats DNS failover. 
+  Content is served to a wide geographic audience without a content delivery network, which raises latency and origin load. 
+  A workload has no plan for distributed denial-of-service attacks, so unwanted traffic crowds out legitimate users. 
+  Connectivity to private networks relies on a single link, one VPN tunnel, or a single internet provider, any of which is a single point of failure. 
+  Dynamic routing is omitted, so a healthy backup path sits idle while an operator changes routes manually. 
+  Failover paths are never tested, so their behavior and recovery time are unknown until a real failure. 