

# Pull request continuous integration

Publication date: **July 14, 2022 ([Diagram history](diagram-history.md))**

With this architecture, you can build a continuous integration pipeline for Git pull requests by using AWS CodeBuild, AWS CodePipeline, and AWS Lambda.

## Pull request continuous integration diagram
<a name="pull-request-continuous-integration-diagram"></a>

![Pull request continuous integration pipeline using CodeBuild, CodePipeline, and Lambda with Git providers.](https://docs.aws.amazon.com/reference-architecture-diagrams/latest/devops/images/pull-request-continuous-integration.png)


The following steps describe the architecture:

1. Webhooks connect supported Git providers (such as GitHub or Bitbucket) and AWS CodeBuild. The Git provider sends events when a PR is created or updated. For [AWS CodeCommit](https://docs.aws.amazon.com/codecommit/latest/userguide/), an [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/) function triggers the build.

1. CodeBuild accepts Git PR events and compresses the PR codebase in an archive. It stores this archive in the Git Artifacts [Amazon S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/) bucket. CodeBuild then posts a message on an [Amazon Simple Queue Service](https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/) queue about a fresh codebase ready for processing.

1. An Lambda function polls the Amazon SQS queue and consumes the message. It starts the CI process and moves the new codebase to the Pipeline Source Amazon S3 bucket. The Lambda function checks automation prerequisites. It also removes obsolete codebases from the backlog when updates target an existing PR.

1. [AWS CodePipeline](https://docs.aws.amazon.com/codepipeline/latest/userguide/) orchestrates the CI workflow. It validates the codebase, runs unit tests, builds artifacts, creates a preview environment, and runs integration and end-to-end (E2E) tests. [Amazon EventBridge](https://docs.aws.amazon.com/eventbridge/latest/userguide/) monitors pipeline stage changes. An Lambda function updates the PR based on status events (success, in progress, failed, completed).

## Further reading
<a name="pull-request-continuous-integration-further-reading"></a>

For additional information, see the following resources:
+ [AWS Architecture Icons](https://aws.amazon.com/architecture/icons)
+ [AWS Architecture Center](https://aws.amazon.com/architecture)
+ [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected)
+ [AWS CodePipeline product page](https://aws.amazon.com/codepipeline/)