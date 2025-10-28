#

Examples of using ARC readiness check API operations with the AWS CLI

This section walks through simple application examples, using the AWS Command Line Interface to work with readiness check
features in Amazon Application Recovery Controller (ARC) using API operations. The examples are intended to help you develop a basic
understanding of how to work with readiness check capabilities using the CLI.

Readiness check in ARC audits for mismatches for the resources in your application replicas. To set up readiness checks
for your application, you must set up—or model—your application resources in ARC _cells_ that
align with the replicas that you've created for your application. You then set up readiness checks that audit these replicas, to
help you make sure that your standby application replica and its resources match your production replica, on an ongoing basis

Let’s look at a simple case where you have an application named Simple-Service that
currently runs in the US East (N. Virginia) Region (us-east-1). You also have a standby copy of the
application in the US West (Oregon) Region (us-west-2). In this example, we'll configure
readiness checks to compare these two versions of the application. This lets us ensure
that the standby, US West (Oregon) Region, is ready to receive traffic, if it needs to in a failover
scenario.

For more information about using the AWS CLI, see the
[AWS CLI Command Reference](../../../cli/latest/reference/route53-recovery-readiness/index.md "../../../cli/latest/reference/route53-recovery-readiness/index.md").
For a list of readiness API actions and links to more information, see [Readiness check API operations](actions.md "actions.md").

_Cells_ in ARC represent fault boundaries (like Availability Zones or Regions) and are collected
into _recovery groups_. A recovery group represents an application that you want to check
failover readiness for. For more information about the components of readiness check, see
[Readiness check components](introduction-components-readiness.md "introduction-components-readiness.md") .

###### Note

ARC is a global service that supports endpoints in multiple AWS Regions but you must
specify the US West (Oregon) Region (that is, specify the parameter `--region us-west-2`)
in most ARC CLI commands. For example, to create resources such as recovery groups or readiness checks.

For our application example, we'll start by creating one cell for each Region where we have resources. Then we'll
create a recovery group, and then complete the setup for a readiness check.

##

1.  Create cells

1a. Create a us-east-1 cell.

```
aws route53-recovery-readiness --region us-west-2 create-cell \
				--cell-name east-cell
```

```
{
    "CellArn": "arn:aws:route53-recovery-readiness::111122223333:cell/east-cell",
    "CellName": "east-cell",
    "Cells": [],
    "ParentReadinessScopes": [],
    "Tags": {}
}
```

1b. Create a us-west-1 cell.

```
aws route53-recovery-readiness --region us-west-2 create-cell \
				--cell-name west-cell
```

```
{
    "CellArn": "arn:aws:route53-recovery-readiness::111122223333:cell/west-cell",
    "CellName": "west-cell",
    "Cells": [],
    "ParentReadinessScopes": [],
    "Tags": {}
}
```

1c. Now we have two cells. You can verify that they exist by calling the `list-cells` API.

```
aws route53-recovery-readiness --region us-west-2 list-cells
```

```
{
    "Cells": [
        {
            "CellArn": "arn:aws:route53-recovery-readiness::111122223333:cell/east-cell",
            "CellName": "east-cell",
            "Cells": [],
            "ParentReadinessScopes": [],
            "Tags": {}
        },
        {
            "CellArn": "arn:aws:route53-recovery-readiness::111122223333:cell/west-cell",
            "CellName": "west-cell"
            "Cells": [],
            "ParentReadinessScopes": [],
            "Tags": {}
        }
    ]
}
```

##

2.  Create a recovery group

Recovery groups are the top-level resource for recovery readiness in ARC. A recovery group represents an application
as a whole. In this step, we'll create a recovery group to model an overall application, and then add the two cells
that we created.

2a. Create a recovery group.

```
aws route53-recovery-readiness --region us-west-2 create-recovery-group \
				--recovery-group-name simple-service-recovery-group \
			    --cells "arn:aws:route53-recovery-readiness::111122223333:cell/east-cell"\
			    "arn:aws:route53-recovery-readiness::111122223333:cell/west-cell"
```

```
{
    "Cells": [],
    "RecoveryGroupArn": "arn:aws:route53-recovery-readiness::111122223333:recovery-group/simple-service-recovery-group",
    "RecoveryGroupName": "simple-service-recovery-group",
    "Tags": {}
}
```

2b. (Optional) You can verify that your recovery group was created correctly by calling the
`list-recovery-groups` API.

```
aws route53-recovery-readiness --region us-west-2 list-recovery-groups
```

```
{
    "RecoveryGroups": [
        {
            "Cells": [
                "arn:aws:route53-recovery-readiness::111122223333:cell/east-cell",
                "arn:aws:route53-recovery-readiness::111122223333:cell/west-cell"
            ],
            "RecoveryGroupArn": "arn:aws:route53-recovery-readiness::111122223333:recovery-group/simple-service-recovery-group",
            "RecoveryGroupName": "simple-service-recovery-group",
            "Tags": {}
        }
    ]
}
```

