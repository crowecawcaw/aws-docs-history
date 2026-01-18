# Troubleshoot restoring your SQL Server database

from AWS VSS solution snapshots

Before you try any troubleshooting steps, we recommend that you verify that you've met all
[VSS snapshot restore prerequisites](ms-ssdb-ec2-vss-restore-prereq.md "ms-ssdb-ec2-vss-restore-prereq.md").

## Debug failures in

AWSEC2-RestoreSqlServerDatabaseWithVss from the Systems Manager console

In the Systems Manager console, the **Failure details** section in the automation
runbook **Execution Details** page includes the following information:

- **Failure Message**
- **Failure Type**
- **Failure Stage**

Together, these details offer a general overview of the cause of the failure. For a more
comprehensive understanding, you must examine the specific step execution that failed.

The steps in `AWSEC2-RestoreSqlServerDatabaseWithVss` can be
classified into three main categories:

**Script Execution Steps**

These use the `aws:executeScript` action and include the following
steps.

- `ExtractPrepareVssRestoreOutput`
- `PrepareForVolumeCreation`
- `ExtractCurrIterValues`
- `ConcatVolumeIds`

If one of these steps fails, investigate the step execution and review the
execution logs found under **OutputPayload** in the
**Outputs** section to determine what caused the issue.

**EC2 API Interaction Steps**

These interact with Amazon EC2 APIs to create volumes from snapshots, attach them to
instances, and monitor volume status. Many of these steps are performed within loop
steps. If a loop step fails, identify the specific step within the loop that caused
the failure to pinpoint the root cause. The **Failure details**
section in the step execution details page provides relevant information for debugging.

**Run Command Execution Steps**

These use the `aws:RunCommand` action to execute commands on the target
instance. If a failure occurs due to a run command execution, examine the step execution
details. Under **Outputs**, select the **CommandId**
link for the command to access the **Run command execution** page, where
you can view the complete log for debugging purposes.
