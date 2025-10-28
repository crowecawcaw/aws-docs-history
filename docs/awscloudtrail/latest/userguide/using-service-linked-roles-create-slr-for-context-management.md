# Using roles for creating and managing CloudTrail event context in CloudTrail

AWS CloudTrail uses AWS Identity and Access Management (IAM) [service-linked roles](../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-linked-role "../../../IAM/latest/UserGuide/id_roles_terms-and-concepts.md#iam-term-service-linked-role"). A service-linked role is a unique type of IAM role that is
linked directly to CloudTrail. Service-linked roles are predefined by CloudTrail and
include all the permissions that the service requires to call other AWS services on your
behalf.

A service-linked role makes setting up CloudTrail easier because you don’t have to
manually add the necessary permissions. CloudTrail defines the permissions of its
service-linked roles, and unless defined otherwise, only CloudTrail can assume its roles.
The defined permissions include the trust policy and the permissions policy, and that
permissions policy cannot be attached to any other IAM entity.

You can delete a service-linked role only after first deleting their related resources.
This protects your CloudTrail resources because you can't inadvertently remove permission
to access the resources.

For information about other services that support service-linked roles, see [AWS services
that work with IAM](../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md "../../../IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.md") and look for the services that have **Yes** in the **Service-linked roles** column. Choose a
**Yes** with a link to view the service-linked role
documentation for that service.

## Service-linked role

permissions for CloudTrail

CloudTrail uses the service-linked role named **AWSServiceRoleForCloudTrailEventContext**
– This service linked role is used for managing CloudTrail Event Context and EventBridge rules.

The AWSServiceRoleForCloudTrailEventContext service-linked role trusts the following services to assume the
role:

- `context.cloudtrail.amazonaws.com`

The role permissions policy named CloudTrailEventContext allows CloudTrail to complete
the following actions on the specified resources:

- Actions on resource tags:
  - `tag:GetResources`

- Actions on all Amazon EventBridge resources for the CloudTrail service principal to create
  rules:
  - `events:PutRule`

- Actions on all Amazon EventBridge resources for the CloudTrail service principal to manage the rules
  it creates:
  - `events:PutTargets`
  - `events:DeleteRule`
  - `events:RemoveTargets`
  - `events:RemoveTargets`

- Actions on all Amazon EventBridge resources for the CloudTrail service principal to describe the
  rules it creates:
  - `events:DescribeRule`
  - `events:DeRegisterResource`

- Actions on all Amazon EventBridge resources:
  - `events:ListRules`

You must configure permissions to allow your users, groups, or roles to create, edit, or
delete a service-linked role. For more information, see [Service-linked role permissions](../../../IAM/latest/UserGuide/using-service-linked-roles.md#service-linked-role-permissions "../../../IAM/latest/UserGuide/using-service-linked-roles.md#service-linked-role-permissions") in the
_IAM User Guide_.

For more information about the managed policy associated with AWSServiceRoleForCloudTrailEventContext, see [AWS managed policies for AWS CloudTrail](security-iam-awsmanpol.md "security-iam-awsmanpol.md").

## Creating a service-linked role for

CloudTrail

You don't need to manually create a service-linked role. When you
begin using the context event feature in the AWS Management Console, the AWS CLI, or the AWS API, CloudTrail
creates the service-linked role for you.

If you delete this service-linked role, and then need to create it again, you can use
the same process to recreate the role in your account. When you
begin using the context event feature, CloudTrail creates the service-linked role for you again.

## Editing a service-linked role for

CloudTrail

CloudTrail does not allow you to edit the AWSServiceRoleForCloudTrailEventContext service-linked role. After
you create a service-linked role, you cannot change the name of the role because various
entities might reference the role. However, you can edit the description of the role using
IAM. For more information, see [Editing a service-linked role](../../../IAM/latest/UserGuide/using-service-linked-roles.md#edit-service-linked-role "../../../IAM/latest/UserGuide/using-service-linked-roles.md#edit-service-linked-role") in the
_IAM User Guide_.

## Deleting the AWSServiceRoleForCloudTrailEventContext service-linked role for

CloudTrail

If you no longer need to use a feature or service that requires the AWSServiceRoleForCloudTrailEventContext
service-linked role, we recommend that you delete that role. That way you don’t have an
unused entity that is not actively monitored or maintained. However, you must clean up the
resources for your service-linked role before you can manually delete it by removing the
TagContext key from event data stores.

###### Note

If the CloudTrail service is using the role when you try to delete the resources,
then the deletion might fail. If that happens, wait for a few minutes and try the operation
again.

###### To delete CloudTrail resources used by the AWSServiceRoleForCloudTrailEventContext service linked

role

1. At the terminal or command line, run the **put-event-configuration**
   command for the event store from which you want to remove the `TagContext`
   key. For example, to remove the `TagContext` key from an event store in the `111122223333` account in the US East (Ohio) Region with an ARN of
   `arn:aws:cloudtrail:us-east-2:111122223333:eventdatastore/a1b2c3d4-5678-90ab-cdef-EXAMPLE11111` where `TagContext` is the only context key selector,
   you would use the **put-event-configuration** command with no value specified for `--context-key-selectors`:

```
 aws cloudtrail put-event-configuration --event-data-store arn:aws:cloudtrail:`us-east-2`:`111122223333`:eventdatastore/`a1b2c3d4-5678-90ab-cdef-EXAMPLE11111` --max-event-size Large --context-key-selectors
```

2. Repeat this command for every data store in every Region in the partition. For more
   information, see [Identify AWS resources with Amazon Resource Names (ARNs)](../../../IAM/latest/UserGuide/reference-arns.md "../../../IAM/latest/UserGuide/reference-arns.md").

**To manually delete the service-linked role using
IAM**

Use the IAM console, the AWS CLI, or the AWS API to delete the AWSServiceRoleForCloudTrailEventContext service-linked
role. For more information, see [Deleting a service-linked role](../../../IAM/latest/UserGuide/using-service-linked-roles.md#delete-service-linked-role "../../../IAM/latest/UserGuide/using-service-linked-roles.md#delete-service-linked-role") in the _IAM User Guide_.
