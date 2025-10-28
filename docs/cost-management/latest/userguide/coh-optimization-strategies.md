# Understanding cost optimization strategies

Cost Optimization Hub groups your recommendations into the following cost optimization strategies:

**Purchase Savings Plans**

Purchase Compute, EC2 instance, and SageMaker Savings Plans.

**Purchase reservations**

Purchase EC2, Amazon RDS, OpenSearch, Amazon Redshift, ElastiCache, MemoryDB, and
DynamoDB reservations.

**Stop**

Stop idle or unused resources to save up to 100% of the resource cost.

**Delete**

Delete idle or unused resources to save up to 100% of the resource cost.

**Scale in**

Scale in idle or unused resources to save on resource costs.

**Rightsize**

Move to a smaller EC2 instance type of the same CPU architecture.

**Upgrade**

Move to a later generation product, such as moving from Amazon EBS io1 volume type to
io2.

**Migrate to Graviton**

Move from x86 to Graviton to save costs.

The following table shows the full mapping of recommended actions and resource type.

| Action                        | Resource type                                      | Conditions                                      | Implementation effort | Resource restart needed | Rollback possible |
| ----------------------------- | -------------------------------------------------- | ----------------------------------------------- | --------------------- | ----------------------- | ----------------- | ------------------------------ | ----------------------------------------------- | -------- | --- | --- |
| Purchase Savings Plans        | Compute Savings Plans                              | All                                             | Very low              | No                      | No                |
| EC2 Instance Savings Plans    | All                                                | Very low                                        | No                    | No                      |                   | SageMaker Savings Plans        | All                                             | Very low | No  | No  |
| Purchase reservations         | EC2 Reserved Instances                             | All                                             | Very low              | No                      | Yes               |
| Amazon RDS Reserved Instances | All                                                | Very low                                        | No                    | No                      |                   | Amazon Redshift reserved nodes | All                                             | Very low | No  | No  |
| OpenSearch Reserved Instances | All                                                | Very low                                        | No                    | No                      |                   | ElastiCache reserved nodes     | All                                             | Very low | No  | No  |
| MemoryDB reserved instances   | All                                                | Very low                                        | No                    | No                      |                   | DynamoDB reserved capacity     | All                                             | Very low | No  | No  |
| Stop                          | EC2 instance                                       | All                                             | Low                   | No                      | Yes               |
| RDS DB instance               | RDS MySQL and RDS PostgreSQL engines only          | Low                                             | Yes                   | Yes                     |
| Delete                        | EBS volume                                         | All                                             | Low                   | No                      | No                |
| Amazon ECS service            | All                                                | Low                                             | No                    | No                      |                   | RDS DB instance                | Aurora MySQL and Aurora PostgreSQL engines only | Low      | No  | Yes |
| Scale in                      | EC2 Auto Scaling group                             | All                                             | Low                   | No                      | No                |
| Rightsize                     | EC2 instance (standalone)                          | No hypervisor change                            | Medium                | Yes                     | Yes               |
| EC2 instance (standalone)     | With hypervisor change                             | High                                            | Yes                   | Yes                     |                   | EC2 Auto Scaling group         | All                                             | Medium   | Yes | Yes |
| EBS volume                    | All                                                | Low                                             | No                    | Yes                     |                   | Lambda function                | All                                             | Low      | No  | Yes |
| Amazon ECS service            | All                                                | Low                                             | Yes                   | Yes                     |                   | RDS DB instance                | All                                             | Medium   | Yes | Yes |
| RDS DB instance storage       | All                                                | Low                                             | No                    | Yes                     |                   | Aurora DB cluster storage      | All                                             | Low      | No  | Yes |
| Upgrade                       | EC2 instance (standalone)                          | No hypervisor change                            | Medium                | Yes                     | Yes               |
| EC2 instance (standalone)     | With hypervisor change                             | High                                            | Yes                   | Yes                     |                   | EC2 Auto Scaling group         | All                                             | Medium   | Yes | Yes |
| EBS volume                    | All                                                | Low                                             | No                    | Yes                     |                   | RDS DB instance                | All                                             | Medium   | Yes | Yes |
| RDS DB instance storage       | All                                                | Low                                             | No                    | Yes                     |
| Migrate to Graviton           | EC2 instance (standalone)                          | With Graviton-compatible inferred workload type | High                  | Yes                     | Yes               |
| EC2 instance (standalone)     | Without Graviton-compatible inferred workload type | Very high                                       | Yes                   | Yes                     |                   | EC2 Auto Scaling group         | With Graviton-compatible inferred workload type | High     | Yes | Yes |
| EC2 Auto Scaling group        | Without Graviton-compatible inferred workload type | Very high                                       | Yes                   | Yes                     |                   | RDS DB instance                | All                                             | Medium   | Yes | Yes |
