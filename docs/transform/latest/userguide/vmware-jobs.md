# Migration jobs

To start migrating, create a workspace and launch a migration job. A workspace is
a logical container for one or more migration jobs, giving you a single place to
manage your entire migration.

## Getting a workspace

For information about creating a workspace, see [Getting started](getting-started.md "getting-started.md").

Your workspace determines the AWS Region where your jobs, discovery data, and
AWS Transform recommendations reside. To work in a different AWS Region, ask your
administrator to create a workspace in that Region. For information about supported
AWS Regions, see [Supported Regions for AWS Transform](regions.md "regions.md").

You can specify a different AWS Region as your migration target. This means you
can run discovery in one Region but deploy your target environment in another. If
you do that, some of your data is transferred across AWS Regions. Server
replication data is not transferred across Regions; it goes directly from your
source environment into your target account and Region. For more information, see
[Connect target AWS accounts and regions](transform-vmware-connect-target-account.md "transform-vmware-connect-target-account.md").

## Job types

Whether you need an end-to-end migration or want to tackle a specific phase,
AWS Transform offers several types of migration jobs to choose from. In addition to
these preset options, you can add or remove any step from your job at any time to
customize your migration workflow.

### End-to-end migration

Best for complete migrations where you want AWS Transform to handle everything
from discovery through rehost.

1. Perform discovery
2. Build migration plan
3. Connect target accounts
4. Build landing zone
5. Migrate network
6. Migrate servers

### Discovery and migration planning

Use this when you want to assess your environment and build a wave plan
before committing to execution.

1. Perform discovery
2. Build migration plan

### Network migration

Use this when your landing zone and accounts are already set up and you
need to migrate your network configuration to AWS.

1. Connect target accounts
2. Migrate network

### Landing zone

Use this when you need to set up your multi-account AWS foundation
before migrating workloads.

1. Connect target accounts
2. Build landing zone

### Landing zone, network, and server migration

Use this when you already have discovery and planning complete and want
AWS Transform to handle infrastructure setup and execution.

1. Connect target accounts
2. Build landing zone
3. Migrate network
4. Migrate servers

### Migration planning and server migration

Use this when your network is already in place and you want to go from
discovery straight to rehost.

1. Perform discovery
2. Build migration plan
3. Connect target accounts
4. Migrate servers

## Creating and starting a job

To create a migration job, complete the following steps. For information about
the different job types, see [Job types](#vmware-job-types "#vmware-job-types").

###### To create and start a new migration job

1. On your workspace landing page, choose **Create a job**.
2. Choose the migration option, and then specify the type of
   migration job that you want to create. For information about the steps
   included in each of the migration job types, see [Job types](#vmware-job-types "#vmware-job-types").
3. After you answer all the chat questions, choose **Create
   job**.

## Downloading a workspace summary report

You can generate a workspace summary report as a downloadable PDF at any time
during your migration. The report provides a consolidated view across all migration
jobs in your workspace, including:

- Job statuses and current workflow steps
- User actions and approvals
- Wave planning details
- Network migration topology
- Landing zone configuration
- Rehost progress
- Containerization decisions
- Key artifacts produced

To generate a report, ask the agent in the chat. For example, “Give
me a workspace summary of my migration progress across all jobs.” The agent
compiles data from all jobs and delivers the PDF directly in chat.

## Limitations

AWS Transform has the following limitations:

- If you stop a running migration job, and then ask the agent to restart it, the
  job will start again from the beginning and you will lose any progress you have
  made in the job. However, artifacts created in the job before restarting it will
  still be available.
- You can specify one target AWS Region per migration job. To migrate applications to different target Regions, create multiple migration jobs.
- Multi-account migration – Single region only – You can migrate to multiple accounts within a single AWS Region. For multi-Region migrations, you must create separate projects for each target region.
- Multi-account migration – One account per wave – Each migration wave can target only one account. Applications requiring different target accounts must be placed in separate waves.
- Multi-account migration – AWS Organizations required – All target accounts must be part of an AWS Organization.
