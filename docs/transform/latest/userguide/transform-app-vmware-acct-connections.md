# AWS account connectors for

VMware migrations

To perform a VMware migration, you need an AWS account target account connector.

The target AWS account connector connects your migration job to your new AWS
environment where your workloads will reside after the migration. It's important to
ensure that the target AWS account that you specify for this connector is properly
set up with the necessary permissions, quotas, and configurations to support your
migrated infrastructure.

When you create your target AWS account connector, AWS Transform will ask you to
specify a target AWS Region. That is the AWS Region where your target
environment with all your servers will reside. You can specify any one of the
following AWS Regions for the target account connector:

- US East (N. Virginia)
- US East (Ohio)
- US West (Oregon)
- Asia Pacific (Mumbai)
- Asia Pacific (Tokyo)
- Asia Pacific (Osaka)
- Asia Pacific (Seoul)
- Asia Pacific (Sydney)
- Asia Pacific (Singapore)
- Canada (Central)
- Europe (Frankfurt)
- Europe (London)
- Europe (Paris)
- Europe (Ireland)
- Europe (Stockholm)
- South America (São Paulo)

###### Important

If you specify a target AWS Region that is different from the AWS Transform
AWS Region, that means AWS Transform will be transferring your data across
AWS Regions.

The target connector connects your migration job to the target AWS account and
target AWS Region for the following purposes:

- **Network-infrastructure setup** – The
  target account is where you will create new Amazon VPCs and associated network
  resources to host your migrated applications in the target AWS Region that
  you specify when you create the target connector.
- **Amazon EC2-instance setup** – The target
  AWS account is where you will migrate your VMware virtual machines and run
  them as Amazon EC2 instances in the target AWS Region.
- **Testing and validation:** – Before
  final cutover, you will use the target AWS account for testing the
  migrated servers and ensuring they function correctly in the AWS
  environment.
- **Cost management** – The target
  AWS account will be where the costs for running your migrated
  infrastructure are incurred and where you can track those costs.
- **Long-term operations** –
  Post-migration, this target AWS account becomes your primary account for
  operating and managing your former source workloads in AWS.

###### Note

AWS Transform may update connector types when introducing features requiring
permission changes within your AWS accounts. You can use a connector version that
is compatible with your VMware migration job. New connectors are created with the
latest version for that connector type. The current version for the discovery account connector type is 1.0.
The current version for target account connector type is 2.0.
