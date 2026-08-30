# Pull Request Continuous Integration

Publication date: **July 14, 2022 ([Diagram history](#diagram-history "#diagram-history"))**

This architecture shows how to build a continuous integration pipeline for Git pull requests by using AWS CodeBuild, Amazon API Gateway, and AWS Lambda.

## Pull Request Continuous Integration

![Architecture diagram showing a pull request continuous integration pipeline by using AWS CodeBuild, Amazon API Gateway, and AWS Lambda.](images/pull-request-continuous-integration.png)

1. Webhooks connect supported Git providers (such as GitHub or Bitbucket) and AWS CodeBuild. The Git provider sends events when a PR is created or updated. For [AWS CodeCommit](../../../codecommit/latest/userguide/welcome.md "../../../codecommit/latest/userguide/welcome.md"), an [AWS Lambda](../../../lambda/latest/dg/welcome.md "../../../lambda/latest/dg/welcome.md") function triggers the build.
2. AWS CodeBuild accepts Git PR events and compresses the PR codebase in an archive. It stores this archive in the Git Artifacts [Amazon S3](../../../AmazonS3/latest/userguide/Welcome.md "../../../AmazonS3/latest/userguide/Welcome.md") bucket. AWS CodeBuild then posts a message on an [Amazon Simple Queue Service](../../../AWSSimpleQueueService/latest/SQSDeveloperGuide/welcome.md "../../../AWSSimpleQueueService/latest/SQSDeveloperGuide/welcome.md") queue about a fresh codebase ready for processing.
3. An Lambda function polls the Amazon SQS queue and consumes the message. It starts the CI process and moves the new codebase to the Pipeline Source Amazon S3 bucket. The Lambda function checks automation prerequisites. It also removes obsolete codebases from the backlog when updates target an existing PR.
4. [Amazon API Gateway](../../../codepipeline/latest/userguide/welcome.md "../../../codepipeline/latest/userguide/welcome.md") orchestrates the CI workflow. It validates the codebase, runs unit tests, builds artifacts, creates a preview environment, and runs integration and end-to-end (E2E) tests. [https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-what-is.html](../../../eventbridge/latest/userguide/eb-what-is.md "../../../eventbridge/latest/userguide/eb-what-is.md") monitors pipeline stage changes. An Lambda function updates the PR based on status events (success, in progress, failed, completed).

## Further reading

For additional information, refer to

- [AWS Architecture Icons](https://aws.amazon.com/architecture/icons "https://aws.amazon.com/architecture/icons")
- [AWS Architecture Center](https://aws.amazon.com/architecture "https://aws.amazon.com/architecture")
- [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected "https://aws.amazon.com/architecture/well-architected")
- [Amazon API Gateway product page](https://aws.amazon.com/codepipeline/ "https://aws.amazon.com/codepipeline/")

## Diagram history

To be notified about updates to this reference architecture diagram, subscribe to the RSS feed.

| Change              | Description                                     | Date          |
| ------------------- | ----------------------------------------------- | ------------- |
| Initial publication | Reference architecture diagram first published. | July 14, 2022 |

###### Note

To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you are using.
