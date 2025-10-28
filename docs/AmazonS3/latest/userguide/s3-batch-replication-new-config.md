# Create a Batch Replication job for new

replication rules or destinations

In Amazon S3, live replication doesn't replicate any objects that already existed in your
source bucket before you created a replication configuration. Live replication automatically
replicates only new and updated objects that are written to the bucket after the replication
configuration is created. To replicate already existing objects, you can use
S3 Batch Replication to replicate these objects on demand.

When you create the first rule in a new live replication configuration or add a new
destination bucket to an existing replication configuration through the Amazon S3 console, you
can optionally create a Batch Replication job. You can use this Batch Replication job to
replicate existing objects in the source bucket to the destination bucket.

To use Batch Replication for an existing configuration without adding a new destination
bucket, see [Create a Batch Replication job for
existing replication rules](s3-batch-replication-existing-config.md "s3-batch-replication-existing-config.md").

###### Prerequisites

Before creating your Batch Replication job, you must create a Batch Operations AWS Identity and Access Management
(IAM) role to grant Amazon S3 permissions to perform actions on your behalf. For more
information, see [Configuring an IAM role for
S3 Batch Replication](s3-batch-replication-policies.md "s3-batch-replication-policies.md").

## Using Batch Replication for a

new replication rule or destination through the Amazon S3 console

When you create the first rule in a new replication configuration or add a new
destination bucket to an existing configuration through the Amazon S3 console, you can choose
to create a Batch Replication job to replicate existing objects in the source
bucket.

###### To create a Batch Replication job when creating or updating a replication

configuration

1. Sign in to the AWS Management Console and open the Amazon S3 console at
   [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. In the left navigation pane, choose **Buckets**.
3. In the **General purpose buckets** list, choose the name of
   the bucket that contains the objects that you want to replicate.
4. To create a new replication rule or edit an existing rule, choose the
   **Management** tab, and scroll down to
   **Replication rules**:
   - To create a new replication rule, choose **Create replication
     rule**. For examples of how to set up a basic replication
     rule, see [Examples for configuring live replication](replication-example-walkthroughs.md "replication-example-walkthroughs.md").
   - To edit an existing replication rule, select the option button next to
     the rule name, and then choose **Edit rule**.

5. Create your new replication rule or edit the destination for your existing
   replication rule, and choose **Save**.

After you create the first rule in a new replication configuration or edit an
existing configuration to add a new destination, a **Replicate existing
objects?** dialog appears, giving you the option to create a
Batch Replication job. 6. If you want to create and run this job now, choose **Yes, replicate
existing objects**.

If you want to create a Batch Replication job at a later time, choose
**No, do not replicate existing objects**. 7. If you chose **Yes, replicate existing objects**, the
**Create Batch Operations job** page appears. The
S3 Batch Replication job has the following settings:

**Job run options**

If you want the S3 Batch Replication job to run immediately,
choose **Automatically run the job when it's
ready**. If you want to run the job at a later time,
choose **Wait to run the job when it's
ready**.

###### Note

If you choose **Automatically run the job when it's
ready**, you won't be able to create and save a
Batch Operations manifest. To save the Batch Operations manifest, choose
**Wait to run the job when it's ready**.

**Batch Operations manifest**

If you chose **Wait to run the job when it's
ready**, the **Batch Operations manifest**
section appears. The manifest is a list of all of the objects that
you want to run the specified action on. You can choose to save the
manifest. Similar to S3 Inventory files, the manifest will be saved
as a CSV file and stored in a bucket. To learn more about Batch Operations
manifests, see [Specifying a manifest](batch-ops-create-job.md#specify-batchjob-manifest "batch-ops-create-job.md#specify-batchjob-manifest").

**Completion report**

S3 Batch Operations executes one task for each object specified in the
manifest. Completion reports provide an easy way to view the results
of your tasks in a consolidated format with no additional setup
required. You can request a completion report for all tasks or only
for failed tasks. To learn more about completion reports, see [Completion reports](batch-ops-job-status.md#batch-ops-completion-report "batch-ops-job-status.md#batch-ops-completion-report").

**Permissions**

One of the most common causes of replication failures is
insufficient permissions in the provided AWS Identity and Access Management (IAM) role. For
information about creating this role, see [Configuring an IAM role for
S3 Batch Replication](s3-batch-replication-policies.md "s3-batch-replication-policies.md"). Make sure that you
create or choose an IAM role that has the required permissions for
Batch Replication. 8. Choose **Save**.
