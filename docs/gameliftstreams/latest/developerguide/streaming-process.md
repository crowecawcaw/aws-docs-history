# Starting your first stream in Amazon GameLift Streams

This tutorial walks you through the steps to get started with Amazon GameLift Streams to stream your application or game. Amazon GameLift Streams runs your application and streams them directly to your end-users' web browser. You'll learn how to upload and configure the application you want to stream, and how to manage the way Amazon GameLift Streams streams. By the end, you will test how your application streams on Amazon GameLift Streams by interacting with it directly in the Amazon GameLift Streams console.

###### Before you start, understand Amazon GameLift Streams pricing.

You can find the cost of Amazon GameLift Streams in the [Pricing page](https://aws.amazon.com/gamelift/streams/pricing/ "https://aws.amazon.com/gamelift/streams/pricing/"). To learn more, refer to [Managing usage and bills for Amazon GameLift Streams](pricing.md "pricing.md").

You incur cost for using Amazon GameLift Streams, specifically when you:

- Create an Amazon GameLift Streams application in [Step 2: Configure your application for Amazon GameLift Streams](#streaming-process-create-application "#streaming-process-create-application")
- Create a stream group in [Step 3: Manage how Amazon GameLift Streams streams your application](#streaming-process-stream-group "#streaming-process-stream-group")

**Do not skip [Step 5: Clean up (don't skip)](#streaming-process-cleanup "#streaming-process-cleanup")**. To avoid unnecessary charges
after you're done trying Amazon GameLift Streams, you must clean up all your resources.

###### Topics

- [Prerequisites](#streaming-process-prerequisites "#streaming-process-prerequisites")
- [Step 1: Upload your application to an Amazon S3 bucket](#streaming-process-upload-application "#streaming-process-upload-application")
- [Step 2: Configure your application for Amazon GameLift Streams](#streaming-process-create-application "#streaming-process-create-application")
- [Step 3: Manage how Amazon GameLift Streams streams your application](#streaming-process-stream-group "#streaming-process-stream-group")
- [Step 4: Test your stream in Amazon GameLift Streams](#streaming-process-stream-session "#streaming-process-stream-session")
- [Step 5: Clean up (don't skip)](#streaming-process-cleanup "#streaming-process-cleanup")

## Prerequisites

Complete the following tasks before you start the tutorial.

- Sign up for an AWS account and create a user with administrative access, if you don't already have one.
  Refer to the [Setting up](setting-up.md "setting-up.md") topic in this guide for help with this task.
  You do not need to download the Amazon GameLift Streams Web SDK or set up the AWS CLI at this time — you will complete the following steps using the AWS Management Console.
- Get a version of your application content files with no digital rights management (DRM).
  Collect the files required to run the application, including executables and assets, into
  a folder, but _do not_ compress the folder.

## Step 1: Upload your application to an Amazon S3 bucket

Amazon GameLift Streams uses Amazon Simple Storage Service (Amazon S3) to store your application or game files in the cloud and
access it for streaming. In this step, you upload your application files to an Amazon S3 bucket.
Complete this step in the Amazon S3 Console.

###### Note

The Amazon S3 storage class that Amazon GameLift Streams requires is the default **S3 Standard**. Other storage classes like **S3 Glacier** or objects being moved to **Infrequent Access** or **Archive Access** by **S3 Intelligent-Tiering** are not supported by Amazon GameLift Streams.

To optimize storage cost, you can delete the application from your S3 bucket after you complete [Step 2: Configure your application for Amazon GameLift Streams](#streaming-process-create-application "#streaming-process-create-application") and the application is in **Ready** status.

**Application limitations**

| Name                  | Default      | Adjustable | Description                                                                                                                                  |
| --------------------- | ------------ | ---------- | -------------------------------------------------------------------------------------------------------------------------------------------- |
| Files per application | 30,000 files | Yes\*      | The maximum number of files that you can have in an application, in this account.                                                            |
| Single file size      | 80 GiB       | No         | The maximum size of a single file in an application. Note that a gibibyte (GiB) equals 1024\*1024\*1024 bytes.                               |
| Application size      | 100 GiB      | Yes\*      | The maximum total size of an Amazon GameLift Streams application, in this account. Note that a gibibyte (GiB) equals 1024\*1024\*1024 bytes. |

\*To request an increase, sign in to the AWS Management Console and open the Service Quotas console to [Amazon GameLift Streams](https://console.aws.amazon.com/servicequotas/home/services/gameliftstreams/quotas "https://console.aws.amazon.com/servicequotas/home/services/gameliftstreams/quotas"),
where you can review your current quotas in the **Applied account-level quota value** column and submit a request to increase a value.

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

###### Warning

Ensure that the application files you uploaded are the correct ones, and are
within the application file size limitations. If you want to update your files later,
you must repeat [Step 2: Configure your application for Amazon GameLift Streams](#streaming-process-create-application "#streaming-process-create-application"), which can take a few minutes.

## Step 2: Configure your application for Amazon GameLift Streams

**What is an application in Amazon GameLift Streams?**

An Amazon GameLift Streams application is a resource that contains a game or interactive application that runs on Amazon GameLift Streams infrastructure and delivers gameplay experiences to players
through cloud streaming. The application executes on AWS compute instances and renders game content that is streamed directly to players' devices over the internet, eliminating
the need for players to download, install, or run the game locally.

In this step, you configure the application you want to stream with Amazon GameLift Streams by creating an Amazon GameLift Streams application. When you create an
Amazon GameLift Streams application, you provide the Amazon S3 URI to the application folder you uploaded to your Amazon S3 bucket, and the relative path to a valid
executable or script file. Complete this step in the Amazon GameLift Streams console.

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

Amazon GameLift Streams takes a few minutes to prepare your application. In the **Applications** page, the new application is in **Processing** status. When your application is in **Ready** status, you can go to the next step, [Step 3: Manage how Amazon GameLift Streams streams your application](#streaming-process-stream-group "#streaming-process-stream-group").

If the request returns an error, or if the application is created but in **Error** status, make sure that you're working with user credentials that include access to both Amazon S3 and Amazon GameLift Streams.

###### Note

When an application is in **Ready** status, you can safely delete the application files in your Amazon S3 bucket, without affecting your new application. This also helps optimize storage cost. For more information, see [Delete an application](applications.md#applications-delete "applications.md#applications-delete").

For more information, refer to [Prepare an application in Amazon GameLift Streams](applications.md "applications.md").

## Step 3: Manage how Amazon GameLift Streams streams your application

**What is a stream group?**

Manage how Amazon GameLift Streams streams your applications by using a stream group. A stream group is a collection of compute resources that Amazon GameLift Streams uses to stream your application to end users.
When you create a stream group, you specify the hardware configuration (CPU, GPU, RAM) that will run your game (known as the _stream class_),
the geographical locations where your game can run,
and the number of streams that can run simultaneously in each location (known as _stream capacity_).
You can link an application when you create the stream group, or wait until later, but you must link at least one application before you can stream from a stream group.
After a stream group has been created, Amazon GameLift Streams allocates compute resources in the locations where you have allocated stream capacity.
At this point, you can also associate additional applications to the stream group so that you have a choice of which one to stream.

With your application ready, the next thing you need is compute resources for Amazon GameLift Streams to stream it. In this step, you manage how Amazon GameLift Streams streams your application by creating a stream group. Complete this step in the Amazon GameLift Streams console.

###### To create a stream group in the Amazon GameLift Streams console

1. Sign in to the AWS Management Console and open the [Amazon GameLift Streams console](https://console.aws.amazon.com/gameliftstreams/ "https://console.aws.amazon.com/gameliftstreams/"). Choose the AWS Region where you want to create your stream group. This Region must be the same as that of the application that you want to stream with the stream group. For more information, refer to [Choosing a Region](../../../awsconsolehelpdocs/latest/gsg/select-region.md "../../../awsconsolehelpdocs/latest/gsg/select-region.md") in the _AWS Management Console Getting Started Guide_.
2. To open the creation workflow, in the navigation pane, choose **Stream groups**, and then choose **Create stream group**.
3. In **Define stream group**, enter the following:
   1. **Description**

   A human-readable label for your stream group. This value doesn't have to be unique. As a best practice, use a meaningful description, name, or label for the stream group.
   You can edit this field at any time. 2. **Tags**

   Tags are labels that can help you organize your AWS resources. For more information, refer to [Tagging your AWS resources](../../../tag-editor/latest/userguide/tagging.md "../../../tag-editor/latest/userguide/tagging.md").

4. In **Select stream class**, choose a stream class for the stream group.
   1. **Stream class options**

   The
   type of compute resources to run and stream applications with. This choice impacts the quality of the streaming experience and the cost. You can specify only one stream class per stream group.
   Choose the class that best fits your application.

   | Stream class          | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |
   | --------------------- | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- | ----------------------------- |
   | `gen6n_pro_win2022`   | (NVIDIA, pro) Supports applications with extremely high 3D scene complexity which require maximum resources.<br>Runs applications on Microsoft Windows Server 2022 Base and supports DirectX 12.<br>Compatible with Unreal Engine versions up through 5.6, 32 and 64-bit applications, and anti-cheat technology.<br>Uses NVIDIA L4 Tensor Core GPU.<br>Resources per application: vCPUs: 16. RAM: 64 GB. VRAM: 24 GB.<br>Tenancy: Supports up to one concurrent stream session. |
   | `gen6n_pro`           | (NVIDIA, pro) Supports applications with extremely high 3D scene complexity which require maximum resources.<br>Uses NVIDIA L4 Tensor Core GPU.<br>Resources per application: vCPUs: 16. RAM: 64 GB. VRAM: 24 GB.<br>Tenancy: Supports up to one concurrent stream session.                                                                                                                                                                                                      |
   | `gen6n_ultra_win2022` | (NVIDIA, ultra) Supports applications with high 3D scene complexity.<br>Runs applications on Microsoft Windows Server 2022 Base and supports DirectX 12.<br>Compatible with Unreal Engine versions up through 5.6, 32 and 64-bit applications, and anti-cheat technology.<br>Uses NVIDIA L4 Tensor Core GPU.<br>Resources per application: vCPUs: 8. RAM: 32 GB. VRAM: 24 GB.<br>Tenancy: Supports up to one concurrent stream session.                                          |
   | `gen6n_ultra`         | (NVIDIA, ultra) Supports applications with high 3D scene complexity.<br>Uses NVIDIA L4 Tensor Core GPU.<br>Resources per application: vCPUs: 8. RAM: 32 GB. VRAM: 24 GB.<br>Tenancy: Supports up to one concurrent stream session.                                                                                                                                                                                                                                               |
   | `gen6n_high`          | (NVIDIA, high) Supports applications with moderate-to-high 3D scene complexity.<br>Uses NVIDIA L4 Tensor Core GPU.<br>Resources per application: vCPUs: 4. RAM: 16 GB. VRAM: 12 GB.<br>Tenancy: Supports up to two concurrent stream sessions.                                                                                                                                                                                                                                   |
   | `gen6n_medium`        | (NVIDIA, medium) Supports applications with moderate 3D scene complexity.<br>Uses NVIDIA L4 Tensor Core GPU.<br>Resources per application: vCPUs: 2. RAM: 8 GB. VRAM: 6 GB.<br>Tenancy: Supports up to four concurrent stream sessions.                                                                                                                                                                                                                                          |
   | `gen6n_small`         | (NVIDIA, small) Supports applications with lightweight 3D scene complexity and low CPU usage.<br>Uses NVIDIA L4 Tensor Core GPU.<br>Resources per application: vCPUs: 1. RAM: 4 GB. VRAM: 2 GB.<br>Tenancy: Supports up to twelve concurrent stream sessions.                                                                                                                                                                                                                    |
   | `gen5n_win2022`       | (NVIDIA, ultra) Supports applications with extremely high 3D scene complexity.<br>Runs applications on Microsoft Windows Server 2022 Base and supports DirectX 12 and DirectX 11.<br>Supports Unreal Engine up through version 5.6, 32 and 64-bit applications, and anti-cheat technology.<br>Uses NVIDIA A10G Tensor Core GPU.<br>Resources per application: vCPUs: 8. RAM: 32 GB. VRAM: 24 GB.<br>Tenancy: Supports one concurrent stream session.                             |
   | `gen5n_high`          | (NVIDIA, high) Supports applications with moderate-to-high 3D scene complexity.<br>Uses NVIDIA A10G Tensor Core GPU.<br>Resources per application: vCPUs: 4. RAM: 16 GB. VRAM: 12 GB.<br>Tenancy: Supports up to two concurrent stream sessions.                                                                                                                                                                                                                                 |
   | `gen5n_ultra`         | (NVIDIA, ultra) Supports applications with extremely high 3D scene complexity.<br>Uses NVIDIA A10G Tensor Core GPU.<br>Resources per application: vCPUs: 8. RAM: 32 GB. VRAM: 24 GB.<br>Tenancy: Supports one concurrent stream session.                                                                                                                                                                                                                                         |
   | `gen4n_win2022`       | (NVIDIA, ultra) Supports applications with high 3D scene complexity.<br>Runs applications on Microsoft Windows Server 2022 Base and supports DirectX 12 and DirectX 11.<br>Supports Unreal Engine up through version 5.6, 32 and 64-bit applications, and anti-cheat technology.<br>Uses NVIDIA T4 Tensor Core GPU.<br>Resources per application: vCPUs: 8. RAM: 32 GB. VRAM: 16 GB.<br>Tenancy: Supports one concurrent stream session.                                         |
   | `gen4n_high`          | (NVIDIA, high) Supports applications with moderate-to-high 3D scene complexity.<br>Uses NVIDIA T4 Tensor Core GPU.<br>Resources per application: vCPUs: 4. RAM: 16 GB. VRAM: 8 GB.<br>Tenancy: Supports up to two concurrent stream sessions.                                                                                                                                                                                                                                    |
   | `gen4n_ultra`         | (NVIDIA, ultra) Supports applications with high 3D scene complexity.<br>Uses NVIDIA T4 Tensor Core GPU.<br>Resources per application: vCPUs: 8. RAM: 32 GB. VRAM: 16 GB.<br>Tenancy: Supports one concurrent stream session.                                                                                                                                                                                                                                                     | To continue, choose **Next**. |

5. In **Link application**, choose an application that you want to stream, or select "**No application**" to choose one at a later time.
   You can edit the stream group after it has been created to add or remove applications.
   You can only link an application that's in `Ready` status and has a runtime that's compatible with the stream class you've chosen.
   By default, these are the only applications that are shown in the table. To see all applications in `Ready` status, choose `All runtimes` in the drop down list.

###### Note

If you don't see your application listed, then check the current AWS Region
setting. You can only link an application to a stream group that's in the same Region.

To continue, choose **Next**. 6. In **Configure stream settings**, under **Locations and capacity**, choose one or more locations where your stream group will have capacity to stream your application.
By default, the region where you create the stream group, known as the _primary location_, has already been added to your stream group and cannot be removed.
You can add additional locations by checking the box next to each location that you want to add. For lower latency and better quality streaming, you should choose locations closer to your users.

For each location, you can specify its _streaming capacity_. Stream capacity represents the number of concurrent streams that can be active at a time.
You set stream capacity per location in each stream group.

    * **Always-on capacity:**
     This setting, if non-zero, indicates minimum streaming capacity which is allocated to you
     and is never released back to the service. You pay for this base level of capacity at all times,
     whether used or idle.
    * **Maximum capacity:**
     This indicates the maximum capacity that the service can allocate for you. Newly created
     streams may take a few minutes to start. Capacity is released back to the service when
     idle. You pay for capacity that is allocated to you until it is released.
    * **Target-idle capacity:**
     This indicates idle capacity which the service pre-allocates and hold for you in
     anticipation of future activity. This helps to insulate your users from capacity-allocation
     delays. You pay for capacity which is held in this intentional idle state.

You can increase or decrease your total stream capacity at any time to meet changes in user demand for a location by adjusting
either capacity. Amazon GameLift Streams fulfills streaming requests using the idle, pre-allocated resources in the always-on capacity pool if any are
available. If all always-on capacity is in use, Amazon GameLift Streams will provision additional compute resources up to the maximum number specified
in on-demand capacity. As allocated capacity scales, the change is reflected in your total cost for the stream group.

Linked applications will be automatically replicated to each enabled location. An application must finish replicating in a remote location before the remote location can host a stream.
To check on the replication status, open the stream group after it has been created and refer to the **Replication status** column in the table of linked applications.
Click on the current status to see the replication status for each added location.

###### Note

Application data will be stored in all enabled locations including the primary location for this stream group.
Stream session data will be stored in both the primary location and the location where the streaming occurred. 7. In **Review and create stream group**, verify your stream group configuration and make changes as needed. When everything is correct, choose **Create stream group**.

For more information, refer to [Manage streaming with an Amazon GameLift Streams stream group](stream-groups.md "stream-groups.md").

## Step 4: Test your stream in Amazon GameLift Streams

**What is a stream session?**

Refers to the stream itself. This is an instance of a stream that Amazon GameLift Streams transmits from the server to the end-user. A stream session runs on a compute resource, or stream capacity, that a stream group has allocated.
Also referred to as _stream_ for short.

You can see how your application streams by running it directly in the Amazon GameLift Streams console. When you start a stream, Amazon GameLift Streams uses one of the compute resources that your stream group allocates. So, you must have available capacity in your stream group.

###### To test your stream in the Amazon GameLift Streams console

1. Sign in to the AWS Management Console and open the [Amazon GameLift Streams console](https://console.aws.amazon.com/gameliftstreams/ "https://console.aws.amazon.com/gameliftstreams/").
2. You can test a stream in several ways. Start from the **Stream groups** page or **Test stream** page and
   follow these steps:
   1. Select a stream group that you want to use to stream.
   2. If you're starting from the **Stream groups** page, choose **Test stream**.
      If you're starting from the **Test stream** page, select **Choose**.
      This opens the **Test stream** configuration page for the selected stream group.
   3. In **Linked applications**, select an application.
   4. In **Location**, choose a location with available capacity.
   5. (Optional) In **Program configurations**, enter command-line arguments or environment variables to pass to the application as it launches.
   6. Confirm your selection, and choose **Test stream**.

3. After your stream loads, you can do the following actions in your stream:
   1. To connect input, such as your mouse, keyboard, and gamepad (except microphones, which are not supported in **Test stream**), choose **Attach
      input**. You automatically attach your mouse when you move the cursor into the stream window.
   2. To have files that were created during the streaming session exported to an Amazon S3 bucket at the end of the session, choose **Export files** and specify the bucket details.
      Exported files can be found on the **Sessions** page.
   3. To view the stream in fullscreen, choose **Fullscreen**. Press **Escape** to reverse this action.

4. To end the stream, choose **Terminate session**. When the stream disconnects, the stream capacity becomes available to start another stream.

###### Note

The **Test stream** feature in the Amazon GameLift Streams console does not support microphones.

## Step 5: Clean up (don't skip)

###### Avoid unnecessary cost

A stream groups incurs costs when it has allocated capacity, even if that capacity is unused. To
avoid unnecessary costs, scale your stream group capacities to your required size. We suggest during
development you scale your always-on capacity to zero when not in use. For more information, refer to
[Best practices to manage Amazon GameLift Streams costs](pricing.md#pricing-manage-costs "pricing.md#pricing-manage-costs").

After you complete the tutorial and no longer need to stream your application, follow these
steps to clean up your Amazon GameLift Streams resources.

###### To delete a stream group using the Amazon GameLift Streams console

1. Sign in to the AWS Management Console and open the [Amazon GameLift Streams console](https://console.aws.amazon.com/gameliftstreams/ "https://console.aws.amazon.com/gameliftstreams/").
2. To view a list of your existing stream groups, in the navigation pane, choose **Stream groups**.
3. Choose the name of the stream group that you want to delete.
4. On the stream group detail page, choose **Delete**.
5. In the **Delete** dialog box, confirm the delete action.

Amazon GameLift Streams begins releasing compute resources and deleting the stream group. During this time, the stream group is in **Deleting** status. After Amazon GameLift Streams deletes the stream group, you can no longer retrieve it.

###### To delete an application using the Amazon GameLift Streams console

1. Sign in to the AWS Management Console and open the [Amazon GameLift Streams console](https://console.aws.amazon.com/gameliftstreams/ "https://console.aws.amazon.com/gameliftstreams/").
2. In the navigation bar, choose **Applications** to view a list
   of your existing applications. Choose the application you want to delete.
3. In the application detail page, choose **Delete**.
4. In the **Delete** dialog box, confirm the delete action.

Amazon GameLift Streams begins deleting the application. During this time, the application is in `Deleting` status. After Amazon GameLift Streams deletes the application, you can no longer retrieve it.

For more information, refer to [Delete a stream group](stream-groups.md#stream-groups-delete "stream-groups.md#stream-groups-delete") and [Delete an application](applications.md#applications-delete "applications.md#applications-delete").