Now that we have a model for our application, let’s add the resources to be monitored. In ARC, a
group of resources that you want to monitor is called a resource set. Resource sets contain resources that are
all of the same type. We compare the resources in a resource set to each other to help determine a cell's readiness
for failover.

##

3.  Create a resource set

Let’s assume our Simple-Service application is indeed very simple and only uses DynamoDB tables. It has a DynamoDB
table in us-east-1 and another one in us-west-2. A resource set also contains a readiness scope, which identifies the
cell that each resource is contained in.

3a. Create a resource set that reflects our Simple-Service application's resources.

```
aws route53-recovery-readiness --region us-west-2 create-resource-set \
				--resource-set-name ImportantInformationTables \
				--resource-set-type AWS::DynamoDB::Table \
				--resources
				ResourceArn="arn:aws:dynamodb:us-west-2:111122223333:table/TableInUsWest2",ReadinessScopes="arn:aws:route53-recovery-readiness::111122223333:cell/west-cell"
				ResourceArn="arn:aws:dynamodb:us-west-2:111122223333:table/TableInUsEast1",ReadinessScopes="arn:aws:route53-recovery-readiness::111122223333:cell/east-cell"

```

```
{
    "ResourceSetArn": "arn:aws:route53-recovery-readiness::111122223333:resource-set/sample-resource-set",
    "ResourceSetName": "ImportantInformationTables",
    "Resources": [
        {
            "ReadinessScopes": [
                "arn:aws:route53-recovery-readiness::111122223333:cell/west-cell"
            ],
            "ResourceArn": "arn:aws:dynamodb:us-west-2:111122223333:table/TableInUsWest2"
        },
        {
            "ReadinessScopes": [
                "arn:aws:route53-recovery-readiness::111122223333:cell/east-cell"
            ],
            "ResourceArn": "arn:aws:dynamodb:us-west-2:111122223333:table/TableInUsEast1"
        }
    ],
    "Tags": {}
}
```

3b. (Optional) You can verify what's included in the resource set by calling the `list-resource-sets` API. This
lists all the resource sets for an AWS account. Here you can see that we have just the one resource set that we created above.

```
aws route53-recovery-readiness --region us-west-2 list-resource-sets
```

```
{
    "ResourceSets": [
        {
            "ResourceSetArn": "arn:aws:route53-recovery-readiness::111122223333:resource-set/ImportantInformationTables",
            "ResourceSetName": "ImportantInformationTables",
            "Resources": [
                {
                    "ReadinessScopes": [
                        "arn:aws:route53-recovery-readiness::111122223333:cell/west-cell"
                    ],
                    "ResourceArn": "arn:aws:dynamodb:us-west-2:111122223333:table/TableInUsWest2"
                },
                {
                    "ReadinessScopes": [
                        "arn:aws:route53-recovery-readiness::111122223333:cell/east-cell"
                    ],
                    "ResourceArn": "arn:aws:dynamodb:us-west-2:111122223333:table/TableInUsEast1"
                }
            ],
            "Tags": {}
        }
    ]
}{
    "ResourceSets": [
        {
            "ResourceSetArn": "arn:aws:route53-recovery-readiness::111122223333:resource-set/ImportantInformationTables",
            "ResourceSetName": "ImportantInformationTables",
            "Resources": [
                {
                    "ReadinessScopes": [
                        "arn:aws:route53-recovery-readiness::111122223333:cell/west-cell"
                    ],
                    "ResourceArn": "arn:aws:dynamodb:us-west-2:111122223333:table/TableInUsWest2"
                },
                {
                    "ReadinessScopes": [
                        "arn:aws:route53-recovery-readiness::&ExampleAWSAccountNo1;:cell/east-cell"
                    ],
                    "ResourceArn": "arn:aws:dynamodb:us-west-2:111122223333:table/TableInUsEast1"
                }
            ],
            "Tags": {}
        }
    ]
}
```

Now we’ve created the cells, recovery group, and resource set to model the Simple-Service application in ARC.
Next, we'll set up readiness checks to monitor the readiness of the resources for fail over.

##

4.  Create a readiness check

A readiness check applies a set of rules to each resource in the resource set that is attached to the check.
Rules are specific to each resource type. That is, there are different rules for `AWS::DynamoDB::Table`,
`AWS::EC2::Instance`,
and so on. Rules check a variety of dimensions for a resource, including configuration, capacity (where available and applicable),
limits (where available and applicable), and routing configurations.

###### Note

To see the rules that are applied to a resource in a readiness check, you can use the
`get-readiness-check-resource-status` API, as described in step 5. To see a list of
all the readiness rules in ARC, use
`list-rules` or see [Readiness rules descriptions in ARC](recovery-readiness.md "recovery-readiness.md").
ARC has a specific set of rules that it runs for each resource type; they're not customizable at this time.

4a. Create a readiness check for the resource set, ImportantInformationTables.

```
aws route53-recovery-readiness --region us-west-2 create-readiness-check \
				--readiness-check-name ImportantInformationTableCheck --resource-set-name ImportantInformationTables
```

