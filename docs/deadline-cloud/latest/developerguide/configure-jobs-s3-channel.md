

# Create a conda channel using S3
<a name="configure-jobs-s3-channel"></a>

If your jobs need to run applications not available on the [`deadline-cloud`](https://docs.aws.amazon.com/deadline-cloud/latest/userguide/create-queue-environment.html#conda-queue-environment) channel or the [`conda-forge`](https://conda-forge.org/) channel on the conda-forge website, you can host a custom conda channel to serve your own packages. When you create a queue in the AWS Deadline Cloud (Deadline Cloud) console, the console adds a conda queue environment by default. To make your packages available to jobs, add the custom channel to the queue environment.

A conda channel is static hosted content that you can host in [a variety of ways](https://rattler-build.prefix.dev/latest/publish/) on the prefix.dev website, including on a filesystem or in an Amazon Simple Storage Service (Amazon S3) bucket. If your Deadline Cloud farm uses a shared filesystem for assets, you can use any path on it as a channel name. You can host the channel in an Amazon S3 bucket for broader access using AWS Identity and Access Management (IAM) permissions.

You can [build and test packages locally](build-test-packages-locally.md), then [publish them to a channel](publish-packages-s3-channel.md). Building packages locally is an easy way to start iterating on package build recipes with no infrastructure setup. You can also use a Deadline Cloud [package building queue](automate-package-builds.md) to build packages and publish them to a channel. A package building queue simplifies maintaining packages for multiple operating systems and accelerator configurations. You can update versions and submit full sets of package builds from anywhere.

You can configure channels for your studio and your Deadline Cloud farm in multiple ways. You can have one Amazon S3 channel and configure all your workstations and farm hosts to use it. You can also have more than one channel and set up mirroring with AWS DataSync (DataSync). For example, your Deadline Cloud package building queue can publish to an Amazon S3 channel that gets mirrored on premises for workstations and on-premises farm hosts.

**Topics**
+ [Build and test packages locally](build-test-packages-locally.md)
+ [Publish packages to an Amazon S3 conda channel](publish-packages-s3-channel.md)
+ [Configure production queue permissions for custom conda packages](#s3-channel-configure-permissions)
+ [Add a conda channel to a queue environment](#s3-channel-add-channel)
+ [Create a conda package for an application or plugin](conda-package.md)
+ [Create a conda build recipe for Blender](create-conda-recipe-blender.md)
+ [Create a conda build recipe for Autodesk Maya](create-conda-recipe-maya.md)
+ [Create a conda build recipe for the Maya adaptor](create-conda-recipe-maya-openjd.md)
+ [Create a conda build recipe for Autodesk Maya to Arnold (MtoA) plugin](create-conda-recipe-mtoa-plugin.md)
+ [Automate package builds with Deadline Cloud](automate-package-builds.md)
+ [Sync plugins to Deadline Cloud workers](plugin-sync.md)

## Configure production queue permissions for custom conda packages
<a name="s3-channel-configure-permissions"></a>

Your production queue needs read-only permissions to the `/Conda` prefix in the queue's S3 bucket. Open the AWS Identity and Access Management (IAM) page for the role associated with the production queue and modify the policy with the following:

1. Open the Deadline Cloud console and navigate to the queue details page for the package build queue.

1. Choose the queue service role, then choose **Edit queue**.

1. Scroll to the **Queue service role** section, then choose **View this role in the IAM console**.

1. From the list of permission policies, choose the **AmazonDeadlineCloudQueuePolicy** for your queue.

1. From the **Permissions** tab, choose **Edit**.

1. Add a new section to the queue service role like the following. Replace {{amzn-s3-demo-bucket}} and {{111122223333}} with your own bucket and account.

   ```
   {
      "Effect": "Allow",
      "Sid": "CustomCondaChannelReadOnly",
      "Action": [
       "s3:GetObject",
       "s3:ListBucket"
      ],
      "Resource": [
       "arn:aws:s3:::amzn-s3-demo-bucket",
       "arn:aws:s3:::amzn-s3-demo-bucket/Conda/*"
      ],
      "Condition": {
       "StringEquals": {
        "aws:ResourceAccount": "111122223333"
       }
      }
     },
   ```

## Add a conda channel to a queue environment
<a name="s3-channel-add-channel"></a>

To use the S3 conda channel, you need to add the `s3://amzn-s3-demo-bucket/Conda/Default` channel location to the `CondaChannels` parameter of jobs that you submit to Deadline Cloud. The submitters provided with Deadline Cloud provide fields to specify custom conda channels and package.

You can avoid modifying every job by editing the conda queue environment for your production queue. Use the following procedure:

1. Open the Deadline Cloud console and navigate to the queue details page for the production queue.

1. Choose the environments tab.

1. Select the **Conda** queue environment, and then choose **Edit**.

1. Choose the **JSON editor**, and then in the script, find the parameter definition for `CondaChannels`.

1. Edit the line `default: "deadline-cloud"` so that it starts with the newly created S3 conda channel:

   ```
   default: "s3://amzn-s3-demo-bucket/Conda/Default deadline-cloud"
   ```

Service-managed fleets enable flexible channel priority for conda by default. For a job requesting `blender=4.5` if Blender 4.5 is in both the new channel and the `deadline-cloud` channel, the package will be pulled from whichever channel is first in the channel list. If a specified package version is not found in the first channel then subsequent channels will be checked in order for the package version.

For customer-managed fleets, you can enable the use of conda packages by using one of the conda queue environment samples in the Deadline Cloud samples repository. For more information, see the [conda queue environment samples](https://github.com/aws-deadline/deadline-cloud-samples/blob/mainline/queue_environments/README.md) on the GitHub website.