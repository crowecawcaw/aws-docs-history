# Create and manage Amazon EMR clusters with Step Functions

Learn how to integrate AWS Step Functions with Amazon EMR using the provided Amazon EMR service integration
APIs. The service integration APIs are similar to the corresponding Amazon EMR APIs, with some
differences in the fields that are passed and in the responses that are returned.

To learn about integrating with AWS services in Step Functions, see [Integrating services](integrate-services.md "integrate-services.md") and [Passing parameters to a service API in Step Functions](connect-parameters.md "connect-parameters.md").

###### Key features of Optimized Amazon EMR integration

- The Optimized Amazon EMR service integration has a customized set of APIs that wrap the
  underlying Amazon EMR APIs, described below. Because of this, it differs significantly from
  the Amazon EMR AWS SDK service integration.
- The [Run a Job (.sync)](connect-to-resource.md#connect-sync "connect-to-resource.md#connect-sync") integration pattern is supported.
  Step Functions does not terminate an Amazon EMR cluster automatically if execution is stopped. If your
  state machine stops before your Amazon EMR cluster has terminated, your cluster may continue
  running indefinitely, and can accrue additional charges. To avoid this, ensure that any
  Amazon EMR cluster you create is terminated properly. For more information, see:

- [Control Cluster
  Termination](../../../emr/latest/ManagementGuide/emr-plan-termination.md "../../../emr/latest/ManagementGuide/emr-plan-termination.md") in the Amazon EMR User Guide.
- The Service Integration Patterns [Run a Job (.sync)](connect-to-resource.md#connect-sync "connect-to-resource.md#connect-sync") section.

###### Note

As of `emr-5.28.0`, you can specify the parameter
`StepConcurrencyLevel` when creating a cluster to allow multiple steps to
run in parallel on a single cluster. You can use the Step Functions `Map` and
`Parallel` states to submit work in parallel to the cluster.

The availability of Amazon EMR service integration is subject to the availability of Amazon EMR
APIs. See [Amazon EMR](../../../govcloud-us/latest/UserGuide/govcloud-emr.md "../../../govcloud-us/latest/UserGuide/govcloud-emr.md") documentation for
limitations in special regions.

###### Note

For integration with Amazon EMR, Step Functions has a hard-coded 60 seconds job polling frequency for the first 10 minutes and 300 seconds after that.

## Optimized Amazon EMR APIs

The following table describes the differences between each Amazon EMR service integration API and corresponding Amazon EMR APIs.

| Amazon EMR Service Integration API                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          | Corresponding EMR API                                                                                                                                           | Differences                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| ----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| _createCluster_<br>Creates and starts running a cluster (job flow). Amazon EMR<br>is linked directly to a unique type of IAM role known as a<br>service-linked role. For `createCluster` and<br>`createCluster.sync` to work, you must have configured<br>the necessary permissions to create the service-linked role<br>`AWSServiceRoleForEMRCleanup`. For more information about<br>this, including a statement you can add to your IAM permissions<br>policy, see [Using the Service-Linked Role for Amazon EMR](../../../emr/latest/ManagementGuide/using-service-linked-roles.md "../../../emr/latest/ManagementGuide/using-service-linked-roles.md"). | [runJobFlow](../../../emr/latest/APIReference/API_RunJobFlow.md "../../../emr/latest/APIReference/API_RunJobFlow.md")                                           | `createCluster` uses the same request syntax as [runJobFlow](../../../emr/latest/APIReference/API_RunJobFlow.md "../../../emr/latest/APIReference/API_RunJobFlow.md"), except for the following:<br>• The field `Instances.KeepJobFlowAliveWhenNoSteps`<br>is mandatory, and must have the Boolean value<br>`TRUE`.<br>• The field `Steps` is not allowed.<br>• The field `Instances.InstanceFleets[index].Name`<br>should be provided and must be unique if the optional<br>`modifyInstanceFleetByName` connector API is<br>used.<br>• The field `Instances.InstanceGroups[index].Name`<br>should be provided and must be unique if the optional<br>`modifyInstanceGroupByName` API is used.<br>Response is this:<br>`<br>{<br>"ClusterId": "string"<br>}<br>`<br>Amazon EMR uses this:<br>`<br>{<br>"JobFlowId": "string"<br>}<br>` |
| _createCluster.sync_<br>Creates and starts running a cluster (job flow).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | [runJobFlow](../../../emr/latest/APIReference/API_RunJobFlow.md "../../../emr/latest/APIReference/API_RunJobFlow.md")                                           | The same as `createCluster`, but waits for the cluster to<br>reach the `WAITING` state.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| _setClusterTerminationProtection_<br>Locks a cluster (job flow) so the EC2 instances in the cluster cannot<br>be terminated by user intervention, an API call, or a job-flow<br>error.                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | [setTerminationProtection](../../../emr/latest/APIReference/API_SetTerminationProtection.md "../../../emr/latest/APIReference/API_SetTerminationProtection.md") | Request uses<br>this:<br>`<br>{<br>"ClusterId": "string"<br>}<br>`<br>Amazon EMR uses<br>this:<br>`<br>{<br>"JobFlowIds": ["string"]<br>}<br>`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| _terminateCluster_<br>Shuts down a cluster (job flow).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      | [terminateJobFlows](../../../emr/latest/APIReference/API_TerminateJobFlows.md "../../../emr/latest/APIReference/API_TerminateJobFlows.md")                      | Request uses<br>this:<br>`<br>{<br>"ClusterId": "string"<br>}<br>`<br>Amazon EMR uses<br>this:<br>`<br>{<br>"JobFlowIds": ["string"]<br>}<br>`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |
| *terminateCluster.sync*Shuts down a cluster (job<br>flow).                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | [terminateJobFlows](../../../emr/latest/APIReference/API_TerminateJobFlows.md "../../../emr/latest/APIReference/API_TerminateJobFlows.md")                      | The same as `terminateCluster`, but waits for the cluster to<br>terminate.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| _addStep_<br>Adds a new step to a running cluster.<br>Optionally, you can also specify the<br>`ExecutionRoleArn`<br>parameter while using this API.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         | [addJobFlowSteps](../../../emr/latest/APIReference/API_AddJobFlowSteps.md "../../../emr/latest/APIReference/API_AddJobFlowSteps.md")                            | Request uses the key `"ClusterId"`. Amazon EMR uses<br>`"JobFlowId"`. Request uses a single<br>step.<br>`<br>{<br>"Step": <"StepConfig object"><br>}<br>`<br>Amazon EMR uses<br>this:<br>`<br>{<br>"Steps": [<StepConfig objects>]<br>}<br>`<br>Response is<br>this:<br>`<br>{<br>"StepId": "string"<br>}<br>`<br>Amazon EMR returns<br>this:<br>`<br>{<br>"StepIds": [<strings>]<br>}<br>`                                                                                                                                                                                                                                                                                                                                                                                                                                           |
| _addStep.sync_<br>Adds a new step to a running cluster.<br>Optionally, you can also specify the<br>`ExecutionRoleArn`<br>parameter while using this API.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    | [addJobFlowSteps](../../../emr/latest/APIReference/API_AddJobFlowSteps.md "../../../emr/latest/APIReference/API_AddJobFlowSteps.md")                            | The same as `addStep`, but waits for the step to<br>complete.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |
| _cancelStep_<br>Cancels a pending step in a running cluster.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | [cancelSteps](../../../emr/latest/APIReference/API_CancelSteps.md "../../../emr/latest/APIReference/API_CancelSteps.md")                                        | Request uses<br>this:<br>`<br>{<br>"StepId": "string"<br>}<br>`<br>Amazon EMR uses<br>this:<br>`<br>{<br>"StepIds": [<strings>]<br>}<br>`<br>Response is<br>this:<br>`<br>{<br>"CancelStepsInfo": <CancelStepsInfo object><br>}<br>`<br>Amazon EMR uses<br>this:<br>`<br>{<br>"CancelStepsInfoList": [<CancelStepsInfo objects>]<br>}<br>`                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            |
| _modifyInstanceFleetByName_<br>Modifies the target On-Demand and target Spot capacities for the<br>instance fleet with the specified<br>`InstanceFleetName`.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                | [modifyInstanceFleet](../../../emr/latest/APIReference/API_ModifyInstanceFleet.md "../../../emr/latest/APIReference/API_ModifyInstanceFleet.md")                | Request is the same as for `modifyInstanceFleet`, except for<br>the following:<br>• The field `Instance.InstanceFleetId` is not<br>allowed.<br>• At runtime the `InstanceFleetId` is determined<br>automatically by the service integration by calling<br>`ListInstanceFleets` and parsing the<br>result.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             |
| _modifyInstanceGroupByName_<br>Modifies the number of nodes and configuration settings of an instance<br>group.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             | [modifyInstanceGroups](../../../emr/latest/APIReference/API_ModifyInstanceGroups.md "../../../emr/latest/APIReference/API_ModifyInstanceGroups.md")             | Request is<br>this:<br>`<br>{<br>"ClusterId": "string",<br>"InstanceGroup": <InstanceGroupModifyConfig object><br>}<br>`<br>Amazon EMR uses a list:<br>`<br>{<br>"ClusterId": ["string"],<br>"InstanceGroups": [<InstanceGroupModifyConfig objects>]<br>}<br>`<br>Within the `InstanceGroupModifyConfig` object, the field<br>`InstanceGroupId` is not allowed.<br>A new field, `InstanceGroupName`, has been added. At<br>runtime the `InstanceGroupId` is determined automatically by<br>the service integration by calling `ListInstanceGroups` and<br>parsing the result.                                                                                                                                                                                                                                                         |

## Workflow example

The following includes a `Task` state that creates a cluster.

```
"Create_Cluster": {
    "Type": "Task",
    "Resource": "arn:aws:states:::elasticmapreduce:createCluster.sync",
    "Arguments": {
        "Name": "MyWorkflowCluster",
        "VisibleToAllUsers": true,
        "ReleaseLabel": "emr-5.28.0",
        "Applications": [
            {
                "Name": "Hive"
            }
        ],
        "ServiceRole": "EMR_DefaultRole",
        "JobFlowRole": "EMR_EC2_DefaultRole",
        "LogUri": "s3n://aws-logs-`account-id`-us-east-1/elasticmapreduce/",
        "Instances": {
            "KeepJobFlowAliveWhenNoSteps": true,
            "InstanceFleets": [
                {
                    "InstanceFleetType": "MASTER",
                    "Name": "MASTER",
                    "TargetOnDemandCapacity": 1,
                    "InstanceTypeConfigs": [
                        {
                            "InstanceType": "m4.xlarge"
                        }
                    ]
                },
                {
                    "InstanceFleetType": "CORE",
                    "Name": "CORE",
                    "TargetOnDemandCapacity": 1,
                    "InstanceTypeConfigs": [
                        {
                            "InstanceType": "m4.xlarge"
                        }
                    ]
                }
            ]
        }
    },
    "End": true
}
```

The following includes a `Task` state that enables termination protection.

```
"Enable_Termination_Protection": {
    "Type": "Task",
    "Resource": "arn:aws:states:::elasticmapreduce:setClusterTerminationProtection",
    "Arguments": {
        "ClusterId": "{% $ClusterId %}",
        "TerminationProtected": true
    },
    "End": true
}
```

The following includes a `Task` state that submits a step to a cluster.

```
"Step_One": {
    "Type": "Task",
    "Resource": "arn:aws:states:::elasticmapreduce:addStep.sync",
    "Arguments": {
        "ClusterId": "{% $ClusterId %}",
        "ExecutionRoleArn": "arn:aws:iam::`account-id`:role/`myEMR-execution-role`",
        "Step": {
            "Name": "The first step",
            "ActionOnFailure": "TERMINATE_CLUSTER",
            "HadoopJarStep": {
                "Jar": "command-runner.jar",
                "Args": [
                    "hive-script",
                    "--run-hive-script",
                    "--args",
                    "-f",
                    "s3://`region`.elasticmapreduce.samples/cloudfront/code/Hive_CloudFront.q",
                    "-d",
                    "INPUT=s3://`region`.elasticmapreduce.samples",
                    "-d",
                    "OUTPUT=s3://`<amzn-s3-demo-bucket>`/MyHiveQueryResults/"
                ]
            }
        }
    },
    "End": true
}
```

The following includes a `Task` state that cancels a step.

```
"Cancel_Step_One": {
    "Type": "Task",
    "Resource": "arn:aws:states:::elasticmapreduce:cancelStep",
    "Arguments": {
        "ClusterId": "{% $ClusterId %}",
        "StepId": "{% $AddStepsResult.StepId %}"
    },
    "End": true
}
```

The following includes a `Task` state that terminates a cluster.

```
"Terminate_Cluster": {
    "Type": "Task",
    "Resource": "arn:aws:states:::elasticmapreduce:terminateCluster.sync",
    "Arguments": {
        "ClusterId": "{% $ClusterId %}",
    },
    "End": true
}
```

The following includes a `Task` state that scales a cluster up or down for an
instance group.

```

"ModifyInstanceGroupByName": {
    "Type": "Task",
    "Resource": "arn:aws:states:::elasticmapreduce:modifyInstanceGroupByName",
    "Arguments": {
        "ClusterId": "j-`account-id`3",
        "InstanceGroupName": "MyCoreGroup",
        "InstanceGroup": {
            "InstanceCount": 8
        }
    },
    "End": true
}
```

The following includes a `Task` state that scales a cluster up or down for an
instance fleet.

```
"ModifyInstanceFleetByName": {
    "Type": "Task",
    "Resource": "arn:aws:states:::elasticmapreduce:modifyInstanceFleetByName",
    "Arguments": {
        "ClusterId": "j-`account-id`3",
        "InstanceFleetName": "MyCoreFleet",
        "InstanceFleet": {
            "TargetOnDemandCapacity": 8,
            "TargetSpotCapacity": 0
        }
    },
    "End": true
}
```

## IAM policies for calling Amazon EMR

The following example templates show how AWS Step Functions generates IAM policies based on the resources in your state machine definition. For more information, see [How Step Functions generates IAM policies for integrated
services](service-integration-iam-templates.md "service-integration-iam-templates.md") and [Discover service integration patterns in Step Functions](connect-to-resource.md "connect-to-resource.md").

### `addStep`

_Static resources_

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "elasticmapreduce:AddJobFlowSteps",
 "elasticmapreduce:DescribeStep",
 "elasticmapreduce:CancelSteps"
 ],
 "Resource": [
 "arn:aws:elasticmapreduce:us-east-1:`123456789012`:cluster/`clusterId`"
 ]
 }
 ]
}`

```