```
{
    "ReadinessCheckArn": "arn:aws:route53-recovery-readiness::111122223333:readiness-check/ImportantInformationTableCheck",
    "ReadinessCheckName": "ImportantInformationTableCheck",
    "ResourceSet": "ImportantInformationTables",
    "Tags": {}
}
```

4b. (Optional) To verify that the readiness check was created successfully, run the `list-readiness-checks`
API. This API shows all the readiness checks in an account.

```
aws route53-recovery-readiness --region us-west-2 list-readiness-checks
```

```
{
    "ReadinessChecks": [
        {
            "ReadinessCheckArn": "arn:aws:route53-recovery-readiness::111122223333:readiness-check/ImportantInformationTableCheck",
            "ReadinessCheckName": "ImportantInformationTableCheck",
            "ResourceSet": "ImportantInformationTables",
            "Tags": {}
        }
    ]
}
```

##

5.  Monitor readiness checks

Now that we’ve modeled the application and added a readiness check, we’re ready to monitor
resources. You can model the readiness of your application at four levels: the
readiness check level (a group of resources), the individual resource level, the
cell level (all the resources in an Availability Zone or Region), and the recovery
group level (the application as a whole). Commands for getting each of these types
of readiness statuses are provided below.

5a. See the status of your readiness check.

```
aws route53-recovery-readiness --region us-west-2 get-readiness-check-status\
				--readiness-check-name ImportantInformationTableCheck
```

```
{
    "Readiness": "READY",
    "Resources": [
        {
            "LastCheckedTimestamp": "2021-01-07T00:53:39Z",
            "Readiness": "READY",
            "ResourceArn": "arn:aws:dynamodb:us-west-2:111122223333:table/TableInUsWest2"
        },
        {
            "LastCheckedTimestamp": "2021-01-07T00:53:39Z",
            "Readiness": "READY",
            "ResourceArn": "arn:aws:dynamodb:us-west-2:111122223333:table/TableInUsEast2"
    ]
}
```

5b. See the detailed readiness status of a single resource in a readiness check, including the status of each
rule that is checked.

```
aws route53-recovery-readiness --region us-west-2 get-readiness-check-resource-status \
				--readiness-check-name ImportantInformationTableCheck \
				--resource-identifier "arn:aws:dynamodb:us-west-2:111122223333:table/TableInUsWest2"
```

```
{"Readiness": "READY",
    "Rules": [
        {
            "LastCheckedTimestamp": "2021-01-07T00:55:41Z",
            "Messages": [],
            "Readiness": "READY",
            "RuleId": "DynamoTableStatus"
        },
        {
            "LastCheckedTimestamp": "2021-01-07T00:55:41Z",
            "Messages": [],
            "Readiness": "READY",
            "RuleId": "DynamoCapacity"
        },
        {
            "LastCheckedTimestamp": "2021-01-07T00:55:41Z",
            "Messages": [],
            "Readiness": "READY",
            "RuleId": "DynamoPeakRcuWcu"
        },
        {
            "LastCheckedTimestamp": "2021-01-07T00:55:41Z",
            "Messages": [],
            "Readiness": "READY",
            "RuleId": "DynamoGSIsPeakRcuWcu"
        },
        {
            "LastCheckedTimestamp": "2021-01-07T00:55:41Z",
            "Messages": [],
            "Readiness": "READY",
            "RuleId": "DynamoGSIsConfig"
        },
        {
            "LastCheckedTimestamp": "2021-01-07T00:55:41Z",
            "Messages": [],
            "Readiness": "READY",
            "RuleId": "DynamoGSIsStatus"
        },
        {
            "LastCheckedTimestamp": "2021-01-07T00:55:41Z",
            "Messages": [],
            "Readiness": "READY",
            "RuleId": "DynamoGSIsCapacity"
        },
        {
            "LastCheckedTimestamp": "2021-01-07T00:55:41Z",
            "Messages": [],
            "Readiness": "READY",
            "RuleId": "DynamoReplicationLatency"
        },
        {
            "LastCheckedTimestamp": "2021-01-07T00:55:41Z",
            "Messages": [],
            "Readiness": "READY",
            "RuleId": "DynamoAutoScalingConfiguration"
        },
        {
            "LastCheckedTimestamp": "2021-01-07T00:55:41Z",
            "Messages": [],
            "Readiness": "READY",
            "RuleId": "DynamoLimits"
        }
    ]
}
```

5c. See the overall readiness for a cell.

```
aws route53-recovery-readiness --region us-west-2 get-cell-readiness-summary \
				--cell-name west-cell
```

```
{
    "Readiness": "READY",
    "ReadinessChecks": [
        {
            "Readiness": "READY",
            "ReadinessCheckName": "ImportantTableCheck"
        }
    ]
}
```

5d. Finally, see the top-level readiness of your application, at the recovery group level.

```
aws route53-recovery-readiness --region us-west-2 get-recovery-group-readiness-summary \
				--recovery-group-name simple-service-recovery-group
```

```
{
    "Readiness": "READY",
    "ReadinessChecks": [
        {
            "Readiness": "READY",
            "ReadinessCheckName": "ImportantTableCheck"
        }
    ]
}
```
