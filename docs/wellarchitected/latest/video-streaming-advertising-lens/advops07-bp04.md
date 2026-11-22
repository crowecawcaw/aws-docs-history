

# ADVOPS07-BP04 Conduct post-incident reviews for revenue-affecting events

 Many publisher operations teams conduct post-incident reviews only for availability incidents while revenue-affecting events that did not cause visible downtime go unreviewed. Yield-affecting failure patterns repeat without systematic analysis or improvement. The operational excellence pillar specifies that post-incident analysis should review customer-affecting events, identify contributing factors and preventative actions, and develop mitigations to limit recurrence. 

 **Desired outcome:** 
+  Every incident causing measurable yield loss undergoes a blameless post-incident review producing concrete improvement actions. 
+  Revenue impact is quantified using pre-incident yield baselines (eCPM, fill rate) so that every review starts with a shared understanding of the business stakes. 
+  Improvement action completion rates are tracked, and unresolved actions are escalated in subsequent reviews. 

 **Common anti-patterns:** 
+  Conducting post-incident reviews only for availability incidents while ignoring revenue-affecting events that did not cause system downtime. 
+  Failing to quantify the revenue impact of operational incidents. 
+  Conducting blame-focused reviews that discourage transparent root cause disclosure, limiting accurate identification of systemic problems. 
+  Not tracking improvement action completion rates after reviews. 

 **Benefits of establishing this best practice:** 
+  Quantified revenue impact enabling prioritization of preventative investments. 
+  Reduced recurrence of known failure patterns through systematic improvement actions. 
+  Organizational learning that accelerates operational maturity across all publisher workload teams. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 Treating availability and revenue incidents differently creates an artificial distinction. The business loses revenue either way. A Prebid auction can finish inside its SLO and still return thin demand because of a misconfigured adapter, even while infrastructure remains healthy. The event can drain revenue without ever reaching an incident tracker, so the pattern repeats. 

 Review thresholds determine which events receive a formal review. Ad yield moves constantly with auction timing and demand shifts, so the threshold must separate ordinary movement from a loss worth investigating. Your threshold should correlate to your revenue scale rather than being based on another system's numbers. 

 A review without a dollar figure does not compete for engineering time because the figure gives every incident a common basis for prioritization. Accuracy depends on the baseline used for comparison. Ad revenue rises and falls by hour and day of week, so a mismatched window distorts the loss. The comparison holds only when both periods match. 

 Blameless review comes first because people who fear blame withhold the details that reveal the cause. A review focused on finding a culprit might produce a tidy account while missing the systemic flaw. A blameless review identifies which design, tooling, or process condition allowed the failure. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Define revenue impact thresholds that trigger mandatory post-incident reviews:** Establish thresholds appropriate to your revenue scale. Document them in the operational handbook with both the absolute threshold and the relative threshold. See the absolute and relative thresholds defined above. Configure CloudWatch alarms that alert the on-call team when these thresholds are crossed, creating an automatic trigger for post-incident review initiation. 

1.  **Establish a blameless post-incident review template with revenue impact quantification:** Create a standard template covering: incident timeline (when did each stage of the incident occur), contributing factors (systemic conditions that enabled the incident, not people who caused it), revenue impact calculation (baseline yield × duration comparison, described in the implementation guidance), immediate mitigation actions taken, and preventive improvement actions. Require the revenue impact calculation for every review. This creates a shared vocabulary for prioritizing prevention investments. 

1.  **Calculate revenue impact for each reviewed incident using pre-incident yield baselines:** For each review, retrieve the 7-day rolling average eCPM and fill rate at the same time of day and day of week as the incident. Compare against actual metrics during the incident period. See the methodology described in the implementation guidance above. Document the calculation methodology in the review record so results are reproducible. 

1.  **Track improvement action completion with escalation for overdue items:** For each post-incident review, assign all improvement actions to named owners with specific due dates. Configure a tracking mechanism (Jira, GitHub Issues, or equivalent) with automated reminders at due dates and escalation to team leads for overdue items. Report improvement action completion rates at the monthly operational health review alongside workload health metrics. Low completion rates indicate organizational or resourcing failures that require management attention. 

1.  **Share post-incident lessons across publisher workload teams through quarterly cross-team reviews:** At the end of each quarter, compile post-incident lessons from all publisher workload themes (Prebid, SGAI, FAST channels, and innovative formats) and present them in a cross-team review session. Identify patterns that apply across multiple workload types (for example, a monitoring gap pattern in Prebid that also applies to SGAI) and create new improvement initiatives targeting the cross-cutting issues. Build a searchable post-incident lessons repository that new team members can query during onboarding. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [ADVOPS07-BP05 Share operational knowledge across publisher workload teams](advops07-bp05.md) 
+  [ADVOPS01-BP05 Foster a publisher operations culture that prioritizes yield reliability](advops01-bp05.md) 

 **Related documents:** 
+  [AWS Well-Architected OE pillar OPS11-BP02 guidance on post-incident analysis](https://docs.aws.amazon.com/wellarchitected/latest/operational-excellence-pillar/evolve.html) 
+  [Why you should develop a correction of error (COE)](https://aws.amazon.com/blogs/mt/why-you-should-develop-a-correction-of-error-coe/) 

 **Related services:** 
+  [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) 
+  [Quick](https://aws.amazon.com/quicksight/) 