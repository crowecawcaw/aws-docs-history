# Resource tag-sync tasks

An automatic tag-synchronization of application resources (a _tag-sync task_) is an application resource management strategy
that works by automatically adding and removing
[The awsApplication tag](ar-user-tags.md "ar-user-tags.md") from resources to manage their inclusion in an application.
When you create a tag-sync task in the application, you specify a tag key-value pair to sync to the application,
such as `Project:Blue`. The task then adds any resources
tagged with `Project:Blue` to the application by adding the `awsApplication` tag to those resources.

When you perform the following actions, AWS adds all resources tagged with the `Project:Blue` tag to the application
by applying the `awsApplication` tag to those resources:

- Create an application using the existing tag key-value pair `Project:Blue`.
  For more information about bulk-onboarding application resources
  by specifying an existing tag key-value pair at application
  creation, review [Creating your first application in myApplications](../../../awsconsolehelpdocs/latest/gsg/myApp-getting-started.md#myApp-step1 "../../../awsconsolehelpdocs/latest/gsg/myApp-getting-started.md#myApp-step1")
  in the AWS Management Console _Getting started guide_.
- Create a tag-sync task in an existing application using the `Project:Blue` tag.
  After you configure the tag-sync task, it continuously manages the application's resources, adding or removing resources as they are tagged or
  untagged with the specified key-value pair.

When the task is active, if you tag a resource with the `Project:Blue` tag,
the tag-sync adds that resource to the application by applying the `awsApplication` tag to it.

When you remove the `Project:Blue` tag from a resource, the
tag-sync removes the resource from the application by removing the `awsApplication` tag.

###### Topics

- [Tag-sync task required permissions](#tag-sync-role "#tag-sync-role")
- [Create a tag-sync task](#create-tag-sync "#create-tag-sync")

## Tag-sync task required permissions

Creating and managing application tag-sync tasks requires you to specify or create an IAM role
that allows the tag-sync task to manage the application resources.

When configuring a tag-sync task, AWS recommends creating and using a new role to ensure the role includes the correct trust permissions.
With this option, AWS creates a role named _tag-sync-role-`region`-`uniqueID`_.
This role is comprised of the following permissions:

- The [`ResourceGroupsTaggingAPITagUntagSupportedResources`](../../../aws-managed-policy/latest/reference/ResourceGroupsTaggingAPITagUntagSupportedResources.md "../../../aws-managed-policy/latest/reference/ResourceGroupsTaggingAPITagUntagSupportedResources.md") AWS managed
  policy— Allows the tag-sync task to tag and untag resources. You can modify the role’s resource permissions based on your application needs by adding or removing a specific resource's
  `TagResource` and `UntagResource` permissions. For example, add `amplify:TagResource` and
  `amplify:UntagResource` to allow the tag-sync task to manage tags for AWS Amplify resources.
- A role [trust policy](../../../IAM/latest/UserGuide/id_roles.md#id_roles_terms-and-concepts "../../../IAM/latest/UserGuide/id_roles.md#id_roles_terms-and-concepts")— Allows AWS Resource Groups to assume the role and
  perform related tasks on your behalf.
- An [inline policy](../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#inline-policies "../../../IAM/latest/UserGuide/access_policies_managed-vs-inline.md#inline-policies")— Allows AWS Resource Groups
  to group and ungroup resources.

###### Important

To avoid disrupting the tag-sync task, do not delete this role or edit its trust or inline policies.

If you choose to use an existing IAM role, ensure it includes the following permissions:

- Permissions to tag and untag application resources.

**Option 1**: Use AWS managed policies

Use both the AWS Resource Groups [`ResourceGroupsTaggingAPITagUntagSupportedResources`](../../../ARG/latest/userguide/security_iam_awsmanpol.md#security-iam-awsmanpol-ResourceGroupsTaggingAPITagUntagSupportedResources "../../../ARG/latest/userguide/security_iam_awsmanpol.md#security-iam-awsmanpol-ResourceGroupsTaggingAPITagUntagSupportedResources") and
[`ResourceGroupsandTagEditorFullAccess`](../../../ARG/latest/userguide/security_iam_awsmanpol.md#security-iam-awsmanpol-ResourceGroupsandTagEditorFullAccess "../../../ARG/latest/userguide/security_iam_awsmanpol.md#security-iam-awsmanpol-ResourceGroupsandTagEditorFullAccess") AWS managed policies to grant the permissions
required to tag and untag all of the resource types supported by Resource Groups Tagging API, with some exceptions. The `ResourceGroupsandTagEditorFullAccess` policy
also grants the permissions required to retrieve all tagged, or previously tagged, resources through the Resource Groups Tagging API.

**Option 2**: Manually add permissions to an existing policy

If you choose not to use AWS managed policies, you must manually configure your policy to
include all of the permissions required to tag and untag your specific resources. For example, add the
`sqs:TagQueue` permission if you have an Amazon SQS queue resource in your application. In addition to the
resource-specific permissions, your policy must include the following Resource Groups Tagging API permissions:

    + `resource-groups:GroupResources`
    + `resource-groups:UngroupResources`
    + `tag:GetResources`
    + `tag:TagResources`
    + `tag:UntagResources`

- A [trust policy](../../../IAM/latest/UserGuide/id_roles.md#id_roles_terms-and-concepts "../../../IAM/latest/UserGuide/id_roles.md#id_roles_terms-and-concepts") attached
  that allows AWS Resource Groups to assume the role and perform these tasks on your behalf. The following is an example
  trust policy.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Sid": "Statement1",
 "Effect": "Allow",
 "Principal": {
 "Service": "resource-groups.amazonaws.com"
 },
 "Action": "sts:AssumeRole"
 }
 ]
}`

```

## Create a tag-sync task

This section provides instructions to create a tag-sync task for resources in an existing application
using either myApplications in the AWS Management Console or with the AWS API.

myApplications in AWS Management Console
For instructions to bulk-onboard application resources by specifying an existing tag key-value pair at application
creation, review [Creating your first application in myApplications](../../../awsconsolehelpdocs/latest/gsg/myApp-getting-started.md#myApp-step1 "../../../awsconsolehelpdocs/latest/gsg/myApp-getting-started.md#myApp-step1")
in the AWS Management Console _Getting started guide_.

AWS Resource Groups API

###### To create a tag-sync task

1. Create a new tag-sync task by calling the Resource Groups
   [`StartTagSyncTask` API](../../../ARG/latest/APIReference/API_StartTagSyncTask.md "../../../ARG/latest/APIReference/API_StartTagSyncTask.md")
   and specifying the following parameters:
   - **Group** — The Amazon resource name (ARN) or name of the
     application group for which you want to create a tag-sync task.
   - **TagKey** — The tag key.
   - **TagValue** — The tag value.
   - **RoleARN** — The ARN of the role that AWS Resource Groups assumes when
     performing the tag-sync task to apply the `awsApplication` tag to resources. This role must have the tagging permissions to all resources
     you want to include in the application. For more information, review [Tag-sync task required permissions](#tag-sync-role "#tag-sync-role").

```
aws resourcegroups start-tag-sync-task --group `appgroup-ARN-or-name` --tagkey `tag-key` --tagvalue `tag-value` --roleArn `role-ARN`
```

**Example output**:

The output includes a `TaskArn` that you can later use to query the status of the tag-sync task.

```
{
    "GroupArn" : "string",
    "GroupName" : "string",
    "TaskArn": "string",
    "TagKey" : "string",
    "TagValue" : "string",
    "RoleArn" : "string",
                        }
```

###### Note

For some accounts, an attempted `StartTagSyncTask` call may result in a `GroupNotFound` error. To resolve
this error, call the AppRegistry [`UpdateApplication` API](../dg/API_app-registry_UpdateApplication.md "../dg/API_app-registry_UpdateApplication.md"). This call enables the application to perform
tag-sync tasks. 2. Verify the status of the tag-sync task by calling the
[`GetTagSyncTask` API](../../../ARG/latest/APIReference/API_GetTagSyncTask.md "../../../ARG/latest/APIReference/API_GetTagSyncTask.md"). Enter the
`TaskArn` from the output of the previous `StartTagSyncTask` call.

```
aws resourcegroups get-tag-sync-task --taskArn `task-ARN`
```

**Example output:**

```
{
    "GroupArn" : "string",
    "GroupName" : "string",
    "TaskArn": "string",
    "TagKey" : "string",
    "TagValue" : "string",
    "RoleArn" : "string",
    "Status" : "string",
    "ErrorMessage" : "string",
    "ManagedGroupArn": "string",
    "CreatedAt": "timestamp"
}
```

**(optional) To list all tag-sync tasks**

To list all active tag-sync tasks, call the
[`ListTagSyncTasks` API](../../../ARG/latest/APIReference/API_ListTagSyncTasks.md "../../../ARG/latest/APIReference/API_ListTagSyncTasks.md").
You can optionally include the `Filters` parameter with a `GroupArn` or
`GroupName` to narrow your results to tasks in a specific application.

```
aws resourcegroups list-tag-sync-task --filters `group-name`
```

**Example output**:

```
{
    "TagSyncTasks": [
        {
            "GroupArn" : "string",
            "GroupName" : "string",
            "TaskArn": "string",
            "TagKey" : "string",
            "TagValue" : "string",
            "RoleArn" : "string",
            "Status" : "string",
            "ErrorMessage" : "string",
            "CreatedAt": "timestamp"
        }
    ],
    "NextToken": "string"
 }
```

**To cancel a tag-sync task**

To cancel a tag-sync task, call the
[`CancelTagSyncTask` API](../../../ARG/latest/APIReference/API_CancelTagSyncTask.md "../../../ARG/latest/APIReference/API_CancelTagSyncTask.md") and
enter the `TaskArn` of the tag-sync task you want to delete.

```
aws resourcegroups cancel-tag-sync-task --task-arn `task-ARN`
```
