

# Enable Profile explorer
<a name="enabling-profile-explorer"></a>

By following these steps, you can enable Profile explorer for your administrators and users. This process involves setting up permissions for both layout configuration and viewing access.

**Topics**
+ [Enable administrators to define a layout](#enable-administrators-define-layout)
+ [Enable users to view Profile Explorer](#enable-users-view-profile-explorer)
+ [Verify Setup](#verify-setup)

## Enable administrators to define a layout
<a name="enable-administrators-define-layout"></a>

Administrators need specific permissions to create and edit Profile explorer layouts:
+ Assign the following permissions within the Profile explorer Security profile:
  + **Profile explorer - Edit**: Allows modification of existing Profile explorer layout.
  + **Profile explorer - Create**: Enables creation of the Profile explorer layout.
  + **Profile explorer - View**: Enables access to view configured Profile explorer layout.  
![Add permissions to allow users to create, edit, and view profile explorer layouts.](http://docs.aws.amazon.com/connect/latest/adminguide/images/enable-administrators-define-layout-1.png)

## Enable users to view Profile Explorer
<a name="enable-users-view-profile-explorer"></a>

Users need appropriate permissions to access and interact with Profile explorer layout:
+ Assign the following permissions within the Profile explorer Security profile:
  + **Profile explorer - View**: Enables access to view configured Profile explorer layout.  
![Add permissions to allow users to view Profile explorer layouts.](http://docs.aws.amazon.com/connect/latest/adminguide/images/enable-users-view-profile-explorer-1.png)

## Verify Setup
<a name="verify-setup"></a>

To confirm that Profile explorer can be successfully enabled:

Log in as an administrator to verify you can:
+ Access the Profile explorer page.
+ Create and modify your Profile explorer layout.

Log in as a regular user to verify you can:
+ Access Profile explorer.
+ View the Profile explorer layout.
+ Interact with enabled features.