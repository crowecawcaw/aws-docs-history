

# Understanding cost optimization strategies
<a name="coh-optimization-strategies"></a>

Cost Optimization Hub groups your recommendations into the following cost optimization strategies:

**Purchase Savings Plans**  
Purchase Compute, EC2 instance, and SageMaker Savings Plans.

**Purchase reservations**  
Purchase EC2, Amazon RDS, OpenSearch, Amazon Redshift, ElastiCache, MemoryDB, and DynamoDB reservations.

**Stop**  
Stop idle or unused resources to save up to 100% of the resource cost.

**Delete**  
Delete idle or unused resources to save up to 100% of the resource cost.

**Scale in**  
Scale in idle or unused resources to save on resource costs.

**Rightsize**  
Move to a smaller EC2 instance type of the same CPU architecture.

**Upgrade**  
Move to a later generation product, such as moving from Amazon EBS io1 volume type to io2.

**Migrate to Graviton**  
Move from x86 to Graviton to save costs.

The following table shows the full mapping of recommended actions and resource type.




- **Purchase Savings Plans**
  - **Resource type:** Compute Savings Plans / **Conditions:** All / **Implementation effort:** Very low / **Resource restart needed:** No / **Rollback possible:** No
  - **Resource type:** EC2 Instance Savings Plans / **Conditions:** All / **Implementation effort:** Very low / **Resource restart needed:** No / **Rollback possible:** No
  - **Resource type:** SageMaker Savings Plans / **Conditions:** All / **Implementation effort:** Very low / **Resource restart needed:** No / **Rollback possible:** No

- **Purchase reservations**
  - **Resource type:** EC2 Reserved Instances / **Conditions:** All / **Implementation effort:** Very low / **Resource restart needed:** No / **Rollback possible:** Yes
  - **Resource type:** Amazon RDS Reserved Instances / **Conditions:** All / **Implementation effort:** Very low / **Resource restart needed:** No / **Rollback possible:** No
  - **Resource type:** Amazon Redshift reserved nodes / **Conditions:** All / **Implementation effort:** Very low / **Resource restart needed:** No / **Rollback possible:** No
  - **Resource type:** OpenSearch Reserved Instances / **Conditions:** All / **Implementation effort:** Very low / **Resource restart needed:** No / **Rollback possible:** No
  - **Resource type:** ElastiCache reserved nodes / **Conditions:** All / **Implementation effort:** Very low / **Resource restart needed:** No / **Rollback possible:** No
  - **Resource type:** MemoryDB reserved instances / **Conditions:** All / **Implementation effort:** Very low / **Resource restart needed:** No / **Rollback possible:** No
  - **Resource type:** DynamoDB reserved capacity / **Conditions:** All / **Implementation effort:** Very low / **Resource restart needed:** No / **Rollback possible:** No

- **Stop**
  - **Resource type:** EC2 instance / **Conditions:** All / **Implementation effort:** Low / **Resource restart needed:** No / **Rollback possible:** Yes
  - **Resource type:** RDS DB instance / **Conditions:** RDS MySQL and RDS PostgreSQL engines only / **Implementation effort:** Low / **Resource restart needed:** Yes / **Rollback possible:** Yes

- **Delete**
  - **Resource type:** EBS volume / **Conditions:** All / **Implementation effort:** Low / **Resource restart needed:** No / **Rollback possible:** No
  - **Resource type:** Amazon ECS service / **Conditions:** All / **Implementation effort:** Low / **Resource restart needed:** No / **Rollback possible:** No
  - **Resource type:** RDS DB instance / **Conditions:** Aurora MySQL and Aurora PostgreSQL engines only / **Implementation effort:** Low / **Resource restart needed:** No / **Rollback possible:** Yes

- **Scale in**
  - **Resource type:** EC2 Auto Scaling group
  - **Conditions:** All
  - **Implementation effort:** Low
  - **Resource restart needed:** No
  - **Rollback possible:** No

- **Rightsize**
  - **Resource type:** EC2 instance (standalone) / **Conditions:** No hypervisor change / **Implementation effort:** Medium / **Resource restart needed:** Yes / **Rollback possible:** Yes
  - **Resource type:** EC2 instance (standalone) / **Conditions:** With hypervisor change / **Implementation effort:** High / **Resource restart needed:** Yes / **Rollback possible:** Yes
  - **Resource type:** EC2 Auto Scaling group / **Conditions:** All / **Implementation effort:** Medium / **Resource restart needed:** Yes / **Rollback possible:** Yes
  - **Resource type:** EBS volume / **Conditions:** All / **Implementation effort:** Low / **Resource restart needed:** No / **Rollback possible:** Yes
  - **Resource type:** Lambda function / **Conditions:** All / **Implementation effort:** Low / **Resource restart needed:** No / **Rollback possible:** Yes
  - **Resource type:** Amazon ECS service / **Conditions:** All / **Implementation effort:** Low / **Resource restart needed:** Yes / **Rollback possible:** Yes
  - **Resource type:** RDS DB instance / **Conditions:** All / **Implementation effort:** Medium / **Resource restart needed:** Yes / **Rollback possible:** Yes
  - **Resource type:** RDS DB instance storage / **Conditions:** All / **Implementation effort:** Low / **Resource restart needed:** No / **Rollback possible:** Yes
  - **Resource type:** Aurora DB cluster storage / **Conditions:** All / **Implementation effort:** Low / **Resource restart needed:** No / **Rollback possible:** Yes

- **Upgrade**
  - **Resource type:** EC2 instance (standalone) / **Conditions:** No hypervisor change / **Implementation effort:** Medium / **Resource restart needed:** Yes / **Rollback possible:** Yes
  - **Resource type:** EC2 instance (standalone) / **Conditions:** With hypervisor change / **Implementation effort:** High / **Resource restart needed:** Yes / **Rollback possible:** Yes
  - **Resource type:** EC2 Auto Scaling group / **Conditions:** All / **Implementation effort:** Medium / **Resource restart needed:** Yes / **Rollback possible:** Yes
  - **Resource type:** EBS volume / **Conditions:** All / **Implementation effort:** Low / **Resource restart needed:** No / **Rollback possible:** Yes
  - **Resource type:** RDS DB instance / **Conditions:** All / **Implementation effort:** Medium / **Resource restart needed:** Yes / **Rollback possible:** Yes
  - **Resource type:** RDS DB instance storage / **Conditions:** All / **Implementation effort:** Low / **Resource restart needed:** No / **Rollback possible:** Yes

- **Migrate to Graviton**
  - **Resource type:** EC2 instance (standalone) / **Conditions:** With Graviton-compatible inferred workload type / **Implementation effort:** High / **Resource restart needed:** Yes / **Rollback possible:** Yes
  - **Resource type:** EC2 instance (standalone) / **Conditions:** Without Graviton-compatible inferred workload type / **Implementation effort:** Very high / **Resource restart needed:** Yes / **Rollback possible:** Yes
  - **Resource type:** EC2 Auto Scaling group / **Conditions:** With Graviton-compatible inferred workload type / **Implementation effort:** High / **Resource restart needed:** Yes / **Rollback possible:** Yes
  - **Resource type:** EC2 Auto Scaling group / **Conditions:** Without Graviton-compatible inferred workload type / **Implementation effort:** Very high / **Resource restart needed:** Yes / **Rollback possible:** Yes
  - **Resource type:** RDS DB instance / **Conditions:** All / **Implementation effort:** Medium / **Resource restart needed:** Yes / **Rollback possible:** Yes

