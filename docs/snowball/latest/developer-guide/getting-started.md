AWS Snowball Edge is no longer available to new customers. New customers should explore [AWS DataSync](https://aws.amazon.com/datasync/ "https://aws.amazon.com/datasync/") for online transfers, [AWS Data Transfer Terminal](https://aws.amazon.com/data-transfer-terminal/ "https://aws.amazon.com/data-transfer-terminal/") for
secure physical transfers, or AWS Partner solutions. For edge computing, explore [AWS Outposts](https://aws.amazon.com/outposts/ "https://aws.amazon.com/outposts/").

# Getting started with Snowball Edge

With an AWS Snowball Edge device, you can access the storage and compute power of the AWS Cloud locally and cost effectively in places where connecting to the internet
might not be an option. You can also transfer hundreds of terabytes or petabytes of data
between your on-premises data centers and Amazon Simple Storage Service (Amazon S3).

Following, you can find general instructions for creating and completing your first
AWS Snowball Edge device job in the AWS Snow Family Management Console. The console presents the most common workflows,
separated into job types. You can find more information about specific components of the
AWS Snowball Edge device in this documentation. For an overview of the service as a whole, see [How AWS Snowball Edge works](how-it-works.md "how-it-works.md").

It may take up to 4 weeks to provision and prepare the Snowball Edge for your job before
it is shipped. This timeline should be factored into your project plan to ensure a seamless
transition.

Before you can get started, you must create an AWS account and an
administrator user in AWS Identity and Access Management (IAM). For information, see [Prerequisites for using Snowball Edge](snowball-prereqs.md "snowball-prereqs.md").

###### Topics

- [Creating a job to order a Snowball Edge device](create-job-common.md "create-job-common.md")
- [Cancelling a job to order a Snowball Edge](cancel-job-order.md "cancel-job-order.md")
- [Cloning a job to order a Snowball Edge in the
  AWS Snow Family Management Console](clonejob.md "clonejob.md")
- [Receiving the Snowball Edge](receive-device.md "receive-device.md")
- [Connecting a Snowball Edge to your local
  network](#getting-started-connect "#getting-started-connect")
- [Getting credentials to access a Snowball Edge](#get-credentials "#get-credentials")
- [Unlocking the Snowball Edge](unlockdevice.md "unlockdevice.md")
- [Setting up local users on a Snowball Edge](#setup-local-iam "#setup-local-iam")
- [Rebooting the Snowball Edge device](reboot.md "reboot.md")
- [Powering off the Snowball Edge](turnitoff.md "turnitoff.md")
- [Returning the Snowball Edge device](return-device.md "return-device.md")
- [Return shipping for Snowball Edge](mailing-storage.md "mailing-storage.md")
- [Monitoring the import status from the
  Snowball Edge](monitor-status.md "monitor-status.md")
- [Getting your data transfer job completion report and
  logs](report.md "report.md")

## Connecting a Snowball Edge to your local

network

Using the following procedure, you connect the AWS Snowball Edge device to your local network.
The device doesn't need to be connected to the internet. The device has three doors: a
front, a back, and a top.

###### To connect the device to your network

1. Open the front and back doors, sliding them inside the device door slots.
   Doing this gives you access to the touch screen on the LCD display embedded in
   the front of the device, and the power and network ports in the back.

###### Note

Don't close the front and back doors while you're using the Snowball Edge
device. The open doors allow air to cool the device. Closing the doors while
using the device may cause the device to shut down to prevent
overheating. 2. Open the top door and remove the provided power cable from the cable nook, and
plug the device into power. 3. Choose one of your RJ45, SFP+, or QSFP+ network cables, and plug the device
into your network. The network ports are on the back of the device. 4. Power on the AWS Snowball Edge device by pressing the power button above the LCD
display. 5. When the device is ready, the LCD display shows a short video while the device
is getting ready to start. After about 10 minutes, the device is ready to be
unlocked. 6. (Optional) Change the default network settings through the LCD display by
choosing **CONNECTION**.

You can change your IP address to a different static address, which you
provide by using the following procedure.

To troubleshoot boot-up problems, see [Troubleshooting boot‐up problems with Snowball Edge](boot-troubleshoot.md "boot-troubleshoot.md").

###### To change the IP address of an AWS Snowball Edge device

1. On the LCD display, choose **CONNECTION**.

A screen appears that shows you the current network settings for the
AWS Snowball Edge device. The IP address below the drop-down box is automatically updated
to reflect the DHCP address that the AWS Snowball Edge device requested. 2. (Optional) Change the IP address to a static IP address. You can also keep it
as is.

The device is now connected to your network.

###### Important

To prevent corrupting your data, don't disconnect the AWS Snowball Edge device or change
its connection settings while it's in use.

**Next:**
[Getting credentials to access a Snowball Edge](#get-credentials "#get-credentials")

## Getting credentials to access a Snowball Edge

Each job has a set of credentials that you must get from the AWS Snow Family Management Console or the
job management API to authenticate your access to the Snowball Edge. These credentials are an
encrypted manifest file and an associated unlock code. The manifest file contains important
information about the job and permissions associated with it.

###### Note

You get your credentials after the device is in transit to you. You can see the status of your job in the AWS Snow Family Management Console. For more information, see [Statuses of Snowball Edge jobs](jobstatuses.md "jobstatuses.md").

###### To get your credentials using the console

1. Sign in to the AWS Management Console and open the [AWS Snow Family Management Console](https://console.aws.amazon.com/snowfamily/home "https://console.aws.amazon.com/snowfamily/home").
2. On the console, search the table for the specific job to download the job
   manifest for, and then choose that job.
3. Expand that **Job status** pane, and choose
   **View job details**.
4. In the details pane that appears, expand **Credentials**
   and then do the following:
   - Make a note of the unlock code (including the hyphens), because
     you need to provide all 29 characters to unlock the device.
   - In the dialog box, choose **Download manifest**,
     and follow the instructions to download the job manifest file to your
     computer. The name of your manifest file includes your **Job
     ID**.

###### Note

We recommend that you don't save a copy of the unlock code in the same
location in the computer as the manifest for that job. For more
information, see [Best practices for using a Snowball Edge device](BestPractices.md "BestPractices.md").

Now that you have your credentials, the next step is to download the
Snowball Edge client, which is used to unlock the AWS Snowball Edge device.

**Next:**
[Downloading and installing the Snowball Edge
Client](using-client-commands.md#download-the-client "using-client-commands.md#download-the-client")

## Setting up local users on a Snowball Edge

Following are steps to set up a local administrator on your AWS Snowball Edge device.

1. **Retrieve your root user credentials**

Use the `snowballEdge list-access-keys` and `snowballEdge
 get-secret-access-key` to get your local credentials. For more
information, see [Getting credentials for a Snowball Edge](using-client-commands.md#client-credentials "using-client-commands.md#client-credentials"). 2. **Configure the root user credential using `aws
 configure`**

Supply the `AWS Access Key ID`, `AWS Secret Access
 Key`, and `Default region name`. The region name must be
`snow`. Optionally supply a `Default output format`.
For more information about configuring the AWS CLI, see [Configuring the AWS CLI](../../../cli/latest/userguide/cli-chap-configure.md "../../../cli/latest/userguide/cli-chap-configure.md") in
the _AWS Command Line Interface User Guide_. 3. **Create one or more local users on your
device**

Use the `create-user` command to add users to your device.

```

aws iam create-user --endpoint `endpointIPaddress`:6078 --region snow --user-name `UserName` --profile `ProfileID`

```

After you add users according to your business needs, you can store your
AWS root credentials in a safe location and only use them for
account and service management tasks. For more information about creating
IAM users, see [Creating an
IAM user in your AWS account](../../../IAM/latest/UserGuide/id_users_create.md "../../../IAM/latest/UserGuide/id_users_create.md") in the
_IAM User Guide_. 4. **Create an access key for your user**

###### Warning

This scenario requires IAM users with programmatic access and long-term credentials, which presents a security risk. To help mitigate this risk, we recommend that you provide these users with only the permissions they require to perform the task and that you remove these users when they are no longer needed. Access keys can be updated if necessary. For more information, see [Update access keys](../../../IAM/latest/UserGuide/id-credentials-access-keys-update.md "../../../IAM/latest/UserGuide/id-credentials-access-keys-update.md") in the _IAM User Guide_.

Use the `create-access-key` command to create an access key for
your user.

```

aws iam create-access-key --endpoint `endpointIPaddress`:6078 --region snow --user-name `UserName` --profile `ProfileID`

```

Save the access key information to a file and distribute to your users. 5. **Create an access policy**

You might want different users to have different levels of access to
functionality on your device. The following example creates a policy document
named `s3-only-policy` and attaches it to a user.

JSON

```
`{
 "Version":"2012-10-17",
 "Statement": [
 {
 "Effect": "Allow",
 "Action": "s3:*",
 "Resource": "*"
 }
 ]
}`

```

```

aws iam create-policy --endpoint `endpointIPaddress`:6078 --region snow --policy-name s3-only-policy --policy-document file://s3-only-policy --profile `ProfileID`

```

6. **Attach the policy to your user**

Use the `attach-user-policy` to attach the s3-only-policy to a
user.

```

  aws iam attach-user-policy --endpoint `endpointIPaddress`:6078 --region snow --user-name `UserName` --policy-arn arn:aws:iam::`AccountID`:`policy/POLICYNAME` --profile `ProfileID`

```

For more information about using IAM locally, see [Using IAM locally on a Snowball Edge](using-local-iam.md "using-local-iam.md").
