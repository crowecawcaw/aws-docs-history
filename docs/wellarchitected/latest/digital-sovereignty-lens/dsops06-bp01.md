# DSOPS06-BP01 Track regulatory changes across operating

Regions

Track, analyze, and adapt to regulatory changes across jurisdictions to maintain adherence
and reduce risk.

**Desired outcome**: A resilient, compliance-aligned program that
proactively identifies, assesses, and implements regulatory changes.

**Common anti-patterns:**

- Missing clear ownership and processes for regulatory change management.
- Focusing only on global standards while ignoring region-specific regulations.
- Relying solely on external consultants without building internal expertise.
- Addressing compliance issues reactively instead of proactively.

**Benefits of establishing this best practice:**

- Reduced risk through early identification of regulatory changes.
- Better decision-making for regional expansion and service adoption.
- Increased customer and partner trust through improved regulatory adherence.
- Lower costs by avoiding last-minute remediation.
- Improved alignment between legal, compliance, and technical teams.

**Level of risk exposed if this best practice is not established:**
Medium

## Implementation guidance

Considering setting up a regulatory intelligence function to track new regulations,
amendments to existing laws, and regulatory guidance from authorities across jurisdictions.
Automate compliance checks and evidence collection with AWS Config, AWS Audit Manager, and
AWS Security Hub. Track regulatory changes with third-party governance risk and compliance (GRC)
tools. Adhere to regulatory requirements through regular testing, training, and documentation
updates.

### Implementation steps

1. **Establish a regulatory intelligence function:** Create a
   team of multi-disciplinary experts responsible for monitoring regulatory changes across
   geographic regions and jurisdictions where you operate. Monitor changes to globally
   recognized standards such as ISO, PCI, local privacy laws and cybersecurity standards. A
   regulatory intelligence function should also clearly articulate the impact of impending
   changes on existing business operations and technology solutions. Include the following:
   - Compliance officer with relevant certifications (such as certified information
     privacy professional (CIPP), certified information systems security professional
     (CISSP), or certified in risk and information systems control (CRISC))
   - Legal counsel specializing in cybersecurity and data privacy legislation
   - Cloud architects and security consultants with compliance expertise and
     certifications (such as AWS Certified Security - Specialty or Certified Cloud
     Security Professional (CCSP))
   - Regional compliance specialists for each geographic Region or jurisdiction
     where you operate

2. **Establish partnerships with local legal experts:**
   Partner with local legal firms or compliance consultants in each operating region to
   gain expert insights on regulatory changes. When selecting partners, look for firms
   with:
   - Proven expertise in technology and data protection regulations
   - Active participation in regulatory consultations and industry working groups
   - Established relationships with local regulatory authorities
   - Track record of advising on cloud compliance matters

