# Operational excellence

The operational excellence pillar allows financial services institutions to focus on
managing risks associated with operating workloads in the cloud, satisfying regulatory
requirements, and becoming more agile by automating the operation and management of
traditionally error-prone manual processes.

## Design principles

In addition to the design principles in the AWS Well-Architected Framework whitepaper,
the following design principles can help you achieve operational excellence for your financial
services workloads:

- **Review applicable compliance and regulatory requirements:**
  Financial services institutions must be aware of all applicable regulatory and compliance
  obligations for their use of cloud services, and take appropriate steps to meet those
  obligations.
- **Evaluate legacy policies to determine relevance in the
  cloud:** Financial services institutions often have a robust set of operating
  policies that govern behaviors and decision-making for activities such as disaster
  recovery planning, capacity management, security and compliance guardrails, and data
  backup and recovery. Cloud services support new technologies, architectural patterns, and
  automations which are not possible or practical for on-premises environments. Policies
  which were originally created for on-premise environments should be revisited from a cloud
  perspective, rather than assumed to be necessary and relevant. Change control, for
  example, should focus on changes to the architecture and configuration of the deployment
  pipeline, which cannot be automatically tested and reverted in the event of a failure.
- **Report service disruptions to downstream stakeholders and regulatory
  bodies:** Financial services institutions are required to communicate service
  disruptions, operational events, and failures to downstream stakeholders and regulatory
  bodies. They should continually monitor their workloads in the cloud and conduct root
  cause analysis (RCA) as an exercise in understanding the events and circumstances that led
  to unexpected results, as well as mitigation efforts put in place to help prevent
  recurrence.
- **Establish generative AI-specific governance and oversight
  mechanisms:** Financial institutions must implement specialized governance
  frameworks for generative AI workloads that address model risk management, output
  validation, hallucination detection, and ethical AI considerations. This includes
  establishing clear accountability for generative AI model selection, deployment, and
  ongoing monitoring in production environments.
- **Implement continuous model performance monitoring:** Unlike
  traditional applications, generative AI models can exhibit performance drift, bias
  amplification, and unexpected behaviors over time. Establish continuous monitoring of
  model outputs, accuracy metrics, and alignment with intended use cases to ensure
  consistent and reliable performance in regulated environments.
- **Maintain human-in-the-loop validation and control:**
  Financial institutions must ensure appropriate human oversight and intervention
  capabilities for generative AI systems, particularly for decisions that impact customers,
  regulatory compliance, or financial outcomes. Financial services workloads should be
  continually reviewed and prioritized regarding their risk impact to the overall business
  (for example, based on their reputational, ﬁnancial, or regulatory impact). Clear roles
  and responsibilities should be deﬁned in the organization to understand the risks involved
  in the delivery of business value using cloud services.

Financial services workloads should be continually reviewed and prioritized with regard
to their risk impact to the overall business (for example, based on their reputational,
financial, or regulatory impact). Clear roles and responsibilities should be defined in the
organization to understand the risks involved in the delivery of business value using cloud
services.

- **Implement a risk management process:** Financial
  institutions have adopted a [Three Lines of Defense model](https://www.iansresearch.com/resources/all-blogs/post/security-blog/2022/01/13/how-to-apply-the-three-lines-of-defense "https://www.iansresearch.com/resources/all-blogs/post/security-blog/2022/01/13/how-to-apply-the-three-lines-of-defense") for risk management:
  - **First line of defense:** Operational managers perform
    risk and control procedures on a day-to-day basis.
  - **Second line of defense:** Various risk management and
    compliance functions help build and monitor the first line of defense controls.
  - **Third line of defense:** Internal auditors provide the
    governing body and senior management with comprehensive assurance based on the highest
    level of empowerment and objectivity within the organization.

- **Agent governance framework:** Establish dedicated
  governance structures for autonomous agents with clear boundaries, permissions, and
  escalation paths.
- **Agent monitoring:** Implement specialized monitoring
  for agent activities, decisions, and outcomes with human oversight thresholds.
- **Agent lifecycle management:** Define processes for
  agent deployment, versioning, and retirement.
- **Incident response for agents:** Create specific
  runbooks for incidents involving autonomous agents, including containment
  procedures.
- **Agent feedback loops:** Establish mechanisms to capture
  and incorporate feedback on agent decisions and actions.

## Definitions

Operational excellence in the financial services industry is composed of the following
best practice areas:

1. [Organization](../operational-excellence-pillar/organization.md "../operational-excellence-pillar/organization.md")
2. [Prepare](../operational-excellence-pillar/prepare.md "../operational-excellence-pillar/prepare.md")
3. [Operate](../operational-excellence-pillar/operate.md "../operational-excellence-pillar/operate.md")
4. [Evolve](../operational-excellence-pillar/evolve.md "../operational-excellence-pillar/evolve.md")