_Dynamic resources_

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "elasticmapreduce:AddJobFlowSteps",
 "elasticmapreduce:DescribeStep",
 "elasticmapreduce:CancelSteps"
 ],
 "Resource": "arn:aws:elasticmapreduce:*:*:cluster/*"
 }
 ]
}`

```

### `cancelStep`

_Static resources_

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": "elasticmapreduce:CancelSteps",
 "Resource": [
 "arn:aws:elasticmapreduce:`us-east-1`:`123456789012`:cluster/myCluster-id"
 ]
 }
 ]
}`

```

_Dynamic resources_

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": "elasticmapreduce:CancelSteps",
 "Resource": "arn:aws:elasticmapreduce:*:*:cluster/*"
 }
 ]
}`

```

### `createCluster`

_Static resources_

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "elasticmapreduce:RunJobFlow",
 "elasticmapreduce:DescribeCluster",
 "elasticmapreduce:TerminateJobFlows"
 ],
 "Resource": "*"
 },
 {
 "Effect": "Allow",
 "Action": "iam:PassRole",
 "Resource": [
 "arn:aws:iam::`123456789012`:role/`myRoleName`"
 ]
 }
 ]
}`

```

### `setClusterTerminationProtection`

_Static resources_

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": "elasticmapreduce:SetTerminationProtection",
 "Resource": [
 "arn:aws:elasticmapreduce:`us-east-1`:`123456789012`:cluster/myCluster-id"
 ]
 }
 ]
}`

```

