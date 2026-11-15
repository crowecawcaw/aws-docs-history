

# Privacy and regulatory adherence
<a name="advsec05"></a>

 Advertising data can be subject to different requirements based on jurisdiction, collection context, consent, processing purpose, and business agreement. Privacy and regulatory adherence helps you transition requirements into approved decisions that remain attached to data as it moves and changes. 

 This capability also governs the transition away from tracking methods that expose people across contexts. It defines obligations, evidence, permitted use, migration boundaries, and retirement decisions rather than duplicating data-protection or identity mechanisms. 


|  ADVSEC05: How do you govern regulatory obligations and privacy-preserving advertising across data types, jurisdictions, and channels?  | 
| --- | 
| [ADVSEC05-BP01 Verify that your advertising workload meets applicable data protection obligations](advsec05-bp01.md) | 
| [ADVSEC05-BP02 Design for compliance across both linear and digital data flows](advsec05-bp02.md) | 
| [ADVSEC05-BP03 Enable privacy-preserving advertising capabilities while protecting user data](advsec05-bp03.md) | 

## Capability intent
<a name="advsec05-capability-intent"></a>
+  Regulatory and contractual obligations are translated into approved control objectives with accountable business, privacy, and engineering owners. 
+  Purpose, consent, jurisdiction, retention, and rights-management metadata remain traceable through source and derived data. 
+  Cross-channel processing proceeds only when every contributing source authorizes the intended purpose. 
+  Privacy-preserving capabilities meet accepted utility and exposure criteria without reconnecting results to prohibited legacy identifiers. 
+  Evidence, exceptions, migrations, and decommissioning decisions remain reviewable throughout their lifecycles. 

## Common issues to watch for
<a name="advsec05-common-issues-to-watch-for"></a>
+  Treating a technical setting as compliance proof without linking it to an approved obligation, affected data, and evidence period. 
+  Losing purpose, consent, retention, or deletion metadata in derived datasets, which breaks later use and rights decisions. 
+  Combining linear, digital, household, or user-level data under the least restrictive source rule, which permits uses that one source did not authorize. 
+  Running legacy and replacement tracking paths without isolation, which lets aggregate or identity-limited results flow back into user-level profiles. 
+  Starting privacy alternatives without effectiveness criteria or a retirement plan, which preserves duplicate data stores and exposed interfaces indefinitely. 