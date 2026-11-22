

# Infrastructure protection

 Advertising endpoints receive variable traffic from partners, viewers, devices, and operator interfaces. Infrastructure protection distinguishes expected demand from volumetric abuse and malicious requests without interrupting legitimate auctions or playback sessions. 

 This capability covers network, edge, and request-layer controls. Creative substitution after delivery and changes inside an approved asset belong to content-integrity controls. 


|  ADVSEC03: How do you protect advertising infrastructure from volumetric attacks and malicious request behavior?  | 
| --- | 
| [ADVSEC03-BP01 Protect advertising endpoints against volumetric and application-layer attacks](advsec03-bp01.md) | 

## Capability intent
<a name="advsec03-capability-intent"></a>
+  Critical endpoints remain available during attacks, partner anomalies, and planned traffic peaks. 
+  Traffic decisions account for partner identity, request behavior, business exposure, and confidence in the available baseline. 
+  Teams define the scope and duration of planned-event exceptions, obtain approval, and remove the exceptions after the event. 
+  Teams detect request-layer threats at every approved ingress path without assigning post-delivery content changes to infrastructure controls. 
+  Protection events retain enough technical and business context for timely response and later tuning. 

## Common issues to watch for
<a name="advsec03-common-issues-to-watch-for"></a>
+  Applying one global rate limit to every partner and endpoint, which blocks legitimate demand and hides partner-specific anomalies. 
+  Increasing limits for an event without an owner or expiration, which turns a temporary exception into permanent exposure. 
+  Protecting the public entry point but leaving alternate or internal ingress paths outside equivalent request controls. 
+  Treating successful request parsing as proof of authorization, which misses validly formed abuse and request-layer injection attempts. 
+  Assigning browser-side or post-delivery creative changes to edge controls, which leaves the actual content-integrity response path unclear. 