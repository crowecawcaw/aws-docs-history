# Monitoring dashboards and alarms on Amazon MWAA

The environment details page for an Amazon Managed Workflows for Apache Airflow environment includes a built-in CloudWatch metrics dashboard and an **Environment alarms** table. You can use these features to monitor the health of your environment directly in the Amazon MWAA console, without any additional setup.

Apache Airflow exposes metrics for several processes, including the number of DAG processes, DAG bag size, currently running tasks, task failures, and successes. When you create an environment, Apache Airflow automatically sends metrics for your Amazon MWAA environment to CloudWatch. In addition to the built-in dashboard, you can build custom dashboards in Amazon CloudWatch and add alarms for particular metrics. When an alarm is on a dashboard, it turns red when it enters the `ALARM` state. This makes it easier to monitor the health of your Amazon MWAA environment proactively.

###### Contents

- [View the metrics dashboard](monitoring-dashboard.md#monitoring-dashboard-console-metrics "monitoring-dashboard.md#monitoring-dashboard-console-metrics")

  - [Metrics shown on the dashboard](monitoring-dashboard.md#monitoring-dashboard-console-metrics-list "monitoring-dashboard.md#monitoring-dashboard-console-metrics-list")

- [Create and monitor alarms](monitoring-dashboard.md#monitoring-dashboard-console-alarms "monitoring-dashboard.md#monitoring-dashboard-console-alarms")

  - [Recommended alarms](monitoring-dashboard.md#monitoring-dashboard-console-alarms-recommended "monitoring-dashboard.md#monitoring-dashboard-console-alarms-recommended")

- [Alarm states overview](monitoring-dashboard.md#monitoring-dashboard-states "monitoring-dashboard.md#monitoring-dashboard-states")
- [Example custom dashboards and alarms](monitoring-dashboard.md#monitoring-dashboard-custom "monitoring-dashboard.md#monitoring-dashboard-custom")

  - [About these metrics](monitoring-dashboard.md#monitoring-dashboard-custom-about "monitoring-dashboard.md#monitoring-dashboard-custom-about")
  - [About the dashboard](monitoring-dashboard.md#monitoring-dashboard-custom-about-dash "monitoring-dashboard.md#monitoring-dashboard-custom-about-dash")
  - [Using AWS tutorials](monitoring-dashboard.md#monitoring-dashboard-tutorials "monitoring-dashboard.md#monitoring-dashboard-tutorials")
  - [Using CloudFormation](monitoring-dashboard.md#monitoring-dashboard-cfn "monitoring-dashboard.md#monitoring-dashboard-cfn")

- [Deleting metrics and dashboards](monitoring-dashboard.md#monitoring-dashboard-delete "monitoring-dashboard.md#monitoring-dashboard-delete")
- [What's next?](monitoring-dashboard.md#monitoring-dashboard-next-up "monitoring-dashboard.md#monitoring-dashboard-next-up")

## View the metrics dashboard

The environment details page includes a built-in CloudWatch metrics dashboard, shown in the console under **CloudWatch metrics**. This embedded CloudWatch dashboard displays charts for your environment without any additional setup.

![The CloudWatch metrics pane on the Amazon MWAA environment details page, showing the Alarm recommendations toggle, the Metric sections filter, and example charts in the Containers group.](images/mwaa-metrics-dashboard.png)

To open the full set of metrics in the CloudWatch console, choose **View all in CloudWatch**.

The dashboard displays metrics from the following two CloudWatch namespaces:

- `AmazonMWAA` – Apache Airflow metrics.
- `AWS/MWAA` – Container, queue, and database metrics.

You can use the following controls to change what the dashboard displays:

- Turn on the **Alarm recommendations** toggle to show only the recommended metrics. When you turn on this toggle, each chart draws its alarm threshold as an annotation. The annotation reads _Alarms if `metric` above_ or _Alarms if `metric` below_, depending on the metric.
- Use the **Metric sections** filter to show only the charts in a specific group. The available groups are **Containers**, **Database and queue**, **Scheduler**, **DAG processing**, **Tasks**, and **Triggerer**.

###### Note

If you configure an environment to filter which Apache Airflow metrics it publishes by using the metrics allow list or block list options, some charts might not have data.

###### Note

To view the metrics dashboard, your IAM identity must have permission to read CloudWatch metrics, including `cloudwatch:GetMetricData`, `cloudwatch:GetMetricStatistics`, and `cloudwatch:ListMetrics`. Without these permissions, the charts render with no data.

For the full list of metrics that Amazon MWAA publishes, see [Apache Airflow environment metrics in CloudWatch](access-metrics-cw.md "access-metrics-cw.md").

### Metrics shown on the dashboard

The dashboard organizes charts into six sections that you can filter with **Metric sections**. It shows a curated set of environment-wide metrics; charts come from the `AmazonMWAA` namespace (Apache Airflow metrics) and the `AWS/MWAA` namespace (container, queue, and database metrics). The following table lists the charts in each section and the CloudWatch metrics each one displays.

Dashboard charts and their metrics| Section | Chart | CloudWatch metrics |
| --- | --- | --- |
| Containers | Scheduler CPU utilization | `CPUUtilization` |
| Containers | Scheduler memory utilization | `MemoryUtilization` |
| Containers | Worker CPU utilization | `CPUUtilization` (BaseWorker and AdditionalWorker) |
| Containers | Worker memory utilization | `MemoryUtilization` (BaseWorker and AdditionalWorker) |
| Containers | Web server CPU utilization | `CPUUtilization` |
| Containers | Web server memory utilization | `MemoryUtilization` |
| Containers | Worker containers running | Derived from `CPUUtilization` sample count |
| Containers | Worker heartbeat | `CeleryWorkerHeartbeat` |
| Database and queue | Database freeable memory | `FreeableMemory` |
| Database and queue | Database CPU utilization | `CPUUtilization` |
| Database and queue | Database connections | `DatabaseConnections` |
| Database and queue | Database write latency | `WriteLatency` |
| Database and queue | Oldest queued task age | `ApproximateAgeOfOldestTask` |
| Scheduler | Scheduler heartbeat | `SchedulerHeartbeat` |
| Scheduler | Scheduler critical section duration | `CriticalSectionDuration` |
| Scheduler | Scheduler task states | `TasksExecutable`, `TasksStarving`, `TasksWithoutDagRun` |
| Scheduler | Tasks killed externally | `TasksKilledExternally` |
| Scheduler | Executor open slots | `OpenSlots` |
| DAG processing | DAG parse time | `TotalParseTime` |
| DAG processing | DAG bag size | `DagBagSize` |
| DAG processing | DAG import errors | `ImportErrors`, `DAGFileRefreshError` |
| DAG processing | DAG processor health | `ProcessorTimeouts`, `ManagerStalls` |
| Tasks | Task queue | `QueuedTasks`, `RunningTasks` |
| Tasks | Task successes and failures | `TaskInstanceSuccesses`, `TaskInstanceFailures` |
| Tasks | Zombie tasks killed | `ZombiesKilled` |
| Triggerer | Triggerer heartbeat | `TriggererHeartbeat` |
| Triggerer | Trigger outcomes | `TriggersSucceeded`, `TriggersFailed` |

###### Note

The Triggerer charts appear only on newer Apache Airflow versions. **Trigger outcomes** requires Apache Airflow v2.7.2 or later, and **Triggerer heartbeat** requires v2.8.1 or later.

The dashboard shows aggregate, environment-wide metrics. It does not chart high-cardinality metrics that Apache Airflow publishes per DAG, task, pool, operator, or DAG file, and it charts container CPU and memory but not every container metric. For the complete list of published metrics, see [Apache Airflow environment metrics in CloudWatch](access-metrics-cw.md "access-metrics-cw.md") and [Container, queue, and database metrics for Amazon MWAA](accessing-metrics-cw-container-queue-db.md "accessing-metrics-cw-container-queue-db.md").

## Create and monitor alarms

The environment details page includes an **Alarms** pane where you create and manage your alarms in CloudWatch, and then monitor them in context. The pane shows an **Environment alarms** table that lists the CloudWatch alarms attributed to the environment. Amazon MWAA matches these alarms by CloudWatch namespace and the `Environment` dimension, so the table includes alarms that you author yourself, not only the recommended alarms.

![The Alarms pane on the Amazon MWAA environment details page, showing the Create recommended alarms and Manage in CloudWatch buttons above the Environment alarms table.](images/mwaa-environment-alarms.png)

The pane header shows an **In alarm** count of how many of the environment's alarms are currently in the `ALARM` state. The **Environment alarms** table has the following columns.

| Name                                                                | Status                                                | Condition                                                             | Action                                                                                         | Last updated                                       |
| ------------------------------------------------------------------- | ----------------------------------------------------- | --------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------- | -------------------------------------------------- |
| The alarm name, which links to the alarm in the CloudWatch console. | The alarm status: In alarm, OK, or Insufficient data. | The alarm condition, shown as _for `n` datapoints within `duration`_. | The alarm's action, such as _Notify SNS topic `topic`_, or *-<br>• if the alarm has no action. | The date and time when the alarm was last updated. |

###### Note

To view the alarms in this table, you must have the `cloudwatch:DescribeAlarms` permission.

If the environment has no alarms, the **Environment alarms** table is empty and provides guidance to create the recommended alarms to start monitoring your environment.

The **Alarms** pane provides the following two buttons:

- **Create recommended alarms** – Opens a CloudFormation quick-create stack in a new tab. The stack is named `MWAA-alarms-`environment-name`` and creates a standard set of recommended alarms for the environment.
- **Manage in CloudWatch** – Opens the alarms page in the CloudWatch console.

###### To create the recommended alarms

1. Open the [Amazon MWAA console](https://console.aws.amazon.com/mwaa/home "https://console.aws.amazon.com/mwaa/home"), and then choose your environment to open its details page.
2. In the **Monitoring** view, locate the **Alarms** pane.
3. Choose **Create recommended alarms**. The CloudFormation quick-create stack opens in a new browser tab.
4. Review the stack in the CloudFormation console. If prompted, select the acknowledgment that CloudFormation might create IAM resources.
5. Choose **Create stack**.

After CloudFormation creates the stack, the alarms appear in the **Environment alarms** table and in the CloudWatch console. For more information about what each alarm state means, see [Alarm states overview](#monitoring-dashboard-states "#monitoring-dashboard-states").

### Recommended alarms

When you choose **Create recommended alarms**, the CloudFormation template creates the following alarms. CloudWatch evaluates all of these alarms over 5-minute (300-second) periods.

Recommended alarms created by the CloudFormation template| Alarm | Metric | Threshold condition |
| --- | --- | --- |
| Scheduler heartbeat | `SchedulerHeartbeat` | Sum < 1 for 2 of 2 datapoints; missing data is treated as in alarm. |
| Oldest queued task age | `ApproximateAgeOfOldestTask` | Maximum > 1800 seconds for 3 of 3 datapoints. |
| Scheduler CPU utilization | `CPUUtilization` (Scheduler) | Average > 95% for 3 of 3 datapoints. |
| Scheduler memory utilization | `MemoryUtilization` (Scheduler) | Average > 95% for 3 of 3 datapoints. |
| Worker CPU utilization | `CPUUtilization` (BaseWorker) | Average > 95% for 6 of 6 datapoints. |
| Worker memory utilization | `MemoryUtilization` (BaseWorker) | Average > 95% for 6 of 6 datapoints. |
| Web server CPU utilization | `CPUUtilization` (WebServer) | Average > 95% for 3 of 3 datapoints. |
| Web server memory utilization | `MemoryUtilization` (WebServer) | Average > 95% for 3 of 3 datapoints. |
| Database CPU utilization | `CPUUtilization` (WRITER) | Average > 95% for 3 of 3 datapoints. |
| Database freeable memory | `FreeableMemory` (WRITER) | Average < 512 MiB for 3 of 3 datapoints. |

## Alarm states overview

A metric alarm has the following possible states:

- `OK` – The metric or expression is within the defined threshold.
- `ALARM` – The metric or expression is outside of the defined threshold.
- `INSUFFICIENT_DATA` – The alarm has just started, the metric is not available, or not enough data is available for
  the metric to determine the alarm state.

## Example custom dashboards and alarms

You can define your own dashboards and alarms as infrastructure as code to build custom dashboards programmatically or to standardize monitoring across multiple Amazon MWAA environments. As an alternative to the built-in dashboard on the environment details page, the following tutorial and CloudFormation template create a custom monitoring dashboard. This dashboard displays charts of selected metrics for your Amazon MWAA environment.

### About these metrics

The following list describes each of the metrics created in the custom dashboard by the tutorial and template definitions in this section.

- _QueuedTasks_ - The number of tasks with queued state. Corresponds to the `executor.queued_tasks` Apache Airflow metric.
- _TasksPending_ - The number of tasks pending in executor. Corresponds to the `scheduler.tasks.pending` Apache Airflow metric.

###### Note

Does not apply to Apache Airflow v2.2 and later.

- _RunningTasks_ - The number of tasks running in executor. Corresponds to the `executor.running_tasks` Apache Airflow metric.
- _SchedulerHeartbeat_ - The number of check-ins Apache Airflow performs on the scheduler job. Corresponds to the `scheduler_heartbeat` Apache Airflow metrics.
- _TotalParseTime_ - The number of seconds taken to scan and import all DAG files once. Corresponds to the `dag_processing.total_parse_time` Apache Airflow metric.

### About the dashboard

The following image displays the monitoring dashboard created by the tutorial and template definition in this section.

![This image depicts where to find the Private network option on the Amazon MWAA console.](images/cw-dashboard.png)

### Using AWS tutorials

You can use the following AWS tutorial to automatically create a health status dashboard for any Amazon MWAA environments that are currently deployed. It also creates CloudWatch alarms for unhealthy workers and scheduler heartbeat failures across all Amazon MWAA environments.

- [CloudWatch Dashboard Automation for Amazon MWAA](https://github.com/aws-samples/mwaa-dashboard "https://github.com/aws-samples/mwaa-dashboard")

### Using CloudFormation

You can use the CloudFormation template definition in this section to create a monitoring dashboard in CloudWatch, then add alarms on the CloudWatch console to receive notifications when a metric surpasses a particular threshold. To create the stack using this template definition, refer to [Creating a stack on the CloudFormation console](../../../AWSCloudFormation/latest/UserGuide/cfn-console-create-stack.md "../../../AWSCloudFormation/latest/UserGuide/cfn-console-create-stack.md"). To add an alarm to the dashboard, refer to [Using alarms](../../../AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.md "../../../AmazonCloudWatch/latest/monitoring/AlarmThatSendsEmail.md").

```
AWSTemplateFormatVersion: "2010-09-09"
Description: Creates MWAA Cloudwatch Dashboard
Parameters:
  DashboardName:
    Description: Enter the name of the CloudWatch Dashboard
    Type: String
  EnvironmentName:
    Description: Enter the name of the MWAA Environment
    Type: String
Resources:
  BasicDashboard:
    Type: AWS::CloudWatch::Dashboard
    Properties:
      DashboardName: !Ref DashboardName
      DashboardBody:
        Fn::Sub: '{
              "widgets": [
                  {
                      "type": "metric",
                      "x": 0,
                      "y": 0,
                      "width": 12,
                      "height": 6,
                      "properties": {
                          "view": "timeSeries",
                          "stacked": true,
                          "metrics": [
                              [
                                  "AmazonMWAA",
                                  "QueuedTasks",
                                  "Function",
                                  "Executor",
                                  "Environment",
                                  "${EnvironmentName}"
                              ]
                          ],
                          "region": "${AWS::Region}",
                          "title": "QueuedTasks ${EnvironmentName}",
                          "period": 300
                      }
                  },
                  {
                      "type": "metric",
                      "x": 0,
                      "y": 6,
                      "width": 12,
                      "height": 6,
                      "properties": {
                          "view": "timeSeries",
                          "stacked": true,
                          "metrics": [
                              [
                                  "AmazonMWAA",
                                  "RunningTasks",
                                  "Function",
                                  "Executor",
                                  "Environment",
                                  "${EnvironmentName}"
                              ]
                          ],
                          "region": "${AWS::Region}",
                          "title": "RunningTasks ${EnvironmentName}",
                          "period": 300
                      }
                  },
                  {
                      "type": "metric",
                      "x": 12,
                      "y": 6,
                      "width": 12,
                      "height": 6,
                      "properties": {
                          "view": "timeSeries",
                          "stacked": true,
                          "metrics": [
                              [
                                  "AmazonMWAA",
                                  "SchedulerHeartbeat",
                                  "Function",
                                  "Scheduler",
                                  "Environment",
                                  "${EnvironmentName}"
                              ]
                          ],
                          "region": "${AWS::Region}",
                          "title": "SchedulerHeartbeat ${EnvironmentName}",
                          "period": 300
                      }
                  },
                  {
                      "type": "metric",
                      "x": 12,
                      "y": 0,
                      "width": 12,
                      "height": 6,
                      "properties": {
                          "view": "timeSeries",
                          "stacked": true,
                          "metrics": [
                              [
                                  "AmazonMWAA",
                                  "TasksPending",
                                  "Function",
                                  "Scheduler",
                                  "Environment",
                                  "${EnvironmentName}"
                              ]
                          ],
                          "region": "${AWS::Region}",
                          "title": "TasksPending ${EnvironmentName}",
                          "period": 300
                      }
                  },
                  {
                      "type": "metric",
                      "x": 0,
                      "y": 12,
                      "width": 24,
                      "height": 6,
                      "properties": {
                          "view": "timeSeries",
                          "stacked": true,
                          "region": "${AWS::Region}",
                          "metrics": [
                              [
                                  "AmazonMWAA",
                                  "TotalParseTime",
                                  "Function",
                                  "DAG Processing",
                                  "Environment",
                                  "${EnvironmentName}"
                              ]
                          ],
                          "title": "TotalParseTime  ${EnvironmentName}",
                          "period": 300
                      }
                  }
              ]
          }'
```

## Deleting metrics and dashboards

If you delete an Amazon MWAA environment, the corresponding dashboard is also deleted. CloudWatch metrics are stored for fifteen (15) months and can not be deleted. The CloudWatch console limits the search of metrics to two (2) weeks after a metric is last ingested to ensure that the most up to date instances are shown for your Amazon MWAA environment. To learn more, refer to [Amazon CloudWatch FAQs](https://aws.amazon.com/cloudwatch/faqs/ "https://aws.amazon.com/cloudwatch/faqs/").

## What's next?

- Learn how to create a DAG that queries the Amazon Aurora PostgreSQL metadata database for your environment and publishes custom metrics to CloudWatch in [Using a DAG to write custom metrics in CloudWatch](samples-custom-metrics.md "samples-custom-metrics.md").
