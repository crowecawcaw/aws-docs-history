# Prepare an application in Amazon GameLift Streams

To set up streaming with Amazon GameLift Streams, first you upload the game or other application that you want to stream, then you configure an application
resource within Amazon GameLift Streams to define metadata about your game. An Amazon GameLift Streams application consists of the files you uploaded (executable and any
supporting files) and a configuration that instructs Amazon GameLift Streams what executable to run when streaming.

Each Amazon GameLift Streams application represents a single version of your content. If you have multiple versions, you must create a separate application
for each version. After you create an application, you cannot update the files. If you need to update the executable or any supporting files,
you must create a new Amazon GameLift Streams application.

## Before you upload

Before you create an Amazon GameLift Streams application, verify that your game adheres to the following limitations.

| Name                  | Default      | Adjustable | Description                                                                                                                                  |
| --------------------- | ------------ | ---------- | -------------------------------------------------------------------------------------------------------------------------------------------- |
| Files per application | 30,000 files | Yes\*      | The maximum number of files that you can have in an application, in this account.                                                            |
| Single file size      | 80 GiB       | No         | The maximum size of a single file in an application. Note that a gibibyte (GiB) equals 1024\*1024\*1024 bytes.                               |
| Application size      | 100 GiB      | Yes\*      | The maximum total size of an Amazon GameLift Streams application, in this account. Note that a gibibyte (GiB) equals 1024\*1024\*1024 bytes. |

