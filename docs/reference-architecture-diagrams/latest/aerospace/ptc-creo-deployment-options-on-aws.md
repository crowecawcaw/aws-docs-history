

# PTC Creo on Amazon WorkSpaces Applications: Amazon EC2 File Share for Users
<a name="ptc-creo-deployment-options-on-aws"></a>

Publication date: **March 24, 2022 ([Diagram history](diagram-history.md))**

This architecture gives you a blueprint for providing secure access to [PTC Creo](https://www.ptc.com/en/products/creo) hosted in the AWS Cloud using Amazon S3 for the private user folder, and an EC2-based file share folder for collaboration with other users before committing their computer-aided designs (CADs) into [PTC Windchill product lifecycle management](https://d1.awsstatic.com/architecture-diagrams/ArchitectureDiagrams/ptc-windchill-plm-on-aws.pdf?mfgr_ed3) (PLM).

## PTC Creo on Amazon WorkSpaces Applications: Amazon EC2 File Share for Users diagram
<a name="ptc-creo-deployment-options-on-aws-diagram1"></a>

![Reference architecture diagram showing.blueprint for providing secure access to PTC Creo hosted in the AWS Cloud using Amazon S3 for the private user folder, and an EC2-based file share folder for collaboration with other users before committing their computer-aided designs (CADs) into PTC Windchill product lifecycle management (PLM).](https://docs.aws.amazon.com/reference-architecture-diagrams/latest/aerospace/images/ptc-creo-deployment-options-on-aws.png)


1. Windows Bastion Host running on an [Amazon EC2](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/) instance is used by administrators to log on to instances in the private subnet. 

1. Images created by [Amazon WorkSpaces Applications](https://docs.aws.amazon.com/appstream2/latest/developerguide/) are provisioned in the private subnet that will be used in the generation of the WorkSpaces Applications fleet. 

1. Global Creo License Manger running on Amazon EC2 instances is used by WorkSpaces Applications fleet instances that are being generated. Licenses are consumed when WorkSpaces Applications instances are created and licenses released after WorkSpaces Applications instances are deprecated. 

1. The Amazon WorkSpaces Applications fleet is created in private subnets in two different Availability Zones that users connect to, either on an on-demand or always-on basis. 

1. Users connect to the WorkSpaces Applications fleet instances using a web browser, or Amazon WorkSpaces Applications Windows Client. 

1. A file share based on Amazon EC2 instances backed by [Amazon Elastic Block Store](https://docs.aws.amazon.com/ebs/latest/userguide/) (Amazon EBS) volumes is created for users to use a common server message block (SMB) share for collaboration, before committing the final CADs into the PTC Windchill file vault. 

1. In the process of setting up the Amazon WorkSpaces Applications stack, users can select an [Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/) folder as a private folder for each user to persist application settings, user data, and files. 

## Further reading
<a name="ptc-creo-deployment-options-on-aws-further-reading"></a>

 For additional information, refer to 
+ [AWS Architecture Icons](https://aws.amazon.com/architecture/icons)
+ [AWS Architecture Center](https://aws.amazon.com/architecture)
+  [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected) 