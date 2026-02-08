# Bundle options for WorkSpaces Personal

Before selecting a bundle, ensure the bundle you want to select is compatible with
your WorkSpaces' protocol, operating system, network, and compute type. For more information
about protocols, see [Protocols for Amazon WorkSpaces](amazon-workspaces-protocols.md "amazon-workspaces-protocols.md"). For more information about networks, see [Amazon WorkSpaces client network requirements](workspaces-network-requirements.md "workspaces-network-requirements.md").

###### Note

- We recommend not exceeding a 250 ms maximum network latency for PCoIP
  WorkSpaces. To get the best PCoIP WorkSpaces user experience, we recommend keeping the
  network latency under 100 ms. When the round-trip time (RTT) exceeds 375 ms,
  the WorkSpaces client connection will shut down. For the best DCV user experience, we recommend keeping the RTT under 250 ms.
  If the RTT is between 250 ms and 400 ms, the user can access the WorkSpace,
  but performance will decrease significantly.
- We recommend testing the performance of bundles you want to choose in a
  test environment by running and using applications that replicate your
  users' daily tasks.
- BYOP (Bring Your Own Protocol) bundles are for WorkSpaces Core. The BYOP
  bundles provided by Amazon WorkSpaces don't have a WorkSpaces provided streaming protocol
  installed. You won't be able to connect using WorkSpaces clients or gateways.
  To understand the shared responsibility model for Amazon WorkSpaces Core, see the
  [Technology Partner Integration Guide for Amazon WorkSpaces Core](chrome-extension://efaidnbmnnnibpcajpcglclefindmkaj/https://docs.aws.amazon.com/pdfs/workspaces-core/latest/pg/workspacescore-pg.pdf "chrome-extension://efaidnbmnnnibpcajpcglclefindmkaj/https://docs.aws.amazon.com/pdfs/workspaces-core/latest/pg/workspacescore-pg.pdf").
  For more information, see [Amazon WorkSpaces Core](https://aws.amazon.com/workspaces-family/core/ "https://aws.amazon.com/workspaces-family/core/").

###### Important

- GraphicsPro bundle reaches end-of-life on October 31, 2025. We recommend
  migrating your GraphicsPro WorkSpaces to supported bundles before October 31,

2025. For more information, see [Migrate a WorkSpace in WorkSpaces Personal](migrate-workspaces.md "migrate-workspaces.md").

- The Graphics bundle will no longer be supported after November 30, 2023.
  We recommend switching to a supported GPU enabled bundle for WorkSpaces using the
  Graphics bundle.
- Graphics and GraphicsPro bundles aren't currently available in the
  Asia Pacific (Mumbai) Region.
- Plus applications bundles with Office 2016 or Office 2019 will no longer be supported after October 14, 2025. We recommend migrating your WorkSpaces bundles with those Office version to use Office 2021 or Office 2024. For more information, see, [Manage applications in WorkSpaces Personal](manage-applications.md "manage-applications.md").
  The following are the bundles that WorkSpaces offers. For information about bundles in
  WorkSpaces, see [Amazon WorkSpaces Bundles](https://aws.amazon.com/workspaces/details/#Amazon_WorkSpaces_Bundles "https://aws.amazon.com/workspaces/details/#Amazon_WorkSpaces_Bundles").

This bundle is well-suited for the following:

- Basic text editing and data entry
- Web browsing with light usage
- Instant messaging
  This bundle is not recommended for word processing, audio and video conferencing, screen sharing, software development tool,
  business intelligence applications, and graphics applications.

This bundle is well-suited for the following:

- Basic text editing and data entry
- Web browsing
- Instant messaging
- Email
  This bundle is not recommended for audio and video conferencing, screen sharing,
  word processing, software development tool, business intelligence applications,
  and graphics applications.

This bundle is well-suited for the following:

- Web browsing
- Word processing
- Instant messaging
- Email
- Spreadsheets
- Audio processing
- Courseware
  This bundle is not recommended for video conferencing, screen sharing,
  software development tool, business intelligence applications, and graphics
  applications.

This bundle is well-suited for the following:

- Web browsing
- Word processing
- Email
- Instant messaging
- Spreadsheets
- Audio processing
- Software development (Integrated Development Environment (IDE))
- Entry to mid-level data processing
- Audio and video conferencing
  This bundle is not recommended for screen sharing, software development tool, business intelligence applications,
  and graphics applications.

This bundle is well-suited for the following:

- Web browsing
- Word processing
- Email
- Instant messaging
- Spreadsheets
- Audio processing
- Software development (Integrated Development Environment (IDE))
- Data warehousing
- Business intelligence applications
- Audio and video conferencing
  This bundle is not recommended for machine learning model training, and graphics applications.

These bundles, including GeneralPurpose.4xlarge and GeneralPurpose.8xlarge,
are well-suited for the following:

- Web browsing
- Word processing
- Email
- Instant messaging
- Spreadsheets
- Audio processing
- Software development (Integrated Development Environment (IDE))
- Data warehousing
- Business intelligence applications
- Audio and video conferencing
- Batch processing
- CPU-based ML (machine learning) model training
  This bundle is not recommended for 3D rendering, photo-realistic design,
  game streaming, or ML model training for complex models.

The G6 WorkSpace bundles utilize NVIDIA L4 GPUs with 3rd generation AMD EPYC (Milan) processors and are available in three variants: G6, Gr6, and G6f. The G6 WorkSpaces feature a standard 1:4 vCPU-to-memory ratio, providing balanced compute and memory resources for general graphics workloads. The Gr6 WorkSpaces offer a 1:8 vCPU-to-memory ratio, delivering double the memory per vCPU for graphics applications with higher memory requirements.
The G6f WorkSpaces provide fractional GPU allocation, making them suitable for workloads that do not require full GPU processing capacity for computationally intensive operations.
Refer to [Amazon EC2 G6 Instances page](https://aws.amazon.com/ec2/instance-types/g6/ "https://aws.amazon.com/ec2/instance-types/g6/") for more information.
The G6 WorkSpace bundles support all use cases that existing bundles support, such as daily tasks, data processing and analysis, audio conferencing and software development. Additionally, they enable the followiing use cases:

- Graphic design
- CAD/CAM (computer-aided design/computer-aided manufacturing)
- Video transcoding
- 3D rendering
- Game streaming
- ML (machine learning) model training and ML inference

This bundle offers a high level of graphics performance, and moderate level of CPU
performance and memory for your WorkSpaces and is well-suited for the following:

- Web browsing
- Word processing
- Email
- Spreadsheets
- Instant messaging
- Audio conferencing
- Software development (Integrated Development Environment (IDE))
- Entry to mid-level data processing
- Data warehousing
- Business intelligence applications
- Graphic design
- CAD/CAM (computer-aided design/computer-aided manufacturing)
  This bundle is not recommended for audio and video conferencing, 3D rendering, photo-realistic design, and
  machine learning model training.

This bundle offers a high level of graphics performance, CPU performance, and
memory for your WorkSpaces and is well-suited for the following:

- Web browsing
- Word processing
- Email
- Spreadsheets
- Instant messaging
- Audio conferencing
- Software development (Integrated Development Environment (IDE))
- Entry to mid-level data processing
- Data warehousing
- Business intelligence applications
- Graphic design
- CAD/CAM (computer-aided design/computer-aided manufacturing)
- Video transcoding
- 3D rendering
- Photo-realistic design
- Game streaming
- ML (machine learning) model training and ML inference
  This bundle is not recommended for audio and video conferencing.
