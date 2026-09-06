

# AWS Overview
<a name="overview-aws"></a>

 AWS offers a broad set of global, cloud-based services, including compute, storage, networking, Internet of Things (IoT), and many others. These services help organizations move faster, lower IT costs, and support scalability. AWS is trusted by the largest enterprises and popular start-ups to power a wide variety of workloads, such as web and mobile applications, game development, data processing and warehousing, storage, and archiving.

## AWS Services
<a name="overview-aws-services"></a>

 AWS provides over 200 cloud services that you can use in combinations tailored to your business or organizational needs. For information about all AWS services, see the [Amazon Web Services Cloud Platform](https://docs.aws.amazon.com/aws-technical-content/latest/aws-overview/amazon-web-services-cloud-platform.html#services) documentation.

This section introduces the AWS services that are most relevant for the deployment and operation of SAP solutions. The following list provides a high-level description of each service and its use for SAP systems. To view features, pricing, and documentation for an individual service, follow the *details*link after the description.



- **  **Compute**  **
  - **Service:** Amazon Elastic Compute Cloud (Amazon EC2)
  - **Description:** Secure, resizable compute capacity in the cloud. ([details](https://aws.amazon.com/ec2))
  - **SAP uses:** Virtual and bare metal servers for the installation and operation of SAP systems.

- **  **Storage**  **
  - **Service:** Amazon Elastic Block Store (Amazon EBS) / **Description:** Persistent block storage volumes for use with EC2 instances. ([details](https://aws.amazon.com/ebs)) / **SAP uses:** File systems for SAP software (e.g., `/usr/sap`), SAP database log and data files, and SAP local backups.
  - **Service:** Amazon Simple Storage Service (Amazon S3) / **Description:** Object storage service that offers an extremely durable, highly available, and infinitely scalable data storage infrastructure. ([details](https://aws.amazon.com/s3)) / **SAP uses:** Highly durable storage for file backups, database backups, archiving data, data lakes, and more.
  - **Service:** Amazon Elastic File System (Amazon EFS) / **Description:** Simple, scalable, elastic file system for Linux-based workloads for use with AWS Cloud services and on-premises resources. ([details](https://aws.amazon.com/efs)) / **SAP uses:** Shared file system for SAP application servers (e.g., `/sapmnt`).
  - **Service:** Amazon FSx for Windows File Server / **Description:** Fully managed, highly durable, and available native Microsoft Windows file system. ([details](https://aws.amazon.com/fsx/windows)) / **SAP uses:** Shared file system for SAP application servers (e.g., `/sapmnt`).
  - **Service:** Amazon FSx for NetApp ONTAP / **Description:** Fully managed, highly reliable, scalable, high-performing file storage built on NetApp ONTAP file system([details](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/what-is-fsx-ontap.html)) / **SAP uses:** Shared file system for SAP application servers (e.g., `/sapmnt`).

- **  **Networking**  **
  - **Service:** Amazon Virtual Compute Cloud (Amazon VPC) / **Description:** Logically isolated section of the AWS Cloud where you can launch AWS resources in a virtual network that you define. ([details](https://docs.aws.amazon.com/vpc/)) / **SAP uses:** Network for SAP resources. You can control the level of isolation of your EC2 instance from other networks, instances, and on-premises network resources, such as those in production and non-production environments.
  - **Service:** Amazon Site-to-Site VPN / **Description:** Enables you to securely connect your on-premises network or branch office site to your VPC. ([details](https://docs.aws.amazon.com/vpn/latest/s2svpn/VPC_VPN.html)) / **SAP uses:** Network connectivity between on-premises systems/users and SAP systems on AWS.
  - **Service:**  AWS Directs Connect / **Description:** Lets you establish private network connectivity between AWS and your data center, office, or co-location environment. ([details](https://aws.amazon.com/directconnect)) / **SAP uses:** Private network connectivity between on-premises systems/users and the SAP system or environment on AWS.
  - **Service:** Amazon Route 53 / **Description:** Highly available and scalable cloud Domain Name System (DNS) web service. ([details](https://aws.amazon.com/route53)) / **SAP uses:** Name and address resolution for SAP systems running on AWS.
  - **Service:** Amazon Time Sync / **Description:** Highly accurate and reliable time reference that is natively accessible from EC2 instances. ([Linux](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/configure-ec2-ntp.html) \| [Windows](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/set-time.html)) / **SAP uses:** Time synchronization for your SAP systems on EC2 instances.

- **  **Management and operation tools**  **
  - **Service:**  AWS Management Console / **Description:** Simple web interface to provision and manage AWS resources. ([details](https://aws.amazon.com/console)) / **SAP uses:** Provisioning and management of AWS resources for your SAP environment on AWS.
  - **Service:**  AWS Command Line Interface (AWS CLI) / **Description:** Command-line tool set to provision and manage AWS resources. ([details](https://docs.aws.amazon.com/cli)) / **SAP uses:** Creation of scripts to automate the provisioning and management of AWS resources for your SAP environment on AWS.
  - **Service:**  AWS CloudFormation / **Description:** An easy way to create a collection of related AWS resources and provision them in an orderly and predictable fashion. ([details](https://aws.amazon.com/cloudformation)) / **SAP uses:** Automated provisioning of AWS resources for new SAP landscapes, disaster recovery environments, and other use cases.
  - **Service:** Amazon CloudWatch / **Description:** Monitoring for AWS Cloud resources and the applications you run on AWS: collect and track metrics, collect and monitor log files, and set alarms. ([details](https://aws.amazon.com/cloudwatch)) / **SAP uses:** Monitoring SAP systems running on AWS using [Amazon CloudWatch Application Insights](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/cloudwatch-application-insights.html).
  - **Service:**  AWS CloudTrail / **Description:** Records activity made on your account and delivers log files to your S3 bucket. ([details](https://aws.amazon.com/cloudtrail)) / **SAP uses:** Audit capabilities within your AWS account, such as use of the Amazon EC2 API.
  - **Service:**  AWS Launch Wizard for SAP / **Description:**  AWS Launch Wizard for SAP is a service that guides you through the sizing, configuration, and deployment of SAP applications on AWS. ([details](https://docs.aws.amazon.com/launchwizard/latest/userguide/launch-wizard-sap.html)) / **SAP uses:** Setup and configuration of resources required for your SAP deployment.
  - **Service:**  AWS Backint Agent for SAP HANA / **Description:** SAP certified solution to backup and restore SAP HANA database to and from Amazon S3. ([details](https://docs.aws.amazon.com/sap/latest/sap-hana/aws-backint-agent-what-is.html)) / **SAP uses:** Backup solution to store SAP HANA database backups to Amazon S3.

- **  **Security, identity, and compliance**  **
  - **Service:**  AWS Identity and Access Management (AWS IAM)
  - **Description:** Manages access to AWS services and resources securely. Using AWS IAM, you can create and manage AWS users and groups, and use permissions to allow and deny their access to AWS resources. ([details](https://aws.amazon.com/iam))
  - **SAP uses:** Fine-grained access control using a least privileged security model to access specific AWS services and actions; e.g., to allow SAP BASIS resources to launch, to stop and start EC2 instances without terminating them.



## AWS Global Infrastructure
<a name="overview-global-infrastructure"></a>

The AWS Cloud infrastructure is built around Regions and Availability Zones. An AWS Region is a physical location that provides multiple, physically separated and isolated Availability Zones. Each Availability Zone consists of one or more data centers that are connected with low-latency, high-throughput, and highly redundant networking. These Availability Zones offer an easier and more effective way to design and operate your applications and databases, making them more highly available, fault tolerant, and scalable than traditional single or multiple data center infrastructures.

For a list of the available AWS Regions and to learn more about the AWS global infrastructure, see [Global Infrastructure](https://aws.amazon.com/about-aws/globalinfrastructure) on the AWS website.

## AWS Security and Compliance
<a name="overview-security-compliance"></a>

### Security
<a name="overview-security"></a>

At AWS, security is our top priority. As an AWS customer, you will benefit from a data center and network architecture built to meet the requirements of the most security-sensitive organizations. Security in the cloud is much like security in your on-premises data centers—​only without the costs of maintaining facilities and hardware. In the cloud, you don’t have to manage physical servers or storage devices. Instead, you use software-based security tools to monitor and protect the flow of information into and out of your cloud resources.

As an AWS customer you inherit all the best practices of AWS policies, architecture, and operational processes built to satisfy the requirements of our most security-sensitive customers, and get the flexibility and agility you need in security controls.

The AWS Cloud enables a shared responsibility model. While AWS manages security **of** the cloud, you are responsible for security **in** the cloud. This means that you retain control of the security you choose to implement to protect your own data, platform, applications, systems, and networks no differently than you would in an on-site data center.

To learn more about AWS security, see [AWS Cloud Security](https://aws.amazon.com/security) on the AWS website.

### Compliance
<a name="overview-compliance"></a>

 AWS provides robust controls to help maintain security and data protection in the cloud. As systems are built on top of AWS Cloud infrastructure, compliance responsibilities will be shared. By tying together governance-focused, audit-friendly service features with applicable compliance or audit standards, AWS compliance enablers build on traditional programs and help you operate in an AWS security control environment.

The IT infrastructure that AWS provides to its customers is designed and managed in alignment with best security practices and a variety of IT security standards. The following is a partial list of assurance programs with which AWS complies:
+ SOC 1/ISAE 3402, SOC 2, SOC 3
+ FISMA, FIPS, DIACAP, and FedRAMP
+ PCI DSS Level 1
+ ISO 9001, ISO 27001, ISO 27017, ISO 27701, ISO 27018

For more information, see [AWS Compliance Programs](https://aws.amazon.com/compliance/programs/).

## AWS Provisioning and Management
<a name="overview-resource-mgmt"></a>

The provisioning and management of AWS services and resources use a self-service model managed by the customer or a partner. For an overview of the tools available for provisioning and management, see the management tools in the [AWS Services](#overview-aws-services) section.

Figure 1 shows the services managed by AWS and the services managed by the customer or partner for SAP.

 **Figure 1: Managed services for SAP on AWS ** 

![Managed services for SAP](http://docs.aws.amazon.com/sap/latest/general/images/sap-overview-managed-services.png)
