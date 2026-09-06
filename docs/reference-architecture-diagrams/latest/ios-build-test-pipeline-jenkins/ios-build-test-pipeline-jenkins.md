

# iOS Build and Test Pipeline Using Jenkins
<a name="ios-build-test-pipeline-jenkins"></a>

Publication date: **November 23, 2021 ([Diagram history](#diagram-history))**

This architecture shows how to automate building and testing iOS apps by using Jenkins, Amazon Elastic Compute Cloud Mac instances, and AWS Device Farm.

## iOS Build and Test Pipeline Using Jenkins
<a name="diagram1"></a>

![Architecture diagram showing an iOS build and test pipeline by using Jenkins, Amazon Elastic Compute Cloud Mac instances, and AWS Device Farm.](http://docs.aws.amazon.com/reference-architecture-diagrams/latest/ios-build-test-pipeline-jenkins/images/ios-build-test-pipeline-jenkins.png)


1. A developer initiates a build and test activity in [Amazon API Gateway](https://docs.aws.amazon.com/codepipeline/latest/userguide/welcome.html) by pushing a code change to [AWS CodeCommit](https://docs.aws.amazon.com/codecommit/latest/userguide/welcome.html).

1. Amazon API Gateway detects the change in AWS CodeCommit and creates a job for Jenkins.

1. Jenkins on [Amazon EC2](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/concepts.html) Mac uses the CodePipeline plugin to poll Amazon API Gateway, downloads the source, and triggers the build project.

1. The Amazon EC2 Mac instance builds the artifacts (as .ipa files). The CodePipeline plugin for Jenkins compresses and uploads the build artifacts to Amazon API Gateway through [Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html).

1. Amazon API Gateway runs the test stage on [AWS Device Farm](https://docs.aws.amazon.com/devicefarm/latest/developerguide/welcome.html) to test the build artifacts (.ipa files) on multiple real devices.

1. AWS Device Farm automatically fetches the build artifacts from the Amazon S3 bucket, runs the test cases, and records the results.

1. AWS Device Farm makes the test results, logs, and recordings available for review through the Device Farm console or through Amazon S3 pre-signed URLs.

## Further reading
<a name="further-reading"></a>

For additional information, refer to
+ [AWS Architecture Icons](https://aws.amazon.com/architecture/icons)
+ [AWS Architecture Center](https://aws.amazon.com/architecture)
+ [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected)
+ [Amazon API Gateway product page](https://aws.amazon.com/codepipeline/)

## Diagram history
<a name="diagram-history"></a>

To be notified about updates to this reference architecture diagram, subscribe to the RSS feed.

| Change | Description | Date | 
| --- |--- |--- |
| [Initial publication](#diagram-history) | Reference architecture diagram first published. | November 23, 2021 | 

**Note**  
To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you are using.