

# Using service-linked roles for AWS Clean Rooms
<a name="using-service-linked-roles"></a>

AWS Clean Rooms uses AWS Identity and Access Management (IAM) [service-linked roles](https://docs.aws.amazon.com/IAM/latest/UserGuide/id_roles_terms-and-concepts.html#iam-term-service-linked-role). A service-linked role is a unique type of IAM role that is linked directly to AWS Clean Rooms. Service-linked roles are predefined by AWS Clean Rooms and include all the permissions that the service requires to call other AWS services on your behalf.

A service-linked role makes setting up AWS Clean Rooms easier because you don’t have to manually add the necessary permissions. AWS Clean Rooms defines the permissions of its service-linked roles, and unless defined otherwise, only AWS Clean Rooms can assume its roles. The defined permissions include the trust policy and the permissions policy, and that permissions policy cannot be attached to any other IAM entity.

You can delete a service-linked role only after first deleting their related resources. This protects your AWS Clean Rooms resources because you can't inadvertently remove permission to access the resources.

For information about other services that support service-linked roles, see [AWS services that work with IAM](https://docs.aws.amazon.com/IAM/latest/UserGuide/reference_aws-services-that-work-with-iam.html) and look for the services that have **Yes** in the **Service-linked roles** column. Choose a **Yes** with a link to view the service-linked role documentation for that service.

## Service-linked role permissions for AWS Clean Rooms
<a name="slr-permissions"></a>

AWS Clean Rooms uses the service-linked role named **AWSServiceRoleForAWSCleanRooms** – to publish Clean Rooms-related CloudWatch metrics to your AWS account.

The AWSServiceRoleForAWSCleanRooms service-linked role trusts the following services to assume the role:
+ `cleanrooms.amazonaws.com`

The role permissions policy named AWSCleanRoomsServiceRolePolicy allows AWS Clean Rooms to complete the following actions on the specified resources:
+ Action: `cloudwatch:PutMetricData` on `all AWS resources, restricted to the AWS Clean Rooms namespace`

You must configure permissions to allow your users, groups, or roles to create, edit, or delete a service-linked role. For more information, see [Service-linked role permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/using-service-linked-roles.html#service-linked-role-permissions) in the *IAM User Guide*.

## Creating a service-linked role for AWS Clean Rooms
<a name="create-slr"></a>

You can use the IAM console to create a service-linked role with the **AWSServiceRoleForAWSCleanRooms** use case. In the AWS CLI or the AWS API, create a service-linked role with the `cleanrooms.amazonaws.com` service name. For more information, see [Creating a service-linked role](https://docs.aws.amazon.com/IAM/latest/UserGuide/using-service-linked-roles.html#create-service-linked-role) in the *IAM User Guide*. If you delete this service-linked role, you can use this same process to create the role again.

## Editing a service-linked role for AWS Clean Rooms
<a name="edit-slr"></a>

AWS Clean Rooms does not allow you to edit the AWSServiceRoleForAWSCleanRooms service-linked role. After you create a service-linked role, you cannot change the name of the role because various entities might reference the role. However, you can edit the description of the role using IAM. For more information, see [Editing a service-linked role](https://docs.aws.amazon.com/IAM/latest/UserGuide/using-service-linked-roles.html#edit-service-linked-role) in the *IAM User Guide*.

## Deleting a service-linked role for AWS Clean Rooms
<a name="delete-slr"></a>

If you no longer need to use a feature or service that requires a service-linked role, we recommend that you delete that role. That way you don’t have an unused entity that is not actively monitored or maintained. However, you must clean up the resources for your service-linked role before you can manually delete it.

To delete the **AWSServiceRoleForAWSCleanRooms**, you must first delete all [collaborations](https://docs.aws.amazon.com/clean-rooms/latest/userguide/delete-collaboration.html) and [memberships](https://docs.aws.amazon.com/clean-rooms/latest/userguide/leave-collab.html) in your AWS account.

**Note**  
If the AWS Clean Rooms service is using the role when you try to delete the resources, then the deletion might fail. If that happens, wait for a few minutes and try the operation again.

**To manually delete the service-linked role using IAM**

Use the IAM console, the AWS CLI, or the AWS API to delete the AWSServiceRoleForAWSCleanRooms service-linked role. For more information, see [Deleting a service-linked role](https://docs.aws.amazon.com/IAM/latest/UserGuide/using-service-linked-roles.html#delete-service-linked-role) in the *IAM User Guide*.

## Supported Regions for AWS Clean Rooms service-linked roles
<a name="slr-regions"></a>

AWS Clean Rooms supports using service-linked roles in all of the Regions where the service is available. For more information, see [AWS Regions and endpoints](https://docs.aws.amazon.com/general/latest/gr/clean-rooms.html#clean-rooms_region).