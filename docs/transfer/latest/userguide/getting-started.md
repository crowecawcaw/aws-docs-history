# Getting started with AWS Transfer Family server endpoints

Use this tutorial to get started with AWS Transfer Family (Transfer Family). You'll learn how to create
an SFTP-enabled server with publicly accessible endpoint using Amazon S3 storage, add a user
with service-managed authentication, and transfer a file with Cyberduck.

###### Topics

- [Prerequisites](#getting-started-prerequisites "#getting-started-prerequisites")
- [Step 1: Sign in to the AWS Transfer Family
  console](#getting-started-logging-in "#getting-started-logging-in")
- [Step 2: Create an SFTP-enabled
  server](#getting-started-server "#getting-started-server")
- [Step 3: Add a service managed user](#getting-started-user "#getting-started-user")
- [Step 4: Transfer a file using a
  client](#getting-started-transfer-file "#getting-started-transfer-file")

## Prerequisites

Before you begin, be sure to complete the requirements in [Prerequisites](setting-up.md "setting-up.md"). As part of this setup, you
create an Amazon Simple Storage Service (Amazon S3) bucket and an AWS Identity and Access Management (IAM) user role.

There are permissions required for using the AWS Transfer Family console, and there are
permissions required for configuring other AWS services that Transfer Family uses, such as
Amazon Simple Storage Service, AWS Certificate Manager, Amazon Elastic File System, and Amazon Route 53. For example, for users that are
transferring files into and out of AWS using Transfer Family,
**AmazonS3FullAccess** grants permissions to setup and use an
Amazon S3 bucket. Some of the permissions in this policy are needed to create Amazon S3
buckets.

To use the Transfer Family console, you require the following:

- **AWSTransferConsoleFullAccess** grants permissions for
  your SFTP user to create Transfer Family resources.
- **IAMFullAccess** (or specifically a policy that allows
  creation of IAM roles) is only needed if you want Transfer Family to automatically
  create a logging role for your server in Amazon CloudWatch Logs or a user role for a user
  logging into a server.
- To create and delete VPC server types, you need to add the actions
  **ec2:CreateVpcEndpoint** and
  **ec2:DeleteVpcEndpoints** to your policy. For
  information about limiting VPC endpoint access for security purposes, see
  [Limiting VPC endpoint access for Transfer Family
  servers](create-server-in-vpc.md#limit-vpc-endpoint-access "create-server-in-vpc.md#limit-vpc-endpoint-access").

###### Note

The **AmazonS3FullAccess** and
**IAMFullAccess** polices are, themselves, not needed for
general usage of AWS Transfer Family. They are presented here as a simple way to make sure
that all of the permissions that you need are covered. Additionally, these are
AWS managed policies, which are standard policies that are available to all
AWS customers. You can view the individual permissions in these policies and
determine a minimal set that you need for your purposes.

## Step 1: Sign in to the AWS Transfer Family

console

###### To sign in to Transfer Family

1. Sign in to the AWS Management Console and open the AWS Transfer Family console at [https://console.aws.amazon.com/transfer/](https://console.aws.amazon.com/transfer/ "https://console.aws.amazon.com/transfer/").
2. For **Account ID or alias**, enter the ID for your
   AWS account.
3. For **IAM user name**, enter the name of the user role
   that you created for Transfer Family.
4. For **Password**, enter your AWS account
   password.
5. Choose **Sign in**.

## Step 2: Create an SFTP-enabled

server

Secure Shell (SSH) File Transfer Protocol (SFTP) is a network protocol used for
secure transfer of data over the internet. The protocol supports the full security
and authentication functionality of SSH. It is widely used to exchange data,
including sensitive information between business partners in a variety of industries
such as financial services, healthcare, retail, and advertising.

###### To create an SFTP-enabled server

1. Select **Servers** from the Navigation pane then choose
   **Create server**.
2. In **Choose protocols**, select
   **SFTP**, and then choose **Next**.
3. In **Choose an identity provider**, choose
   **Service managed** to store user identities and keys
   in Transfer Family, and then choose **Next**.
4. In **Choose an endpoint**, do the following:
   1. For **Endpoint type**, choose the
      **Publicly accessible** endpoint type.
   2. For **Custom hostname**, choose
      **None**.
   3. Choose **Next**.

5. In **Choose a domain**, choose **Amazon
   S3**.
6. In **Configure additional details**, for
   **Cryptographic algorithm options**, choose a security
   policy that contains the cryptographic algorithms enabled for use by your
   server. Our latest security policy is the default: for details, see
   [Security policies for AWS Transfer Family servers](security-policies.md "security-policies.md").

###### Note

Only if you are adding a managed workflow for your server, choose
**Create a new role** for **CloudWatch
logging**. To log server events, you do not need to create
an IAM role. 7. In **Review and create**, choose **Create
server**. You are taken to the **Servers**
page.

It can take a couple of minutes before the status for your new server changes to
**Online**. At that point, your server can perform file operations,
but you'll need to create a user first. For details on creating users, see
[Managing users for server endpoints](create-user.md "create-user.md").

## Step 3: Add a service managed user

###### To add a user to the SFTP-enabled server

1. On the **Servers** page, select the server that you want
   to add a user to.
2. Choose **Add user**.
3. In the **User configuration** section, for
   **Username**, enter the username. This
   username must be a minimum of 3 and a maximum of 100 characters. You can use the following
   characters in the username: a–z, A-Z, 0–9, underscore '\_',
   hyphen '-', period '.' and at sign '@'. The username can't start with
   a hyphen '-', period '.' or at sign '@'.
4. For **Access**, choose the IAM role that you created in
   [Create an IAM role and policy](requirements-roles.md "requirements-roles.md").
   This IAM role includes an IAM policy that contains permissions to access
   your Amazon S3 bucket, as well as a trust relationship with the AWS Transfer Family service.
   The procedure outlined in [To establish a trust relationship](requirements-roles.md#establish-trust-transfer "requirements-roles.md#establish-trust-transfer") shows how to establish the
   proper trust relationship.
5. For **Policy**, choose **None**.
6. For **Home directory**, choose the Amazon S3 bucket where you
   want to store the data that you transfer using AWS Transfer Family. Enter the path to
   the `home` directory. This is the directory that your users see
   when they log in using their client.

We recommend using a directory path that contains the username so that you
have the option to use a session policy. A session policy limits a user's
access in the Amazon S3 bucket to that user's `home` directory.
For more information about using session policies, see [How session policies work](requirements-roles.md#session-policy "requirements-roles.md#session-policy").

If you prefer, you can keep this parameter blank to use your Amazon S3 bucket's
`root` directory. If you choose this option, make sure that
your IAM role provides access to the`root` directory. 7. Select the **Restricted** check box to prevent your users
from accessing anything outside of their `home` directory. This
also prevents users from seeing the Amazon S3 bucket name or folder name. 8. For **SSH public key**, enter the public SSH key portion
of the SSH key pair in `ssh-rsa
 `<string>`` format.

Your key must be validated by the service before you can add your new
user. For more information about how to generate an SSH key pair, see [Generate SSH keys for service-managed users](sshkeygen.md "sshkeygen.md"). 9. (Optional) For **Key** and **Value**,
enter one or more tags as key-value pairs, and choose **Add
tag**. 10. Choose **Add** to add your new user to the server that
you chose.

The new user appears in the **Users** section of the
**Server details** page.

## Step 4: Transfer a file using a

client

You transfer files over the AWS Transfer Family service by specifying the transfer operation
in a client. AWS Transfer Family supports several clients. For details, see [Transferring files over a server endpoint using a
client](transfer-file.md "transfer-file.md")

This section contains procedures for using Cyberduck and OpenSSH.

###### Topics

- [Use Cyberduck](#cyberduck "#cyberduck")
- [Use OpenSSH](#openssh "#openssh")

### Use Cyberduck

###### To transfer files over AWS Transfer Family using Cyberduck

1. Open the [Cyberduck](https://cyberduck.io/download/ "https://cyberduck.io/download/")
   client.
2. Choose **Open Connection**.
3. In the **Open Connection** dialog box, choose
   **SFTP (SSH File Transfer Protocol)**.
4. For **Server**, enter your server endpoint. The
   server endpoint is located on the **Server details**
   page, see [View SFTP, FTPS, and FTP server
   details](configuring-servers-view-info.md "configuring-servers-view-info.md").
5. For **Port number**, enter `22`
   for SFTP.
6. For **Username**, enter the name for the user that
   you created in [Managing users for server endpoints](create-user.md "create-user.md").
7. For **SSH Private Key**, choose or enter the SSH
   private key.
8. Choose **Connect**.
9. Perform your file transfer.

Depending on where your files are, do one of the following:

    * In your local directory (the source), choose the files that
     you want to transfer, and drag and drop them into the Amazon S3
     directory (the target).
    * In the Amazon S3 directory (the source), choose the files that you
     want to transfer, and drag and drop them into your local
     directory (the target).

### Use OpenSSH

Use the instructions that follow to transfer files from the command line using
OpenSSH.

###### Note

This client works only with an SFTP-enabled server.

###### To transfer files over AWS Transfer Family using the OpenSSH command line

utility

1. On Linux or Macintosh, open a command terminal.
2. At the prompt, enter the following command: `% sftp -i
transfer-key sftp_user@service_endpoint`

In the preceding command, `sftp_user` is the username and
`transfer-key` is the SSH private key. Here,
`service_endpoint` is the server's endpoint as shown
in the AWS Transfer Family console for the selected server.

An `sftp` prompt should appear. 3. (Optional) To view the user's home directory, enter the following
command at the `sftp` prompt: `sftp> pwd` 4. On the next line, enter the following text: `sftp> cd
 /`amzn-s3-demo-bucket`/home/sftp_user`

In this getting-started exercise, this Amazon S3 bucket is the target of
the file transfer. 5. On the next line, enter the following command: `sftp> put
 filename.txt`

The `put` command transfers the file into the Amazon S3
bucket.

A message like the following appears, indicating that the file
transfer is in progress, or complete.

`Uploading filename.txt to
 /amzn-s3-demo-bucket/home/sftp_user/filename.txt`

`some-file.txt 100% 127 0.1KB/s 00:00`
