# Actions for AWS FIS

To create an experiment template, you must define one or more actions. For a list of predefined actions provided by AWS FIS, see [Actions reference](fis-actions-reference.md "fis-actions-reference.md").

You can run an action only once during an experiment. To run the same AWS FIS action
more than once in the same experiment, add it to the template multiple times using
different names.

###### Contents

- [Action syntax](#action-syntax "#action-syntax")
- [Action identifiers](#action-identifiers "#action-identifiers")
- [Action parameters](#action-parameters "#action-parameters")
- [Action targets](#action-targets "#action-targets")
- [Action duration](#action-duration "#action-duration")
- [Example actions](#example-actions "#example-actions")

## Action syntax

The following is the syntax for an action.

```
{
    "actions": {
        "`action_name`": {
            "actionId": "aws:`service`:`action-type`",
            "description": "`string`",
            "parameters": {
                "`name`": "`value`"
             },
            "startAfter": ["`action_name`", ...],
            "targets": {
                "`ResourceType`": "`target_name`"
            }
        }
    }
}
```

When you define an action, you provide the following:

**`action_name`**

A name for the action.

**actionId**

The [action identifier](#action-identifiers "#action-identifiers").

**description**

An optional description.

**parameters**

Any [action parameters](#action-parameters "#action-parameters").

**startAfter**

Any actions that must complete before this action can start. Otherwise, the
action runs at the start of the experiment.

**targets**

Any [action targets](#action-targets "#action-targets").

For examples, see [Example actions](#example-actions "#example-actions").

## Action identifiers

Each AWS FIS action has an identifier with the following format:

```
aws:`service-name`:`action-type`
```

For example, the following action stops the target Amazon EC2 instances:

```
aws:ec2:stop-instances
```

For a complete list of actions, see the [AWS FIS Actions reference](fis-actions-reference.md "fis-actions-reference.md").

## Action parameters

Some AWS FIS actions have additional parameters that are specific to the action.
These parameters are used to pass information to AWS FIS when the action is run.

AWS FIS supports custom fault types using the `aws:ssm:send-command` action,
which uses the SSM Agent and an SSM command document to create the fault condition
on the targeted instances. The `aws:ssm:send-command` action includes a
`documentArn` parameter that takes the Amazon Resource Name (ARN) of an SSM
document as a value. You specify values for parameters when you add the action to your
experiment template.

For more information about specifying parameters for the
`aws:ssm:send-command` action, see [Use the aws:ssm:send-command
action](actions-ssm-agent.md#specifying-ssm-actions "actions-ssm-agent.md#specifying-ssm-actions").

Where possible, you can input a rollback configuration (also referred to as a
_post action_) within the action parameters. A post action
returns the target to the state that it was in before the action was run. The post
action runs after the time specified in the action duration. Not all actions can support
post actions. For example, if the action terminates an Amazon EC2 instance, you cannot
recover the instance after it has been terminated.

## Action targets

An action runs on the target resources that you specify. After you define a target,
you can specify its name when you define an action.

```
"targets": {
    "`ResourceType`": "`resource_name`"
}
```

AWS FIS actions support the following resource types for action targets:

- **AutoScalingGroups** – Amazon EC2 Auto Scaling groups
- **Buckets** – Amazon S3 buckets
- **Cluster** – Amazon EKS clusters
- **Clusters** – Amazon ECS, Aurora DSQL, or Amazon Aurora DB clusters
- **DBInstances** – Amazon RDS DB instances
- **Functions** – AWS Lambda functions
- **Instances** – Amazon EC2 instances
- **ManagedResources** – Amazon EKS clusters, Amazon EC2 Application and Network Load Balancers, and Amazon EC2 Auto Scaling
  groups that are enabled for ARC zonal shift.
- **MultiRegionClusters** – Amazon MemoryDB multi-Region clusters
- **Nodegroups** – Amazon EKS node groups
- **Pods** – Kubernetes pods on Amazon EKS
- **ReplicationGroups** – ElastiCache Replication Groups
- **Roles** – IAM roles
- **SpotInstances** – Amazon EC2 Spot Instances
- **Subnets** – VPC subnets
- **Tables** – Amazon DynamoDB multi-Region eventually consistent global tables
- **Tasks** – Amazon ECS tasks
- **TransitGateways** – Transit gateways
- **Volumes** – Amazon EBS volumes

For examples, see [Example actions](#example-actions "#example-actions").

## Action duration

If an action includes a parameter that you can use to specify the duration of the
action, by default, the action is considered complete only after the specified duration has elapsed.
If you have set the `emptyTargetResolutionMode` experiment option to `skip`, then
the action will complete immediately with status 'skipped' when no targets were resolved.
For example, if you specify a duration of 5 minutes, AWS FIS considers the action complete
after 5 minutes. It then starts the next action, until all actions are complete.

Duration can be either the length of time that an action condition is maintained
or the length of time for which metrics are monitored. For example, latency is injected
for the duration of time specified. For near instantaneous action types, such as
terminating an instance, stop conditions are monitored for the duration of time
specified.

If an action includes a post action within the action parameters, the post action runs
after the action completes. The time it takes to complete the post action might cause a
delay between the specified action duration and the beginning of the next action (or the
end of the experiment, if all other actions are complete).

## Example actions

The following are example actions.

###### Examples

- [Stop EC2 instances](#example-action-stop-instances "#example-action-stop-instances")
- [Interrupt Spot Instances](#example-action-send-spot-instance-interupptions "#example-action-send-spot-instance-interupptions")
- [Disrupt network traffic](#example-action-disrupt-connectivity "#example-action-disrupt-connectivity")
- [Terminate EKS workers](#example-action-terminate-nodegroup-instances "#example-action-terminate-nodegroup-instances")
- [Start ARC zonal autoshift](#example-start-arc-zonal-autoshift "#example-start-arc-zonal-autoshift")

###### Example: Stop EC2 instances

The following action stops the EC2 instances identified using the
target named `targetInstances`. After two
minutes, it restarts the target instances.

```
"actions": {
    "`stopInstances`": {
        "actionId": "aws:ec2:stop-instances",
        "parameters": {
            "startInstancesAfterDuration": "`PT2M`"
        },
        "targets": {
            "Instances": "`targetInstances`"
        }
    }
}
```

###### Example: Interrupt Spot Instances

The following action stops the Spot Instances identified using the
target named `targetSpotInstances`. It waits
two minutes before interrupting the Spot Instance.

```
"actions": {
    "`interruptSpotInstances`": {
        "actionId": "aws:ec2:send-spot-instance-interruptions",
        "parameters": {
            "durationBeforeInterruption": "`PT2M`"
        },
        "targets": {
            "SpotInstances": "`targetSpotInstances`"
        }
    }
}
```

###### Example: Disrupt network traffic

The following action denies traffic between the target subnets and subnets in
other Availability Zones.

```
"actions": {
    "`disruptAZConnectivity`": {
        "actionId": "aws:network:disrupt-connectivity",
        "parameters": {
            "scope": "availability-zone",
            "duration": "`PT5M`"
        },
        "targets": {
            "Subnets": "`targetSubnets`"
        }
    }
}
```

###### Example: Terminate EKS workers

The following action terminates 50% of the EC2 instances in the
EKS cluster identified using the target named
`targetNodeGroups`.

```
"actions": {
    "`terminateWorkers`": {
        "actionId": "aws:eks:terminate-nodegroup-instances",
        "parameters": {
            "instanceTerminationPercentage": "`50`"
        },
        "targets": {
            "Nodegroups": "`targetNodeGroups`"
        }
    }
}
```

###### Example: Start ARC zonal autoshift

The following action starts an ARC Zonal autoshift that shifts managed resources away from `az-in-parameters` for `duration-in-parameteres`. The resource type `ManagedResources` is used as a key for the target name in AWS FIS experiment template.

```
{
    "description": "aaa",
    "targets": {
        "ManagedResources-Target-1": {
            "resourceType": "aws:arc:zonal-shift-managed-resource",
            "resourceArns": [
                "arn:aws:elasticloadbalancing:us-east-1:0124567890:loadbalancer/app/application/11223312312516",
            ],
            "selectionMode": "ALL"
        }
    },
    "actions": {
        "arc": {
            "actionId": "aws:arc:start-zonal-autoshift",
            "parameters": {
                "availabilityZoneIdentifier": "us-east-1a",
                "duration": "PT1M"
            },
            "targets": {
               "ManagedResources": "ManagedResources-Target-1"
            }
        }
    },
    "stopConditions": [
        {
            "source": "none"
        }
    ],
    "roleArn": "arn:aws:iam::718579638765:role/fis",
    "tags": {},
    "experimentOptions": {
        "accountTargeting": "single-account",
        "emptyTargetResolutionMode": "fail"
    }
}
```
