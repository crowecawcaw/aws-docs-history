# Design principles

In addition to the [design principles](../security-pillar/security.md "../security-pillar/security.md") found in the security pillar of the AWS Well-Architected
Framework, the following security design principles can help you improve the security
posture of your manufacturing data workloads:

- **Security by design**: Manufacturers must consider a
  security by design (SbD) approach to implement architectures that are pre-tested from a
  security perspective. SbD helps implement the control objectives, security baselines,
  security configurations, and audit capabilities for applications running on AWS.
  Standardized, automated, prescriptive, and repeatable design templates help accelerate
  the deployment of common use cases as well as help align with security standards across
  multiple workloads. For example, to protect customer data and mitigate the risk of data
  disclosure or alteration of sensitive information by unauthorized parties, financial
  institutions need to employ encryption and carefully manage access to encryption keys.
  You can use SbD to turn on encryption for data at rest, in transit, and if necessary, at
  the application level by default.
- **Identify regulatory requirements to be implemented**:
  Regulators expect manufacturers to define security objectives for workloads and
  implement policies that help achieve those objectives. Regulators may also impose their
  own external requirements on specific workloads and expect institutions to monitor and
  report on their compliance with these requirements, with penalties for breaching them.
  Those requirements must be translated into security control objectives that are
  sustainable over time but flexible to adapt as regulations evolve.
- **Automated infrastructure and application
  deployment:** Automation helps companies perform and innovate quickly and scale
  security, compliance, and governance activities across their cloud environments.
  Manufacturers that invest in automated infrastructure and application deployment can
  accelerate the rate of deployments and embed security and governance best practices into
  their software development lifecycle.
- **Governance at scale:** Manual governance processes that
  rely on runbooks and checklists can lead to delays and inaccurate results. Automated
  governance provides a fast, definitive governance check for application deployments at
  scale. Governance at scale typically encompasses several key components:
  - Automating account provisioning to maintain strong security across numerous
    users and business units requesting cloud resources.
  - Enforcing and monitoring budgets across multiple accounts, workloads, and users
    for effective budget and cost management.
  - Managing security, risk, and compliance through automation to help your
    organization improve compliance while supporting business objectives.

- **Security concepts to handle customer information:**
  Manufacturing data protection requires fine-grained access controls at both data source
  and asset levels within AWS. All data must be encrypted at rest and in transit while
  following the principle of least privilege for role-based access. A multi-account
  strategy isolates different manufacturing environments, implementing both preventive and
  detective controls. Secure connectivity between manufacturing facilities and AWS is
  maintained through AWS Direct Connect with a Transit Account architecture for
  centralized security management.

![ADD ALTERNATE TEXT HERE for people using assistive technology.](/images/wellarchitected/latest/modern-industrial-data-technology-lens/images/image10.emf)
Security in the manufacturing industry is composed of the following best practice
areas.

- Security foundations
- Identity and access management
- Detection
- Infrastructure protection
- Data protection
- Incident response
- Application security
  Before you architect a workload, you need to put in place practices that influence
  security. You should control who can do what. In addition, you want to be able to identify
  security incidents, protect your systems and services, and maintain the confidentiality and
  integrity of data through data protection. You should have a well-defined and practiced
  process for responding to security incidents. These tools and techniques are important
  because they support objectives such as preventing financial loss or complying with
  regulatory obligations. Refer to AWS Well Architected Framework for the cloud security
  framework before adopting the manufacturing security practices.
