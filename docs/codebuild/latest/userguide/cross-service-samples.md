# Cross-service samples for CodeBuild

You can use these cross-service samples to experiment with AWS CodeBuild:

[Amazon ECR sample](sample-ecr.md "sample-ecr.md")

Uses a Docker image in an Amazon ECR repository to use Apache Maven to produce a
single JAR file. The sample instructions will show you how to create and push a
Docker image to Amazon ECR, create a Go project, build the project, run the project,
and set up permissions to allow CodeBuild to connect to Amazon ECR.

[Amazon EFS sample](sample-efs.md "sample-efs.md")

Shows how to configure a buildspec file so that a CodeBuild project mounts and
builds on an Amazon EFS file system. The sample instructions will show you how to
create a Amazon VPC, create file system in the Amazon VPC, create and build a project that
uses the Amazon VPC, and then review the generated project file and variables.

[AWS CodePipeline samples](sample-codepipeline.md "sample-codepipeline.md")

Shows how to use AWS CodePipeline to create a build with batch builds as well as
multiple input sources and multiple output artifacts. Included in this section
are example JSON files that show pipeline structures that create batch builds
with separate artifacts, and combined artifacts. An additonal JSON sample is
provided that show the pipeline structure with multiple input sources and
multiple output artifacts.

[AWS Config sample](how-to-integrate-config.md "how-to-integrate-config.md")

Shows how to set up AWS Config. Lists which CodeBuild resources are tracked and
describes how to look up CodeBuild projects in AWS Config. The sample instructions will
show you the prerequisites for integrating with AWS Config, the steps to set up AWS Config,
and the steps to look up CodeBuild projects and data in AWS Config.

[Build notifications
sample](sample-build-notifications.md "sample-build-notifications.md")

Uses Apache Maven to produce a single JAR file. Sends a build notification to
subscribers of an Amazon SNS topic. The sample instructions show you how to set up
permissions so that CodeBuild can communicate with Amazon SNS and CloudWatch, how to create and
identify CodeBuild topics in Amazon SNS, how to subscribe recipients to the topic, and
how to set up rules in CloudWatch.