\*To request an increase, sign in to the AWS Management Console and open the Service Quotas console to [Amazon GameLift Streams](https://console.aws.amazon.com/servicequotas/home/services/gameliftstreams/quotas "https://console.aws.amazon.com/servicequotas/home/services/gameliftstreams/quotas"),
where you can review your current quotas in the **Applied account-level quota value** column and submit a request to increase a value.

###### Note

To save yourself time and effort, verify that the files you are ready to upload are the correct version of your application. While
you can upload new versions later, you will need to repeat the [Create an application](#applications-create "#applications-create") step for each version.

## Upload your application to an Amazon S3 bucket

Now that you have prepared your game for Amazon GameLift Streams, it's time to upload it to an Amazon Simple Storage Service (Amazon S3) bucket in your AWS account.

###### Note

The Amazon S3 storage class that Amazon GameLift Streams requires is the default **S3 Standard**. Other storage classes
like **S3 Glacier** or objects being moved to **Infrequent Access** or
**Archive Access** by **S3 Intelligent-Tiering** are not supported by
Amazon GameLift Streams.

To optimize storage cost, you can delete the application from your S3 bucket after you complete [Create an application](#applications-create "#applications-create") and the application is in **Ready** status.

###### To upload your application to Amazon S3

1. Sign in to the AWS Management Console and open the Amazon S3 console at
   [https://console.aws.amazon.com/s3/](https://console.aws.amazon.com/s3/ "https://console.aws.amazon.com/s3/").
2. Create an Amazon S3 bucket. Enter a bucket name and select an AWS Region. This region must be the same as the application and stream group that you will create later.
   See [AWS Regions and remote locations supported by
   Amazon GameLift Streams](regions-quotas-rande.md "regions-quotas-rande.md") for a list of
   AWS Regions where Amazon GameLift Streams is available. For the remaining fields, keep the default settings.

For more instructions, refer to
[Creating a bucket](../../../AmazonS3/latest/userguide/create-bucket-overview.md "../../../AmazonS3/latest/userguide/create-bucket-overview.md") in the _Amazon Simple Storage Service User Guide_. 3. Open the new bucket and upload the folder with your application files.

###### Warning

You must upload your application files as an uncompressed folder. Don't upload a `.zip` folder.

## Create an application

An Amazon GameLift Streams application is a resource that contains a game or interactive application that runs on Amazon GameLift Streams infrastructure and delivers gameplay experiences to players
through cloud streaming. The application executes on AWS compute instances and renders game content that is streamed directly to players' devices over the internet, eliminating
the need for players to download, install, or run the game locally.

When you create an Amazon GameLift Streams application, you provide the Amazon S3 URI to the application folder you uploaded to your Amazon S3 bucket,
and the relative path to a valid executable or script file.

Amazon GameLift Streams does not keep your application files in sync with the files in the Amazon S3 bucket. If you want to update the files in your Amazon GameLift Streams
application, you must create a new Amazon GameLift Streams application.

Console

###### To create an Amazon GameLift Streams application using the Amazon GameLift Streams console

1.  Sign in to the AWS Management Console and open the [Amazon GameLift Streams console](https://console.aws.amazon.com/gameliftstreams/ "https://console.aws.amazon.com/gameliftstreams/"). Choose the same AWS Region as the Amazon S3 bucket where you uploaded your set of files. For more information, refer to [Choosing a Region](../../../awsconsolehelpdocs/latest/gsg/select-region.md "../../../awsconsolehelpdocs/latest/gsg/select-region.md") in the _AWS Management Console Getting Started Guide_.
2.  In the navigation bar, choose **Applications** and then choose **Create application**.
3.  In **Runtime settings**, enter the following:
    1. **Runtime environment**

    This is the runtime environment to run your application on. Amazon GameLift Streams can run on either Windows, Ubuntu 22.04 LTS, or [Proton](<https://en.wikipedia.org/wiki/Proton_(software)> "https://en.wikipedia.org/wiki/Proton_(software)").

    **You cannot edit this field after the creation workflow.**

    Choose from one of the following runtime environments.

        * For Linux applications:





        	+ Ubuntu 22.04 LTS (`UBUNTU, 22_04_LTS`)
        * For Windows applications:





        	+ Microsoft Windows Server 2022 Base (`WINDOWS, 2022`)
        	+ Proton 9.0-2 (`PROTON, 20250516`)
        	+ Proton 8.0-5 (`PROTON, 20241007`)
        	+ Proton 8.0-2c (`PROTON, 20230704`)

    Review the descriptions and use the comparison checklist to help you select the optimal runtime environment for your application.

4.  In **General settings**, enter the following:
    1. **Description**

    This is a human-readable label for your application. This value does not have to be unique. For best practice, use a meaningful description, name, or label for the application.
    You can edit this field at any time. 2. **Base path**

    This is the Amazon S3 URI to your application's root folder in the Amazon S3 bucket. The folder and any subfolders should contain your build executable and any supporting files.

    A valid URI is the bucket prefix that contains all the files needed to run and stream the application.
    Example: A bucket called `mygamebuild` contains three complete versions of the game build files, each in a separate folder.
    You want to stream the build in the folder `mygamebuild-EN101`.
    In this example, the URI is `s3://amzn-s3-demo-bucket/mygamebuild-EN101`.

    **You cannot edit this field after the creation workflow.** 3. **Executable launch path**

    This is the Amazon S3 URI of the executable file that Amazon GameLift Streams will stream. The file must be contained within the application's root folder. For Windows applications, the file must be a valid Windows executable or batch file with a filename ending in .exe, .cmd, or .bat. For Linux applications, the file must be a valid Linux binary executable or a script that contains an initial interpreter line starting with a shebang ('`#!`').

    **You cannot edit this field after the creation workflow.**

5.  (Optional) In **Application log path**, enter the following:
    1. **Application log path**

    This is the path (or paths) to the application folder or file which contains logs that you want to save.
    Specify each log path relative to your application base path.
    If you use this feature, then at the end of every stream session, Amazon GameLift Streams will copy the file(s) that you specify to the Amazon S3 bucket that you name.
    The copy operation is not performed recursively in an application folder's subfolders.

    To disable logging, remove all application log paths and clear the application log output destination.

    You can edit this field at any time. 2. **Application log output**

    This is the URI to the Amazon S3 bucket where Amazon GameLift Streams will copy application log files. This field is required if you specify an application log path.

    To disable logging, remove all application log paths and clear the application log output destination.

    You can edit this field at any time.

    To save log files on your behalf, Amazon GameLift Streams must be given permission to your S3 bucket for saving.
    If you let Amazon GameLift Streams create the bucket for logging, the permission policy will be applied automatically upon creation.
    If you provide your own bucket, you will need to apply the permission policy, yourself.

    **Bucket permission policy template**

    Copy the following policy code and apply it to the bucket that you want to use for application logs. Be sure to replace **amzn-s3-demo-bucket**
    with the name of your existing S3 bucket.

    ```
    {
      "Version": "2012-10-17",
      "Statement": [
        {
          "Sid": "PutPolicy",
          "Effect": "Allow",
          "Principal": {
            "Service": [
              "gameliftstreams.amazonaws.com"
            ]
          },
          "Action": "s3:PutObject",
          "Resource": "arn:aws:s3:::`amzn-s3-demo-bucket`/*",
          "Condition": {
            "StringEquals": {
              "aws:SourceAccount": "`your 12-digit account id`"
            }
          }
        }
      ]
    }
    ```

6.  (Optional) In **Tags**, assign tags to this application.

Tags are labels that can help you organize your AWS resources. For more information, refer to [Tagging your AWS resources](../../../tag-editor/latest/userguide/tagging.md "../../../tag-editor/latest/userguide/tagging.md").

For example to track application versions, use a tag such as `application-version : my-game-1121`. 7. Choose **Create application**.

CLI
**Prerequisite**

You must configure the AWS CLI with your user credentials and your chosen AWS Region. For setup instructions, refer to [Download the AWS CLI](setting-up.md#setting-up-prereqs "setting-up.md#setting-up-prereqs").

**To create an application using the AWS CLI**

In your AWS CLI use the [CreateApplication](../apireference/API_CreateApplication.md "../apireference/API_CreateApplication.md")
command, customized for your content.

```
aws gameliftstreams create-application \
    --description "`MyGame v1`" \
    --runtime-environment '{"Type":"`PROTON`", "Version":"`20241007`"}' \
    --executable-path "`launcher.exe`" \
    --application-source-uri "`s3://amzn-s3-demo-bucket/example`"
```

where

- `description`:

This is a human-readable label for your application. This value does not have to be unique. For best practice, use a meaningful description, name, or label for the application.
You can edit this field at any time.

- `runtime-environment`:

This is the runtime environment to run your application on. Amazon GameLift Streams can run on either Windows, Ubuntu 22.04 LTS, or [Proton](<https://en.wikipedia.org/wiki/Proton_(software)> "https://en.wikipedia.org/wiki/Proton_(software)").

**You cannot edit this field after the creation workflow.**

Choose from one of the following runtime environments.

    + For Linux applications:




    	- Ubuntu 22.04 LTS (`Type=UBUNTU, Version=22_04_LTS`)
    + For Windows applications:




    	- Microsoft Windows Server 2022 Base (`Type=WINDOWS, Version=2022`)
    	- Proton 9.0-2 (`Type=PROTON, Version=20250516`)
    	- Proton 8.0-5 (`Type=PROTON, Version=20241007`)
    	- Proton 8.0-2c (`Type=PROTON, Version=20230704`)

- `application-source-uri`:

This is the Amazon S3 URI to your application's root folder in the Amazon S3 bucket. The folder and any subfolders should contain your build executable and any supporting files.

A valid URI is the bucket prefix that contains all the files needed to run and stream the application.
Example: A bucket called `mygamebuild` contains three complete versions of the game build files, each in a separate folder.
You want to stream the build in the folder `mygamebuild-EN101`.
In this example, the URI is `s3://amzn-s3-demo-bucket/mygamebuild-EN101`.

**You cannot edit this field after the creation workflow.**

- `executable-path`:

This is the relative path and file name of the executable file that Amazon GameLift Streams will stream. Specify a path relative to the `application-source-uri`. The file must be contained within the application's root folder. For Windows applications, the file must be a valid Windows executable or batch file with a filename ending in .exe, .cmd, or .bat. For Linux applications, the file must be a valid Linux binary executable or a script that contains an initial interpreter line starting with a shebang ('`#!`').

**You cannot edit this field after the creation workflow.**

If the request is successful, Amazon GameLift Streams returns a response similar to the following:

```
{
    "Arn": "arn:aws:gameliftstreams:us-west-2:111122223333:application/a-9ZY8X7Wv6",
    "Description": "MyGame v1",
    "RuntimeEnvironment": {
        "Type": "PROTON",
        "Version": "20241007"
    },
    "ExecutablePath": "launcher.exe",
    "ApplicationSourceUri": "s3://amzn-s3-demo-bucket/example",
    "Id": "a-9ZY8X7Wv6",
    "Status": "PROCESSING",
    "CreatedAt": "2022-11-18T15:47:11.924000-08:00",
    "LastUpdatedAt": "2022-11-18T15:47:11.924000-08:00"
}
```

To check the status of your application, call the [GetApplication](../apireference/API_GetApplication.md "../apireference/API_GetApplication.md") command, as shown in the following example.

```
aws gameliftstreams get-application /
    --identifier `a-9ZY8X7Wv6`
```

Amazon GameLift Streams takes a few minutes to prepare your application. During this time, the new application is in
**Processing** status. When your application is in **Ready** status, you can go to the next step,
[Create a stream group](stream-groups.md#stream-groups-create "stream-groups.md#stream-groups-create").

If the request returns an error, or if the application is created but placed in an **Error** status, make sure that
you're working with user credentials that include access to both Amazon S3 and Amazon GameLift Streams.

###### Note

When an application is in **Ready** status, Amazon GameLift Streams has successfully copied your application files to its private
Amazon S3 bucket. You can delete your original application files without affecting your new application. This also helps you optimize on
storage cost. For more information, see [Delete an application](#applications-delete "#applications-delete").

## Edit an application

You can update the settings for any application in **Ready** status. If you make changes to an existing application,
these changes impact the streaming behavior for both new and existing stream groups.

Console

###### To edit an application in the Amazon GameLift Streams console

1. In the navigation bar, choose **Applications** to view a list of your existing applications.
   Choose the application you want to edit.
2. In the application details page, locate the section that contains the settings you want to change and choose
   **Edit** or **Manage tags** accordingly.
3. You can change the following settings:

**Short description**

This is a human-readable label for your application. This value does not have to be unique. For best practice, use a meaningful description, name, or label for the application.
You can edit this field at any time.

**Application log path**

This is the path (or paths) to the application folder or file which contains logs that you want to save.
Specify each log path relative to your application base path.
If you use this feature, then at the end of every stream session, Amazon GameLift Streams will copy the file(s) that you specify to the Amazon S3 bucket that you name.
The copy operation is not performed recursively in an application folder's subfolders.

To disable logging, remove all application log paths and clear the application log output destination.

You can edit this field at any time.

**Application log output**

This is the URI to the Amazon S3 bucket where Amazon GameLift Streams will copy application log files. This field is required if you specify an application log path.

To disable logging, remove all application log paths and clear the application log output destination.

You can edit this field at any time.

To save log files on your behalf, Amazon GameLift Streams must be given permission to your S3 bucket for saving.
If you let Amazon GameLift Streams create the bucket for logging, the permission policy will be applied automatically upon creation.
If you provide your own bucket, you will need to apply the permission policy, yourself.

For more information, see [Application log bucket permission policy](#application-bucket-permission-template "#application-bucket-permission-template").

**Tags**

Tags are labels that can help you organize your AWS resources. For more information, refer to [Tagging your AWS resources](../../../tag-editor/latest/userguide/tagging.md "../../../tag-editor/latest/userguide/tagging.md").

For example to track application versions, use a tag such as `application-version : my-game-1121`. 4. Choose **Save changes**. The Amazon GameLift Streams console returns to the application details page, displaying the
updated settings.

CLI
**Prerequisite**

You must configure the AWS CLI with your user credentials and your chosen AWS Region. For setup instructions, refer to [Download the AWS CLI](setting-up.md#setting-up-prereqs "setting-up.md#setting-up-prereqs").

**To edit an application using the AWS CLI**

In your AWS CLI use the [UpdateApplication](../apireference/API_UpdateApplication.md "../apireference/API_UpdateApplication.md") command, customized for your content.

```
aws gameliftstreams update-application \
    --identifier `a-9ZY8X7Wv6` \
    --description "`MyGame v2`" \
    --application-log-paths '["`.\\logs`"]' \
    --application-log-output-uri "`s3://amzn-s3-demo-bucket/mygame`"
```

where

- `identifier`: The application to edit.

This value is an
[Amazon Resource Name (ARN)](../../../IAM/latest/UserGuide/reference-arns.md "../../../IAM/latest/UserGuide/reference-arns.md") or ID that uniquely identifies the application resource.

ARN example: `arn:aws:gameliftstreams:us-west-2:111122223333:application/a-9ZY8X7Wv6`

ID example: `a-9ZY8X7Wv6`

- `description`:

This is a human-readable label for your application. This value does not have to be unique. For best practice, use a meaningful description, name, or label for the application.
You can edit this field at any time.

- `application-log-paths`:

This is the path (or paths) to the application folder or file which contains logs that you want to save.
Specify each log path relative to your application base path.
If you use this feature, then at the end of every stream session, Amazon GameLift Streams will copy the file(s) that you specify to the Amazon S3 bucket that you name.
The copy operation is not performed recursively in an application folder's subfolders.

To disable logging, remove all application log paths and clear the application log output destination.

You can edit this field at any time.

- `application-log-output-uri`:

This is the URI to the Amazon S3 bucket where Amazon GameLift Streams will copy application log files. This field is required if you specify an application log path.

To disable logging, remove all application log paths and clear the application log output destination.

You can edit this field at any time.

To save log files on your behalf, Amazon GameLift Streams must be given permission to your S3 bucket for saving.
If you let Amazon GameLift Streams create the bucket for logging, the permission policy will be applied automatically upon creation.
If you provide your own bucket, you will need to apply the permission policy, yourself.

For more information, see [Application log bucket permission policy](#application-bucket-permission-template "#application-bucket-permission-template").

## Delete an application

Delete an application if you no longer need it. This action permanently deletes the application, including the application content
files stored with Amazon GameLift Streams. However, this does not delete the original files that you uploaded to your Amazon S3 bucket; you can delete these
any time after Amazon GameLift Streams creates an application, which is the only time Amazon GameLift Streams accesses your Amazon S3 bucket.

You can only delete an application that meets the following conditions:

- The application is in the **Ready** or **Error** state.
- An application is not streaming in any ongoing stream session. You must wait until the client ends the stream session or call
  [TerminateStreamSession](../apireference/API_TerminateStreamSession.md "../apireference/API_TerminateStreamSession.md") in the Amazon GameLift Streams API to end the stream.

If the application is linked to any stream groups, you must unlink it from all associated stream groups before you can delete it. In the console, a dialog box will walk you through this process.

Console

###### To delete an application using the Amazon GameLift Streams console

1. Sign in to the AWS Management Console and open the [Amazon GameLift Streams console](https://console.aws.amazon.com/gameliftstreams/ "https://console.aws.amazon.com/gameliftstreams/").
2. In the navigation bar, choose **Applications** to view a list
   of your existing applications. Choose the application you want to delete.
3. In the application detail page, choose **Delete**.
4. In the **Delete** dialog box, confirm the delete action.

CLI
**Prerequisite**

You must configure the AWS CLI with your user credentials and your chosen AWS Region. For setup instructions, refer to [Download the AWS CLI](setting-up.md#setting-up-prereqs "setting-up.md#setting-up-prereqs").

**To delete an application using the AWS CLI**

In your AWS CLI use the [DeleteApplication](../apireference/API_DeleteApplication.md "../apireference/API_DeleteApplication.md") command, customized for your content.

```
aws gameliftstreams delete-application \
    --identifier `arn:aws:gameliftstreams:us-west-2:111122223333:application/a-9ZY8X7Wv6`
```

where

- `identifier`: The application to delete.

This value is an
[Amazon Resource Name (ARN)](../../../IAM/latest/UserGuide/reference-arns.md "../../../IAM/latest/UserGuide/reference-arns.md") or ID that uniquely identifies the application resource.

ARN example: `arn:aws:gameliftstreams:us-west-2:111122223333:application/a-9ZY8X7Wv6`

ID example: `a-9ZY8X7Wv6`

Amazon GameLift Streams begins deleting the application. During this time, the application is in `Deleting` status. After Amazon GameLift Streams deletes
the application, you can no longer retrieve it.

## Application log bucket permission policy

If you provide your own application log Amazon S3 bucket, you will need to apply a permission policy to the bucket so that Amazon GameLift Streams can save
log files to the bucket. Use the following template to update the permissions in Amazon S3.

**Bucket permission policy template**

Copy the following policy code and apply it to the bucket that you want to use for application logs. Be sure to replace **amzn-s3-demo-bucket**
with the name of your existing S3 bucket.

```
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "PutPolicy",
      "Effect": "Allow",
      "Principal": {
        "Service": [
          "gameliftstreams.amazonaws.com"
        ]
      },
      "Action": "s3:PutObject",
      "Resource": "arn:aws:s3:::`amzn-s3-demo-bucket`/*",
      "Condition": {
        "StringEquals": {
          "aws:SourceAccount": "`your 12-digit account id`"
        }
      }
    }
  ]
}
```

###### Note

Amazon GameLift Streams does not permit cross-account resource access. The Amazon S3 bucket must be owned by the same AWS account as the application
resource. Although this is strongly enforced by the service, it is a best practice to always include `aws:SourceAccount` or
`aws:SourceArn` conditions to prevent the [confused deputy problem](../../../IAM/latest/UserGuide/confused-deputy.md "../../../IAM/latest/UserGuide/confused-deputy.md") when granting permission to any AWS service.

## Linked stream groups

If you want to stream multiple applications by using the same pool of compute resources, you can link multiple applications to the same
stream group. Similarly, if you want to stream an application by using different sets of compute resources, you can link an application to
multiple stream groups.

For more information about linking applications to stream groups, refer to [Overview of multi-application stream groups](multi-apps.md "multi-apps.md").
