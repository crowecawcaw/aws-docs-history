

# iOS build and test pipeline using Jenkins

Publication date: **November 23, 2021 ([Diagram history](diagram-history.md))**

With this architecture, you can automate building and testing iOS apps by using Jenkins, Amazon Elastic Compute Cloud Mac instances, and AWS Device Farm.

## iOS build and test pipeline using Jenkins diagram
<a name="ios-build-test-pipeline-jenkins-diagram"></a>

![iOS build and test pipeline using Jenkins, Amazon EC2 Mac instances, and Device Farm for device testing.](https://docs.aws.amazon.com/reference-architecture-diagrams/latest/devops/images/ios-build-test-pipeline-jenkins.png)


The following steps describe the architecture:

1. A developer initiates a build and test activity in [AWS CodePipeline](https://docs.aws.amazon.com/codepipeline/latest/userguide/) by pushing a code change to [AWS CodeCommit](https://docs.aws.amazon.com/codecommit/latest/userguide/).

1. CodePipeline detects the change in CodeCommit and creates a job for Jenkins.

1. Jenkins on [Amazon EC2](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/) Mac uses the CodePipeline plugin to poll CodePipeline, downloads the source, and triggers the build project.

1. The Amazon EC2 Mac instance builds the artifacts (as .ipa files). The CodePipeline plugin for Jenkins compresses and uploads the build artifacts to CodePipeline through [Amazon Simple Storage Service](https://docs.aws.amazon.com/AmazonS3/latest/userguide/).

1. CodePipeline runs the test stage on [Device Farm](https://docs.aws.amazon.com/devicefarm/latest/developerguide/) to test the build artifacts (.ipa files) on multiple real devices.

1. Device Farm automatically fetches the build artifacts from the Amazon S3 bucket, runs the test cases, and records the results.

1. Device Farm makes the test results, logs, and recordings available for review through the Device Farm console or through Amazon S3 pre-signed URLs.

## Further reading
<a name="ios-build-test-pipeline-jenkins-further-reading"></a>

For additional information, see the following resources:
+ [AWS Architecture Icons](https://aws.amazon.com/architecture/icons)
+ [AWS Architecture Center](https://aws.amazon.com/architecture)
+ [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected)
+ [AWS CodePipeline product page](https://aws.amazon.com/codepipeline/)