# Migration jobs

To use AWS Transform for migrations, you first need a workspace, which is a logical
container in which you can create one or more transformation jobs. The sections in this
topic describe how to get a workspace and how to create and start a migration job
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
transferring your data across AWS Regions. For more information, see [Connect target AWS accounts and regions](transform-vmware-connect-target-account.md "transform-vmware-connect-target-account.md").

## Job types

AWS Transform offers the following types of migration jobs that you can choose
from depending on your migration needs. In addition to these preset options, you can
dynamically add or remove any step from your job at any time to customize your
migration workflow.

### End-to-end migration

1. Perform discovery
2. Build migration plan
3. Connect target accounts
4. Build landing zone
5. Migrate network
6. Migrate servers

### Discovery and migration planning

1. Perform discovery
2. Build migration plan

### Network migration

1. Connect target accounts
2. Migrate network

### Landing zone

1. Connect target accounts
2. Build landing zone

### Landing zone, network, and server migration

1. Connect target accounts
2. Build landing zone
3. Migrate network
4. Migrate servers

### Migration planning and server migration

Includes discovery, wave plan, and rehost.

1. Perform discovery
2. Build migration plan
3. Connect target accounts
4. Migrate servers

## Creating and starting a job

The first step of a migration project is to create an AWS Transform job. For
migration projects, you can choose different job types, depending on your
goals. The following procedure describes how to create and start a new migration
job of any type. For information about the different job types, see [Job types](#vmware-job-types "#vmware-job-types").

###### To create and start a new migration job

1. On your workspace landing page, choose **Create a job**.
2. Choose the migration option, and then specify the type of
   migration job that you want to create. For information about the steps
   included in each of the migration job types, see [Job types](#vmware-job-types "#vmware-job-types").
3. After you answer all the chat questions, choose **Create
   job**.

## Limitations

AWS Transform has the following limitations:

- If you stop a running migration job, and then ask the agent to restart it, the
  job will start again from the beginning and you will lose any progress you have
  made in the job. However, artifacts created in the job before restarting it will
  still be available.
- You can specify one target AWS Region per migration job. To migrate applications to different target Regions, create multiple migration jobs.
- Multi-account migration – Single region only – You can migrate to multiple accounts within a single AWS Region. For multi-region migrations, you must create separate projects for each target region.
- Multi-account migration – One account per wave – Each migration wave can target only one account. Applications requiring different target accounts must be placed in separate waves.
- Multi-account migration – AWS Organizations required – All target accounts must be part of an AWS Organization.
