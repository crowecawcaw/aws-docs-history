

# Set Defaults from the SageMaker AI Console for Amazon SageMaker Studio Classic
<a name="studio-lcc-defaults-console"></a>

**Important**  
Custom IAM policies that allow Amazon SageMaker Studio or Amazon SageMaker Studio Classic to create Amazon SageMaker resources must also grant permissions to add tags to those resources. The permission to add tags to resources is required because Studio and Studio Classic automatically tag any resources they create. If an IAM policy allows Studio and Studio Classic to create resources but does not allow tagging, "AccessDenied" errors can occur when trying to create resources. For more information, see [Provide permissions for tagging SageMaker AI resources](security_iam_id-based-policy-examples.md#grant-tagging-permissions).  
[AWS managed policies for Amazon SageMaker AI](security-iam-awsmanpol.md) that give permissions to create SageMaker resources already include permissions to add tags while creating those resources.

**Note**  
As of November 30, 2023, the previous Amazon SageMaker Studio experience is now named Amazon SageMaker Studio Classic. The following section is specific to using the Studio Classic application. For information about using the updated Studio experience, see [Amazon SageMaker Studio](studio-updated.md).  
Studio Classic is still maintained for existing workloads but is no longer available for onboarding. You can only stop or delete existing Studio Classic applications and cannot create new ones. We recommend that you [migrate your workload to the new Studio experience](studio-updated-migrate.md).

You can set default lifecycle configuration scripts from the SageMaker AI console for the following resources.
+ Domains
+ User profiles

You cannot set default lifecycle configuration scripts for shared spaces from the SageMaker AI console. For information about setting defaults for shared spaces, see [Set Defaults from the AWS CLI for Amazon SageMaker Studio Classic](studio-lcc-defaults-cli.md).

The following sections outline how to set default lifecycle configuration scripts from the SageMaker AI console.

**Topics**
+ [Prerequisites](#studio-lcc-defaults-cli-prerequisites)
+ [Set a default lifecycle configuration for a domain](#studio-lcc-defaults-cli-domain)
+ [Set a default lifecycle configuration for a user profile](#studio-lcc-defaults-cli-user-profile)

## Prerequisites
<a name="studio-lcc-defaults-cli-prerequisites"></a>

Before you begin, complete the following prerequisites:
+ Onboard to SageMaker AI domain by following the steps in [Amazon SageMaker AI domain overview](gs-studio-onboard.md).
+ Create a lifecycle configuration following the steps in [Create and Associate a Lifecycle Configuration with Amazon SageMaker Studio Classic](studio-lcc-create.md).

## Set a default lifecycle configuration for a domain
<a name="studio-lcc-defaults-cli-domain"></a>

The following procedure shows how to set a default lifecycle configuration for a domain from the SageMaker AI console.

1. Open the Amazon SageMaker AI console at [https://console.aws.amazon.com/sagemaker/](https://console.aws.amazon.com/sagemaker/).

1. From the list of domains, select the name of the domain to set the default lifecycle configuration for.

1. From the **Domain details** page, choose the **Environment** tab.

1. Under **Lifecycle configurations for personal Studio apps**, select the lifecycle configuration that you want to set as the default for the domain. You can set distinct defaults for JupyterServer and KernelGateway applications.

1. Choose **Set as default**. This opens a pop up window that lists the current defaults for JupyterServer and KernelGateway applications.

1. Choose **Set as default** to set the lifecycle configuration as the default for its respective application type.

## Set a default lifecycle configuration for a user profile
<a name="studio-lcc-defaults-cli-user-profile"></a>

The following procedure shows how to set a default lifecycle configuration for a user profile from the SageMaker AI console.

1. Open the Amazon SageMaker AI console at [https://console.aws.amazon.com/sagemaker/](https://console.aws.amazon.com/sagemaker/).

1. From the list of domains, select the name of the domain that contains the user profile that you want to set the default lifecycle configuration for.

1. From the **Domain details** page, choose the **User profiles** tab.

1. Select the name of the user profile to set the default lifecycle configuration for. This opens a **User Details** page.

1. From the **User Details** page, choose **Edit**. This opens an **Edit user profile** page.

1. From the **Edit user profile** page, choose **Step 2 Studio settings**.

1. Under **Lifecycle configurations attached to user**, select the lifecycle configuration that you want to set as the default for the user profile. You can set distinct defaults for JupyterServer and KernelGateway applications.

1. Choose **Set as default**. This opens a pop up window that lists the current defaults for JupyterServer and KernelGateway applications.

1. Choose **Set as default** to set the lifecycle configuration as the default for its respective application type.