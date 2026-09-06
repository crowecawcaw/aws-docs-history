

# Runtime coverage and troubleshooting for Amazon ECS clusters
<a name="gdu-assess-coverage-ecs"></a>

The runtime coverage for Amazon ECS clusters includes the tasks running on AWS Fargate and Amazon ECS container instances[1](#ecs-container-instance).

For an Amazon ECS cluster that runs on Fargate, the runtime coverage is assessed at the task level. The ECS clusters runtime coverage includes those Fargate tasks that have started running after you have enabled Runtime Monitoring and automated agent configuration for Fargate (ECS only). By default, a Fargate task is immutable. GuardDuty will not be able to install the security agent to monitor containers on already running tasks. To include such a Fargate task, you must stop and start the task again. Make sure to check if the associated service is supported.

For information about Amazon ECS container, see [Capacity creation](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/create-capacity.html).

**Topics**
+ [Reviewing coverage statistics](#ecs-review-coverage-statistics-ecs-runtime-monitoring)
+ [Coverage status change with EventBridge notifications](#ecs-runtime-monitoring-coverage-status-change)
+ [Troubleshooting Amazon ECS-Fargate runtime coverage issues](#ecs-runtime-monitoring-coverage-issues-troubleshoot)

## Reviewing coverage statistics
<a name="ecs-review-coverage-statistics-ecs-runtime-monitoring"></a>

The coverage statistics for the Amazon ECS resources associated with your own account or your member accounts is the percentage of the healthy Amazon ECS clusters over all the Amazon ECS clusters in the selected AWS Region. This includes the coverage for Amazon ECS clusters associated with both Fargate and Amazon EC2 instances. The following equation represents this as:

*(Healthy clusters/All clusters)\*100*

### Considerations
<a name="considerations-ecs-coverage-review-stats"></a>
+ The coverage statistics for the ECS cluster include the coverage status of the Fargate tasks or ECS container instances associated with that ECS cluster. The coverage status of the Fargate tasks include tasks that either are in running state or have recently finished running. 
+ In the **ECS clusters runtime coverage** tab, the **Container instances covered** field indicates the coverage status of the Amazon EC2 container instances associated with your Amazon ECS cluster.

  If your Amazon ECS cluster runs only the Fargate launch type, this field displays a dash (-) to indicate that the count is not applicable. A Fargate-only cluster has no Amazon EC2 container instances to cover.
+ If your Amazon ECS cluster is associated with an Amazon EC2 instance that doesn't have a security agent, the Amazon ECS cluster will also have an **Unhealthy** coverage status.

  To identify and troubleshoot the coverage issue for the associated Amazon EC2 instance, see [Troubleshooting Amazon EC2 runtime coverage issues](gdu-assess-coverage-ec2.md#ec2-runtime-monitoring-coverage-issues-troubleshoot) for Amazon EC2 instances.

Choose one of the access methods to review the coverage statistics for your accounts.

------
#### [ Console ]
+ Sign in to the AWS Management Console and open the GuardDuty console at [https://console.aws.amazon.com/guardduty/](https://console.aws.amazon.com/guardduty/).
+ In the navigation pane, choose **Runtime Monitoring**.
+ Choose the **Runtime coverage** tab.
+ Under the **ECS clusters runtime coverage** tab, you can view the coverage statistics aggregated by the coverage status of each Amazon ECS cluster that is available in the **Clusters list** table. 
  + You can filter the **Cluster list** table by the following columns:
    + **Account ID**
    + **Cluster Name**
    + **Agent management type**
    + **Coverage status**
+ If any of your Amazon ECS clusters have the **Coverage status** as **Unhealthy**, the **Issue** column includes additional information about the reason for the **Unhealthy** status.

  If you Amazon ECS clusters are associated with an Amazon EC2 instance, navigate to the **EC2 instance runtime coverage** tab and filter by the **Cluster name** field to view the associated **Issue**.

------
#### [ API/CLI ]
+ Run the [ListCoverage](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListCoverage.html) API with your own valid detector ID, current Region, and service endpoint. You can filter and sort the instance list using this API.
  + You can change the example `filter-criteria` with one of the following options for `CriterionKey`:
    + `ACCOUNT_ID`
    + `ECS_CLUSTER_NAME`
    + `COVERAGE_STATUS`
    + `MANAGEMENT_TYPE`
  + You can change the example `AttributeName` in `sort-criteria` with the following options:
    + `ACCOUNT_ID`
    + `COVERAGE_STATUS`
    + `ISSUE`
    + `ECS_CLUSTER_NAME`
    + `UPDATED_AT`

      The field gets updated only when either a new task gets created in the associated Amazon ECS cluster or there is change in the corresponding coverage status.
  + You can change the {{max-results}} (up to 50).
  + To find the `detectorId` for your account and current Region, see the **Settings** page in the [https://console.aws.amazon.com/guardduty/](https://console.aws.amazon.com/guardduty/) console, or run the [ListDetectors](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListDetectors.html) API.

  ```
  aws guardduty --region {{us-east-1}} list-coverage --detector-id {{12abc34d567e8fa901bc2d34e56789f0}} --sort-criteria '{"AttributeName": "{{ECS_CLUSTER_NAME}}", "OrderBy": "{{DESC}}"}' --filter-criteria '{"FilterCriterion":[{"CriterionKey":"{{ACCOUNT_ID}}", "FilterCondition":{"EqualsValue":"111122223333"}}] }'  --max-results {{5}}
  ```
+ Run the [GetCoverageStatistics](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_GetCoverageStatistics.html) API to retrieve coverage aggregated statistics based on the `statisticsType`.
  + You can change the example `statisticsType` to one of the following options:
    + `COUNT_BY_COVERAGE_STATUS` – Represents coverage statistics for ECS clusters aggregated by coverage status.
    + `COUNT_BY_RESOURCE_TYPE` – Coverage statistics aggregated based on the type of AWS resource in the list.
    + You can change the example `filter-criteria` in the command. You can use the following options for `CriterionKey`:
      + `ACCOUNT_ID`
      + `ECS_CLUSTER_NAME`
      + `COVERAGE_STATUS`
      + `MANAGEMENT_TYPE`
      + `INSTANCE_ID`
  + To find the `detectorId` for your account and current Region, see the **Settings** page in the [https://console.aws.amazon.com/guardduty/](https://console.aws.amazon.com/guardduty/) console, or run the [ListDetectors](https://docs.aws.amazon.com/guardduty/latest/APIReference/API_ListDetectors.html) API.

  ```
  aws guardduty --region {{us-east-1}} get-coverage-statistics --detector-id {{12abc34d567e8fa901bc2d34e56789f0}} --statistics-type {{COUNT_BY_COVERAGE_STATUS}} --filter-criteria '{"FilterCriterion":[{"CriterionKey":"{{ACCOUNT_ID}}", "FilterCondition":{"EqualsValue":"123456789012"}}] }'
  ```

------

For more information about coverage issues, see [Troubleshooting Amazon ECS-Fargate runtime coverage issues](#ecs-runtime-monitoring-coverage-issues-troubleshoot).

## Coverage status change with EventBridge notifications
<a name="ecs-runtime-monitoring-coverage-status-change"></a>

The coverage status of your Amazon ECS cluster might appear as **Unhealthy**. To know when the coverage status changes, we recommend you to monitor the coverage status periodically, and troubleshoot if the status becomes **Unhealthy**. Alternatively, you can create an Amazon EventBridge rule to receive a notification when the coverage status changes from either **Unhealthy** to **Healthy** or otherwise. By default, GuardDuty publishes this in the [EventBridge bus](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-event-bus.html) for your account.

### Sample notification schema
<a name="ecs-gdu-coverage-status-eventbridge-schema"></a>

In an EventBridge rule, you can use the pre-defined sample events and event patterns to receive coverage status notification. For more information about creating an EventBridge rule, see [Create rule](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-get-started.html#eb-gs-create-rule) in the *Amazon EventBridge User Guide*. 

Additionally, you can create a custom event pattern by using the following example notification schema. Make sure to replace the values for your account. To get notified when the coverage status of your Amazon ECS cluster changes from `Healthy` to `Unhealthy`, the `detail-type` should be {{GuardDuty Runtime Protection Unhealthy}}. To get notified when the coverage status changes from `Unhealthy` to `Healthy`, replace the value of `detail-type` with {{GuardDuty Runtime Protection Healthy}}.

```
{
  "version": "0",
  "id": "event ID",
  "detail-type": "GuardDuty Runtime Protection Unhealthy",
  "source": "aws.guardduty",
  "account": "AWS account ID",
  "time": "event timestamp (string)",
  "region": "AWS Region",
  "resources": [
       ],
  "detail": {
    "schemaVersion": "1.0",
    "resourceAccountId": "string",
    "currentStatus": "string",
    "previousStatus": "string",
    "resourceDetails": {
        "resourceType": "ECS",
        "ecsClusterDetails": {
          "clusterName":"",
          "fargateDetails":{
            "issues":[],
            "managementType":""
          },
          "containerInstanceDetails":{
            "coveredContainerInstances":int,
            "compatibleContainerInstances":int
          }
        }
    },
    "issue": "string",
    "lastUpdatedAt": "timestamp"
  }
}
```

## Troubleshooting Amazon ECS-Fargate runtime coverage issues
<a name="ecs-runtime-monitoring-coverage-issues-troubleshoot"></a>

If the coverage status of your Amazon ECS cluster is **Unhealthy**, you can view the reason under the **Issue** column. 

The following table provides the recommended troubleshooting steps for Fargate (Amazon ECS only) issues. For information about Amazon EC2 instance coverage issues, see [Troubleshooting Amazon EC2 runtime coverage issues](gdu-assess-coverage-ec2.md#ec2-runtime-monitoring-coverage-issues-troubleshoot) for Amazon EC2 instances.



- ** Agent not reporting **
  - **Extra information:** Agent not reporting for tasks in `TaskDefinition - '{{TASK_DEFINITION}}'` / **Recommended troubleshooting steps:** Validate that the VPC endpoint for your Amazon ECS cluster's task is correctly configured. For more information, see [Validating VPC endpoint configuration](validate-vpc-endpoint-config-runtime-monitoring.md).<br />If your organization has a service control policy (SCP), validate that permissions boundary is not restricting the `guardduty:SendSecurityTelemetry` permission. For more information, see [Validating your organization service control policy in a multi-account environment](prereq-runtime-monitoring-ecs-support.md#validate-organization-scp-ecs).
  - **Extra information:** `{{VPC_ISSUE}}; for task in TaskDefinition - '{{TASK_DEFINITION}}'` / **Recommended troubleshooting steps:** View the VPC issue details in the extra information.

- ** Agent exited **
  - **Extra information:** ExitCode: `EXIT_CODE` for tasks in `TaskDefinition - '{{TASK_DEFINITION}}'` / **Recommended troubleshooting steps:** View the issue details in the extra information.
  - **Extra information:** Reason: {{REASON}} for tasks in `TaskDefinition - '{{TASK_DEFINITION}}'`
  - **Extra information:** ExitCode: `EXIT_CODE` with reason: '{{EXIT\_CODE}}' for tasks in `TaskDefinition - '{{TASK_DEFINITION}}'`
  - **Extra information:** Agent exited: Reason: `CannotPullContainerError`: pull image manifest has been retried... / **Recommended troubleshooting steps:** In this scenario, GuardDuty is potentially unable to pull the sidecar container image. Your task will continue to run but GuardDuty can't detect potential threats. Perform the following troubleshooting steps one at a time to check if it helps resolving the coverage issue:+  **Permissions:** Ensure your task execution role has the required ECR permissions listed in [Permissions requirements](prereq-runtime-monitoring-ecs-support.md#ecs-runtime-permissions-requirements). <br />+  **Network connectivity:** Verify that your Fargate tasks can reach ECR either through public internet access or properly configured VPC endpoints as described in [Network connectivity requirements](prereq-runtime-monitoring-ecs-support.md#ecs-runtime-network-requirements). <br />+  **Security group configuration:** Check that your security group allows outbound access to the S3 managed prefix list on port 443 as explained in [Security group configuration](prereq-runtime-monitoring-ecs-support.md#ecs-runtime-security-group-requirements). <br />+  Run the [AWSSupport-TroubleshootECSTaskFailedToStart](https://docs.aws.amazon.com/systems-manager-automation-runbooks/latest/userguide/automation-aws-troubleshootecstaskfailedtostart.html) runbook in your cluster's Region to identify specific issues. <br />+  View tasks logs for error messages. For information about how to do this, see [Viewing Amazon ECS container agent logs](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/logs.html) in the *Amazon Elastic Container Service Developer Guide*.  <br />For common errors and troubleshooting, see [Amazon ECS troubleshooting](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/troubleshooting.html) in the *Amazon Elastic Container Service Developer Guide*. <br />These three components (permissions, network connectivity, and security group configuration) are independent but all necessary for successfully downloading the GuardDuty container image from Amazon ECR.<br />If the issue persists, see [My AWS Step Functions workflow is failing unexpectedly](troubleshooting-guardduty-runtime-monitoring.md#runtime-ecs-step-function-failure).

- ** VPC Endpoint Creation Failed **
  - **Extra information:** Enabling private DNS requires both `enableDnsSupport` and `enableDnsHostnames` VPC attributes set to `true` for {{vpcId}} (Service: EC2, Status Code:400, Request ID: {{a1b2c3d4-5678-90ab-cdef-EXAMPLE11111}}).
  - **Recommended troubleshooting steps:** Ensure that the following VPC attributes are set to `true` – `enableDnsSupport` and `enableDnsHostnames`. For more information, see [DNS attributes in your VPC](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-dns.html#vpc-dns-support).<br />If you're using Amazon VPC Console at [https://console.aws.amazon.com/vpc/](https://console.aws.amazon.com/vpc/) to create the Amazon VPC, make sure to select both **Enable DNS hostnames** and **Enable DNS resolution**. For more information, see [VPC configuration options](https://docs.aws.amazon.com/vpc/latest/userguide/create-vpc.html#create-vpc-options).

- **Agent not provisioned**
  - **Extra information:** Unsupported invocation by `{{SERVICE}}` for task(s) in `TaskDefinition - '{{TASK_DEFINITION}}'` / **Recommended troubleshooting steps:** This task was invoked by a `{{SERVICE}}` that is not supported.
  - **Extra information:** Unsupported CPU architecture '{{TYPE}}' for task(s) in `TaskDefinition - '{{TASK_DEFINITION}}'` / **Recommended troubleshooting steps:** This task is running on an unsupported CPU architecture. For information about supported CPU architectures, see [Validating architectural requirements](prereq-runtime-monitoring-ecs-support.md#validating-architecture-req-ecs).
  - **Extra information:** `TaskExecutionRole` missing from `TaskDefinition - '{{TASK_DEFINITION}}'` / **Recommended troubleshooting steps:** The ECS task execution role is missing. For information about providing task execution role and required permissions, see [Prerequisites for container image access](prereq-runtime-monitoring-ecs-support.md#before-enable-runtime-monitoring-ecs).
  - **Extra information:** Missing network configuration '`{{CONFIGURATION_DETAILS}}`' for task(s) in `TaskDefinition - '{{TASK_DEFINITION}}'` / **Recommended troubleshooting steps:** Network configuration issues may show up because of missing VPC configuration, or missing or empty subnets.<br />Validate that your network configuration is correct. For more information, see [Prerequisites for container image access](prereq-runtime-monitoring-ecs-support.md#before-enable-runtime-monitoring-ecs).<br />For more information, see [Amazon ECS task definition parameters](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/task_definition_parameters.html) in the *Amazon Elastic Container Service Developer Guide*.
  - **Extra information:** Tasks started when clusters had exclusion tag are excluded from Runtime Monitoring. Impacted task ID(s): '`{{TASK_ID}}` / **Recommended troubleshooting steps:** When you change the predefined GuardDuty tag from `GuardDutyManaged`-`true` to `GuardDutyManaged`-`false`, GuardDuty will not receive the runtime events for this Amazon ECS cluster.<br />Update the tag to `GuardDutyManaged`-`true` and then relaunch the task.
  - **Extra information:** Services deployed when clusters had exclusion tag are excluded from Runtime Monitoring. Impacted service name(s): '{{`SERVICE_NAME`}}' / **Recommended troubleshooting steps:** When services deployed with the exclusion tag `GuardDutyManaged`-`false`, GuardDuty will not receive runtime events for this Amazon ECS cluster.<br />Update the tag to `GuardDutyManaged`-`true` and then redeploy the service.
  - **Extra information:** Tasks started before enabling Automated Agent Configuration are not covered. Impacted task ID(s): '{{`TASK_ID`}}' / **Recommended troubleshooting steps:** When cluster contains a task that launched before enabling the Automated agent configuration for Amazon ECS, then GuardDuty will be unable to protect this. Relaunch the task for it to be monitored by GuardDuty. 
  - **Extra information:** Services deployed before enabling Automated Agent Configuration are not covered. Impacted service name(s): '{{`SERVICE_NAME`}}' / **Recommended troubleshooting steps:** When services are deployed before enabling Automated agent configuration for Amazon ECS, GuardDuty will not receive runtime events for ECS clusters.
  - **Extra information:** Service '{{`SERVICE_NAME`}}' requires a new deployment to fix/troubleshoot. Refer documentation, Impacted service name(s): '{{`SERVICE_NAME`}}' / **Recommended troubleshooting steps:** A service that started before enabling Runtime Monitoring is not supported. <br />You can either restart the service or update the service with `forceNewDeployment` option by following the steps under [Updating an Amazon ECS service using the console](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/update-service-console-v2.html) in the *Amazon Elastic Container Service Developer Guide*. Alternatively, you can also use the steps under [UpdateService](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_UpdateService.html) in the *Amazon Elastic Container Service API Reference*.
  - **Extra information:** Tasks started before enabling Runtime Monitoring require a relaunch. Impacted task ID(s): '{{`TASK_ID_1`}}' / **Recommended troubleshooting steps:** In Amazon ECS, the tasks are immutable. To assess the runtime behavior or a running AWS Fargate task, make sure that Runtime Monitoring is already enabled, and then restart the task for GuardDuty to add the container sidecar.

- **Others**
  - **Extra information:** Unidentified issue, for tasks in `TaskDefinition - '{{TASK_DEFINITION}}'`
  - **Recommended troubleshooting steps:** Use the following questions to identify the root cause of the issue:+  Did the task start before you enabled Runtime Monitoring? <br />In Amazon ECS, the tasks are immutable. To assess the runtime behavior of a running Fargate task, make sure that Runtime Monitoring is already enabled, and then restart the task for GuardDuty to add the container sidecar. <br />+  Is this task part of a service deployment that started before you enabled Runtime Monitoring? <br />If yes, you can either restart the service or update the service with `forceNewDeployment` by using the steps in [Updating a service](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/update-service-console-v2.html).  <br />You can also use [UpdateService](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_UpdateService.html) or [AWS CLI](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecs/update-service.html). <br />+  Did the task launch after excluding the ECS cluster from Runtime Monitoring? <br />When you change the pre-defined GuardDuty tag from `GuardDutyManaged`-`true` to `GuardDutyManaged`-`false`, GuardDuty will not receive the runtime events for the ECS cluster. <br />+  Does your service contain a task that has an old format of `taskArn`? <br />GuardDuty Runtime Monitoring doesn't support the coverage for tasks that have the old format of `taskArn`.  <br />For information about Amazon Resource Names (ARNs) for Amazon ECS resources, see [Amazon Resource Names (ARNs) and IDs](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/ecs-account-settings.html#ecs-resource-ids). 

