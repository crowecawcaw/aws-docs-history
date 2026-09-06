

# Upload script files from a local directory
<a name="realtime-script-uploading-zip"></a>

If you have your script files stored locally, you can upload them to Amazon GameLift Servers from there. To create the script resource, use either the Amazon GameLift Servers console or the [AWS Command Line Interface (AWS CLI)](https://aws.amazon.com/cli/).

------
#### [  Amazon GameLift Servers console ]

**To create a script resource**

1. Open the [Amazon GameLift Servers console](https://console.aws.amazon.com/gamelift/).

1. In the navigation pane, choose **Hosting**, **Scripts**.

1. On the **Scripts** page, choose **Create script**.

1. On the **Create script** page, under **Script settings,** do the following:

   1. For **Name**, enter a script name.

   1. (Optional) For **Version**, enter version information. Because you can update the content of a script, version data can be helpful in tracking updates.

   1. For **Node.js version**, choose the runtime version of Node.js the server will run on.

   1. For **Script source**, choose **Upload a .zip file**.

   1. For **Script files**, choose **Choose file**, browse for the .zip file that contains your script, and then choose that file.

1. (Optional) Under **Tags**, add tags to the script by entering **Key** and **Value** pairs.

1. Choose **Create**.

   Amazon GameLift Servers assigns an ID to the new script and uploads the designated .zip file. You can view the new script, including its status, on the **Scripts** page.

------
#### [ AWS CLI ]

Use the [`create-script`](https://docs.aws.amazon.com/cli/latest/reference/gamelift/create-script.html) AWS CLI command to define the new script and upload your server script files.

**To create a script resource**

1. Place the .zip file into a directory where you can use the AWS CLI.

1. Open a command line window and switch to the directory where you placed the .zip file.

1. Enter the following **create-script** command and parameters. For the **--zip-file** parameter, be sure to add the string `fileb://` to the name of the .zip file. It identifies the file as binary so that Amazon GameLift Servers processes the compressed content.

   ```
   aws gamelift create-script \
       --name {{user-defined name of script}} \
       --script-version {{user-defined version info}} \
       --zip-file fileb://{{name of zip file}} \
       --node-js-version {{10.x or 24.x}} \
       --region {{region name}}
   ```

   *Example*

   ```
   aws gamelift create-script \
       --name "My_Realtime_Server_Script_1" \
       --script-version "1.0.0" \
       --zip-file fileb://myrealtime_script_1.0.0.zip \
       --node-js-version 24.x \
       --region us-west-2
   ```

   In response to your request, Amazon GameLift Servers returns the new script object.

1. To view the new script, call `[describe-script](https://docs.aws.amazon.com/cli/latest/reference/gamelift/describe-script.html)`.

------