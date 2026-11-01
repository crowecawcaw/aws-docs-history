

# Amazon FSx for NetApp ONTAP NTFS connectivity to Domino Data Lab
<a name="fsxn-ntfs-domino"></a>

Publication date: **October 27, 2026 ([Diagram history](diagram-history.md))**

Domino Data Lab creates volumes that use the UNIX security style on [Amazon FSx for NetApp ONTAP](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/what-is-fsx-ontap.html). This architecture shows how to convert those volumes to the [NTFS security style](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/managing-volumes.html#volume-security-style). Domino runs on [Amazon Elastic Kubernetes Service (Amazon EKS)](https://docs.aws.amazon.com/eks/latest/userguide/what-is-eks.html) and keeps NFS access to the volumes. Users can also access the same data directly over SMB.

## Amazon FSx for NetApp ONTAP NTFS diagram
<a name="fsxn-ntfs-domino-diagram1"></a>

![Architecture diagram showing users who access Domino Data Lab on Amazon EKS through Elastic Load Balancing over HTTPS. Domino connects to FSx for ONTAP over NFS through NetApp Trident. Users also access FSx for ONTAP directly over SMB or NFS, with authentication through AWS Directory Service. External data sources connect through VPC peering, AWS Transit Gateway, an internet gateway, VPN, or AWS Direct Connect. AWS Secrets Manager, Amazon ECR, and Amazon Route 53 support the deployment.](https://docs.aws.amazon.com/reference-architecture-diagrams/latest/storage/images/fsxn-ntfs-domino.png)


The following steps describe the architecture:

1. Users primarily access, generate and modify data stored in FSx for ONTAP / Domino through the Domino application access in their web browser.

1. The [Elastic Load Balancing](https://docs.aws.amazon.com/elasticloadbalancing/latest/userguide/what-is-load-balancing.html) directs user traffic to the Amazon EKS clusters based on availability to Domino nodes.

1. The Domino application connects to FSx for ONTAP through Trident managed volumes with NFS. Domino uses a service account to access the data.

1. Users can also access Domino data stored in FSx for ONTAP directly from their local machine over the SMB protocol. Users can create, edit, and delete files.

1. To authenticate users who connect directly to FSx for ONTAP, the storage virtual machine (SVM) is joined to Microsoft Active Directory, and Active Directory security groups are applied to the volume.

1. You can integrate other external data sources into Domino. These data sources can be in the same VPC, in another VPC, in other clouds, or on premises. To connect them, use [VPC peering](https://docs.aws.amazon.com/vpc/latest/peering/what-is-vpc-peering.html), [AWS Transit Gateway](https://docs.aws.amazon.com/vpc/latest/tgw/what-is-transit-gateway.html), or [AWS Direct Connect](https://docs.aws.amazon.com/directconnect/latest/UserGuide/Welcome.html). You can also use an [internet gateway](https://docs.aws.amazon.com/vpc/latest/userguide/VPC_Internet_Gateway.html) or a [VPN connection](https://docs.aws.amazon.com/vpn/latest/s2svpn/VPC_VPN.html).

1. Domino Data Lab uses [AWS Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/intro.html), [Amazon Elastic Container Registry (Amazon ECR)](https://docs.aws.amazon.com/AmazonECR/latest/userguide/what-is-ecr.html), and [Amazon Route 53](https://docs.aws.amazon.com/Route53/latest/DeveloperGuide/Welcome.html). These services help it manage, secure, and deploy its resources.

## Further reading
<a name="fsxn-ntfs-domino-further-reading"></a>

For additional information, refer to the following resources:
+ [Amazon FSx for NetApp ONTAP User Guide](https://docs.aws.amazon.com/fsx/latest/ONTAPGuide/what-is-fsx-ontap.html)
+ [Amazon EKS User Guide](https://docs.aws.amazon.com/eks/latest/userguide/what-is-eks.html)
+ [AWS Architecture Icons](https://aws.amazon.com/architecture/icons)
+ [AWS Architecture Center](https://aws.amazon.com/architecture)
+ [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected)