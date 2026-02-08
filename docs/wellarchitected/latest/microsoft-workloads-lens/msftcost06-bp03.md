# MSFTCOST06-BP03 Use self-managed Active Directory on Amazon EC2

Depending on the requirements, your Microsoft workload may require
the use of a self-managed Active Directory deployment (either a new
forest or extending an existing one). Deploying Active Directory
domains controllers to Amazon EC2 is fairly simple. Domain
controllers are usually good candidates to run on Amazon EC2
burstable instance family, saving on compute costs. Make sure to
evaluate the capacity planning recommendations provided by Microsoft
to address your workload requirements.

**Desired outcome:** Deploy
self-managed Active Directory domain controllers on Amazon EC2,
leveraging burstable instance families where appropriate to optimize
costs. The implementation will follow Microsoft's capacity planning
guidelines and support either new or extended Active Directory
forests based on organizational requirements, ensuring a robust and
cost-effective directory service solution.

**Common anti-patterns:**

- Deploying Active Directory domain controllers on oversized EC2
  instances, such as using high-performance compute-optimized
  instances when not required. This leads to unnecessary costs and
  underutilized resources, contradicting the goal of cost
  optimization.
- Implementing Active Directory on EC2 without properly evaluating
  Microsoft's capacity planning recommendations. This can result
  in performance issues, scalability problems, and potential
  service disruptions, ultimately affecting the reliability of the
  Microsoft workload and potentially increasing long-term costs
  due to necessary remediation efforts.

**Benefits of establishing this best
practice:**

- Cost-effective directory services through optimized EC2 instance
  selection and burstable computing, reducing operational expenses
  while maintaining performance requirements.
- Enhanced control and flexibility in deploying and managing
  Active Directory infrastructure, supporting both new
  implementations and extensions of existing directory services.

**Level of risk exposed if this best practice
is not established:** Medium

## Implementation guidance

To implement self-managed Active Directory on Amazon EC2, begin by
assessing your workload requirements and consulting Microsoft's
capacity planning recommendations. Choose appropriate EC2 instance
types, favoring burstable instances where suitable. Deploy at
least two domain controllers across different Availability Zones
for high availability. Use Amazon EBS volumes for storage,
ensuring proper backups and snapshots. Implement security best
practices, including network segmentation with VPCs and security
groups. Finally, establish monitoring and alerting using Amazon CloudWatch to maintain optimal performance and availability of
your Active Directory infrastructure.

### Implementation steps

1. Size and deploy EC2 instances based on Microsoft's capacity
   planning guidelines, utilizing burstable instance families
   where appropriate, and ensure distribution across multiple
   Availability Zones for high availability.
2. Configure networking components including VPC design,
   security groups, and DHCP options to support Active
   Directory requirements and establish secure communication
   paths.
3. Install and configure Active Directory Domain Services,
   establishing either a new forest or extending an existing
   one, following Microsoft's recommended configurations and
   security baselines.
4. Implement monitoring and backup solutions using Amazon CloudWatch and automated EBS snapshots to maintain service
   health and enable disaster recovery capabilities.

## Resources

**Related documents:**

- [Self-managed
  Active Directory on Amazon EC2](../../../prescriptive-guidance/latest/optimize-costs-microsoft-workloads/active-directory-self-managed.md "../../../prescriptive-guidance/latest/optimize-costs-microsoft-workloads/active-directory-self-managed.md")
