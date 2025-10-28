# Create a Lifecycle Configuration from the SageMaker AI

Console for Amazon SageMaker Studio Classic

###### Important

Custom IAM policies that allow Amazon SageMaker Studio or Amazon SageMaker Studio Classic to create Amazon SageMaker
resources must also grant permissions to add tags to those resources. The permission to
add tags to resources is required because Studio and Studio Classic automatically tag
any resources they create. If an IAM policy allows Studio and Studio Classic to
create resources but does not allow tagging, "AccessDenied" errors can occur when
trying to create resources. For more information, see [Provide permissions for tagging SageMaker AI
resources](security_iam_id-based-policy-examples.md#grant-tagging-permissions "security_iam_id-based-policy-examples.md#grant-tagging-permissions").

[AWS managed policies for Amazon SageMaker AI](security-iam-awsmanpol.md "security-iam-awsmanpol.md")
that give permissions to create SageMaker resources already include permissions to add tags
while creating those resources.

###### Important

As of November 30, 2023, the previous Amazon SageMaker Studio experience is now named
Amazon SageMaker Studio Classic. The following section is specific to using the Studio Classic application. For
information about using the updated Studio experience, see [Amazon SageMaker Studio](studio-updated.md "studio-updated.md").

Studio Classic is still maintained for existing
workloads but is no longer available for onboarding. You can only stop or delete existing Studio Classic
applications and cannot create new ones. We recommend that you [migrate your workload to the new Studio experience](studio-updated-migrate.md "studio-updated-migrate.md").

The following topic shows how to create a lifecycle configuration from the Amazon SageMaker AI
console to automate customization for your Studio Classic environment.

## Prerequisites

Before you can begin this tutorial, complete the following prerequisite:

- Onboard to Amazon SageMaker Studio Classic. For more information, see [Onboard to Amazon SageMaker Studio Classic](gs-studio-onboard.md "gs-studio-onboard.md").

## Step 1: Create a new lifecycle

configuration

You can create a lifecycle configuration by entering a script from the Amazon SageMaker AI
console.

###### Note

Each script can have up to **16,384
characters**.

The following procedure shows how to create a lifecycle configuration script that
prints `Hello World`.

1. Open the Amazon SageMaker AI console at [https://console.aws.amazon.com/sagemaker/](https://console.aws.amazon.com/sagemaker/ "https://console.aws.amazon.com/sagemaker/").
2. On the left navigation pane, choose **Admin configurations**.
3. Under **Admin configurations**, choose **Lifecycle configurations**.
4. Choose the **Studio** tab.
5. Choose **Create configuration**.
6. Under **Select configuration type**, select the type of
   application that the lifecycle configuration should be attached to. For more
   information about selecting which application to attach the lifecycle
   configuration to, see [Set Default Lifecycle Configurations for Amazon SageMaker Studio Classic](studio-lcc-defaults.md "studio-lcc-defaults.md").
7. Choose **Next**.
8. In the section called **Configuration settings**, enter a
   name for your lifecycle configuration.
9. In the **Scripts** section, enter the following
   content.

```
#!/bin/bash
set -eux
echo 'Hello World!'
```

10. (Optional) Create a tag for your lifecycle configuration.
11. Choose **Submit**.

## Step 2: Attach the lifecycle

configuration to a domain or user profile

Lifecycle configuration scripts associated at the domain level are inherited by all
users. However, scripts that are associated at the user profile level are scoped to a
specific user.

You can attach multiple lifecycle configurations to a domain or user profile for both
JupyterServer and KernelGateway applications.

###### Note

To attach a lifecycle configuration to a shared space, you must use the AWS CLI. For
more information, see [Create a Lifecycle Configuration from the
AWS CLI for Amazon SageMaker Studio Classic](studio-lcc-create-cli.md "studio-lcc-create-cli.md").

The following sections show how to attach a lifecycle configuration to your domain or
user profile.

### Attach to a domain

The following shows how to attach a lifecycle configuration to your existing
domain from the SageMaker AI console.

1. Open the Amazon SageMaker AI console at [https://console.aws.amazon.com/sagemaker/](https://console.aws.amazon.com/sagemaker/ "https://console.aws.amazon.com/sagemaker/").
2. On the left navigation pane, choose **Admin configurations**.
3. Under **Admin configurations**, choose **domains**.
4. From the list of domains, select the domain to attach the
   lifecycle configuration to.
5. From the **Domain details**, choose the
   **Environment** tab.
6. Under **Lifecycle configurations for personal Studio
   apps**, choose **Attach**.
7. Under **Source**, choose **Existing
   configuration**.
8. Under **Studio lifecycle configurations**, select the
   lifecycle configuration that you created in the previous step.
9. Select **Attach to domain**.

### Attach to your user

profile

The following shows how to attach a lifecycle configuration to your existing user
profile.

1. Open the Amazon SageMaker AI console at [https://console.aws.amazon.com/sagemaker/](https://console.aws.amazon.com/sagemaker/ "https://console.aws.amazon.com/sagemaker/").
2. On the left navigation pane, choose **Admin configurations**.
3. Under **Admin configurations**, choose **domains**.
4. From the list of domains, select the domain that contains the user
   profile to attach the lifecycle configuration to.
5. Under **User profiles**, select the user profile.
6. From the **User Details** page, choose
   **Edit**.
7. On the left navigation, choose **Studio
   settings**.
8. Under **Lifecycle configurations attached to user**,
   choose **Attach**.
9. Under **Source**, choose **Existing
   configuration**.
10. Under **Studio lifecycle configurations**, select the
    lifecycle configuration that you created in the previous step.
11. Choose **Attach to user profile**.

## Step 3: Launch an application with the

lifecycle configuration

After you attach a lifecycle configuration to a domain or user profile, you can launch
an application with that attached lifecycle configuration. Choosing which lifecycle
configuration to launch with depends on the application type.

- JupyterServer: When launching a JupyterServer
  application from the console, SageMaker AI always uses the default lifecycle
  configuration. You can't use a different lifecycle configuration when launching
  from the console. For information about changing the default lifecycle
  configuration after launching a JupyterServer application, see [Set Default Lifecycle Configurations for Amazon SageMaker Studio Classic](studio-lcc-defaults.md "studio-lcc-defaults.md").

To select a different attached lifecycle configuration, you must launch with
the AWS CLI. For more information about launching a JupyterServer application with
an attached lifecycle configuration from the AWS CLI, see [Create a Lifecycle Configuration from the
AWS CLI for Amazon SageMaker Studio Classic](studio-lcc-create-cli.md "studio-lcc-create-cli.md").

- KernelGateway: You can select any of the attached lifecycle configurations
  when launching a KernelGateway application using the Studio Classic Launcher.

The following procedure describes how to launch a KernelGateway application with an
attached lifecycle configuration from the SageMaker AI console.

1. Open the Amazon SageMaker AI console at [https://console.aws.amazon.com/sagemaker/](https://console.aws.amazon.com/sagemaker/ "https://console.aws.amazon.com/sagemaker/").
2. Launch Studio Classic. For more information, see [Launch Amazon SageMaker Studio Classic](studio-launch.md "studio-launch.md").
3. In the Studio Classic UI, open the Studio Classic Launcher. For more information, see
   [Use the Amazon SageMaker Studio Classic Launcher](studio-launcher.md "studio-launcher.md").
4. In the Studio Classic Launcher, navigate to the **Notebooks and compute
   resources** section.
5. Click the **Change environment** button.
6. On the **Change environment** dialog, use the dropdown menus
   to select your **Image**, **Kernel**,
   **Instance type**, and a **Start-up
   script**. If there is no default lifecycle configuration, the
   **Start-up script** value defaults to `No
script`. Otherwise, the **Start-up script** value is
   your default lifecycle configuration. After you select a lifecycle
   configuration, you can view the entire script.
7. Click **Select**.
8. Back to the Launcher, click the **Create notebook** to launch
   a new notebook kernel with your selected image and lifecycle
   configuration.

## Step 4: View logs for a lifecycle

configuration

You can view the logs for your lifecycle configuration after it has been attached to a
domain or user profile.

1. First, provide access to CloudWatch for your AWS Identity and Access Management (IAM) role. Add read
   permissions for the following log group and log stream.
   - Log group:`/aws/sagemaker/studio`
   - Log stream:``domain`/`user-profile`/`app-type`/`app-name`/LifecycleConfigOnStart`

For information about adding permissions, see [Enabling logging from certain AWS services](../../../AmazonCloudWatch/latest/logs/AWS-logs-and-resource-policy.md "../../../AmazonCloudWatch/latest/logs/AWS-logs-and-resource-policy.md"). 2. From within Studio Classic, navigate to the **Running
Terminals and Kernels** icon (
![Black square icon representing a placeholder or empty image.](images/studio/icons/running-terminals-kernels.png)
) to monitor your lifecycle configuration. 3. Select an application from the list of running applications. Applications with
attached lifecycle configurations have an attached indicator icon
![Code brackets symbol representing programming or markup languages.](images/studio/studio-lcc-indicator-icon.png)
. 4. Select the indicator icon for your application. This opens a new panel that
lists the lifecycle configuration. 5. From the new panel, select `View logs`. This opens a new tab that
displays the logs.
