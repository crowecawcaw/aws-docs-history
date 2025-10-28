# Change sets for nested stacks

With _change sets for nested stacks_ you can preview the changes to
your application and infrastructure resources across the entire nested stack hierarchy and
proceed with updates when you've confirmed that all the changes are as intended.

See the following sections for more details about change sets for nested stacks:

###### Topics

- [Overview of change sets and
  nested stacks](#overview-of-change-sets-and-nested-stacks "#overview-of-change-sets-and-nested-stacks")
- [Working with change sets for
  nested stacks (console)](#change-sets-for-nested-stacks-console "#change-sets-for-nested-stacks-console")
- [Working with change sets for nested
  stacks (AWS CLI)](#change-sets-for-nested-stacks-cli "#change-sets-for-nested-stacks-cli")

## Overview of change sets and

nested stacks

Change sets for nested stacks combines the following features together to expand
the scope of previewing changes to the entire stack hierarchy:

- A _change set_ is a CloudFormation capability that offers a
  preview of how proposed changes to a stack will impact existing or newly created
  resources. Upon creating a change set, CloudFormation provides a list of proposed
  changes by comparing your stack with the changes to the resources you submitted.
  For more information about change sets, see [Update CloudFormation stacks using change
  sets](using-cfn-updating-stacks-changesets.md "using-cfn-updating-stacks-changesets.md").
- A _nested stack_ is stack created as part of another stack.
  For example, you might have networking and security related resources in one
  nested stack and application resources in another. Partitioning application
  models this way helps with code maintainability and reuse. For more information
  about nested stacks, see [Split a template into reusable pieces using nested
  stacks](using-cfn-nested-stacks.md "using-cfn-nested-stacks.md").

## Working with change sets for

nested stacks (console)

- **Create a change set** – Creates a change
  set by submitting changes from any level of the stack hierarchy. You can submit
  a modified stack template or modified input parameter values and CloudFormation
  compares your nested stack with the changes that you submitted to generate a
  change set. Change sets for nested stacks is enabled by default in the
  CloudFormation console. For more information, see [Create a change set for a CloudFormation stack](using-cfn-updating-stacks-changesets-create.md "using-cfn-updating-stacks-changesets-create.md").

![Create a change set for nested stacks is Enabled by default.](images/change-sets-for-nested-sets-enabled-default.png)

###### Note

A root change set is the change set associated with the stack from which
the whole hierarchy of change sets are created. You must execute or delete
change sets for nested stacks from the root change set. For more
information, see [Performing stack operations
on nested stacks](using-cfn-nested-stacks.md#perform-stack-operations-on-nested-stacks "using-cfn-nested-stacks.md#perform-stack-operations-on-nested-stacks").

- **View the change set** – Visualize
  changes to resources inside nested stacks before executing them. You can view
  the proposed changes in the **Changes** section of your change
  set by navigating through the current stack and its nested change sets. For more
  information, see [View a change set for a CloudFormation stack](using-cfn-updating-stacks-changesets-view.md "using-cfn-updating-stacks-changesets-view.md").
- **Execute the change set** – Execute the
  changes described in the change set that pertain to the current stack and its
  descendants. The execute operation must be made from the root change set. For
  more information, see [Execute a change set for a CloudFormation stack](using-cfn-updating-stacks-changesets-execute.md "using-cfn-updating-stacks-changesets-execute.md").
- **Delete the change set** – Removes the
  change sets from the current stack. Deleting a change set helps to prevent you
  or another user from accidentally initiating a change set that shouldn't be
  applied. The delete operation must be executed from the root change set. For
  more information, see [Delete a change set for a CloudFormation stack](using-cfn-updating-stacks-changesets-delete.md "using-cfn-updating-stacks-changesets-delete.md").

## Working with change sets for nested

stacks (AWS CLI)

- [create-change-set](../../../cli/latest/reference/cloudformation/create-change-set.md "../../../cli/latest/reference/cloudformation/create-change-set.md") – Change sets
  for nested stacks isn't enabled by default for the AWS CLI. To create a
  change set for the entire stack hierarchy, specify the
  `--include-nested-stacks` option. For more information,
  see [Create a change set for a CloudFormation stack](using-cfn-updating-stacks-changesets-create.md "using-cfn-updating-stacks-changesets-create.md").
  The following AWS CLI example creates a change set for the specified root
  stack.

```
aws cloudformation create-change-set \
    --stack-name `my-root-stack` \
    --change-set-name `my-root-stack-change-set` \
    --template-body `file://template.yaml` \
    --capabilities CAPABILITY_IAM \
    --include-nested-stacks
```

The following is example output.

```
{
    "Id":"arn:aws:cloudformation:us-west-2:123456789012:changeSet/`my-root-stack-change-set`/4eca1a01-e285-xmpl-8026-9a1967bfb4b0",
    "StackId": "arn:aws:cloudformation:us-west-2:123456789012:Stack/`my-root-stack`/d0a825a0-e4cd-xmpl-b9fb-061c69e99204"
}
```

- [describe-change-set](../../../cli/latest/reference/cloudformation/describe-change-set.md "../../../cli/latest/reference/cloudformation/describe-change-set.md") – Returns a
  list of changes that CloudFormation will make if you execute the change set.
  If the change set specified contains child change sets that belong to
  nested stacks, then `ChangeSetId` will return information
  about that change set. For more information, see [View a change set for a CloudFormation stack](using-cfn-updating-stacks-changesets-view.md "using-cfn-updating-stacks-changesets-view.md").
  The following AWS CLI example describes the change set for the specified root
  stack.

```
aws cloudformation describe-change-set \
    --change-set-name `my-root-stack-change-set` \
    --stack-name `my-root-stack`
```

The following is example output.

```
{
    "Changes": [
        {
            "Type": "Resource",
            "ResourceChange": {
                "Action": "Modify",
                "LogicalResourceId": "ChildStack",
                "PhysicalResourceId": "arn:aws:cloudformation:us-west-2:123456789012:stack/`my-nested-stack`/d0a825a0-e4cd-xmpl-b9fb-061c69e99205",
                "ResourceType": "AWS::CloudFormation::Stack",
                "Replacement": "False",
                "ChangeSetId": "arn:aws:cloudformation:us-west-2:123456789012:changeSet/`my-nested-stack-change-set`/4eca1a01-e285-xmpl-8026-9a1967bfb4b0",
                "Scope": [
                    "Properties"
                ],
                "Details": [
                    {
                        "Target": {
                            "Attribute": "Properties",
                            "RequiresRecreation": "Never"
                        },
                        "Evaluation": "Dynamic",
                        "ChangeSource": "Automatic"
                    }
                ]
            }
        }
    ],
    "ChangeSetName": "`my-root-stack-change-set`",
    "ChangeSetId": "arn:aws:cloudformation:us-west-2:123456789012:changeSet/`my-root-stack-change-set`/4eca1a01-e285-xmpl-8026-9a1967bfb4b0",
    "StackId": "arn:aws:cloudformation:us-west-2:123456789012:stack/`my-root-stack`/d0a825a0-e4cd-xmpl-b9fb-061c69e99204",
    "StackName": "`my-root-stack`",
    "IncludeNestedStacks": true,
    "ParentChangeSetId": null,
    "RootChangeSetId": null,
    "Description": null,
    "Parameters": null,
    "CreationTime": "2020-11-18T05:20:56.651Z",
    "ExecutionStatus": "AVAILABLE",
    "Status": "CREATE_COMPLETE",
    "StatusReason": null,
    "NotificationARNs": [

    ],
    "RollbackConfiguration": {

    },
    "Capabilities": [
        "CAPABILITY_IAM"
    ],
    "Tags": null
}
```

The following AWS CLI example describes the change set for the specified nested
stack.

```
aws cloudformation describe-change-set \
    --change-set-name `my-nested-stack-change-set` \
    --stack-name `my-nested-stack`
```

The following is example output.

```
{
    "Changes": [
        {
            "Type": "Resource",
            "ResourceChange": {
                "Action": "Modify",
                "LogicalResourceId": "function",
                "PhysicalResourceId": "my-function",
                "ResourceType": "AWS::Lambda::Function",
                "Replacement": "False",
                "ChangeSetId": null,
                "Scope": [
                    "Properties"
                ],
                "Details": [
                    {
                        "Target": {
                            "Attribute": "Properties",
                            "Name": "Timeout",
                            "RequiresRecreation": "Never"
                        },
                        "Evaluation": "Static",
                        "ChangeSource": "DirectModification"
                    }
                ]
            }
        }
    ],
    "ChangeSetName": "`my-nested-stack-change-set`",
    "ChangeSetId": "arn:aws:cloudformation:us-west-2:123456789012:changeSet/`my-nested-stack-change-set`/4eca1a01-e285-xmpl-8026-9a1967bfb4b0",
    "StackId": "arn:aws:cloudformation:us-west-2:123456789012:stack/`my-nested-stack`/d0a825a0-e4cd-xmpl-b9fb-061c69e99205",
    "ParentChangeSetId": "arn:aws:cloudformation:us-west-2:123456789012:changeSet/`my-root-stack-change-set`/4eca1a01-e285-xmpl-8026-9a1967bfb4b0",
    "RootChangeSetId": "arn:aws:cloudformation:us-west-2:123456789012:changeSet/`my-root-stack-change-set`/4eca1a01-e285-xmpl-8026-9a1967bfb4b0",
    "IncludeNestedStacks": true,
    "StackName": "`my-nested-stack`",
    "Description": null,
    "Parameters": null,
    "CreationTime": "2020-11-18T05:20:56.651Z",
    "ExecutionStatus": "UNAVAILABLE",
    "Status": "CREATE_COMPLETE",
    "StatusReason": "Executable from root change set",
    "NotificationARNs": [

    ],
    "RollbackConfiguration": {

    },
    "Capabilities": [
        "CAPABILITY_IAM"
    ],
    "Tags": null
}
```

- [execute-change-set](../../../cli/latest/reference/cloudformation/execute-change-set.md "../../../cli/latest/reference/cloudformation/execute-change-set.md") – Creates or
  updates a stack using the input information that was provided when the
  specified change set was created. To create a change set for the entire
  stack hierarchy, you must specify the
  `–-include-nested-stacks` option during the
  **create-change-set** operation. For more
  information, see [Execute a change set for a CloudFormation stack](using-cfn-updating-stacks-changesets-execute.md "using-cfn-updating-stacks-changesets-execute.md").

###### Note

**execute-change-set** must be executed from the
root change set and will apply the change set on the whole hierarchy
of stacks.
The following AWS CLI example executes a change set for the specified root
stack.

```
aws cloudformation execute-change-set \
    --stack-name `my-root-stack` \
    --change-set-name `my-root-stack-change-set`
```

- [delete-change-set](../../../cli/latest/reference/cloudformation/delete-change-set.md "../../../cli/latest/reference/cloudformation/delete-change-set.md") – Deletes the
  specified change set. Deleting change sets ensures that no one uses the
  wrong change set. Deleting change sets is asynchronous for change sets
  created with the `–-include-nested-stacks` option. For more
  information, see [Delete a change set for a CloudFormation stack](using-cfn-updating-stacks-changesets-delete.md "using-cfn-updating-stacks-changesets-delete.md").

###### Note

**delete-change-set** must be executed from the
root change set and will delete the whole hierarchy of change sets.
Nested stacks in the `REVIEW_IN_PROGRESS` status will
also be deleted if they were created during the
**create-change-set** operation.
The following AWS CLI example deletes the change set for the specified root
stack.

```
aws cloudformation delete-change-set \
    --stack-name `my-root-stack` \
    --change-set-name `my-root-stack-change-set`
```
