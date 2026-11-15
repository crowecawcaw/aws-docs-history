

# Database DevOps on AWS
<a name="database-devops"></a>

Publication date: **March 31, 2023 ([Diagram history](diagram-history.md))**

Use this architecture in the development workflow to automate database changes as part of DevOps practice. Build an orchestration to deploy database changes at the same rate as application code, enforce database-application-joint code reviews, integrate database and application code operations, detect abnormal system behavior, and automate notifications to appointed teams.

## Development workflow
<a name="database-devops-development"></a>

![A developer commits code to CodeCommit, and CodePipeline builds, tests, and deploys it to Amazon RDS.](https://docs.aws.amazon.com/reference-architecture-diagrams/latest/data-analytics/images/database-devops-1.png)


The following steps describe the architecture:

1. The developer commits both application and database code to [AWS CodeCommit](https://docs.aws.amazon.com/codecommit/latest/userguide/).

1. At every push request, AWS CodeCommit enforces code reviews through the use of approval rules.

1. [Amazon CodeGuru Reviewer](https://docs.aws.amazon.com/codeguru/latest/reviewer-ug/) automatically evaluates code changes, detects errors, and offers code recommendations.

1. AWS CodeCommit initiates [AWS CodePipeline](https://docs.aws.amazon.com/codepipeline/latest/userguide/) to take pipeline actions.

1. The CodePipeline Source action checks out application and database code.

1. The CodePipeline Build action invokes a build management tool to start the application and database code build phase.

1. The build tool calls the database change tool. It downloads the database scripts and runs them against the target database.

1. The build tool calls database test scripts and validates output.

1. The CodePipeline Deploy action deploys code to the target environment.

1. The CodePipeline Build action publishes build artifacts to [AWS CodeArtifact](https://docs.aws.amazon.com/codeartifact/latest/ug/) for others to consume.

1. (Optional) Performance Insights on [Amazon RDS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/) and [Amazon DevOps Guru](https://docs.aws.amazon.com/devops-guru/latest/userguide/) automatically apply ML techniques to detect performance bottlenecks and operational issues.

1. [Amazon EventBridge](https://docs.aws.amazon.com/eventbridge/latest/userguide/) captures events and sends them to an [Amazon SNS](https://docs.aws.amazon.com/sns/latest/dg/) topic for user notifications.

## Production workflow
<a name="database-devops-production"></a>

Use this architecture in the production workflow to automate database changes as part of DevOps practice. Build an orchestration to deploy database changes at the same rate as application code, detect abnormal system behavior, and automate notifications to appointed teams to take corrective actions.

![CodePipeline builds and deploys database changes to the Amazon RDS production database.](https://docs.aws.amazon.com/reference-architecture-diagrams/latest/data-analytics/images/database-devops-2.png)


The following steps describe the architecture:

1. The release manager issues a production deployment request.

1. CodePipeline invokes the build management tool which calls the database change management tool.

1. The database change tool downloads the database change scripts and runs them against the target Amazon RDS production database.

1. CodePipeline initiates the Deploy action to deploy code to the target environment.

1. (Optional) Use Performance Insights on Amazon RDS and DevOps Guru to automatically apply ML techniques to detect performance bottlenecks and operational issues.

1. EventBridge captures events and sends them to an Amazon SNS topic for user notifications.

## Further reading
<a name="database-devops-further-reading"></a>

For additional information, refer to the following resources:
+ [AWS Architecture Icons](https://aws.amazon.com/architecture/icons)
+ [AWS Architecture Center](https://aws.amazon.com/architecture)
+ [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected)