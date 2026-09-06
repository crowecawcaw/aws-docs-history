

# Using roles for schema discovery in Amazon EventBridge
<a name="using-service-linked-roles-service-action-2"></a>

The following topic details usage of the ****AWSServiceRoleForSchemas**** service-linked role.

## Service-linked role permissions for EventBridge
<a name="service-linked-role-permissions-service-action-2"></a>

EventBridge uses the service-linked role named ****AWSServiceRoleForSchemas**** – Grants permissions to Managed Rules created by Amazon EventBridge schemas..

The **AWSServiceRoleForSchemas** service-linked role trusts the following services to assume the role:
+ `schemas.amazonaws.com`

The role permissions policy named ****AmazonEventBridgeSchemasServiceRolePolicy**** allows EventBridge to complete the following actions on the specified resources:
+ Action: `put, enable, disable, and delete rules; put and remove targets; list targets per rule` on `all managed rules created by EventBridge`

You must configure permissions to allow your users, groups, or roles to create, edit, or delete a service-linked role. For more information, see [Service-linked role permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/using-service-linked-roles.html#service-linked-role-permissions) in the *IAM User Guide*.

## Creating a service-linked role for EventBridge
<a name="create-service-linked-role-service-action-2"></a>

You don't need to manually create a service-linked role. When you conduct a Schema Discovery in the AWS Management Console, the AWS CLI, or the AWS API, EventBridge creates the service-linked role for you. 

**Important**  
 This service-linked role can appear in your account if you completed an action in another service that uses the features supported by this role. If you were using the EventBridge service before November 27, 2019, when it began supporting service-linked roles, then EventBridge created the **AWSServiceRoleForSchemas** role in your account. To learn more, see [A new role appeared in my AWS account](https://docs.aws.amazon.com/IAM/latest/UserGuide/troubleshoot_roles.html#troubleshoot_roles_new-role-appeared).

If you delete this service-linked role, and then need to create it again, you can use the same process to recreate the role in your account. When you conduct a Schema Discovery, EventBridge creates the service-linked role for you again. 

## Editing a service-linked role for EventBridge
<a name="edit-service-linked-role-service-action-2"></a>

EventBridge does not allow you to edit the **AWSServiceRoleForSchemas** service-linked role. After you create a service-linked role, you cannot change the name of the role because various entities might reference the role. However, you can edit the description of the role using IAM. For more information, see [Editing a service-linked role](https://docs.aws.amazon.com/IAM/latest/UserGuide/using-service-linked-roles.html#edit-service-linked-role) in the *IAM User Guide*.

## Deleting a service-linked role for EventBridge
<a name="delete-service-linked-role-service-action-2"></a>

If you no longer need to use a feature or service that requires a service-linked role, we recommend that you delete that role. That way you don’t have an unused entity that is not actively monitored or maintained. However, you must clean up your service-linked role before you can manually delete it.

### Cleaning up a service-linked role
<a name="service-linked-role-review-before-delete-service-action-2"></a>

Before you can use IAM to delete a service-linked role, you must first delete any resources used by the role.

**Note**  
If the EventBridge service is using the role when you try to delete the resources, then the deletion might fail. If that happens, wait for a few minutes and try the operation again.

**To delete EventBridge resources used by the **AWSServiceRoleForSchemas** (console)**

1. Open the Amazon EventBridge console at [https://console.aws.amazon.com/events/](https://console.aws.amazon.com/events/).

1. Under **Buses** choose **Event buses**, then choose an event bus.

1. Choose **Stop discovery**.

**To delete EventBridge resources used by the **AWSServiceRoleForSchemas** (AWS CLI)**
+ Use the following command: `[delete-discoverer](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/events/delete-discoverer.html)`.

**To delete EventBridge resources used by the **AWSServiceRoleForSchemas** (API)**
+ Use the following command: `[DeleteDiscoverer](https://docs.aws.amazon.com/eventbridge/latest/schema-reference/v1-discoverers-id-discovererid.html#DeleteDiscoverer)`.

### Manually delete the service-linked role
<a name="slr-manual-delete-service-action-2"></a>

Use the IAM console, the AWS CLI, or the AWS API to delete the **AWSServiceRoleForSchemas** service-linked role. For more information, see [Deleting a service-linked role](https://docs.aws.amazon.com/IAM/latest/UserGuide/using-service-linked-roles.html#delete-service-linked-role) in the *IAM User Guide*.

## Supported Regions for EventBridge service-linked roles
<a name="slr-regions-service-action-2"></a>

EventBridge supports using service-linked roles in all of the Regions where the service is available. For more information, see [AWS Regions and endpoints](https://docs.aws.amazon.com/general/latest/gr/rande.html).