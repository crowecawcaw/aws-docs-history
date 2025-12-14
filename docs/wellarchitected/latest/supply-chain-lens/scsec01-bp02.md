# SCSEC01-BP02 Use cloud services to maintain security controls while scaling your supply chain environment

Using cloud security services enables organizations to implement
consistent, automated security controls that scale seamlessly with
dynamic supply chain environments. These services provide built-in
capabilities for threat detection, data protection, identity
management, and compliance monitoring across your entire supply
chain environment.

By integrating cloud security services directly into your
infrastructure as code and CI/CD pipelines, you can make sure
security controls are consistently applied from development
through production while maintaining operational agility.

This approach reduces the operational burden on security teams
while providing enhanced visibility and protection for supply
chain workloads as they scale to meet changing business demands.

**Desired outcome:** Efficient
provisioning of secure, compliance-aligned resources at scale
using AWS native services.

**Benefits**
**of establishing this best
practice:** Streamlined governance and enhanced security
through automated, consistent resource management.

**Level of risk exposed if this best
practice is not established:** Medium

## Implementation guidance

- Use cloud management and governance services like AWS Control Tower, Service Catalog, and AWS Security Hub CSPM to
  provision secure, compliance-aligned resources at scale.
- AWS Control Tower can help set up a secure multi-account
  environment following best practices for separation of
  duties and least privilege access, while Service Catalog
  allows you to create and manage pre-approved, secure IT
  service catalogs for your supply chain workloads.

### Implementation steps

1. Deploy AWS Control Tower to establish a secure
   multi-account environment with guardrails that enforce
   separation of duties and least privilege access across
   your supply chain infrastructure.
2. Create standardized, pre-approved templates in Service Catalog to enable self-service provisioning of secure
   supply chain workloads while maintaining governance
   controls.
3. Implement AWS Security Hub CSPM to gain centralized visibility
   into security findings, automate compliance checks, and
   continuously monitor security best practices across supply
   chain accounts.
4. Use AWS Artifact to access and distribute compliance
   reports, certifications, and attestations that demonstrate
   the security posture of your cloud-based supply chain to
   stakeholders and auditors.
5. Configure AWS Audit Manager to automatically collect and
   organize evidence for regulatory compliance, simplifying
   audit preparation and demonstrating adherence to industry
   standards.
6. Integrate these services with your CI/CD pipelines and
   infrastructure as code to make sure security controls
   scale automatically with your supply chain workloads and
   maintain consistency across environments.
