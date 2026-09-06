

# Bring Your Own Windows Desktop Licenses for Amazon WorkSpaces Applications
<a name="byol-windows-images"></a>

Amazon WorkSpaces Applications now supports Windows Desktop operating systems (such as Windows 11) through Bring Your Own License (BYOL). You can use your existing Windows Desktop OS licenses and custom images with Amazon WorkSpaces Applications. This lets you stream business-critical applications that require Microsoft Windows Desktop OS while using your current licensing investments.

## Overview
<a name="byol-overview"></a>

With BYOL for Amazon WorkSpaces Applications, you can:
+ **Migrate Windows 11 applications** that are non-compliant with Windows Server editions to AWS and stream them to your users
+ **Reduce costs** by leveraging existing Microsoft VDA E3/E5 licenses, eliminating duplicate licensing and saving RDS SAL fee per user per month compared to non-BYOL options
+ **Maintain full compliance** with Microsoft licensing requirements — AWS provisions dedicated hardware for your BYOL instances

## How it works
<a name="byol-how-it-works"></a>

BYOL for Amazon WorkSpaces Applications reuses the existing Amazon WorkSpaces BYOL infrastructure. This means:
+ If you are **already using BYOL on Amazon WorkSpaces**, you can simply import your existing BYOL images into Amazon WorkSpaces Applications
+ If you are **new to Amazon WorkSpaces BYOL**, you first set up your dedicated BYOL account in Amazon WorkSpaces, create an image, and then import that image into Amazon WorkSpaces Applications
+ **Shared dedicated infrastructure** — Customers use the same BYOL dedicated infrastructure for both WorkSpaces and Amazon WorkSpaces Applications

