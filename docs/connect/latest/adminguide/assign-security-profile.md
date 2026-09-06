

# Assign a security profile for Connect Customer to a contact center user
<a name="assign-security-profile"></a>

## Required permissions to assign security profiles
<a name="assign-security-profiles-required-permissions"></a>

Before you can assign a security profile to a user, you must be logged in with an Connect Customer account that has the **Users - Edit** permission, as shown in the following image. Or, if you're creating the user's account for the first time, you need **Users - Create** permission. 

![The users and permissions section of the security profiles page.](http://docs.aws.amazon.com/connect/latest/adminguide/images/SecurityProfile_cloudscape_users_edit.png)


By default, the Connect Customer **Admin** security profile has these permissions.

## How to assign security profiles
<a name="how-to-assign-security-profiles"></a>

1. Review [Best practices for Connect Customer and Contact Control Panel (CCP) security profiles](security-profile-best-practices.md).

1. Log in to the Connect Customer admin website at https://{{instance name}}.my.connect.aws/.

1. Choose **Users**, **User management**.

1. Select one or more users and choose **Edit**.

1. For **Security Profiles**, add or remove security profiles as needed. To add a security profile, put your cursor in the field and select the security profile from the list. To remove a security profile, choose the **x** next to its name. 

1. Choose **Save**.