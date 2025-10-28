# `AWSSupport-AnalyzeEMRLogs`

**Description**

This runbook helps identify errors while running a job on an Amazon EMR cluster. The
runbook analyzes a list of defined logs on the file system and looks for a list of
predefined keywords. These log entries are used to create Amazon CloudWatch Events events so you
can take any needed actions based on the events. Optionally, the runbook publishes
log entries to the Amazon CloudWatch Logs log group of your choosing. This runbook currently
looks for the following errors and patterns in log files:

- **`container_out_of_memory – YARN container ran out of
memory, running job may fail.`**
- **`yarn_nodemanager_health: CORE or TASK node is running low on disk
space and will not be able to run tasks.`**
- **`node_state_change: CORE or TASK node is unreachable by the MASTER
node.`**
- **`step_failure: An EMR Step has failed.`**
- **`no_core_nodes_running: No CORE nodes are currently running,
cluster is unhealthy.`**
- **`hdfs_missing_blocks: There are missing HDFS blocks which could
lead to data loss.`**
- **`hdfs_high_util: HDFS Utilization is high, which may affect jobs
and cluster health.`**
- **`instance_controller_restart: Instance-Controller process has
restarted. This process is essential for cluster health.`**
- **`instance_controller_restart_legacy: Instance-Controller process
has restarted. This process is essential for cluster health.`**
- **`high_load: High Load Average detected, may affect node health
reporting or result in timeouts or slowdowns.`**
- **`yarn_node_blacklisted: CORE or TASK node has been blacklisted by
YARN from running tasks.`**
- **`yarn_node_lost: CORE or TASK node has been marked as LOST by
YARN, possible connectivity issues.`**
  Instances associated with the `ClusterID` that you specify must be
  managed by AWS Systems Manager. You can run this automation once, schedule the automation to
  run at a specific time interval, or remove a schedule created previously by an
  automation. This runbook supports Amazon EMR release versions 5.20 to 6.30.

