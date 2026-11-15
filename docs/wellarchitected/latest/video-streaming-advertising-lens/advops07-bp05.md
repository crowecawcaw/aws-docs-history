

# ADVOPS07-BP05 Share operational knowledge across publisher workload teams
<a name="advops07-bp05"></a>

 Siloed teams operating Prebid, SGAI, FAST channel, and ad format workloads miss opportunities to apply cross-organization operational improvements. Many operational patterns, such ascanary deployment strategies, automated rollback procedures, yield anomaly detection approaches, apply across multiple publisher workload types. Systematic knowledge sharing helps your teams apply organizationally-tested outcomes, which improves time and revenue cost. 

 **Desired outcome:** 
+  Operational insights, incident lessons, and optimization techniques are systematically shared across publisher workload teams, accelerating improvement across all themes. 
+  A shared knowledge base houses runbooks, playbooks, and incident retrospectives accessible to all publisher workload teams. 
+  Quarterly cross-team reviews provide a forum where each team presents significant improvements and challenges, enabling cross-pollination of effective practices. 

 **Common anti-patterns:** 
+  Publisher workload teams operate in complete isolation without sharing operational insights, and each team rediscovers the same monitoring patterns, runbook approaches, and yield optimization techniques independently. 
+  Duplicating runbook development effort across teams for similar failure patterns. 
+  Lacking a shared knowledge base, so incident lessons are lost when team members change roles or leave the organization. 

 **Benefits of establishing this best practice:** 
+  Accelerated operational improvement through cross-pollination of insights. 
+  Reduced duplicated effort in runbook and playbook development. 
+  Faster adoption of proven operational patterns across all publisher workload teams. 

 **Level of risk exposed if this best practice is not established:** Medium 

## Implementation guidance
<a name="implementation-guidance"></a>

 A veteran Prebid team has developed adapter failover procedures through real incidents. An SGAI team facing similar problems can reuse those procedures instead of rebuilding them. 

 Patterns don't transfer cleanly between workloads. A Prebid failover routine resembles an SGAI routine without matching it exactly. Excessive standardization forces teams to change valid requirements to fit a shared template. Teams must distinguish a cross-cutting pattern from a workload-specific one, and that judgment improves after several teams solve related problems. 

 Meetings and presentations can happen without changing runbooks or working practices. Real transfer occurs when one team runs another team's pattern in production. Measure adoption to confirm that sharing changed operations. 

 Undocumented knowledge is lost when its owner leaves the team. A shared repository of runbooks and retrospectives persists across role changes. Shared ownership often leaves maintenance unassigned when each team assumes another owns the repository. Contributors need a reason to share instead of retaining what they know. Recognize reusable techniques and systems to sustain contribution over time. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Establish a cross-team operational knowledge base:** Create a Git repository structured as a knowledge base: shared-patterns/ (cross-cutting operational patterns applicable to all workload types), prebid/ (Prebid-specific runbooks, playbooks, and lessons), sgai/ (SGAI-specific content), fast-channels/ (FAST-specific content), ad-formats/ (innovative format content), and incident-learnings/ (post-incident retrospectives tagged by workload type and pattern type). Require all operational documentation to be stored here. Remove silos by establishing this as the single authoritative location. 

1.  **Launch a cross-team community of practice with monthly cadence:** Schedule monthly 60-minute community of practice meetings with mandatory participation from at least one representative from each publisher workload team. Define the standing agenda: (1) incident learning of the month (one team shares a significant learning), (2) operational improvement demo (one team shares an improvement they implemented), (3) challenges and help requests (open floor for teams to ask for input from others), (4) knowledge base update review (what was added to the shared knowledge base this month). Rotate facilitation monthly. 

1.  **Implement a quarterly cross-team operational review:** Schedule quarterly 90-minute reviews where each team presents: top 3 operational improvements from the quarter (with measured MTTD/MTTR improvements), current top 3 open operational challenges, and operational health trend (MTTD, MTTR, and automation coverage: is the team improving?). Produce a quarterly summary document identifying cross-cutting patterns that could be standardized and shared. Share the summary with leadership as evidence of operational improvement program effectiveness. 

1.  **Identify and standardize cross-cutting operational patterns:** After 2–3 cycles of the community of practice, catalog the patterns that appear across multiple teams. Common cross-cutting patterns to look for: yield anomaly detection structures (SLO tiers, alarm hierarchies), automated rollback with guardrails (SSM Automation document structures), canary deployment patterns for yield-sensitive changes, and post-incident revenue impact quantification. Create canonical versions of these patterns in the shared-patterns/ knowledge base section that each team can adapt for their specific workload. 

1.  **Measure knowledge sharing effectiveness through cross-team runbook adoption rates:** Track the metric: "fraction of operational improvements that originated in one team and were adopted by another team." This can be measured by reviewing Git commit history for pull requests from team A that implement patterns from team B's runbooks. Set quarterly targets for this adoption rate (for example, at least 2 cross-team knowledge transfers per quarter per team) and report it alongside operational health metrics. A low adoption rate indicates that knowledge sharing activities are happening but not translating into operational improvements. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [ADVOPS07-BP04 Conduct post-incident reviews for revenue-affecting events](advops07-bp04.md) 

 **Related documents:** 
+  [AWS Well-Architected OE pillar OPS11-BP08 guidance on documenting and sharing lessons learned](https://docs.aws.amazon.com/wellarchitected/latest/operational-excellence-pillar/evolve.html) 