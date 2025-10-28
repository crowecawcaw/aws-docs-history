# Configuring AWS Systems Manager to install the EFS

client

There are two one-time configurations required to set up Systems Manager to automatically install or
update the `amazon-efs-utils` package.

1. Configure an AWS Identity and Access Management (IAM) instance profile with the required permissions.
2. Configure an Association (including the schedule) used for installation or updates by the
   State Manager.

## Step 1: Configure an IAM instance

profile with the required permissions

By default, AWS Systems Manager doesn't have permission to manage your Amazon EFS clients and
install or update the amazon-efs-utils package. You must grant access to Systems Manager by using an
AWS Identity and Access Management (IAM) instance profile. An instance profile is a container that passes IAM role
information to an Amazon EC2 (EC2) instance at launch.

Use the `AmazonElasticFileSystemsUtils` AWS managed permission policy to
assign the appropriate permissions to roles. You can create a new role for your instance
profile or add the `AmazonElasticFileSystemsUtils` permission policy to an existing
role. You must then use this instance profile to launch your EC2 instances. For more
information, see [Configure instance
permissions required for Systems Manager](../../../systems-manager/latest/userguide/setup-instance-permissions.md "../../../systems-manager/latest/userguide/setup-instance-permissions.md").

## Step 2: Configure an association used by State

Manager

The `amazon-efs-utils` package is included with Distributor and is
ready for you to deploy to managed EC2 instances. To view the latest version of
`amazon-efs-utils` that is available for installation, you can use the
AWS Systems Manager console or your preferred AWS command line tool. To access Distributor, open the
[https://console.aws.amazon.com/systems-manager/](https://console.aws.amazon.com/systems-manager/ "https://console.aws.amazon.com/systems-manager/") and choose **Distributor** in the left navigation pane.
Locate **AmazonEFSUtils** in the **Owned by Amazon** section.
Choose **AmazonEFSUtils** to see the package details. For more information,
see [View
packages](../../../systems-manager/latest/userguide/distributor-view-packages.md "../../../systems-manager/latest/userguide/distributor-view-packages.md").

Using State Manager, you can install or update the `amazon-efs-utils`
package on your managed EC2 instances immediately or on a schedule. Additionally, you
can ensure that `amazon-efs-utils` is automatically installed on new
EC2 instances. For more information about installation or updating packages using
Distributor and State Manager, see [Working with
Distributor](../../../systems-manager/latest/userguide/distributor-working-with.md "../../../systems-manager/latest/userguide/distributor-working-with.md").

To automatically install or update the amazon-efs-utils package on instances using the
Systems Manager console, see [Scheduling a package installation or update (console)](../../../systems-manager/latest/userguide/distributor-working-with-packages-deploy.md#distributor-deploy-sm-pkg-console "../../../systems-manager/latest/userguide/distributor-working-with-packages-deploy.md#distributor-deploy-sm-pkg-console"). This will prompt you to create
an association for State Manager, which defines the state you want to apply to a set of
instances. Use the following inputs when you create your association:

- For **Parameters** choose **Action** >
  **Install** and **Installation Type** > **In-place
  update**.
- For **Targets** the recommended setting is **Choose all
  instances** to register all new and existing EC2 instances as targets to
  automatically install or update **AmazonEFSUtils**. Alternatively, you can
  specify instance tags, select instances manually, or choose a resource group to apply the
  association to a subset of instances. If you specify instance tags, you must launch your
  EC2 instances with the tags to allows AWS Systems Manager to automatically install
  or update the Amazon EFS client.
- For **Specify schedule** the recommended setting for
  **AmazonEFSUtils** is every 30 days. You can use controls to create a cron
  or rate schedule for the association.

To use AWS Systems Manager to mount EFS file systems to multiple EC2 instances,
see [Mounting EFS to multiple
EC2 instances](mount-multiple-ec2-instances.md "mount-multiple-ec2-instances.md") .
