# AWS resources supported by Compute Optimizer

This chapter outlines the AWS resources that Compute Optimizer generates recommendations for. It also provides you with the specific resource types supported by Compute Optimizer.

AWS Compute Optimizer generates recommendations for the following AWS resources:

- **Amazon Elastic Compute Cloud (Amazon EC2) instances**

Compute Optimizer generates recommendations for many Amazon EC2 instance types. For more information about the specific
instance types that Compute Optimizer supports, see [Supported Amazon EC2 instance types](#supported-ec2-instances "#supported-ec2-instances").

- **Amazon EC2 Auto Scaling groups**

Compute Optimizer generates recommendations for EC2 Auto Scaling groups. For more information, see [Supported Amazon EC2 Auto Scaling groups](#supported-asg "#supported-asg").

- **Amazon Elastic Block Store (Amazon EBS) volumes**

Compute Optimizer generates recommendations for various EBS volume types. For more information about the specific
EBS volume types that Compute Optimizer supports, see [Supported Amazon EBS volume types](#supported-ebs-volumes "#supported-ebs-volumes").

- **AWS Lambda functions**

Compute Optimizer generates memory size recommendations for Lambda functions that meet specific requirements. For more
information, see [Lambda function requirements](requirements.md#requirements-lambda-functions "requirements.md#requirements-lambda-functions").

- **Amazon Elastic Container Service (Amazon ECS) services on AWS Fargate**

Compute Optimizer generates recommendations for Amazon ECS services on Fargate that meet specific requirements. For more
information, see [Requirements for Amazon ECS services on Fargate](requirements.md#requirements-ecs-fargate "requirements.md#requirements-ecs-fargate").

- **Commercial software licenses**

Compute Optimizer generates license recommendations for Microsoft SQL Servers on Amazon EC2 that meet specific requirements. For more
information, see [Commercial software license requirements](requirements.md#requirements-license "requirements.md#requirements-license").

- **Amazon Aurora and Amazon Relational Database Service (Amazon RDS) databases**

Compute Optimizer generates Aurora and RDS DB instances, RDS DB instance storage, and Aurora DB cluster recommendations for RDS for MySQL, RDS for PostgreSQL, and
Amazon Aurora databases. For more information about the specific Amazon RDS resources supported by Compute Optimizer, see [Supported Amazon Aurora and RDS databases](#supported-rds "#supported-rds").

- **Amazon NAT Gateway**

Compute Optimizer generates idle recommendations for NAT Gateway. For more information, see [Viewing idle resource recommendations](view-idle-recommendations.md "view-idle-recommendations.md").

###### Note

In order to generate recommendations for each resource, the resources must meet Compute Optimizer's metric and
resource-specific requirements. For a list of the requiremtents for each resource, see [Resource requirements](requirements.md "requirements.md").

###### Topics

- [Supported Amazon EC2 instance types](#supported-ec2-instances "#supported-ec2-instances")
- [Supported Amazon EC2 Auto Scaling groups](#supported-asg "#supported-asg")
- [Supported Amazon EBS volume types](#supported-ebs-volumes "#supported-ebs-volumes")
- [Supported Amazon Aurora and RDS databases](#supported-rds "#supported-rds")
- [Additional resources](#supported-add-resources "#supported-add-resources")

## Supported Amazon EC2 instance types

Compute Optimizer generates recommendations for the instance types listed in this section.
The following table lists the EC2 instance types that are supported by Compute Optimizer.

| Instance series                           | Instance family |
| ----------------------------------------- | --------------- | ------ | ------ | ------- | ------- | ------- | ------- | ------- | -------- | --------- | --------- | --------- | --- | ---- | ----- | ---- | ----- | ---- | ---- | --- | -------- | --- | -------- | ---- | -------- | --- | -------- |
| \*_C_<br>• – Compute optimized            | C1              | C3     | C4     | C5      | C5a     | C5ad    | C5d     | C5n     | C6a      | C6g       | C6gd      | C6gn      | C6i | C6in | C6id  | C7a  | C7g   | C7gd | C7gn | C7i | C7i-flex | C8g | C8gd     | C8gn |
| \*_D_<br>• – Dense storage                | D2              | D3     | D3en   |
| \*_G_<br>• – Graphics intensive           | G4dn            | G5g    | G5     | G6      | Gr6     | G6e     |
| \*_Hpc_<br>• – High performance computing | H1              | Hpc6a  | Hpc6id | Hpc7a   | Hpc7g   |
| \*_I_<br>• – Storage optimized            | I2              | I3     | I3en   | I4g     | I4i     | I7ie    | I8g     | Im4gn   | Is4gen   | I8ge      |
| \*_M_<br>• – General purpose              | M1              | M2     | M3     | M4      | M5      | M5a     | M5ad    | M5d     | M5dn     | M5n       | M5zn      | M6a       | M6g | M6gd | M6i   | M6id | M6idn | M6in | M7a  | M7g | M7gd     | M7i | M7i-flex | M8g  | M8gd     | M8i | M8i-flex |
| \*_P_<br>• – GPU accelerated              | P3              | P4     | P4d    | P4de    | P5      | P5e     | P5en    |
| \*_R_<br>• – Memory optimized             | R3              | R4     | R5     | R5a     | R5ad    | R5b     | R5d     | R5dn    | R5n      | R6a       | R6g       | R6gd      | R6i | R6id | R6idn | R6in | R7a   | R7g  | R7gd | R7i | R7iz     | R8g | R8gd     | R8i  | R8i-flex |
| \*_T_<br>• – Burstable performance        | T1              | T2     | T3     | T3a     | T4g     |
| \*_U_<br>• – High memory                  | U-3tb1          | U-6tb1 | U-9tb1 | U-12tb1 | U-18tb1 | U-24tb1 | U7i-6tb | U7i-8tb | U7i-12tb | U7in-16tb | U7in-24tb | U7in-32tb |
| \*_X_<br>• – Memory intensive             | X1              | X1e    | X2gd   | X2idn   | X2iedn  | X2iezn  | X8g     |
| \*_Z_<br>• – High memory                  | z1d             |

###### Note

- If an EC2 instance isn't listed, then it isn't supported by Compute Optimizer.
- Compute Optimizer doesn't generate EC2 rightsizing recommendations for Spot Instances.

## Supported Amazon EC2 Auto Scaling groups

Compute Optimizer generates rightsizing and idle recommendations for Amazon EC2 Auto Scaling groups. This section outlines what Compute Optimizer supports for both types of recommendations.

### Rightsizing recommendations

Compute Optimizer supports rightsizing recommendations for EC2 Auto Scaling groups that have the following:

- Single EC2 instance types
- Mixed EC2 instance types
- One or multiple scaling policies based on CPU utilization:
  - Target tracking
  - Predictive scaling
  - Simple scaling
  - Step scaling

- Scheduled scaling policies
- No scaling policy

###### Note

Compute Optimizer doesn't support rightsizing recommendations for EC2 Auto Scaling groups that have the following:

- EC2 instance types that aren’t [supported by Compute Optimizer](supported-resources.md#supported-ec2-instances "supported-resources.md#supported-ec2-instances")
- Spot Instances
- Mixed instance types that contain any instances outside of the C, M, or R instance families
- Amazon ECS or Amazon EKS workloads
- Mixed instance types containing both AMD and Intel instances
- Mixed instance types using instance weights
- Mixed instance types containing both x86 and Graviton instances
- Mixed instance types containing instances on different platforms, such as Windows, SQL Server, and Linux

### Idle recommendations

Compute Optimizer supports idle recommendations for EC2 Auto Scaling groups that use most of the [Supported Amazon EC2 instance types](#supported-ec2-instances "#supported-ec2-instances"). This includes EC2 Auto Scaling groups that have the following:

- EC2 Spot Instances
- Mixed instance types containing any of the instance families that Compute Optimizer supports (including G and P instance families)
- Amazon ECS or Amazon EKS workloads

## Supported Amazon EBS volume types

Compute Optimizer generates recommendations for the following EBS volume types that are attached
to an instance:

- HDD `st1` and `sc1`
- General Purpose SSD `gp2` and `gp3`
- Provisioned IOPS SSD `io1`, `io2`, and
  `io2 Block Express`

Compute Optimizer also generates recommendations to move your data out from previous
generation HDD Magnetic volumes. For more information, see
[Amazon EBS previous generation volumes](https://aws.amazon.com//ebs/previous-generation/ "https://aws.amazon.com//ebs/previous-generation/").

## Supported Amazon Aurora and RDS databases

The following sections outline the Amazon Aurora and RDS resources supported by Compute Optimizer.

### Database engines

Compute Optimizer Compute Optimizer generates recommendations for Amazon Aurora and RDS databases running the following engines:

- RDS for MySQL
- RDS for PostgreSQL
- Aurora MySQL-Compatible Edition
- Aurora PostgreSQL-Compatible Edition

### RDS DB instances

Compute Optimizer generates recommendations for several DB instance types. For more information about Aurora and RDS DB instance types,
see [DB instance classes](../../../AmazonRDS/latest/UserGuide/Concepts.md "../../../AmazonRDS/latest/UserGuide/Concepts.md")
in the _Amazon Relational Database Service User Guide_ and [DB instance class types](../../../AmazonRDS/latest/AuroraUserGuide/Concepts.DBInstanceClass.md "../../../AmazonRDS/latest/AuroraUserGuide/Concepts.DBInstanceClass.md") in the _Amazon Aurora User Guide for Aurora_.

The following tables list the DB instance types for the databases that are supported by Compute Optimizer.

Amazon RDS
The DB instance types for the RDS for MySQL and RDS for PostgreSQL database engines supported by Compute Optimizer.

| DB instance class family      | Type   |
| ----------------------------- | ------ | -------- | --------- | ------ | ------ | ------ | ------- | ------ | ------- | ------ |
| **General purpose**           | db.m7g | db.m6g   | db.m6i    | db.m5  | db.m3  | db.m1  | db.m2   | db.m5d | db.m6gd | db.m6i |
| **Memory-optimized R family** | db.r3  | db.r4    | db.r5     | db.r5b | db.r5d | db.r6g | db.r6gd | db.r6i | db.r7g  |
| **Burstable-performance**     | db.t3  | db.t4g   |
| **Memory-optimized Z family** | db.x2g | db.x2idn | db.x2iedn |

Amazon Aurora
The DB instance types for the Aurora MySQL-Compatible Edition and Aurora PostgreSQL-Compatible Edition database engines supported by Compute Optimizer.

| DB instance class family      | Type    |
| ----------------------------- | ------- | ------- | ------ | ------ | ------ |
| **Memory-optimized R family** | db.r4   | db.r5   | db.r6g | db.r6i | db.r7g |
| **Memory-optimized X family** | db.x2g  |
| **Burstable-performance**     | db.t2   | db.t3   | db.t4g |
| **Optimized Reads**           | db.r6gd | db.r6id |

###### Note

Compute Optimizer doesn't support **db.serverless – Aurora Serverless v2 instance class with automatic capacity scaling**.

### RDS DB instance storage

Compute Optimizer generates recommendations for the following RDS DB instance storage volume types:

- General Purpose SSD `gp2` and `gp3`
- Provisioned IOPS SSD `io1`

### Aurora DB cluster storage

Compute Optimizer generates recommendations for Aurora DB cluster storage Aurora Standard configurations.

###### Note

Compute Optimizer only provides recommendations to switch from Aurora Standard to Aurora I/O-Optimized storage configurations.

For more information about both configurations, see [Amazon Aurora
storage](../../../AmazonRDS/latest/AuroraUserGuide/Aurora.Overview.md "../../../AmazonRDS/latest/AuroraUserGuide/Aurora.Overview.md") in the _Amazon Aurora User Guide for Aurora_.

## Additional resources

- [Resource requirements](requirements.md "requirements.md")
- [Metrics analyzed by AWS Compute Optimizer](metrics.md "metrics.md")
- [Getting started with AWS Compute Optimizer](getting-started.md "getting-started.md")
