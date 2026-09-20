

# Bundle options for WorkSpaces Personal
<a name="bundle-options"></a>

Before selecting a bundle, ensure the bundle you want to select is compatible with your WorkSpaces' protocol, operating system, network, and compute type. For more information about protocols, see [Protocols for Amazon WorkSpaces](https://docs.aws.amazon.com/workspaces/latest/adminguide/amazon-workspaces-protocols.html). For more information about networks, see [Amazon WorkSpaces client network requirements](https://docs.aws.amazon.com/workspaces/latest/adminguide/workspaces-network-requirements.html). 

**Note**  
We recommend not exceeding a 250 ms maximum network latency for PCoIP WorkSpaces. To get the best PCoIP WorkSpaces user experience, we recommend keeping the network latency under 100 ms. When the round-trip time (RTT) exceeds 375 ms, the WorkSpaces client connection will shut down. For the best DCV user experience, we recommend keeping the RTT under 250 ms. If the RTT is between 250 ms and 400 ms, the user can access the WorkSpace, but performance will decrease significantly.
We recommend testing the performance of bundles you want to choose in a test environment by running and using applications that replicate your users' daily tasks.
BYOP (Bring Your Own Protocol) bundles are for WorkSpaces Core. The BYOP bundles provided by Amazon WorkSpaces don't have a WorkSpaces provided streaming protocol installed. You won't be able to connect using WorkSpaces clients or gateways. To understand the shared responsibility model for Amazon WorkSpaces Core, see the [ Technology Partner Integration Guide for Amazon WorkSpaces Core](chrome-extension://efaidnbmnnnibpcajpcglclefindmkaj/https://docs.aws.amazon.com/pdfs/workspaces-core/latest/pg/workspacescore-pg.pdf). For more information, see [ Amazon WorkSpaces Core](https://aws.amazon.com/workspaces-family/core/).
BYOP bundles support nested virtualization. Nested virtualization operates at the hypervisor layer independently of the streaming protocol. We recommend Power (4 vCPU) or higher bundles for the best experience when using nested virtualization. For more information, see [Nested virtualization for WorkSpaces Personal](https://docs.aws.amazon.com/workspaces/latest/adminguide/nested-virtualization.html).

**Important**  
GraphicsPro bundle reaches end-of-life on October 31, 2025. We recommend migrating your GraphicsPro WorkSpaces to supported bundles before October 31, 2025. For more information, see [Migrate a WorkSpace in WorkSpaces Personal](migrate-workspaces.md).
The Graphics bundle will no longer be supported after November 30, 2023. We recommend switching to a supported GPU enabled bundle for WorkSpaces using the Graphics bundle.
Graphics and GraphicsPro bundles aren't currently available in the Asia Pacific (Mumbai) Region.
Plus applications bundles with Office 2016 or Office 2019 will no longer be supported after October 14, 2025. We recommend migrating your WorkSpaces bundles with those Office versions to use Office 2021 or Office 2024. For more information, see [Manage applications in WorkSpaces Personal](manage-applications).

The following are the bundles that WorkSpaces offers:

Each bundle provides the hardware specifications listed in the following table, including vCPU and memory (shown in GiB). For GPU-enabled bundles, the table also lists GPU count and video memory. Bundle specifications are subject to change. For more information about pricing, storage volume sizes, and Region availability, see [Amazon WorkSpaces Pricing](https://aws.amazon.com/workspaces/desktop-as-a-service/pricing/).


| Bundle | vCPU | Memory (GiB) | GPU and video memory | 
| --- | --- | --- | --- | 
| Value | 1 | 2 | Not applicable | 
| Standard | 2 | 4 | Not applicable | 
| Performance | 2 | 8 | Not applicable | 
| Power | 4 | 16 | Not applicable | 
| PowerPro | 8 | 32 | Not applicable | 
| GeneralPurpose.4xlarge | 16 | 64 | Not applicable | 
| GeneralPurpose.8xlarge | 32 | 128 | Not applicable | 
| Graphics.g4dn | 4 | 16 | 1 GPU, 16 GiB video memory | 
| GraphicsPro.g4dn | 16 | 64 | 1 GPU, 16 GiB video memory | 
| Graphics.g6f.large | 2 | 8 | 1/8 GPU, 3 GiB video memory | 
| Graphics.g6f.xlarge | 4 | 16 | 1/8 GPU, 3 GiB video memory | 
| Graphics.g6f.2xlarge | 8 | 32 | 1/4 GPU, 6 GiB video memory | 
| Graphics.g6f.4xlarge | 16 | 64 | 1/2 GPU, 12 GiB video memory | 
| Graphics.gr6f.4xlarge | 16 | 128 | 1/2 GPU, 12 GiB video memory | 
| Graphics.g6.xlarge | 4 | 16 | 1 GPU, 24 GiB video memory | 
| Graphics.g6.2xlarge | 8 | 32 | 1 GPU, 24 GiB video memory | 
| Graphics.g6.4xlarge | 16 | 64 | 1 GPU, 24 GiB video memory | 
| Graphics.g6.8xlarge | 32 | 128 | 1 GPU, 24 GiB video memory | 
| Graphics.g6.16xlarge | 64 | 256 | 1 GPU, 24 GiB video memory | 
| Graphics.gr6.4xlarge | 16 | 128 | 1 GPU, 24 GiB video memory | 
| Graphics.gr6.8xlarge | 32 | 256 | 1 GPU, 24 GiB video memory | 
| Graphics.g7.2xlarge | 8 | 32 | 1 GPU, 32 GiB video memory | 
| Graphics.g7.4xlarge | 16 | 64 | 1 GPU, 32 GiB video memory | 
| Graphics.g7.8xlarge | 32 | 128 | 1 GPU, 32 GiB video memory | 
| Graphics.g7.12xlarge | 48 | 192 | 2 GPUs, 64 GiB video memory | 

## Value bundle
<a name="value"></a>

This bundle is well-suited for the following:
+ Basic text editing and data entry
+ Web browsing with light usage
+ Instant messaging

This bundle is not recommended for word processing, audio and video conferencing, screen sharing, software development tools, business intelligence applications, and graphics applications.

## Standard bundle
<a name="standard"></a>

This bundle is well-suited for the following:
+ Basic text editing and data entry
+ Web browsing
+ Instant messaging
+ Email

This bundle is not recommended for audio and video conferencing, screen sharing, word processing, software development tools, business intelligence applications, and graphics applications.

## Performance bundle
<a name="performance"></a>

This bundle is well-suited for the following:
+ Web browsing
+ Word processing
+ Instant messaging
+ Email
+ Spreadsheets
+ Audio processing
+ Courseware

This bundle is not recommended for video conferencing, screen sharing, software development tools, business intelligence applications, and graphics applications.

## Power bundle
<a name="power"></a>

This bundle is well-suited for the following:
+ Web browsing
+ Word processing
+ Email
+ Instant messaging
+ Spreadsheets
+ Audio processing
+ Software development (Integrated Development Environment (IDE))
+ Entry to mid-level data processing
+ Audio and video conferencing

This bundle is not recommended for screen sharing, software development tools, business intelligence applications, and graphics applications.

## PowerPro bundle
<a name="powerpro"></a>

This bundle is well-suited for the following:
+ Web browsing
+ Word processing
+ Email
+ Instant messaging
+ Spreadsheets
+ Audio processing
+ Software development (Integrated Development Environment (IDE))
+ Data warehousing
+ Business intelligence applications
+ Audio and video conferencing

This bundle is not recommended for machine learning model training, and graphics applications.

## General purpose bundles
<a name="generalpurpose"></a>

These bundles, including GeneralPurpose.4xlarge and GeneralPurpose.8xlarge, are well-suited for the following:
+ Web browsing
+ Word processing
+ Email
+ Instant messaging
+ Spreadsheets
+ Audio processing
+ Software development (Integrated Development Environment (IDE))
+ Data warehousing
+ Business intelligence applications
+ Audio and video conferencing
+ Batch processing
+ CPU-based ML (machine learning) model training

This bundle is not recommended for 3D rendering, photo-realistic design, game streaming, or ML model training for complex models.

## Graphics G7 bundles
<a name="graphicsg7"></a>

The Graphics G7 WorkSpace bundle is powered by NVIDIA RTX PRO 4500 Blackwell Server Edition GPUs. It delivers high GPU performance for graphics and AI inference workloads. Graphics G7 is available for WorkSpaces Personal (using the Amazon DCV protocol) and WorkSpaces Core (using Bring Your Own Protocol (BYOP)). It supports Windows Server 2022, Windows Server 2025, and Windows 11. For more information, see [Amazon EC2 G7 instances](https://aws.amazon.com/ec2/instance-types/g7/).

The Graphics G7 WorkSpace bundle is well-suited for the following use cases:
+ Graphic design
+ CAD/CAM (computer-aided design/computer-aided manufacturing)
+ 3D rendering
+ Video transcoding
+ Game streaming
+ Machine learning (ML) model training and AI inference

**Note**  
Graphics G7 is available in US East (N. Virginia), US East (Ohio), and US West (Oregon).

## Graphics G6 bundles
<a name="graphicsg6"></a>

The G6 WorkSpace bundles utilize NVIDIA L4 GPUs with 3rd generation AMD EPYC (Milan) processors and are available in three variants: G6, Gr6, and G6f. The G6 WorkSpaces feature a standard 1:4 vCPU-to-memory ratio, providing balanced compute and memory resources for general graphics workloads. The Gr6 WorkSpaces offer a 1:8 vCPU-to-memory ratio, delivering double the memory per vCPU for graphics applications with higher memory requirements. The G6f WorkSpaces provide fractional GPU allocation, making them suitable for workloads that do not require full GPU processing capacity for computationally intensive operations. Refer to [Amazon EC2 G6 Instances page](https://aws.amazon.com/ec2/instance-types/g6/) for more information. The G6 WorkSpace bundles support all use cases that existing bundles support, such as daily tasks, data processing and analysis, audio conferencing and software development. Additionally, they enable the following use cases:
+ Graphic design
+ CAD/CAM (computer-aided design/computer-aided manufacturing)
+ Video transcoding
+ 3D rendering
+ Game streaming
+ ML (machine learning) model training and ML inference

## Graphics.g4dn bundle
<a name="graphicsg4dn"></a>

This bundle offers a high level of graphics performance, and moderate level of CPU performance and memory for your WorkSpaces and is well-suited for the following:
+ Web browsing
+ Word processing
+ Email
+ Spreadsheets
+ Instant messaging
+ Audio conferencing
+ Software development (Integrated Development Environment (IDE))
+ Entry to mid-level data processing
+ Data warehousing
+ Business intelligence applications
+ Graphic design
+ CAD/CAM (computer-aided design/computer-aided manufacturing)

This bundle is not recommended for audio and video conferencing, 3D rendering, photo-realistic design, and machine learning model training.

## GraphicsPro.g4dn bundle
<a name="graphicsprog4dn"></a>

This bundle offers a high level of graphics performance, CPU performance, and memory for your WorkSpaces and is well-suited for the following:
+ Web browsing
+ Word processing
+ Email
+ Spreadsheets
+ Instant messaging
+ Audio conferencing
+ Software development (Integrated Development Environment (IDE))
+ Entry to mid-level data processing
+ Data warehousing
+ Business intelligence applications
+ Graphic design
+ CAD/CAM (computer-aided design/computer-aided manufacturing)
+ Video transcoding
+ 3D rendering
+ Photo-realistic design
+ Game streaming
+ ML (machine learning) model training and ML inference

This bundle is not recommended for audio and video conferencing.