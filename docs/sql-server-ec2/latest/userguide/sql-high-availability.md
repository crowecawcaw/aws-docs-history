

# Amazon EC2 High Availability for SQL Server on Amazon EC2
<a name="sql-high-availability"></a>

Amazon EC2 High Availability for SQL Server (SQL HA) allows you to configure Amazon EC2 instances running license-included SQL Server as part of a HA cluster to reduce licensing costs. This feature identifies the SQL Server standby (also known as passive) instances in your SQL HA deployments and waives SQL Server licensing fees for them, allowing you to pay only Windows rates for these standby instances while maintaining your HA configuration.

## Supported SQL Server High Availability deployments
<a name="high-availability-support"></a>

SQL HA supports the following two SQL Server High Availability deployment types:
+ Always On Availability Groups
+ Always On Failover Cluster Instances

For Always On Availability Groups, SQL HA identifies primary and secondary (also known as standby or passive) replicas and waives the SQL Server licenses on the secondary replicas (Amazon EC2 instances) that are not actively serving read traffic. For Failover Cluster Instances, SQL HA recognizes which instances are active and which are standing by for failover scenarios and waives the SQL Server licenses on the standby instances. For more information about the SQL HA configurations, see [Deploy SQL Server on Amazon EC2](create-sql-server-on-ec2-instance.md)

## Considerations and requirements
<a name="sql-high-availability-consids"></a>
+ SQL HA supports two or more Amazon EC2 instances (also known as nodes) per SQL Server HA cluster. Every node in the cluster must be enabled for SQL HA standby detection, and all nodes must be in the same AWS account and Region.
+ All of the nodes in a SQL Server HA cluster must belong to the same set of HA clusters. If any node participates in an additional availability group or failover cluster instance that the other nodes are not part of, then none of the nodes in that deployment receive the SQL Server license waiver.
+ At least one node in the SQL Server HA cluster must be active. If SQL HA classifies every node as standby, no node receives the SQL Server license waiver.
+ An active instance can cover one or more standby instances, as long as its vCPU count is equal to or greater than the total vCPUs of the standby instances that it covers. For example, an active instance with 8 vCPUs can cover two standby instances with 4 vCPUs each.
+ vCPUs from different active instances can't be combined to cover a single standby instance. For example, two active instances with 8 vCPUs each can't cover a standby instance with 16 vCPUs.
+ SQL HA saves license costs for SQL Server license-included Amazon EC2 instances only. For more information, see [SQL Server licensing options](sql-server-on-ec2-licensing.md#sql-server-on-ec2-licensing-options-included).
+ Cross-Region deployments are not supported.
+ The SQL Server standby node must meet requirements to receive the license savings, including: 1. Does not serve incoming traffic; 2. Does not run active SQL Server workloads; 3. Is not a readable secondary (except master, msdb, tempdb, or model databases); 4. For Always On Availability Groups, there is no standalone database running outside of the Availability Group.
+ SQL HA supports SQL Server (Standard and Enterprise Editions) 2017 and later on Windows Server 2019 and later.
+ Windows PowerShell must be 5.1 or above.
+ Amazon EC2 Reserved Instances are not supported by SQL HA. If you are using Reserved Instances, discounts may not be applied to these instances in the same payer account. We recommend using Savings Plans instead to benefit from both SQL HA license savings and Savings Plans compute cost savings. For more information, see the [Savings Plans User Guide](https://docs.aws.amazon.com/savingsplans/latest/userguide/what-is-savings-plans.html).
+ This feature may be terminated at any time, in which case AWS will provide you with as much prior notice as is reasonably practicable under the circumstances.

## Prerequisites
<a name="sql-high-availability-prerequisites"></a>

To get the license savings for your SQL HA workload, your environment must meet several requirements:
+ You have SQL Server license-included HA workloads on Amazon EC2. You can use AWS Launch Wizard to simplify the SQL Server deployment on Amazon EC2. For more information, see [AWS Launch Wizard for SQL Server](https://docs.aws.amazon.com/launchwizard/latest/userguide/launch-wizard-sql.html).
+ AWS Systems Manager Agent (SSM Agent) must be installed and running on the instances in the SQL HA deployment. For more information, see [Working with SSM Agent](https://docs.aws.amazon.com/systems-manager/latest/userguide/ssm-agent.html).
+ You must attach the **AWSEC2SqlHaInstancePolicy** managed policy to your instance role or use a custom role with the required permissions for the Amazon EC2 to access your instances, including permissions for AWS Systems Manager to run commands, access to AWS Secrets Manager for retrieving SQL Server credentials, and Amazon EC2 permissions to read instance metadata.
+ By default, AWS Systems Manager uses the built-in `[NT AUTHORITY\SYSTEM]` user to access SQL Server HA metadata. You will need to store secrets in AWS Secrets Manager only when your security policies have restricted or disabled the `[NT AUTHORITY\SYSTEM]` account.
+ Network connectivity allows AWS Systems Manager commands to reach your instances.