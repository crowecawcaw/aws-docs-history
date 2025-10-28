# Game Production in the Cloud - Workstations

Publication date: **December 1, 2021 ([Diagram history](#diagram-history "#diagram-history"))**

This architecture, which is agnostic of game engine and software, walks through the use of streaming remote workstations with the NICE DCV protocol. It covers the high level considerations for use of cloud development workstations for games.

## Game Production in the Cloud - Workstations Diagram

![Reference architecture diagram showing game production in the cloud using streaming workstations](images/game-production-in-the-cloud-workstations.png)

1. NICE DCV is a streaming protocol that supports 4K, 60 FPS streaming. Developers using
   a browser connect using TCP connections, whereas desktop clients can use QUIC UDP over
   port 8443 for increased performance.
2. Developers use **AWS Client VPN** for a secure connection to
   network interfaces in the workstations subnets with source network address translation
   (SNAT).
3. **Amazon Route 53** provides private DNS for the resources in
   the VPC, as well as inbound and outbound DNS forwarding.
4. **AWS Directory Service** provides managed directory service for
   Microsoft Active Directory to enable local game project storage mapped to individual
   users.
5. Workstations are created using an **Amazon Machine Image** (AMI) built with **Amazon EC2**
   **Image Builder**. Images include NICE DCV server, developer
   software, registry changes, and drivers (such as NVIDIA gaming drivers or peripheral
   drivers). The **AWS Marketplace** includes common AMIs used for
   workstations.
6. Fleets of workstations use graphics **Amazon Elastic Compute Cloud** (Amazon EC2)
   instance types that provide GPUs and are scaled using **Amazon EC2 Auto Scaling** groups.
7. A Session Manager Broker enables management of NICE DCV sessions.
8. Local file storage of projects are hosted in **Amazon FSx for Windows File Server**. Developers commit to a separate continuous integration and
   continuous delivery (CI/CD) pipeline by pushing from local storage to source
   control.

## Download editable diagram

To customize this reference architecture diagram based on your business needs, [download the ZIP file](samples/game-production-in-the-cloud-workstations.md "samples/game-production-in-the-cloud-workstations.md") which contains an editable PowerPoint.

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
| Initial publication | Reference architecture diagram first published. | December 1, 2021 | ###### Note To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you are using. |
