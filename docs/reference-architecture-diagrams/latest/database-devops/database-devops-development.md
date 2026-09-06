

# Database DevOps on AWS: Development Workflow
<a name="database-devops-development"></a>

Publication date: **March 31, 2023 ([Diagram history](#diagram-history))**

Use this architecture in the development workflow to automate database changes as part of DevOps practice. Build an orchestration to deploy database changes at the same rate as application code, enforce database-application-joint code reviews, integrate database and application code operations, detect abnormal system behavior, and automate notifications to appointed teams.

## Database DevOps on AWS: Development Workflow
<a name="diagram1"></a>

![Architecture diagram showing database DevOps development workflow with AWS CodeCommit, CodePipeline, CodeBuild, and Amazon RDS.](http://docs.aws.amazon.com/reference-architecture-diagrams/latest/database-devops/images/database-devops-1.png)


The following steps describe the architecture:

1. The developer checks both application and database code into [AWS CodeCommit](https://docs.aws.amazon.com/codecommit/latest/userguide/welcome.html).

1. At every push request, AWS CodeCommit enforces code reviews through the use of approval rules.

1. Amazon CodeGuru Reviewer automatically evaluates code changes, detects errors, and offers code recommendations.

1. AWS CodeCommit initiates [CodePipeline](https://docs.aws.amazon.com/codepipeline/latest/userguide/welcome.html) to take pipeline actions.

1. The CodePipeline Source action checks out application and database code.

1. The CodePipeline Build action invokes a build management tool to start the application and database code build phase.

1. The build tool calls the database change tool. It downloads the database scripts and runs them against the target database.

1. The build tool calls database test scripts and validates output.

1. The CodePipeline Deploy action deploys code to the target environment.

1. Build artifacts are published to [AWS CodeArtifact](https://docs.aws.amazon.com/codeartifact/latest/ug/welcome.html) for others to consume.

1. (Optional) Use Performance Insights on [Amazon RDS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Welcome.html) and Amazon DevOps Guru to automatically apply ML techniques to detect performance bottlenecks and operational issues.

1. [EventBridge](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-what-is.html) captures events and sends them to an [Amazon SNS](https://docs.aws.amazon.com/sns/latest/dg/welcome.html) topic for user notifications.

## Further reading
<a name="further-reading"></a>

For additional information, refer to the following resources:
+ [AWS Architecture Icons](https://aws.amazon.com/architecture/icons)
+ [AWS Architecture Center](https://aws.amazon.com/architecture)
+ [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected)

## Diagram history
<a name="diagram-history"></a>

To be notified about updates to this reference architecture diagram, subscribe to the RSS feed.

| Change | Description | Date | 
| --- |--- |--- |
| [Initial publication](#diagram-history) | Reference architecture diagram first published. | March 31, 2023 | 

**Note**  
To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you are using.