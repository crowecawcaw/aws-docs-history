

# Create a WorkSpace using guided setup
<a name="create-workspaces-guided"></a>

Use guided setup to create a personal WorkSpace in the WorkSpaces console without manually configuring each resource. You answer a short set of questions about your use case, and then WorkSpaces recommends a configuration. The guided flow then walks you through provisioning the required resources—the directory, network (VPC and subnets), and the WorkSpace.

Use guided setup when you want WorkSpaces to choose recommended defaults for you. Use the standard [Create a WorkSpace in WorkSpaces Personal](create-workspaces-personal.md) flow when you want to configure every resource yourself.

**What it sets up for you:** the directory (create new or reuse existing) and the network (recommended new VPC and subnets, or reuse existing). It also creates a WorkSpace for your selected user.

**Note**  
Guided setup is not available in the Africa (Cape Town) Region. In that Region, use the standard [Create a WorkSpace in WorkSpaces Personal](create-workspaces-personal.md) flow.
The guided setup flow does not support Bring Your Own License (BYOL) bundles. To create BYOL WorkSpaces, use the standard [Create a WorkSpace in WorkSpaces Personal](create-workspaces-personal.md) flow.

## Prerequisites
<a name="create-workspaces-guided-prerequisites"></a>

Before you use guided setup, make sure that you have the following:
+ Permissions to create WorkSpaces resources in the console. The guided flow requires additional permissions beyond the standard create flow. These include `workspaces:Personalization`, which stores your use-case answers and recommendations to personalize the experience. For the complete list, see [Amazon WorkSpaces Console operations permissions reference](wsp-console-permissions-ref.md).
+ A directory and VPC are optional. The guided flow can create an AWS Managed Microsoft AD directory and a VPC for you, or you can reuse an existing directory or VPC.

## Create a WorkSpace with guided setup
<a name="create-workspaces-guided-create"></a>

**To create a WorkSpace with guided setup**

1. Open the WorkSpaces console at [https://console.aws.amazon.com/workspaces/v2/home](https://console.aws.amazon.com/workspaces/v2/home).

1. In the navigation pane, choose **WorkSpaces**.

1. Choose **Create WorkSpaces**.

1. For **Creation method**, keep **Get a Recommendation**, which is selected by default. (To copy an existing WorkSpace or configure everything manually, see [Create a WorkSpace in WorkSpaces Personal](create-workspaces-personal.md).)

1. Answer the short questionnaire about your use case. WorkSpaces recommends a bundle and configuration, which you can adjust.

1. Set up the directory: choose an existing directory, or let the flow create one for you.

1. Select or create the user to provision the WorkSpace for.

1. Review the remaining settings, and then choose **Create WorkSpaces**.

## Directory provisioning
<a name="create-workspaces-guided-provisioning"></a>

When you choose to create a new directory, the guided flow starts a provisioning workflow that creates the network (VPC and subnets) and an AWS Managed Microsoft AD directory, and registers the directory with WorkSpaces. The console shows each provisioning step as it completes. Creating a new directory can take up to 40 minutes. You can leave the page and return later; provisioning continues in the background. The workflow runs with your IAM permissions, so your role must include the provisioning actions listed in [Amazon WorkSpaces Console operations permissions reference](wsp-console-permissions-ref.md).

## Monitor the WorkSpace creation
<a name="create-workspaces-guided-monitor"></a>

After you choose **Create WorkSpaces**, a status page tracks the WorkSpace creation (typically 10–20 minutes). You can leave the page and check back later. When creation is complete, the WorkSpace status becomes `AVAILABLE`, and the status page shows the registration code and the steps to connect.

## If provisioning does not finish
<a name="create-workspaces-guided-recovery"></a>

If a provisioning step fails, the console shows which step stopped. You can edit your input and retry. If an attempt can't be retried in place, you can discard the retry and start over. Resources created during a failed attempt—such as the VPC, subnets, or directory—are not deleted automatically, and may continue to incur charges until you delete them. Your progress is saved as a draft, so you can leave the flow and resume where you left off.

## Next steps
<a name="create-workspaces-guided-next-steps"></a>

After the WorkSpace is available, you can connect to it, create a custom bundle based on it, and manage its lifecycle. See the following topics for details.
+ [Connect to the WorkSpace](create-workspaces-personal.md#connect-workspace-ad-connector)
+ [Create a custom WorkSpaces image and bundle for WorkSpaces Personal](create-custom-bundle.md)
+ [Administer WorkSpaces Personal](administer-workspaces.md)
+ [Delete a WorkSpace in WorkSpaces Personal](delete-workspaces.md)