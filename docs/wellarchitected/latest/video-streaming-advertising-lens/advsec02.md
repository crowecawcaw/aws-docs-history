

# Data protection
<a name="advsec02"></a>

 Advertising data moves through auctions, media workflows, shared analysis environments, and measurement systems operated by separate organizations. Data protection keeps that information confidential and unaltered while preserving the latency, availability, and collaboration properties that advertising workloads require. 

 This capability covers protection in transit, at rest, during collaboration, and during record-level computation. It doesn't define identity governance or decide which regulatory obligations apply. 


|  ADVSEC02: How do you protect advertising data throughout transit, storage, collaboration, and computation?  | 
| --- | 
| [ADVSEC02-BP01 Encrypt DSP to SSP communication in transit using TLS](advsec02-bp01.md) | 
| [ADVSEC02-BP02 Protect linear distribution feeds and ad signaling in converged delivery](advsec02-bp02.md) | 
| [ADVSEC02-BP03 Implement secure data collaboration with least privileged access and privacy controls](advsec02-bp03.md) | 
| [ADVSEC02-BP04 Implement confidential computing for cross-party measurement without exposing raw viewer data](advsec02-bp04.md) | 

## Capability intent
<a name="advsec02-capability-intent"></a>
+  Data sensitivity, processing purpose, and trust boundaries determine protection requirements throughout the data lifecycle. 
+  Protection remains effective as data crosses partner, network, media, storage, and computation boundaries. 
+  Cryptographic identities, keys, certificates, and release authority have limited scope, named owners, and controlled lifecycles. 
+  Cross-party analysis reveals only approved information and produces evidence that every contributor can evaluate. 
+  Control owners detect, review, and resolve control changes, exceptions, and failures without bypassing partner or data-owner decisions. 

## Common issues to watch for
<a name="advsec02-common-issues-to-watch-for"></a>
+  Protecting primary data stores but leaving copies in logs, exports, media paths, or temporary computation outside the same control boundary. 
+  Selecting encryption or collaboration technology before defining what each party can learn, which produces controls that don't match the trust model. 
+  Reusing broad keys, certificates, or administrative authority across partners, which turns one compromise or rotation failure into a shared outage or exposure. 
+  Teams trust the collaboration environment, then share raw records or permit unrestricted analysis. This removes purpose and disclosure limits. 
+  Updating protected workloads or release policies without contributor approval, which breaks attestation and weakens the basis for partner trust. 