# Tutorial: Create a Custom Linux-Based WorkSpaces Applications Image

This tutorial describes how to create a custom Linux-based Amazon WorkSpaces Applications image that contains
applications which you can stream to your users.

###### Important

Don't create a user named "as2-streaming-user" in your image builder. This is a
reserved username for Fleet. If you create this username outside of the WorkSpaces Applications workflow,
you might experience streaming issues in Fleets.

###### Contents

- [Step 1: Install Linux Applications on the Image Builder](#tutorial-linux-image-install "#tutorial-linux-image-install")
- [Step 2: Generate Application Optimization Manifest File](#tutorial-linux-image-manifest "#tutorial-linux-image-manifest")
- [Step 3: Create an WorkSpaces Applications Application Catalog](#tutorial-linux-image-catalog "#tutorial-linux-image-catalog")
- [Step 4: Create Default Application Settings and Environment Variables](#tutorial-linux-image-create-default-app-settings "#tutorial-linux-image-create-default-app-settings")
- [Step 5: Test Applications and Settings](#tutorial-linux-image-test-applications "#tutorial-linux-image-test-applications")
- [Step 6: Finish Creating Your Image](#tutorial-linux-image-finish-create-image "#tutorial-linux-image-finish-create-image")
- [Step 7 (Optional): Tag and Copy an Image](#tutorial-linux-image-tag-copy "#tutorial-linux-image-tag-copy")
- [Step 8: Clean Up](#tutorial-linux-image-finish "#tutorial-linux-image-finish")

## Step 1: Install Linux Applications on the Image Builder

In this step, you connect a Linux image builder and install your applications on the
image builder.

###### To install applications on the image builder

1. Connect to the image builder by doing either of the following:
   - [Use the WorkSpaces Applications console](managing-image-builders-connect-console.md "managing-image-builders-connect-console.md") (for web connections only)
   - [Create a streaming URL](managing-image-builders-connect-streaming-URL.md "managing-image-builders-connect-streaming-URL.md") (for web or WorkSpaces Applications client connections)

   ###### Note

   You will be logged in as an ImageBuilderAdmin user to the Amazon
   Linux GNOME desktop and have root admin privileges.

2. Install the applications that you need. For example, to install a Chromium
   browser from a public yum repo, first open the Terminal application, then run
   the following command:

**[ImageBuilderAdmin]$ sudo yum update && sudo yum install
chromium.x86_64**

###### Note

Download and install applications only from sites that you trust.

## Step 2: Generate Application Optimization Manifest File

In this step, you generate a manifest file for each application you installed in step

1.

###### To generate a manifest file for optimizing the launch performance of an application

1. Make sure the application (e.g., Chromium) that you are trying to optimize is
   launched and running.
2. In a Terminal window, run the following command to list processes related to
   the application:

**[ImageBuilderAdmin]$ ps -ef | grep chromium** 3. Find the root parent PID from the output of the command above. The following
is an example output, and the root parent PID is 16712:

###### Example

```
[ImageBuilderAdmin]$ ps -ef | grep chromium

ImageBu+ 16712 4128 0 Aug26 ? 00:00:44 /usr/lib64/chromium- browser/chromium-browser --enable-plugins --enable-extensions -- enable-user- scripts --enable-printing --enable-gpu-rasterization -- enable-sync --auto-ssl- client-auth

ImageBu+ 16726 16712 0 Aug26 ? 00:00:00 /usr/lib64/chromium- browser/chromium-browser --type=zygote --no-zygote-sandbox ImageBu+ 16727 16712 0 Aug26 ? 00:00:00 /usr/lib64/chromium- browser/chromium- browser --type=zygote

ImageBu+ 16731 16727 0 Aug26 ? 00:00:00 /usr/lib64/chromium- browser/chromium-browser --type=zygot
```

4. Keep the application running and make sure to use the initial components
   required by your users. This ensures that these components are captured by the
   optimization process.
5. Create script file (e.g., `~/getfilestool.sh`) with the
   following content:

```
#!/bin/bash
## usage getfilestool.sh $pid
lsof -p $(pstree -p $1 | grep -o '([0-9]\+)' | grep -o '[0-9]\+' | tr '\012' ,)|grep REG | sed -n '1!p' | awk '{print $9}'|awk 'NF'
```

6. Verify that the file can be run by running the following command:

**[ImageBuilderAdmin]$ chmod u+x ~/getfilestool.sh** 7. Run the following command to capture all running files from the root parent
process found in step 3 above, and save it to a temporary manifest file:

**[ImageBuilderAdmin]$ sudo ~/getfilestool.sh 16712 >
/tmp/chromium-manifest.txt** 8. Verify the content of the optimization manifest, which is a line-delimited
text file for each application.

## Step 3: Create an WorkSpaces Applications Application Catalog

In this step, you use the CLI tool `AppStreamImageAssistant` on the
image builder to create an WorkSpaces Applications application catalog by specifying applications
for your image. For each application that you plan to stream, you can specify the name,
display name, executable ﬁle to launch, and icon to display.

###### To create an WorkSpaces Applications application catalog

1. From the image builder desktop, open **Terminal** either from
   the side panel or by opening the app grid.
2. Run **AppStreamImageAssistant --help** to see the list of
   available commands. You will use these commands to add applications and create
   an Image.
3. Run the following command to add an installed application (e.g., Chromium) to
   the application list for WorkSpaces Applications users:

```
AppStreamImageAssistant add-application \
 --name Chromium \
 --absolute-app-path /usr/lib64/chromium-browser/chromium-browser \
 --display-name Chromium \
 --absolute-icon-path /usr/share/icons/hicolor/256x256/apps/chromium-browser.png \
 --absolute-manifest-path /tmp/chromium-manifest.txt
```

Alternatively, run the following command:

```
AppStreamImageAssistant add-application \
 --name="Chromium" \
 --absolute-app-path="/usr/lib64/chromium-browser/chromium-browser" \
 --display-name="Chromium" \
 --absolute-icon-path="/usr/share/icons/hicolor/256x256/apps/chromium-browser.png" \
 --absolute-manifest-path="/tmp/chromium-manifest.txt"
```

4. To add more applications, repeat step 3 for each additional
   application.
5. To see the list of applications that have been added in the catalog, along
   with metadata like icon paths and launch parameters, run the following
   command:

**AppStreamImageAssistant list-applications** 6. To remove applications from the catalog, run the following command:

**AppStreamImageAssistant remove-application –-name
`application_name`**

## Step 4: Create Default Application Settings and Environment Variables

In this step, you create default application settings and environment variables for your
WorkSpaces Applications users. Doing this enables your users to get started with applications quickly
during their WorkSpaces Applications streaming sessions, without the need to create or configure these
settings themselves.

###### To create default application and environment variables for your users

1. Launch the application that you want create the default settings for. For
   example, in a Terminal window, run following command to launch Chromium
   browser:

**[ImageBuilderAdmin]$ chromium-browser** 2. Configure the settings of the application. For example, set the home page of
the Chromium browser as `https://aws.amazon.com`. 3. Make sure the Chromium application is closed, and then run the following
commands to copy the configuration for Chromium to
**/etc/skel**:

**[ImageBuilderAdmin]$ sudo mkdir /etc/skel/.config**

**[ImageBuilderAdmin]$ sudo cp -R ~/.config/chromium
/etc/skel/.config** 4. Set the environment variables and add it to the script file. For example, run
the following commands:

**[ImageBuilderAdmin]$ echo "export
`FOO`=`BAR`" | sudo
tee -a /etc/profile.d/myenvvars.sh**

**[ImageBuilderAdmin]$ sudo chmod +x
/etc/profile.d/myenvvars.sh**

## Step 5: Test Applications and Settings

In this step, verify that the applications you've added run correctly, and the
default application settings and environment variables work as expected.

###### To test your applications and default settings on an image builder

1. Create a test user that has no root permissions. For example, in a
   **Terminal** window, run the following commands to create
   **test-user** on the image builder:

**[ImageBuilderAdmin]$ sudo useradd -m test-user**

**[ImageBuilderAdmin]$ echo -e 'Pa55w0rdas2!!!\nPa55w0rdas2!!!\n' |
sudo passwd test-user** 2. Switch to the test user:

**[ImageBuilderAdmin]$ su - test-user** 3. Launch the application (e.g., Chromium) as the test user:

**[test-user]$ /usr/bin/chromium-browser** 4. Verify that the default settings are available for the test user (e.g., the
Chromium home page is https://aws.amazon.com/). 5. Verify that the environment variables are available for the test user. For
example, run the following command:

**[test-user]$ echo $`FOO`**

This command should display the output
**`BAR`** in the terminal. 6. Run the following commands to delete the test user before creating an image
from this image builder:

**# logout test user**

**[test-user]$ logout**

**# kill test user's running processes**

**[ImageBuilderAdmin]$ sudo killall -u test-user**

**# delete user**

**[ImageBuilderAdmin]$ sudo userdel -r test-user**

## Step 6: Finish Creating Your Image

In this step, choose an image name and finish creating your image.

###### To create the image

1. In a **Terminal** window, create an image from your Image
   Builder by running **AppStreamImageAssistant create-image**. This
   image contains your installed and registered applications, plus any session
   scripts and default application settings that you have configured.

To see the list of available options, run **AppStreamImageAssistant
create-image --help**. For more information, see the
**create-image** operation in [Create Your Amazon WorkSpaces Applications Image Programmatically by Using the Image Assistant CLI Operations](programmatically-create-image.md "programmatically-create-image.md"). 2. The remote session disconnects after a few moments. When the **Lost
Connectivity** message appears, close the browser tab. While the
image is created, the image builder status appears as
**Snapshotting**. You cannot connect to the image builder
until this process finishes. 3. Return to the console and navigate to **Images**,
**Image Registry**. Verify that your new image appears in
the list.

While your image is being created, the image status in the image registry of
the console appears as **Pending**. You can't connect to images
that are in a **Pending** status. 4. Choose the **Refresh** icon to update the status. After your
image is created, the image status changes to **Available** and
the image builder is automatically stopped.

To continue creating images, start the image builder and connect to it from
the console, or create a new image builder.

## Step 7 (Optional): Tag and Copy an Image

You can add one or more tags to an image during image creation or after you create an
image. You can also copy the image within the same Region or to a new Region within the
same Amazon Web Services account. Copying a source image results in an identical but distinct
destination image. AWS does not copy any user-defined tags, however. Also, you can
only copy custom images that you create, not the base images that are provided by AWS.

###### Note

You can copy up to two images at the same time to a destination. If the
destination to which you are copying an image is at the image limit, you receive an
error. To copy the image in this case, you must first remove images from the
destination. After the destination is below the image quota (also referred to as
limit), initiate the image copy from the source Region. For more information, see
[Amazon WorkSpaces Applications Service Quotas](limits.md "limits.md").

###### To add tags to an existing image

1. In the navigation pane, choose **Images**, **Image
   Registry**.
2. In the image list, select the image to which you want to add tags.
3. Choose **Tags**, choose **Add/Edit Tags**,
   and then choose **Add Tag**. Specify the key and value for the
   tag, and then choose **Save**.

For more information, see [Tagging Your Amazon WorkSpaces Applications Resources](tagging-basic.md "tagging-basic.md").

###### To copy an image

Copying an image across geographically diverse regions enables you to stream
applications from multiple regions based on the same image. By streaming your
applications in closer proximity to your users, you can improve your users'
experience streaming applications with WorkSpaces Applications.

1. In the navigation pane, choose **Images**, **Image
   Registry**.
2. In the image list, select the image that you want to copy.
3. Choose **Actions**, **Copy**.
4. In the **Copy Image** dialog box, specify the following
   information, and then choose **Copy Image**:
   - For **Destination region**, choose the region to
     which to copy the new image.
   - For **Name**, specify a name that the image will have
     when it is copied to the destination.
   - For **Description** (optional), specify a description
     that the image will have when it is copied to the destination.

5. To check on the progress of the copy operation, return to the console and
   navigate to **Images**, **Image Registry**.
   Use the navigation bar to switch to the destination region (if applicable), and
   confirm that your new image appears in the list of images.

The new image first appears with a status of **Copying** in the image registry of your console. After the image
is successfully created, the status of the image changes to **Available**, which means that you can use the image to
launch a stack and stream your applications.

## Step 8: Clean Up

Finally, you can stop your running image builders to free up resources and avoid
unintended charges to your account. We recommend stopping any unused, running image
builders. For more information, see [WorkSpaces Applications Pricing](https://aws.amazon.com/appstream2/pricing/ "https://aws.amazon.com/appstream2/pricing/").

###### To stop a running image builder

1. In the navigation pane, choose **Images**, **Image
   Builders**, and select the running image builder instance.
2. Choose **Actions**, **Stop**.
