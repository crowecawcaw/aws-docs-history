

# Create a security profile in Connect Customer
<a name="create-security-profile"></a>

By creating a security profile, you can grant your users only the permissions that they need.

For each permission group, there is a set of resources and supported set of actions. For example, users are part of the **Users and permissions** group, which supports the following actions: view, edit, create, remove, enable/disable, and edit permission. 

Some actions depend on other actions. When you choose an action that depends on another action, the dependent action is automatically chosen and must also be granted. For example, if you add permission to edit users, we also add permission to view users.

## Required permissions to create security profiles
<a name="create-security-profiles-required-permissions"></a>

Before you can create a new security profile, you must be logged in with a Connect Customer account that has **Security profiles - Create** permissions, as shown in the following image. 

![The users and permissions section of the security profiles page.](http://docs.aws.amazon.com/connect/latest/adminguide/images/SecurityProfile_cloudscape_sp_create.png)


By default, the Connect Customer **Admin** security profile has these permissions.

## How to create security profiles
<a name="how-to-security-profiles-required-permissions"></a>

1. Log in to the Connect Customer admin website at https://{{instance name}}.my.connect.aws/.

1. Choose **Users**, **Security profiles**.

1. Choose **Add new security profile**. The **Create security profile** dialog opens.

1. Enter a name and description for the security profile.

1. Choose **Create**. You are redirected to the **Edit permissions** page where you can configure permissions for the security profile.

1. Choose the appropriate permissions for the security profile from each permission group. For each permission type, choose one or more actions. Selecting some actions results in other actions being selected. For example, selecting **Edit** also selects **View** for the resource and any dependent resources.

1. Choose **Save**.

## Tag-based access controls
<a name="security-profile-tag-based-access-controls"></a>

You can configure tag-based access controls on a security profile. Use these steps to enforce tag-based access controls.

1. On the security profile detail page, choose the **Access control** tab.

1. In the **Tag-based access control** section, choose **Edit**. In the **Resources** box, enter the resources to be restricted using tags.  
![The access control section of the security profile page.](http://docs.aws.amazon.com/connect/latest/adminguide/images/SecurityProfile_cloudscape_access_control_tab.png)

1. Enter the **Key** and **Value** combination for the resource tags that you want to restrict access to.

1. Make sure that you have enabled *View* permissions for the resources that you have selected.

1. Choose **Save**.

**Note**  
It is mandatory to specify both a resource type and an access control tag when configuring tag-based access controls. As a best practice, make sure that you have matching resource tags on a security profile that has tag-based access controls configured. To learn more about tag-based access controls in Connect Customer, see [Apply tag-based access control in Connect Customer](tag-based-access-control.md).

## Tag security profiles
<a name="security-profile-tagging"></a>

You can add resource tags to a security profile. Use these steps to add a resource tag to a security profile.

1. On the security profile detail page, choose the **Tags** tab.

1. Choose **Manage tags**. Enter a **Key** and **Value** combination to tag the resource, as shown in the following image.  
![The tags section of the security profiles page.](http://docs.aws.amazon.com/connect/latest/adminguide/images/SecurityProfile_cloudscape_tags_tab.png)

1. Choose **Save**.

For more information about tagging resources, see [Add tags to resources in Connect Customer](tagging.md).