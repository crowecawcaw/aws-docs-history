

# Database DevOps on AWS: Production Workflow
<a name="database-devops-production"></a>

Publication date: **March 31, 2023 ([Diagram history](database-devops-development.md#diagram-history))**

Use this architecture in the production workflow to automate database changes as part of DevOps practice. Build an orchestration to deploy database changes at the same rate as application code, detect abnormal system behavior, and automate notifications to appointed teams to take corrective actions.

## Database DevOps on AWS: Production Workflow
<a name="diagram2"></a>

![Architecture diagram showing database DevOps production workflow with CodePipeline, CodeBuild, and Amazon RDS.](http://docs.aws.amazon.com/reference-architecture-diagrams/latest/database-devops/images/database-devops-2.png)


The following steps describe the architecture:

1. The release manager issues a production deployment request.

1. [CodePipeline](https://docs.aws.amazon.com/codepipeline/latest/userguide/welcome.html) invokes the build management tool which calls the database change management tool.

1. The database change tool downloads the database change scripts and runs them against the target [Amazon RDS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/Welcome.html) production database.

1. CodePipeline initiates the Deploy action to deploy code to the target environment.

1. (Optional) Use Performance Insights on Amazon RDS and Amazon DevOps Guru to automatically apply ML techniques to detect performance bottlenecks and operational issues.

1. [EventBridge](https://docs.aws.amazon.com/eventbridge/latest/userguide/eb-what-is.html) captures events and sends them to an [Amazon SNS](https://docs.aws.amazon.com/sns/latest/dg/welcome.html) topic for user notifications.