_Dynamic resources_

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": "elasticmapreduce:SetTerminationProtection",
 "Resource": "arn:aws:elasticmapreduce:*:*:cluster/*"
 }
 ]
}`

```

### `modifyInstanceFleetByName`

_Static resources_

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "elasticmapreduce:ModifyInstanceFleet",
 "elasticmapreduce:ListInstanceFleets"
 ],
 "Resource": [
 "arn:aws:elasticmapreduce:`us-east-1`:`123456789012`:cluster/myCluster-id"
 ]
 }
 ]
}`

```

_Dynamic resources_

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "elasticmapreduce:ModifyInstanceFleet",
 "elasticmapreduce:ListInstanceFleets"
 ],
 "Resource": "arn:aws:elasticmapreduce:*:*:cluster/*"
 }
 ]
}`

```

### `modifyInstanceGroupByName`

_Static resources_

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "elasticmapreduce:ModifyInstanceGroups",
 "elasticmapreduce:ListInstanceGroups"
 ],
 "Resource": [
 "arn:aws:elasticmapreduce:`us-east-1`:`123456789012`:cluster/myCluster-id"
 ]
 }
 ]
}`

```

_Dynamic resources_

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "elasticmapreduce:ModifyInstanceGroups",
 "elasticmapreduce:ListInstanceGroups"
 ],
 "Resource": "*"
 }
 ]
}`

```

### `terminateCluster`

_Static resources_

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "elasticmapreduce:TerminateJobFlows",
 "elasticmapreduce:DescribeCluster"
 ],
 "Resource": [
 "arn:aws:elasticmapreduce:`us-east-1`:`123456789012`:cluster/myCluster-id"
 ]
 }
 ]
}`

```

_Dynamic resources_

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": [
 "elasticmapreduce:TerminateJobFlows",
 "elasticmapreduce:DescribeCluster"
 ],
 "Resource": "arn:aws:elasticmapreduce:*:*:cluster/*"
 }
 ]
}`

```
