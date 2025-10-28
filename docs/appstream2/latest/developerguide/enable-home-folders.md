# Enable Home Folders for Your AppStream 2.0

Users

Before enabling home folders, you must do the following:

- Check that you have the correct AWS Identity and Access Management (IAM) permissions for Amazon S3
  actions. For more information, see [Using IAM Policies to Manage Administrator Access to the Amazon S3 Bucket for Home Folders and Application Settings Persistence](s3-iam-policy.md "s3-iam-policy.md").
- Use an image that was created from an AWS base image released on or
  after May 18, 2017. For a current list of released AWS images, see [AppStream 2.0 Base Image and Managed Image Update
  Release Notes](base-image-version-history.md "base-image-version-history.md").
- Enable network connectivity to Amazon S3 from your virtual private cloud (VPC)
  by configuring internet access or a VPC endpoint for Amazon S3. For more
  information, see [Networking and Access for Amazon AppStream 2.0](managing-network.md "managing-network.md") and [Using Amazon S3 VPC Endpoints for
  AppStream 2.0 Features](managing-network-vpce-iam-policy.md "managing-network-vpce-iam-policy.md").
  You can enable or disable home folders while creating a stack (see [Create a Stack in Amazon AppStream 2.0](set-up-stacks-fleets-install.md "set-up-stacks-fleets-install.md")), or after the stack is created by
  using the AWS Management Console for AppStream 2.0, AWS SDK, or AWS CLI. For each AWS Region, home
  folders are backed up by an Amazon S3 bucket.

The first time you enable home folders for an AppStream 2.0 stack in an AWS Region, the
service creates an Amazon S3 bucket in your account in that same Region. The same bucket
is used to store the content of home folders for all users and all stacks in that
Region. For more information, see [Amazon S3 Bucket Storage](home-folders-s3.md "home-folders-s3.md").

###### Note

For guidance that you can provide your users to help them get started with
using home folders during AppStream 2.0 streaming sessions, see [Use Home Folders](home-folders-end-user.md "home-folders-end-user.md").

###### To enable home folders while creating a stack

- Follow the steps in [Create a Stack in Amazon AppStream 2.0](set-up-stacks-fleets-install.md "set-up-stacks-fleets-install.md"), and make sure that
  **Enable Home Folders** is selected.

###### To enable home folders for an existing stack

1. Open the AppStream 2.0 console at
   [https://console.aws.amazon.com/appstream2](https://console.aws.amazon.com/appstream2 "https://console.aws.amazon.com/appstream2").
2. In the left navigation pane, choose **Stacks**, and
   select the stack for which to enable home folders.
3. Below the stacks list, choose **Storage** and select
   **Enable Home Folders**.
4. In the **Enable Home Folders** dialog box, choose
   **Enable**.
