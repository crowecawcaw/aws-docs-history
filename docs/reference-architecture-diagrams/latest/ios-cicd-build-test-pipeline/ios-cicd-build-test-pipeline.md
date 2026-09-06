

# iOS CI/CD Build and Test Pipeline
<a name="ios-cicd-build-test-pipeline"></a>

Publication date: **November 17, 2021 ([Diagram history](#diagram-history))**

This architecture shows how to automate building and testing iOS apps by using Amazon API Gateway, Amazon Elastic Compute Cloud Mac instances, and AWS Device Farm.

## iOS CI/CD Build and Test Pipeline
<a name="diagram1"></a>

![Architecture diagram showing an iOS CI/CD build and test pipeline by using Amazon API Gateway, Amazon Elastic Compute Cloud Mac instances, and AWS Device Farm.](http://docs.aws.amazon.com/reference-architecture-diagrams/latest/ios-cicd-build-test-pipeline/images/ios-cicd-build-test-pipeline.png)


1. A developer initiates a build or test activity in [Amazon API Gateway](https://docs.aws.amazon.com/codepipeline/latest/userguide/welcome.html) by pushing a code change to [AWS CodeCommit](https://docs.aws.amazon.com/codecommit/latest/userguide/welcome.html).

1. Amazon API Gateway detects the change in AWS CodeCommit and invokes [AWS Step Functions](https://docs.aws.amazon.com/step-functions/latest/dg/welcome.html) to start the build process.

1. An [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/welcome.html) function loads required build scripts from an [Amazon Simple Storage Service](https://docs.aws.amazon.com/AmazonS3/latest/userguide/Welcome.html) bucket and triggers an [AWS Systems Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/what-is-systems-manager.html) Run command.

1. Build scripts initiate an iOS build on the [Amazon Elastic Compute Cloud](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/concepts.html) Mac instance and put the build artifacts in an Amazon S3 bucket.

1. The AWS Systems Manager Run command runs the build scripts on an Amazon EC2 Mac instance and sends run logs to [Amazon CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/WhatIsCloudWatch.html).

1. Amazon API Gateway detects the built artifacts in Amazon S3 and starts [AWS Device Farm](https://docs.aws.amazon.com/devicefarm/latest/developerguide/welcome.html) to test the app on multiple real devices.

1. AWS Device Farm generates test results, logs, and recordings. You can review them through the AWS Device Farm console or through Amazon S3 pre-signed URLs.

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
| [Initial publication](#diagram-history) | Reference architecture diagram first published. | November 17, 2021 | 

**Note**  
To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you are using.