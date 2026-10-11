

# Monitoring with the AWS DataSync console dashboard
<a name="management-console-dashboard"></a>

You can monitor your data transfers using the AWS DataSync console dashboard. From the dashboard, you can view all active task executions and filter them by properties such as **Start time**, **Status**, and **Task ID**. You can also view a summary of data transferred, files transferred, and task execution statuses.

## Access the AWS DataSync console dashboard
<a name="accessing-console-dashboard"></a>

1. Open the AWS DataSync console at [https://console.aws.amazon.com/datasync/](https://console.aws.amazon.com/datasync/).

1. In the left navigation pane, choose **Dashboard**.

## Service overview
<a name="service-overview"></a>

**Service overview** displays the following information:

**Tasks**  
Total number of tasks in the AWS Region

**Locations**  
Total number of locations in the AWS Region

**Agents**  
Total number of agents in the AWS Region

**Data throughput**  
The aggregate data throughput for all active (running) task executions. This includes task executions with the status: `LAUNCHING`, ` PREPARING`, or `TRANSFERRING`.  
For more information, see [Understanding data transfer performance counters](transfer-performance-counters.md).

## Task executions (table view)
<a name="task-executions-table"></a>

The **Task executions** table displays all task executions, initially filtered to the last 7 days. The following property filters are supported:

**Execution ID**  
Task execution ID

**Start time**  
The time that DataSync sends the request to start the task execution

**Status**  
The status of the task execution

**Task ID**  
The task ID associated with the task execution

**Task mode**  
The `TaskMode` of the task associated with the task execution

**Task name**  
The `TaskName` of the task associated with the task execution

**Note**  
Task execution history is retained for 30 days. For more information, see [DataSync quotas](datasync-limits.md#task-hard-limits).

## Total transferred by task (table view)
<a name="total-transferred-by-task-table"></a>

The **Total transferred by task** table displays the total **Data transferred** and **Files transferred** per task.

**Note**  
This is an aggregation of the **Task executions** table above. Any property filters applied to the **Task executions** table also apply to this table.