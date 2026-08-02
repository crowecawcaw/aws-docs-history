# Getting started: initial setup

This section walks you through the initial setup of Scenario Discovery: accessing the
console and creating a workspace.

## Accessing Scenario Discovery

You access Scenario Discovery through the AWS IoT SiteWise console. Navigate to AWS IoT SiteWise and open
Scenario Discovery from the left navigation menu near the bottom. Choose
**Get Started** to explore the benefits, features, use cases,
and how Scenario Discovery works.

![AWS IoT SiteWise console with Scenario Discovery in the navigation menu](images/sd-image2.png)

![Scenario Discovery benefits, features, and use cases overview](images/sd-image3.png)

You can now create a workspace.

![Scenario Discovery get started page](images/sd-image4.png)

## What is a workspace?

A workspace is a data tenancy concept that allows you to maintain multiple data-isolated
tenants within a single AWS account. You can use workspaces to track usage, billing,
resources, and datasets as they relate to your specific projects. You can identify resources,
storage, and usage on a per-project basis and develop, version, and maintain per-project
environments independently of one another, all within one AWS account.

## Creating your workspace

A workspace is your team's dedicated, isolated environment. Workspace Admins configure
access control, environment isolation, and data governance policies.

To create a workspace, complete the following steps:

1. From the Scenario Discovery console, choose **Create
   Workspace**.
2. Enter a workspace name and optional description.
3. Review and choose **Create workspace**.

![Workspaces management view showing active environments](images/sd-image5.png)

![Creating a workspace and signing up with your email](images/sd-image6.png)

![Linking an existing user account to your new workspace](images/sd-image7.png)

![Configuring workspace name and encryption settings](images/sd-image8.png)

For creating an encrypted workspace with your own KMS keys, see
[Encryption at rest](sd-encryption.md "sd-encryption.md") for instructions.

![Verifying your new workspace in the workspaces list](images/sd-image9.png)

![Overview of the workspace created](images/sd-image10.png)

You have now created a workspace.
