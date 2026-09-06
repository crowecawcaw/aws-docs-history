

# Troubleshooting missing job records in Slurm accounting
<a name="troubleshooting-missing-accounting-records"></a>

Jobs that ran to completion are missing from Slurm accounting reports, such as the output of the `sacct` or `sreport` commands. Records are absent only for a limited time window, typically one that follows a period of very high job submission rate. Accounting reports are complete before and after that window. This topic applies to clusters that have Slurm accounting enabled. For more information about accounting, see [Slurm accounting in AWS PCS](slurm-accounting.md).

## Common cause
<a name="troubleshooting-missing-accounting-records-cause"></a>

The Slurm controller daemon (`slurmctld`) doesn't write accounting data to the accounting database directly. It sends the data to the Slurm database daemon (`slurmdbd`) through an internal, in-memory queue. The queue can reach its maximum size if jobs are submitted faster than `slurmdbd` commits records to the database. When the queue is full, `slurmctld` discards new accounting messages instead of adding them to the queue.

Discarded messages aren't retried, so the job history that they carried is permanently absent from the accounting database. Only accounting data is affected. Job scheduling and job execution continue normally. Records that `slurmdbd` already committed remain in the database. Accounting resumes automatically when the queue drains.

## Resolution
<a name="troubleshooting-missing-accounting-records-resolution"></a>

**To confirm the cause and reduce the chance of recurrence**

1. Search the `slurmctld` log of the cluster for entries similar to the following.

   ```
   error: agent queue is full (33794), discarding DBD_JOB_START:1425 request
   ```

   Each entry corresponds to one discarded accounting message. The message type identifies the record that was lost, such as `DBD_JOB_START`, `DBD_JOB_COMPLETE`, `DBD_STEP_START`, or `DBD_STEP_COMPLETE`. If the cluster doesn't deliver scheduler logs, set up log delivery. This lets you confirm the cause if the condition occurs again. For more information, see [Scheduler logs in AWS PCS](monitoring_scheduler-logs.md).

1. Set the `CommitDelay` parameter to `1` in the slurmdbd configuration of the cluster. With this setting, `slurmdbd` groups database commits instead of committing each record individually, which increases the rate at which it drains the queue. Use the `SlurmdbdCustomSettings` property of the cluster to apply the setting. For more information, see [Configuring custom SlurmDBD settings in AWS PCS](slurmdbd-custom-settings.md) and [CommitDelay](https://slurm.schedmd.com/slurmdbd.conf.html#OPT_CommitDelay) in the Slurm documentation.
**Important**  
`SlurmdbdCustomSettings` replaces the slurmdbd settings of the cluster instead of adding to them. Any setting that you omit from the update request is removed. If the cluster might already have slurmdbd settings, run `aws pcs get-cluster` first, add `{parameterName=CommitDelay,parameterValue="1"}` to the retrieved list, then submit the complete list.  
**Example – Setting `CommitDelay` on a cluster**  

   ```
   aws pcs update-cluster --cluster-identifier {{my-cluster}} \
   --slurm-configuration \
   'SlurmdbdCustomSettings=[{parameterName=CommitDelay,parameterValue="1"}]'
   ```

1. Confirm that the setting is in place. In the AWS Management Console, view **Additional scheduler settings** for the cluster. In the AWS CLI, run the following command and check the `slurmConfiguration` field of the response.

   ```
   aws pcs get-cluster --cluster-identifier {{my-cluster}}
   ```

**Note**  
Accounting records that `slurmctld` discarded can't be recovered. Jobs that ran during the affected window remain absent from accounting reports.

## Prevention
<a name="troubleshooting-missing-accounting-records-prevention"></a>

To detect queue saturation while it happens instead of finding missing records later, deliver `slurmctld` logs to Amazon CloudWatch Logs, Amazon Simple Storage Service (Amazon S3), or Amazon Data Firehose, and monitor them for `agent queue is full` entries. For more information, see [Scheduler logs in AWS PCS](monitoring_scheduler-logs.md).

Keep `CommitDelay` set to `1` on clusters that run workloads with a high job submission rate.