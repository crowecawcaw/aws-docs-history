

# Identity and access management

 Access management for an advertising platform protects sensitive data, financial information, and programmatic access while keeping permissions appropriate for authorized users. Advertising platforms face a dual authentication challenge. Human users (campaign managers, traffickers, and analysts) need interactive identity flows, while machine-to-machine traffic (bid requests, creative syncs, and reporting APIs) requires low-latency token validation that doesn't exceed the 100 ms bid response window. Additional challenges arise from converged linear and digital environments, where panel data and census-level data must be governed with strict consent and identity boundaries. 


|  ADVSEC01: How do you manage identities, access control, and authorization across your advertising platform and its programmatic partners?  | 
| --- | 
| [ADVSEC01-BP01 Implement user authentication and access control to protect bidding process and content](advsec01-bp01.md) | 
| [ADVSEC01-BP02 Restrict DSP access to allow only authorized SSPs](advsec01-bp02.md) | 
| [ADVSEC01-BP03 Restrict DSP outbound traffic to authorized SSPs only](advsec01-bp03.md) | 
| [ADVSEC01-BP04 Implement least privilege access to protect programmatic workloads](advsec01-bp04.md) | 
| [ADVSEC01-BP05 Implement cross-platform identity governance for converged linear and digital operations](advsec01-bp05.md) | 

## Capability intent
<a name="advsec01-capability-intent"></a>
+  All SSP and DSP participants are authenticated using industry-standard protocols before they can submit or receive bid requests, and your authentication system handles high request volume without adding latency to the bid response window. 
+  Authorization policies are scoped to advertising-specific boundaries (per-campaign, per-advertiser, per-publisher, and per-data-type access controls) enforced consistently regardless of which component processes the request. 
+  Agentic AI workloads (campaign optimization agents, creative agents, and measurement agents) operate with minimal permissions scoped to their specific function. 
+  Cross-environment identity governance covers both linear panel-based household-level and digital user-level identity spaces with consent boundary enforcement. 
+  Industry identity solutions integrate with controls for token lifecycles and sharing-participant verification. 

## Common issues to watch for
<a name="advsec01-common-issues-to-watch-for"></a>
+  Using a single shared API key for all programmatic partners rather than issuing unique credentials per SSP or DSP relationship. 
+  Relying solely on IP-based allowlisting for partner authentication without cryptographic verification of request origin. 
+  Applying the same authentication flow to human users and machine-to-machine traffic without accounting for latency constraints. 
+  Granting broad read access to all campaign data when a partner only needs performance metrics for their specific campaigns. 
+  Deploying AI agents with the same permissions as human administrators, allowing agents unrestricted access to audience data, creative assets, and financial records. 
+  Resolving linear panel data to individual digital identifiers without verifying that consent covers both use cases. 