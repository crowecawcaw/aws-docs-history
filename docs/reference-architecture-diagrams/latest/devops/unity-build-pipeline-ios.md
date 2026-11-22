

# Unity build pipeline: iOS games on AWS Cloud

Publication date: **November 24, 2021 ([Diagram history](diagram-history.md))**

With this architecture, you can build Unity-based games for iOS in the AWS Cloud with Jenkins by using a two-stage pipeline on Amazon Elastic Compute Cloud Spot Instances and Amazon EC2 Mac instances.

## Unity build pipeline: iOS games on AWS Cloud diagram
<a name="unity-build-pipeline-ios-diagram"></a>

![Unity build pipeline for iOS games on AWS Cloud using Jenkins, Amazon EC2 Spot Instances, and Amazon EC2 Mac instances.](https://docs.aws.amazon.com/reference-architecture-diagrams/latest/devops/images/unity-build-pipeline-ios.png)


The following steps describe the architecture:

1. Source code is stored in an [AWS CodeCommit](https://docs.aws.amazon.com/codecommit/latest/userguide/) repository. Jenkins pulls it on a build start.

1. A Unity container image is pulled from Amazon Elastic Container Registry and deployed by the Jenkins Docker agent on a worker node.

1. The first build stage runs on [Amazon EC2](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/) Spot Instances. It generates an Xcode project from Unity source code. These instances are placed into an Auto Scaling group for scalability and redundancy.

1. A Unity Build Server vends floating licenses to workers in the Auto Scaling group.

1. The Unity license binds to the Amazon EC2 instance's Ethernet interface MAC address. An elastic network interface preserves the MAC address if the instance is recreated.

1. The resulting Xcode project transfers to a Jenkins worker on an Amazon EC2 Mac Instance. This worker finalizes and signs the build and exports an .ipa file.

1. Certificates, private keys, and provisioning profiles are stored in AWS Secrets Manager. The Mac dynamically pulls them during a build.

1. An .ipa archive file is exported as a Jenkins artifact and stored in an [Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/) bucket.

## Further reading
<a name="unity-build-pipeline-ios-further-reading"></a>

For additional information, see the following resources:
+ [AWS Architecture Icons](https://aws.amazon.com/architecture/icons)
+ [AWS Architecture Center](https://aws.amazon.com/architecture)
+ [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected)
+ [AWS Game Tech product page](https://aws.amazon.com/gametech/)