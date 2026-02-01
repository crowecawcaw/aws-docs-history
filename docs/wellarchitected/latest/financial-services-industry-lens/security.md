# Security

The security pillar focuses on the ability to protect information,
systems, and assets through risk assessments and mitigation
strategies, while also delivering business value to the
organization. In addition to the regulations that apply to any
business, financial institutions are challenged with industry-
specific requirements such as frequsently-changing regulations and
their variation by region. Institutions that operate in more than
one country or Region must also meet different requirements in
different places. Financial institutions (FI) are historically a
frequent target of security incidents, both because of the assets
they maintain and their fundamental role in the daily functioning of
a modern society. FIs have to comply with rules and laws around the
protection of personal and financial information. The continuity of
their operations depends directly on the security resilience they
put in place.

With the adoption of generative AI technologies, financial
institutions face additional security challenges in protecting
sensitive financial data, preventing unauthorized model access,
and ensuring AI system outputs comply with regulatory
requirements. FIs must implement comprehensive security controls
across AI components including models, data stores, and endpoints
while preventing potential risks such as prompt injection, data
poisoning, or harmful model responses that could impact customer
data or financial operations.

## Design principles

In addition to the
[design
principles](../security-pillar/security.md "../security-pillar/security.md") found in the security pillar of the
AWS Well-Architected Framework, the following security design
principles can help you improve the security posture of your
financial services workloads:

- **Security by design:**
  Financial services institutions must consider a Security by
  Design (SbD) approach to implement architectures that are
  pre-tested from a security perspective. SbD helps implement
  the control objectives, security baselines, security
  configurations, and audit capabilities for applications running
  on AWS. Standardized, automated, prescriptive, and repeatable
  design templates help accelerate the deployment of common use
  cases as well as help align with security standards across
  multiple workloads. For example, to protect

customer data and mitigate the risk of data disclosure or
alteration of sensitive information by unauthorized parties,
financial institutions need to employ encryption and carefully
manage access to encryption keys. SbD allows you to turn on
encryption for data at rest, in transit, and if necessary, at
the application level by default. For generative AI workloads,
SbD must include implementing comprehensive access controls
across AI components, securing data and communication flows, and
establishing guardrails to govern how AI systems interact with
data and execute workflows.

- **Identify regulatory requirements to be
  implemented:** Regulators expect financial services
  institutions to define security objectives for workloads and
  implement policies that help achieve those objectives.
  Regulators may also impose their own external requirements on
  specific workloads and expect institutions to monitor and
  report on their compliance with these requirements, with
  penalties for breaching them. Those requirements must be
  translated into security control objectives that are
  sustainable over time but flexible to adapt as regulations
  evolve. With generative AI adoption, financial institutions
  must consider additional regulatory requirements around model
  governance, data protection, and AI system outputs. This
  includes implementing controls to prevent harmful or biased
  responses, verifying the explainability and auditability of
  decisions, and protecting sensitive financial data used in AI
  training and inference.
- **Automated infrastructure and
  application deployment:** Automation helps companies
  to perform and innovate quickly and scale security,
  compliance, and governance activities across their cloud
  environments. Financial services institutions that invest in
  automated infrastructure and application deployment can
  accelerate the rate of deployments and embed security and
  governance best practices into their software development
  lifecycle. For generative AI systems, automation should extend
  to response validation, prompt security, and model access
  controls to ensure consistent security across AI workloads.
- **Automated governance:**
  Manual governance processes that rely on runbooks and
  checklists often lead to delays and inaccurate results.
  Automated governance provides a fast, definitive governance
  check for application deployments at scale. Governance at
  scale typically addresses the following components:
  - **Account management:**
    Automate account provisioning and maintain good security
    when hundreds of users and business units are requesting
    cloud-based resources.
  - **Budget and cost
    management:** Enforce and monitor budgets across
    many accounts, workloads, and users.
  - **Security and compliance
    automation:** Manage security, risk, and
    compliance at scale to keep the organization compliant
    while achieving business objectives.
  - **AI system governance:**
    Implement automated guardrails and monitoring for model
    responses, data access patterns, and prompt security to
    maintain control over AI system behaviors while enabling
    innovation.

- **Agent authentication and
  authorization:** Implement fine-grained permission
  models for agent actions with principle of least privilege.
- **Agent action boundaries:**
  Define clear security boundaries for what actions agents can
  perform.
- **Agent chain-of-thought
  security:** Implement security controls for agent
  reasoning processes.
- **Tool access controls:**
  Establish governance for which tools agents can access and
  under what conditions.
- **Agent prompt injection
  protection:** Implement safeguards against
  manipulation of agent instructions or goals.

## Definitions

Security in the financial services industry is composed of the
following best practice areas.

- Security foundations
- Identity and access management
- Detection
- Infrastructure protection
- Data protection
- Incident response
- Application security

Before you architect any workload, you need to put in place
practices that influence security. You should control who can do
what. In addition, you want to be able to identify security
incidents, protect your systems and services, and maintain the
confidentiality and integrity of data through data protection. You
should have a well-defined and practiced process for responding to
security incidents. These tools and techniques are important
because they support objectives such as preventing financial loss
or complying with regulatory obligations.
