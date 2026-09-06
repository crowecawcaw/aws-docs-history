

# Create and manage Amazon EMR clusters with Step Functions
<a name="connect-emr"></a>

Learn how to integrate AWS Step Functions with Amazon EMR using the provided Amazon EMR service integration APIs. The service integration APIs are similar to the corresponding Amazon EMR APIs, with some differences in the fields that are passed and in the responses that are returned.

To learn about integrating with AWS services in Step Functions, see [Integrating services](integrate-services.md) and [Passing parameters to a service API in Step Functions](connect-parameters.md).

**Key features of Optimized Amazon EMR integration**  
The Optimized Amazon EMR service integration has a customized set of APIs that wrap the underlying Amazon EMR APIs, described below. Because of this, it differs significantly from the Amazon EMR AWS SDK service integration.
The [Run a Job (.sync)](connect-to-resource.md#connect-sync) integration pattern is supported.

Step Functions does not terminate an Amazon EMR cluster automatically if execution is stopped. If your state machine stops before your Amazon EMR cluster has terminated, your cluster may continue running indefinitely, and can accrue additional charges. To avoid this, ensure that any Amazon EMR cluster you create is terminated properly. For more information, see:
+ [Control Cluster Termination](https://docs.aws.amazon.com/emr/latest/ManagementGuide/emr-plan-termination.html) in the Amazon EMR User Guide.
+ The Service Integration Patterns [Run a Job (.sync)](connect-to-resource.md#connect-sync) section.

**Note**  
As of `emr-5.28.0`, you can specify the parameter `StepConcurrencyLevel` when creating a cluster to allow multiple steps to run in parallel on a single cluster. You can use the Step Functions `Map` and `Parallel` states to submit work in parallel to the cluster.

The availability of Amazon EMR service integration is subject to the availability of Amazon EMR APIs. See [Amazon EMR](https://docs.aws.amazon.com/govcloud-us/latest/UserGuide/govcloud-emr.html) documentation for limitations in special regions.

**Note**  
For integration with Amazon EMR, Step Functions has a hard-coded 60 seconds job polling frequency for the first 10 minutes and 300 seconds after that.

## Optimized Amazon EMR APIs
<a name="connect-emr-api"></a>

The following table describes the differences between each Amazon EMR service integration API and corresponding Amazon EMR APIs.


| Amazon EMR Service Integration API | Corresponding EMR API | Differences | 
| --- | --- | --- | 
| createClusterCreates and starts running a cluster (job flow). <br /> Amazon EMR is linked directly to a unique type of IAM role known as a service-linked role. For `createCluster` and `createCluster.sync` to work, you must have configured the necessary permissions to create the service-linked role `AWSServiceRoleForEMRCleanup`. For more information about this, including a statement you can add to your IAM permissions policy, see [Using the Service-Linked Role for Amazon EMR](https://docs.aws.amazon.com/emr/latest/ManagementGuide/using-service-linked-roles.html).  | [runJobFlow](https://docs.aws.amazon.com/emr/latest/APIReference/API_RunJobFlow.html) | createCluster uses the same request syntax as [runJobFlow](https://docs.aws.amazon.com/emr/latest/APIReference/API_RunJobFlow.html), except for the following: +  The field `Instances.KeepJobFlowAliveWhenNoSteps` is mandatory, and must have the Boolean value `TRUE`. <br />+  The field `Steps` is not allowed. <br />+  The field `Instances.InstanceFleets[index].Name` should be provided and must be unique if the optional `modifyInstanceFleetByName` connector API is used. <br />+  The field `Instances.InstanceGroups[index].Name` should be provided and must be unique if the optional `modifyInstanceGroupByName` API is used. Response is this: <pre>{<br />  "ClusterId": "string"<br />}</pre> Amazon EMR uses this: <pre>{<br />  "JobFlowId": "string"<br />}</pre>  | 
| createCluster.syncCreates and starts running a cluster (job flow).  | [runJobFlow](https://docs.aws.amazon.com/emr/latest/APIReference/API_RunJobFlow.html) | The same as createCluster, but waits for the cluster to reach the WAITING state. | 
| setClusterTerminationProtectionLocks a cluster (job flow) so the EC2 instances in the cluster cannot be terminated by user intervention, an API call, or a job-flow error. | [setTerminationProtection](https://docs.aws.amazon.com/emr/latest/APIReference/API_SetTerminationProtection.html) | Request uses this:<pre>{<br />  "ClusterId": "string"<br />}</pre> Amazon EMR uses this:<pre>{<br />  "JobFlowIds": ["string"]<br />}</pre>  | 
| terminateClusterShuts down a cluster (job flow). | [terminateJobFlows](https://docs.aws.amazon.com/emr/latest/APIReference/API_TerminateJobFlows.html) | Request uses this:<pre>{<br />  "ClusterId": "string"<br />}</pre> Amazon EMR uses this:<pre>{<br />  "JobFlowIds": ["string"]<br />}</pre> | 
| terminateCluster.syncShuts down a cluster (job flow). | [terminateJobFlows](https://docs.aws.amazon.com/emr/latest/APIReference/API_TerminateJobFlows.html) | The same as terminateCluster, but waits for the cluster to terminate. | 
| addStepAdds a new step to a running cluster.<br />Optionally, you can also specify the `[ExecutionRoleArn](https://docs.aws.amazon.com/emr/latest/APIReference/API_AddJobFlowSteps.html#EMR-AddJobFlowSteps-request-ExecutionRoleArn)` parameter while using this API. | [addJobFlowSteps](https://docs.aws.amazon.com/emr/latest/APIReference/API_AddJobFlowSteps.html) | Request uses the key "ClusterId". Amazon EMR uses "JobFlowId". Request uses a single step.<pre>{<br />  "Step": <"StepConfig object"><br />}</pre> Amazon EMR uses this:<pre>{<br />  "Steps": [<StepConfig objects>]<br />}</pre> Response is this:<pre>{<br />  "StepId": "string"<br />}</pre> Amazon EMR returns this:<pre>{<br />  "StepIds": [<strings>]<br />}</pre>  | 
| addStep.syncAdds a new step to a running cluster.<br />Optionally, you can also specify the `[ExecutionRoleArn](https://docs.aws.amazon.com/emr/latest/APIReference/API_AddJobFlowSteps.html#EMR-AddJobFlowSteps-request-ExecutionRoleArn)` parameter while using this API. | [addJobFlowSteps](https://docs.aws.amazon.com/emr/latest/APIReference/API_AddJobFlowSteps.html) | The same as addStep, but waits for the step to complete. | 
| cancelStepCancels a pending step in a running cluster. | [cancelSteps](https://docs.aws.amazon.com/emr/latest/APIReference/API_CancelSteps.html) |  Request uses this:<pre>{<br />  "StepId": "string"<br />}</pre> Amazon EMR uses this:<pre>{<br />  "StepIds": [<strings>]<br />}</pre> Response is this:<pre>{<br />  "CancelStepsInfo": <CancelStepsInfo object><br />}</pre> Amazon EMR uses this:<pre>{<br />  "CancelStepsInfoList": [<CancelStepsInfo objects>]<br />}</pre>  | 
| modifyInstanceFleetByNameModifies the target On-Demand and target Spot capacities for the instance fleet with the specified `InstanceFleetName`. | [modifyInstanceFleet](https://docs.aws.amazon.com/emr/latest/APIReference/API_ModifyInstanceFleet.html) | Request is the same as for modifyInstanceFleet, except for the following: +  The field `Instance.InstanceFleetId` is not allowed. <br />+  At runtime the `InstanceFleetId` is determined automatically by the service integration by calling `ListInstanceFleets` and parsing the result.   | 
| modifyInstanceGroupByNameModifies the number of nodes and configuration settings of an instance group. | [modifyInstanceGroups](https://docs.aws.amazon.com/emr/latest/APIReference/API_ModifyInstanceGroups.html) | Request is this:<pre>{<br />  "ClusterId": "string",<br />  "InstanceGroup": <InstanceGroupModifyConfig object><br />}</pre> Amazon EMR uses a list: <pre>{<br />  "ClusterId": ["string"],<br />  "InstanceGroups": [<InstanceGroupModifyConfig objects>]<br />}</pre>Within the `InstanceGroupModifyConfig` object, the field `InstanceGroupId` is not allowed.<br />A new field, `InstanceGroupName`, has been added. At runtime the `InstanceGroupId` is determined automatically by the service integration by calling `ListInstanceGroups` and parsing the result. | 

## Workflow example
<a name="connect-emr-api-examples"></a>

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
        "LogUri": "s3n://aws-logs-{{account-id}}-us-east-1/elasticmapreduce/",
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
        "ExecutionRoleArn": "arn:aws:iam::{{account-id}}:role/{{myEMR-execution-role}}",
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
                    "s3://{{region}}.elasticmapreduce.samples/cloudfront/code/Hive_CloudFront.q",
                    "-d",
                    "INPUT=s3://{{region}}.elasticmapreduce.samples",
                    "-d",
                    "OUTPUT=s3://{{<amzn-s3-demo-bucket>}}/MyHiveQueryResults/"
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

The following includes a `Task` state that scales a cluster up or down for an instance group.

```
"ModifyInstanceGroupByName": {
    "Type": "Task",
    "Resource": "arn:aws:states:::elasticmapreduce:modifyInstanceGroupByName",
    "Arguments": {
        "ClusterId": "j-{{account-id}}3",
        "InstanceGroupName": "MyCoreGroup",
        "InstanceGroup": {
            "InstanceCount": 8
        }
    },
    "End": true
}
```

The following includes a `Task` state that scales a cluster up or down for an instance fleet.

```
"ModifyInstanceFleetByName": {
    "Type": "Task",
    "Resource": "arn:aws:states:::elasticmapreduce:modifyInstanceFleetByName",
    "Arguments": {
        "ClusterId": "j-{{account-id}}3",
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
<a name="emr-iam"></a>

The following example templates show how AWS Step Functions generates IAM policies based on the resources in your state machine definition. For more information, see [How Step Functions generates IAM policies for integrated services](service-integration-iam-templates.md) and [Discover service integration patterns in Step Functions](connect-to-resource.md).

### `addStep`
<a name="emr-iam-addstep"></a>

*Static resources*

****  

```
{
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
                "arn:aws:elasticmapreduce:us-east-1:{{123456789012}}:cluster/{{clusterId}}"
            ]
        }
    ]
}
```

*Dynamic resources*

****  

```
{
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
}
```

### `cancelStep`
<a name="emr-iam-cancelstep"></a>

*Static resources*

****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "elasticmapreduce:CancelSteps",
            "Resource": [
                "arn:aws:elasticmapreduce:{{us-east-1}}:{{123456789012}}:cluster/myCluster-id"
            ]
        }
    ]
}
```

*Dynamic resources*

****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "elasticmapreduce:CancelSteps",
            "Resource": "arn:aws:elasticmapreduce:*:*:cluster/*"
        }
    ]
}
```

### `createCluster`
<a name="emr-iam-createcluster"></a>

*Static resources*

****  

```
{
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
        "arn:aws:iam::{{123456789012}}:role/{{myRoleName}}"
      ]
    }
  ]
}
```

### `setClusterTerminationProtection`
<a name="emr-iam-clusterterminationprotection"></a>

*Static resources*

****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "elasticmapreduce:SetTerminationProtection",
            "Resource": [
                "arn:aws:elasticmapreduce:{{us-east-1}}:{{123456789012}}:cluster/myCluster-id"
            ]
        }
    ]
}
```

*Dynamic resources*

****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
        {
            "Effect": "Allow",
            "Action": "elasticmapreduce:SetTerminationProtection",
            "Resource": "arn:aws:elasticmapreduce:*:*:cluster/*"
        }
    ]
}
```

### `modifyInstanceFleetByName`
<a name="emr-iam-modifyinstancefleetbyname"></a>

*Static resources*

****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "elasticmapreduce:ModifyInstanceFleet",
                "elasticmapreduce:ListInstanceFleets"
            ],
            "Resource": [
                "arn:aws:elasticmapreduce:{{us-east-1}}:{{123456789012}}:cluster/myCluster-id"
            ]
        }
    ]
}
```

*Dynamic resources*

****  

```
{
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
}
```

### `modifyInstanceGroupByName`
<a name="emr-iam-modifyinstancegroupbyname"></a>

*Static resources*

****  

```
{
    "Version":"2012-10-17",		 	 	 
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "elasticmapreduce:ModifyInstanceGroups",
                "elasticmapreduce:ListInstanceGroups"
            ],
            "Resource": [
                "arn:aws:elasticmapreduce:{{us-east-1}}:{{123456789012}}:cluster/myCluster-id"
            ]
        }
    ]
}
```

*Dynamic resources*

****  

```
{
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
}
```

### `terminateCluster`
<a name="emr-iam-terminatecluster"></a>

*Static resources*

****  

```
{
  "Version":"2012-10-17",		 	 	 
  "Statement": [
    {
      "Effect": "Allow",
      "Action": [
        "elasticmapreduce:TerminateJobFlows",
        "elasticmapreduce:DescribeCluster"
      ],
      "Resource": [
        "arn:aws:elasticmapreduce:{{us-east-1}}:{{123456789012}}:cluster/myCluster-id"
      ]
    }
  ]
}
```

*Dynamic resources*

****  

```
{
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
}
```