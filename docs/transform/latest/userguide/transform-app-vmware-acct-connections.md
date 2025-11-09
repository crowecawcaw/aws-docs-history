# AWS account connectors for

VMware migrations

To perform a VMware migration, you need two types of AWS account connectors.

## Discovery account connector

This AWS account connector is for discovery and planning purposes. It gives
AWS Transform permissions to perform discovery-related actions within the AWS account
that you specify. AWS Transform performs these actions in the AWS Region of the
workspace that has the VMware migration job. To use another AWS Region for
discovery, ask your administrator to provide you a workspace in that AWS Region. A
workspace can be in one of the following AWS Regions:

- US East (N. Virginia)
- Europe (Frankfurt)

After you create this connector, AWS Transform creates an Amazon S3 bucket for you in the
discovery account and Region. It uses that bucket for storing data that is
discovered from your source VMware environment. This discovery data is crucial for
planning and performing the migration. This data includes information about your
source servers, applications, networks, and dependencies.

AWS Transform uses the discovery data for the following purposes:

- To analyze your source environment, which is essential for planning the
  migration strategy.
- To understand your current network setup, which is crucial for planning
  the network configuration in AWS.
- To assess security requirements and compliance needs based on your current
  setup.
- To understand application dependencies, which is critical for planning the
  migration waves and ensuring all necessary components are moved
  together.
- To determine the appropriate Amazon EC2 instance types and sizes for your
  migrated VMs based on the discovery data.

## Target account connector

This AWS account connector connects your migration job to your new AWS
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

If you specify a target AWS Region that is different from the discovery
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
