# Design principles

The Well-Architected Framework identifies a set of four general
design principles to facilitate good design in the cloud for
financial services workloads.

1. **Documented operational
   planning**—To define your cloud-operating model, you
   must work with internal consumers and stakeholders to set a
   common goal and strategic direction. Many organizations have
   adopted the “Three Lines of Defense” model to improve
   effectiveness of risk management:
   - At the first line of defense, operational managers are responsible for initiating
     risk and control procedures on a day-to-day basis.
   - The second line establishes various risk management and compliance functions to
     help build and/or monitor the first line-of-defense controls.
   - As the third line of defense, internal auditors provide the governing body and
     senior management with comprehensive assurance based on the highest level of empowerment and objectivity within the
     organization.
     Establishing clear roles and responsibilities across the three lines of defense is
     vital to developing an effective operating model for regulated cloud adoption, see [Three Lines of Defense](https://www.theiia.org/en/content/position-papers/2020/the-iias-three-lines-model-an-update-of-the-three-lines-of-defense/ "https://www.theiia.org/en/content/position-papers/2020/the-iias-three-lines-model-an-update-of-the-three-lines-of-defense/") from the Institute of Internal Auditors (IIA).

2. **Automated infrastructure and application
   deployment**—Automation enables you to perform and innovate quickly and scale
   security, compliance, and governance activities across your cloud environments. Financial
   services institutions that invest in automated infrastructure and application deployment are
   able to accelerate the rate of deployments and more simply embed security and governance
   best practices into their software development lifecycle.
3. **Security by design**—Financial services institutions must
   consider [Security by
   Design (SbD)](https://aws.amazon.com/compliance/security-by-design/ "https://aws.amazon.com/compliance/security-by-design/") approach to implement architectures that are pre-tested from a
   security perspective. SbD helps implement the control objectives, security baselines,
   security configurations, and audit capabilities for applications running on AWS.
   Standardized, automated, prescriptive, and repeatable design templates help accelerate the
   deployment of common use cases as well as help align with security standards (and ease the evidence
   requirements for audit) across multiple workloads. For example, to protect customer data and
   mitigate the risk of data disclosure or alteration of sensitive information by unauthorized
   parties, financial institutions need to employ encryption and carefully manage access to
   encryption keys. SbD allows you to turn on encryption for data at rest, in transit, and if
   necessary, at the application level by default.
4. **Automated governance**—Humans working with runbooks and
   checklists often lead to delays and inaccurate results. Automated governance provides a
   fast, definitive governance check for applications deployment at scale. Governance at scale
   typically addresses the following components:
   - **Account management:** Automate account provisioning and
     maintain good security when hundreds of users and business units are requesting
     cloud-based resources.
   - **Budget and cost management:** Enforce and monitor budgets
     across many accounts, workloads, and users.
   - **Security and compliance automation:** Manage security,
     risk, and compliance at scale to verify that the organization maintains compliance,
     while performing against business objectives.
