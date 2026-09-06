

# Using roles to create secrets for API destinations in EventBridge
<a name="using-service-linked-roles-service-action-1"></a>

The following topic details usage of the ****AWSServiceRoleForAmazonEventBridgeApiDestinations**** service-linked role.

## Service-linked role permissions for EventBridge
<a name="service-linked-role-permissions-service-action-1"></a>

EventBridge uses the service-linked role named ****AWSServiceRoleForAmazonEventBridgeApiDestinations**** – Enables access to the Secrets Manager Secrets created by EventBridge.

The **AWSServiceRoleForAmazonEventBridgeApiDestinations** service-linked role trusts the following services to assume the role:
+ `apidestinations.events.amazonaws.com`

The role permissions policy named **AmazonEventBridgeApiDestinationsServiceRolePolicy** allows EventBridge to complete the following actions on the specified resources:
+ Action: `create, describe, update and delete secrets; get and put secret values` on `secrets created for all connections by EventBridge`

You must configure permissions to allow your users, groups, or roles to create, edit, or delete a service-linked role. For more information, see [Service-linked role permissions](https://docs.aws.amazon.com/IAM/latest/UserGuide/using-service-linked-roles.html#service-linked-role-permissions) in the *IAM User Guide*.

## Creating a service-linked role for EventBridge
<a name="create-service-linked-role-service-action-1"></a>

You don't need to manually create a service-linked role. When you create a connection in the AWS Management Console, the AWS CLI, or the AWS API, EventBridge creates the service-linked role for you. 

**Important**  
 This service-linked role can appear in your account if you completed an action in another service that uses the features supported by this role. If you were using the EventBridge service before February 11, 2021, when it began supporting service-linked roles, then EventBridge created the **AWSServiceRoleForAmazonEventBridgeApiDestinations** role in your account. To learn more, see [A new role appeared in my AWS account](https://docs.aws.amazon.com/IAM/latest/UserGuide/troubleshoot_roles.html#troubleshoot_roles_new-role-appeared).

If you delete this service-linked role, and then need to create it again, you can use the same process to recreate the role in your account. When you create a connection, EventBridge creates the service-linked role for you again. 

## Editing a service-linked role for EventBridge
<a name="edit-service-linked-role-service-action-1"></a>

EventBridge does not allow you to edit the **AWSServiceRoleForAmazonEventBridgeApiDestinations** service-linked role. After you create a service-linked role, you cannot change the name of the role because various entities might reference the role. However, you can edit the description of the role using IAM. For more information, see [Editing a service-linked role](https://docs.aws.amazon.com/IAM/latest/UserGuide/using-service-linked-roles.html#edit-service-linked-role) in the *IAM User Guide*.

## Deleting a service-linked role for EventBridge
<a name="delete-service-linked-role-service-action-1"></a>

If you no longer need to use a feature or service that requires a service-linked role, we recommend that you delete that role. That way you don’t have an unused entity that is not actively monitored or maintained. However, you must clean up your service-linked role before you can manually delete it.

### Cleaning up a service-linked role
<a name="service-linked-role-review-before-delete-service-action-1"></a>

Before you can use IAM to delete a service-linked role, you must first delete any resources used by the role.

**Note**  
If the EventBridge service is using the role when you try to delete the resources, then the deletion might fail. If that happens, wait for a few minutes and try the operation again.

**To delete EventBridge resources used by the **AWSServiceRoleForAmazonEventBridgeApiDestinations** (console)**

1. Open the Amazon EventBridge console at [https://console.aws.amazon.com/events/](https://console.aws.amazon.com/events/).

1. Under **Integrations** choose **API destinations**, then choose the **Connections** tab.

1. Choose the connection, then choose **Delete**.

**To delete EventBridge resources used by the **AWSServiceRoleForAmazonEventBridgeApiDestinations** (AWS CLI)**
+ Use the following command: `[delete-connection](https://awscli.amazonaws.com/v2/documentation/api/latest/reference/events/delete-connection.html)`.

**To delete EventBridge resources used by the **AWSServiceRoleForAmazonEventBridgeApiDestinations** (API)**
+ Use the following command: `[DeleteConnection](https://docs.aws.amazon.com/eventbridge/latest/APIReference/API_DeleteConnection.html)`.

### Manually delete the service-linked role
<a name="slr-manual-delete-service-action-1"></a>

Use the IAM console, the AWS CLI, or the AWS API to delete the **AWSServiceRoleForAmazonEventBridgeApiDestinations** service-linked role. For more information, see [Deleting a service-linked role](https://docs.aws.amazon.com/IAM/latest/UserGuide/using-service-linked-roles.html#delete-service-linked-role) in the *IAM User Guide*.

## Supported Regions for EventBridge service-linked roles
<a name="slr-regions-service-action-1"></a>

EventBridge supports using service-linked roles in all of the Regions where the service is available. For more information, see [AWS Regions and endpoints](https://docs.aws.amazon.com/general/latest/gr/rande.html).