3. **Work with local regulatory authorities:** Engage with
   regulators and join consultation exercises. Use [regulatory sandboxes](https://ico.org.uk/for-organisations/advice-and-services/regulatory-sandbox/the-guide-to-the-sandbox/ "https://ico.org.uk/for-organisations/advice-and-services/regulatory-sandbox/the-guide-to-the-sandbox/") where available to prepare for new regulations.
4. **Use AWS services and Marketplace offerings:** Integrate
   AWS compliance resources into your tracking system. Use [AWS Artifact](../../../artifact/latest/ug/what-is-aws-artifact.md "../../../artifact/latest/ug/what-is-aws-artifact.md") to access
   AWS compliance reports and agreements, which are updated as AWS achieves new
   certifications and attestations. While AWS Artifact provides compliance documentation,
   you'll need to supplement it with external sources to track regulatory changes
   themselves. Explore [governance, risk, and
   compliance (GRC) solutions](https://aws.amazon.com/marketplace/solutions/security/governance-risk-compliance/ "https://aws.amazon.com/marketplace/solutions/security/governance-risk-compliance/") in AWS Marketplace.
5. **Implement GRC software:** Evaluate leading GRC products
   that complement AWS services. Solutions like [OneTrust](https://my.onetrust.com/s/article/UUID-5fea572c-9591-7d8a-9588-e5074715161f?language=en_US&topicId=0TORO0000003R6v4AE "https://my.onetrust.com/s/article/UUID-5fea572c-9591-7d8a-9588-e5074715161f?language=en_US&topicId=0TORO0000003R6v4AE") integrate with AWS to collect compliance evidence and establish
   traceability between requirements and controls.
6. **Update training curriculum:** Maintain training velocity
   and update your training courses regularly to align with changing regulations.
7. **Establish regular review cycles:**
   - Conduct quarterly reviews of compliance policies, control implementations, and
     workload configurations to verify they remain aligned with current regulations.
   - Watch for new regulations and regulatory changes related to cross-border data
     transfers and new requirements related to data residency.
   - Establish regulatory change management metrics and KPIs, such as:
     - Time from regulatory change announcement to implementation completion
     - Number of regulatory changes identified and assessed per quarter

   - Update documentation and controls as regulations evolve.

This approach combines technology, expertise, and processes to improve regulatory
adherence in a complex and dynamic regulatory environment.

## Resources

**Related best practices:**

- [OPS01-BP03
  Evaluate governance requirements](../operational-excellence-pillar/ops_priorities_governance_reqs.md "../operational-excellence-pillar/ops_priorities_governance_reqs.md")
- [OPS01-BP04
  Evaluate compliance requirements](../operational-excellence-pillar/ops_priorities_compliance_reqs.md "../operational-excellence-pillar/ops_priorities_compliance_reqs.md")
- [OPS07-BP02 Maintain a consistent review of operational readiness](../../../en_us/wellarchitected/latest/operational-excellence-pillar/ops_ready_to_support_const_orr.md "../../../en_us/wellarchitected/latest/operational-excellence-pillar/ops_ready_to_support_const_orr.md")
- [REL08-BP04 Deploy using immutable infrastructure](../../../en_us/wellarchitected/latest/reliability-pillar/rel_tracking_change_management_immutable_infrastructure.md "../../../en_us/wellarchitected/latest/reliability-pillar/rel_tracking_change_management_immutable_infrastructure.md")
- [REL08-BP05 Deploy changes with automation](../../../en_us/wellarchitected/latest/reliability-pillar/rel_tracking_change_management_automated_changemgmt.md "../../../en_us/wellarchitected/latest/reliability-pillar/rel_tracking_change_management_automated_changemgmt.md")
- [OPS07-BP05 Make informed decisions to deploy systems and changes](../operational-excellence-pillar/ops_ready_to_support_informed_deploy_decisions.md "../operational-excellence-pillar/ops_ready_to_support_informed_deploy_decisions.md")

**Related documents:**

- [Amazon Web Services: Risk and Compliance](../../../whitepapers/latest/aws-risk-and-compliance/welcome.md "../../../whitepapers/latest/aws-risk-and-compliance/welcome.md")
- [Operational Readiness Reviews (ORR)](../operational-readiness-reviews/wa-operational-readiness-reviews.md "../operational-readiness-reviews/wa-operational-readiness-reviews.md")

**Related videos:**

- [AWS re:Inforce 2025 - Best
  practices for managing governance, risk, and compliance globally (GRC301)](https://www.youtube.com/watch?v=pCNIpnb9tvE "https://www.youtube.com/watch?v=pCNIpnb9tvE")
- [AWS re:Inforce 2024 -
  Automation in action: Strategies for risk mitigation (GRC301)](https://www.youtube.com/watch?v=gbo-Z01NTc8 "https://www.youtube.com/watch?v=gbo-Z01NTc8")
- [AWS Summit ANZ 2021 - Build an
  effective governance and compliance strategy with AWS Audit Manager](https://www.youtube.com/watch?v=FZ4u0Lzo6ZM "https://www.youtube.com/watch?v=FZ4u0Lzo6ZM")
- [AWS re:Inforce 2023 - Using
  AI/ML to scale governance, risk management, and audits (GRC222)](https://www.youtube.com/watch?v=dwLFJxBonKo "https://www.youtube.com/watch?v=dwLFJxBonKo")
