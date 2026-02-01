# DSOPS01-BP03 Implement compliance training and

awareness

Compliance-trained software professionals can design and build
systems that adhere to regulations (for example, GDPR, HIPAA, and
PCI-DSS). Without awareness, even well-intentioned technical
decisions can lead to vulnerabilities or solutions that don't meet
regulatory requirements, exposing organizations to potential risk.

**Desired outcome:** Software
professionals are equipped with knowledge and skills required to
consistently design, develop, and maintain systems that meet
compliance requirements.

**Common anti-patterns:**

- Generic compliance training without context or applicability.
- Focusing on compliance training completion rates rather than
  effectiveness.
- Failing to update training and guidance when regulations change.
- Creating siloed compliance knowledge within specialized teams.
- Lack of opportunities to practice compliance measures in a
  hands-on setting, making it harder to apply design principles
  and best practices in real-world scenarios.

**Benefits of establishing this best
practice:**

- Improved security posture across systems and services.
- Reduced need for late-stage remediation or redesigns.
- Reduced risk of violations and associated penalties.
- Fosters accountability for security and privacy by default.
- Increased customer trust through demonstrable regulatory
  adherence and security practices.
- More efficient development cycles by addressing compliance
  requirements early.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Develop a structured, role-specific program combining foundational
training, hands-on practice, and continuous reinforcement. Align
content with organizational risk profiles, integrate compliance
into development workflows, and use automated tooling to address
regulatory needs in real-world scenarios.

### Implementation steps

1. **Assess**: Baseline your
   learning needs.
   - Conduct surveys to determine current understanding of
     regulatory requirements across teams. Consult with
     subject matter experts to identify knowledge and skills
     gaps.
   - Identify the regulatory standards that apply to your
     organization.
     - Use existing documentation such as business impact
       analysis (BIA), data protection impact analysis
       (DPIA) documents, and risk registers.
     - Use existing policy documentation such as security,
       data handling, privacy, data classification, and
       data retention policies.
     - Get read-only access to production or
       production-like environments to study existing
       compliance related controls.

   - Map requirements to specific technical roles and
     responsibilities.

2. **Define success criteria**:
   Training programs must lead to successful outcomes (for
   example, a 25-50% reduction in compliance violations within
   six months or a 20-30% improvement in developer confidence
   when dealing with specific compliance standards).
3. **Develop content**: Create
   training content and reusable assets that cover identified
   regulatory standards and address skills and knowledge gaps.
   - Create role-specific learning paths for targeting
     specific technical and operational roles.
   - Focus on secure architecture and design patterns,
     augmented with data protection and data privacy-related
     best practices.
   - Cover secure coding standards, safe data handling, and
     incident response procedures.
   - Cover reporting procedures (for example, security
     incident reporting, available escalation paths, key
     points of contact, and whistleblower helplines).
   - Cover AWS services and independent software vendor (ISV)
     products related to compliance and security.
   - Create searchable knowledge bases of compliance
     requirements. Consider incorporating LLM-powered search
     augmented with
     [Amazon
     Bedrock Knowledge Bases](https://aws.amazon.com/bedrock/knowledge-bases/ "https://aws.amazon.com/bedrock/knowledge-bases/") and
     [AWS MCP Servers](https://awslabs.github.io/mcp/ "https://awslabs.github.io/mcp/").
   - Create a library of reusable reference architectures,
     prescriptive guidance, solution accelerators, and code
     examples that developers can readily apply.
     [AWS Architecture Center](https://aws.amazon.com/architecture/ "https://aws.amazon.com/architecture/") and
     [AWS Samples](https://github.com/orgs/aws-samples/repositories?q=compliance "https://github.com/orgs/aws-samples/repositories?q=compliance") provide a starting point.

4. **Deliver**: Provide regular
   training sessions using a combination of talks, discussions,
   and hands-on exercises.
   - Deploy interactive e-learning modules to deliver
     training content.
   - Conduct hands-on workshops for practical application of
     skills (for example, breach response drills).
   - Arrange expert-led sessions for complex topics.

5. **Apply**: Incorporate
   compliance considerations into existing design and
   development processes.
   - Deploy compliance and vulnerability checking linters and
     IDE plugins.
   - Apply a compliance checklist when evaluating
     architecture decisions and during code reviews.
   - Incorporate automated compliance validation into
     Continuous Integration and Continuous Deployment (CI/CD)
     pipelines.
   - Establish office hours with subject matter experts.

6. **Track, refine, and
   reinforce**: Regularly monitor and evaluate the
   effectiveness of training programs.
   - Track violations in code reviews and security testing.
   - Track audit outcomes and incident trends to refine
     training content.
   - Measure effectiveness through knowledge assessments.
   - Share updates on evolving standards through newsletters
     or other team messaging channels.
   - Reinforce training content through code reviews and
     security testing.

7. **Scale up**: Once you
   achieve your initial success metrics, scale the program.
   - Deploy learning management systems (LMSs) across the
     organization.
   - Drive professional certification and accreditation
     programs. Consider providing subscriptions to online
     learning solutions to enable your colleagues to prepare.
   - Consider setting up moderated team channels so that
     teams can discuss and share best practices and
     challenges.

## Resources

**Related best practices:**

- [OPS03-BP06
  Team members are encouraged to maintain and grow their skill
  sets](../../../en_us/wellarchitected/latest/operational-excellence-pillar/ops_org_culture_team_enc_learn.md "../../../en_us/wellarchitected/latest/operational-excellence-pillar/ops_org_culture_team_enc_learn.md")
- [OPS11-BP04
  Perform knowledge management](../../../en_us/wellarchitected/latest/operational-excellence-pillar/ops_evolve_ops_knowledge_management.md "../../../en_us/wellarchitected/latest/operational-excellence-pillar/ops_evolve_ops_knowledge_management.md")
- [SEC11-BP01
  Train for application security](../security-pillar/sec_appsec_train_for_application_security.md "../security-pillar/sec_appsec_train_for_application_security.md")

**Related resources:**

- [Comprehensive
  resource for AWS compliance offerings](https://aws.amazon.com/compliance/ "https://aws.amazon.com/compliance/")
- [Get
  started on security training with content built by AWS
  experts](https://aws.amazon.com/training/learn-about/security/ "https://aws.amazon.com/training/learn-about/security/")
- [Automated
  compliance checks against industry standards](https://aws.amazon.com/security-hub/ "https://aws.amazon.com/security-hub/")
- [Policy-as-code
  evaluation tool](https://github.com/aws-cloudformation/cloudformation-guard "https://github.com/aws-cloudformation/cloudformation-guard")
- [Resource
  compliance monitoring and remediation](https://aws.amazon.com/config/ "https://aws.amazon.com/config/")
- [Continuous
  audit evidence collection](https://aws.amazon.com/audit-manager/ "https://aws.amazon.com/audit-manager/")
- [Compliance-focused
  reference deployments](https://aws.amazon.com/quickstart/architecture/compliance-hipaa/ "https://aws.amazon.com/quickstart/architecture/compliance-hipaa/")
- [Set up
  and govern compliant multi-account environments](https://aws.amazon.com/controltower/ "https://aws.amazon.com/controltower/")
