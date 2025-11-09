# PTC Creo on Amazon WorkSpaces Applications – EC2-based File Share for Users

Publication date: **March 24, 2022 ([Diagram history](#diagram-history "#diagram-history"))**

This architecture gives you a blueprint for providing secure access to [PTC Creo](https://www.ptc.com/en/products/creo "https://www.ptc.com/en/products/creo") hosted in the AWS Cloud using Amazon S3 for the private user folder, and an EC2-based file share folder for collaboration with other users before committing their computer-aided designs (CADs) into [PTC Windchill product lifecycle management](https://d1.awsstatic.com/architecture-diagrams/ArchitectureDiagrams/ptc-windchill-plm-on-aws.pdf?mfgr_ed3 "https://d1.awsstatic.com/architecture-diagrams/ArchitectureDiagrams/ptc-windchill-plm-on-aws.pdf?mfgr_ed3") (PLM).

## PTC Creo on Amazon WorkSpaces Applications – EC2-based File Share for Users

![Reference architecture diagram showing.blueprint for providing secure access to PTC Creo hosted in the AWS Cloud using Amazon S3 for the private user folder, and an EC2-based file share folder for collaboration with other users before committing their computer-aided designs (CADs) into PTC Windchill product lifecycle management (PLM).](images/ptc-creo-deployment-options-on-aws.png)

1. Windows Bastion Host running on an **Amazon EC2** instance is
   used by administrators to log on to instances in the private subnet.
2. Images created by **Amazon AppStream** are provisioned in the
   private subnet that will be used in the generation of the **Amazon AppStream** fleet.
3. Global Creo License Manger running on **Amazon EC2** instances
   is used by **Amazon AppStream** fleet instances that are being
   generated. Licenses are consumed when **Amazon AppStream** instances are
   created and licenses released after **Amazon AppStream** instances are
   deprecated.
4. The **Amazon WorkSpaces Applications** fleet is created in private subnets in
   two different Availability Zones that users connect to, either on an on-demand or
   always-on basis.
5. Users connect to the **Amazon AppStream** fleet instances using a
   web browser, or **Amazon WorkSpaces Applications** Windows Client.
6. A file share based on **Amazon EC2** instances backed by
   **Amazon Elastic Block Store** (Amazon EBS) volumes is created for users to use a
   common server message block (SMB) share for collaboration, before committing the final
   CADs into the PTC Windchill file vault.
7. In the process of setting up the **Amazon WorkSpaces Applications** stack,
   users can select an **Amazon S3** folder as a private folder for
   each user to persist application settings, user data, and files.

## Download editable diagram

To customize this reference architecture diagram based on your business needs, [download the ZIP file](samples/ptc-creo-deployment-options-on-aws.md "samples/ptc-creo-deployment-options-on-aws.md") which contains an editable PowerPoint.

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

| Change              | Description                                     | Date           |
| ------------------- | ----------------------------------------------- | -------------- |
| Initial publication | Reference architecture diagram first published. | March 24, 2022 |

###### Note

To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you are using.
