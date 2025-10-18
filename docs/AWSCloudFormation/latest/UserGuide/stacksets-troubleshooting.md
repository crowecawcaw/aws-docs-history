# Troubleshooting AWS CloudFormation StackSets

This topic contains some common StackSets issues, and suggested solutions for those
 issues.

###### Topics

* [Common reasons for stack
 operation failure](#common-reasons-for-stack-operation-failure "#common-reasons-for-stack-operation-failure")
* [Retrying failed
 stack creation or update operations](#retrying-failed-stack-creation-or-update-operations "#retrying-failed-stack-creation-or-update-operations")
* [Stack instance deletion fails](#stack-instance-delete-fails "#stack-instance-delete-fails")
* [Stack import operation fails](#stack-import-fails "#stack-import-fails")
* [Stack instance
 failure count for StackSets operations](#stack-instance-failure-count-for-stackset-operations "#stack-instance-failure-count-for-stackset-operations")

## Common reasons for stack
 operation failure


Problem: A stack operation failed, and the stack
 instance status is `OUTDATED`.


Cause: There can be several common causes for stack
 operation failure.



* Insufficient permissions in a target account for creating resources that are
 specified in your template.
* The CloudFormation template might have errors. Validate the template in CloudFormation
 and fix errors before trying to create your StackSet.
* The template could be trying to create global resources that must be unique
 but aren't, such as S3 buckets.
* A specified target account number doesn't exist. Check the target account
 numbers that you specified on the **Set deployment options**
 page of the wizard.
* The administrator account does not have a trust relationship with the target
 account.
* The maximum number of a resource that is specified in your template already
 exists in your target account. For example, you might have reached the limit of
 allowed IAM roles in a target account, but the template creates more IAM
 roles.
* You have reached the maximum number of stacks that are allowed in a StackSet. For
 the maximum number of stacks per StackSet, see [Understand CloudFormation quotas](cloudformation-limits.md "cloudformation-limits.md").

Solution: For more information about the permissions
 required of target and administrator accounts before you can create StackSets, see
 [Give all users of the administrator
 account permissions to manage stacks in all target accounts](stacksets-prereqs-self-managed.md#stacksets-prereqs-accountsetup "stacksets-prereqs-self-managed.md#stacksets-prereqs-accountsetup").


## Retrying failed
 stack creation or update operations


Problem: A stack creation or update failed, and the
 stack instance status is `OUTDATED`. To troubleshoot why a stack creation or
 update failed, open the CloudFormation console, and view the events for the stack, which
 will have a status of `DELETED` (for failed create operations) or
 `FAILED` (for failed update operations). Browse the stack events, and
 find the **Status reason** column. The value of **Status
 reason** explains why the stack operation failed.


After you have fixed the underlying cause of the stack creation failure, and you are
 ready to retry stack creation, perform the following steps.


Solution: Perform the following steps to retry your
 stack operation.


1. In the console, select the StackSet that contains the stack on which the operation
 failed.
2. In the **Actions** menu, choose **Edit StackSet
 details** to retry creating or updating stacks.
3. On the **Specify template** page, to use the same CloudFormation
 template, keep the default option, **Use current template**. If
 your stack operation failed because the template required changes, and you want
 to upload a revised template, choose **Upload a template to Amazon
 S3** instead, and then choose **Browse** to select
 your updated template. When you are finished uploading your revised template,
 choose **Next**.
4. On the **Specify stack details** page, if you are not
 changing any parameters that are specific to your template, choose
 **Next**.
5. On the **Set deployment options** page, change defaults for
 **Maximum concurrent accounts** and **Failure
 tolerance**, if desired. For more information about these settings,
 see [StackSet operation options](stacksets-concepts.md#stackset-ops-options "stacksets-concepts.md#stackset-ops-options").
6. On the **Review** page, review your selections, and fill the
 checkbox to acknowledge required IAM capabilities. Choose
 **Submit**.
7. If your stack is not successfully updated, repeat this procedure, after you've
 resolved any underlying issues that are preventing stack creation.

## Stack instance deletion fails


Problem: A stack deletion has failed.


Cause: Stack deletion will fail for any stacks on which
 termination protection has been enabled.


Solution: Determine if termination protection has been
 enabled for the stack. If it has, disable termination protection and then perform the
 stack instance deletion again.


## Stack import operation fails


Problem: A stack import operation fails to import
 existing stacks into new or existing StackSets. The stack instance is in an
 `INOPERABLE` status.


Solution: Revert the stack import operation, by
 completing the following tasks.



1. Use **Delete Stacks from StackSets** option and enable
 **RetainStacks** during configuration, then proceed to
 delete stack instances from your StackSet. For more information, For more
 information, see [Delete stacks from AWS CloudFormation StackSets](stackinstances-delete.md "stackinstances-delete.md") .
2. You will see the stack instances of the StackSet are updated to remove the
 `INOPERABLE` stack instance.
3. Fix the stack instances according to the import failure error and retry the
 stack import operation.

## Stack instance
 failure count for StackSets operations


The stack instance failure count alerts you if stack instances fail to provision or
 update. These stack instances didn't deploy because of one or more of the following
 reasons:



* Existing resource(s) with a similar configuration
* Missing dependencies, such as AWS Identity and Access Management (IAM) roles
* Other conflicting factors

If you want to deploy with maximum concurrency, max concurrency count is one more than
 the failure tolerance count, at most. For example, if the failure tolerance count is 9,
 then max concurrency count can’t be more than 10. This will cause the operation to
 return `SUCCEEDED` even if some stack instances fail to update. The new stack
 instance failure count enables you to determine if the operation only conditionally
 succeeded because the failure tolerance count is set to allow all failures.


You can use the AWS Management Console, AWS SDK, or AWS CLI to get the failure count and filter
 stack instances to determine which instances need to be redeployed.


### Using the console


###### To view the number of failed stack instances:

1. Open the [CloudFormation
 console](https://console.aws.amazon.com/cloudformation "https://console.aws.amazon.com/cloudformation") and choose **StackSets**.
2. Choose your StackSet, and then choose the **Operations**
 tab.
3. Choose a status in the **Status** column to view the
 status details. You will find the number of failed stack instances for a
 particular operation in the status details.

###### To view the account, region, and status of stack instances for the
 operation:

1. In the status details, choose the failed stack instances count.
 *Example:*
**Stack instances: `<number of failed stack
 instances>`**.
2. Expand the side panel by choosing the panel header. The results in the
 side panel are the statuses of the stack instances after the completion of
 the selected operation.

###### To view the current stack instance details for an operation:

1. Choose the **Stack Instances** tab.
2. Filter by **Last operation ID**. The results are the
 current statuses and status reasons from the last operation to modify the
 instance. You can use this filter in combination with **AWS
 account**, **AWS region**,
 **Detailed Status**, and **Drift
 status** to further refine your search results.

### Using the AWS CLI


To get the number of failed stack instances, call
 `describe-stack-set-operation` or
 `list-stack-set-operations` and see
 `StatusDetails`.



```
aws cloudformation describe-stack-set-operation --stack-set-name `ss1` \
    --operation-id `5550e62f-c822-4331-88fa-21c1d7bafc60`
```


```
{
    "StackSetOperation": {
        "OperationId": "5550e62f-c822-4331-88fa-21c1d7bafc60",
        "StackSetId": "ss1:9101ca57-49fc-4a61-a5a6-4c97b8adb08f",
        "Action": "CREATE",
        "Status": "SUCCEEDED",
        "OperationPreferences": {
            "RegionOrder": [],
            "FailureToleranceCount": 10,
            "MaxConcurrentCount": 10
        },
        "AdministrationRoleARN": "arn:aws:iam::123456789012:role/AWSCloudFormationStackSetAdministrationRole",
        "ExecutionRoleName": "AWSCloudFormationStackSetExecutionRole",
        "CreationTimestamp": "2022-10-26T17:18:53.947000+00:00",
        "EndTimestamp": "2022-10-26T17:19:35.304000+00:00",
        "StatusDetails": {
            "FailedStackInstancesCount": 3
        }
    }
}
```


```
aws cloudformation list-stack-set-operations --stack-set-name `ss1`
```


```
{
    "Summaries": [
        {
            "OperationId": "5550e62f-c822-4331-88fa-21c1d7bafc60",
            "Action": "CREATE",
            "Status": "SUCCEEDED",
            "CreationTimestamp": "2022-10-26T17:18:53.947000+00:00",
            "EndTimestamp": "2022-10-26T17:19:35.304000+00:00",
            "StatusDetails": {
                "FailedStackInstancesCount": 3
            },
            "OperationPreferences": {
                "RegionOrder": [],
                "FailureToleranceCount": 10,
                "MaxConcurrentCount": 10
            }
        }
    ]
}
```

To get a historical overview for a particular operation, use
 `list-stack-set-operation-results` to view the status and status
 reason for each stack instance after the operation completed. See the following
 example to find the `Status` and `StatusReason`:



```
aws cloudformation list-stack-set-operation-results --stack-set-name `ss1` \
  --operation-id `5550e62f-c822-4331-88fa-21c1d7bafc60` --filters `Name=OPERATION_RESULT_STATUS,Values=FAILED`
```


```
{
    "Summaries": [
        {
            "Account": "123456789012",
            "Region": "us-west-2",
            "Status": "FAILED",
            "StatusReason": "Account 123456789012 should have 'AWSCloudFormationStackSetExecutionRole' role with trust relationship to Role 'AWSCloudFormationStackSetAdministrationRole'.",
            "AccountGateResult": {
                "Status": "SKIPPED",
                "StatusReason": "Account 123456789012 should have 'AWSCloudFormationStackSetExecutionRole' role with trust relationship to Role 'AWSCloudFormationStackSetAdministrationRole'."
            },
            "OrganizationalUnitId": ""
        },
        {
            "Account": "123456789012",
            "Region": "us-west-1",
            "Status": "FAILED",
            "StatusReason": "Account 123456789012 should have 'AWSCloudFormationStackSetExecutionRole' role with trust relationship to Role 'AWSCloudFormationStackSetAdministrationRole'.",
            "AccountGateResult": {
                "Status": "SKIPPED",
                "StatusReason": "Account 123456789012 should have 'AWSCloudFormationStackSetExecutionRole' role with trust relationship to Role 'AWSCloudFormationStackSetAdministrationRole'."
            },
            "OrganizationalUnitId": ""
        },
        {
            "Account": "123456789012",
            "Region": "us-east-1",
            "Status": "FAILED",
            "StatusReason": "Account 123456789012 should have 'AWSCloudFormationStackSetExecutionRole' role with trust relationship to Role 'AWSCloudFormationStackSetAdministrationRole'.",
            "AccountGateResult": {
                "Status": "SKIPPED",
                "StatusReason": "Account 123456789012 should have 'AWSCloudFormationStackSetExecutionRole' role with trust relationship to Role 'AWSCloudFormationStackSetAdministrationRole'."
            },
            "OrganizationalUnitId": ""
        }
    ]
}
```

Use `list-stack-instances` with the `DETAILED_STATUS` and
 `LAST_OPERATION_ID` filters to get a list of stack instances that
 failed in the last operation that tried to deploy the stack instance. See the
 `--filters` flag in the example with `DETAILED_STATUS` and
 `LAST_OPERATION_ID`:



```
aws cloudformation list-stack-instances --stack-set-name `ss1` \
  --filters `Name=DETAILED_STATUS,Values=FAILED Name=LAST_OPERATION_ID,Values=5550e62f-c822-4331-88fa-21c1d7bafc60`
```


```
{
    "Summaries": [
        {
            "StackSetId": "ss1:9101ca57-49fc-4a61-a5a6-4c97b8adb08f",
            "Region": "us-east-1",
            "Account": "123456789012",
            "Status": "OUTDATED",
            "StatusReason": "Account 123456789012 should have 'AWSCloudFormationStackSetExecutionRole' role with trust relationship to Role 'AWSCloudFormationStackSetAdministrationRole'.",
            "StackInstanceStatus": {
                "DetailedStatus": "FAILED"
            },
            "OrganizationalUnitId": "",
            "DriftStatus": "NOT_CHECKED",
            "LastOperationId": "5550e62f-c822-4331-88fa-21c1d7bafc60"
        },
        {
            "StackSetId": "ss1:9101ca57-49fc-4a61-a5a6-4c97b8adb08f",
            "Region": "us-west-1",
            "Account": "123456789012",
            "Status": "OUTDATED",
            "StatusReason": "Account 123456789012 should have 'AWSCloudFormationStackSetExecutionRole' role with trust relationship to Role 'AWSCloudFormationStackSetAdministrationRole'.",
            "StackInstanceStatus": {
                "DetailedStatus": "FAILED"
            },
            "OrganizationalUnitId": "",
            "DriftStatus": "NOT_CHECKED",
            "LastOperationId": "5550e62f-c822-4331-88fa-21c1d7bafc60"
        },
        {
            "StackSetId": "ss1:9101ca57-49fc-4a61-a5a6-4c97b8adb08f",
            "Region": "us-west-2",
            "Account": "123456789012",
            "Status": "OUTDATED",
            "StatusReason": "Account 123456789012 should have 'AWSCloudFormationStackSetExecutionRole' role with trust relationship to Role 'AWSCloudFormationStackSetAdministrationRole'.",
            "StackInstanceStatus": {
                "DetailedStatus": "FAILED"
            },
            "OrganizationalUnitId": "",
            "DriftStatus": "NOT_CHECKED",
            "LastOperationId": "5550e62f-c822-4331-88fa-21c1d7bafc60"
        }
    ]
}
```

To find the last operation ID to modify a stack instance, use
 `list-stack-instances` or `describe-stack-instance` to get
 the `LastOperationId`:



```
aws cloudformation describe-stack-instance --stack-set-name `ss1` \
  --stack-instance-account `123456789012` --stack-instance-region `us-east-2`
```


```
{
    "StackInstance": {
        "StackSetId": "ss1:9101ca57-49fc-4a61-a5a6-4c97b8adb08f",
        "Region": "us-west-2",
        "Account": "123456789012",
        "ParameterOverrides": [],
        "Status": "OUTDATED",
        "StackInstanceStatus": {
            "DetailedStatus": "FAILED"
        },
        "StatusReason": "Account 123456789012 should have 'AWSCloudFormationStackSetExecutionRole' role with trust relationship to Role 'AWSCloudFormationStackSetAdministrationRole'.",
        "OrganizationalUnitId": "",
        "DriftStatus": "NOT_CHECKED",
        "LastOperationId": "5550e62f-c822-4331-88fa-21c1d7bafc60"
    }
}
```
