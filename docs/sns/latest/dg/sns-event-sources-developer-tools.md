

# Developer tools services
<a name="sns-event-sources-developer-tools"></a>

The following table describes how Amazon SNS integrates with AWS developer tools services, such as AWS CodeBuild, AWS CodeCommit, AWS CodeDeploy, Amazon CodeGuru, and AWS CodePipeline to provide notifications for critical events such as build status changes, repository updates, deployment progress, performance anomalies, and pipeline actions. 

These integrations helps you efficiently monitor and manage your software development workflows by receiving timely alerts on important events.


| AWS service | Benefit of using with Amazon SNS | 
| --- | --- | 
| [AWS CodeBuild](https://docs.aws.amazon.com/codebuild/latest/userguide/welcome.html) – Compiles your source code, runs unit tests, and produces artifacts that are ready to deploy. | Receive notifications when builds succeed, fail, or move from one build phase to another. For more information, see [Build notifications sample for CodeBuild](https://docs.aws.amazon.com/codebuild/latest/userguide/sample-build-notifications.html) in the *AWS CodeBuild User Guide*. | 
| [AWS CodeCommit](https://docs.aws.amazon.com/codecommit/latest/userguide/welcome.html) – Provides version control for privately storing and managing assets in the cloud. | Receive notifications about CodeCommit repository events. For more information, see [Example: Create an AWS CodeCommit trigger for an Amazon SNS topic](https://docs.aws.amazon.com/codecommit/latest/userguide/how-to-notify-sns.html) in the *AWS CodeCommit User Guide*. | 
| [AWS CodeDeploy](https://docs.aws.amazon.com/codedeploy/latest/userguide/welcome.html) – Automates application deployments to Amazon EC2 instances, on-premises instances, serverless Lambda functions, or Amazon ECS services. | Receive notifications for CodeDeploy deployments or instance events. For more information, see [Create a trigger for a CodeDeploy event](https://docs.aws.amazon.com/codedeploy/latest/userguide/monitoring-sns-event-notifications-create-trigger.html) in the *AWS CodeDeploy User Guide*. | 
| [Amazon CodeGuru](https://docs.aws.amazon.com/codeguru/latest/profiler-ug/what-is-codeguru-profiler.html) – Collects runtime performance data from your live applications, and provides recommendations that can help you fine-tune your application performance. | Receive notifications when anomalies occur. For more information, see [Working with anomalies and recommendation reports](https://docs.aws.amazon.com/codeguru/latest/profiler-ug/working-with-recommendation-reports.html) in the *Amazon CodeGuru User Guide*. | 
| [AWS CodePipeline](https://docs.aws.amazon.com/codepipeline/latest/userguide/welcome.html) – Automates the steps required to release software changes continuously. | Receive notifications about approval actions. For more information, see [Manage approval actions in CodePipeline](https://docs.aws.amazon.com/codepipeline/latest/userguide/approvals.html) in the *AWS CodePipeline User Guide*. | 