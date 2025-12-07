# VMware migration jobs

To use AWS Transform for VMware migrations, you first need a workspace, which is a logical
container in which you can create one or more transformation jobs. The sections in this
topic describe how to get a workspace and how to create and start a VMware migration job
in it.

## Getting a workspace

For information about getting a workspace, see [Getting started](getting-started.md "getting-started.md").

The workspace that you use determines the AWS Region where you can create
transformation jobs. That is the AWS Region where your jobs will reside. Your
discovery data and AWS Transform recommendations will also reside in this AWS Region.
To create workspaces and jobs in a different AWS Region, ask your administrator to
create a different workspace for you. For information about supported AWS Regions,
see [Supported Regions for AWS Transform](regions.md "regions.md").

Even though the AWS Region where you can create jobs and store discovery data
and recommendations is determined by your AWS Transform administrator, you can specify a
different AWS Region as your target for the migration. In other words, you can run
discovery and receive AWS Transform recommendations in one AWS Region, but then create
your target environment in a different AWS Region. If you do that, you will be
transferring your data across AWS Regions. For more information, see [AWS account connectors for
VMware migrations](transform-app-vmware-acct-connections.md "transform-app-vmware-acct-connections.md").

## Job types

AWS Transform offers the following types of VMware migration jobs that you can choose
from depending on your migration needs.

### End-to-end migration

1. Perform discovery
2. Generate wave plan
3. Generate VPC configuration
4. (Optional) Deploy VPC networks
5. Migrate servers

### Network migration only

1. Generate VPC configuration
2. (Optional) Deploy VPC networks

### Network-and-server

migration

1. Generate VPC configuration
2. (Optional) Deploy VPC networks
3. Migrate servers

### Discovery and server

migration

1. Perform discovery
2. Generate wave plan
3. Migrate servers

## Creating and starting a

job

The first step of a migration project is to create an AWS Transform job. For
VMware migration projects, you can choose different job types, depending on your
goals. The following procedure describes how to create and start a new VMware
migration job of any type. For information about the different job types, see [Job types](#vmware-job-types "#vmware-job-types").

###### To create and start a new VMware migration job

1. On your workspace landing page, choose **Create a job**.
2. Choose the VMware migration option, and then specify the type of VMware
   migration job that you want to create. For information about the steps
   included in each of the four VMware migration job types, see [Job types](#vmware-job-types "#vmware-job-types").
3. After you answer all the chat questions, choose **Create
   job**.
