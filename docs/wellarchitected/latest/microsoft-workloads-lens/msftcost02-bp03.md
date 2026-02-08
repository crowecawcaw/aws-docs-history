# MSFTCOST02-BP03 Bring Your Own Licenses (BYOL)

If you have already invested in licenses for your Microsoft
workload, such as having enterprise licensing agreements, you can
choose to bring your own licenses to AWS and save costs on EC2.
Depending on when the licenses were acquired and the version,
Windows Server licenses can be brought to Amazon EC2 Dedicated
Hosts. Other products covered by Software Assurance and License
Mobility in the agreement, like SQL Server, can be brought to
default (shared) tenancy.

AWS License Manager provides the flexibility to convert between
Bring Your Own License (BYOL) and License Included configurations,
allowing you to optimize licensing costs based on your needs and
eligibility. This conversion capability enables you to switch
between license models without having to rebuild instances, making
it easier to adapt to changing licensing requirements or to take
advantage of different cost models. For more information on
licensing options, see the Microsoft FAQ on the AWS public page, or
contact your account team to help you engage with a Microsoft expert
on AWS to guide you through the options.

**Desired outcome:** Successfully
optimize costs and maintain compliance by leveraging existing
Microsoft licenses through BYOL implementation on AWS, while
ensuring seamless license management and flexibility to convert
between license models as needed, resulting in documented cost
savings and efficient resource utilization without service
disruption.

**Common anti-patterns:**

- Misaligned license deployment: Incorrectly deploying Windows
  Server licenses on shared tenancy instead of required Dedicated
  Hosts, or placing SQL Server with software assurance on
  Dedicated Hosts when it could run on shared tenancy, resulting
  in unnecessary costs and compliance violations.
- Missed conversion opportunities: Failing to utilize AWS License Manager's conversion capabilities between BYOL and license
  included configurations, leading to unnecessary instance
  rebuilds and downtime when licensing requirements change or cost
  optimization opportunities arise.
- Independent license decision-making: Making BYOL decisions
  without consulting AWS account teams or Microsoft licensing
  experts, resulting in missed opportunities for cost savings,
  improper license mobility implementation, and potential
  compliance issues with enterprise agreements.

**Benefits of establishing this best
practice:**

- By leveraging existing Microsoft licenses through BYOL,
  organizations can significantly reduce EC2 instance costs
  compared to License Included options. This maximizes the value
  of existing enterprise licensing agreements and allows for more
  efficient allocation of IT budgets.
- AWS License Manager's ability to convert between BYOL and
  License Included configurations provides unprecedented
  flexibility. This allows organizations to adapt quickly to
  changing business needs, licensing requirements, or cost
  structures without service interruptions or time-consuming
  instance rebuilds.
- Properly implementing BYOL with guidance from AWS and Microsoft
  experts ensures compliance with complex licensing terms. This
  minimizes the risk of unexpected costs or penalties during
  audits, while also ensuring that licenses are correctly applied
  to the right types of instances (for example, Windows Server on
  Dedicated Hosts, SQL Server on shared tenancy when applicable).

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

Start with a comprehensive audit of existing Microsoft licenses,
then engage AWS account teams for expert guidance on BYOL
implementation. Deploy AWS License Manager to track and manage
licenses, ensuring proper instance placement (Dedicated Hosts
versus shared tenancy) based on license terms. Regularly review
and optimize configurations, maintaining thorough documentation
for compliance purposes.

### Implementation steps

1. Audit existing Microsoft licenses and enterprise agreements
2. Consult AWS and Microsoft experts for BYOL eligibility and
   options
3. Set up AWS License Manager for tracking and conversion
   capabilities
4. Deploy licenses correctly (for example, Windows Server on
   Dedicated Hosts, SQL Server on shared tenancy)
5. Establish regular review process for ongoing optimization
   and compliance

## Resources

**Related documents:**

- [Amazon Web Services and Microsoft FAQs](https://aws.amazon.com/windows/faq/ "https://aws.amazon.com/windows/faq/")
- [Bring
  licenses for Windows and SQL Server workloads](../../../prescriptive-guidance/latest/optimize-costs-microsoft-workloads/byol-ded-hosts.md "../../../prescriptive-guidance/latest/optimize-costs-microsoft-workloads/byol-ded-hosts.md")

**Related tools:**

- [What
  is AWS License Manager?](../../../license-manager/latest/userguide/license-manager.md "../../../license-manager/latest/userguide/license-manager.md")
