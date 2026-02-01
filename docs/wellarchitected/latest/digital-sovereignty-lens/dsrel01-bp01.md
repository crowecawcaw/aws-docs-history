# DSREL01-BP01 Document and rank critical business continuity

risks

Documenting and ranking critical business continuity risks enables
you to proactively identify potential service disruptions and
allocate resources effectively. You should also consider compliance
obligations while ranking risks.

Without a structured approach, you risk regulatory penalties and
compliance violations. You may also face operational disruptions and
damage to customer trust.

**Desired outcome:** A prioritized
risk register documents critical business continuity risks, aligned
mitigation strategies, and recovery procedures. Organizations
maintain effective compliance management and operational resilience
through systematic risk tracking and mitigation.

**Common anti-patterns:**

- Conducting risk assessments without cross-functional input,
  missing critical dependencies and creating incomplete risk
  profiles.
- Treating risk documentation as one-time deliverables instead of
  living artifacts that evolve with changing business conditions.
- Lacking data-driven quantitative risk metrics and clear recovery
  objectives, making it difficult to prioritize investments.
- Limiting risk assessment to technical or compliance aspects
  only, ignoring business impact and operational dependencies.
- Conducting infrequent testing and validation of recovery
  procedures, leading to outdated plans and unverified
  assumptions.

**Benefits of establishing this best
practice:**

- Systematic risk management documentation supports regulatory
  adherence. Stakeholder confidence is built by demonstrating
  preparedness and providing transparency to customers, partners,
  and regulators.
- Uses data-driven decision making to focus investments on
  highest-impact risks and avoid over-engineering low-impact
  areas.
- Accelerates incident response and reduces downtime through
  proactive identification of vulnerabilities.
- Provides systematic documentation that demonstrates due
  diligence to auditors and enables effective compliance
  management across the organization.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Start by assembling a cross-functional team, including members
from IT, security, compliance, legal, and business units.
Together, establish a standardized risk assessment framework that
aligns with regulatory requirements. Create a centralized risk
register. Use the register to document critical workloads, track
dependencies, record compliance obligations, and prioritize risks
based on likelihood and impact. Include regular updates and
validation through testing to maintain effectiveness and
regulatory adherence.

Many sovereign nations are having to deal with an ever-increasing
number of cyber-attacks and acts of sabotage. As a mitigation,
nations are putting forward new regulatory requirements related to
cyber-resiliency with the objective of protecting critical
national infrastructure, and strategically important public
services.

New regulations such as the
[EU
Digital Operational Resilience Act](https://www.eiopa.europa.eu/digital-operational-resilience-act-dora_en "https://www.eiopa.europa.eu/digital-operational-resilience-act-dora_en") (EU DORA) applies to a
broad set of financial entities and requires them to bolster their
cybersecurity and ICT operational resiliency capabilities. It is
implemented on three levels. On
[Level
1 - Regulation and amending Directive](https://eur-lex.europa.eu/eli/reg/2022/2554/oj "https://eur-lex.europa.eu/eli/reg/2022/2554/oj"), Section II, Article
6 explicitly calls out for a sound, comprehensive, well-documented
ICT risk management framework.

### Implementation steps

1. **Identify and document
   risks**: Conduct business impact analysis (BIA) to
   identify critical workloads and their dependencies. BIA
   should uncover the following:
   - **Technical risks:**
     Infrastructure failures, security breaches, data loss
   - **Operational risks:**
     Process failures, human error, third-party dependencies
   - **Compliance risks:**
     Regulatory changes, audit findings, policy violations

2. **Prioritize risks**:
   - Score each risk by likelihood and impact (typically 1-5
     scale)
   - Calculate risk priority: Likelihood × impact = risk
     score
   - Consider:
     - Financial impact (revenue loss, fines, remediation
       costs)
     - Operational impact (downtime, service degradation)
     - Reputational impact (customer trust, brand damage)
     - Compliance impact (regulatory penalties, legal
       exposure)

3. **Build mitigation
   strategies**: For each risk, document the
   following:
   - **Preventive controls:**
     What stops the risk from occurring (automation,
     redundancy, monitoring)
   - **Detective controls:**
     How you'll detect if it happens (alarms, audits, logs)
   - **Remediation measures:**
     How you'll respond (runbooks, failover procedures)
   - **Owner:** Who's
     accountable for managing this risk
   - **Timeline:** By when
     will the risk be fully mitigated
   - **Impact:** What impact
     will it have on systems and operations if the strategy
     were to be implemented

4. **Track risks over time**:
   - Use a centralized tool (for example, collaborative
     trackers)
   - Schedule regular reviews (monthly for high risks,
     quarterly for medium or low)
   - Track metrics: open risks, overdue mitigations, risk
     trend over time
   - Integrate with change management (assess new risks when
     deploying changes)

5. **Create recovery
   procedures**:
   - Document step-by-step recovery runbooks
   - Establish teams and roles related to incident management
   - Establish escalation paths and communication plans
   - Map system dependencies that are part of your recovery
     path
   - Define recovery metrics for each critical workload

6. **Maintain operational
   resilience**:
   - Test recovery procedures regularly (tabletop exercises,
     DR drills using AWS GameDays, AWS chaos engineering
     tools, AWS Skills Builder). This facilitates discovery
     of previously unknown risks.
   - Update risk register after incidents (lessons learned)
   - Conduct periodic risk assessments (at least annually)

The following is a example of what a risk register could look
like:

| Risk ID | Description            | Category  | Likelihood | Impact | Priority | Mitigation strategy | Owner    | Status | Review date |
| ------- | ---------------------- | --------- | ---------- | ------ | -------- | ------------------- | -------- | ------ | ----------- |
| R-001   | Primary Region failure | Technical | 2          | 5      | 10       | Multi-Region DR     | Ops Lead | Active | Monthly     |

Additional fields may include:

1. Expected date on which the mitigation strategy will be
   reviewed.
2. Estimated cost of maintaining the as-is state without
   mitigating the risk.
3. The impact of activating a given mitigation strategy.

The key is making risk registers a continual process rather than
a one-off document. Integrate risk review into your regular
operational cadence, and verify that high-priority risks have an
owner.

## Resources

**Related best practices:**

- [OPS01-BP06
  Evaluate tradoffs while managing benefits and risks](../operational-excellence-pillar/ops_priorities_eval_tradeoffs.md "../operational-excellence-pillar/ops_priorities_eval_tradeoffs.md")
- [OPS10-BP03
  Prioritize operational events based on business impact](../operational-excellence-pillar/ops_event_response_prioritize_events.md "../operational-excellence-pillar/ops_event_response_prioritize_events.md")
- [OPS01-BP05
  Evaluate threat landscape](../operational-excellence-pillar/ops_priorities_eval_threat_landscape.md "../operational-excellence-pillar/ops_priorities_eval_threat_landscape.md")

**Related documents:**

- [Risk
  Management](../../../whitepapers/latest/aws-caf-governance-perspective/risk-management.md "../../../whitepapers/latest/aws-caf-governance-perspective/risk-management.md")

**Related videos:**

- [AWS re:Invent 2023: Backup and Disaster Recovery Strategies for
  Increased Resilience: Leveraging AWS Services for
  Cost-Effective Business Continuity (ARC208)](https://aws.amazon.com/awstv/watch/173a403d06b/ "https://aws.amazon.com/awstv/watch/173a403d06b/")
