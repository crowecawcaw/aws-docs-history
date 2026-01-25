# Upload script files from Amazon S3

You can store your script files in an Amazon S3 bucket and upload them to Amazon GameLift Servers from there.
When you create your script, you specify the S3 bucket location and Amazon GameLift Servers retrieves your
script files from Amazon S3.

###### To create a script resource

1. **Store your script files in an S3 bucket.**
   Create a .zip file containing your server script files and upload it to an S3
   bucket in an AWS account that you control. Take note of the object
   URI—you need this when creating a Amazon GameLift Servers script.

###### Note

Amazon GameLift Servers doesn't support uploading from S3 buckets with names that contain a
period (.). 2. **Give Amazon GameLift Servers access to your script files.** To
create an AWS Identity and Access Management (IAM) role that allows Amazon GameLift Servers to access the S3 bucket
containing your server script, follow the instructions in
[Set up an IAM service role for Amazon GameLift Servers](../developerguide/setting-up-role.md "../developerguide/setting-up-role.md"). After you
create the new role, take note of its name, which you need when creating a
script. 3. **Create a script.** Use the Amazon GameLift Servers console or the
AWS CLI to create a new script record. To make this request, you must have the
IAM `PassRole` permission, as described in
[IAM permission examples for Amazon GameLift Servers](../developerguide/gamelift-iam-policy-examples.md "../developerguide/gamelift-iam-policy-examples.md").

Console

1. In the [Amazon GameLift Servers console](https://console.aws.amazon.com/gamelift "https://console.aws.amazon.com/gamelift"),
   in the navigation pane, choose **Hosting**,
   **Scripts**.
2. On the **Scripts** page, choose **Create
   script**.
3. On the **Create script** page, under
   **Script settings**, do the following:
   1. For **Name**, enter a script name.
   2. (Optional) For **Version**, enter version
      information. Because you can update the content of a script,
      version data can be helpful in tracking updates.
   3. For **Node.js version**, choose the runtime version of Node.js the server will run on.
   4. For **Script source**, choose
      **Amazon S3 URI**.
   5. Enter the **S3 URI** of the script object
      that you uploaded to Amazon S3, and then choose the
      **Object version**. If you don't
      remember the Amazon S3 URI and object version, choose
      **Browse S3**, and then search for the
      script object.

4. (Optional) Under **Tags**, add tags to the script
   by entering **Key** and **Value**
   pairs.
5. Choose **Create**.

Amazon GameLift Servers assigns an ID to the new script and uploads the designated
.zip file. You can view the new script, including its status, on the
**Scripts** page.

AWS CLI
Use the [`create-script`](../../../cli/latest/reference/gamelift/create-script.md "../../../cli/latest/reference/gamelift/create-script.md") AWS CLI command to define the
new script and upload your server script files.

1. Open a command line window and switch to a directory where you can
   use the AWS CLI.
2. Enter the following **create-script** command and
   parameters. The **--storage-location** parameter
   specifies the Amazon S3 bucket location of your script files.

```
aws gamelift create-script \
    --name [`user-defined name of script`] \
    --script-version [`user-defined version info`] \
    --storage-location "Bucket"=`S3 bucket name`,"Key"=`name of zip file in S3 bucket`,"RoleArn"=`Access role ARN` \
    --node-js-version `10.x or 24.x` \
    --region `region name`
```

_Example_

```
aws gamelift create-script \
    --name "My_Realtime_Server_Script_1" \
    --script-version "1.0.0" \
    --storage-location "Bucket"="gamelift-script","Key"="myrealtime_script_1.0.0.zip","RoleArn"="arn:aws:iam::123456789012:role/S3Access" \
    --node-js-version 24.x \
    --region us-west-2
```

In response to your request, Amazon GameLift Servers returns the new script
object. 3. To view the new script, call [`describe-script`](../../../cli/latest/reference/gamelift/describe-script.md "../../../cli/latest/reference/gamelift/describe-script.md").