For detailed information on setting up BYOL in Amazon WorkSpaces, see [Bring Your Own Windows Desktop Licenses in WorkSpaces](https://docs.aws.amazon.com/workspaces/latest/adminguide/byol-windows-images.html).

## Prerequisites
<a name="byol-prerequisites"></a>

Before you begin, verify the following:
+ **Licensing requirement** — Your Microsoft licensing agreement allows Windows to run in a virtual hosted environment. VDA E3/E5 user licenses (purchased under subscription from Microsoft) are required for Windows Desktop Client BYOL on AWS. See [Amazon Web Services and Microsoft](https://aws.amazon.com/windows/resources/licensing/).
+ **Minimum WorkSpaces instances commitment** — You must use a minimum of 50 WorkSpaces per Region. These 50 WorkSpaces can be any mix of AlwaysOn/On-Demand Amazon WorkSpaces Applications unique users streaming sessions, and/or WorkSpaces Personal instances in the same region per month.
+ **Windows versions supported** — You will need a Windows virtual machine image or Windows ISO image file that uses a supported Windows OS version.
+ **Network connectivity** — Ensure required HTTPS endpoints are accessible for the image import process.

## Supported Windows Versions
<a name="byol-supported-windows-versions"></a>

The following Windows 11 versions are supported for Amazon WorkSpaces Applications BYOL:
+ Windows 11 Version 24H2 (October 2024 release)
+ Windows 11 Version 25H2 (September 2025 release)

**Note**  
Windows 10 images imported through WorkSpaces are not supported for Amazon WorkSpaces Applications. Only Windows 11 images can be used with Amazon WorkSpaces Applications.

## Getting Started
<a name="byol-getting-started"></a>

If your account is already enabled for BYOL, you do not need to provision new dedicated infrastructure to run Amazon WorkSpaces Applications fleets powered by Windows Desktop OS. You can skip **Step 1**. Amazon WorkSpaces Applications will use the same dedicated BYOL account for provisioning the fleets. The same dedicated hardware that supports your existing WorkSpaces Personal or Pools BYOL workloads can be used for Amazon WorkSpaces Applications.

### Step 1: Enable your account for BYOL (First time only)
<a name="byol-step1"></a>

1. Log in to the AWS Console

1. Choose the Region where you want to enable BYOL

1. Navigate to **Services** → **Amazon WorkSpaces** → **Account Settings** (in the left navigation)

1. In the **Bring Your Own License (BYOL)** section, choose **Get Started with BYOL**

1. Choose **Enable account for BYOL** and confirm the minimum requirements

1. **Choose IP range (First time only)** — Select an IP/CIDR range for your BYOL management network interface. Once chosen, it cannot be altered.

For detailed steps on image import, see [Bring Your Own Windows Desktop Licenses in WorkSpaces](https://docs.aws.amazon.com/workspaces/latest/adminguide/byol-windows-images.html).

**Note**  
Graphics BYOL enablement is not yet supported through the WorkSpaces Console. Please create an AWS Support ticket for Graphics BYOL.

**Note**  
BYOL enablement is shared between WorkSpaces and Amazon WorkSpaces Applications through the unified "Account Settings" interface.

### Step 2: Create a BYOL image in Amazon WorkSpaces
<a name="byol-step2"></a>

#### Option A: For existing WorkSpaces BYOL customers
<a name="byol-step2-option-a"></a>

If you already have BYOL images in Amazon WorkSpaces, you can skip directly to **Step 3** to import your existing images into Amazon WorkSpaces Applications.

#### Option B: For new BYOL Customers
<a name="byol-step2-option-b"></a>
+ **(Optional) Validate your image before importing** — If you are importing a customized virtual machine image, run the WorkSpaces Image Checker tool to ensure compatibility. If importing a Windows ISO, you can skip this step.
+ **Import the image** — After enabling BYOL, choose **Import Image**. You have three options:
  + **VM import** — Imports a virtual machine image (VHDX, VMDK, or OVF file) that has already been customized
  + **ISO import** — Imports a Windows ISO image downloaded from Microsoft that has not been customized
  + **AMI import** — Imports an existing Amazon EC2 AMI to use as your BYOL image

For detailed steps on image import, see [Bring Your Own Windows Desktop Licenses in WorkSpaces](https://docs.aws.amazon.com/workspaces/latest/adminguide/byol-windows-images.html).

### Step 3: Import BYOL Image into Amazon WorkSpaces Applications
<a name="byol-step3"></a>

Once your BYOL image is successfully created in Amazon WorkSpaces:

1. Navigate to the **Amazon WorkSpaces Applications Console**. Note: Your console role will also need to include the `workspaces:DescribeWorkspaceImages` permission.

1. Go to **Images** → **Import Image**

1. Select **Amazon WorkSpaces Image** as the image source. Enter the WorkSpaces Image ID (starts with "wsi-").

1. Provide image details (name, display name, description)

1. Complete the import process

**Note**  
At the time of launch, you can import your Windows 11 and Windows Server 2022/Server 2025 images into Amazon WorkSpaces Applications.

### Step 4: Customize your image (Optional)
<a name="byol-step4"></a>

You can optionally use Image Builder to configure custom applications, optimize launch performance, and create a snapshot to produce a custom image:

1. Launch an Image Builder instance from your imported BYOL image

1. Connect to the Image Builder and install/configure your applications

1. Create a snapshot to generate your customized image

### Step 5: Create fleet and stream to users
<a name="byol-step5"></a>

1. Navigate to the **Fleets** console in Amazon WorkSpaces Applications

1. Create a fleet using your BYOL image

1. Configure fleet settings (instance type, scaling policies, etc.)

1. Once the fleet is ready, your end users can start streaming from BYOL instances

## Supported instance types
<a name="byol-supported-instance-types"></a>

The following instance types are available for BYOL Amazon WorkSpaces Applications:
+ **Standard:** stream.standard.medium, stream.standard.large, stream.standard.xlarge, stream.standard.2xlarge
+ **Compute-optimized:** stream.compute.large, stream.compute.xlarge, stream.compute.2xlarge, stream.compute.4xlarge, stream.compute.8xlarge
+ **Memory-optimized:** stream.memory.large, stream.memory.xlarge, stream.memory.2xlarge, stream.memory.4xlarge, stream.memory.8xlarge
+ **Graphics (requires separate approval):** stream.graphics.g6 and stream.graphics.g7 families

## Region availability
<a name="byol-region-availability"></a>

Windows BYOL for Amazon WorkSpaces Applications is available in all regions where both Amazon WorkSpaces Applications and WorkSpaces Personal are offered:
+ US East (N. Virginia)
+ US East (Ohio)
+ US West (Oregon)
+ Asia Pacific (Malaysia)
+ Asia Pacific (Mumbai)
+ Asia Pacific (Seoul)
+ Asia Pacific (Singapore)
+ Asia Pacific (Sydney)
+ Asia Pacific (Tokyo)
+ Canada (Central)
+ Europe (Frankfurt)
+ Europe (Ireland)
+ Europe (London)
+ Europe (Paris)
+ Israel (Tel Aviv)
+ South America (São Paulo)
+ AWS GovCloud (US-West)
+ AWS GovCloud (US-East)

## Important considerations
<a name="byol-important-considerations"></a>
+ **Dedicated infrastructure** — BYOL images powered by Windows Desktop OS (Windows 11) run on dedicated infrastructure only. Windows Server OS images continue to run on shared infrastructure.
+ **No multi-session support** — Multi-session Windows 11 is not available due to Microsoft licensing restrictions.
+ **Image sharing** — You can share BYOL images only with AWS accounts that are enabled for BYOL and are part of your organization (under the same payer account).
+ **Separate BYOL account not required** — You can use your existing AWS account for Amazon WorkSpaces Applications BYOL workloads. The same dedicated infrastructure account (DP account) can host WorkSpaces Personal, WorkSpaces Pools, and Amazon WorkSpaces Applications.
+ **Image operations** — Import creates images in both WorkSpaces and Amazon WorkSpaces Applications (if selected). Copy, update, and delete operations are service-specific and do not reflect across services.

**Note**  
Streaming from Interface VPC Endpoints is currently not supported for fleets powered by Windows Desktop operating system (such as Windows 11).

## Frequently asked questions
<a name="byol-faq"></a>

Can I use my existing BYOL WorkSpaces images with Amazon WorkSpaces Applications?  
Yes. You can import your existing WorkSpaces Personal/Pools images into Amazon WorkSpaces Applications. The image OS and version must be supported by Amazon WorkSpaces Applications (Windows 11 and Windows Server 2022/Server 2025 at launch).

Can I use existing Amazon WorkSpaces Applications images for BYOL?  
No. Existing Amazon WorkSpaces Applications images are for Windows Server operating systems, whereas BYOL is for Windows Desktop operating systems only.

How can I provide software updates to my end users?  
You can use the managed image updates procedure to get an automated way to update your image with the latest Windows OS updates, driver updates, and Amazon WorkSpaces Applications agent software.

Can I delete a BYOL image?  
Yes, you can delete a BYOL image if there is no active fleet or Image Builder referencing it. Deletion removes the image from the respective service only.