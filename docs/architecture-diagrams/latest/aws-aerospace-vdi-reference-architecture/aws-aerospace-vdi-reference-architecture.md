# Aerospace Virtual Desktop

Infrastructure (VDI) and High Performance Computing (HPC) on AWS

Publication date: **January 26, 2022 ([Diagram history](#diagram-history "#diagram-history"))**

This architectural diagram shows the process for running computer-aided engineering (CAE)
computations and visualizations in the cloud with desktop access.

## Aerospace VDI and HPC on AWS Diagram

![Reference architecture diagram showing the process for running computer-aided engineering (CAE) computations and visualizations in the cloud with desktop access..](images/aws-aerospace-vdi-reference-architecture.png)

1. The user starts virtual desktop (VD) sessions, starts and monitors high performance
   computing (HPC) jobs using a web interface or application programming interface (API),
   accesses VD sessions with NICE DCV client, and shares data with the VD and HPC environment
   using SFTP.
2. The AMI Build environment produces AMIs with specialized software for VDI and HPC
   environment.
3. NICE DCV session to Windows VDI.
4. NICE DCV session to Linux VDI.
5. AWS Directory Service is used for the centralized user management. The cluster head node, Linux and
   Windows VDIs, HPC compute nodes join the Active Directory domain.
6. AWS Transfer for SFTP is used to share data between on-premises and the cluster.
7. Amazon EFSAmazon FSx for NetApp ONTAP is used for storing of cluster applications and for sharing data
   with on-premises. Amazon FSx for NetApp ONTAP stores user data which needs to be easily accessible from
   Windows and Linux VDIs. Amazon FSx for Lustre is used by HPC nodes during computations.
8. Amazon EC2 is used for HPC compute nodes. The cluster’s Head node spawns and stops the
   compute nodes using auto scaling groups.
9. Amazon OpenSearch Service stores HPC job and hosts information.

You can use the [Scale-Out
Computing on AWS](https://aws.amazon.com/solutions/implementations/scale-out-computing-on-aws/ "https://aws.amazon.com/solutions/implementations/scale-out-computing-on-aws/") solution as a foundation for implementation of the
environment.

## Download editable diagram

To customize this reference architecture diagram based on your business needs, [download the ZIP file](samples/aws-aerospace-vdi-reference-architecture.md "samples/aws-aerospace-vdi-reference-architecture.md") which contains an editable PowerPoint.

## Create a free AWS account

[![Sign up for a free AWS account](images/signup.png)](https://portal.aws.amazon.com/gp/aws/developer/registration/index.html "https://portal.aws.amazon.com/gp/aws/developer/registration/index.html")

Sign up for an AWS account. New accounts include 12 months of [AWS Free Tier](https://aws.amazon.com/free/ "https://aws.amazon.com/free/") access, including the use of Amazon EC2, Amazon S3, and
Amazon DynamoDB.

## Further reading

For additional information, refer to

- [AWS Architecture
  Icons](https://aws.amazon.com/architecture/icons "https://aws.amazon.com/architecture/icons")
- [AWS Architecture Center](https://aws.amazon.com/architecture "https://aws.amazon.com/architecture")
- [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected "https://aws.amazon.com/architecture/well-architected")

## Diagram history

To be notified about updates to this reference architecture diagram, subscribe to the RSS feed.

| Change              | Description                                     | Date             |
| ------------------- | ----------------------------------------------- | ---------------- | ----------------------------------------------------------------------------------------------------------- |
| Initial publication | Reference architecture diagram first published. | January 26, 2023 | ###### Note To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you are using. |
