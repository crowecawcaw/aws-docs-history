

# REL12-BP02 Perform post-incident analysis

 Post-incident analysis is the structured review of a customer-impacting event to find its contributing factors and prevent recurrence. Done well, it produces durable improvements across every workload that shares the same design, which helps you avoid repeating incidents. 

 **Desired outcome:** 
+  Your teams follow a consistent, agreed approach to reviewing customer-impacting events. 
+  Each analysis identifies root causes and contributing factors, not only the immediate trigger. 
+  You capture corrective actions with clear ownership and track them to completion. 
+  Findings are shared beyond the responding team, so other workloads can apply the same mitigations. 

 **Common anti-patterns:** 
+  Teams stop at the first contributing factor and do not look deeper for related problems. 
+  Analysis blames human error without adding the training or automation that would prevent it. 
+  The review focuses on assigning blame, which creates fear and discourages honest disclosure. 
+  Findings stay within a small group, so other teams never benefit from the lessons. 
+  No mechanism captures institutional knowledge, and the same root cause produces repeat incidents. 

 **Benefits of establishing this best practice:** 
+  Other workloads mitigate shared risks before they cause an incident. 
+  Recurrence drops because corrective actions address root causes, not symptoms. 
+  Teams build a searchable record of past failures that speeds future investigations. 
+  A blameless culture surfaces honest detail, which produces more accurate analysis. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 The [correction of error (COE) process](https://aws.amazon.com/blogs/mt/why-you-should-develop-a-correction-of-error-coe/) provides a repeatable structure for post-incident analysis. Document what happened, why it happened, and what will prevent it. Review those findings and track corrective actions to completion. A COE is most valuable when it targets the architectural pattern behind the trigger, because a fix applied to one workload often protects others that share the same design. 

 When people fear blame or consequences, they withhold the detail that makes root-cause analysis accurate, and the review produces a shallow, incomplete result. A blameless approach treats each incident as a property of the system, not an individual's failing. It still requires accountability, but through system design that makes human error hard to commit and easy to recover from. When you find human error, correct it with automation, guardrails, or process changes rather than with a penalty. 

 Techniques such as the [five whys](https://en.wikipedia.org/wiki/Five_whys) push past the first plausible explanation to the underlying condition that allowed the failure. [AWS DevOps Agent](https://docs.aws.amazon.com/devopsagent/latest/userguide/about-aws-devops-agent.html) can accelerate this by correlating logs, metrics, and traces into an incident timeline and surfacing contributing factors for human review. Analyze near misses and systems that behave unexpectedly while still meeting their function. They often reveal latent weaknesses before customers feel any impact. In every review, ask why your existing testing did not catch this. If no test covers the case, write one. 

 Assign clear ownership for the process so investigations and follow-ups do not stall. Keep findings in a knowledge repository that responders can search, and add recurring patterns to developer guides and pre-deployment checklists. Share results openly through review meetings that anyone can attend, so other teams can apply the mitigations before facing the same incident. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Run the analysis blame-free:** Establish that the goal is to prevent recurrence, not to penalize individuals. A blameless review lets the people involved assess corrective actions dispassionately and collaborate honestly across teams. 

1.  **Document the incident with a standard structure:** Capture each incident in a consistent format so reviews are comparable and searchable. Record what happened, the impact on customers and the business, the root cause, and the supporting data such as metrics and graphs. Note cross-pillar implications, especially security, along with the lessons learned and the corrective and related actions. 

1.  **Define standard operating procedures for the review:** Write procedures that specify the steps, the information to collect, and the questions to answer during analysis. Set up a standardized incident reporting process that captures the initial report, logs, communications, and actions taken. 

1.  **Investigate to root cause:** Go beyond the immediate trigger using techniques such as the five whys. Treat near misses and unexpected behavior as incidents worth reviewing, and assess why existing tests did not detect the issue. Add tests for the case when none exist. 

1.  **Capture and share institutional knowledge:** Record key findings in a knowledge management system and identify patterns to add to developer guides or pre-deployment checklists. Share findings through open review meetings so other teams can apply the mitigations. Continually refine the process based on feedback and lessons learned. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [REL12-BP01 Use playbooks to investigate failures](rel12-bp01.md) 
+  [REL12-BP04 Test resilience using chaos engineering](rel12-bp04.md) 
+  [REL12-BP05 Conduct game days regularly](rel12-bp05.md) 

 **Related documents:** 
+  [Why you should develop a correction of error (COE)](https://aws.amazon.com/blogs/mt/why-you-should-develop-a-correction-of-error-coe/) 
+  [Amazon's approach to failing successfully](https://builder.aws.com/learn/topics/builders-library) 
+  [About AWS DevOps Agent](https://docs.aws.amazon.com/devopsagent/latest/userguide/about-aws-devops-agent.html) 

 **Related videos:** 
+  [AWS re:Invent 2025 - Mastering Root Cause Analysis: Rebuilding trust after outages (ARC211)](https://www.youtube.com/watch?v=MCCpBJqicEY) 