# Cross-AZ: Traffic Slowdown

You can use the Cross-AZ: Traffic Slowdown scenario to inject packet loss to disrupt and slow down traffic between Availability Zones (AZs).
The packet loss impairs cross-AZ communication, a partial disruption, sometimes known as a gray failure. It injects packet loss on network flows between target resources.
Network flows represent the traffic between computing resources — the data packets carrying requests, responses, and other communications between your servers, containers, and services.
The scenario can help to validate observability setups, tune alarm thresholds, discover application sensitivity and dependencies in cross-AZ communication, and practice critical operational decisions like AZ evacuation.

By default, the scenario injects 15% packet loss to 100% of outbound network flows for target resources from the selected AZ for a duration of 30 minutes.
You can use the **Edit shared parameters** dialog in the AWS FIS console to adjust the following parameters at the scenario level, which then apply to the underlying actions:

- Availability Zone - you can select the AZ to impair, and packet loss will be injected from that AZ to the other AZs within the Region.
- Packet Loss - adjust the packet loss lower for subtle disruption testing, such as 5%, or higher to test severe communication degradation and recovery mechanisms, such as 50%, or even 100% for total connectivity impact.
- Flows percentage - reduce to impair a subset of traffic.
  For example, you can inject 15% packet loss affecting 25% of the network flows for even more subtle testing.
- Duration - set how long the experiment runs. You can shorten for quicker tests, or run longer sustained tests.
  For example, set the duration to 2 hours to help test recovery mechanisms under impaired conditions.
- Resource targeting - you can define target resources for the overall scenario using tags (for EC2 instances or ECS tasks on EC2 or Fargate) or labels (for EKS pods on EC2).
  You can specify your own tags and labels, or use the defaults provided in the scenario.
  If you don’t wish to use tags or labels, you can edit the action to target resources by specifying other parameters.
- Customization - If you don’t want to target EC2 or ECS resources, you can leave the actions with default tags. The experiment won’t find any resources to target and the action will be skipped.
  However, if you don’t want to target EKS resources, you should remove the EKS action and target from the scenario completely, as it requires an EKS cluster identifier to be provided.
  For even more granular customization, you can modify individual actions in the experiment template directly.

## Actions

Together, the following actions help create the symptoms of a traffic slowdown between AZs by introducing packet loss on outbound communication from the target AZ to other AZs in the region at the network layer.
These actions run in parallel, each injecting 15% packet loss for 30 minutes by default. After this period, communication returns to normal.
The scenario needs at least one of the following resource types in the selected AZ to run: EC2 instance, ECS task, or EKS pod.

### ECS Network Packet Loss

