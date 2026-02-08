# MSFTSEC01-BP03 Develop a comprehensive software update

strategy

Microsoft regularly releases scheduled security updates and
emergency patches to address vulnerabilities. Stay informed about
the latest security advisories from relevant vendors. It's crucial
to keep your Microsoft application and its underlying components
up-to-date with the latest security fixes on a regular schedule to
avoid security gaps. Develop a plan for applying critical emergency
patches when released. Consider implementing automated processes to
streamline this update process, which keeps your Microsoft
environment secure and current with minimal manual intervention.

**Desired outcome:** Establish an
automated and systematic approach to patch management that verifies
Microsoft workloads receive timely security updates while
maintaining system stability and minimizing downtime through proper
testing and deployment procedures.

**Common anti-patterns:**

- Applying patches without proper testing or staging procedures,
  potentially introducing system instability or breaking critical
  applications during production deployments.
- Delaying security updates for extended periods due to fear of
  system disruption, leaving systems vulnerable to known exploits
  and security threats that could have been avoided.
- Managing patches manually across multiple systems without
  automation, leading to inconsistent patch levels, missed
  updates, and increased administrative overhead that doesn't
  scale effectively.

**Benefits of establishing this best
practice:**

- Reduced security vulnerabilities through timely application of
  security patches and updates, minimizing the window of exposure
  to known threats and exploits targeting Microsoft technologies.
- Improved operational efficiency through automated patch
  management processes that reduce manual effort, maintain
  consistency across environments, and provide better visibility
  into patch compliance status.
- Enhanced system stability and reliability through structured
  testing and deployment procedures that validate patches before
  production deployment, reducing the risk of patch-related
  outages or application failures.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Developing a comprehensive software update strategy requires
balancing security needs with operational stability. Implement a
structured approach that includes automated patch management,
testing procedures, and emergency response capabilities.

Use AWS Systems Manager Patch Manager to automate routine updates
while maintaining control over critical systems through approval
processes and maintenance windows. For Windows instances in
private subnets without internet connectivity, consider
implementing Windows Server Update Services (WSUS) in public
subnets to provide local patch distribution while still using
Systems Manager for orchestration and compliance monitoring.

### Implementation steps

1. Establish patch management policies that define update
   schedules, testing requirements, and approval processes for
   different types of systems and environments.
2. Configure AWS Systems Manager Patch Manager to automate
   patch deployment with appropriate maintenance windows and
   approval workflows.
3. Create staging environments that mirror production systems
   for testing patches before deployment to critical workloads.
4. Set up patch groups and baselines in Systems Manager to
   manage different update requirements for various system
   types and criticality levels.
5. Implement monitoring and alerting for patch compliance
   status using AWS Systems Manager Compliance and Amazon CloudWatch dashboards.
6. Establish emergency patch procedures for critical security
   vulnerabilities that require immediate attention outside of
   normal maintenance windows.
7. Configure automated rollback procedures and system snapshots
   before patch deployment to enable quick recovery if issues
   occur.
8. Create regular reporting mechanisms to track patch
   adherence, update success rates, and identify systems that
   require attention.

## Resources

**Related documents:**

- [AWS Systems Manager Patch Manager](../../../systems-manager/latest/userguide/patch-manager.md "../../../systems-manager/latest/userguide/patch-manager.md")
- [Microsoft
  Security Update Guide](https://msrc.microsoft.com/update-guide/ "https://msrc.microsoft.com/update-guide/")

**Related tools:**

- [AWS Systems Manager](../../../systems-manager/latest/userguide/what-is-systems-manager.md "../../../systems-manager/latest/userguide/what-is-systems-manager.md")
- [Windows
  Server Update Services (WSUS)](https://docs.microsoft.com/en-us/windows-server/administration/windows-server-update-services/get-started/windows-server-update-services-wsus "https://docs.microsoft.com/en-us/windows-server/administration/windows-server-update-services/get-started/windows-server-update-services-wsus")
- [Microsoft
  Update Catalog](https://www.catalog.update.microsoft.com/ "https://www.catalog.update.microsoft.com/")
