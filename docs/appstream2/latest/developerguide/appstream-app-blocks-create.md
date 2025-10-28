# Create an AppStream 2.0 App Block

Follow these steps to create an app block with the AppStream 2.0 packaging type.

## Step 1: Configure the app

block

###### To configure the app block

1. Open the AppStream 2.0 console at
   [https://console.aws.amazon.com/appstream2](https://console.aws.amazon.com/appstream2 "https://console.aws.amazon.com/appstream2").
2. From the left-hand navigation menu, choose **Applications
   Manager**, **App blocks**, and
   **Create app block**.
3. For app block packaging, select **AppStream 2.0**.
4. For **App block details**, type a unique name identifier
   for the app block. Optionally, you can also specify the following:
   - **Name** – A unique name for the app
     block.
   - **Display name** (optional) – A friendly
     name for the app block.
   - **Description** (optional) – A description
     for the app block.

5. (Optional) An app block with AppStream 2.0 packaging doesn't need a setup
   script. You can optionally provide post-installation steps the
   following **Advanced Options**:
   - For **Post setup script object in S3**,
     either enter the Amazon S3 URI that represents the
     post setup script object, or choose **Browse
     S3** to navigate to your Amazon S3
     buckets and find the setup script object.
   - For **Post setup script executable**,
     enter the executable needed for your post setup
     script.

###### Note

If your setup script can execute directly, enter the filename
of the setup script. If your setup script relies on another
executable (for example, Microsoft PowerShell) to execute, enter
the path to that executable.

Path to Microsoft PowerShell on Microsoft Windows:

`C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe`

Optionally, for **Setup script executable
arguments** under **Script
settings**, enter in the arguments that need to be
provided to the setup script executable to execute your setup
script.

###### Note

If you are using a Microsoft PowerShell script, you must
specify the "-File" parameter with the name of your setup script
as an executable argument. Additionally, ensure that the
Execution Policy allows your script to be run. To learn more,
see [about_Execution_Policies](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_execution_policies?view=powershell-7.2 "https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_execution_policies?view=powershell-7.2") and [What is PowerShell?](https://docs.microsoft.com/en-us/powershell/scripting/overview?view=powershell-7.2 "https://docs.microsoft.com/en-us/powershell/scripting/overview?view=powershell-7.2").

For **Execution duration in seconds** under
**Script settings**, enter the timeout
duration for your setup script.

###### Note

The execution duration in seconds is how long AppStream 2.0 waits for
the setup script to run before continuing. If your setup script
doesn’t complete within this duration, an error is displayed to
your user and the application will attempt to launch. The setup
script is terminated after the execution duration has
elapsed. 6. Under **Import Settings**, choose **Create
new app block application file**. For **S3
Location** under **Import settings**,
either enter the Amazon S3 URI that represents the bucket,
or choose **Browse S3** to navigate to your
Amazon S3 buckets and select an appropriate bucket. The list
of Amazon S3 buckets is global and lists all the buckets
across all regions. Make sure you select the bucket in the region
where you want to create your app block. For more information about
setting bucket permissions, see [Store Application Icon, Setup Script, Session Script,
and VHD in an S3 Bucket](store-s3-bucket.md "store-s3-bucket.md"). 7. Select an app block builder. Only app block builders that are not
associated with other app blocks are available. If the list is
empty, either create a new app block builder, or disassociate the
existing ones to use. App block builder is a reusable resource that
you can use to create your application package.

###### Note

If you do not select an app block builder here, you can still
create your app block in the **Inactive**
state, and activate your app block later. For more information,
see [Activate an App Block](appstream-app-blocks-activate.md "appstream-app-blocks-activate.md"). 8. (Optional) For **Tags**, create tags for the app
block resource. 9. Choose **Next**. 10. Review the information that you entered, and choose one of the
following options:

    * Choose **Create app block** if you didn't
     select an app block builder in step 7.
    * Choose **Launch app block builder** if
     you chose an app block builder in step 7. Then continue to
     Step 2 to create your application package using the app
     block builder streaming session.

At this point, your app block resource is created, but it is
**Inactive** and can't be used for Elastic fleets.

## Step 2: Create the Application Package

Use the app block builder streaming instance to package your applications and
activate your app block. The app block created using app block builder will
have AppStream 2.0 packaging, and the application package will be uploaded onto the
Amazon S3 bucket in your AWS account.

###### To create the application package

1. After your streaming session is on, the application builder assistant
   automatically starts. If it doesn’t start, start it manually using
   the desktop icon.
2. The initial screen provides instructions for the application
   packaging process.
3. Bring your application installer onto your app block builder
   streaming session by using one of the following options:
   - Download the application installers from the web.
   - Use your streaming session file interface.
   - Download the application installer from another AWS
     service using a machine role.

4. After you have all the required application installers, stop all
   the other apps running on the instance and choose **Start
   recording**. The app block builder starts recording
   system changes, and the screen says **Recording in
   progress**.
5. Start installing your applications one by one.
6. When you are done with application installation, choose
   **Stop recording**, and the system will stop
   recording changes. If you want to make any more changes to your
   application package, such as add more applications or remove an
   already installed application, choose **Start
   recording**, and make sure the system is in
   **Recording in progress** mode.

###### Note

If your application installation fails, choose
**Report a problem** to collect AppStream 2.0
related logs from the instance, and report the problem to the
AppStream 2.0 team. When you are done, end your app block builder
streaming session. You can try to restart the process creating
an app block by using a new app block builder instance. If the
problem persists, then try to create your app block using custom
packaging. 7. When you are done installing all the applications, choose
**Stop recording**. You can test your
application, by using the Start Menu or browsing the application
using File Explorer. 8. Choose **Next** to review your app block details.

###### Note

The recommended size of an application package (VHD) file for
an Elastic fleet is less than 1.5 GB. If your VHD file size is
bigger than 1.5 GB, try reducing the number of applications
packaged within one app block.

Application package (VHD) file size will not shrink if you
uninstall an application. Restart the application packaging
process using a new app block streaming session, and install
fewer applications. 9. Choose **Finish app block creation and
disconnect** to create the application package and
upload it to the Amazon S3 bucket. If you are successful,
the streaming session will automatically disconnect, and the app
block will be in an **Active** state.

###### Note

If your application installation fails, choose
**Report a problem** to collect AppStream 2.0
related logs from the instance, and report the problem to the
AppStream 2.0 team. When you are done, end your app block builder
streaming session. You can try to restart the process creating
an app block by using a new app block builder instance. If the
problem persists, then try to create your app block using custom
packaging.
