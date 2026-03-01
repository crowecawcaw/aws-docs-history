# Creating Default Application Settings for Your Users

Follow these steps to create default application settings for your users.

###### Contents

- [Step 1: Install Linux Applications on the Image Builder](#app-settings-image-install "#app-settings-image-install")
- [Step 2: Create a TemplateUser Account](#app-settings-template-user "#app-settings-template-user")
- [Step 3: Create Default Application Settings](#app-settings-image-create-default-app-settings "#app-settings-image-create-default-app-settings")
- [Step 4: Save Default Application Settings](#app-settings-image-save-default-app-settings "#app-settings-image-save-default-app-settings")
- [Step 5: Test Default Application Settings (optional)](#app-settings-image-test-applications "#app-settings-image-test-applications")
- [Step 6: Clean Up](#app-settings-image-finish "#app-settings-image-finish")

## Step 1: Install Linux Applications on the Image Builder

In this step, you connect a Linux image builder and install your applications on
the image builder.

###### To install applications on the image builder

1. Connect to the image builder by doing either of the following:
   - [Use the
     WorkSpaces Applications console](managing-image-builders-connect-console.md "managing-image-builders-connect-console.md") (for web connections only)
   - [Create a streaming URL](managing-image-builders-connect-streaming-URL.md "managing-image-builders-connect-streaming-URL.md") (for web or WorkSpaces Applications client
     connections)

   ###### Note

   You will be logged in as an ImageBuilderAdmin user to the
   Amazon Linux GNOME desktop and have root admin
   privileges.

2. Install the applications that you need. For example, to install a Chromium
   browser from a public yum repo, first open the Terminal application, then
   run the following command:

**[ImageBuilderAdmin]$ sudo yum update && sudo yum install
chromium.x86_64**

## Step 2: Create a TemplateUser Account

In this step, you create a TemplateUser account, which creates default application
settings for your streaming users.

###### To create a TemplateUser Account

1. Create a TemplateUser account that has no root permissions. For example,
   in a Terminal window, run the following commands to create TemplateUser on
   the image builder:

**[ImageBuilderAdmin]$ sudo useradd -m TemplateUser**

**[ImageBuilderAdmin]$ echo -e
'<`password`>\n<`password`>\n'
| sudo passwd TemplateUser** 2. Switch to the TemplateUser account:

**[ImageBuilderAdmin]$ su - TemplateUser**

## Step 3: Create Default Application Settings

In this step, you create default application settings for your WorkSpaces Applications users. Doing
this enables your users to get started with applications quickly during their WorkSpaces Applications
streaming sessions, without the need to create or configure these settings
themselves.

###### To create default application settings for your users

1. Launch the application that you want to create the default settings for.
   For example, in a Terminal window, run following command to launch Chromium
   browser:

**[TemplateUser]$ chromium-browser** 2. Configure the settings of the application. For example, set the home page
of the Chromium browser as
`https://aws.amazon.com`. 3. Close the applications. 4. Log out:

**[TemplateUser]$ logout**

## Step 4: Save Default Application Settings

In this step, you copy the default application settings you added to the
**/etc/skel/** directory, and make them available to your
streaming users.

###### To save default application settings

- Run the following command in a Terminal window to copy the default
  application settings for your streaming users:

**[ImageBuilderAdmin]$ sudo cp -r -f /home/TemplateUser/.
/etc/skel**

## Step 5: Test Default Application Settings (optional)

In this step, verify that the applications you've added run correctly, and the
default application settings work as expected.

###### To test your applications and default settings on an image builder

1. Create a test user that has no root permissions. For example, in a
   **Terminal** window, run the following commands to
   create **test-user** on the image builder:

**[ImageBuilderAdmin]$ sudo useradd -m test-user**

**[ImageBuilderAdmin]$ echo -e
'`password`>\n<`password`>\n'
| sudo passwd test-user** 2. Switch to the test user:

**[ImageBuilderAdmin]$ su - test-user** 3. Launch the application (e.g., Chromium) as the test user:

**[test-user]$ /usr/bin/chromium-browser** 4. Verify that the default settings are available for the test user (e.g.,
the Chromium home page is https://aws.amazon.com/). 5. Log out:

**[test-user]$ logout**

## Step 6: Clean Up

Finally, your last step is to clean up.

###### To clean up

1. Delete TemplateUser:

**[ImageBuilderAdmin]$ sudo killall -u
TemplateUser**

**[ImageBuilderAdmin]$ sudo userdel -r
TemplateUser** 2. Delete test-user (not required if you skipped step 5):

**[ImageBuilderAdmin]$ sudo killall -u test-user**

**ImageBuilderAdmin]$ sudo userdel -r test-user**
