# Create an App Block with an

Existing App Package

You can use your existing application package (VHD) with AppStream 2.0 packaging to
create AppStream 2.0 app blocks. To do this, copy your application package (VHD) file
from the source Amazon S3 bucket to another destination
Amazon S3 bucket. The destination bucket can be in a different region.

###### To create an app block with existing app package

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

If your post setup script can execute directly, enter the filename of
the post setup script. If your post setup script relies on another
executable (for example, Microsoft PowerShell) to execute, enter the
path to that executable.

Path to Microsoft PowerShell on Microsoft Windows:

`C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe`

Optionally, for **Post setup script executable
arguments**, enter in the arguments that need to be
provided to the setup script executable to execute your setup
script.

###### Note

If you are using a Microsoft PowerShell script, you must specify the
"-File" parameter with the name of your post setup script as an
executable argument. Additionally, ensure that the Execution Policy
allows your script to be run. To learn more, see [about_Execution_Policies](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_execution_policies?view=powershell-7.2 "https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_execution_policies?view=powershell-7.2") and [What is PowerShell?](https://docs.microsoft.com/en-us/powershell/scripting/overview?view=powershell-7.2 "https://docs.microsoft.com/en-us/powershell/scripting/overview?view=powershell-7.2").

For **Execution duration in seconds** under
**Script settings**, enter the timeout
duration for your setup script.

###### Note

The execution duration in seconds is how long AppStream 2.0 waits for the
post setup script to run before continuing. If your post setup
script doesn’t complete within this duration, an error is displayed
to your user and the application will attempt to launch. The setup
script is terminated after the execution duration has
elapsed. 6. Choose **Use existing app block application file** under
**Import settings**. For **S3
Location**, you can enter the Amazon S3 URI for the
object in an Amazon S3 bucket that represents the application
package (VHD), Or, choose **Browse S3** to navigate to
your Amazon S3 buckets and select the object in an
Amazon S3 bucket. The list of Amazon S3 buckets is
global and lists all the buckets across all regions. Make sure you
select the bucket in the region where you want to create your app block. 7. Choose **Next**. 8. Review the information that you entered, and choose **Create app
block**.
At this point your app block resource is created and in the
**Active** state.
