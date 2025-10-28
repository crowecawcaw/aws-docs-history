# Example AWS FIS experiment templates

If you're using the AWS FIS API or a command line tool to create an experiment template,
you can construct the template in JavaScript Object Notation (JSON). For more information
about the components of an experiment template, see [AWS FIS experiment template components](experiment-templates.md "experiment-templates.md").

To create an experiment using one of the example templates, save it to a JSON file (for example,
`my-template.json`), replace the placeholder values in `italics`
with your own values, and then run the following [create-experiment-template](../../../cli/latest/reference/fis/create-experiment-template.md "../../../cli/latest/reference/fis/create-experiment-template.md") command.

```
aws fis create-experiment-template --cli-input-json file://`my-template`.json
```

###### Example templates

- [Stop EC2 instances based on filters](#stop-instances-filters "#stop-instances-filters")
- [Stop a specified number of EC2 instances](#stop-instances-count "#stop-instances-count")
- [Run a pre-configured AWS FIS SSM document](#cpu-fault-injection "#cpu-fault-injection")
- [Run a predefined Automation runbook](#run-automation-runbook "#run-automation-runbook")
- [Throttle API actions on EC2 instances with the target IAM role](#inject-api-throttle "#inject-api-throttle")
- [Stress test CPU of pods in a Kubernetes cluster](#stress-test "#stress-test")
- [Provisioned throughput exception for specified number of Kinesis Data Streams](#throughput-kinesis "#throughput-kinesis")
- [Experiment role permissions example](#permissions-example "#permissions-example")

## Stop EC2 instances based on filters

The following example stops all running Amazon EC2 instances in the specified Region
with the specified tag in the specified VPC. It restarts them after two minutes.

```
{
    "tags": {
        "Name": "StopEC2InstancesWithFilters"
    },
    "description": "Stop and restart all instances in us-east-1b with the tag env=prod in the specified VPC",
    "targets": {
        "myInstances": {
            "resourceType": "aws:ec2:instance",
            "resourceTags": {
                "`env`": "`prod`"
            },
            "filters": [
                {
                    "path": "Placement.AvailabilityZone",
                    "values": ["`us-east-1b`"]
                },
                {
                    "path": "State.Name",
                    "values": ["`running`"]
                },
                {
                    "path": "VpcId",
                    "values": [ "`vpc-aabbcc11223344556`"]
                }
            ],
            "selectionMode": "`ALL`"
        }
    },
    "actions": {
        "StopInstances": {
            "actionId": "aws:ec2:stop-instances",
            "description": "stop the instances",
            "parameters": {
                "startInstancesAfterDuration": "`PT2M`"
            },
            "targets": {
                "Instances": "myInstances"
            }
        }
    },
    "stopConditions": [
        {
            "source": "aws:cloudwatch:alarm",
            "value": "arn:aws:cloudwatch:`us-east-1`:`111122223333`:alarm:`alarm-name`"
        }
    ],
    "roleArn": "arn:aws:iam::`111122223333`:role/`role-name`"
}
```

## Stop a specified number of EC2 instances

The following example stops three instances with the specified tag. AWS FIS selects the
specific instances to stop at random. It restarts these instances after two minutes.

```
{
    "tags": {
        "Name": "StopEC2InstancesByCount"
    },
    "description": "Stop and restart three instances with the specified tag",
    "targets": {
        "myInstances": {
            "resourceType": "aws:ec2:instance",
            "resourceTags": {
                "`env`": "`prod`"
            },
            "selectionMode": "`COUNT(3)`"
        }
    },
    "actions": {
        "StopInstances": {
            "actionId": "aws:ec2:stop-instances",
            "description": "stop the instances",
            "parameters": {
                "startInstancesAfterDuration": "`PT2M`"
            },
            "targets": {
                "Instances": "myInstances"
            }
        }
    },
    "stopConditions": [
        {
            "source": "aws:cloudwatch:alarm",
            "value": "arn:aws:cloudwatch:`us-east-1`:`111122223333`:alarm:`alarm-name`"
        }
    ],
    "roleArn": "arn:aws:iam::`111122223333`:role/`role-name`"
}
```

## Run a pre-configured AWS FIS SSM document

The following example runs a CPU fault injection for 60 seconds on the specified EC2 instance
using a pre-configured AWS FIS SSM document, [AWSFIS-Run-CPU-Stress](actions-ssm-agent.md#awsfis-run-cpu-stress "actions-ssm-agent.md#awsfis-run-cpu-stress"). AWS FIS monitors the experiment for two minutes.

```
{
    "tags": {
        "Name": "CPUStress"
    },
    "description": "Run a CPU fault injection on the specified instance",
    "targets": {
        "myInstance": {
            "resourceType": "aws:ec2:instance",
            "resourceArns": ["arn:aws:ec2:`us-east-1`:`111122223333`:instance/`instance-id`"],
            "selectionMode": "`ALL`"
        }
    },
    "actions": {
        "CPUStress": {
            "actionId": "aws:ssm:send-command",
            "description": "run cpu stress using ssm",
            "parameters": {
                "duration": "`PT2M`",
                "documentArn": "arn:aws:ssm:`us-east-1`::document/`AWSFIS-Run-CPU-Stress`",
                "documentParameters": "{\"DurationSeconds\": \"`60`\", \"InstallDependencies\": \"`True`\", \"CPU\": \"`0`\"}"
            },
            "targets": {
                "Instances": "myInstance"
            }
        }
    },
    "stopConditions": [
        {
            "source": "aws:cloudwatch:alarm",
            "value": "arn:aws:cloudwatch:`us-east-1`:`111122223333`:alarm:`alarm-name`"
        }
    ],
    "roleArn": "arn:aws:iam::`111122223333`:role/`role-name`"
}
```

## Run a predefined Automation runbook

The following example publishes a notification to Amazon SNS using a runbook provided by Systems Manager,
[AWS-PublishSNSNotification](../../../systems-manager-automation-runbooks/latest/userguide/automation-aws-publishsnsnotification.md "../../../systems-manager-automation-runbooks/latest/userguide/automation-aws-publishsnsnotification.md"). The role must have permissions to publish notifications to the
specified SNS topic.

```
{
    "description": "Publish event through SNS",
    "stopConditions": [
        {
            "source": "none"
        }
    ],
    "targets": {
    },
    "actions": {
        "sendToSns": {
            "actionId": "aws:ssm:start-automation-execution",
            "description": "Publish message to SNS",
            "parameters": {
                "documentArn": "arn:aws:ssm:`us-east-1`::document/AWS-PublishSNSNotification",
                "documentParameters": "{\"Message\": \"`Hello, world`\", \"TopicArn\": \"arn:aws:sns:`us-east-1`:`111122223333`:`topic-name`\"}",
                "maxDuration": "`PT1M`"
            },
            "targets": {
            }
        }
    },
    "roleArn": "arn:aws:iam::`111122223333`:role/`role-name`"
}
```

## Throttle API actions on EC2 instances with the target IAM role

The following example throttles 100% of the API calls specified in the action definition for API calls made by the IAM role(s) specified in the target definition.

###### Note

If you wish to target EC2 instances that are members of an Auto Scaling group, please use the **aws:ec2:asg-insufficient-instance-capacity-error** action, and target by Auto Scaling group instead. For more information, see [aws:ec2:asg-insufficient-instance-capacity-error](fis-actions-reference.md#asg-ice "fis-actions-reference.md#asg-ice").

```
{
    "tags": {
        "Name": "ThrottleEC2APIActions"
    },
    "description": "Throttle the specified EC2 API actions on the specified IAM role",
    "targets": {
        "myRole": {
            "resourceType": "aws:iam:role",
            "resourceArns": ["arn:aws:iam::`111122223333`:role/`role-name`"],
            "selectionMode": "`ALL`"
        }
    },
    "actions": {
        "ThrottleAPI": {
            "actionId": "aws:fis:inject-api-throttle-error",
            "description": "Throttle APIs for 5 minutes",
            "parameters": {
                "service": "ec2",
                "operations": "`DescribeInstances,DescribeVolumes`",
                "percentage": "`100`",
                "duration": "`PT2M`"
            },
            "targets": {
                "Roles": "myRole"
            }
        }
    },
    "stopConditions": [
        {
            "source": "aws:cloudwatch:alarm",
            "value": "arn:aws:cloudwatch:`us-east-1`:`111122223333`:alarm:`alarm-name`"
        }
    ],
    "roleArn": "arn:aws:iam::`111122223333`:role/`role-name`"
}
```

## Stress test CPU of pods in a Kubernetes cluster

The following example uses Chaos Mesh to stress test the CPU of pods in an Amazon EKS Kubernetes cluster for one minute.

```
{
    "description": "ChaosMesh StressChaos example",
    "targets": {
        "Cluster-Target-1": {
            "resourceType": "aws:eks:cluster",
            "resourceArns": [
                "arn:aws:eks:arn:aws::`111122223333`:cluster/`cluster-id`"
            ],
            "selectionMode": "`ALL`"
        }
    },
    "actions": {
        "TestCPUStress": {
            "actionId": "aws:eks:inject-kubernetes-custom-resource",
            "parameters": {
                "maxDuration": "`PT2M`",
                "kubernetesApiVersion": "chaos-mesh.org/v1alpha1",
                "kubernetesKind": "StressChaos",
                "kubernetesNamespace": "default",
                "kubernetesSpec": "{\"selector\":{\"namespaces\":[\"default\"],\"labelSelectors\":{\"run\":\"nginx\"}},\"mode\":\"all\",\"stressors\": {\"cpu\":{\"workers\":1,\"load\":50}},\"duration\":\"1m\"}"
            },
            "targets": {
                "Cluster": "Cluster-Target-1"
            }
        }
    },
    "stopConditions": [{
        "source": "none"
    }],
    "roleArn": "arn:aws:iam::`111122223333`:role/`role-name`",
    "tags": {}
}
```

The following example uses Litmus to stress test the CPU of pods in an Amazon EKS Kubernetes cluster for one minute.

```
{
    "description": "Litmus CPU Hog",
    "targets": {
        "MyCluster": {
            "resourceType": "aws:eks:cluster",
            "resourceArns": [
                "arn:aws:eks:arn:aws::`111122223333`:cluster/`cluster-id`"
            ],
            "selectionMode": "`ALL`"
        }
    },
    "actions": {
        "MyAction": {
            "actionId": "aws:eks:inject-kubernetes-custom-resource",
            "parameters": {
                "maxDuration": "`PT2M`",
                "kubernetesApiVersion": "litmuschaos.io/v1alpha1",
                "kubernetesKind": "ChaosEngine",
                "kubernetesNamespace": "litmus",
                "kubernetesSpec": "{\"engineState\":\"active\",\"appinfo\":{\"appns\":\"default\",\"applabel\":\"run=nginx\",\"appkind\":\"deployment\"},\"chaosServiceAccount\":\"litmus-admin\",\"experiments\":[{\"name\":\"pod-cpu-hog\",\"spec\":{\"components\":{\"env\":[{\"name\":\"TOTAL_CHAOS_DURATION\",\"value\":\"60\"},{\"name\":\"CPU_CORES\",\"value\":\"1\"},{\"name\":\"PODS_AFFECTED_PERC\",\"value\":\"100\"},{\"name\":\"CONTAINER_RUNTIME\",\"value\":\"docker\"},{\"name\":\"SOCKET_PATH\",\"value\":\"/var/run/docker.sock\"}]},\"probe\":[]}}],\"annotationCheck\":\"false\"}"
            },
            "targets": {
                "Cluster": "MyCluster"
            }
        }
    },
    "stopConditions": [{
        "source": "none"
    }],
    "roleArn": "arn:aws:iam::`111122223333`:role/`role-name`",
    "tags": {}
}
```

## Provisioned throughput exception for specified number of Kinesis Data Streams

The following example throws a provisioned throughput exception for 100% of requests up to five Kinesis Data Streams with the specified tag. AWS FIS selects the streams to affect at random. After 5 minutes the fault is removed.

```
{
    "description": "Kinesis stream experiment",
    "targets": {
        "KinesisStreams-Target-1": {
            "resourceType": "aws:kinesis:stream",
            "resourceTags": {
                   "tag-key": "tag-value"
            },
            "selectionMode": "COUNT(5)"
        }
    },
    "actions": {
         "kinesis": {
              "actionId": "aws:kinesis:stream-provisioned-throughput-exception",
              "description": "my-stream",
              "parameters": {
                   "duration": "PT5M",
                   "percentage": "100",
                   "service": "kinesis"
              },
              "targets": {
                    "KinesisStreams": "KinesisStreams-Target-1"
              }
         }
   },
   "stopConditions": [
         {
              "source": "none"
         }
   ],
   "roleArn": "arn:aws:iam::111122223333:role/role-name",
   "tags": {},
   "experimentOptions": {
       "accountTargeting": "single-account",
       "emptyTargetResolutionMode": "fail"
   }
}
```

## Experiment role permissions example

The following permission allows you to run the
`aws:kinesis:stream-provisioned-throughput-exception` and
`aws:kinesis:stream-expired-iterator-exception` actions on a specific
stream impacting 50% of requests.

```
{
    "Version": "2012-10-17",
     "Statement": [
        {
            "Effect": "Allow",
            "Action": "kinesis:InjectApiError",
            "Resource": "*"
            "Condition": {
                "ForAllValues:StringEquals": {
                    "kinesis:FisActionId": [
                        "aws:kinesis:stream-provisioned-throughput-exception",
                        "aws:kinesis:stream-expired-iterator-exception"
                    ],
                    "kinesis:FisTargetArns": [
                        "arn:aws:kinesis:us-east-1:111122223333:stream/stream-name"
                    ],
                },
                "NumericEquals": {
                    "kinesis:FisInjectPercentage": "50"
                }
            }
        },
        {
             "Action": [
                   "kinesis:DescribeStreamSummary",
              ],
             "Resource": "*",
             "Effect": "Allow"
        }
    ]
}
```
