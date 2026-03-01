# Troubleshooting Notification Codes

The following are notification codes and resolution steps for notifications that you
might see when you set up and use Amazon WorkSpaces Applications. These notifications can be found in the
**Notifications** tab in the WorkSpaces Applications console, after selecting an
image builder or fleet. You can also get fleet notifications by using the WorkSpaces Applications API
operation [DescribeFleets](../APIReference/API_DescribeFleets.md "../APIReference/API_DescribeFleets.md") or the [describe-fleets](../../../cli/latest/reference/appstream/describe-fleets.md "../../../cli/latest/reference/appstream/describe-fleets.md") CLI
command.

## Active Directory Internal Service

Follow these steps if you receive an internal service error when you set up and
use Active Directory with Amazon WorkSpaces Applications.

**INTERNAL_SERVICE_ERROR**

**Message**: The user name or password is incorrect.

**Resolution**: This error might occur
when the computer object that was created in the Microsoft Active
Directory domain for the resource was deleted or disabled. You can
resolve this error by enabling the computer object in the Active
Directory domain, and then starting the resource again. You might also
need to reset the computer object account in the Active Directory
domain. If you continue to encounter this error, contact AWS Support.
For more information, see [AWS Support Center](https://console.aws.amazon.com/support/home#/ "https://console.aws.amazon.com/support/home#/").

## Active Directory Domain Join

The following are notification codes and resolution steps for issues with domain
join that you might encounter when you set up and use Active Directory with
Amazon WorkSpaces Applications.

**DOMAIN_JOIN_ERROR_ACCESS_DENIED**

**Message**: Access is denied.

**Resolution**: The service account
specified in the directory configuration does not have permissions to
create the computer object or reuse an existing one. Validate the
permissions and start the image builder or fleet. For more information,
see [Granting Permissions to Create and Manage Active Directory Computer Objects](active-directory-permissions.md "active-directory-permissions.md").

**DOMAIN_JOIN_ERROR_LOGON_FAILURE**

**Message**: The username or password is
incorrect.

**Resolution**: The service account
specified in the directory configuration has an invalid username or
password. Update the configuration and re-create the image builder or
fleet that had the error.

**DOMAIN_JOIN_NERR_PASSWORD_EXPIRED**

**Message**: The password of this user
has expired.

**Resolution**: The password for the
service account specified in the WorkSpaces Applications directory configuration has
expired. Change the password for the service account in your Active
Directory domain, update the configuration, and then re-create the image
builder or fleet that had the error.

**DOMAIN_JOIN_ERROR_DS_MACHINE_ACCOUNT_QUOTA_EXCEEDED**

**Message**: Your computer could not be
joined to the domain. You have exceeded the maximum number of computer
accounts you are allowed to create in this domain. Contact your system
administrator to have this limit reset or increased.

**Resolution**: The service account
specified on the directory configuration does not have permissions to
create the computer object or reuse an existing one. Validate the
permissions and start the image builder or fleet. For more information,
see [Granting Permissions to Create and Manage Active Directory Computer Objects](active-directory-permissions.md "active-directory-permissions.md").

**DOMAIN_JOIN_ERROR_INVALID_PARAMETER**

**Message**: A parameter is incorrect.
This error is returned if the `LpName` parameter is NULL or the `NameType`
parameter is specified as `NetSetupUnknown` or an unknown nametype.

**Resolution**: This error can occur when
the distinguished name for the OU is incorrect. Validate the OU and try again. If you continue to encounter this error,
contact AWS Support. For more information, see
[AWS Support Center](https://console.aws.amazon.com/support/home#/ "https://console.aws.amazon.com/support/home#/").

**DOMAIN_JOIN_ERROR_MORE_DATA**

**Message**: More data is
available.

**Resolution**: This error can occur when the distinguished
name for the OU is incorrect. Validate the OU and try again. If you continue to encounter this error, contact AWS Support. For more information, see
[AWS Support Center](https://console.aws.amazon.com/support/home#/ "https://console.aws.amazon.com/support/home#/").

**DOMAIN_JOIN_ERROR_NO_SUCH_DOMAIN**

**Message**: The specified domain either
does not exist or could not be contacted.

**Resolution**: The streaming instance
was unable to contact your Active Directory domain. To ensure network
connectivity, confirm your VPC, subnet, and security group settings. For
more information, see [My WorkSpaces Applications streaming instances aren't joining the Active Directory domain.](troubleshooting-active-directory.md#troubleshooting-active-directory-5 "troubleshooting-active-directory.md#troubleshooting-active-directory-5")

**DOMAIN_JOIN_NERR_WORKSTATION_NOT_STARTED**

**Message**: The Workstation service has
not been started.

**Resolution**: An error occurred
starting the Workstation service. Ensure that the service is enabled in
your image. If you continue to encounter this error, contact AWS Support. For
more information, see [AWS Support Center](https://console.aws.amazon.com/support/home#/ "https://console.aws.amazon.com/support/home#/").

**DOMAIN_JOIN_ERROR_NOT_SUPPORTED**

**Message**: The request is not
supported. This error is returned if a remote computer was specified in
the `lpServer` parameter and this call is not supported on the remote
computer.

**Resolution**: Contact AWS Support for
assistance. For more information, see [AWS Support Center](https://console.aws.amazon.com/support/home#/ "https://console.aws.amazon.com/support/home#/").

**DOMAIN_JOIN_ERROR_FILE_NOT_FOUND**

**Message**: The system cannot find the
file specified.

**Resolution**: This error occurs when an
invalid organizational unit (OU) distinguished name is provided.
The distinguished name must start with `OU=`.
Validate the OU distinguished name and try again. For more information, see
[Finding the Organizational Unit Distinguished Name](active-directory-oudn.md "active-directory-oudn.md").

**DOMAIN_JOIN_INTERNAL_SERVICE_ERROR**

**Message**: The account already exists.

**Resolution**: This error can occur in the following scenarios:

- If the issue isn't permissions-related, check the Netdom logs
  for errors and make sure that you provided the correct
  OU.
- The service account specified in the directory configuration
  does not have permissions to create the computer object or reuse
  an existing one. If this is the case, validate the permissions
  and start the image builder or fleet. For more information, see
  [Granting Permissions to Create and Manage Active Directory Computer Objects](active-directory-permissions.md "active-directory-permissions.md").
- After WorkSpaces Applications creates the computer object, it is moved from the
  OU in which it was created. In this case, the first image
  builder or fleet is created successfully, but any new image
  builder or fleet that uses the computer object fails. When
  Active Directory searches for the computer object in the
  specified OU and detects that an object with the same name
  exists elsewhere in the domain, the domain join is not
  successful.
- The name of the OU specified in the WorkSpaces Applications Directory Config
  includes spaces before or after the commas in the directory
  configuration. In this case, when a fleet or image builder
  attempts to rejoin the Active Directory domain, WorkSpaces Applications cannot
  cycle the computer objects correctly and the domain rejoin does
  not succeed. To resolve this issue for a fleet, do the
  following:

      1. Stop the fleet.
      2. Edit the Active Directory domain settings for the
       fleet to remove the Directory Config and Directory OU to
       which the fleet is joined. For more information, see
       [Step 3: Create a Domain-Joined Fleet](active-directory-directory-setup.md#active-directory-setup-fleet "active-directory-directory-setup.md#active-directory-setup-fleet").
      3. Update the WorkSpaces Applications Directory Config to specify an OU
       that doesn't contain spaces. For more information, see
       [Step 1: Create a Directory Config Object](active-directory-directory-setup.md#active-directory-setup-config "active-directory-directory-setup.md#active-directory-setup-config").
      4. Edit the Active Directory domain settings for the
       fleet to specify the Directory Config with the updated
       Directory OU.

  To resolve this issue for an image builder, do the
  following:

      1. Delete the image builder.
      2. Update the WorkSpaces Applications Directory Config to specify an OU
       that doesn't contain spaces. For more information, see
       [Step 1: Create a Directory Config Object](active-directory-directory-setup.md#active-directory-setup-config "active-directory-directory-setup.md#active-directory-setup-config").
      3. Create a new image builder and specify the Directory
       Config with the updated Directory OU. For more
       information, see [Launch an Image Builder to Install and Configure Streaming Applications](tutorial-image-builder-create.md "tutorial-image-builder-create.md").

## Image Internal Service

If you receive an internal service error after you use managed WorkSpaces Applications image
updates to initiate an image update, follow these steps.

**INTERNAL_SERVICE_ERROR**

**Message**: WorkSpaces Applications could not update
image `image-name`. Failed to
update/install/configure/disable <software name>. Check your source
image and try again. If this problem persists, contact AWS Support.

**Resolution**: This error can occur when
there is an issue with the source image. Try to update the image
again.

If updating again doesn't work, make sure that you're using the latest
version of SSM Agent. For version information, see [WorkSpaces Applications Base Image and Managed Image Update Release Notes](base-image-version-history.md "base-image-version-history.md"). For installation
information, see [Manually install SSM Agent on EC2 instances for Windows
Server](../../../systems-manager/latest/userguide/sysman-install-win.md "../../../systems-manager/latest/userguide/sysman-install-win.md").

If the error continues to occur, launch an image builder from the
image. For more information, see [Launch an Image Builder to Install and Configure Streaming Applications](tutorial-image-builder-create.md "tutorial-image-builder-create.md"). If you can't launch image
builder from the image, there is another issue with the image that needs
to be resolved before you can use managed AppStream 2.0 image updates to
update the image. If you continue to encounter this error, contact AWS Support. For more information, see [AWS Support Center](https://console.aws.amazon.com/support/home#/ "https://console.aws.amazon.com/support/home#/").

## Session Provisioning

The following are notification codes and resolution steps for issues with session
provisioning that you might encounter when your end users try to provision the
streaming session.

###### Note

"X" below equals the number of sessions that encountered a given error
code.

**USER_PROFILE_MOUNTING_FAILURE**

**Message**: X session(s) encountered
user profile mounting failures.

**Resolution**: To troubleshoot this
issue, check if any user profiles have been corrupted or if any third
party processes on instance are interfering with user profile mounting.
If you continue to encounter this error, contact AWS Support. For more
information, see [AWS Support Center](https://console.aws.amazon.com/support/home#/ "https://console.aws.amazon.com/support/home#/").

**USER_PROFILE_DOWNLOADING_FAILURE**

**Message**: X session(s) encountered
user profile downloading failures.

**Resolution**: To troubleshoot this
issue, check your network configuration. If you continue to encounter
this error, contact AWS Support. For more information, see
[AWS Support Center](https://console.aws.amazon.com/support/home#/ "https://console.aws.amazon.com/support/home#/").

**HOME_FOLDER_MOUNTING_FAILURE**

**Message**: X session(s) encountered
home folder mounting failures.

**Resolution**: To troubleshoot this
issue, check your network configuration. If you continue to encounter
this error, contact AWS Support. For more information, see
[AWS Support Center](https://console.aws.amazon.com/support/home#/ "https://console.aws.amazon.com/support/home#/").
