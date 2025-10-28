# Using roles for AWS Batch

AWS Batch uses AWS Identity and Access Management (IAM) [service-linked roles](../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-linked-role "../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-linked-role"). A service-linked role is a unique type of IAM role that is
linked directly to AWS Batch. Service-linked roles are predefined by AWS Batch and
include all the permissions that the service requires to call other AWS services on your
behalf.

A service-linked role makes setting up AWS Batch easier because you don't have to
manually add the necessary permissions. AWS Batch defines the permissions of its
service-linked roles, and unless defined otherwise, only AWS Batch can assume its roles.
The defined permissions include the trust policy and the permissions policy, and that
permissions policy cannot be attached to any other IAM entity.

###### Note

Do one of the following
to specify a service role for an AWS Batch compute environment.

- Use an empty string for the service role. This lets AWS Batch create the service role.
- Specify the service role in the following format:
  `arn:aws:iam::`account_number`:role/aws-service-role/batch.amazonaws.com/AWSServiceRoleForBatch`.
  For more information, see [Incorrect role name or ARN](invalid_compute_environment.md#invalid_service_role_arn "invalid_compute_environment.md#invalid_service_role_arn") in the AWS Batch User Guide.

You can delete a service-linked role only after first deleting their related resources.
This protects your AWS Batch resources because you can't inadvertently remove permission
to access the resources.

For information about other services that support service-linked roles, see [AWS services
that work with IAM](../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md "../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md") and look for the services that have **Yes** in the **Service-linked roles** column. Choose a
**Yes** with a link to view the service-linked role
documentation for that service.

## Service-linked role

permissions for AWS Batch

AWS Batch uses the service-linked role named **AWSServiceRoleForBatch**
– Allows AWS Batch to create and manage AWS resources on your behalf.

The AWSServiceRoleForBatch service-linked role trusts the following services to assume the
role:

- `batch.amazonaws.com`

The role permissions policy named [BatchServiceRolePolicy](security-iam-awsmanpol.md#security-iam-awsmanpol-BatchServiceRolePolicy "security-iam-awsmanpol.md#security-iam-awsmanpol-BatchServiceRolePolicy") allows AWS Batch to complete
the following actions on the specified resources:

- `autoscaling` – Allows AWS Batch to create and manage Amazon EC2 Auto Scaling resources. AWS Batch creates and manages
  Amazon EC2 Auto Scaling groups for most compute environments.
- `ec2` – Allows AWS Batch to control the lifecycle of Amazon EC2 instances as well as create and manage
  launch templates and tags. AWS Batch creates and manages EC2 Spot Fleet requests for some EC2 Spot compute
  environments.
- `ecs` - Allows AWS Batch to create and managed Amazon ECS clusters, task-definitions and tasks for job
  execution.
- `eks` - Allows AWS Batch to describe the Amazon EKS cluster resource for validations.
- `iam` - Allows AWS Batch to validate and pass roles provided by owner to Amazon EC2, Amazon EC2 Auto Scaling and
  Amazon ECS.
- `logs` – Allows AWS Batch to create and manage log groups and log streams for AWS Batch jobs.

You must configure permissions to allow your users, groups, or roles to create, edit, or
delete a service-linked role. For more information, see [Service-linked role permissions](../../../IAM/latest/UserGuide/using-service-linked-roles.md#service-linked-role-permissions "../../../IAM/latest/UserGuide/using-service-linked-roles.md#service-linked-role-permissions") in the
_IAM User Guide_.

## Creating a service-linked role for

AWS Batch

You don't need to manually create a service-linked role. When you
create a compute environment in the AWS Management Console, the AWS CLI, or the AWS API, AWS Batch
creates the service-linked role for you.

###### Important

This service-linked role can appear in your account if you completed an action in another
service that uses the features supported by this role. If you were using the AWS Batch service before March 10, 2021, when it began
supporting service-linked roles, then AWS Batch created the AWSServiceRoleForBatch role in
your account. To
learn more, see [A new role appeared in my AWS account](../../../IAM/latest/UserGuide/troubleshoot_roles.md#troubleshoot_roles_new-role-appeared "../../../IAM/latest/UserGuide/troubleshoot_roles.md#troubleshoot_roles_new-role-appeared").

If you delete this service-linked role, and then need to create it again, you can use
the same process to recreate the role in your account. When you
create a compute environment, AWS Batch creates the service-linked role for you again.

## Editing a service-linked role for

AWS Batch

AWS Batch does not allow you to edit the AWSServiceRoleForBatch service-linked role. After
you create a service-linked role, you cannot change the name of the role because various
entities might reference the role. However, you can edit the description of the role using
IAM. For more information, see [Editing a service-linked role](../../../IAM/latest/UserGuide/using-service-linked-roles.md#edit-service-linked-role "../../../IAM/latest/UserGuide/using-service-linked-roles.md#edit-service-linked-role") in the
_IAM User Guide_.

**To allow an IAM entity to edit the description of the AWSServiceRoleForBatch service-linked
role**

Add the following statement to the permissions policy. This allows the IAM entity to edit the description of a
service-linked role.

```
{
    "Effect": "Allow",
    "Action": [
        "iam:UpdateRoleDescription"
    ],
    "Resource": "arn:aws:iam::*:role/aws-service-role/batch.amazonaws.com/AWSServiceRoleForBatch",
    "Condition": {"StringLike": {"iam:AWSServiceName": "batch.amazonaws.com"}}
}
```

## Deleting a service-linked role for

AWS Batch

If you no longer need to use a feature or service that requires a service-linked role,
we recommend that you delete that role. That way you don't have an unused entity that is not
actively monitored or maintained. However, you must clean up your service-linked role before
you can manually delete it.

**To allow an IAM entity to delete the AWSServiceRoleForBatch service-linked role**

Add the following statement to the permissions policy. This allows the IAM entity to delete a service-linked
role.

```
{
    "Effect": "Allow",
    "Action": [
        "iam:DeleteServiceLinkedRole",
        "iam:GetServiceLinkedRoleDeletionStatus"
    ],
    "Resource": "arn:aws:iam::*:role/aws-service-role/batch.amazonaws.com/AWSServiceRoleForBatch",
    "Condition": {"StringLike": {"iam:AWSServiceName": "batch.amazonaws.com"}}
}
```

### Cleaning up a

service-linked role

Before you can use IAM to delete a service-linked role, you must first confirm that the role has no active
sessions and delete all of the AWS Batch compute environments that use the role in all AWS Regions in a single
partition.

###### To check whether the service-linked role has an active session

1. Open the IAM console at
   [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. In the navigation pane, choose **Roles** and then the AWSServiceRoleForBatch name (not the check
   box).
3. On the **Summary** page, choose **Access Advisor** and review recent
   activity for the service-linked role.

###### Note

If you don't know whether AWS Batch is using the AWSServiceRoleForBatch role, you can try to delete the role. If the
service is using the role, then the role will fail to delete. You can view the Regions where the role is being
used. If the role is being used, then you must wait for the session to end before you can delete the role. You
can't revoke the session for a service-linked role.

###### To remove AWS Batch resources used by the AWSServiceRoleForBatch service-linked role

You must delete all AWS Batch compute environments that use the AWSServiceRoleForBatch role in all AWS Regions before you
can delete the AWSServiceRoleForBatch role.

1. Open the AWS Batch console at [https://console.aws.amazon.com/batch/](https://console.aws.amazon.com/batch/ "https://console.aws.amazon.com/batch/").
2. From the navigation bar, select the Region to use.
3. In the navigation pane, choose **Compute environments**.
4. Select the compute environment.
5. Choose **Disable**. Wait for the **State** to change to
   **DISABLED**.
6. Select the compute environment.
7. Choose **Delete**. Confirm that you want to delete the compute environment by choosing
   **Delete compute environment**.
8. Repeat steps 1–7 for all compute environments that use the service-linked role in all Regions.

### Deleting a service-linked role in IAM (Console)

You can use the IAM console to delete a service-linked role.

###### To delete a service-linked role (console)

1. Sign in to the AWS Management Console and open the IAM console at [https://console.aws.amazon.com/iam/](https://console.aws.amazon.com/iam/ "https://console.aws.amazon.com/iam/").
2. In the navigation pane of the IAM console, choose **Roles**. Then
   select the check box next to AWSServiceRoleForBatch, not the name or row itself.
3. Choose **Delete role**.
4. In the confirmation dialog box, review the service last accessed data, which shows
   when each of the selected roles last accessed an AWS service. This helps you to
   confirm whether the role is currently active. If you want to proceed, choose
   **Yes, Delete** to submit the service-linked role for
   deletion.
5. Watch the IAM console notifications to monitor the progress of the service-linked
   role deletion. Because the IAM service-linked role deletion is asynchronous, after you
   submit the role for deletion, the deletion task can succeed or fail.
   - If the task succeeds, then the role is removed from the list and a
     notification of success appears at the top of the page.
   - If the task fails, you can choose **View details** or
     **View Resources** from the notifications to learn why the
     deletion failed. If the deletion fails because the role is using the service's
     resources, then the notification includes a list of resources, if the service
     returns that information. You can then [clean up the resources](../../../IAM/latest/UserGuide/using-service-linked-roles.md#service-linked-role-review-before-delete "../../../IAM/latest/UserGuide/using-service-linked-roles.md#service-linked-role-review-before-delete") and submit the deletion again.

   ###### Note

   You might have to repeat this process several times, depending on the
   information that the service returns. For example, your service-linked role
   might use six resources and your service might return information about five
   of them. If you clean up the five resources and submit the role for deletion
   again, the deletion fails and the service reports the one remaining
   resource. A service might return all of the resources, a few of them, or it
   might not report any resources.
   - If the task fails and the notification does not include a list of
     resources, then the service might not return that information. To learn how to clean
     up the resources for that service, see [AWS services that work with IAM](../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md "../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md"). Find your service in
     the table, and choose the **Yes** link to view the
     service-linked role documentation for that service.

### Deleting a service-linked role in IAM (AWS CLI)

You can use IAM commands from the AWS Command Line Interface to delete a service-linked role.

###### To delete a service-linked role (CLI)

1. Because a service-linked role can't be deleted if it's being used or has associated resources, you must
   submit a deletion request. That request can be denied if these conditions aren't met. You must capture the
   `deletion-task-id` from the response to check the status of the deletion task. Enter the following
   command to submit a service-linked role deletion request:

```
`$` `aws iam delete-service-linked-role --role-name AWSServiceRoleForBatch`
```

2. Use the following command to check the status of the deletion task:

```
`$` `aws iam get-service-linked-role-deletion-status --deletion-task-id `deletion-task-id``
```

The status of the deletion task can be `NOT_STARTED`, `IN_PROGRESS`,
`SUCCEEDED`, or `FAILED`. If the deletion fails, the call returns the reason that it failed
so that you can troubleshoot. If the deletion fails because the role is using the service's resources, then
the notification includes a list of resources, if the service returns that information. You can then [clean up the
resources](../../../IAM/latest/UserGuide/using-service-linked-roles.md#service-linked-role-review-before-delete "../../../IAM/latest/UserGuide/using-service-linked-roles.md#service-linked-role-review-before-delete") and submit the deletion again.

###### Note

You might have to repeat this process several times, depending on the information that the service returns.
For example, your service-linked role might use six resources and your service might return information about
five of them. If you clean up the five resources and submit the role for deletion again, the deletion fails and
the service reports the one remaining resource. A service might return all of the resources, a few of them. Or,
it might not report any resources. To learn how to clean up the resources for a service that doesn't report any
resources, see [AWS services that work
with IAM](../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md "../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md"). Find your service in the table, and choose the **Yes** link to
view the service-linked role documentation for that service.

### Deleting a service-linked role in IAM (AWSAPI)

You can use the IAM API to delete a service-linked role.

###### To delete a service-linked role (API)

1. To submit a deletion request for a service-linked roll, call [DeleteServiceLinkedRole](../../../IAM/latest/APIReference/API_DeleteServiceLinkedRole.md "../../../IAM/latest/APIReference/API_DeleteServiceLinkedRole.md").
   In the request, specify the AWSServiceRoleForBatch role name.

Because a service-linked role cannot be deleted if it is being used or has
associated resources, you must submit a deletion request. That request can be denied if
these conditions are not met. You must capture the `DeletionTaskId` from the
response to check the status of the deletion task. 2. To check the status of the deletion, call [GetServiceLinkedRoleDeletionStatus](../../../IAM/latest/APIReference/API_GetServiceLinkedRoleDeletionStatus.md "../../../IAM/latest/APIReference/API_GetServiceLinkedRoleDeletionStatus.md"). In the request, specify the
`DeletionTaskId`.

The status of the deletion task can be `NOT_STARTED`,
`IN_PROGRESS`, `SUCCEEDED`, or `FAILED`. If the
deletion fails, the call returns the reason that it failed so that you can troubleshoot.
If the deletion fails because the role is using the service's resources, then the
notification includes a list of resources, if the service returns that information. You
can then [clean up the
resources](../../../IAM/latest/UserGuide/using-service-linked-roles.md#service-linked-role-review-before-delete "../../../IAM/latest/UserGuide/using-service-linked-roles.md#service-linked-role-review-before-delete") and submit the deletion again.

###### Note

You might have to repeat this process several times, depending on the information
that the service returns. For example, your service-linked role might use six
resources and your service might return information about five of them. If you clean
up the five resources and submit the role for deletion again, the deletion fails and
the service reports the one remaining resource. A service might return all of the
resources, a few of them, or it might not report any resources. To learn how to clean
up the resources for a service that does not report any resources, see
[AWS services that work with IAM](../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md "../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md"). Find your service in
the table, and choose the **Yes** link to view the
service-linked role documentation for that service.

## Supported Regions for AWS Batch

service-linked roles

AWS Batch supports using service-linked roles in all of the Regions where the
service is available. For more information, see [AWS Batch endpoints](../../../general/latest/gr/batch.md#batch_region "../../../general/latest/gr/batch.md#batch_region").
