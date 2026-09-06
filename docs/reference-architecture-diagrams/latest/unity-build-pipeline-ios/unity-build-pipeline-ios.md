

# Unity Build Pipeline: iOS Games on AWS Cloud
<a name="unity-build-pipeline-ios"></a>

Publication date: **November 24, 2021 ([Diagram history](#diagram-history))**

This architecture shows how to build Unity-based games for iOS in the AWS Cloud with Jenkins by using a two-stage pipeline on Amazon EC2 Spot Instances and Amazon EC2 Mac Instances.

## Unity Build Pipeline: iOS Games on AWS Cloud
<a name="diagram1"></a>

![Architecture diagram showing a Unity build pipeline for iOS games on AWS Cloud by using Jenkins, Amazon Elastic Compute Cloud Spot Instances, and Amazon Elastic Compute Cloud Mac Instances.](http://docs.aws.amazon.com/reference-architecture-diagrams/latest/unity-build-pipeline-ios/images/unity-build-pipeline-ios.png)


1. Source code is stored in an [AWS CodeCommit](https://docs.aws.amazon.com/codecommit/latest/userguide/welcome.html) repository. Jenkins pulls it on a build start.

1. A Unity container image is pulled from Amazon Elastic Container Registry and deployed by the Jenkins Docker agent on a worker node.

1. The first build stage runs on [Amazon EC2](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/concepts.html) Spot Instances. It generates an Xcode project from Unity source code. These instances are placed into an Auto Scaling group for scalability and redundancy.

1. A Unity Build Server vends floating licenses to workers in the Auto Scaling group.

1. The Unity license binds to the Amazon EC2 instance's Ethernet interface MAC address. An elastic network interface preserves the MAC address if the instance is recreated.

1. The resulting Xcode project transfers to a Jenkins worker on an Amazon EC2 Mac Instance. This worker finalizes and signs the build and exports an .ipa file.

1. Certificates, private keys, and provisioning profiles are stored in AWS Secrets Manager. The Mac dynamically pulls them during a build.

1. An .ipa archive file is exported as a Jenkins artifact and stored in an [Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html) bucket.

## Further reading
<a name="further-reading"></a>

For additional information, refer to
+ [AWS Architecture Icons](https://aws.amazon.com/architecture/icons)
+ [AWS Architecture Center](https://aws.amazon.com/architecture)
+ [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected)
+ [AWS Game Tech product page](https://aws.amazon.com/gametech/)

## Diagram history
<a name="diagram-history"></a>

To be notified about updates to this reference architecture diagram, subscribe to the RSS feed.

| Change | Description | Date | 
| --- |--- |--- |
| [Initial publication](#diagram-history) | Reference architecture diagram first published. | November 24, 2021 | 

**Note**  
To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you are using.