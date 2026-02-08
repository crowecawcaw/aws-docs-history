# MSFTCOST08-BP01 Refactor to cross-platform .NET and move to

Linux

Migrating .NET Framework applications to .NET 8 or later enables
cross-platform deployment, improved security, and better
performance. This modernization allows applications to run on Linux
systems, leverage cloud-native features, and benefit from the latest
optimizations, resulting in more efficient and maintainable systems.

**Desired outcome:** Aim to achieve
reduced licensing costs, improved performance, and enhanced
security. The modernized applications run efficiently on Linux
environments, including AWS Graviton processors, while leveraging
the latest .NET features and cloud-native capabilities. This
transformation results in a more cost-effective, scalable, and
maintainable application portfolio that aligns with modern cloud
architecture principles.

**Common anti-patterns:**

- Continuing to rely on Windows-specific dependencies and COM
  components without evaluating modern alternatives, making the
  migration to Linux impossible and perpetuating technical debt
  and higher operational costs.
- Attempting to run portions of the application on Linux while
  keeping critical components on Windows servers, creating a
  complex hybrid architecture that increases operational overhead
  and negates the cost benefits of the migration while introducing
  potential compatibility issues.

**Benefits of establishing this best
practice:**

- Moving to Linux eliminates Windows licensing costs while
  enabling the use of cost-effective infrastructure options like
  AWS Graviton processors, resulting in significant operational
  cost savings and improved performance metrics through modern
  .NET optimizations.
- Cross-platform .NET applications can be deployed across diverse
  environments using containerization technologies, enabling
  efficient CI/CD pipelines, simplified scaling strategies, and
  better resource utilization in cloud environments, leading to
  improved application reliability and reduced maintenance
  overhead.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Begin with an AWS Transform-assisted assessment to identify
Windows dependencies, then implement an incremental migration
strategy focusing on high-impact components first. Utilize
automated refactoring tools for conversion to cross-platform .NET,
containerize the application, and establish comprehensive testing
protocols to ensure successful deployment on Linux environments
while maintaining application performance and reliability.

### Implementation steps

1. Conduct application assessment using AWS Transform to
   identify Windows dependencies and migration challenges
2. Develop a phased migration plan, prioritizing components for
   maximum cost-benefit impact
3. Refactor code to cross-platform .NET using AWS Transform's
   AI-powered tools and manual adjustments
4. Containerize the application and implement a robust testing
   strategy for Linux environments
5. Deploy the refactored application to Linux servers,
   including AWS Graviton instances, and monitor performance

## Resources

**Related documents:**

- [Refactor
  to modern .NET and move to Linux](../../../prescriptive-guidance/latest/optimize-costs-microsoft-workloads/net-refactor-linux.md "../../../prescriptive-guidance/latest/optimize-costs-microsoft-workloads/net-refactor-linux.md")

**Related tools:**

- [Modernizing
  .NET with AWS Transform](../../../transform/latest/userguide/dotnet.md "../../../transform/latest/userguide/dotnet.md")
