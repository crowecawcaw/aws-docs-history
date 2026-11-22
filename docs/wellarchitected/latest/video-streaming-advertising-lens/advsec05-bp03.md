

# ADVSEC05-BP03 Enable privacy-preserving advertising capabilities while protecting user data

 Advertising platforms need targeting and measurement that don't depend on cross-site or cross-application identification. The migration itself creates risk, as legacy tracking and its replacement can expose the same people through separate data paths. 

 **Desired outcome:** 
+  You have selected privacy-preserving capabilities through documented privacy, utility, custody, and service-dependency criteria. 
+  You have isolated replacement capabilities from legacy identifiers throughout the migration period. 
+  You have measured business effectiveness under approved privacy constraints and established governed timelines for retiring legacy tracking. 

 **Common anti-patterns:** 
+  Adding privacy-preserving capabilities without an inventory or retirement plan for legacy tracking. 
+  Sending results from an aggregate or identity-limited system back into a user-level profile store. 
+  Selecting a service-specific API without documenting withdrawal risk or an alternative path. 
+  Declaring success from privacy properties alone without measuring advertising effectiveness and data exposure. 

 **Benefits of establishing this best practice:** 
+  Reduces data concentration and linkage risk as legacy tracking is retired. 
+  Gives product, privacy, and revenue owners one record of migration trade-offs and decisions. 
+  Preserves the ability to change services or methods without rebuilding every advertising use case. 

 **Level of risk exposed if this best practice is not established:** Medium 

## Implementation guidance
<a name="implementation-guidance"></a>

 Privacy, utility, and platform dependence are relative to the advertising function and threat model. Contextual targeting reduces how much you rely on identity, but it can expose sensitive page content. Aggregate measurement limits record-level disclosure, yet narrow or repeated queries can still leak data. First-party identity shifts who owns the relationship, but the data stays sensitive. A migration acceptance envelope sets the limits you accept for disclosure risk, continuity, population reach, reversibility, and service control. 

 Joining legacy and replacement results at the user level sharpens the comparison, but that union can rebuild the very tracking path you are trying to retire. An evaluation bridge isolates that comparison for a set period. Keep it apart from your production identity services, and send only aggregate or identity-limited results to approved measurement. 

 Exposure remains after you stop collecting data. Identifiers, interfaces, derived profiles, and recomputation paths can preserve the old capability long after new events stop arriving. Proving that you retired it creates its own risk, where detailed evidence can hold enough data to rebuild what you retired. Share the decision across owners so no one team alone balances effectiveness, residual exposure, evidence, and the risk that a service or partner changes the mechanism mid-migration. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Build the tracking dependency inventory:** Record cookies, device identifiers, identity graphs, partner IDs, fingerprinting signals, and derived profiles. Map each mechanism to its use cases, data stores, interfaces, owners, retention, and downstream dependencies. 

1.  **Set acceptance envelopes:** For each advertising function, approve the utility floor, exposure ceiling, coverage requirement, service-dependency tolerance, and failure behavior. Evaluate contextual classification under [ADVSEC04-BP02 Create guardrails and controls to maintain brand safety and content moderation within your workload](advsec04-bp02.md), collaboration under [ADVSEC02-BP03 Implement secure data collaboration with least privileged access and privacy controls](advsec02-bp03.md), and authenticated relationships under [ADVSEC01-BP01 Implement user authentication and access control to protect bidding process and content](advsec01-bp01.md). 

1.  **Isolate both paths and the evaluation bridge:** Use separate data stores, access roles, namespaces, and telemetry for legacy and replacement paths. Limit the bridge to the approved population, duration, join authority, and aggregate outputs, then block those outputs from enriching legacy profiles. 

1.  **Run the governed comparison:** Register the baseline, population, duration, success measures, privacy measures, and stop conditions before traffic enters the experiment. Preserve results at the granularity approved by the applicable acceptance envelope. 

1.  **Apply migration gates:** Compare the experiment with the applicable acceptance envelope before expanding a use case. Record utility gaps, privacy exceptions, service dependencies, unresolved legacy links, and the owner of each remediation. 

1.  **Prove legacy-path retirement:** Stop collection, remove interfaces, revoke access, expire retained identifiers, and disable recomputation from legacy data. Confirm that telemetry, storage, and dependency inventories no longer show active use, then retain the decommissioning evidence. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [ADVSEC04-BP02 Create guardrails and controls to maintain brand safety and content moderation within your workload](advsec04-bp02.md) 
+  [ADVSEC02-BP03 Implement secure data collaboration with least privileged access and privacy controls](advsec02-bp03.md) 
+  [ADVSEC01-BP01 Implement user authentication and access control to protect bidding process and content](advsec01-bp01.md) 
+  [ADVSEC01-BP05 Implement cross-platform identity governance for converged linear and digital operations](advsec01-bp05.md) 

 **Related documents:** 
+  [Navigating the Maze of Identity Solutions: A Guide for Advertisers, Publishers, and AdTech](https://iabtechlab.com/navigating-the-maze-of-identity-solutions-a-guide-for-advertisers-publishers-and-adtech/) 
+  [Privacy-enhanced data collaboration on AWS](https://aws.amazon.com/advertising-marketing/privacy-enhanced-data-collaboration/) 