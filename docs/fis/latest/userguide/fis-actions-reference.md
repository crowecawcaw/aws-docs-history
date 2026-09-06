

# AWS FIS Actions reference
<a name="fis-actions-reference"></a>

An action is the fault injection activity that you run on a target using AWS Fault Injection Service (AWS FIS). AWS FIS provides preconfigured actions for specific types of targets across AWS services. You add actions to an experiment template, which you then use to run experiments.

This reference describes the common actions in AWS FIS, including information about the action parameters and the required IAM permissions. You can also list the supported AWS FIS actions using the AWS FIS console or the [list-actions](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/fis/list-actions.html) command from the AWS Command Line Interface (AWS CLI). Once you have the name of a specific action, you can view detailed information about the action by using the [get-action](https://docs.aws.amazon.com/cli/latest/reference/fis/get-action.html) command. For more information on using AWS FIS commands with the AWS CLI, see the [AWS Command Line Interface User Guide](https://docs.aws.amazon.com/cli/latest/userguide/) and [fis](https://docs.aws.amazon.com/cli/latest/reference/fis/index.html) in the *AWS CLI Command Reference*. 

For more information on how AWS FIS actions work, see [Actions for AWS FIS](action-sequence.md) and [How AWS Fault Injection Service works with IAM](security_iam_service-with-iam.md).

**Topics**
+ [Fault injection actions](#fis-actions-reference-fis)
+ [Recovery action](#fis-actions-recovery)
+ [Wait action](#fis-actions-reference-wait)
+ [Amazon CloudWatch actions](#cloudwatch-actions-reference)
+ [Amazon DynamoDB actions](#dynamodb-actions-reference)
+ [Amazon Aurora DSQL actions](#dsql-actions-reference)
+ [Amazon EBS actions](#ebs-actions-reference)
+ [Amazon EC2 actions](#ec2-actions-reference)
+ [Amazon ECS actions](#ecs-actions-reference)
+ [Amazon EKS actions](#eks-actions-reference)
+ [Amazon ElastiCache actions](#elasticache-actions-reference)
+ [Amazon Kinesis Data Streams actions](#aws-kinesis-actions)
+ [AWS Lambda actions](#aws-lambda-actions-reference)
+ [Amazon MemoryDB action](#memorydb-actions-reference)
+ [Network actions](#network-actions-reference)
+ [Amazon RDS actions](#rds-actions-reference)
+ [Amazon S3 actions](#s3-actions-reference-fis)
+ [Systems Manager actions](#ssm-actions-reference)
+ [AWS Direct Connect actions](#directconnect-actions-reference)
+ [Use Systems Manager SSM documents with AWS FIS](actions-ssm-agent.md)
+ [Use the AWS FIS aws:ecs:task actions](ecs-task-actions.md)
+ [Use the AWS FIS aws:eks:pod actions](eks-pod-actions.md)
+ [Use the AWS FIS aws:lambda:function actions](use-lambda-actions.md)

## Fault injection actions
<a name="fis-actions-reference-fis"></a>

AWS FIS supports the following fault injection actions.

**Topics**
+ [aws:fis:inject-api-internal-error](#inject-api-internal-error)
+ [aws:fis:inject-api-throttle-error](#inject-api-throttle-error)
+ [aws:fis:inject-api-unavailable-error](#inject-api-unavailable-error)

### aws:fis:inject-api-internal-error
<a name="inject-api-internal-error"></a>

Injects Internal Errors into requests made by the the target IAM role. The specific response depends on each service and API. For more information, please review the SDK and API documentation of your service.

**Resource type**
+ **aws:iam:role**

**Parameters**
+ **duration** – The duration, from one minute to 12 hours. In the AWS FIS API, the value is a string in ISO 8601 format. For example, PT1M represents one minute. In the AWS FIS console, you enter the number of seconds, minutes, or hours.
+ **service** – The target AWS API namespace. The supported value is `ec2` and `kinesis`.
+ **percentage** – The percentage (1-100) of calls to inject the fault into.
+ **operations** – The operations to inject the fault into, separated using commas. For a list of the API actions for the `ec2` namespace, see [Amazon EC2 API Reference](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_Operations.html) and [Amazon Kinesis Data Streams API Reference](https://docs.aws.amazon.com/kinesis/latest/APIReference/API_Operations.html). 

**Permissions**
+ `fis:InjectApiInternalError`

### aws:fis:inject-api-throttle-error
<a name="inject-api-throttle-error"></a>

Injects throttling errors into requests made by the target IAM role. The specific response depends on each service and API. For more information, please review the SDK and API documentation of your service.

**Resource type**
+ **aws:iam:role**

**Parameters**
+ **duration** – The duration, from one minute to 12 hours. In the AWS FIS API, the value is a string in ISO 8601 format. For example, PT1M represents one minute. In the AWS FIS console, you enter the number of seconds, minutes, or hours.
+ **service** – The target AWS API namespace. The supported value is `ec2` and `kinesis`.
+ **percentage** – The percentage (1-100) of calls to inject the fault into.
+ **operations** – The operations to inject the fault into, separated using commas. For a list of the API actions for the `ec2` namespace, see [Amazon EC2 API Reference](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_Operations.html) and [Amazon Kinesis Data Streams API Reference](https://docs.aws.amazon.com/kinesis/latest/APIReference/API_Operations.html). 

**Permissions**
+ `fis:InjectApiThrottleError`

### aws:fis:inject-api-unavailable-error
<a name="inject-api-unavailable-error"></a>

Injects Unavailable errors into requests made by the target IAM role. The specific response depends on each service and API. For more information, please review the SDK and API documentation of your service.

**Resource type**
+ **aws:iam:role**

**Parameters**
+ **duration** – The duration, from one minute to 12 hours. In the AWS FIS API, the value is a string in ISO 8601 format. For example, PT1M represents one minute. In the AWS FIS console, you enter the number of seconds, minutes, or hours.
+ **service** – The target AWS API namespace. The supported value is `ec2` and `kinesis`.
+ **percentage** – The percentage (1-100) of calls to inject the fault into.
+ **operations** – The operations to inject the fault into, separated using commas. For a list of the API actions for the `ec2` namespace, see [Amazon EC2 API Reference](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_Operations.html) and [Amazon Kinesis Data Streams API Reference](https://docs.aws.amazon.com/kinesis/latest/APIReference/API_Operations.html). 

**Permissions**
+ `fis:InjectApiUnavailableError`

## Recovery action
<a name="fis-actions-recovery"></a>

Recovery actions are performed to mitigate risk or protect applications after impairment.

AWS FIS supports the following recovery actions.

### aws:arc:start-zonal-autoshift
<a name="recovery"></a>

Automatically shifts traffic for supported resources away from a potentially impaired Availability Zone (AZ) and reroutes them to healthy AZs in the same AWS Region. This allows for experiencing zonal autoshift through FIS. Zonal autoshift is a capability in Amazon Application Recovery Controller (ARC) that allows AWS to shift traffic for a resource away from an AZ, on your behalf, when AWS determines that there is an impairment that could potentially affect customers in the AZ.

When you run the `aws:arc:start-zonal-autoshift` action, AWS FIS manages the zonal shift using the StartZonalShift, UpdateZonalShift, and CancelZonalShift APIs with the `expiresIn` field for these requests set to 1 minute as a safety mechanism. This enables AWS FIS to quickly rollback the zonal shift in the case of any unexpected events such as network outages or system issues. In the ARC console, the expiration time field will display AWS FIS-managed, and the actual expected expiration is determined by the duration specified in the zonal shift action.

**Resource type**
+ **aws:arc:zonal-shift-managed-resource**

  Zonal shift managed resources are resource types including Amazon EKS clusters, Amazon EC2 Application and Network Load Balancers, and Amazon EC2 Auto Scaling groups that can be enabled for ARC zonal autoshift. For more information, see [supported resources](https://docs.aws.amazon.com/r53recovery/latest/dg/arc-zonal-shift.resource-types.html) and [enabling zonal autoshift resources](https://docs.aws.amazon.com/r53recovery/latest/dg/arc-zonal-autoshift.start-cancel.html) in the *ARC Developer Guide*.

**Parameters**
+ **duration** – The length of time for which traffic will be shifted. In the AWS FIS API, the value is a string in ISO 8601 format. For example, PT1M represents one minute. In the AWS FIS console, you enter the number of seconds, minutes, or hours.
+ **availabilityZoneIdentifier** – Traffic moves away from this AZ. This can be an AZ name (us-east-1a) or AZ ID (use1-az1).
+ **managedResourceTypes** – The resource types from which traffic will be shifted, separated by commas. Possible options are `ASG` (Auto Scaling Group), `ALB` (Application Load Balancer), `NLB` (Network Load Balancer), and `EKS` (Amazon EKS). 
+ **zonalAutoshiftStatus** – The `zonalAutoshiftStatus` status of the resources that you want to target. Possible options are `ENABLED` `DISABLED`, and `ANY`. The default is `ENABLED`.

**Permissions**
+ arc-zonal-shift:StartZonalShift
+ arc-zonal-shift:GetManagedResource
+ arc-zonal-shift:UpdateZonalShift
+ arc-zonal-shift:CancelZonalShift
+ arc-zonal-shift:ListManagedResources
+ autoscaling:DescribeTags
+ tag:GetResources

## Wait action
<a name="fis-actions-reference-wait"></a>

AWS FIS supports the following wait action.

### aws:fis:wait
<a name="wait"></a>

Runs the AWS FIS wait action.

**Parameters**
+ **duration** – The duration, from one minute to 12 hours. In the AWS FIS API, the value is a string in ISO 8601 format. For example, PT1M represents one minute. In the AWS FIS console, you enter the number of seconds, minutes, or hours.

**Permissions**
+ None

## Amazon CloudWatch actions
<a name="cloudwatch-actions-reference"></a>

AWS FIS supports the following Amazon CloudWatch action.

### aws:cloudwatch:assert-alarm-state
<a name="assert-alarm-state"></a>

Verifies that the specified alarms are in one of the specified alarm states.

**Resource type**
+ None

**Parameters**
+ **alarmArns** – The ARNs of the alarms, separated by commas. You can specify up to five alarms.
+ **alarmStates** – The alarm states, separated by commas. The possible alarm states are `OK`, `ALARM`, and `INSUFFICIENT_DATA`.

**Permissions**
+ `cloudwatch:DescribeAlarms`

## Amazon DynamoDB actions
<a name="dynamodb-actions-reference"></a>

AWS FIS supports the following Amazon DynamoDB action.

### aws:dynamodb:global-table-pause-replication
<a name="global-table-pause-replication"></a>

Pauses Amazon DynamoDB multi-Region global table replication to any replica table. Tables may continue to be replicated for up to 5 minutes after action begins.

**Multi-Region strongly consistent (MRSC) global tables**  
The following statements will be dynamically appended to the policy for the target DynamoDB MRSC global table:

```
{
   "Statement":[
      {
         "Sid": "DoNotModifyFisDynamoDbPauseReplicationEXPxxxxxxxxxxxxxxx",
         "Effect":"Deny",
         "Principal":{
            "AWS": "*"
         },
         "Action":[
            "dynamodb:UpdateTable"
         ],
         "Resource":"arn:aws:dynamodb:us-east-1:123456789012:table/ExampleGlobalTable",
         "Condition": {
            "DateLessThan": {
                "aws:CurrentTime": "2024-04-10T09:51:41.511Z"
            },
            "ArnEquals": {
                "aws:PrincipalArn": "arn:aws:iam::123456789012:role/aws-service-role/replication.dynamodb.amazonaws.com/AWSServiceRoleForDynamoDBReplication"
            }
         }
      },
      {
         "Sid": "DoNotModifyFisDynamoDbPauseReplicationEXPxxxxxxxxxxxxxxxForApplicationAutoScaling",
         "Effect":"Deny",
         "Principal":{
            "AWS": "*"
         },
         "Action":[
            "dynamodb:DescribeTable",
            "dynamodb:UpdateTable"
         ],
         "Resource":"arn:aws:dynamodb:us-east-1:123456789012:table/ExampleGlobalTable",
         "Condition": {
            "DateLessThan": {
              "aws:CurrentTime": "2024-04-10T09:51:41.511Z"
            },
            "ArnEquals": {
                "aws:PrincipalArn": "arn:aws:iam::123456789012:role/aws-service-role/dynamodb.application-autoscaling.amazonaws.com/AWSServiceRoleForApplicationAutoScaling_DynamoDBTable"
            }
         }
      }
   ]
}
```

If a target table does not have any attached resource polices, a resource policy is created for the duration of the experiment, and automatically deleted when the experiment ends. Otherwise, the fault statement is inserted into an existing policy, without any additional modifications to the existing policy statements. The fault statement is then removed from the policy at the end of the experiment.

Target Amazon DynamoDB MRSC global tables are subject to an additional quota. This quota enforces that no single table may be subject to more than 5,040 minutes of impairment in a 7-day rolling window.

**Multi-Region eventually consistent (MREC) global tables**  
The following two statements will be dynamically appended to the policy for the target DynamoDB MREC global table:

```
{
   "Statement":[
      {
         "Sid": "DoNotModifyFisDynamoDbPauseReplicationEXPxxxxxxxxxxxxxxxServicePrincipal",
         "Effect":"Deny",
         "Principal":{
            "AWS": "*"
         },
         "Action":[
            "dynamodb:ReadDataForReplication",
            "dynamodb:WriteDataForReplication"
         ],
         "Resource":"arn:aws:dynamodb:us-east-1:123456789012:table/ExampleGlobalTable",
         "Condition": {
            "StringEquals": {
              "aws:PrincipalServiceName": "replication.dynamodb.amazonaws.com"
            },
            "DateLessThan": {
              "aws:CurrentTime": "2024-04-10T09:51:41.511Z"
            }
         }
      },
      {
         "Sid": "DoNotModifyFisDynamoDbPauseReplicationEXPxxxxxxxxxxxxxxx",
         "Effect":"Deny",
         "Principal":{
            "AWS": "*"
         },
         "Action":[
            "dynamodb:GetItem",
            "dynamodb:PutItem",
            "dynamodb:UpdateItem",
            "dynamodb:DeleteItem",
            "dynamodb:DescribeTable",
            "dynamodb:UpdateTable",
            "dynamodb:Scan",
            "dynamodb:DescribeTimeToLive",
            "dynamodb:UpdateTimeToLive"
         ],
         "Resource":"arn:aws:dynamodb:us-east-1:123456789012:table/ExampleGlobalTable",
         "Condition": {
            "DateLessThan": {
              "aws:CurrentTime": "2024-04-10T09:51:41.511Z"
            },
            "ArnEquals": {
                "aws:PrincipalArn": "arn:aws:iam::123456789012:role/aws-service-role/replication.dynamodb.amazonaws.com/AWSServiceRoleForDynamoDBReplication"
            }
         }
      }
   ]
}
```

The following statement will be dynamically appended to the stream policy for the target DynamoDB MREC global table:

```
{
   "Statement":[
      {
         "Sid": "DoNotModifyFisDynamoDbPauseReplicationEXPxxxxxxxxxxxxxxx",
         "Effect":"Deny",
         "Principal":{
            "AWS": "*"
         },
         "Action":[
            "dynamodb:GetRecords",
            "dynamodb:DescribeStream",
            "dynamodb:GetShardIterator"
         ],
         "Resource":"arn:aws:dynamodb:us-east-1:123456789012:table/ExampleGlobalTable/stream/2023-08-31T09:50:24.025",
         "Condition": {
            "DateLessThan": {
              "aws:CurrentTime": "2024-04-10T09:51:41.511Z"
            },
            "ArnEquals": {
                "aws:PrincipalArn": "arn:aws:iam::123456789012:role/aws-service-role/replication.dynamodb.amazonaws.com/AWSServiceRoleForDynamoDBReplication"
            }
         }
      }
   ]
}
```

If a target table or stream does not have any attached resource polices, a resource policy is created for the duration of the experiment, and automatically deleted when the experiment ends. Otherwise, the fault statement is inserted into an existing policy, without any additional modifications to the existing policy statements. The fault statement is then removed from the policy at the end of the experiment.

**Resource type**
+ **aws:dynamodb:global-table**

**Parameters**
+ **duration** – In the AWS FIS API, the value is a string in ISO 8601 format. For example, PT1M represents one minute. In the AWS FIS console, you enter the number of seconds, minutes, or hours.

**Permissions**
+ `dynamodb:PutResourcePolicy`
+ `dynamodb:DeleteResourcePolicy`
+ `dynamodb:GetResourcePolicy`
+ `dynamodb:DescribeTable`
+ `tag:GetResources`
+ `dynamodb:InjectError` \*

\* The permission is only required if you are targeting MRSC global tables

## Amazon Aurora DSQL actions
<a name="dsql-actions-reference"></a>

AWS FIS supports the following Amazon Aurora DSQL actions.

### aws:dsql:cluster-connection-failure
<a name="cluster-connection-failure"></a>

Creates controlled connection failures in an Aurora DSQL cluster for a specified duration to test application resilience.

**Resource type**
+ **aws:dsql:cluster**

**Parameters**
+ **duration** – The duration, from one minute to 12 hours. In the AWS FIS API, the value is a string in ISO 8601 format. For example, PT1M represents one minute. In the AWS FIS console, you enter the number of seconds, minutes, or hours.
+ **percentage** – The percentage (1-100) of calls to inject the fault into.

**Permissions**
+ `dsql:InjectError`
+ `dsql:GetCluster`
+ `tag:GetResources`

To initiate the experiment with Aurora DSQL, see [Fault injection testing](https://docs.aws.amazon.com/aurora-dsql/latest/userguide/disaster-recovery-resiliency.html#fault-injection-testing.html) in the *Aurora DSQL User Guide*.

## Amazon EBS actions
<a name="ebs-actions-reference"></a>

AWS FIS supports the following Amazon EBS action.

**Topics**
+ [aws:ebs:pause-volume-io](#pause-volume-io)
+ [aws:ebs:volume-io-latency](#volume-latency-injection)

### aws:ebs:pause-volume-io
<a name="pause-volume-io"></a>

Pauses I/O operations on target EBS volumes. The target volumes must be in the same Availability Zone and must be attached to instances built on the Nitro System. The volumes can't be attached to instances on an Outpost.

To initiate the experiment using the Amazon EC2 console, see [Fault testing on Amazon EBS](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-fis.html) in the *Amazon EC2 User Guide*.

**Resource type**
+ **aws:ec2:ebs-volume**

**Parameters**
+ **duration** – The duration, from one second to 12 hours. In the AWS FIS API, the value is a string in ISO 8601 format. For example, PT1M represents one minute, PT5S represents five seconds, and PT6H represents six hours. In the AWS FIS console, you enter the number of seconds, minutes, or hours. If the duration is small, such as PT5S, the I/O is paused for the specified duration, but it might take longer for the experiment to complete due to the time it takes to initialize the experiment.

**Permissions**
+ `ec2:DescribeVolumes`
+ `ec2:PauseVolumeIO`
+ `tag:GetResources`

### aws:ebs:volume-io-latency
<a name="volume-latency-injection"></a>

Injects latency on I/O operations of target EBS volumes. The target volumes must be in the same Availability Zone. The volumes can't be attached to instances on an Outpost.

To initiate the experiment using the Amazon EC2 console, see [ Fault testing on Amazon EBS](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ebs-fis.html) in the *Amazon EBS User Guide*.

**Resource type**
+ **aws:ec2:ebs-volume**

**Parameters**
+ **readIOPercentage** – The percentage of read I/O operations that latency will be injected on, from 0.1% to 100.%. This is the percentage of all read I/O operations on the volume that will be impacted during the experiment. The default is 100.
+ **readIOLatencyMilliseconds** – The amount of latency injected on read I/O operations in milliseconds, from 1ms (io2 volumes) or 10ms (non-io2 volumes) to 60 seconds. This is the latency value that will be observed on the specified percentage of the read I/O during the experiment. The default is 100.
+ **writeIOPercentage** – The percentage of write I/O operations that latency will be injected on, from 0.1% to 100.%. This is the percentage of all write I/O operations on the volume that will be impacted during the experiment. The default is 100.
+ **writeIOLatencyMilliseconds** – The amount of latency injected on write I/O operations in milliseconds, from 1ms (io2 volumes) or 10ms (non-io2 volumes) to 60 seconds. This is the latency value that will be observed on the specificed percentage of the read I/O during the experiment. The default is 100.
+ **duration** – The duration for which the latency will be injected, from 1 second to 12 hours.

**Permissions**
+ `ec2:DescribeVolumes`
+ `ec2:InjectVolumeIOLatency`
+ `tag:GetResources`

## Amazon EC2 actions
<a name="ec2-actions-reference"></a>

AWS FIS supports the following Amazon EC2 actions.

**Topics**
+ [aws:ec2:api-insufficient-instance-capacity-error](#api-ice)
+ [aws:ec2:asg-insufficient-instance-capacity-error](#asg-ice)
+ [aws:ec2:reboot-instances](#reboot-instances)
+ [aws:ec2:send-spot-instance-interruptions](#send-spot-instance-interruptions)
+ [aws:ec2:stop-instances](#stop-instances)
+ [aws:ec2:terminate-instances](#terminate-instances)

AWS FIS also supports fault injection actions through the AWS Systems Manager SSM Agent. Systems Manager uses an SSM document that defines actions to perform on EC2 instances. You can use your own document to inject custom faults, or you can use pre-configured SSM documents. For more information, see [Use Systems Manager SSM documents with AWS FIS](actions-ssm-agent.md).

### aws:ec2:api-insufficient-instance-capacity-error
<a name="api-ice"></a>

Injects `InsufficientInstanceCapacity` error responses on requests made by the target IAM roles. Supported operations are RunInstances, CreateCapacityReservation, StartInstances, CreateFleet calls. Requests that include capacity asks in multiple Availability Zones are not supported. This action doesn't support defining targets using resource tags, filters, or parameters.

For the Auto Scaling LaunchInstances operation, InsufficientInstanceCapacity errors will be returned in the response's `errors` field, but the Auto Scaling group's desired capacity will still be updated, allowing the asynchronous scaling process to potentially launch instances. For broader testing of insufficient capacity handling with LaunchInstances, consider using this action together with [aws:ec2:asg-insufficient-instance-capacity-error](#asg-ice).

**Resource type**
+ **aws:iam:role**

**Parameters**
+ **duration** – In the AWS FIS API, the value is a string in ISO 8601 format. For example, PT1M represents one minute. In the AWS FIS console, you enter the number of seconds, minutes, or hours.
+ **availabilityZoneIdentifiers** – The comma separated list of Availability Zones. Supports Zone IDs (e.g. `"use1-az1, use1-az2"`) and Zone names (e.g. `"us-east-1a"`).
+ **percentage** – The percentage (1-100) of calls to inject the fault into.

**Permissions**
+ `ec2:InjectApiError`with condition key `ec2:FisActionId` value set to `aws:ec2:api-insufficient-instance-capacity-error` and `ec2:FisTargetArns` condition key set to target IAM roles.

For an example policy, see [Example: Use condition keys for `ec2:InjectApiError`](security_iam_id-based-policy-examples.md#security-iam-policy-examples-ec2).

### aws:ec2:asg-insufficient-instance-capacity-error
<a name="asg-ice"></a>

Injects `InsufficientInstanceCapacity` error responses on requests made by the target Auto Scaling groups. This action only supports Auto Scaling groups using launch templates. To learn more about insufficient instance capacity errors, see the [Amazon EC2 user guide](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/troubleshooting-launch.html#troubleshooting-launch-capacity). 

**Resource type**
+ **aws:ec2:autoscaling-group**

**Parameters**
+ **duration** – In the AWS FIS API, the value is a string in ISO 8601 format. For example, PT1M represents one minute. In the AWS FIS console, you enter the number of seconds, minutes, or hours.
+ **availabilityZoneIdentifiers** – The comma separated list of Availability Zones. Supports Zone IDs (e.g. `"use1-az1, use1-az2"`) and Zone names (e.g. `"us-east-1a"`).
+ **percentage** – Optional. The percentage (1-100) of the target Auto Scaling group's launch requests to inject the fault. The default is 100.

**Permissions**
+ `ec2:InjectApiError`with condition key ec2:FisActionId value set to `aws:ec2:asg-insufficient-instance-capacity-error` and `ec2:FisTargetArns` condition key set to target Auto Scaling groups.
+ `autoscaling:DescribeAutoScalingGroups`

For an example policy, see [Example: Use condition keys for `ec2:InjectApiError`](security_iam_id-based-policy-examples.md#security-iam-policy-examples-ec2).

### aws:ec2:reboot-instances
<a name="reboot-instances"></a>

Runs the Amazon EC2 API action [RebootInstances](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_RebootInstances.html) on the target EC2 instances.

**Resource type**
+ **aws:ec2:instance**

**Parameters**
+ None

**Permissions**
+ `ec2:RebootInstances`
+ `ec2:DescribeInstances`

**AWS managed policy**
+ [AWSFaultInjectionSimulatorEC2Access](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSFaultInjectionSimulatorEC2Access.html)

### aws:ec2:send-spot-instance-interruptions
<a name="send-spot-instance-interruptions"></a>

Interrupts the target Spot Instances. Sends a [Spot Instance interruption notice](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/spot-interruptions.html#spot-instance-termination-notices) to target Spot Instances two minutes before interrupting them. The interruption time is determined by the specified **durationBeforeInterruption** parameter. Two minutes after the interruption time, the Spot Instances are terminated or stopped, depending on their interruption behavior. A Spot Instance that was stopped by AWS FIS remains stopped until you restart it.

Immediately after the action is initiated, the target instance receives an [EC2 instance rebalance recommendation](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/rebalance-recommendations.html). If you specified **durationBeforeInterruption**, there could be a delay between the rebalance recommendation and the interruption notice.

For more information, see [Tutorial: Test Spot Instance interruptions using AWS FIS](fis-tutorial-spot-interruptions.md). Alternatively, to initiate the experiment by using the Amazon EC2 console, see [Initiate a Spot Instance interruption](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/initiate-a-spot-instance-interruption.html) in the *Amazon EC2 User Guide*.

**Resource type**
+ **aws:ec2:spot-instance**

**Parameters**
+ **durationBeforeInterruption** – The time to wait before interrupting the instance, from 2 to 15 minutes. In the AWS FIS API, the value is a string in ISO 8601 format. For example, PT2M represents two minutes. In the AWS FIS console, you enter the number of minutes.

**Permissions**
+ `ec2:SendSpotInstanceInterruptions`
+ `ec2:DescribeInstances`

**AWS managed policy**
+ [AWSFaultInjectionSimulatorEC2Access](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSFaultInjectionSimulatorEC2Access.html)

### aws:ec2:stop-instances
<a name="stop-instances"></a>

Runs the Amazon EC2 API action [StopInstances](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_StopInstances.html) on the target EC2 instances.

**Resource type**
+ **aws:ec2:instance**

**Parameters**
+ **startInstancesAfterDuration** – Optional. The time to wait before starting the instance, from one minute to 12 hours. In the AWS FIS API, the value is a string in ISO 8601 format. For example, PT1M represents one minute. In the AWS FIS console, you enter the number of seconds, minutes, or hours. If the instance has an encrypted EBS volume, you must grant AWS FIS permission to the KMS key used to encrypt the volume, or add the experiment role to the KMS key policy.
+ **completeIfInstancesTerminated** – Optional. If true, and if `startInstancesAfterDuration` is also true, this action will not fail when targeted EC2 instances have been terminated by a separate request outside of FIS and cannot be restarted. For example, Auto Scaling groups may terminate stopped EC2 instances under their control before this action completes. The default is false. 

**Permissions**
+ `ec2:StopInstances`
+ `ec2:StartInstances`
+ `ec2:DescribeInstances` – Optional. Required with **completeIfInstancesTerminated** to validate instance state at end of action.
+ `kms:CreateGrant` – Optional. Required with **startInstancesAfterDuration** to restart instances with encrypted volumes.

**AWS managed policy**
+ [AWSFaultInjectionSimulatorEC2Access](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSFaultInjectionSimulatorEC2Access.html)

### aws:ec2:terminate-instances
<a name="terminate-instances"></a>

Runs the Amazon EC2 API action [TerminateInstances](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_TerminateInstances.html) on the target EC2 instances.

**Resource type**
+ **aws:ec2:instance**

**Parameters**
+ None

**Permissions**
+ `ec2:TerminateInstances`
+ `ec2:DescribeInstances`

**AWS managed policy**
+ [AWSFaultInjectionSimulatorEC2Access](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSFaultInjectionSimulatorEC2Access.html)

## Amazon ECS actions
<a name="ecs-actions-reference"></a>

AWS FIS supports the following Amazon ECS actions.

**Topics**
+ [aws:ecs:drain-container-instances](#drain-container-instances)
+ [aws:ecs:stop-task](#stop-task)
+ [aws:ecs:task-cpu-stress](#task-cpu-stress)
+ [aws:ecs:task-io-stress](#task-io-stress)
+ [aws:ecs:task-kill-process](#task-kill-process)
+ [aws:ecs:task-network-blackhole-port](#task-network-blackhole-port)
+ [aws:ecs:task-network-latency](#task-network-latency)
+ [aws:ecs:task-network-packet-loss](#task-network-packet-loss)

### aws:ecs:drain-container-instances
<a name="drain-container-instances"></a>

Runs the Amazon ECS API action [UpdateContainerInstancesState](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_UpdateContainerInstancesState.html) to drain the specified percentage of underlying Amazon EC2 instances on the target clusters.

**Resource type**
+ **aws:ecs:cluster**

**Parameters**
+ **drainagePercentage** – The percentage (1-100).
+ **duration** – The duration, from one minute to 12 hours. In the AWS FIS API, the value is a string in ISO 8601 format. For example, PT1M represents one minute. In the AWS FIS console, you enter the number of seconds, minutes, or hours.

**Permissions**
+ `ecs:DescribeClusters`
+ `ecs:UpdateContainerInstancesState`
+ `ecs:ListContainerInstances`
+ `tag:GetResources`

**AWS managed policy**
+ [AWSFaultInjectionSimulatorECSAccess](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSFaultInjectionSimulatorECSAccess.html)

### aws:ecs:stop-task
<a name="stop-task"></a>

Runs the Amazon ECS API action [StopTask](https://docs.aws.amazon.com/AmazonECS/latest/APIReference/API_StopTask.html) to stop the target task.

**Resource type**
+ **aws:ecs:task**

**Parameters**
+ None

**Permissions**
+ `ecs:DescribeTasks`
+ `ecs:ListTasks`
+ `ecs:StopTask`
+ `tag:GetResources`

**AWS managed policy**
+ [AWSFaultInjectionSimulatorECSAccess](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSFaultInjectionSimulatorECSAccess.html)

### aws:ecs:task-cpu-stress
<a name="task-cpu-stress"></a>

Runs CPU stress on the target tasks. Uses the [AWSFIS-Run-CPU-Stress](https://console.aws.amazon.com/systems-manager/documents/AWSFIS-Run-CPU-Stress/description) SSM document. The tasks must be managed by AWS Systems Manager. For more information, see [ECS task actions](ecs-task-actions.md).

**Resource type**
+ **aws:ecs:task**

**Parameters**
+ **duration** – The duration of the stress test, in ISO 8601 format.
+ **percent** – Optional. The target load percentage, from 0 (no load) to 100 (full load). The default is 100.
+ **workers** – Optional. The number of stressors to use. The default is 0, which uses all stressors.
+ **installDependencies** – Optional. If this value is `True`, Systems Manager installs the required dependencies on the sidecar container for the SSM agent, if they are not already installed. The default is `True`. The dependency is **stress-ng**.

**Permissions**
+ `ecs:DescribeTasks`
+ `ssm:SendCommand`
+ `ssm:ListCommands`
+ `ssm:CancelCommand`

### aws:ecs:task-io-stress
<a name="task-io-stress"></a>

Runs I/O stress on the target tasks. Uses the [AWSFIS-Run-IO-Stress](https://console.aws.amazon.com/systems-manager/documents/AWSFIS-Run-IO-Stress/description) SSM document. The tasks must be managed by AWS Systems Manager. For more information, see [ECS task actions](ecs-task-actions.md).

**Resource type**
+ **aws:ecs:task**

**Parameters**
+ **duration** – The duration of the stress test, in ISO 8601 format.
+ **percent** – Optional. The percentage of free space on the file system to use during the stress test. The default is 80%.
+ **workers** – Optional. The number of workers. Workers perform a mix of sequential, random, and memory-mapped read/write operations, forced synchronizing, and cache dropping. Multiple child processes perform different I/O operations on the same file. The default is 1.
+ **installDependencies** – Optional. If this value is `True`, Systems Manager installs the required dependencies on the sidecar container for the SSM agent, if they are not already installed. The default is `True`. The dependency is **stress-ng**.

**Permissions**
+ `ecs:DescribeTasks`
+ `ssm:SendCommand`
+ `ssm:ListCommands`
+ `ssm:CancelCommand`

### aws:ecs:task-kill-process
<a name="task-kill-process"></a>

Stops the specified process in the tasks, using the **killall** command. Uses the [AWSFIS-Run-Kill-Process](https://console.aws.amazon.com/systems-manager/documents/AWSFIS-Run-Kill-Process/description) SSM document. The task definition must have `pidMode` set to `task`. The tasks must be managed by AWS Systems Manager. For more information, see [ECS task actions](ecs-task-actions.md).

**Resource type**
+ **aws:ecs:task**

**Parameters**
+ **processName** – The name of the process to stop.
+ **signal** – Optional. The signal to send along with the command. The possible values are `SIGTERM` (which the receiver can choose to ignore) and `SIGKILL` (which cannot be ignored). The default is `SIGTERM`.
+ **installDependencies** – Optional. If this value is `True`, Systems Manager installs the required dependencies on the sidecar container for the SSM agent, if they are not already installed. The default is `True`. The dependency is **killall**.

**Permissions**
+ `ecs:DescribeTasks`
+ `ssm:SendCommand`
+ `ssm:ListCommands`
+ `ssm:CancelCommand`

### aws:ecs:task-network-blackhole-port
<a name="task-network-blackhole-port"></a>

Drops inbound or outbound traffic for the specified protocol and port, using the [Amazon ECS Fault Injection endpoints](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/fault-injection.html). Uses the [AWSFIS-Run-Network-Blackhole-Port-ECS](https://console.aws.amazon.com/systems-manager/documents/AWSFIS-Run-Network-Blackhole-Port-ECS/description) SSM document. The task definition must have `pidMode` set to `task`. The tasks must be managed by AWS Systems Manager. You can't set `networkMode` to `bridge` in the task definition. For more information, see [ECS task actions](ecs-task-actions.md).

When `useEcsFaultInjectionEndpoints` is set to `false`, the fault uses the `iptables` tool, and uses the [AWSFIS-Run-Network-Blackhole-Port](https://console.aws.amazon.com/systems-manager/documents/AWSFIS-Run-Network-Blackhole-Port/description) SSM document. 

**Resource type**
+ **aws:ecs:task**

**Parameters**
+ **duration** – The duration of the test, in ISO 8601 format.
+ **port** – The port number.
+ **trafficType** – The type of traffic. The possible values are `ingress` and `egress`.
+ **protocol** – Optional. The protocol. The possible values are `tcp` and `udp`. The default is `tcp`.
+ **installDependencies** – Optional. If this value is `True`, Systems Manager installs the required dependencies on the sidecar container for the SSM agent, if they are not already installed. The default is `True`. The dependencies are **atd**, **curl-minimal**, **dig** and **jq**.
+ **useEcsFaultInjectionEndpoints** – Optional. If set to true, the Amazon ECS Fault Injection APIs will be used. The default is false.

**Permissions**
+ `ecs:DescribeTasks`
+ `ssm:SendCommand`
+ `ssm:ListCommands`
+ `ssm:CancelCommand`

### aws:ecs:task-network-latency
<a name="task-network-latency"></a>

Adds latency and jitter to the network interface for egress traffic to specific sources, using the [Amazon ECS Fault Injection endpoints](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/fault-injection.html) . Uses the [AWSFIS-Run-Network-Latency-ECS](https://console.aws.amazon.com/systems-manager/documents/AWSFIS-Run-Network-Latency-ECS/description) SSM document. The task definition must have `pidMode` set to `task`. The tasks must be managed by AWS Systems Manager. You can't set `networkMode` to `bridge` in the task definition. For more information, see [ECS task actions](ecs-task-actions.md).

When `useEcsFaultInjectionEndpoints` is set to `false`, the fault uses the `tc` tool, and uses the [AWSFIS-Run-Network-Latency-Sources](https://console.aws.amazon.com/systems-manager/documents/AWSFIS-Run-Network-Latency-Sources/description) SSM document. 

Use the `flowsPercent` parameter to add latency on a percentage of the connections. To use the `flowsPercent` parameter, the ECS Agent version should be `1.100.0` or higher.

To use AZ names or AZ IDs in the `sources` parameter, all targets of the action must be on the same VPC.

**Resource type**
+ **aws:ecs:task**

**Parameters**
+ **duration** – The duration of the test, in ISO 8601 format.
+ **delayMilliseconds** – Optional. The delay, in milliseconds. The default is 200.
+ **jitterMilliseconds** – Optional. The jitter, in milliseconds. The default is 10.
+ **flowsPercent** – Optional. The percentage of network flows that will be affected by the action. The default is 100%.
+ **sources** – Optional. The sources, separated by commas, without spaces. The possible values are: an IPv4 address, an IPv4 CIDR block, a domain name, an AZ name (us-east-1a), an AZ ID (use1-az1), ALL, `DYNAMODB`, and `S3`. If you specify `DYNAMODB` or `S3`, this applies only to the Regional endpoint in the current Region. The default is ALL, which matches all IPv4 traffic. IPv6 traffic is not impaired by this action.
+ **installDependencies** – Optional. If this value is `True`, Systems Manager installs the required dependencies on the sidecar container for the SSM agent, if they are not already installed. The default is `True`. The dependencies are **atd**, **curl-minimal**, **dig**, **jq** and **lsof**.
+ **useEcsFaultInjectionEndpoints** – Optional. If set to true, the Amazon ECS Fault Injection APIs will be used. The default is false.

**Permissions**
+ `ecs:DescribeTasks`
+ `ecs:DescribeContainerInstances`
+ `ec2:DescribeInstances`
+ `ec2:DescribeSubnets`
+ `ssm:SendCommand`
+ `ssm:ListCommands`
+ `ssm:CancelCommand`

### aws:ecs:task-network-packet-loss
<a name="task-network-packet-loss"></a>

Adds packet loss to the network interface for egress traffic to specific sources, using the [Amazon ECS Fault Injection endpoints](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/fault-injection.html). Uses the [AWSFIS-Run-Network-Packet-Loss-ECS](https://console.aws.amazon.com/systems-manager/documents/AWSFIS-Run-Network-Packet-Loss-ECS/description) SSM document. The task definition must have `pidMode` set to `task`. The tasks must be managed by AWS Systems Manager. You can't set `networkMode` to `bridge` in the task definition. For more information, see [ECS task actions](ecs-task-actions.md).

When `useEcsFaultInjectionEndpoints` is set to `false`, the fault uses the `tc` tool, and uses the [AWSFIS-Run-Network-Packet-Loss-Sources](https://console.aws.amazon.com/systems-manager/documents/AWSFIS-Run-Network-Packet-Loss-Sources/description) SSM document. 

Use the `flowsPercent` parameter to inject packet loss on a percentage of the connections. To use the `flowsPercent` parameter, the ECS Agent version should be `1.100.0` or higher.

To use AZ names or AZ IDs in the `sources` parameter, all targets of the action must be on the same VPC.

**Resource type**
+ **aws:ecs:task**

**Parameters**
+ **duration** – The duration of the test, in ISO 8601 format.
+ **lossPercent** – Optional. The percentage of packet loss. The default is 7%.
+ **flowsPercent** – Optional. The percentage of network flows that will be affected by the action. The default is 100%.
+ **sources** – Optional. The sources, separated by commas, without spaces. The possible values are: an IPv4 address, an IPv4 CIDR block, a domain name, an AZ name (us-east-1a), an AZ ID (use1-az1), ALL, `DYNAMODB`, and `S3`. If you specify `DYNAMODB` or `S3`, this applies only to the Regional endpoint in the current Region. The default is ALL, which matches all IPv4 traffic. IPv6 traffic is not impaired by this action.
+ **installDependencies** – Optional. If this value is `True`, Systems Manager installs the required dependencies on the sidecar container for the SSM agent, if they are not already installed. The default is `True`. The dependencies are **atd**, **curl-minimal**, **dig**, **jq** and **lsof**.
+ **useEcsFaultInjectionEndpoints** – Optional. If set to true, the Amazon ECS Fault Injection APIs will be used. The default is false.

**Permissions**
+ `ecs:DescribeTasks`
+ `ecs:DescribeContainerInstances`
+ `ec2:DescribeInstances`
+ `ec2:DescribeSubnets`
+ `ssm:SendCommand`
+ `ssm:ListCommands`
+ `ssm:CancelCommand`

## Amazon EKS actions
<a name="eks-actions-reference"></a>

AWS FIS supports the following Amazon EKS actions.

**Topics**
+ [aws:eks:inject-kubernetes-custom-resource](#inject-kubernetes-custom-resource)
+ [aws:eks:pod-cpu-stress](#pod-cpu-stress)
+ [aws:eks:pod-delete](#pod-delete)
+ [aws:eks:pod-io-stress](#pod-io-stress)
+ [aws:eks:pod-memory-stress](#pod-memory-stress)
+ [aws:eks:pod-network-blackhole-port](#pod-network-blackhole-port)
+ [aws:eks:pod-network-latency](#pod-network-latency)
+ [aws:eks:pod-network-packet-loss](#pod-network-packet-loss)
+ [aws:eks:terminate-nodegroup-instances](#terminate-nodegroup-instance)

### aws:eks:inject-kubernetes-custom-resource
<a name="inject-kubernetes-custom-resource"></a>

Runs a ChaosMesh or Litmus experiment on a single target cluster. You must install ChaosMesh or Litmus on the target cluster.

When you create an experiment template and define a target of type `aws:eks:cluster`, you must target this action to a single Amazon Resource Name (ARN). This action doesn't support defining targets using resource tags, filters, or parameters.

When you install ChaosMesh, you must specify the appropriate container runtime. Starting with Amazon EKS version 1.23, the default runtime changed from Docker to **containerd**. Starting with version 1.24, Docker was removed.

**Resource type**
+ **aws:eks:cluster**

**Parameters**
+ **kubernetesApiVersion** – The API version of the [Kubernetes custom resource](https://kubernetes.io/docs/concepts/extend-kubernetes/api-extension/custom-resources/). The possible values are `chaos-mesh.org/v1alpha1` \| `litmuschaos.io/v1alpha1`.
+ **kubernetesKind** – The Kubernetes custom resource kind. The value depends on the API version.
  + `chaos-mesh.org/v1alpha1` – The possible values are `AWSChaos` \| `DNSChaos` \| `GCPChaos` \| `HTTPChaos` \| `IOChaos` \| `JVMChaos` \| `KernelChaos` \| `NetworkChaos` \| `PhysicalMachineChaos` \| `PodChaos` \| `PodHttpChaos` \| `PodIOChaos` \| `PodNetworkChaos` \| `Schedule` \| `StressChaos` \| `TimeChaos` \|
  + `litmuschaos.io/v1alpha1` – The possible value is `ChaosEngine`.
+ **kubernetesNamespace** – The [Kubernetes namespace](https://kubernetes.io/docs/concepts/overview/working-with-objects/namespaces/).
+ **kubernetesSpec** – The `spec` section of the Kubernetes custom resource, in JSON format.
+ **maxDuration** – The maximum time allowed for the automation execution to complete, from one minute to 12 hours. In the AWS FIS API, the value is a string in ISO 8601 format. For example, PT1M represents one minute. In the AWS FIS console, you enter the number of seconds, minutes, or hours.

**Permissions**  
No AWS Identity and Access Management (IAM) permissions are required for this action. The permissions required to use this action are controlled by Kubernetes using RBAC authorization. For more information, see [Using RBAC Authorization](https://kubernetes.io/docs/reference/access-authn-authz/rbac/) in the official Kubernetes documentation. For more information about Chaos Mesh, see the [official Chaos Mesh documentation](https://chaos-mesh.org/docs/). For more information about Litmus, see the [official Litmus documentation](https://docs.litmuschaos.io/docs/introduction/what-is-litmus/).

### aws:eks:pod-cpu-stress
<a name="pod-cpu-stress"></a>

Runs CPU stress on the target pods. For more information, see [EKS Pod actions](eks-pod-actions.md).

**Resource type**
+ **aws:eks:pod**

**Parameters**
+ **duration** – The duration of the stress test, in ISO 8601 format.
+ **percent** – Optional. The target load percentage, from 0 (no load) to 100 (full load). The default is 100.
+ **workers** – Optional. The number of stressors to use. The default is 0, which uses all stressors.
+ **kubernetesServiceAccount** – The Kubernetes service account. For information about the required permissions, see [Configure the Kubernetes service account](eks-pod-actions.md#configure-service-account).
+ **fisPodContainerImage** – Optional. The container image used to create the fault injector pod. The default is to use the images provided by AWS FIS. For more information, see [Pod container images](eks-pod-actions.md#eks-pod-container-images).
+ **maxErrorsPercent** – Optional. The percentage of targets that can fail before the fault injection fails. The default is 0.
+ **fisPodLabels** – Optional. The Kubernetes labels that are attached to the fault orchestration pod created by FIS.
+ **fisPodAnnotations** – Optional. The Kubernetes annotations that are attached to the fault orchestration pod created by FIS.
+ **fisPodSecurityPolicy** – Optional. The [Kubernetes Security Standards](https://kubernetes.io/docs/concepts/security/pod-security-standards/) policy to use for the fault orchestration pod created by FIS and the ephemeral containers. Possible values are `privileged`, `baseline` and `restricted`. This action is compatible with all policy levels.

**Permissions**
+ `eks:DescribeCluster`
+ `ec2:DescribeSubnets`
+ `tag:GetResources`

**AWS managed policy**
+ [AWSFaultInjectionSimulatorEKSAccess](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSFaultInjectionSimulatorEKSAccess.html)

### aws:eks:pod-delete
<a name="pod-delete"></a>

Deletes the target pods. For more information, see [EKS Pod actions](eks-pod-actions.md).

**Resource type**
+ **aws:eks:pod**

**Parameters**
+ **gracePeriodSeconds** – Optional. The duration, in seconds, to wait for the pod to terminate gracefully. If the value is 0, we perform the action immediately. If the value is nil, we use the default grace period for the pod.
+ **kubernetesServiceAccount** – The Kubernetes service account. For information about the required permissions, see [Configure the Kubernetes service account](eks-pod-actions.md#configure-service-account).
+ **fisPodContainerImage** – Optional. The container image used to create the fault injector pod. The default is to use the images provided by AWS FIS. For more information, see [Pod container images](eks-pod-actions.md#eks-pod-container-images).
+ **maxErrorsPercent** – Optional. The percentage of targets that can fail before the fault injection fails. The default is 0.
+ **fisPodLabels** – Optional. The Kubernetes labels that are attached to the fault orchestration pod created by FIS.
+ **fisPodAnnotations** – Optional. The Kubernetes annotations that are attached to the fault orchestration pod created by FIS.
+ **fisPodSecurityPolicy** – Optional. The [Kubernetes Security Standards](https://kubernetes.io/docs/concepts/security/pod-security-standards/) policy to use for the fault orchestration pod created by FIS and the ephemeral containers. Possible values are `privileged`, `baseline` and `restricted`. This action is compatible with all policy levels.

**Permissions**
+ `eks:DescribeCluster`
+ `ec2:DescribeSubnets`
+ `tag:GetResources`

**AWS managed policy**
+ [AWSFaultInjectionSimulatorEKSAccess](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSFaultInjectionSimulatorEKSAccess.html)

### aws:eks:pod-io-stress
<a name="pod-io-stress"></a>

Runs I/O stress on the target pods. For more information, see [EKS Pod actions](eks-pod-actions.md).

**Resource type**
+ **aws:eks:pod**

**Parameters**
+ **duration** – The duration of the stress test, in ISO 8601 format.
+ **workers** – Optional. The number of workers. Workers perform a mix of sequential, random, and memory-mapped read/write operations, forced synchronizing, and cache dropping. Multiple child processes perform different I/O operations on the same file. The default is 1.
+ **percent** – Optional. The percentage of free space on the file system to use during the stress test. The default is 80%.
+ **kubernetesServiceAccount** – The Kubernetes service account. For information about the required permissions, see [Configure the Kubernetes service account](eks-pod-actions.md#configure-service-account).
+ **fisPodContainerImage** – Optional. The container image used to create the fault injector pod. The default is to use the images provided by AWS FIS. For more information, see [Pod container images](eks-pod-actions.md#eks-pod-container-images).
+ **maxErrorsPercent** – Optional. The percentage of targets that can fail before the fault injection fails. The default is 0.
+ **fisPodLabels** – Optional. The Kubernetes labels that are attached to the fault orchestration pod created by FIS.
+ **fisPodAnnotations** – Optional. The Kubernetes annotations that are attached to the fault orchestration pod created by FIS.
+ **fisPodSecurityPolicy** – Optional. The [Kubernetes Security Standards](https://kubernetes.io/docs/concepts/security/pod-security-standards/) policy to use for the fault orchestration pod created by FIS and the ephemeral containers. Possible values are `privileged` and `baseline`.

**Permissions**
+ `eks:DescribeCluster`
+ `ec2:DescribeSubnets`
+ `tag:GetResources`

**AWS managed policy**
+ [AWSFaultInjectionSimulatorEKSAccess](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSFaultInjectionSimulatorEKSAccess.html)

### aws:eks:pod-memory-stress
<a name="pod-memory-stress"></a>

Runs memory stress on the target pods. For more information, see [EKS Pod actions](eks-pod-actions.md).

**Resource type**
+ **aws:eks:pod**

**Parameters**
+ **duration** – The duration of the stress test, in ISO 8601 format.
+ **workers** – Optional. The number of stressors to use. The default is 1.
+ **percent** – Optional. The percentage of virtual memory to use during the stress test. The default is 80%.
+ **kubernetesServiceAccount** – The Kubernetes service account. For information about the required permissions, see [Configure the Kubernetes service account](eks-pod-actions.md#configure-service-account).
+ **fisPodContainerImage** – Optional. The container image used to create the fault injector pod. The default is to use the images provided by AWS FIS. For more information, see [Pod container images](eks-pod-actions.md#eks-pod-container-images).
+ **maxErrorsPercent** – Optional. The percentage of targets that can fail before the fault injection fails. The default is 0.
+ **fisPodLabels** – Optional. The Kubernetes labels that are attached to the fault orchestration pod created by FIS.
+ **fisPodAnnotations** – Optional. The Kubernetes annotations that are attached to the fault orchestration pod created by FIS.
+ **fisPodSecurityPolicy** – Optional. The [Kubernetes Security Standards](https://kubernetes.io/docs/concepts/security/pod-security-standards/) policy to use for the fault orchestration pod created by FIS and the ephemeral containers. Possible values are `privileged`, `baseline` and `restricted`. This action is compatible with all policy levels.

**Permissions**
+ `eks:DescribeCluster`
+ `ec2:DescribeSubnets`
+ `tag:GetResources`

**AWS managed policy**
+ [AWSFaultInjectionSimulatorEKSAccess](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSFaultInjectionSimulatorEKSAccess.html)

### aws:eks:pod-network-blackhole-port
<a name="pod-network-blackhole-port"></a>

Drops inbound or outbound traffic for the specified protocol and port. Only compatible with the [Kubernetes Security Standards](https://kubernetes.io/docs/concepts/security/pod-security-standards/) `privileged`policy. For more information, see [EKS Pod actions](eks-pod-actions.md).

**Resource type**
+ **aws:eks:pod**

**Parameters**
+ **duration** – The duration of the test, in ISO 8601 format.
+ **protocol** – The protocol. The possible values are `tcp` and `udp`.
+ **trafficType** – The type of traffic. The possible values are `ingress` and `egress`.
+ **port** – The port number.
+ **kubernetesServiceAccount** – The Kubernetes service account. For information about the required permissions, see [Configure the Kubernetes service account](eks-pod-actions.md#configure-service-account).
+ **fisPodContainerImage** – Optional. The container image used to create the fault injector pod. The default is to use the images provided by AWS FIS. For more information, see [Pod container images](eks-pod-actions.md#eks-pod-container-images).
+ **maxErrorsPercent** – Optional. The percentage of targets that can fail before the fault injection fails. The default is 0.
+ **fisPodLabels** – Optional. The Kubernetes labels that are attached to the fault orchestration pod created by FIS.
+ **fisPodAnnotations** – Optional. The Kubernetes annotations that are attached to the fault orchestration pod created by FIS.

**Permissions**
+ `eks:DescribeCluster`
+ `ec2:DescribeSubnets`
+ `tag:GetResources`

**AWS managed policy**
+ [AWSFaultInjectionSimulatorEKSAccess](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSFaultInjectionSimulatorEKSAccess.html)

### aws:eks:pod-network-latency
<a name="pod-network-latency"></a>

Adds latency and jitter to the network interface using the **tc** tool for traffic to or from specific sources. Only compatible with the [Kubernetes Security Standards](https://kubernetes.io/docs/concepts/security/pod-security-standards/) `privileged`policy. For more information, see [EKS Pod actions](eks-pod-actions.md).

Use the `flowsPercent` parameter to add latency on a percentage of the connections.

**Resource type**
+ **aws:eks:pod**

**Parameters**
+ **duration** – The duration of the test, in ISO 8601 format.
+ **interface** – Optional. The network interfaces, separated by commas. ALL and DEFAULT values are supported. The default is `DEFAULT`, which will target the primary network interface for the Operating System.
+ **delayMilliseconds** – Optional. The delay, in milliseconds. The default is 200.
+ **jitterMilliseconds** – Optional. The jitter, in milliseconds. The default is 10.
+ **flowsPercent** – Optional. The percentage of network flows that will be affected by the action. The default is 100%.
+ **sources** – Optional. The sources, separated by commas, without spaces. The possible values are: an IPv4 address, an IPv4 CIDR block, a domain name, an AZ name (us-east-1a), an AZ ID (use1-az1), ALL, `DYNAMODB`, and `S3`. If you specify `DYNAMODB` or `S3`, this applies only to the Regional endpoint in the current Region. For domain names, 10 DNS resolution attempts are made to collect IP addresses. Due to DNS load balancing and rotation, this action may not impair all possible IP addresses the domain could resolve to. The default is ALL, which matches all IPv4 traffic. IPv6 traffic is not impaired by this action.
+ **kubernetesServiceAccount** – The Kubernetes service account. For information about the required permissions, see [Configure the Kubernetes service account](eks-pod-actions.md#configure-service-account).
+ **fisPodContainerImage** – Optional. The container image used to create the fault injector pod. The default is to use the images provided by AWS FIS. For more information, see [Pod container images](eks-pod-actions.md#eks-pod-container-images).
+ **maxErrorsPercent** – Optional. The percentage of targets that can fail before the fault injection fails. The default is 0.
+ **fisPodLabels** – Optional. The Kubernetes labels that are attached to the fault orchestration pod created by FIS.
+ **fisPodAnnotations** – Optional. The Kubernetes annotations that are attached to the fault orchestration pod created by FIS.

**Permissions**
+ `eks:DescribeCluster`
+ `ec2:DescribeSubnets`
+ `tag:GetResources`

**AWS managed policy**
+ [AWSFaultInjectionSimulatorEKSAccess](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSFaultInjectionSimulatorEKSAccess.html)

### aws:eks:pod-network-packet-loss
<a name="pod-network-packet-loss"></a>

Adds packet loss to the network interface using the **tc** tool. Only compatible with the [Kubernetes Security Standards](https://kubernetes.io/docs/concepts/security/pod-security-standards/) `privileged`policy. For more information, see [EKS Pod actions](eks-pod-actions.md).

Use the `flowsPercent` parameter to inject packet loss on a percentage of the connections.

**Resource type**
+ **aws:eks:pod**

**Parameters**
+ **duration** – The duration of the test, in ISO 8601 format.
+ **interface** – Optional. The network interfaces, separated by commas. ALL and DEFAULT values are supported. The default is `DEFAULT`, which will target the primary network interface for the Operating System.
+ **lossPercent** – Optional. The percentage of packet loss. The default is 7%.
+ **flowsPercent** – Optional. The percentage of network flows that will be affected by the action. The default is 100%.
+ **sources** – Optional. The sources, separated by commas, without spaces. The possible values are: an IPv4 address, an IPv4 CIDR block, a domain name, an AZ name (us-east-1a), an AZ ID (use1-az1), ALL, `DYNAMODB`, and `S3`. If you specify `DYNAMODB` or `S3`, this applies only to the Regional endpoint in the current Region. For domain names, 10 DNS resolution attempts are made to collect IP addresses. Due to DNS load balancing and rotation, this action may not impair all possible IP addresses the domain could resolve to. The default is ALL, which matches all IPv4 traffic. IPv6 traffic is not impaired by this action.
+ **kubernetesServiceAccount** – The Kubernetes service account. For information about the required permissions, see [Configure the Kubernetes service account](eks-pod-actions.md#configure-service-account).
+ **fisPodContainerImage** – Optional. The container image used to create the fault injector pod. The default is to use the images provided by AWS FIS. For more information, see [Pod container images](eks-pod-actions.md#eks-pod-container-images).
+ **maxErrorsPercent** – Optional. The percentage of targets that can fail before the fault injection fails. The default is 0.
+ **fisPodLabels** – Optional. The Kubernetes labels that are attached to the fault orchestration pod created by FIS.
+ **fisPodAnnotations** – Optional. The Kubernetes annotations that are attached to the fault orchestration pod created by FIS.

**Permissions**
+ `eks:DescribeCluster`
+ `ec2:DescribeSubnets`
+ `tag:GetResources`

**AWS managed policy**
+ [AWSFaultInjectionSimulatorEKSAccess](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSFaultInjectionSimulatorEKSAccess.html)

### aws:eks:terminate-nodegroup-instances
<a name="terminate-nodegroup-instance"></a>

Runs the Amazon EC2 API action [TerminateInstances](https://docs.aws.amazon.com/AWSEC2/latest/APIReference/API_TerminateInstances.html) on the target node group. Only compatible with Amazon EKS managed node groups. Self-managed node groups are not supported. For more information, see [EKS manage compute](https://docs.aws.amazon.com/eks/latest/userguide/eks-compute.html).

**Resource type**
+ **aws:eks:nodegroup**

**Parameters**
+ **instanceTerminationPercentage** – The percentage (1-100) of instances to terminate.

**Permissions**
+ `ec2:DescribeInstances`
+ `ec2:TerminateInstances`
+ `eks:DescribeNodegroup`
+ `tag:GetResources`

**AWS managed policy**
+ [AWSFaultInjectionSimulatorEKSAccess](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSFaultInjectionSimulatorEKSAccess.html)

## Amazon ElastiCache actions
<a name="elasticache-actions-reference"></a>

AWS FIS supports the following ElastiCache action.

### aws:elasticache:replicationgroup-interrupt-az-power
<a name="replicationgroup-interrupt-az-power"></a>

Interrupts power to nodes in the specified Availability Zone for target ElastiCache replication groups with Multi-AZ enabled. Only one Availability Zone per replication group can be impacted at a time. When a primary node is targeted, the corresponding read replica with the least replication lag is promoted to primary. Read replica replacements in the specified Availability Zone are blocked for the duration of this action, which means that target Replication Groups operate with reduced capacity. The target for this action supports both Redis and Valkey engines. The action does not support the "serverless" deployment option.

**Resource type**
+ **aws:elasticache:replicationgroup**

**Parameters**
+ **duration** – The duration, from one minute to 12 hours. In the AWS FIS API, the value is a string in ISO 8601 format. For example, PT1M represents one minute. In the AWS FIS console, you enter the number of seconds, minutes, or hours.

**Permissions**
+ `elasticache:InterruptClusterAzPower`
+ `elasticache:DescribeReplicationGroups`
+ `tag:GetResources`

## Amazon Kinesis Data Streams actions
<a name="aws-kinesis-actions"></a>

Amazon Kinesis Data Streams supports the following Kinesis actions.

**Topics**
+ [aws:kinesis:stream-provisioned-throughput-exception](#throughput-exception)
+ [aws:kinesis:stream-expired-iterator-exception](#iterator-exception)

### aws:kinesis:stream-provisioned-throughput-exception
<a name="throughput-exception"></a>

Injects `ProvisionedThroughputExceededException` error responses on requests for the targeted Kinesis Data Streams. Supported operations include: `GetRecords`, `GetShardIterator`, `PutRecord`, and `PutRecords`.

**Resource type**
+ ****aws:kinesis:stream****

**Parameters**
+ **duration** – The duration, which ranges from one minute to 12 hours. In the AWS FISAPI, the value is a string in ISO 8601 format. For example, PT1M represents one minute. In the AWS FIS console, you enter the number of seconds, minutes, or hours.
+ **percentage** – The percentage (1-100) of calls to inject the fault into.

**Permissions**
+ `kinesis:InjectApiError`

### aws:kinesis:stream-expired-iterator-exception
<a name="iterator-exception"></a>

Injects `ExpiredIteratorException` error responses for `GetRecords` calls targeting specified Kinesis Data Streams.

**Resource type**
+ ******aws:kinesis:stream******

**Parameters**
+ **duration** – The duration, which ranges from one minute to 12 hours. In the AWS FISAPI, the value is a string in ISO 8601 format. For example, PT1M represents one minute. In the AWS FIS console, you enter the number of seconds, minutes, or hours.
+ **percentage** – The percentage (1-100) of calls to inject the fault into.

**Permissions**
+ `kinesis:InjectApiError`

## AWS Lambda actions
<a name="aws-lambda-actions-reference"></a>

AWS Lambda supports the following Lambda actions

**Topics**
+ [aws:lambda:invocation-add-delay](#invocation-add-delay)
+ [aws:lambda:invocation-error](#invocation-error)
+ [aws:lambda:invocation-http-integration-response](#invocation-http-integration-response)

### aws:lambda:invocation-add-delay
<a name="invocation-add-delay"></a>



Delays starting a function for a number of milliseconds that you specify. The effect of this action is similar to Lambda cold starts, but the additional time is spent as part of the billed duration and is applied to all execution environments rather than only affecting new execution environments. This means that you may experience both a Lambda cold start and this delay. By setting a latency value higher than the timeout configured on the Lambda function, this action will also provide access to a high fidelity timeout event.

**Resource type**
+ **aws:lambda:function**

**Parameters**
+ **duration** – The length of time that the action lasts. In the AWS FIS API, the value is a string in ISO 8601 format. For example, PT1M represents one minute. In the AWS FIS console, you enter the number of seconds, minutes, or hours.
+ **invocationPercentage** – Optional. The percentage (1-100) of function invocations to inject the fault into. The default is 100.
+ **startupDelayMilliseconds** – Optional. The amount of time in milliseconds (0-900,000) to wait between invocation and execution of function code. The default is 1000.

**Permissions**
+ `s3:PutObject`
+ `s3:DeleteObject`
+ `lambda:GetFunction`
+ `tag:GetResources`

### aws:lambda:invocation-error
<a name="invocation-error"></a>



Marks Lambda function invocations as failed. This action is useful for testing error handling mechanisms, such as alarms and retry configurations. While using this action, you select whether or not to run the function code before returning an error.

**Resource type**
+ **aws:lambda:function**

**Parameters**
+ **duration** – The length of time that the action lasts. In the AWS FIS API, the value is a string in ISO 8601 format. For example, PT1M represents one minute. In the AWS FIS console, you enter the number of seconds, minutes, or hours.
+ **invocationPercentage** – Optional. The percentage (1-100) of function invocations to inject the fault into. The default is 100.
+ **preventExecution** – If the value is true, the action will return the error without executing the function. We recommend setting the `AWS_FIS_POLL_MAX_WAIT_MILLISECONDS` environment variable to a non-zero value (for example, `2000`) to ensure the extension has up-to-date fault configuration before evaluating the invocation. For more information, see [AWS FIS Lambda environment variables](use-lambda-actions.md#fis-extension-environment-variables).

**Permissions**
+ `s3:PutObject`
+ `s3:DeleteObject`
+ `lambda:GetFunction`
+ `tag:GetResources`

### aws:lambda:invocation-http-integration-response
<a name="invocation-http-integration-response"></a>



Modifies the behavior of the function. You select a content type and HTTP response code to support integrations with ALB, API-GW and VPC Lattice. To enable selectively impacting upstream or downstream integrations, you can choose whether to directly return the modified response or whether to run the function and replace the response after the function finishes execution.

**Resource type**
+ **aws:lambda:function**

**Parameters**
+ **contentTypeHeader** – String value of HTTP content type header to return from Lambda function.
+ **duration** – The length of time that the action lasts. In the AWS FIS API, the value is a string in ISO 8601 format. For example, PT1M represents one minute. In the AWS FIS console, you enter the number of seconds, minutes, or hours.
+ **invocationPercentage** – Optional. The percentage (1-100) of function invocations to inject the fault into. The default is 100.
+ **preventExecution** – If the value is true, the action will return the response without executing the function. We recommend setting the `AWS_FIS_POLL_MAX_WAIT_MILLISECONDS` environment variable to a non-zero value (for example, `2000`) to ensure the extension has up-to-date fault configuration before evaluating the invocation. For more information, see [AWS FIS Lambda environment variables](use-lambda-actions.md#fis-extension-environment-variables).
+ **statusCode** – Value of HTTP status code (000-999) to return from Lambda function.

**Permissions**
+ `s3:PutObject`
+ `s3:DeleteObject`
+ `lambda:GetFunction`
+ `tag:GetResources`

## Amazon MemoryDB action
<a name="memorydb-actions-reference"></a>

AWS FIS supports the following MemoryDB action.

### aws:memorydb:multi-region-cluster-pause-replication
<a name="multi-region-cluster-pause-replication"></a>

Pauses the replication between one regional cluster and all other regional clusters within the multi-Region cluster. The regional cluster targeted is the cluster in the Region where the FIS experiment is running. While the replication is paused, the multi-Region cluster cannot be updated. Once the action completes, it may take a few minutes for the multi-Region cluster to return to an available state. To learn more about Amazon MemoryDB Multi-Region, see the [Amazon MemoryDB Multi-Region Developer Guide](https://docs.aws.amazon.com/memorydb/latest/devguide/multi-region.html). For Region availability, see [MemoryDB Multi-Region Prerequisites and limitations](https://docs.aws.amazon.com/memorydb/latest/devguide/multi-region.prereq.html).

**Resource type**
+ **aws:memorydb:multi-region-cluster**

**Parameters**
+ **duration** – The duration, from one minute to 12 hours. In the AWS FIS API, the value is a string in ISO 8601 format. For example, PT1M represents one minute. In the AWS FIS console, you enter the number of seconds, minutes, or hours.

**Permissions**
+ `memorydb:DescribeMultiRegionClusters`
+ `memorydb:PauseMultiRegionClusterReplication`
+ `tag:GetResources`

## Network actions
<a name="network-actions-reference"></a>

AWS FIS supports the following network actions.

**Topics**
+ [aws:network:disrupt-connectivity](#disrupt-connectivity)
+ [aws:network:route-table-disrupt-cross-region-connectivity](#route-table-disrupt-cross-region-connectivity)
+ [aws:network:transit-gateway-disrupt-cross-region-connectivity](#transit-gateway-disrupt-cross-region-connectivity)
+ [aws:network:disrupt-vpc-endpoint](#disrupt-vpc-endpoint)

### aws:network:disrupt-connectivity
<a name="disrupt-connectivity"></a>

Denies the specified traffic to the target subnets by temporarily cloning the original network access control list (network ACL) associated with the targeted subnet. FIS adds deny rules to the cloned network ACL, which has a tag managedbyFIS=true, and associates it with the subnet for the duration of the action. At action completion, FIS deletes the cloned network ACL and restores the original network ACL association.

**Resource type**
+ **aws:ec2:subnet**

**Parameters**
+ **scope** – The type of traffic to deny. When the scope is not `all`, the maximum number of entries in network ACLs is 20. The possible values are:
  + `all` – Denies all traffic entering and leaving the subnet. Note that this option allows intra-subnet traffic, including traffic to and from network interfaces in the subnet.
  + `availability-zone` – Denies intra-VPC traffic to and from subnets in other Availability Zones. The maximum number of subnets that can be targeted in a VPC is 30.
  + `dynamodb` – Denies traffic to and from the Regional endpoint for DynamoDB in the current Region.
  + `prefix-list` – Denies traffic to and from the specified prefix list.
  + `s3` – Denies traffic to and from the Regional endpoint for Amazon S3 in the current Region.
  + `s3express` – Denies traffic to and from the zonal endpoint for Amazon S3 Express One Zone in the target subnets’ AZ. Target subnets must reside in AZs where S3 Express One Zone is currently available. For more information, see [S3 Express One Zone Availability Zones and Regions.](https://docs.aws.amazon.com/AmazonS3/latest/userguide/s3-express-Endpoints.html)
  + `vpc` – Denies traffic entering and leaving the VPC.
+ **duration** – The duration, from one minute to 12 hours. In the AWS FIS API, the value is a string in ISO 8601 format. For example, PT1M represents one minute. In the AWS FIS console, you enter the number of seconds, minutes, or hours.
+ **prefixListIdentifier** – If the scope is `prefix-list`, this is the identifier of the customer managed prefix list. You can specify a name, an ID, or an ARN. The prefix list can have at most 10 entries.

**Permissions**
+ `ec2:CreateNetworkAcl` – Creates the network ACL with the tag managedByFIS=true.
+ `ec2:CreateNetworkAclEntry` – The network ACL must have the tag managedByFIS=true.
+ `ec2:CreateTags`
+ `ec2:DeleteNetworkAcl` – The network ACL must have the tag managedByFIS=true.
+ `ec2:DescribeManagedPrefixLists`
+ `ec2:DescribeNetworkAcls`
+ `ec2:DescribeSubnets`
+ `ec2:DescribeVpcs`
+ `ec2:GetManagedPrefixListEntries`
+ `ec2:ReplaceNetworkAclAssociation`

**AWS managed policy**
+ [AWSFaultInjectionSimulatorNetworkAccess](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSFaultInjectionSimulatorNetworkAccess.html)

### aws:network:route-table-disrupt-cross-region-connectivity
<a name="route-table-disrupt-cross-region-connectivity"></a>

Blocks traffic that originates in the target subnets and is destined for the specified Region. Creates route tables that include all routes for the Region to isolate. To allow FIS to create these route tables, raise the Amazon VPC quota for `routes per route table` to 250 (or 350 if the `region` parameter is us-east-1) plus the number of routes in your existing route tables.

**Resource type**
+ **aws:ec2:subnet**

**Parameters**
+ `region` – The code of the Region to isolate (for example, eu-west-1).
+ `duration` – The length of time the action lasts. In the AWS FIS API, the value is a string in ISO 8601 format. For example, PT1M represents one minute. In the AWS FIS console, you enter the number of seconds, minutes, or hours.

**Permissions**
+ `ec2:AssociateRouteTable`
+ `ec2:CreateManagedPrefixList` †
+ `ec2:CreateNetworkInterface` †
+ `ec2:CreateRoute` †
+ `ec2:CreateRouteTable` †
+ `ec2:CreateTags` †
+ `ec2:DeleteManagedPrefixList` †
+ `ec2:DeleteNetworkInterface` †
+ `ec2:DeleteRouteTable` †
+ `ec2:DescribeManagedPrefixLists`
+ `ec2:DescribeNetworkInterfaces`
+ `ec2:DescribeRouteTables`
+ `ec2:DescribeSubnets`
+ `ec2:DescribeVpcPeeringConnections`
+ `ec2:DescribeVpcs`
+ `ec2:DisassociateRouteTable`
+ `ec2:GetManagedPrefixListEntries`
+ `ec2:ModifyManagedPrefixList` †
+ `ec2:ModifyVpcEndpoint`
+ `ec2:ReplaceRouteTableAssociation`

† Scoped using the tag managedByFIS=true. You do not need to manage this tag. AWS FIS adds and removes this tag during the experiment. 

**AWS managed policy**
+ [AWSFaultInjectionSimulatorNetworkAccess](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSFaultInjectionSimulatorNetworkAccess.html)

### aws:network:transit-gateway-disrupt-cross-region-connectivity
<a name="transit-gateway-disrupt-cross-region-connectivity"></a>

Blocks traffic from the target transit gateway peering attachments that is destined for the specified Region.

**Resource type**
+ **aws:ec2:transit-gateway**

**Parameters**
+ `region` – The code of the Region to isolate (for example, eu-west-1).
+ `duration` – The length of time the action lasts. In the AWS FIS API, the value is a string in ISO 8601 format. For example, PT1M represents one minute. In the AWS FIS console, you enter the number of seconds, minutes, or hours.

**Permissions**
+ `ec2:AssociateTransitGatewayRouteTable`
+ `ec2:DescribeTransitGatewayAttachments`
+ `ec2:DescribeTransitGatewayPeeringAttachments`
+ `ec2:DescribeTransitGateways`
+ `ec2:DisassociateTransitGatewayRouteTable`

**AWS managed policy**
+ [AWSFaultInjectionSimulatorNetworkAccess](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSFaultInjectionSimulatorNetworkAccess.html)

### aws:network:disrupt-vpc-endpoint
<a name="disrupt-vpc-endpoint"></a>

Blocks inbound and outbound traffic of the target interface VPC endpoints. FIS creates a managed security group with empty rules and temporarily replaces security groups of the target VPC endpoints with this managed security group. If modifications are made to the target resources during action execution, the action will fail and the resources will not be restored to their pre-experiment state. Additionally, if a FIS-managed security group is modified during action execution, it will not be deleted by FIS. .

**Resource type**
+ **aws:ec2:vpc-endpoint**

**Parameters**
+ `duration` – The length of time the action lasts. In the AWS FIS API, the value is a string in ISO 8601 format. For example, PT1M represents one minute. In the AWS FIS console, you enter the number of seconds, minutes, or hours.

**Permissions**
+ `ec2:DescribeVpcEndpoints`
+ `ec2:DescribeSecurityGroups`
+ `ec2:ModifyVpcEndpoint`
+ `ec2:CreateSecurityGroup`
+ `ec2:DeleteSecurityGroup`
+ `ec2:RevokeSecurityGroupEgress`
+ `ec2:CreateTags`
+ `vpce:AllowMultiRegion` \*

\* The permission is only required if you are targeting cross-region VPC endpoints

## Amazon RDS actions
<a name="rds-actions-reference"></a>

AWS FIS supports the following Amazon RDS actions.

**Topics**
+ [aws:rds:failover-db-cluster](#failover-db-cluster)
+ [aws:rds:reboot-db-instances](#reboot-db-instances)

### aws:rds:failover-db-cluster
<a name="failover-db-cluster"></a>

Runs the Amazon RDS API action [FailoverDBCluster](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_FailoverDBCluster.html) on the target Aurora DB cluster. RDS clusters and DocumentDB clusters are supported.

**Resource type**
+ **aws:rds:cluster**

**Parameters**
+ None

**Permissions**
+ `rds:FailoverDBCluster`
+ `rds:DescribeDBClusters`
+ `tag:GetResources`

**AWS managed policy**
+ [AWSFaultInjectionSimulatorRDSAccess](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSFaultInjectionSimulatorRDSAccess.html)

### aws:rds:reboot-db-instances
<a name="reboot-db-instances"></a>

Runs the Amazon RDS API action [RebootDBInstance](https://docs.aws.amazon.com/AmazonRDS/latest/APIReference/API_RebootDBInstance.html) on the target DB instance. RDS clusters and DocumentDB clusters are supported.

**Resource type**
+ **aws:rds:db**

**Parameters**
+ **forceFailover** – Optional. If the value is true, and if instances are Multi-AZ, forces failover from one Availability Zone to another. The default is false.

**Permissions**
+ `rds:RebootDBInstance`
+ `rds:DescribeDBInstances`
+ `tag:GetResources`

**AWS managed policy**
+ [AWSFaultInjectionSimulatorRDSAccess](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSFaultInjectionSimulatorRDSAccess.html)

## Amazon S3 actions
<a name="s3-actions-reference-fis"></a>

AWS FIS supports the following Amazon S3 action.

**Topics**
+ [aws:s3:bucket-pause-replication](#bucket-pause-replication)

### aws:s3:bucket-pause-replication
<a name="bucket-pause-replication"></a>

 Pauses replication from target source buckets to destination buckets. Destination buckets can be in different AWS Regions or within the same Region as the source bucket. Existing objects may continue to be replicated for up to one hour after action begins. This action only supports targeting by tags. To learn more about Amazon S3 Replication, see the [Amazon S3 user guide](https://docs.aws.amazon.com/AmazonS3/latest/userguide/replication.html).

**Resource type**
+ **aws:s3:bucket**

**Parameters**
+ **duration** – The duration, from one minute to 12 hours. In the AWS FIS API, the value is a string in ISO 8601 format. For example, PT1M represents one minute. In the AWS FIS console, you enter the number of seconds, minutes, or hours.
+ **region** – The AWS region where destination buckets are located.
+ **destinationBuckets** – Optional. Comma separated list of destination S3 bucket(s).
+ **prefixes** – Optional. Comma separated list of S3 object key prefixes from replication rule filters. Replication rules of target buckets with a filter based on the prefix(es) will be paused. 

**Permissions**
+ `S3:PutReplicationConfiguration` with condition key `S3:IsReplicationPauseRequest` set to `True`
+ `S3:GetReplicationConfiguration` with condition key `S3:IsReplicationPauseRequest` set to `True`
+ `S3:PauseReplication`
+ `S3:ListAllMyBuckets`
+ `tag:GetResources`

For an example policy, see [Example: Use condition keys for `aws:s3:bucket-pause-replication`](security_iam_id-based-policy-examples.md#security-iam-policy-examples-s3).

## Systems Manager actions
<a name="ssm-actions-reference"></a>

AWS FIS supports the following Systems Manager actions.

**Topics**
+ [aws:ssm:send-command](#ssm-send-command)
+ [aws:ssm:start-automation-execution](#ssm-start-automation-execution)

### aws:ssm:send-command
<a name="ssm-send-command"></a>

Runs the Systems Manager API action [SendCommand](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_SendCommand.html) on the target EC2 instances. The Systems Manager document (SSM document) defines the actions that Systems Manager performs on your instances. For more information, see [Use the aws:ssm:send-command action](actions-ssm-agent.md#specifying-ssm-actions).

**Resource type**
+ **aws:ec2:instance**

**Parameters**
+ **documentArn** – The Amazon Resource Name (ARN) of the document. In the console, this parameter is completed for you if you choose a value from **Action type** that corresponds to one of the [pre-configured AWS FIS SSM documents](actions-ssm-agent.md#fis-ssm-docs).
+ **documentVersion** – Optional. The version of the document. If empty, the default version runs.
+ **documentParameters** – Conditional. The required and optional parameters that the document accepts. The format is a JSON object with keys that are strings and values that are either strings or arrays of strings.
+ **duration** – The duration, from one minute to 12 hours. In the AWS FIS API, the value is a string in ISO 8601 format. For example, PT1M represents one minute. In the AWS FIS console, you enter the number of seconds, minutes, or hours.

**Permissions**
+ `ssm:SendCommand`
+ `ssm:ListCommands`
+ `ssm:CancelCommand`

**AWS managed policy**
+ [AWSFaultInjectionSimulatorEC2Access](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSFaultInjectionSimulatorEC2Access.html)

### aws:ssm:start-automation-execution
<a name="ssm-start-automation-execution"></a>

Runs the Systems Manager API action [StartAutomationExecution](https://docs.aws.amazon.com/systems-manager/latest/APIReference/API_StartAutomationExecution.html).

**Resource type**
+ None

**Parameters**
+ **documentArn** – The Amazon Resource Name (ARN) of the automation document.
+ **documentVersion** – Optional. The version of the document. If empty, the default version runs.
+ **documentParameters** – Conditional. The required and optional parameters that the document accepts. The format is a JSON object with keys that are strings and values that are either strings or arrays of strings.
+ **maxDuration** – The maximum time allowed for the automation execution to complete, from one minute to 12 hours. In the AWS FIS API, the value is a string in ISO 8601 format. For example, PT1M represents one minute. In the AWS FIS console, you enter the number of seconds, minutes, or hours.

**Permissions**
+ `ssm:GetAutomationExecution`
+ `ssm:StartAutomationExecution`
+ `ssm:StopAutomationExecution`
+ `iam:PassRole` – Optional. Required if the automation document assumes a role.

**AWS managed policy**
+ [AWSFaultInjectionSimulatorSSMAccess](https://docs.aws.amazon.com/aws-managed-policy/latest/reference/AWSFaultInjectionSimulatorSSMAccess.html)

## AWS Direct Connect actions
<a name="directconnect-actions-reference"></a>

AWS FIS supports the following AWS Direct Connect action.

**Topics**
+ [aws:directconnect:virtual-interface-disconnect](#directconnect-virtual-interface-disconnect)

### aws:directconnect:virtual-interface-disconnect
<a name="directconnect-virtual-interface-disconnect"></a>

Tests the resilience of the AWS Direct Connect connection by temporarily disrupting the Border Gateway Protocol (BGP) sessions between the on-premises networks and peers associated with target Virtual Interfaces (VIFs). Before initiating the experiment, FIS verifies that all VIFs targeted in the experiment are in an 'available' state and each VIF has all BGP peers with 'available' state and 'up' BGP status. During the experiment, BGP peering sessions for the targeted Virtual Interfaces will be placed in the down state. For the detailed information about Direct Connect failover testing, please refer to the [AWS Direct Connect documentation](https://docs.aws.amazon.com/directconnect/latest/UserGuide/resiliency_failover.html).

**Resource type**
+ aws:directconnect:virtual-interface

**Parameters**
+ `duration` – The duration, from 10 minutes to 12 hours. In the AWS FIS API, the value is a string in ISO 8601 format. For example, PT10M represents ten minutes. In the AWS FIS console, you enter the number of seconds, minutes, or hours.

**Permissions**
+ `directconnect:DescribeVirtualInterfaces`
+ `directconnect:StartBgpFailoverTest`
+ `directconnect:ListVirtualInterfaceTestHistory`
+ `directconnect:StopBgpFailoverTest`
+ `tag:GetResources`