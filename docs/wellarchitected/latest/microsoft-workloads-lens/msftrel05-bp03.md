# MSFTREL05-BP03 Implement self-healing procedures

Establish automated remediation capabilities that can detect,
diagnose, and resolve common issues in Microsoft workloads without
human intervention. Self-healing procedures reduce mean time to
recovery (MTTR) and minimize the impact of transient failures on
business operations.

**Desired outcome:** Implement
automated self-healing procedures to proactively detect and
remediate common issues in Microsoft workloads, providing for
minimal downtime through automated instance recovery, health-based
reboots, and configuration management.

**Common anti-patterns:**

- Waiting for human operators to detect and respond to system
  failures during off-hours.
- Implementing reactive fixes without addressing root causes
  through automation.
- Creating complex automation that requires extensive maintenance
  and troubleshooting.
- Over-automating without proper testing, leading to cascading
  failures.

**Benefits of establishing this best
practice:**

- Significantly reduced mean time to recovery (MTTR) for common
  failure scenarios.
- Improved availability during off-hours when human operators may
  not be immediately available.
- Consistent and predictable response to system issues, reducing
  human error.
- Enhanced operational efficiency by freeing teams to focus on
  strategic initiatives rather than routine maintenance.
- Improved adherence to service level agreements (SLAs) through
  automated response capabilities.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

When implementing self-healing procedures for Microsoft workloads,
consider the balance between automation sophistication and
operational complexity. Start with well-understood, low-risk
scenarios before expanding to more complex remediation actions.

**Key considerations for
customers**

- **Scope and prioritization:**
  Begin by identifying the most common and impactful failure
  scenarios in your Microsoft workloads. Focus on issues that
  occur frequently, have clear remediation steps, and pose
  minimal risk when automated. Examples include service
  restarts, disk space cleanup, and basic connectivity issues.
- **Testing and validation:**
  Thoroughly test automated remediation actions in
  non-production environments. Establish clear success criteria
  and rollback procedures. Consider implementing gradual
  rollouts and canary deployments for automation changes.
- **Monitoring and alerting
  strategy:** Design monitoring that can distinguish
  between symptoms and root causes. Avoid creating automation
  that treats symptoms without addressing underlying issues, as
  this can mask systemic problems.
- **Impact scope control:**
  Implement safeguards to avoid automated actions from causing
  widespread impact. Use circuit breakers, rate limiting, and
  approval workflows for high-risk remediation actions.
- **Documentation and knowledge
  transfer:** Maintain clear documentation of automated
  procedures, including trigger conditions, actions taken, and
  escalation paths. Verify that team members understand when and
  how automation will intervene.

### Implementation steps

1. Analyze historical incidents to identify the most common and
   impactful issues. Prioritize scenarios with clear
   remediation steps and low automation risk.
2. Configure Amazon CloudWatch alarms and custom metrics to
   detect failure conditions. Verify that monitoring can
   differentiate between transient issues and persistent
   problems.
3. Create AWS Systems Manager Automation documents for each
   remediation scenario. Test thoroughly in non-production
   environments with various failure conditions.
4. Start with simple, low-risk actions like service restarts.
   Gradually expand to more complex scenarios like instance
   replacement or database failover as confidence builds.
5. Configure specific Microsoft workload automation:
   - Deploy auto-recovery for EC2 instances running Windows
     Server.
   - Set up automated instance reboots based on health checks
     for IIS and other Windows services.
   - Configure automatic failover for SQL Server Always On
     Availability Groups.
   - Implement automated patch management through AWS Systems Manager Patch Manager.
   - Use State Manager for configuration drift correction on
     Windows systems.
   - Active Directory and DNS automation:
     - Automatically restart Active Directory Domain
       Services when authentication failures exceed
       thresholds.
     - Reset DNS service when name resolution failures are
       detected.
     - Trigger domain controller health checks and
       automatic promotion of backup DCs.

   - IIS and web application remediation:
     - Restart application pools when memory usage exceeds
       defined limits.
     - Clear IIS logs when disk space is low.
     - Reset worker processes experiencing high CPU
       utilization.
     - Automatically recycle application pools based on
       request failure rates.

   - SQL Server specific automation:
     - Restart SQL Server services when connection timeouts
       increase.
     - Automatically shrink transaction logs when they
       exceed size thresholds.
     - Trigger index maintenance when fragmentation levels
       are high.
     - Reset SQL Server Agent jobs that fail due to
       transient issues.

   - Windows service and process management:
     - Restart Windows services that have stopped
       unexpectedly.
     - Kill and restart hung processes based on CPU or
       memory thresholds.
     - Clear Windows event logs when they reach capacity
       limits.
     - Reset network adapters when connectivity issues are
       detected.

   - File system and storage remediation:
     - Automatically clean temporary files when disk space
       is low.
     - Compress old log files to free up storage space.
     - Move archived data to lower-cost storage tiers.
     - Reset file permissions when access issues are
       detected.

   - Performance and resource optimization:
     - Automatically scale EC2 instances based on
       performance metrics.
     - Clear memory caches when system performance
       degrades.
     - Restart services consuming excessive resources.
     - Trigger garbage collection for .NET applications
       experiencing memory leaks.

6. Monitor automation effectiveness and adjust thresholds based
   on real-world performance. Implement logging and metrics to
   track automation success rates.

## Resources

**Related documents:**

- [AWS Systems Manager Automation](../../../systems-manager/latest/userguide/systems-manager-automation.md "../../../systems-manager/latest/userguide/systems-manager-automation.md")
- [Working
  with SSM Agent on EC2 instances for Windows Server](../../../systems-manager/latest/userguide/ssm-agent-windows.md "../../../systems-manager/latest/userguide/ssm-agent-windows.md")
- [Patching
  applications released by Microsoft on Windows Server](../../../systems-manager/latest/userguide/patch-manager-patching-windows-applications.md "../../../systems-manager/latest/userguide/patch-manager-patching-windows-applications.md")
- [Use
  AWS Systems Manager to enable CloudWatch memory metrics for
  Windows Server Amazon EC2 instances](https://aws.amazon.com/blogs/modernizing-with-aws/use-aws-systems-manager-to-enable-cloudwatch-memory-metrics-for-windows-server-amazon-ec2-instances/ "https://aws.amazon.com/blogs/modernizing-with-aws/use-aws-systems-manager-to-enable-cloudwatch-memory-metrics-for-windows-server-amazon-ec2-instances/")

**Related tools:**

- [AWS Systems Manager](https://aws.amazon.com/systems-manager/ "https://aws.amazon.com/systems-manager/")
- [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/ "https://aws.amazon.com/cloudwatch/")
