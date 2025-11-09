# Create a conda channel using S3

If you have custom packages for applications that are not available on the
`deadline-cloud` or `conda-forge` channels you can create a conda
channel that contains the packages that your environments use. You can store the packages in
an Amazon S3 bucket and use AWS Identity and Access Management permissions to control access to the channel.

You can use a Deadline Cloud queue to build the packages for your conda channel to make it
easier to update and maintain the application packages.

A key benefit of this approach is that your package building queue can create packages
for multiple different operating systems, and with or without CUDA support. By comparison,
if you build packages on your workstation, you need to create and manage
different workstations for these cases.

The following examples show how to create a conda channel that provides and application
for your environments. The application in the examples is Blender 4.2, but any
of the Deadline Cloud integrated applications can be used.

You can use an AWS CloudFormation template to create a Deadline Cloud farm that includes a package building
queue, or you can follow the instructions below to create the example farm yourself. For the
AWS CloudFormation template, see [A starter AWS Deadline Cloud farm](https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/cloudformation/farm_templates/starter_farm "https://github.com/aws-deadline/deadline-cloud-samples/tree/mainline/cloudformation/farm_templates/starter_farm")
in the Deadline Cloud samples repository on GitHub.

###### Topics

- [Create a package building queue](#s3-channel-create-queue "#s3-channel-create-queue")
- [Configure production queue permissions
  for custom conda packages](#s3-channel-configure-permissions "#s3-channel-configure-permissions")
- [Add a conda channel to a queue environment](#s3-channel-add-channel "#s3-channel-add-channel")
- [Create a conda package for an application](conda-package.md "conda-package.md")
- [Create a conda build recipe for
  Blender](create-conda-recipe-blender.md "create-conda-recipe-blender.md")
- [Create a conda build recipe for Autodesk Maya](create-conda-recipe-maya.md "create-conda-recipe-maya.md")
- [Create a conda build recipe for Autodesk Maya to Arnold (MtoA) plugin](create-conda-recipe-mtoa-plugin.md "create-conda-recipe-mtoa-plugin.md")

## Create a package building queue

In this example you create a Deadline Cloud queue to build the Blender 4.2 application. This
simplifies delivery of the finished packages to the Amazon S3 bucket used as the conda channel
and lets you use your existing fleet to build the package. This reduces the number of
infrastructure components to manage.

Follow the instructions in [Create a queue](../userguide/create-queue.md "../userguide/create-queue.md") in the
_Deadline Cloud User Guide_. Make the following changes:

- In step 5, choose an existing S3 bucket. Specify a root folder name such as
  `DeadlineCloudPackageBuild` so that build artifacts stay separate
  from your normal Deadline Cloud attachments.
- In step 6, you can associate the package building queue with an existing fleet, or
  you can create an entirely new fleet if your current fleet is unsuitable.
- In step 9, create a new service role for your package building queue. You will
  modify the permissions to give the queue the permissions required for uploading packages
  and reindexing a conda channel.

### Configure the package building queue

permissions

To allow the package build queue to access the `/Conda` prefix in the
queue's S3 bucket, you must modify the queue's role to give it read/write access. The role
needs the following permissions so that package build jobs can upload new packages and
reindex the channel.

- `s3:GetObject`
- `s3:PutObject`
- `s3:ListBucket`
- `s3:GetBucketLocation`
- `s3:DeleteObject`

1. Open the Deadline Cloud console and navigate to the queue details page for the package
   build queue.
2. Choose the queue service role, then choose **Edit queue**.
3. Scroll to the **Queue service role** section, then choose
   **View this role in the IAM console**.
4. From the list of permission policies, choose the
   **AmazonDeadlineCloudQueuePolicy** for your queue.
5. From the **Permissions** tab, choose
   **Edit**.
6. Update the queue service role to the following. Replace
   `amzn-s3-demo-bucket` and
   `111122223333` with your own bucket and
   account.

```
{
   "Effect": "Allow",
   "Sid": "CustomCondaChannelReadWrite",
   "Action": [
    "s3:GetObject",
    "s3:PutObject",
    "s3:DeleteObject",
    "s3:ListBucket",
    "s3:GetBucketLocation"
   ],
   "Resource": [
    "arn:aws:s3:::amzn-s3-demo-bucket",
    "arn:aws:s3:::amzn-s3-demo-bucket/Conda/*"			],
   "Condition": {
    "StringEquals": {
     "aws:ResourceAccount": "111122223333"
    }
   }
  },
```

## Configure production queue permissions

for custom conda packages

Your production queue needs read-only permissions to the `/Conda` prefix in
the queue's S3 bucket. Open the AWS Identity and Access Management (IAM) page for the role associated with the
production queue and modify the policy with the following:

1. Open the Deadline Cloud console and navigate to the queue details page for the package build
   queue.
2. Choose the queue service role, then choose **Edit queue**.
3. Scroll to the **Queue service role** section, then choose
   **View this role in the IAM console**.
4. From the list of permission policies, choose the
   **AmazonDeadlineCloudQueuePolicy** for your queue.
5. From the **Permissions** tab, choose
   **Edit**.
6. Add a new section to the queue service role like the following. Replace
   `amzn-s3-demo-bucket` and
   `111122223333` with your own bucket and
   account.

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

To use the S3 conda channel, you need to add the
`s3://amzn-s3-demo-bucket/Conda/Default` channel location to the
`CondaChannels` parameter of jobs that you submit to Deadline Cloud. The submitters
provided with Deadline Cloud provide fields to specify custom conda channels and package.

You can avoid modifying every job by editing the conda queue environment for your
production queue. For a service-managed queue, use the following procedure:

1. Open the Deadline Cloud console and navigate to the queue details page for the production
   queue.
2. Choose the environments tab.
3. Select the **Conda** queue environment, and then choose
   **Edit**.
4. Choose the **JSON editor**, and then in the script, find the parameter
   definition for `CondaChannels`.
5. Edit the line `default: "deadline-cloud"` so that it starts with the
   newly created S3 conda channel:

```
default: "s3://amzn-s3-demo-bucket/Conda/Default deadline-cloud"
```

Service-managed fleets enable flexible channel priority for conda by default. For a
job requesting `blender=4.2` if Blender 4.2 is in both the new channel and the
`deadline-cloud` channel, the package will be pulled from whichever channel
is first in the channel list. If a specified package version is not found in the first
channel then subsequent channels will be checked in order for the package version.

For customer-managed fleets, you can enable the use of conda packages by using one of
the [Conda queue environment samples](https://github.com/aws-deadline/deadline-cloud-samples/blob/mainline/queue_environments/README.md "https://github.com/aws-deadline/deadline-cloud-samples/blob/mainline/queue_environments/README.md") in the Deadline Cloud samples GitHub repository.
