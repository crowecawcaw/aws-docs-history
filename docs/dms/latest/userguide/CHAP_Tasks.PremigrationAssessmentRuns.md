

# Specifying, starting, and viewing premigration assessment runs
<a name="CHAP_Tasks.PremigrationAssessmentRuns"></a>

A premigration assessment specifies one or more individual assessments to run based on a new or existing migration task configuration. Each individual assessment evaluates a specific element of the source or target database depending on considerations such as the migration type, supported objects, index configuration, and other task settings, such as table mappings to identify the schemas and tables to migrate. For example, an individual assessment might evaluate what source data types or primary key formats can and cannot be migrated.

## Specifying individual assessments
<a name="CHAP_Tasks.PremigrationAssessmentRuns.Individual"></a>

When creating a new assessment run, you can choose to run some or all of the individual assessments that are applicable to your task configuration.

AWS DMS supports premigration assessment runs for the following relational source and target database engines:
+ [Oracle assessments](CHAP_Tasks.AssessmentReport.Oracle.md) 
+ [Sql Server assessments](CHAP_Tasks.AssessmentReport.SqlServer.md) 
+ [MySQL assessments](CHAP_Tasks.AssessmentReport.MySQL.md) (includes MariaDB and Amazon Aurora MySQL-Compatible Edition)
+ [PostgreSQL assessments](CHAP_Tasks.AssessmentReport.PG.md) (includes Amazon Aurora PostgreSQL-Compatible Edition)
+ [MariaDB assessments](CHAP_Tasks.AssessmentReport.MariaDB.md)
+ [Db2 LUW Assessments](CHAP_Tasks.AssessmentReport.Db2.md)

## Starting and viewing premigration assessment runs
<a name="CHAP_Tasks.PremigrationAssessmentRuns.AssessmentRun"></a>

You can start a premigration assessment run for a new or existing migration task using the AWS DMS Management Console, the AWS CLI, and the AWS DMS API.

**To start a premigration assessment run for a new or existing task**

1. From the **Database migration tasks** page in the AWS DMS Management Console, do one of the following:
   + To create a new task and assess it, choose **Create task**. The **Create database migration task page** opens:

     1. Enter the task settings required to create your task, including table mapping.

     1. In the **Premigration assessment** section, the **Premigration assessment run** checkbox is checked. This page contains the options to specify an assessment run for the new task.
**Note**  
When creating a new task, enabling a premigration assessment run disables the option to start the task automatically on task creation. You can start the task manually after the assessment run completes.
   + To assess an existing task, choose the **Identifier** for an existing task on the **Database migration tasks** page. The task page for the chosen existing task opens:

     1. Choose **Actions** and select **Create premigration assessment**. A **Create premigration assessment** page opens with options to specify an assessment run for the existing task. 

1. Enter a unique name for your assessment run, or leave the default value.

1. Select the available individual assessments that you want to include in this assessment run. You can only select the available individual assessments based on your current task settings. By default, all available individual assessments are enabled and selected.

1. Search for and choose an Amazon S3 bucket and folder in your account to store your assessment result report. For information about setting up resources for assessment runs, see [Creating prerequisites for premigration assessments](CHAP_Tasks.AssessmentReport.Prerequisites.md).

1. Select or enter an IAM role with full account access to your chosen Amazon S3 bucket and folder. For information about setting up resources for assessment runs, see [Creating prerequisites for premigration assessments](CHAP_Tasks.AssessmentReport.Prerequisites.md).

