# AZ: Application Slowdown

You can use the AZ: Application Slowdown scenario to introduce additional latency between resources within a single Availability Zone (AZ).
This latency creates many of the symptoms of an application slowdown, a partial disruption, sometimes known as a gray failure. It adds latency to network flows between target resources.
Network flows represent the traffic between computing resources — the data packets carrying requests, responses, and other communications between your servers, containers, and services.
The scenario can help to validate observability setups, tune alarm thresholds, discover application sensitivity to slowdowns, and practice critical operational decisions like AZ evacuation.

By default, the scenario adds 200ms of latency to 100% of network flows between target resources within the selected AZ for a duration of 30 minutes.
You can use the **Edit shared parameters** dialog in the AWS FIS console to adjust the following parameters at the scenario level, which then apply to the underlying actions:

- Availability Zone - you can select the AZ to impair in the scenario.
- Milliseconds (ms) of latency - adjust this based on your application’s sensitivity and needs.
  You can set latency lower for more sensitive applications or higher to test timeout handling, for example.
  Consider using multiples of your current application latency as a baseline.
- Flows percentage - reduce to impair a subset of traffic.
  For example, you can add 200ms latency affecting 25% of the network flows for even more subtle testing.
- Duration - set how long the experiment runs. You can shorten for quicker tests, or run longer sustained tests.
  For example, set the duration to 2 hours to test your recovery mechanisms under impaired conditions.
- Resource targeting - you can define target resources for the overall scenario using tags (for EC2 instances or ECS tasks on EC2 or Fargate) or labels (for EKS pods on EC2).
  You can specify your own tags and labels, or use the defaults provided in the scenario.
  If you don’t wish to use tags or labels, you can edit the action to target resources by specifying other parameters.
- Customization - If you don’t want to target EC2 or ECS resources, you can leave the actions with default tags. The experiment won’t find any resources to target and the action will be skipped.
  However, if you don’t want to target EKS resources, you should remove the EKS action and target from the scenario completely, as it requires an EKS cluster identifier to be provided.
  For even more granular customization, you can modify individual actions in the experiment template directly.

## Actions

Together, the following actions help create many of the symptoms of an application slowdown in a single AZ by introducing additional latency on the network flows, which then propagates through the application.
These actions run in parallel, each adding 200ms latency for 30 minutes by default. After this period, latency returns to normal levels.
The scenario needs at least one of the following resource types to run: EC2 instance, ECS task, or EKS pod.

### ECS Network Latency

