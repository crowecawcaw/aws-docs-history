# Create a Custom App Block

You can use the AppStream 2.0 console to create the app block resource once you have your
VHD and setup script created and uploaded to an S3 bucket in your AWS account. To
learn more about storing the VHD and setup script in an Amazon S3 bucket, see [Store Application Icon, Setup Script, Session Script,
and VHD in an S3 Bucket](store-s3-bucket.md "store-s3-bucket.md").

###### Note

You must have IAM permissions to perform the `S3:GetObject`
action on the VHD and setup script objects in the Amazon S3 bucket to create the app
block resource.

###### To create the app block resource

1. Open the AppStream 2.0 console at
   [https://console.aws.amazon.com/appstream2](https://console.aws.amazon.com/appstream2 "https://console.aws.amazon.com/appstream2").
2. From the left-hand navigation menu, choose
   **Applications**, **App block**, and
   **Create app block**.
3. For app block packaging, select **Custom**.
4. For **App block details**, type a unique name identifier
   for the app block. Optionally, you can also specify the following:
   - **Display name** – A friendly name for the app
     block.
   - **Description** – A description for the app
     block.

5. For **Virtual hard disk object in S3** under
   **Script settings**, either enter the S3 URI that
   represents the VHD object, or choose **Browse S3** to
   navigate to your S3 buckets and find the VHD object.
6. For **Setup script object in S3** under **Script
   settings**, either enter the S3 URI that represents the setup
   script object, or choose **Browse S3** to navigate to your
   S3 buckets and find the setup script object.
7. For **Setup script executable** under **Script
   settings**, enter the executable necessary for your setup
   script.

###### Note

If your setup script can execute directly, enter the filename of the
setup script. If your setup script relies on another executable (for
example, Microsoft PowerShell) to execute, enter the path to that
executable.

Path to Microsoft PowerShell on Microsoft Windows:

`C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe` 8. Optionally, for **Setup script executable arguments**
under **Script settings**, enter in the arguments that need
to be provided to the setup script executable to execute your setup
script.

###### Note

If you are using a Microsoft PowerShell script, you must specify the
"-File" parameter with the name of your setup script as an executable
argument. Additionally, ensure that the Execution Policy allows your
script to be run. To learn more, see [about_Execution_Policies](https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_execution_policies?view=powershell-7.2 "https://docs.microsoft.com/en-us/powershell/module/microsoft.powershell.core/about/about_execution_policies?view=powershell-7.2") and [What is PowerShell?](https://docs.microsoft.com/en-us/powershell/scripting/overview?view=powershell-7.2 "https://docs.microsoft.com/en-us/powershell/scripting/overview?view=powershell-7.2"). 9. For **Execution duration in seconds** under
**Script settings**, enter the timeout duration for
your setup script.

###### Note

The execution duration in seconds is how long AppStream 2.0 waits for the
setup script to run before continuing. If your setup script doesn’t
complete within this duration, an error is displayed to your user and
the application will attempt to launch. The setup script is terminated
after the execution duration has elapsed. 10. (Optional) For **Tags**, create tags for the app block
resource 11. Review the information that you entered, and choose
**Create**. 12. If your app block was created successfully, you see a success message at
the top of the console. If an error occurred, you see a descriptive error
message and will need to try creating the app block again.