1. Optionally choose a setting to encrypt the assessment result report in your Amazon S3 bucket. For information about S3 bucket encryption, see [ Setting default server-side encryption behavior for Amazon S3 buckets ](https://docs.aws.amazon.com/AmazonS3/latest/userguide/bucket-encryption.html).

1. Choose **Create task** for a new task or choose **Create** for an existing task.

   The **Database migration tasks** page opens listing your new or modified task with a **Status** of **Creating...** and a banner message indicating that your premigration assessment run will start once the task is created.

AWS DMS provides access to the latest and all prior premigration assessment runs using the AWS DMS Management Console, the AWS CLI, or the AWS DMS API. 

**To view results for the assessment run**

1. From the AWS DMS Management Console, choose the **Identifier** for your existing task on the **Database migration tasks** page. The task page for the existing task opens.

1. Choose the **Premigration assessments** tab on the existing task page. This opens a **Premigration assessments** section on that page showing results of the the assessment runs, listed by name, in reverse chronological order. The latest result appears at the top of the list. Choose the name of the assessment run whose results you want to view.

These assessment run results start with the name of the latest assessment run and an overview of its status followed by a listing of the specified individual assessments and their status. You can then explore details of the status of each individual assessment by choosing its name in the list, with results available down to the table column level.

Both the status overview for an assessment run and each individual assessment shows a **Status** value. This value indicates the overall status of the assessment run and a similar status for each individual assessment. Following is a list of the **Status** values for the assessment run:
+ `"cancelling"` – The assessment run was cancelled.
+ `"deleting"` – The assessment run was deleted.
+ `"failed"` – At least one individual assessment completed with a `failed` status. This status takes priority over all other statuses, including error conditions.
+ `"error-provisioning"` – An internal error occurred while resources were provisioned (during `provisioning` status). This status is only assigned when no individual assessments have a failed status, as provisioning errors may have prevented assessments from running that could have resulted in failed validations.
+ `"error-executing"` – An internal error occurred while individual assessments ran (during `running` status). This status is only assigned when no individual assessments have a failed status, as error conditions may have prevented assessments from completing that could have resulted in failed validations.
+ `"invalid state"` – The assessment run is in an unknown state.
+ `"passed"` – All individual assessments have completedsuccessfully with no failed, warning, or error statuses.
+ `"provisioning"` – Resources required to run individual assessments are being provisioned.
+ `"running"` – Individual assessments are being ran.
+ `"starting"` – The assessment run is starting, but resources are not yet being provisioned for individual assessments.
+ `"warning"` – At least one individual assessment completed with a `warning` status, and no assessments have failed or error statuses.

Following is a list of the **Status** values for each individual assessment of the assessment run:
+ `"cancelled"` – The individual assessment was cancelled as part of cancelling the assessment run.
+ `"error"` – The individual assessment did not complete successfully.
+ `"failed"` – The individual assessment completed successfully with a failed validation result: view the details of the result for more information.
+ `"invalid state"` – The individual assessment is in an unknown state.
+ `"passed"` – The individual assessment completed with a successful validation result.
+ `"pending"` – The individual assessment is waiting to run.
+ `"running"` – The individual assessment is running.
+ `"warning"` – The individual assessment completed with a warning status.
+ `"skipped"` – The individual assessment were skipped during the assessment run.

You can also view the JSON files for the assessment run results on Amazon S3.

**To view the JSON files for the assessment run on Amazon S3**

1. From the AWS DMS Management Console, choose the Amazon S3 bucket link shown in the status overview of the assessment run. This displays a list of bucket folders and other Amazon S3 objects stored in the bucket. If your results are stored in a bucket folder, open the folder.

1. You can find your assessment run results in several JSON files. A `summary.json` file contains the overall results of the assessment run. The remaining files are each named for an individual assessment that was specified for the assessment run, such as `unsupported-data-types-in-source.json`. These files each contain the results for the corresponding individual assessment from the chosen assessment run.

To start and view the results of premigration assessment runs for an existing migration task, you can run the following CLI commands and AWS DMS API operations:
+ CLI: [`describe-applicable-individual-assessments`](https://docs.aws.amazon.com/cli/latest/reference/dms/describe-applicable-individual-assessments), API: [`DescribeApplicableIndividualAssessments`](https://docs.aws.amazon.com/dms/latest/APIReference/API_DescribeApplicableIndividualAssessments.html) – Provides a list of individual assessments that you can specify for a new premigration assessment run, given one or more task configuration parameters.
+ CLI: [`start-replication-task-assessment-run`](https://docs.aws.amazon.com/cli/latest/reference/dms/start-replication-task-assessment-run), API: [`StartReplicationTaskAssessmentRun`](https://docs.aws.amazon.com/dms/latest/APIReference/API_StartReplicationTaskAssessmentRun.html) – Starts a new premigration assessment run for one or more individual assessments of an existing migration task.
+ CLI: [`describe-replication-task-assessment-runs`](https://docs.aws.amazon.com/cli/latest/reference/dms/describe-replication-task-assessment-runs), API: [`DescribeReplicationTaskAssessmentRuns`](https://docs.aws.amazon.com/dms/latest/APIReference/API_DescribeReplicationTaskAssessmentRuns.html) – Returns a paginated list of premigration assessment runs based on filter settings.
+ CLI: [`describe-replication-task-individual-assessments`](https://docs.aws.amazon.com/cli/latest/reference/dms/describe-replication-task-individual-assessments), API: [`DescribeReplicationTaskIndividualAssessments`](https://docs.aws.amazon.com/dms/latest/APIReference/API_DescribeReplicationTaskIndividualAssessments.html) – Returns a paginated list of individual assessments based on filter settings.
+ CLI: [`cancel-replication-task-assessment-run`](https://docs.aws.amazon.com/cli/latest/reference/dms/cancel-replication-task-assessment-run), API: [`CancelReplicationTaskAssessmentRun`](https://docs.aws.amazon.com/dms/latest/APIReference/API_CancelReplicationTaskAssessmentRun.html) – Cancels, but doesn't delete, a single premigration assessment run.
+ CLI: [`delete-replication-task-assessment-run`](https://docs.aws.amazon.com/cli/latest/reference/dms/delete-replication-task-assessment-run), API: [`DeleteReplicationTaskAssessmentRun`](https://docs.aws.amazon.com/dms/latest/APIReference/API_DeleteReplicationTaskAssessmentRun.html) – Deletes the record of a single premigration assessment run.