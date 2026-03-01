# Rerunning automation executions

You can rerun AWS Systems Manager automation executions to repeat tasks with either identical or
modified parameters. The rerun capability allows you to efficiently replicate automation
executions without manually recreating automation configurations, reducing operational
overhead and potential configuration errors.

When you rerun an automation execution, Systems Manager preserves the original runbook
parameters, Amazon CloudWatch alarms, and tags from the previous execution. The system creates a
new execution with a new execution ID and updated timestamps. You can rerun any type of
automation execution, including simple executions, rate control executions,
cross-account and cross-region executions, and manual executions.

## Rerun an automation execution (console)

The following procedures describe how to use the Systems Manager console to rerun an
automation execution.

###### To rerun an automation execution from the Automation home page

Open the AWS Systems Manager console at [https://console.aws.amazon.com/systems-manager/](https://console.aws.amazon.com/systems-manager/ "https://console.aws.amazon.com/systems-manager/").

1. In the navigation pane, choose **Automation**.
2. In the executions list, select the execution that you want to
   rerun.
3. Choose **Rerun execution**.
4. On the **Execute automation document** page, review the
   pre-populated parameters, execution mode, and target configuration from the
   original execution.
5. (Optional) Modify any parameters, targets, or other settings as needed for
   your rerun.
6. Choose **Execute** to start the rerun with a new
   execution ID.

###### To rerun an automation execution from the execution details page

Open the AWS Systems Manager console at [https://console.aws.amazon.com/systems-manager/](https://console.aws.amazon.com/systems-manager/ "https://console.aws.amazon.com/systems-manager/").

1. In the navigation pane, choose **Automation**.
2. Choose the execution ID of the automation that you want to rerun.
3. On the execution details page, choose **Rerun
   execution**.
4. On the **Execute automation document** page, review the
   pre-populated parameters, execution mode, and target configuration from the
   original execution.
5. (Optional) Modify any parameters, targets, or other settings as needed for
   your rerun.
6. Choose **Execute** to start the rerun with a new
   execution ID.

###### To copy an automation execution to a new execution

Open the AWS Systems Manager console at [https://console.aws.amazon.com/systems-manager/](https://console.aws.amazon.com/systems-manager/ "https://console.aws.amazon.com/systems-manager/").

1. In the navigation pane, choose **Automation**.
2. Choose the execution ID of the automation that you want to copy.
3. On the execution details page, choose **Actions**, and
   then choose **Copy to new**.
4. On the **Execute automation document** page, review the
   pre-populated parameters, execution mode, and target configuration from the
   original execution.
5. (Optional) Modify any parameters, targets, or other settings as needed for
   your new execution.
6. Choose **Execute** to start the new execution.
