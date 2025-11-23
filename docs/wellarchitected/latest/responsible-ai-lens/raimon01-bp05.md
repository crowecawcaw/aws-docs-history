# RAIMON01-BP05 Design protocols that trigger human oversight of

automated monitoring alerts

Set protocols for when human reviewers should be involved in system
oversight decisions. Create sampling-based human review processes
that validate the accuracy and effectiveness of automated monitoring
systems, including procedures for evaluating edge cases and
challenging scenarios. Implement feedback mechanisms that enable
human reviewers to improve automated monitoring through labeling
ambiguous cases, refining alert criteria, and identifying new
monitoring requirements. Design human oversight workflows that
provide escalation paths, decision-making authority, and
documentation requirements for monitoring decisions that affect
system operation.

**Level of risk exposed if this best
practice is not established:** High

## Implementation considerations

1. Configure human review triggers in monitoring systems based on
   alert severity, confidence thresholds, and business impact.
   Use workflow orchestration tools like AWS Step Functions to
   route decisions and Amazon A2I for human review management.
2. Establish sampling protocols to validate monitoring accuracy,
   focusing on edge cases and high-risk scenarios. Integrate
   annotation tools for human reviewers to assess and label
   sampled alerts.
3. Create feedback loops allowing reviewers to label ambiguous
   cases and suggest monitoring improvements. Use Amazon A2I for
   feedback collection and AWS Step Functions to route feedback
   for monitoring system improvements.
4. Design escalation paths with clear authority levels and
   documentation requirements for critical monitoring decisions.
   Configure workflow tools to manage approvals and maintain
   audit trails of human oversight activities.
5. Document human oversight decisions, rationale, and outcomes to
   support continuous improvement of monitoring protocols. For
   example, documenting human interventions on monitoring alerts
   with timestamps, reviewer identity, decision rationale, and
   subsequent monitoring system behavior changes.

## Resources

**Related documents**

- [Amazon
  Augmented AI](../../../augmented-ai/latest/developerguide/what-is.md "../../../augmented-ai/latest/developerguide/what-is.md")
- [AWS Systems Manager Incident Manager](../../../incident-manager/latest/userguide/what-is-incident-manager.md "../../../incident-manager/latest/userguide/what-is-incident-manager.md")
- [ISO/IEC
  42001:2023 A.6.2.6 AI system operation and monitoring](https://www.iso.org/standard/42001 "https://www.iso.org/standard/42001")