AZ: Application Slowdown includes [aws:ecs:task-network-latency](fis-actions-reference.md#task-network-latency "fis-actions-reference.md#task-network-latency") to introduce latency for ECS tasks.
The action targets tasks in the selected AZ. By default, it targets tasks with a [tag](../../../AmazonECS/latest/developerguide/ecs-using-tags.md "../../../AmazonECS/latest/developerguide/ecs-using-tags.md") named `AZApplicationSlowdown` with a value of `LatencyForECS`.
You can replace the default tag with your own, or add the scenario tag to your tasks. If no valid tasks are found this action will be skipped.
Before running an experiment on ECS, you should follow the [setup steps for ECS task actions](ecs-task-actions.md "ecs-task-actions.md").

### EKS Network Latency

AZ: Application Slowdown includes [aws:eks:pod-network-latency](fis-actions-reference.md#pod-network-latency "fis-actions-reference.md#pod-network-latency") to introduce latency for EKS pods.
The action targets pods in the selected AZ. By default, it targets pods within a cluster that have labels with the format key=value.
The default label provided is `AZApplicationSlowdown=LatencyForEKS`. You can replace the default label with your own, or add this label to your pods.
If no valid pods are found this action will be skipped. Before running an experiment on EKS, you should follow the [setup steps for EKS pod actions](eks-pod-actions.md "eks-pod-actions.md").

### EC2 Network Latency

AZ: Application Slowdown uses the [aws:ssm:send-command](fis-actions-reference.md#ssm-send-command "fis-actions-reference.md#ssm-send-command") action to run the [AWSFIS-Run-Network-Latency-Sources](actions-ssm-agent.md#awsfis-run-network-latency-sources "actions-ssm-agent.md#awsfis-run-network-latency-sources") document to introduce latency for EC2 instances.
The action targets instances in the selected AZ. By default, it targets instances with a [tag](../../../AWSEC2/latest/UserGuide/Using_Tags.md "../../../AWSEC2/latest/UserGuide/Using_Tags.md") named `AZApplicationSlowdown` with a value of `LatencyForEC2`.
You can replace the default tag with your own, or add this tag to your instances. If no valid instances are found this action will be skipped.
Before running an experiment on EC2 using SSM, you should [configure the AWS Systems Manager agent](actions-ssm-agent.md "actions-ssm-agent.md").

## Limitations

- This scenario does not include [stop conditions](stop-conditions.md "stop-conditions.md").
  The correct stop conditions for your application should be added to the experiment template.

## Requirements

- Add the required permissions to the AWS FIS [experiment role](getting-started-iam-service-role.md "getting-started-iam-service-role.md").
- You need to target one or more resources from any of the following 3 types within the selected AZ: EC2 instances, ECS tasks, or EKS pods.
- All targets of the scenario must be in the same VPC.

## Permissions

To run this scenario you need an IAM role with a trust policy that allows FIS to assume the role and the managed policies for the resource types you target in the experiment: EC2, ECS, and EKS.
When you create an experiment template from the AZ: Application Slowdown scenario, FIS creates the role for you with the trust policy and the following AWS managed policies:

- [AWSFaultInjectionSimulatorEC2Access](security-iam-awsmanpol.md#AWSFaultInjectionSimulatorEC2Access "security-iam-awsmanpol.md#AWSFaultInjectionSimulatorEC2Access")
- [AWSFaultInjectionSimulatorECSAccess](security-iam-awsmanpol.md#AWSFaultInjectionSimulatorECSAccess "security-iam-awsmanpol.md#AWSFaultInjectionSimulatorECSAccess")
- [AWSFaultInjectionSimulatorEKSAccess](security-iam-awsmanpol.md#AWSFaultInjectionSimulatorEKSAccess "security-iam-awsmanpol.md#AWSFaultInjectionSimulatorEKSAccess")

If you’re using an existing [IAM role](getting-started-iam-service-role.md "getting-started-iam-service-role.md") to run the AZ: Application Slowdown scenario, you can attach the following policy to grant AWS FIS the necessary permissions:

```
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Sid": "DescribeTasks",
            "Effect": "Allow",
            "Action": "ecs:DescribeTasks",
            "Resource": "*"
        },
        {
            "Sid": "DescribeContainerInstances",
            "Effect": "Allow",
            "Action": "ecs:DescribeContainerInstances",
            "Resource": "arn:aws:ecs:*:*:container-instance/*/*"
        },
        {
            "Sid": "DescribeInstances",
            "Effect": "Allow",
            "Action": "ec2:DescribeInstances",
            "Resource": "*"
        },
        {
            "Sid": "DescribeSubnets",
            "Effect": "Allow",
            "Action": "ec2:DescribeSubnets",
            "Resource": "*"
        },
        {
            "Sid": "DescribeCluster",
            "Effect": "Allow",
            "Action": "eks:DescribeCluster",
            "Resource": "arn:aws:eks:*:*:cluster/*"
        },
        {
            "Sid": "TargetResolutionByTags",
            "Effect": "Allow",
            "Action": "tag:GetResources",
            "Resource": "*"
        },
        {
            "Sid": "SendCommand",
            "Effect": "Allow",
            "Action": [
                "ssm:SendCommand"
            ],
            "Resource": [
                "arn:aws:ec2:*:*:instance/*",
                "arn:aws:ssm:*:*:managed-instance/*",
                "arn:aws:ssm:*:*:document/*"
            ]
        },
        {
            "Sid": "ListCommands",
            "Effect": "Allow",
            "Action": [
                "ssm:ListCommands"
            ],
            "Resource": "*"
        },
        {
            "Sid": "CancelCommand",
            "Effect": "Allow",
            "Action": [
                "ssm:CancelCommand"
            ],
            "Resource": "*"
        }
    ]
}
```

## Scenario Content

The following content defines the scenario.
This JSON can be saved and used to create an [experiment template](experiment-templates.md "experiment-templates.md") using the [create-experiment-template](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/fis/create-experiment-template.html "https://awscli.amazonaws.com/v2/documentation/api/latest/reference/fis/create-experiment-template.html") command from the AWS Command Line Interface (AWS CLI).
For the most recent version of the scenario, visit the scenario library in the FIS console and go to the **Content** tab.

```
{
    "tags": {
        "Name": "AZ: Application Slowdown"
    },
    "description": "Add latency between resources within a single AZ.",
    "actions": {
        "LatencyForEKS": {
            "actionId": "aws:eks:pod-network-latency",
            "parameters": {
                "delayMilliseconds": "200",
                "duration": "PT30M",
                "flowsPercent": "100",
                "interface": "DEFAULT",
                "kubernetesServiceAccount": "fis-service-account",
                "sources": "us-east-1a"
            },
            "targets": {
                "Pods": "TargetsForEKS"
            }
        },
        "LatencyForEC2": {
            "actionId": "aws:ssm:send-command",
            "parameters": {
                "duration": "PT30M",
                "documentArn": "arn:aws:ssm:us-east-1::document/AWSFIS-Run-Network-Latency-Sources",
                "documentParameters": "{\"DelayMilliseconds\":\"200\",\"Sources\":\"us-east-1a\",\"Interface\":\"DEFAULT\",\"TrafficType\":\"egress\",\"DurationSeconds\":\"1800\",\"FlowsPercent\":\"100\",\"InstallDependencies\":\"True\"}"
            },
            "targets": {
                "Instances": "TargetsForEC2"
            }
        },
        "LatencyForECS": {
            "actionId": "aws:ecs:task-network-latency",
            "parameters": {
                "delayMilliseconds": "200",
                "duration": "PT30M",
                "flowsPercent": "100",
                "installDependencies": "true",
                "sources": "us-east-1a",
                "useEcsFaultInjectionEndpoints": "true"
            },
            "targets": {
                "Tasks": "TargetsForECS"
            },
            "startAfter": []
        }
    },
    "targets": {
        "TargetsForEKS": {
            "parameters": {
                "availabilityZoneIdentifier": "us-east-1a",
                "clusterIdentifier": "",
                "namespace": "default",
                "selectorType": "labelSelector",
                "selectorValue": "AZApplicationSlowdown=LatencyForEKS"
            },
            "resourceType": "aws:eks:pod",
            "selectionMode": "ALL"
        },
        "TargetsForEC2": {
            "filters": [
                {
                    "path": "Placement.AvailabilityZone",
                    "values": [
                        "us-east-1a"
                    ]
                }
            ],
            "resourceTags": {
                "AZApplicationSlowdown": "LatencyForEC2"
            },
            "resourceType": "aws:ec2:instance",
            "selectionMode": "ALL"
        },
        "TargetsForECS": {
            "filters": [
                {
                    "path": "AvailabilityZone",
                    "values": [
                        "us-east-1a"
                    ]
                }
            ],
            "resourceTags": {
                "AZApplicationSlowdown": "LatencyForECS"
            },
            "resourceType": "aws:ecs:task",
            "selectionMode": "ALL"
        }
    },
    "experimentOptions": {
        "accountTargeting": "single-account",
        "emptyTargetResolutionMode": "skip"
    },
    "stopConditions": [
        {
            "source": "none"
        }
    ]
}
```
