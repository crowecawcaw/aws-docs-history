

# Getting started: initial setup
<a name="sd-setup"></a>

This section walks you through the initial setup of Scenario Discovery: accessing the console and creating a workspace.

## Accessing Scenario Discovery
<a name="sd-accessing"></a>

You access Scenario Discovery through the AWS IoT SiteWise console. Navigate to AWS IoT SiteWise and open Scenario Discovery from the left navigation menu near the bottom. Choose **Get Started** to explore the benefits, features, use cases, and how Scenario Discovery works.

![AWS IoT SiteWise console with Scenario Discovery in the navigation menu](http://docs.aws.amazon.com/iot-sitewise/latest/userguide/images/sd-image2.png)


![Scenario Discovery benefits, features, and use cases overview](http://docs.aws.amazon.com/iot-sitewise/latest/userguide/images/sd-image3.png)


You can now create a workspace.

![Scenario Discovery get started page](http://docs.aws.amazon.com/iot-sitewise/latest/userguide/images/sd-image4.png)


## What is a workspace?
<a name="sd-what-is-workspace"></a>

A workspace is a data tenancy concept that allows you to maintain multiple data-isolated tenants within a single AWS account. You can use workspaces to track usage, billing, resources, and datasets as they relate to your specific projects. You can identify resources, storage, and usage on a per-project basis and develop, version, and maintain per-project environments independently of one another, all within one AWS account.

## Creating your workspace
<a name="sd-creating-workspace"></a>

A workspace is your team's dedicated, isolated environment. Workspace Admins configure access control, environment isolation, and data governance policies.

To create a workspace, complete the following steps:

1. From the Scenario Discovery console, choose **Create Workspace**.

1. Enter a workspace name and optional description.

1. Review and choose **Create workspace**.

![Workspaces management view showing active environments](http://docs.aws.amazon.com/iot-sitewise/latest/userguide/images/sd-image5.png)


![Creating a workspace and signing up with your email](http://docs.aws.amazon.com/iot-sitewise/latest/userguide/images/sd-image6.png)


![Linking an existing user account to your new workspace](http://docs.aws.amazon.com/iot-sitewise/latest/userguide/images/sd-image7.png)


![Configuring workspace name and encryption settings](http://docs.aws.amazon.com/iot-sitewise/latest/userguide/images/sd-image8.png)


For creating an encrypted workspace with your own KMS keys, see [Encryption at rest](sd-encryption.md) for instructions.

![Verifying your new workspace in the workspaces list](http://docs.aws.amazon.com/iot-sitewise/latest/userguide/images/sd-image9.png)


![Overview of the workspace created](http://docs.aws.amazon.com/iot-sitewise/latest/userguide/images/sd-image10.png)


You have now created a workspace.