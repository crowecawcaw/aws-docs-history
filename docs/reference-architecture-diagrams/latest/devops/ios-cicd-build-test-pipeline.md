

# iOS CI/CD build and test pipeline

Publication date: **November 17, 2021 ([Diagram history](diagram-history.md))**

With this architecture, you can automate building and testing iOS apps by using AWS CodePipeline, Amazon Elastic Compute Cloud Mac instances, and AWS Device Farm.

## iOS CI/CD build and test pipeline diagram
<a name="ios-cicd-build-test-pipeline-diagram"></a>

![iOS CI/CD build and test pipeline using CodePipeline, Amazon EC2 Mac instances, and Device Farm for device testing.](https://docs.aws.amazon.com/reference-architecture-diagrams/latest/devops/images/ios-cicd-build-test-pipeline.png)


The following steps describe the architecture:

1. A developer initiates a build or test activity in [AWS CodePipeline](https://docs.aws.amazon.com/codepipeline/latest/userguide/) by pushing a code change to [AWS CodeCommit](https://docs.aws.amazon.com/codecommit/latest/userguide/).

1. CodePipeline detects the change in CodeCommit and invokes [AWS Step Functions](https://docs.aws.amazon.com/step-functions/latest/dg/welcome.html) to start the build process.

1. An [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/) function loads required build scripts from an [Amazon Simple Storage Service](https://docs.aws.amazon.com/AmazonS3/latest/userguide/) bucket and triggers an [AWS Systems Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/) Run Command.

1. Build scripts initiate an iOS build on the [Amazon Elastic Compute Cloud](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/) Mac instance and put the build artifacts in an Amazon S3 bucket.

1. The Systems Manager Run Command runs the build scripts on an Amazon EC2 Mac instance and sends run logs to [Amazon CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/).

1. CodePipeline detects the built artifacts in Amazon S3 and starts [Device Farm](https://docs.aws.amazon.com/devicefarm/latest/developerguide/) to test the app on multiple real devices.

1. Device Farm generates test results, logs, and recordings. You can review them through the Device Farm console or through Amazon S3 pre-signed URLs.

## Further reading
<a name="ios-cicd-build-test-pipeline-further-reading"></a>

For additional information, see the following resources:
+ [AWS Architecture Icons](https://aws.amazon.com/architecture/icons)
+ [AWS Architecture Center](https://aws.amazon.com/architecture)
+ [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected)
+ [AWS CodePipeline product page](https://aws.amazon.com/codepipeline/)