[Run this Automation (console)](https://console.aws.amazon.com/systems-manager/automation/execute/AWSSupport-AnalyzeEMRLogs "https://console.aws.amazon.com/systems-manager/automation/execute/AWSSupport-AnalyzeEMRLogs")

**Document type**

Automation

**Owner**

Amazon

**Platforms**

Linux, macOS, Windows

**Parameters**

- AutomationAssumeRole

Type: String

Description: (Optional) The Amazon Resource Name (ARN) of the AWS Identity and Access Management
(IAM) role that allows Systems Manager Automation to perform the actions on your
behalf. If no role is specified, Systems Manager Automation uses the permissions of
the user that starts this runbook.

- ClusterID

Type: String

Description: (Required) The ID of the cluster whose nodes logs you want to
analyze.

- Operation

Type: String

Valid values: Run Once | Schedule | Remove Schedule

Description: (Required) The operation to perform on the cluster.

- IntervalTime

Type: String

Valid values: 5 minutes | 10 minutes | 15 minutes

Description: (Optional) The duration of time between running the
automation. This parameter is only applicable if you specify
`Schedule` for the `Operation` parameter.

- LogToCloudWatchLogs

Type: String

Valid values: yes | no

Description: (Optional) If you specify `yes` for the value of
this parameter, the automation creates a CloudWatch Logs log group with the name
specified in the `CloudWatchLogGroup` parameter to store any
matched log entries.

- CloudWatchLogGroup

Type: String

Description: (Optional) The name of the CloudWatch Logs log group you want to store
any matched log entries in. This parameter is only applicable if you specify
`yes` for the `LogToCloudWatchLogs` parameter.

- CreateLogInsightsDashboard

Type: String

Valid values: yes | no

Description: (Optional) If you specify `yes` , CloudWatch dashboard
is created if it does not already exist. This parameter is only applicable
if you specify `yes` for the `LogToCloudWatchLogs`
parameter.

- CreateMetricFilters

Type: String

Valid values: yes | no

Description: (Optional) Specify `yes` if you want to create
metric filters for the CloudWatch Logs log group. This parameter is only applicable if
you specify `yes` for the `LogToCloudWatchLogs`
parameter.
**Required IAM permissions**

The `AutomationAssumeRole` parameter requires the following actions to
use the runbook successfully.

- `ssm:StartAutomationExecution`
- `ssm:GetDocument`
- `ssm:ListDocuments`
- `ssm:DescribeAutomationExecutions`
- `ssm:DescribeAutomationStepExecutions`
- `ssm:GetAutomationExecution`
- `ssm:DescribeInstanceInformation`
- `ssm:ListCommandInvocations`
- `ssm:ListCommands`
- `ssm:SendCommand`
- `iam:CreateRole`
- `iam:DeleteRole`
- `iam:GetRolePolicy`
- `iam:PutRolePolicy`
- `iam:DeleteRolePolicy`
- `iam:passrole`
- `cloudformation:DescribeStacks`
- `cloudformation:DeleteStack`
- `cloudformation:CreateStack`
- `events:DeleteRule`
- `events:RemoveTargets`
- `events:PutTargets`
- `events:PutRule`
- `events:DescribeRule`
- `logs:DescribeLogGroups`
- `logs:CreateLogGroup`
- `logs:PutMetricFilter`
- `cloudwatch:PutDashboard`
- `elasticmapreduce:ListInstances`
- `elasticmapreduce:DescribeCluster`

**Document Steps**

- `aws:executeAwsApi` - Gathers information about the Amazon EMR cluster
  specified in the `ClusterID` parameter.
- `aws:branch` - Branches based on input.
  - If the provided operation is `Run Once` or
    `Schedule` :
    - `aws:assertAwsResourceProperty` - Verifies the
      cluster is available.
    - `aws:executeAwsApi` - Gathers the IDs of all
      instances running in the cluster.
    - `aws:assertAwsResourceProperty` - Verifies the
      SSM Agent is running on all instances in the cluster.
    - `aws:branch` - Branches based on whether you
      specified to run the automation once or on a schedule.
      - If the provided operation is `Run
Once` :
        - `aws:branch` - Branches based on the
          value specified in the
          `LogToCloudWatchLogs` parameter.
          - If `LogToCloudWatchLogs` value
            is `yes` :
            - `aws:executeScript` - Checks if a CloudWatch Logs
              log group with the name specified in parameter
              `CloudWatchLogGroup` already exists. If
              not, the group is created with the name specified.
            - `aws:branch` - Branches based on the
              value specified in the
              `CreateMetricFilters` parameter.
              - If `CreateMetricFilters` value
                is `yes` :
                - `aws:executeAwsApi` - 12 steps are ran
                  for each metric filter
                - `aws:branch` - Branches based on the
                  value specified in the
                  `CreateLogInsightsDashboard` parameter.
                  - If `CreateLogInsightsDashboard`
                    value is `yes` :
                    - `aws:executeAwsApi` - Creates a CloudWatch
                      dashboard with the same name specified in the
                      `CloudWatchLogGroup` parameter, if it
                      does not already exist.

                  - If `CreateLogInsightsDashboard`
                    value is `no` :
                    - `aws:runCommand` - Runs a shell script
                      to find log patterns on each instance in the
                      cluster.

              - If `CreateMetricFilters` value
                is `no` :
                - `aws:branch` - Branches based on the
                  value specified in
                  `CreateLogInsightsDashboard` parameter.
                  - If `CreateLogInsightsDashboard`
                    value is `yes` :
                    - `aws:executeAwsApi` - Creates a CloudWatch
                      dashboard with the same name specified in the
                      `CloudWatchLogGroup` parameter, if it
                      does not already exist.

                  - If `CreateLogInsightsDashboard`
                    value is `no` :
                    - `aws:runCommand` - Runs a shell script
                      to find log patterns on each instance in the
                      cluster.

          - If `LogToCloudWatchLogs` value
            is `no` :
            - `aws:executeAwsApi` - Runs a shell
              script to find log patterns on each instance in
              the cluster.

      - If the provided operation is
        `Schedule` :
        - `aws:createStack` - Creates an Amazon EventBridge
          event that targets this runbook.

  - If the provided operation is `Remove Schedule` :
    - `aws:executeAwsApi` - Verifies a schedule exists
      for the cluster.
    - `aws:deleteStack` - Deletes the schedule.

**Outputs**

GetClusterInformation.ClusterName

GetClusterInformation.ClusterState

ListingClusterInstances.InstanceIDs

CreatingScheduleCloudFormationStack.StackStatus

RemovingScheduleByDeletingScheduleCloudFormationStack.StackStatus

CheckIfLogGroupExists.output

FindLogPatternOnEMRNode.CommandId
