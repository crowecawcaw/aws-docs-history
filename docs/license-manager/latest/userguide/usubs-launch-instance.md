

# Launch an instance from a license included AMI
<a name="usubs-launch-instance"></a>

After you have subscribed to a product, you must launch instances for your users to connect to from the AWS Marketplace AMI that includes the product. After you launch an instance, AWS Systems Manager attempts to join the instance to the Active Directory domain and perform additional configuration and hardening on the resource. The configurations to make the instance ready to use can take around 20 minutes to complete. You can confirm the resource is ready to use from the **User association** page of the License Manager console by checking for a **Health status** of **Active** for the instance.

**Important**  
The instances you launch must meet the required prerequisites to be in compliance. Resources that are unable to complete the initial configuration are terminated. For more information, see the [Prerequisites to create user-based subscriptions in License Manager](user-based-subscriptions.md#usubs-prerequisites) and [Troubleshoot user-based subscriptions in License Manager](user-based-subscriptions-troubleshoot.md).

**Launch an instance with user-based subscriptions**

1. Access the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/).

1. Under **Images**, choose **AMI Catalog**.

1. Choose **AWS Marketplace AMIs**.

1. Enter the product name into the search box and press enter. For example, you might search for **Visual Studio**.

1. Under **Publisher**, select **Amazon Web Services**. 

1. Choose **Select** for the product that you want to launch an instance to provide user-based subscriptions.

1. Choose **Continue** to proceed.

1. Choose **Launch Instance with AMI**.

1. Complete the wizard while ensuring that you:

   1. Choose a Nitro based instance type that is not Graviton based.

   1. Choose a VPC and subnet from which your instance can connect to your AWS Managed Microsoft AD directory.

   1. Choose a security group that permits connectivity from your instance to your Active Directory.

   1. Expand **Advanced details** and choose an IAM role that allows Systems Manager functionality for your instance.

1. Choose **Launch instance**.

When you have running instances from the AWS Marketplace AMI, you must subscribe users to the product and associate them with instances, which provide the product so that they can use it.

## Launch an instance from a specific operating system version AMI
<a name="usubs-launch-specific-os-vsn"></a>

When you launch an instance from an AMI that supports Office LTSC Professional Plus, Office LTSC Standard, or Microsoft Visual Studio, the launch defaults to the latest Windows operating system version of the AMI (for example Windows Server 2025). To launch with a specific operating system version AMI, follow these steps.

1. Open the AWS Marketplace console at [https://console.aws.amazon.com/marketplace](https://console.aws.amazon.com/marketplace).

1. Choose **Manage subscriptions** from the navigation pane.

1. To streamline subscription results, you can search for all or part of the subscription name. For example, `Office LTSC Professional Plus`, `Office LTSC Standard`, or `Visual Studio Enterprise`.

1. Select **Launch new instance** from the subscription panel. This opens a launch configuration page.

1. To launch an instance from an AMI that's based on an earlier version of the Windows OS platform, select the **full AWS Marketplace website** link, located under the **Software version**. This takes you to a configuration page where you can select from a list of versions.

1. The list shows the latest AMI versions for the supported Windows OS platforms. Select the Windows OS version that you want to launch from.

## Launch an instance with both Microsoft Office and Microsoft Visual Studio products
<a name="launch-multi-product-instance"></a>

You can launch an EC2 instance that has both Microsoft Office and Microsoft Visual Studio products pre-installed using a single AMI by creating an EC2 Image Builder pipeline through License Manager. The pipeline builds a golden AMI that bundles your selected products — for example, Visual Studio Professional 2022 and Office LTSC Professional Plus 2024 — on a single AMI. You can then launch instances from that AMI with all products ready to use.

### Prerequisites
<a name="launch-multi-product-prereqs"></a>

Before you create EC2 Image Builder pipeline via License Manager, ensure the following:
+ You have active AWS Marketplace subscriptions for at least two user-based subscription products (for example, both a Visual Studio Enterprise subscription and an Office LTSC Professional subscription).
+ You have an EC2 Image Builder infrastructure configuration in your account. This defines the VPC, subnet, security groups, and IAM instance profile that Image Builder uses when building the image. If you don't have one, create it in the [EC2 Image Builder console](https://console.aws.amazon.com/imagebuilder/home#/infrastructureConfigurations/create).

### Step 1: Create a multi-product EC2 image builder pipeline
<a name="launch-multi-product-create-pipeline"></a>

1. Open the License Manager console at [https://console.aws.amazon.com/license-manager/](https://console.aws.amazon.com/license-manager/).

1. In the navigation pane, under **User-based subscriptions**, choose **Products and Pipelines**.

1. Choose the **EC2 Image Builder pipelines** tab.

1. Choose **Create pipeline**.

1. For **Windows version**, select the required Windows Server version.

1. For **Products**, select two or more licensed products to include. Only products you are subscribed to in AWS Marketplace and compatible with the selected Windows version are displayed.

1. For **EC2 Image Builder infrastructure configuration**, select an existing infrastructure configuration from your account.

1. Choose **Create pipeline**.

After creation, License Manager creates the underlying image recipe and pipeline in EC2 Image Builder. You can run the pipeline immediately from the EC2 Image Builder console.

**Note**  
License Manager will only create the pipeline and the corresponding recipe required to build the multi-product AMI. You can manage and update the pipeline through EC2 Image Builder console.

### Step 2: Run the pipeline to produce an AMI
<a name="launch-multi-product-run-pipeline"></a>

1. From the **EC2 Image Builder pipelines** tab, select your pipeline and choose **View in Image Builder**.

1. In the EC2 Image Builder console, choose **Run pipeline** to start a build.

1. Wait for the build to complete.

### Step 3: Launch an instance from the multi-product AMI
<a name="launch-multi-product-launch-instance"></a>

After the pipeline build completes, you can launch an instance from the output AMI using either of the following methods.

**Option A: Launch from the EC2 Image Builder console**  


1. In the EC2 Image Builder console, open the pipeline that completed the build.

1. Under **Output images**, find the AMI produced by the latest build.

1. Choose the AMI link to open it in the EC2 console, then choose **Launch instance from AMI**.

1. Complete the launch wizard while ensuring that you:

   1. Choose a Nitro-based instance type that is not Graviton-based.

   1. Choose a VPC and subnet from which your instance can connect to your AWS Managed Microsoft AD directory.

   1. Choose a security group that permits connectivity from your instance to your Active Directory.

   1. Expand **Advanced details** and choose an IAM role that allows Systems Manager functionality for your instance.

1. Choose **Launch instance**.

**Option B: Launch from the EC2 console**  


1. Access the Amazon EC2 console at [https://console.aws.amazon.com/ec2/](https://console.aws.amazon.com/ec2/).

1. Under **Images**, choose **AMIs**.

1. Find the AMI produced by your pipeline. Pipeline-produced AMIs have names prefixed with `license-manager-created-`.

1. Select the AMI and choose **Launch instance from AMI**.

1. Complete the launch wizard while ensuring that you:

   1. Choose a Nitro-based instance type that is not Graviton-based.

   1. Choose a VPC and subnet from which your instance can connect to your AWS Managed Microsoft AD directory.

   1. Choose a security group that permits connectivity from your instance to your Active Directory.

   1. Expand **Advanced details** and choose an IAM role that allows Systems Manager functionality for your instance.

1. Choose **Launch instance**.

The instance launches with all selected licensed products pre-installed and pre-licensed. After the instance is active in License Manager console, subscribe users to the corresponding products and associate them with the instance so they can use it.