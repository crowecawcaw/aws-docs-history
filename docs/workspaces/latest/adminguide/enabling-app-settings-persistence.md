# Enabling application settings

persistence

###### Contents

- [Prerequisites for enabling
  application settings persistence](#prerequisites-app-settings-persistence "#prerequisites-app-settings-persistence")
- [Best practices for
  enabling application settings persistence](#best-practices-app-settings-persistence "#best-practices-app-settings-persistence")
- [How to enable application
  settings persistence](#howto-enable-app-settings-persistence "#howto-enable-app-settings-persistence")

## Prerequisites for enabling

application settings persistence

To enable application settings persistence, you must first do the
following:

- Use an image that was created from a base image published by AWS on or
  after December 7,

2017.

- Enable network connectivity to Amazon S3 from your virtual private cloud (VPC)
  by configuring internet access or a VPC endpoint for Amazon S3. For more
  information, see the _Home Folders and VPC Endpoints_
  section in [Networking and Access for WorkSpaces Pools](managing-network.md "managing-network.md").

## Best practices for

enabling application settings persistence

To enable application settings persistence without providing internet access to
your WorkSpaces, use a VPC endpoint. This endpoint must be in the VPC to which your
WorkSpaces in WorkSpaces Pools are connected. You must attach a custom policy to enable
WorkSpaces Pools access to the endpoint. For information about how to create the custom
policy, see the _Home Folders and VPC Endpoints_ section in [Networking and Access for WorkSpaces Pools](managing-network.md "managing-network.md"). For more
information about private Amazon S3 endpoints, see [VPC Endpoints](../../../vpc/latest/userguide/vpc-endpoints.md "../../../vpc/latest/userguide/vpc-endpoints.md") and
[Endpoints for Amazon S3](../../../vpc/latest/userguide/vpc-endpoints-s3.md "../../../vpc/latest/userguide/vpc-endpoints-s3.md") in the _Amazon VPC User Guide_.

## How to enable application

settings persistence

You can enable or disable application settings persistence while creating a
directory or after the directory is created by using the WorkSpaces console. For each
AWS Region, persistent application settings are stored in an S3 bucket in your
account.

The first time you enable application settings persistence for a directory in an
AWS Region, WorkSpaces Pools creates an S3 bucket in your AWS account in the same
Region. The same bucket stores the application settings VHD file for all users and
all directories in that AWS Region. For more information, see _Amazon S3
Bucket Storage_ in [Administer the VHDs for your users'
application settings](administer-app-settings-vhds.md "administer-app-settings-vhds.md").

###### To enable application settings persistence while creating a directory

- Follow the steps in [Configure SAML 2.0 and create a WorkSpaces Pools
  directory](create-directory-pools.md "create-directory-pools.md"), and make sure that **Enable
  Application Settings Persistence** is selected.

###### To enable application settings persistence for an existing directory

1. Open the WorkSpaces console at [https://console.aws.amazon.com/workspaces/v2/home](https://console.aws.amazon.com/workspaces/v2/home "https://console.aws.amazon.com/workspaces/v2/home").
2. In the left navigation pane, choose **Pools**, and select
   the pool for which to enable application persistence.
3. Choose **Edit** in the **Settings**
   section of the page.
4. In the **Application Persistence** section of the page,
   select **Enable Application settings persistence**.
5. Choose **Save changes**.

New streaming sessions now have application settings persistence enabled.
