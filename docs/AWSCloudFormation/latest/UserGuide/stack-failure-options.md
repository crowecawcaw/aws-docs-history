# Choose how to handle failures when provisioning

resources

If your stack operation fails, you don't have to roll back resources that were already
successfully provisioned and start over from the beginning every time. Instead, you can
troubleshoot resources in a `CREATE_FAILED` or `UPDATE_FAILED` status, and
then resume provisioning from the point where the problem occurred.

To do this, you must enable the preserve successfully provisioned resources option. This
option is available for all stack deployments and change set operations.

- For stack creation, if you choose the **Preserve successfully provisioned
  resources** option, CloudFormation preserves the state of resources that were successfully
  created and leaves the failed ones in a failed state until the next update operation is
  performed.
- During update and change set operations, choosing **Preserve successfully
  provisioned resources** preserves the state of successful resources while rolling back
  failed resources to their last known stable state. Failed resources will be in an
  `UPDATE_FAILED` state. Resources without a last known stable state will be deleted
  upon the next stack operation.

###### Topics

- [Overview of stack failure options](#stack-failure-options-overview "#stack-failure-options-overview")
- [Required conditions for pausing stack
  rollback](#stack-failure-options-conditions "#stack-failure-options-conditions")
- [Preserve successfully provisioned resources
  (console)](#stack-failure-options-console "#stack-failure-options-console")
- [Preserve successfully provisioned resources
  (AWS CLI)](#stack-failure-options-cli "#stack-failure-options-cli")

## Overview of stack failure options

Before issuing an operation from the CloudFormation console, API, or AWS CLI, specify the behavior
for provisioned resource failure. Then, proceed with the deployment process of your resources
without any other modifications. In the event of an operational failure, CloudFormation stops at the
first failure in each independent provisioning path. CloudFormation identifies dependencies between
resources to parallelize independent provisioning actions. Then it proceeds to provision
resources on each independent provisioning path until it encounters a failure. A failure in one
path doesn’t affect other provisioning paths. CloudFormation will continue to provision the resources
until completion or stop on a different failure.

Remediate any issues to continue the deployment process. CloudFormation performs the necessary
updates before retrying provisioning actions on resources that couldn’t be successfully
provisioned earlier. You remediate issues by submitting a **Retry**,
**Update**, or **Roll back** operations. For example, if
you're provisioning an Amazon EC2 instance and the EC2 instance fails during a create operation, you
might want to investigate the error, rather than rolling back the failed resource right away. You
can review system status checks and instances status checks, and then select the
**Retry** operation once the issues is resolved.

When a stack operation fails, and you've specified **Preserve successfully
provisioned resources** from the **Stack failure options** menu, you
can select the following options.

- **Retry** – Retries provisioning operation on failed resources and
  continues provisioning the template until the successful completion of the stack operation or
  the next failure. Select this option if the resource failed to provision due to an issue that
  doesn't require template modifications, such as an AWS Identity and Access Management (IAM) permission.
- **Update** – Resources that have been provisioned are updated on
  template updates. Resources that failed to create or update will be retried. Select this option
  if the resource failed to provision due to template errors, and you've modified the template.
  When you update a stack that's in a `FAILED` state, you must select
  **Preserve successfully provisioned resources** for the **Stack
  failure options** to continue updating your stack.
- **Roll back** – CloudFormation rolls back the stack to the last known
  stable state.

## Required conditions for pausing stack

rollback

To prevent CloudFormation from automatically rolling back and deleting the resources that were
successfully created, the following conditions must be met.

1. When you create or update the stack, you must choose the option to **Preserve
   successfully provisioned resources**. This tells CloudFormation not to delete the
   resources that were created successfully, even if the overall stack operation fails.
2. The stack operation must have failed, meaning the stack status is either
   `CREATE_FAILED` or `UPDATE_FAILED`.

###### Note

Immutable update types aren't supported.

## Preserve successfully provisioned resources

(console)

Create stack

###### To preserve successfully provisioned resources during a create stack operation

1. Sign in to the AWS Management Console and open the AWS CloudFormation console at
   [https://console.aws.amazon.com/cloudformation](https://console.aws.amazon.com/cloudformation/ "https://console.aws.amazon.com/cloudformation/").
2. From the **Stacks** page, choose **Create stack** at
   top right, and then choose **With new resources (standard)**.
3. For **Prerequisite - Prepare template**, choose **Choose an
   existing template**.
4. Under **Specify template**, choose to either specify the URL for the
   S3 bucket that contains your stack template or upload a stack template file. Then, choose
   **Next**.
5. On the **Specify stack details** page, enter a stack name in the
   **Stack name** box.
6. In the **Parameters** section, specify parameters that are defined in
   your stack template.

You can use or change any parameters with default values. 7. When you're satisfied with the parameter values, choose
**Next**. 8. On the **Configure stack options** page, you can set additional
options for your stack. 9. For **Stack failure options**, select **Preserve successfully
provisioned resources**. 10. When you're satisfied with the stack options, choose **Next**. 11. Review your stack on the **Review** page and select **Create
stack**.

_Results_: Resources that failed to create transition the stack status
to `CREATE_FAILED` to prevent the stack from rolling back when the stack operation
encounters a failure. Resources that are successfully provisioned are in a
`CREATE_COMPLETE` state. You can monitor the stack in the **Stack
events** tab.

Update stack

###### To preserve successfully provisioned resources during an update stack operation

1.  Sign in to the AWS Management Console and open the AWS CloudFormation console at
    [https://console.aws.amazon.com/cloudformation](https://console.aws.amazon.com/cloudformation/ "https://console.aws.amazon.com/cloudformation/").
2.  Select the stack you want to update and then choose **Update**.
3.  On the **Update stack** page, choose a stack template by using one of
    the following options:

        * **Use existing template**
        * **Replace current template**
        * **Edit template in Infrastructure Composer**

    Accept your settings and select **Next**.

4.  On the **Specify stack details** page, specify parameters that are
    defined in your stack template.

You can use or change any parameters with default values. 5. When you're satisfied with the parameter values, choose
**Next**. 6. On the **Configure stack options** page, you can set additional
options for your stack. 7. For the **Behavior on provisioning failure**, select
**Preserve successfully provisioned resources**. 8. When you're satisfied with the stack options, choose **Next**. 9. Review your stack on the **Review** page and select **Update
stack**.

_Results_: Resources that failed to update transition the stack status
to `UPDATE_FAILED` and roll back to the last known stable state. Resources without
a last known stable state will be deleted by CloudFormation upon the next stack operation.
Resources that are successfully provisioned are in a `CREATE_COMPLETE` or
`UPDATE_COMPLETE` state. You can monitor the stack in the **Stack
events** tab.

Change set

###### Note

You can initiate a change set for a stack with a status of `CREATE_FAILED` or
`UPDATE_FAILED`, but not for a status of
`UPDATE_ROLLBACK_FAILED`.

###### To Preserve successfully provisioned resources during a change set operation

1. Sign in to the AWS Management Console and open the AWS CloudFormation console at
   [https://console.aws.amazon.com/cloudformation](https://console.aws.amazon.com/cloudformation/ "https://console.aws.amazon.com/cloudformation/").
2. Select the stack that contains the change set you want to initiate, and then choose the
   **Change sets** tab.
3. Select the change set and then choose **Execute**.
4. For **Execute change set**, select the **Preserve successfully
   provisioned resources** option.
5. Select **Execute change set**.

_Results_: Resources that failed to update transition the stack status
to `UPDATE_FAILED` and roll back to the last known stable state. Resources without
a last known stable state will be deleted by CloudFormation upon the next stack operation.
Resources that are successfully provisioned are in a `CREATE_COMPLETE` or
`UPDATE_COMPLETE` state. You can monitor the stack in the **Stack
events** tab.

## Preserve successfully provisioned resources

(AWS CLI)

Create stack

###### To preserve successfully provisioned resources during a stack create operation

Specify the `--disable-rollback` option or `on-failure DO_NOTHING`
enumeration during a [create-stack](../../../cli/latest/reference/cloudformation/create-stack.md "../../../cli/latest/reference/cloudformation/create-stack.md")
operation.

1. Provide a stack name and template to the **create-stack** command with
   the `--disable-rollback` option.

```
aws cloudformation create-stack --stack-name `myteststack` \
    --template-body `file://template.yaml` \
    --disable-rollback
```

The command returns the following output.

```
{
    "StackId": "arn:aws:cloudformation:us-east-1:123456789012:stack/myteststack/466df9e0-0dff-08e3-8e2f-5088487c4896"
}
```

2. Describe the state of the stack using the **describe-stacks**
   command.

```
aws cloudformation describe-stacks --stack-name `myteststack`
```

The command returns the following output.

```
{
    "Stacks":  [
        {
            "StackId": "arn:aws:cloudformation:us-east-1:123456789012:stack/myteststack/466df9e0-0dff-08e3-8e2f-5088487c4896",
            "Description": "AWS CloudFormation Sample Template",
            "Tags": [],
            "Outputs": [],
            "StackStatusReason": “The following resource(s) failed to create: [MyBucket]”,
            "CreationTime": "2013-08-23T01:02:15.422Z",
            "Capabilities": [],
            "StackName": "myteststack",
            "StackStatus": "CREATE_FAILED",
            "DisableRollback": true
        }
    ]
}
```

Update stack

###### To preserve successfully provisioned resources during a stack update operation

1. Provide an existing stack name and template to the **update-stack**
   command with the `--disable-rollback` option.

```
aws cloudformation update-stack --stack-name `myteststack` \
    --template-url `https://s3.amazonaws.com/`amzn-s3-demo-bucket`/updated.template` --disable-rollback
```

The command returns the following output.

```
{
    "StackId": "arn:aws:cloudformation:us-east-1:123456789012:stack/myteststack/466df9e0-0dff-08e3-8e2f-5088487c4896"
}
```

2. Describe the state of the stack using either the **describe-stacks** or
   **describe-stack-events** command.

```
aws cloudformation describe-stacks --stack-name `myteststack`
```

The command returns the following output.

```
{
    "Stacks":  [
        {
            "StackId": "arn:aws:cloudformation:us-east-1:123456789012:stack/myteststack/466df9e0-0dff-08e3-8e2f-5088487c4896",
            "Description": "AWS CloudFormation Sample Template",
            "Tags": [],
            "Outputs": [],
            "CreationTime": "2013-08-23T01:02:15.422Z",
            "Capabilities": [],
            "StackName": "myteststack",
            "StackStatus": "UPDATE_COMPLETE",
            "DisableRollback": true
        }
    ]
}
```

Change set

###### Note

You can initiate a change set for a stack with a status of `CREATE_FAILED` or
`UPDATE_FAILED`
but not for a status of `UPDATE_ROLLBACK_FAILED`.

###### To preserve successfully provisioned resources during a change set operation

Specify the `--disable-rollback` option
during an [execute-change-set](../../../cli/latest/reference/cloudformation/execute-change-set.md "../../../cli/latest/reference/cloudformation/execute-change-set.md")
operation.

1. Provide a stack name and template to the **execute-change-set** command
   with the `--disable-rollback` option.

```
aws cloudformation execute-change-set --stack-name `myteststack` \
    --change-set-name `my-change-set` --template-body `file://template.yaml`
```

The command returns the following output.

```
{
 "Id": "arn:aws:cloudformation:us-east-1:123456789012:changeSet/my-change-set/bc9555ba-a949-xmpl-bfb8-f41d04ec5784",
 "StackId": "arn:aws:cloudformation:us-east-1:123456789012:stack/myteststack/466df9e0-0dff-08e3-8e2f-5088487c4896"
}
```

2. Initiate the change set with `--disable-rollback` option.

```
aws cloudformation execute-change-set --stack-name `myteststack` \
    --change-set-name `my-change-set` -–disable-rollback
```

3. Determine the status of the stack using either the **describe-stacks**
   or **describe-stack-events** command.

```
aws cloudformation describe-stack-events --stack-name `myteststack`
```

The command returns the following output.

```
{
   "StackEvents": [
     {
        "StackId": "arn:aws:cloudformation:us-east-1:123456789012:stack/myteststack/466df9e0-0dff-08e3-8e2f-5088487c4896",
        "EventId": "49c966a0-7b74-11ea-8071-024244bb0672",
        "StackName": "myteststack",
        "LogicalResourceId": " MyBucket",
        "PhysicalResourceId": "myteststack-MyBucket-abcdefghijk1",
        "ResourceType": "AWS::S3::Bucket",
        "Timestamp": "2020-04-10T21:43:17.015Z",
        "ResourceStatus": "UPDATE_FAILED"
        "ResourceStatusReason": "User XYZ is not allowed to perform S3::UpdateBucket on MyBucket"
     }
}
```

4. Fix permissions errors and retry the operation.

```
aws cloudformation update-stack --stack-name `myteststack` \
    --use-previous-template --disable-rollback
```

The command returns the following output.

```
{
    "StackId": "arn:aws:cloudformation:us-east-1:123456789012:stack/myteststack/466df9e0-0dff-08e3-8e2f-5088487c4896"
}
```

5. Describe the state of the stack using either the **describe-stacks** or
   **describe-stack-events** command.

```
aws cloudformation describe-stacks --stack-name `myteststack`
```

The command returns the following output.

```
{
    "Stacks":  [
        {
            "StackId": "arn:aws:cloudformation:us-east-1:123456789012:stack/myteststack/466df9e0-0dff-08e3-8e2f-5088487c4896",
            "Description": "AWS CloudFormation Sample Template",
            "Tags": [],
            "Outputs": [],
            "CreationTime": "2013-08-23T01:02:15.422Z",
            "Capabilities": [],
            "StackName": "myteststack",
            "StackStatus": "UPDATE_COMPLETE",
            "DisableRollback": true
        }
    ]
}
```

### Rolling back a stack

You can use the [rollback-stack](../../../cli/latest/reference/cloudformation/rollback-stack.md "../../../cli/latest/reference/cloudformation/rollback-stack.md") command to
roll back a stack with a `CREATE_FAILED` or `UPDATE_FAILED` stack status
to its last stable state.

The following **rollback-stack** command rolls back the specified
stack.

```
aws cloudformation rollback-stack --stack-name `myteststack`
```

The command returns the following output.

```
{
    "StackId": "arn:aws:cloudformation:us-east-1:123456789012:stack/myteststack/466df9e0-0dff-08e3-8e2f-5088487c4896"
}
```

###### Note

The **rollback-stack** operation will delete a stack if it doesn't contain
a last known stable state.
