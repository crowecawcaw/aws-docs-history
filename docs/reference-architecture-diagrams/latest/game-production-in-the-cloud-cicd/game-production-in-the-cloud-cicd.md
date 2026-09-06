

# Game Production in the Cloud: CI/CD
<a name="game-production-in-the-cloud-cicd"></a>

Publication date: **November 10, 2021 ([Diagram history](#cicd-history))**

This architecture provides an engine-agnostic, high-level approach for offloading game builds from remote or on-premises game development environments to the AWS Cloud. This architecture helps developers migrate or build new build farms on AWS.

## Game Production in the Cloud: CI/CD diagram
<a name="cicd-diagram"></a>

![Reference architecture diagram showing how to offload game builds to the AWS Cloud by using Perforce, Jenkins, Amazon EC2 Spot Instances, and Amazon EC2 Mac instances.](http://docs.aws.amazon.com/reference-architecture-diagrams/latest/game-production-in-the-cloud-cicd/images/game-production-in-the-cloud-cicd.png)


The following steps describe the architecture:

1. AWS Direct Connect provides a low-latency, private, dedicated connection to AWS for in-office developers. Remote developers use AWS Client VPN.

1. AWS Transit Gateway simplifies network management for connectivity between VPCs and from on-premises networks.

1. Perforce manages source and version control (CI) backed by [Amazon Elastic Block Store](https://docs.aws.amazon.com/ebs/latest/userguide/) storage for quickly accessed, persistent data. Perforce Helix Core (P4D) is available on AWS Marketplace.

1. Commits start a build (CD) in Jenkins when developers push changes to Perforce tied to a branch. The Jenkins controller calls engine headless CLI commands to run and parallelize the build process across ephemeral, Docker nodes such as [Amazon EC2](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/) Spot Instances (one hour or less build time), or Amazon EC2 On-Demand instances.

1. The Xcode portion of iOS builds is offloaded to [Amazon EC2 Mac instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-mac-instances.html) to sign, build, and export the .ipa file. This approach splits the process and reduces build times. [AWS Secrets Manager](https://docs.aws.amazon.com/secretsmanager/latest/userguide/) holds provisioning profiles, private keys, and certificates.

1. Build artifacts delivered to [Amazon Simple Storage Service](https://docs.aws.amazon.com/AmazonS3/latest/userguide/) trigger third-party notification flows of success or failures. [AWS Device Farm](https://docs.aws.amazon.com/devicefarm/latest/developerguide/) provides automated testing.

## Further reading
<a name="cicd-further-reading"></a>

For additional information, see the following resources:
+  [AWS Architecture Icons](https://aws.amazon.com/architecture/icons) 
+  [AWS Architecture Center](https://aws.amazon.com/architecture/) 
+  [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected) 

## Diagram history
<a name="cicd-history"></a>

To be notified about updates to this reference architecture diagram, subscribe to the RSS feed.

| Change | Description | Date | 
| --- |--- |--- |
| [Initial publication](#cicd-history) | Reference architecture diagram first published. | November 10, 2021 | 

**Note**  
To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you are using.