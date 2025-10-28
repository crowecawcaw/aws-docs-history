#

Definitions

Following is a list of definitions related to the AWS
Well-Architected Framework and EUC workloads.

## AWS Definitions

- EUC
  - **Amazon AppStream 2.0:** Secure, reliable, and
    scalable application streaming and low-cost virtual
    desktop service
  - **[Amazon WorkSpaces](https://aws.amazon.com/workspaces/ "https://aws.amazon.com/workspaces/") Family:** Comprehensive, fully
    persistent, Virtual Desktop Infrastructure for most worker
    types
  - **[Amazon WorkSpaces Core](https://aws.amazon.com/workspaces/core/ "https://aws.amazon.com/workspaces/core/"):** Virtual desktop
    infrastructure APIs for third-party VDI software
  - **[Amazon WorkSpaces Secure Browser](https://aws.amazon.com/workspaces/web/ "https://aws.amazon.com/workspaces/web/"):** Secure,
    low-cost browser service for access to internal websites
    and Software as a Service apps
  - **[Amazon
    WorkDocs](https://aws.amazon.com/workdocs/ "https://aws.amazon.com/workdocs/"):** Secure document sharing and
    content collaboration—connecting teams everywhere
  - **[Amazon
    DCV](https://aws.amazon.com/hpc/dcv/ "https://aws.amazon.com/hpc/dcv/"):** Amazon DCV is a high-performance
    remote display protocol that provides secure remote
    desktop delivery and application streaming, avoiding the
    need for expensive dedicated workstations.

- Hardware
  - **[Amazon WorkSpaces Thin Client](https://aws.amazon.com/workspaces/thin-client/ "https://aws.amazon.com/workspaces/thin-client/"):** Reduce costs,
    simplify logistics, and accelerate deployment using
    virtual desktops

- Storage
  - **[Amazon FSx](https://aws.amazon.com/fsx/ "https://aws.amazon.com/fsx/"):** Launch, run, and scale feature-rich
    and highly performant file systems with just a few clicks
  - **[Amazon S3](https://aws.amazon.com/s3/ "https://aws.amazon.com/s3/"):** Object storage built to retrieve any
    amount of data from anywhere
  - **[Amazon EFS](https://aws.amazon.com/pm/efs/ "https://aws.amazon.com/pm/efs/"):** Share file data without
    provisioning storage

- Compute
  - **[Amazon EC2](https://aws.amazon.com/ec2/ "https://aws.amazon.com/ec2/"):** Secure and resizable compute
    capacity for virtually any workload

- Cost
  - **[Amazon WorkSpaces Family Pricing](https://aws.amazon.com/workspaces/pricing/ "https://aws.amazon.com/workspaces/pricing/"):** Pricing
    across the Amazon WorkSpaces Family services is designed
    to be flexible and cost-effective, allowing you to pay for
    the resources you need without over provisioning.
  - **[Bring
    Your Own Windows Desktop Licenses
    (BYOL)](../../../workspaces/latest/adminguide/byol-windows-images.md "../../../workspaces/latest/adminguide/byol-windows-images.md"):** If your licensing agreement with
    Microsoft allows it, you can bring and deploy your Windows
    10 or 11 desktop on your WorkSpaces.
  - **[Cost
    Optimizer for Amazon AppStream 2.0](https://github.com/aws-samples/cost-optimizer-for-amazon-appstream2 "https://github.com/aws-samples/cost-optimizer-for-amazon-appstream2"):**
    Monitors your AppStream 2.0 app block builders and image
  - **[Cost
    Optimizer for Amazon WorkSpaces](https://aws.amazon.com/solutions/implementations/cost-optimizer-for-amazon-workspaces/ "https://aws.amazon.com/solutions/implementations/cost-optimizer-for-amazon-workspaces/"):** Monitor
    Amazon WorkSpaces usage and optimize costs builders and
    notifies you and/or stops them when they are active for
    longer than specified thresholds.

- Managed directories for WorkSpaces
  - **[AD
    Connector](../../../directoryservice/latest/admin-guide/directory_ad_connector.md "../../../directoryservice/latest/admin-guide/directory_ad_connector.md"):** A directory gateway with
    which you can redirect directory requests to your
    on-premises Microsoft Active Directory without caching any
    information in the cloud.
  - **[AWS Managed Microsoft AD](../../../directoryservice/latest/admin-guide/directory_microsoft_ad.md "../../../directoryservice/latest/admin-guide/directory_microsoft_ad.md"):** AWS Directory Service lets you run Microsoft Active Directory (AD) as a
    managed service.
  - **[Simple
    AD](../../../directoryservice/latest/admin-guide/directory_simple_ad.md "../../../directoryservice/latest/admin-guide/directory_simple_ad.md"):** Provides a subset of the features
    offered by AWS Managed Microsoft AD, including the ability
    to manage user accounts and group memberships, create and
    apply group policies, securely connect to Amazon EC2
    instances, and provide Kerberos-based single sign-on
    (SSO).
  - **[Cross
    Trust](../../../workspaces/latest/adminguide/launch-workspace-trusted-domain.md "../../../workspaces/latest/adminguide/launch-workspace-trusted-domain.md"):** You can establish a trust
    relationship between your AWS Managed Microsoft AD
    directory and your on-premises domain.

- Protocols for Amazon WorkSpaces
  - **[Amazon
    WSP (WorkSpaces Streaming Protocol)](https://aws.amazon.com/workspaces/wsp/ "https://aws.amazon.com/workspaces/wsp/"):**
    Built using
    [Amazon
    DCV](https://aws.amazon.com/hpc/dcv/ "https://aws.amazon.com/hpc/dcv/") technology, enabling high-performance remote
    access to Amazon WorkSpaces instances for a wide range of
    workloads and use cases.
  - **[PCoIP
    (PC over IP)](../../../workspaces/latest/adminguide/amazon-workspaces-protocols.md#w11aac13b7b7 "../../../workspaces/latest/adminguide/amazon-workspaces-protocols.md#w11aac13b7b7"):** Amazon WorkSpaces supports
    PCoIP when needed based on the type of devices your users
    will be accessing their WorkSpaces from, which operating
    system is on your WorkSpaces, what network conditions your
    users will be facing, and whether your users require
    bidirectional video support.

- Networking
  - **[Internet
    gateway](../../../vpc/latest/userguide/VPC_Internet_Gateway.md "../../../vpc/latest/userguide/VPC_Internet_Gateway.md"):** Horizontally scaled, redundant,
    and highly available VPC component that allows
    communication between your VPC and the internet. It
    supports IPv4 and IPv6 traffic.
  - **[NAT gateway](../../../vpc/latest/userguide/vpc-nat.md "../../../vpc/latest/userguide/vpc-nat.md"):**
    Allow resources in private subnets to connect to the
    internet, other VPCs, or on-premises networks. These
    instances can communicate with services outside the VPC,
    but they cannot receive unsolicited connection requests.
  - **[Public
    subnets](../../../vpc/latest/userguide/configure-subnets.md#subnet-types "../../../vpc/latest/userguide/configure-subnets.md#subnet-types"):** Subnet which has a direct route
    to an internet gateway. Resources in a public subnet can
    access the public internet.
  - **[Private
    subnets](../../../vpc/latest/userguide/configure-subnets.md#subnet-types "../../../vpc/latest/userguide/configure-subnets.md#subnet-types"):** Subnet which does not have a
    direct route to an internet gateway. Resources in a
    private subnet require a
    [NAT
    device](../../../vpc/latest/userguide/vpc-nat.md "../../../vpc/latest/userguide/vpc-nat.md") to access the public internet.
  - **[Amazon Virtual Private Cloud (VPC)](../../../vpc.md "../../../vpc.md"):** Launch AWS
    resources in a logically isolated virtual network that
    you've defined. This virtual network closely resembles a
    traditional network that you'd operate in your own data
    center, with the benefits of using the scalable
    infrastructure of AWS.
  - **[AWS Regions](../../../AWSEC2/latest/UserGuide/using-regions-availability-zones.md#concepts-regions "../../../AWSEC2/latest/UserGuide/using-regions-availability-zones.md#concepts-regions"):** Each Region is designed to be
    isolated from the other Regions. This achieves the
    greatest possible fault tolerance and stability.
  - [**Availability
    Zone:**](../../../AWSEC2/latest/UserGuide/using-regions-availability-zones.md#concepts-availability-zones "../../../AWSEC2/latest/UserGuide/using-regions-availability-zones.md#concepts-availability-zones") Each Region has multiple, isolated
    locations known as Availability Zones.
  - **[Amazon Route 53](https://aws.amazon.com/route53/ "https://aws.amazon.com/route53/"):** A reliable and cost-effective
    way to route end users to your Internet applications. As
    such, Amazon Route 53 is a highly available and scalable
    Domain Name System (DNS) web service that connects user
    requests to internet applications running on AWS or
    on-premises.
  - **[DHCP
    Option Sets in Amazon VPC](../../../vpc/latest/userguide/VPC_DHCP_Options.md "../../../vpc/latest/userguide/VPC_DHCP_Options.md"):** Network
    devices in your VPC use Dynamic Host Configuration
    Protocol (DHCP). You can use DHCP option sets to
    control: The DNS servers, domain names, or Network Time
    Protocol (NTP) servers used by the devices in your VPC and
    whether DNS resolution is enabled in your VPC.

- Security
  - **[AWS Identity and Access Management](https://aws.amazon.com/iam/ "https://aws.amazon.com/iam/") (IAM):**
    Helps an administrator securely control access to AWS
    resources.
  - **[Security
    groups](../../../vpc/latest/userguide/vpc-security-groups.md "../../../vpc/latest/userguide/vpc-security-groups.md"):** Controls the traffic that is
    allowed to reach and leave the resources that it is
    associated with.

- Monitoring
  - **[Amazon CloudWatch](../../../cloudwatch.md "../../../cloudwatch.md"):** Provides a reliable,
    scalable, and flexible monitoring solution that you can
    start using within minutes. You no longer need to set up,
    manage, and scale your own monitoring systems and
    infrastructure.
  - **[Amazon EventBridge](https://aws.amazon.com/pm/eventbridge/ "https://aws.amazon.com/pm/eventbridge/"):** Serverless event bus to
    build event-driven applications at scale.
  - **[VPC
    Flow Logs](../../../vpc/latest/userguide/flow-logs.md "../../../vpc/latest/userguide/flow-logs.md"):** Enables you to capture
    information about the IP traffic going to and from network
    interfaces in your VPC.

- Management
  - **[AWS Management Console](https://aws.amazon.com/console/ "https://aws.amazon.com/console/"):** Everything you need
    to access and manage the AWS Cloud in one web interface
  - **[AWS Command Line Interface (CLI)](https://aws.amazon.com/cli/ "https://aws.amazon.com/cli/"):** A unified
    tool to manage your AWS services. You can control multiple
    AWS services from the command line and automate them
    through scripts.
  - **[Amazon WorkSpaces API](../../../workspaces/latest/api/welcome.md "../../../workspaces/latest/api/welcome.md"):** Provides detailed
    information about the actions, data types, parameters, and
    errors of the WorkSpaces service.
  - **[Tag
    Editor](../../../tag-editor/latest/userguide/tagging.md "../../../tag-editor/latest/userguide/tagging.md"):** Tags are key and value pairs
    that act as metadata for organizing your AWS resources.
  - **[AWS Organizations](../../../organizations/latest/userguide/orgs_introduction.md "../../../organizations/latest/userguide/orgs_introduction.md"):** An account management
    service that enables you to consolidate multiple AWS accounts into an organization that you create and
    centrally manage. AWS Organizations includes account
    management and consolidated billing capabilities that
    enable you to better meet the budgetary, security, and
    compliance needs of your business.
  - **[End
    User Compute (EUC) Toolkit](https://aws.amazon.com/blogs/desktop-and-application-streaming/euc-toolkit/ "https://aws.amazon.com/blogs/desktop-and-application-streaming/euc-toolkit/"):** Offers a
    range of features to help manage EUC workloads at scale.
  - **[Service
    control policies (SCPs)](../../../organizations/latest/userguide/orgs_manage_policies_scps.md "../../../organizations/latest/userguide/orgs_manage_policies_scps.md"):** A type of
    organization policy that you can use to manage permissions
    in your organization. SCPs offer central control over the
    maximum available permissions for the accounts in your
    organization. SCPs help you to verify that your accounts
    stay within your organization's access control guidelines.

- WorkSpaces
  - **[Running
    mode](../../../workspaces/latest/adminguide/running-mode.md "../../../workspaces/latest/adminguide/running-mode.md"):**
    - **AlwaysOn:** Use when
      paying a fixed monthly fee for unlimited usage of your
      WorkSpaces. This mode is best for users who use their
      WorkSpace full time as their primary desktop.
    - **AutoStop:** Use when
      paying for your WorkSpaces by the hour. With this
      mode, your WorkSpaces stop after a specified period of
      disconnection, and the state of apps and data is
      saved.

  - **[WorkSpace
    bundles and images](../../../workspaces/latest/adminguide/amazon-workspaces-bundles.md "../../../workspaces/latest/adminguide/amazon-workspaces-bundles.md"):**
    - **WorkSpace bundle:** A
      WorkSpace bundle is a combination of an operating
      system, and storage, compute, and software resources.
      When you launch a WorkSpace, you select the bundle
      that meets your needs. The default bundles available
      for WorkSpaces are called public bundles.
    - **Custom image:** If
      you have launched a Windows or Linux WorkSpace and
      have customized it, you can create a custom image from
      that WorkSpace. A custom image contains only the OS,
      software, and settings for the WorkSpace.
    - **Custom bundle:**
      After you create a custom image, you can build a
      custom bundle that combines the custom WorkSpace image
      and the underlying compute and storage configuration
      that you select. You can then specify this custom
      bundle when you launch new WorkSpaces to make sure
      that the new WorkSpaces have the same consistent
      configuration (hardware and software).

- AppStream 2.0
  - **[Fleet
    types](../../../appstream2/latest/developerguide/fleet-type.md "../../../appstream2/latest/developerguide/fleet-type.md"):**
    - **OnDemand:** Streaming
      instances run only when users are streaming
      applications and desktops.
    - **Always-On:**
      Streaming instances run constantly, even when no users
      are streaming applications and desktops.
    - **Elastic:** The pool
      of streaming instances is managed by AppStream 2.0.
      When your users select their application or desktop to
      launch, they will start streaming after the app block
      has been downloaded and mounted to a streaming
      instance.

  - **[Images](../../../appstream2/latest/developerguide/managing-images.md "../../../appstream2/latest/developerguide/managing-images.md"):** You
    can create Amazon AppStream 2.0 images that contain
    applications you can stream to your users and default
    system and application settings to enable your users to
    get started with those applications quickly.
  - **[Image
    Builders](../../../appstream2/latest/developerguide/managing-image-builders.md "../../../appstream2/latest/developerguide/managing-image-builders.md"):** Amazon AppStream 2.0 uses EC2
    instances to stream applications. You launch instances
    from base images, called image builders, which AppStream
    2.0 provides. To create your own custom image, you connect
    to an image builder instance, install and configure your
    applications for streaming, and then create your image by
    creating a snapshot of the image builder instance.

## Partner software

- **WorkSpot:** A software
  partner that provides cloud-native virtual desktop
  infrastructure (VDI) turnkey solutions.
- **LeoStream:** A software
  partner that provides remote desktop access solutions
  supporting hosted desktop deployments.
- **VMWare:** A virtualization
  software provider.
- **ControlUp:** Provides support
  to IT teams when monitoring and troubleshooting virtual
  desktop systems. Offers real-time monitoring, troubleshooting,
  automation, and data analytics.
- **Nuvens:** A member of AWS'
  Partner Network (APN) that supports AWS' virtual desktop
  services, namely Amazon WorkSpaces Manager and AppStream 2.0.
  Our services support AWS' customers to provision, secure, and
  extract intelligence from end-point devices, end-user apps,
  and data on AWS.
- **LiquidWare:** Provides a
  bundle of solutions including ProfileUnity, FlexApp and
  Stratusphere UX that can be used to begin as on-premises VDI
  desktops and can provide a migration path to cloud-hosted or
  desktops as a service (DaaS), with a secure, high-quality
  work-from-anywhere desktop experience.
- **Lakeside Software:** Offers a
  suite of virtual solutions such as ProActiveIT, DEX, HelpDesk,
  Digital Workplace, and Systrack.

## Industry definitions

- **[Security
  Assertion Markup Language (SAML) 2.0](https://en.wikipedia.org/wiki/Security_Assertion_Markup_Language "https://en.wikipedia.org/wiki/Security_Assertion_Markup_Language"):** A
  standard for exchanging authentication and authorization
  identities between security domains.
- **Pooled:** Creates a set (or
  pool) of virtual desktops. Users are connected to one of the
  machines and it is users' machine for the duration they are
  connected to it. Once the user disconnects, the machine
  becomes available to the pool again and a different user will
  be allocated to it.
- **Non-pooled
  (dedicated):** Provides each user with a persistent
  dedicated virtual machine. This approach offers individual
  isolation and customization options.
- **[Federal
  Risk and Authorization Management Program
  (FedRAMP)](https://aws.amazon.com/compliance/fedramp/ "https://aws.amazon.com/compliance/fedramp/"):** A US government-wide program that
  delivers a standard approach to the security assessment,
  authorization, and continuous monitoring for cloud products
  and services.
