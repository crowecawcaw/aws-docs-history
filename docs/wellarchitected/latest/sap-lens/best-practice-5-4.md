# Best Practice 5.4 – Create a strategy

for managing security controls

Having evaluated business requirements based on data classification, create a strategy
that balances the security controls of your broader organization with the application
guides and open standards available. Take into consideration the implementation effort and
acknowledge risk.

**Suggestion 5.4.1 - Identify a matrix to assess risk**

A range of risk management frameworks are available for specific industries and
geographies. Understand the risk framework adopted by your organization and how this
applies to managing risks related to your SAP workloads.

- AWS Documentation: [Example Risk Matrix](../security-pillar/governance.md "../security-pillar/governance.md")
- AWS Blog: [Scaling
  a governance, risk, and compliance program for the cloud](https://aws.amazon.com/blogs/security/scaling-a-governance-risk-and-compliance-program-for-the-cloud/ "https://aws.amazon.com/blogs/security/scaling-a-governance-risk-and-compliance-program-for-the-cloud/")
- [NIST Risk
  Management Framework](https://www.nist.gov/cyberframework/risk-management-framework "https://www.nist.gov/cyberframework/risk-management-framework")

**Suggestion 5.4.2 - Evaluate security and compliance requirements
mandated by your organization**

Consult with your cloud center of excellence, legal team, compliance teams, and
managed service provider to understand their security baseline and how controls are
enforced. Evaluate whether all of these controls can easily be applied to your SAP
workload and identify areas that might require an exception, for example allow and deny
lists for AWS services, inbound and outbound traffic flow and access
restrictions.

**Suggestion 5.4.3 - Identify and agree on a process for
exceptions**

In some situations, software, business, or support requirements for SAP might require
you to deviate from the standard security patterns. Identify a process to agree and
document any exceptions with a change advisory board or security design authority and
reassess the process on a regular basis.

AWS Documentation: [Change Management in the Cloud](../../../whitepapers/latest/change-management-in-the-cloud/change-management-in-the-cloud.md "../../../whitepapers/latest/change-management-in-the-cloud/change-management-in-the-cloud.md")