Cross-AZ: Traffic Slowdown includes [aws:ecs:task-network-packet-loss](fis-actions-reference.md#task-network-packet-loss "fis-actions-reference.md#task-network-packet-loss") to inject packet loss for ECS tasks.
The action targets tasks in the selected AZ, and impairs their outbound communication to all other AZs in the Region.
You can further customize the scope of the impact by editing the action and adding or removing AZs from the `Sources` field.
By default, it targets tasks with a [tag](../../../AmazonECS/latest/developerguide/ecs-using-tags.md "../../../AmazonECS/latest/developerguide/ecs-using-tags.md") named `CrossAZTrafficSlowdown` with a value of `PacketLossForECS`.
You can replace the default tag with your own, or add the scenario tag to your tasks. If no valid tasks are found this action will be skipped.
Before running an experiment on ECS, you should follow the [setup steps for ECS task actions](ecs-task-actions.md "ecs-task-actions.md").

### EKS Network Packet Loss

Cross-AZ: Traffic Slowdown includes [aws:eks:pod-network-packet-loss](fis-actions-reference.md#pod-network-packet-loss "fis-actions-reference.md#pod-network-packet-loss") to inject packet loss for EKS pods.
The action targets pods in the selected AZ, and impairs their outbound communication to all other AZs in the region.
You can further customize the scope of the impact by editing the action and adding or removing AZs from the `Sources` field.
By default, it targets pods within a cluster that have labels with the format key=value. The default label provided is `CrossAZTraffic=PacketLossForEKS`.
You can replace the default label with your own, or add this label to your pods. If no valid pods are found this action will be skipped.
Before running an experiment on EKS, you should follow the [setup steps for EKS pod actions](eks-pod-actions.md "eks-pod-actions.md").

### EC2 Network Packet Loss

Cross-AZ: Traffic Slowdown uses the [aws:ssm:send-command](fis-actions-reference.md#ssm-send-command "fis-actions-reference.md#ssm-send-command") action to run the [AWSFIS-Run-Network-Packet-Loss-Sources](actions-ssm-agent.md#awsfis-run-network-packet-loss-sources "actions-ssm-agent.md#awsfis-run-network-packet-loss-sources") document to inject packet loss for EC2 instances, and impairs their outbound communication to all other AZs in the Region.
You can further customize the scope of the impact by editing the action and adding or removing AZs from the `Sources` field. The action targets instances in the selected AZ.
By default, it targets instances with a [tag](../../../AWSEC2/latest/UserGuide/Using_Tags.md "../../../AWSEC2/latest/UserGuide/Using_Tags.md") named `CrossAZTrafficSlowdown` with a value of `PacketLossForEC2`. You can replace the default tag with your own, or add this tag to your instances.
If no valid instances are found this action will be skipped.
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
When you create an experiment template from the Cross-AZ: Traffic Slowdown scenario, FIS creates the role for you with the trust policy and the following AWS managed policies:

- [AWSFaultInjectionSimulatorEC2Access](security-iam-awsmanpol.md#AWSFaultInjectionSimulatorEC2Access "security-iam-awsmanpol.md#AWSFaultInjectionSimulatorEC2Access")
- [AWSFaultInjectionSimulatorECSAccess](security-iam-awsmanpol.md#AWSFaultInjectionSimulatorECSAccess "security-iam-awsmanpol.md#AWSFaultInjectionSimulatorECSAccess")
- [AWSFaultInjectionSimulatorEKSAccess](security-iam-awsmanpol.md#AWSFaultInjectionSimulatorEKSAccess "security-iam-awsmanpol.md#AWSFaultInjectionSimulatorEKSAccess")

If you’re using an existing [IAM role](getting-started-iam-service-role.md "getting-started-iam-service-role.md") to run the Cross-AZ: Traffic Slowdown scenario, you can attach the following policy to grant AWS FIS the necessary permissions:

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
        "Name": "Cross-AZ: Traffic Slowdown"
    },
    "description": "Inject packet loss to disrupt and slow down traffic between AZs.",
    "actions": {
        "PacketLossForEC2": {
            "actionId": "aws:ssm:send-command",
            "parameters": {
                "duration": "PT30M",
                "documentArn": "arn:aws:ssm:us-east-1::document/AWSFIS-Run-Network-Packet-Loss-Sources",
                "documentParameters": "{\"Sources\":\"us-east-1b,us-east-1c,us-east-1d,us-east-1e,us-east-1f\",\"LossPercent\":\"15\",\"Interface\":\"DEFAULT\",\"TrafficType\":\"egress\",\"DurationSeconds\":\"1800\",\"FlowsPercent\":\"100\",\"InstallDependencies\":\"True\"}"
            },
            "targets": {
                "Instances": "TargetsForEC2"
            }
        },
        "PacketLossForECS": {
            "actionId": "aws:ecs:task-network-packet-loss",
            "parameters": {
                "sources": "us-east-1b,us-east-1c,us-east-1d,us-east-1e,us-east-1f",
                "lossPercent": "15",
                "duration": "PT30M",
                "flowsPercent": "100",
                "installDependencies": "true",
                "useEcsFaultInjectionEndpoints": "true"
            },
            "targets": {
                "Tasks": "TargetsForECS"
            }
        },
        "PacketLossForEKS": {
            "actionId": "aws:eks:pod-network-packet-loss",
            "parameters": {
                "sources": "us-east-1b,us-east-1c,us-east-1d,us-east-1e,us-east-1f",
                "lossPercent": "15",
                "duration": "PT30M",
                "flowsPercent": "100",
                "interface": "DEFAULT",
                "kubernetesServiceAccount": "fis-service-account"
            },
            "targets": {
                "Pods": "TargetsForEKS"
            }
        }
    },
    "targets": {
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
                "CrossAZTrafficSlowdown": "PacketLossForEC2"
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
                "CrossAZTrafficSlowdown": "PacketLossForECS"
            },
            "resourceType": "aws:ecs:task",
            "selectionMode": "ALL"
        },
        "TargetsForEKS": {
            "parameters": {
                "availabilityZoneIdentifier": "us-east-1a",
                "clusterIdentifier": "",
                "namespace": "default",
                "selectorType": "labelSelector",
                "selectorValue": "CrossAZTrafficSlowdown=PacketLossForEKS"
            },
            "resourceType": "aws:eks:pod",
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
