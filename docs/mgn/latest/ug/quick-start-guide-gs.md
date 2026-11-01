

# Quick start guide for AWS Transform MGN
<a name="quick-start-guide-gs"></a>

This quick start is a high-level checklist of the AWS Transform MGN migration flow. Each step links to the detailed instructions for that step. For a one-page overview of the migration flow, see [Migration workflow](migration-workflow-gs.md).

## Before you begin
<a name="qs-before-you-begin"></a>

Before you start the migration, make sure that:
+ To [initialize the service](mgn-initialize-console.md), you use an IAM user with the AdministratorAccess managed policy attached.
+ AWS Transform MGN is [available in your target AWS Region](what-is-mgn.md#supported-regions).
+ Your source environment and AWS network meet the [network requirements](preparing-environments.md), including the required ports.

The following diagram shows the network architecture for AWS Transform MGN.

![Data replication from corporate data center through AWS Replication Agent to staging area and migrated resources in AWS.](https://docs.aws.amazon.com/mgn/latest/ug/images/AWSMGNArchitecture.png)


The service is free for each server for 2,160 hours, which is 90 days when used continuously, but you pay for the AWS resources you provision during the migration. Learn more about [costs during migration](adding-servers.md).

## Step 1: Initialize the service
<a name="qs-step-initialize"></a>

AWS Transform MGN must be initialized in each AWS Region in which you plan to use it. When you initialize MGN with the console, the initialization process creates your replication template, which determines how data is replicated from your source servers to AWS.

Learn more about [initializing MGN with the console](mgn-initialize-console.md) and the [replication template](replication-settings-template.md).

## Step 2: Add source servers
<a name="qs-step-add-servers"></a>

Add source servers to AWS Transform MGN by installing the AWS Replication Agent on them.

How you know you're done: in the **Source servers** list, the **Migration lifecycle** column shows **Not ready** while the initial sync runs, and changes to **Ready for testing** when the initial sync is complete. The **Data replication status** column shows **Healthy** when all data has been copied and changes are replicated continuously.

Learn more about [adding source servers](adding-servers.md), [installing the AWS Replication Agent](agent-installation.md), and the [migration lifecycle](source-server-migration-metrics.md#source-server-migration-metrics-lifecycle).

## Step 3: Review launch settings
<a name="qs-step-launch-settings"></a>

Launch settings determine how a test or cutover instance is launched for each source server in AWS. AWS Transform MGN creates them automatically, including the Amazon EC2 launch template, each time you add a source server, and you can modify them at any time.

Learn more about [launch settings](launch-settings.md) and [reviewing launch settings for a source server](launch-settings-source.md).

## Step 4: Launch and validate test instances
<a name="qs-step-test"></a>

Launch test instances to verify that your source servers function properly in AWS before you initiate a cutover.

What you do:
+ Check that the server shows **Ready for testing** and **Healthy**, then choose **Test and cutover**, then under **Testing**, choose **Launch test instances**.
+ Connect to each test instance with SSH (Linux) or RDP (Windows), validate connectivity, and run acceptance tests for your application.
+ When testing is complete, choose **Test and cutover**, then under **Testing**, choose **Mark as "Ready for cutover"**.

How you know you're done: the **Migration lifecycle** column changes from **Test in progress** to **Ready for cutover**.

**Tip**  
You can test as many times as you need. Each new test replaces the previous test instance, and data replication continues. You are billed for test instances, so terminate them when you no longer need them.

Learn more about [launching test instances](launching-test-servers.md) and [marking servers as Ready for cutover](finalizing-test.md).

## Step 5: Launch cutover instances
<a name="qs-step-cutover"></a>

After you finalize testing for your source servers, launch cutover instances at a set date and time. The cutover migrates your source servers to the cutover instances in AWS.

What you do:
+ Confirm that the server shows **Ready for cutover**, that **Data replication status** is **Healthy**, and that there is no lag.
+ Stop all operational services on the source server. We recommend that you shut down the source server so that it doesn't drift from the cutover instance. Don't reboot source servers before the cutover.
+ Choose **Test and cutover**, then under **Cutover**, choose **Launch cutover instances**.
+ Connect to the cutover instances with SSH or RDP and validate your application.

How you know you're done: the **Migration lifecycle** column shows **Cutover in progress**.

Learn more about [launching cutover instances](launch-cutover.md).

## Step 6: Complete the migration
<a name="qs-step-complete"></a>

After you confirm that the cutover instance works as expected, finalize the cutover. Then disconnect the source server from AWS Transform MGN, and archive or delete the source server.

**Important**  
Don't disconnect a source server until the cutover instance works correctly. You might need to fall back to the source server, and restarting replication requires reinstalling the agent.

What you do:
+ Choose **Test and cutover**, then choose **Finalize cutover**. This stops data replication, discards replicated data, terminates replication resources, and sends the AWS Replication Agent a command to uninstall itself (typically up to 10 minutes).
+ Choose **Actions**, then choose **Disconnect from service**.
+ Choose **Actions**, then choose **Mark as archived**.

How you know you're done: after you finalize the cutover, the **Migration lifecycle** column shows **Cutover complete**, and the **Next step** column shows **Mark as archived**.

Learn more about [managing source servers after migration](server-post-migration.md), including how to [finalize the cutover](server-post-migration.md#server-post-migration-finalize-cutover), [disconnect the source server](server-post-migration.md#server-post-migration-disconnect), and [archive the source server](server-post-migration.md#server-post-migration-archive).