# WorkSpaces Pools Active Directory

Administration

Setting up and using Active Directory with WorkSpaces Pools involves the following
administrative tasks.

###### Tasks

- [Granting Permissions to Create and
  Manage Active Directory Computer Objects](#active-directory-permissions "#active-directory-permissions")
- [Finding the Organizational Unit
  Distinguished Name](#active-directory-oudn "#active-directory-oudn")
- [Granting Local
  Administrator Rights on custom images](#active-directory-image-builder-local-admin "#active-directory-image-builder-local-admin")
- [Locking the Streaming Session When
  the User is Idle](#active-directory-session-lock "#active-directory-session-lock")
- [Configuring WorkSpaces Pools to Use
  Domain Trusts](#active-directory-domain-trusts "#active-directory-domain-trusts")

## Granting Permissions to Create and

Manage Active Directory Computer Objects

To allow WorkSpaces Pools to perform Active Directory computer object operations, you
need an account with sufficient permissions. As a best practice, use an account that
has only the minimum privileges necessary. The minimum Active Directory
organizational unit (OU) permissions are as follows:

- Create Computer Object
- Change Password
- Reset Password
- Write Description

Before setting up permissions, you'll need to do the following first:

- Obtain access to a computer or an EC2 instance that is joined to your
  domain.
- Install the Active Directory User and Computers MMC snap-in. For more
  information, see [Installing or Removing Remote Server Administration Tools for Windows
  7](https://technet.microsoft.com/en-us/library/ee449483.aspx "https://technet.microsoft.com/en-us/library/ee449483.aspx") in the Microsoft documentation.
- Log in as a domain user with appropriate permissions to modify the OU
  security settings.
- Create or identify the user, service account, or group for which to
  delegate permissions.

###### To set up minimum permissions

1. Open **Active Directory Users and Computers** in your
   domain or on your domain controller.
2. In the left navigation pane, select the first OU on which to provide
   domain join privileges, open the context (right-click) menu , and then
   choose **Delegate Control**.
3. On the **Delegation of Control Wizard** page, choose
   **Next**, **Add**.
4. For **Select Users, Computers, or Groups**, select the
   pre-created user, service account, or group, and then choose
   **OK**.
5. On the **Tasks to Delegate** page, choose
   **Create a custom task to delegate**, and then choose
   **Next**.
6. Choose **Only the following objects in the folder**,
   **Computer objects**.
7. Choose **Create selected objects in this folder**,
   **Next**.
8. For **Permissions**, choose **Read**,
   **Write**, **Change Password**,
   **Reset Password**, **Next**.
9. On the **Completing the Delegation of Control Wizard**
   page, verify the information and choose **Finish**.
10. Repeat steps 2-9 for any additional OUs that require these
    permissions.

If you delegated permissions to a group, create a user or service account with a
strong password and add that account to the group. This account will then have
sufficient privileges to connect your WorkSpaces to the directory. Use this account when
creating your WorkSpaces Pools directory configuration.

## Finding the Organizational Unit

Distinguished Name

When you register your Active Directory domain with WorkSpaces Pools, you must provide
an organizational unit (OU) distinguished name. Create an OU for this purpose. The
default Computers container is not an OU and cannot be used by WorkSpaces Pools. The
following procedure shows how to obtain this name.

###### Note

The distinguished name must start with `OU=` or it cannot
be used for computer objects.

Before you complete this procedure, you'll need to do the following first:

- Obtain access to a computer or an EC2 instance that is joined to your
  domain.
- Install the Active Directory User and Computers MMC snap-in. For more
  information, see [Installing or Removing Remote Server Administration Tools for Windows
  7](https://technet.microsoft.com/en-us/library/ee449483.aspx "https://technet.microsoft.com/en-us/library/ee449483.aspx") in the Microsoft documentation.
- Log in as a domain user with appropriate permissions to read the OU
  security properties.

###### To find the distinguished name of an OU

1. Open **Active Directory Users and Computers** in your
   domain or on your domain controller.
2. Under **View**, ensure that **Advanced
   Features** is enabled.
3. In the left navigation pane, select the first OU to use for WorkSpaces computer
   objects, open the context (right-click) menu, and then choose
   **Properties**.
4. Choose **Attribute Editor**.
5. Under **Attributes**, for
   **distinguishedName**, choose
   **View**.
6. For **Value**, select the distinguished name, open the
   context menu, and then choose **Copy**.

## Granting Local

Administrator Rights on custom images

By default, Active Directory domain users do not have local administrator rights
on images. You can grant these rights by using Group Policy preferences in your
directory, or manually, by using the local administrator account on an image.
Granting local administrator rights to a domain user allows that user to install
applications on and create custom images in WorkSpaces Pools.

###### Contents

- [Using Group Policy preferences](#group-policy "#group-policy")
- [Using the local Administrators group on the
  WorkSpace to create images](#manual-procedure "#manual-procedure")

### Using Group Policy preferences

You can use Group Policy preferences to grant local administrator rights to
Active Directory users or groups and to all computer objects in the specified
OU. The Active Directory users or groups to which you want to grant local
administrator permissions must already exist. To use Group Policy preferences,
you'll need to do the following first:

- Obtain access to a computer or an EC2 instance that is joined to your
  domain.
- Install the Group Policy Management Console (GPMC) MMC snap-in. For
  more information, see [Installing or Removing Remote Server Administration Tools for
  Windows 7](https://technet.microsoft.com/en-us/library/ee449483.aspx "https://technet.microsoft.com/en-us/library/ee449483.aspx") in the Microsoft documentation.
- Log in as a domain user with permissions to create Group Policy
  objects (GPOs). Link GPOs to the appropriate OUs.

###### To use Group Policy preferences to grant local administrator

permissions

1. In your directory or on a domain controller, open the command prompt
   as an administrator, type `gpmc.msc`, and then press
   ENTER.
2. In the left console tree, select the OU where you will create a new
   GPO or use an existing GPO, and then do either of the following:
   - Create a new GPO by opening the context (right-click) menu and
     choosing **Create a GPO in this domain, Link it
     here**. For **Name**, provide a
     descriptive name for this GPO.
   - Select an existing GPO.

3. Open the context menu for the GPO, and choose
   **Edit**.
4. In the console tree, choose **Computer
   Configuration**, **Preferences**,
   **Windows Settings**, **Control Panel
   Settings**, and **Local Users and
   Groups**.
5. Select **Local Users and Groups** selected, open the
   context menu , and choose **New**, **Local
   Group**.
6. For **Action**, choose
   **Update**.
7. For **Group name**, choose **Administrators
   (built-in)**.
8. Under **Members**, choose **Add…**
   and specify the Active Directory users or groups to which to assign
   local administrator rights on the streaming instance. For
   **Action**, choose **Add to this
   group**, and choose **OK**.
9. To apply this GPO to other OUs, select the additional OU, open the
   context menu and choose **Link an Existing
   GPO**.
10. Using the new or existing GPO name that you specified in step 2,
    scroll to find the GPO, and then choose **OK**.
11. Repeat steps 9 and 10 for additional OUs that should have this
    preference.
12. Choose **OK** to close the **New Local Group
    Properties** dialog box.
13. Choose **OK** again to close the GPMC.

To apply the new preference to the GPO, you must stop and restart any running
image builders or fleets. The Active Directory users and groups that you
specified in step 8 are automatically granted local administrator rights on the
image builders and fleets in the OU to which the GPO is linked.

### Using the local Administrators group on the

WorkSpace to create images

To grant Active Directory users or groups local administrator rights on an
image, you can manually add these users or groups to the local Administrators
group on the image.

The Active Directory users or groups to which to grant local administrator
rights must already exist.

1. Connect to the WorkSpace you use to build images. The WorkSpace must
   be running and domain-joined.
2. Choose **Start**, **Administrative
   Tools**, and then double-click **Computer
   Management**.
3. In the left navigation pane, choose **Local Users and
   Groups** and open the **Groups**
   folder.
4. Open the **Administrators** group and choose
   **Add...**.
5. Select all Active Directory users or groups to which to assign local
   administrator rights and choose **OK**. Choose
   **OK** again to close the **Administrator
   Properties** dialog box.
6. Close Computer Management.
7. To log in as an Active Directory user and test whether that user has
   local administrator rights on the WorkSpaces, choose **Admin
   Commands**, **Switch user**, and then
   enter the credentials of the relevant user.

## Locking the Streaming Session When

the User is Idle

WorkSpaces Pools relies on a setting that you configure in the GPMC to lock the
streaming session after your user is idle for specified amount of time. To use the
GPMC, you'll need to do the following first:

- Obtain access to a computer or an EC2 instance that is joined to your
  domain.
- Install the GPMC. For more information, see [Installing or Removing Remote Server Administration Tools for Windows
  7](https://technet.microsoft.com/en-us/library/ee449483.aspx "https://technet.microsoft.com/en-us/library/ee449483.aspx") in the Microsoft documentation.
- Log in as a domain user with permissions to create GPOs. Link GPOs to the
  appropriate OUs.

###### To automatically lock the streaming instance when your user is idle

1. In your directory or on a domain controller, open the command prompt as an
   administrator, type `gpmc.msc`, and then press ENTER.
2. In the left console tree, select the OU where you will create a new GPO or
   use an existing GPO, and then do either of the following:
   - Create a new GPO by opening the context (right-click) menu and
     choosing **Create a GPO in this domain, Link it
     here**. For **Name**, provide a
     descriptive name for this GPO.
   - Select an existing GPO.

3. Open the context menu for the GPO, and choose
   **Edit**.
4. Under **User Configuration**, expand
   **Policies**, **Administrative
   Templates**, **Control Panel**, and then
   choose **Personalization**.
5. Double-click **Enable screen saver**.
6. In the **Enable screen saver** policy setting, choose
   **Enabled**.
7. Choose **Apply**, and then choose
   **OK**.
8. Double-click **Force specific screen saver**.
9. In the **Force specific screen saver** policy setting,
   choose **Enabled**.
10. Under **Screen saver executable name**, enter
    `scrnsave.scr`. When this setting is enabled, the
    system displays a black screen saver on the user's desktop.
11. Choose **Apply**, and then choose
    **OK**.
12. Double-click **Password protect the screen
    saver**.
13. In the **Password protect the screen saver** policy
    setting, choose **Enabled**.
14. Choose **Apply**, and then choose
    **OK**.
15. Double-click **Screen saver timeout**.
16. In the **Screen saver timeout** policy setting, choose
    **Enabled**.
17. For **Seconds**, specify the length of time that users
    must be idle before the screen saver is applied. To set the idle time to 10
    minutes, specify 600 seconds.
18. Choose **Apply**, and then choose
    **OK**.
19. In the console tree, under **User Configuration**, expand
    **Policies**, **Administrative
    Templates**, **System**, and then choose
    **Ctrl+Alt+Del Options**.
20. Double-click **Remove Lock Computer**.
21. In the **Remove Lock Computer** policy setting, choose
    **Disabled**.
22. Choose **Apply**, and then choose
    **OK**.

## Configuring WorkSpaces Pools to Use

Domain Trusts

WorkSpaces Pools supports Active Directory domain environments where network resources
such as file servers, applications, and computer objects reside in one domain, and
the user objects reside in another. The domain service account used for computer
object operations does not need to be in the same domain as the WorkSpaces Pools computer
objects.

When creating the directory configuration, specify a service account that has the
appropriate permissions to manage computer objects in the Active Directory domain
where the file servers, applications, computer objects and other network resources
reside.

Your end user Active Directory accounts must have the "Allowed to Authenticate"
permissions for the following:

- WorkSpaces Pools computer objects
- Domain controllers for the domain

For more information, see [Granting Permissions to Create and
Manage Active Directory Computer Objects](#active-directory-permissions "#active-directory-permissions").
