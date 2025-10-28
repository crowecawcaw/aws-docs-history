# Design principles

Well-Architected migration design principles are a set of
considerations used as the basis for a well-architected migrated
workload. The design principles are high-level guidance that we
recommend you follow for a successful migration.

1. **Create a clear vision for the
   journey**: Define the business goal of the migration
   (_why_ migrate?) and think more about
   _how_ you transform both your business and
   technology while migrating to AWS, not just about moving your
   workloads. The why and transformation goals are the key
   principles that help you define everything else during the
   migration journey.
2. **Get leadership support early in the
   project**: Executive sponsorship is critical as strong
   organizational alignment is required to make timely decisions
   and resolve potential challenges and tradeoffs. Consider forming
   a dedicated team, usually known as [CCoE](../../../whitepapers/latest/public-sector-cloud-transformation/building-a-cloud-center-of-excellence-ccoe-to-transform-the-entire-enterprise.md "../../../whitepapers/latest/public-sector-cloud-transformation/building-a-cloud-center-of-excellence-ccoe-to-transform-the-entire-enterprise.md")
   (for more detail, see [What
   is a cloud center of excellence and why should organization
   create one?](https://aws.amazon.com/blogs/publicsector/what-is-cloud-center-excellence-why-should-your-organization-create-one/ "https://aws.amazon.com/blogs/publicsector/what-is-cloud-center-excellence-why-should-your-organization-create-one/"))
3. **Understand where you are moving
   to**: Learn about AWS and its differences from
   traditional on-premises data centers (or other clouds). This is
   critical to the migration's success. Define your [AWS accounts strategy](../../../whitepapers/latest/organizing-your-aws-environment/organizing-your-aws-environment.md "../../../whitepapers/latest/organizing-your-aws-environment/organizing-your-aws-environment.md") and leverage [AWS Control Tower](https://aws.amazon.com/controltower/ "https://aws.amazon.com/controltower/") and AWS Organizations to build
   landing zones to provide ongoing account management, governance,
   and implementation of AWS best practices.
4. **Define the migration scope:**
   Determine what to migrate and, based on that, define the
   migration strategy (how to migrate).
5. **Know your applications:**
   Define what good looks like when moving to AWS. Based on that,
   choose the right
   [migration
   strategy](../../../prescriptive-guidance/latest/large-migration-guide/migration-strategies.md "../../../prescriptive-guidance/latest/large-migration-guide/migration-strategies.md") for each based on the [7
   Rs](../../../prescriptive-guidance/latest/migration-retiring-applications/apg-gloss.md#apg.migration.terms "../../../prescriptive-guidance/latest/migration-retiring-applications/apg-gloss.md#apg.migration.terms") approach (for more detail, see [Determining
   the R type for migration](../../../prescriptive-guidance/latest/application-portfolio-assessment-guide/prioritization-and-migration-strategy.md#migration-r-type "../../../prescriptive-guidance/latest/application-portfolio-assessment-guide/prioritization-and-migration-strategy.md#migration-r-type")).
6. **Get the application owners and teams
   buy-in early**: Understand application dependencies,
   both technical and business, internal, and external.
7. **Understand your application
   requirements**: For example, performance, utilization,
   resiliency, security, compliance, and operations. Optimize
   (right-size) to create more efficient and elastic workloads
   after the migration.
8. **Align with applicable governance,
   regulatory and compliance frameworks**: Incorporate
   security best practices as part of your workload migration
   strategy.
9. **Maintain your operations during the
   migration to the Cloud**: Consider your current
   operations while you have a hybrid environment and once you are
   completely on cloud. Plan your monitoring, backup, and lifecycle
   management at level required by your organization for production
   workloads.
10. **Create the migration plans**:
    Split migration into smaller units (migration waves), where each
    unit could be an application or a group of applications. Move
    each unit, test, validate and repeat. Create or adapt
    operational runbooks, seeking to automate the process of early
    migration waves (mobilize) and apply these runbooks to scale the
    migration of each subsequent wave.
