

# REL08-BP05 Deploy changes with automation

 Changes to production are one of the largest sources of operational risk. Automate deployments and patching to remove manual steps where human error exists so that every change follows the same tested path. 

 **Desired outcome:** 
+  Your release process runs through automation with pre-production testing, automatic rollback, and staggered production deployments. 
+  Developers no longer watch deployments manually, because the pipeline catches and reverses failures. 
+  You lint and test your infrastructure as code to catch configuration failures before they reach production. 
+  When a production failure occurs, you add a test that catches the same problem in future releases. 

 **Common anti-patterns:** 
+  Teams make manual changes to production. 
+  Teams skip automated steps through manual emergency workflows. 
+  Teams abandon established plans and processes to meet accelerated timelines. 
+  Teams run rapid follow-on deployments without allowing bake time. 
+  Teams do not lint their infrastructure as code, so known failure patterns reach production. 
+  Teams do not update their tests after a failure occurs. 

 **Benefits of establishing this best practice:** 
+  Human error drops because automation replaces manual deployment steps. 
+  Problems are caught before production, because every change is tested on the way there. 
+  Automatic rollback returns the workload to its last working state when a production issue appears. 
+  Infrastructure misconfigurations are caught in the pipeline through linting rather than in production. 

 **Level of risk exposed if this best practice is not established:** Medium 

## Implementation guidance
<a name="implementation-guidance"></a>

 Automated deployment builds on a [continuous integration and continuous delivery](https://en.wikipedia.org/wiki/CI/CD) (CI/CD) pipeline. A commit passes through automated stage gates for build, test, and deployment, and each gate can halt the pipeline or trigger a rollback. The pipeline runs tests, detects anomalies, and reverses changes automatically. 

 Automate your hardest procedures, because they are the most likely to fail when done by humans under pressure. A rarely-used procedure run manually during an incident is a common source of new failures. Encode the procedure once, test it, and run it automatically to remove that risk. 

 Apply the same quality controls to IaC as to application code. Lint your infrastructure templates to catch common misconfigurations, such as insecure settings or missing guardrails, before deployment. New failure patterns emerge over time, so update your linting rules as you discover them and confirm each is addressed before deployment. Enforce reliability thresholds, such as a minimum instance count for availability, early in the pipeline. 

 *Bake time* is how long you wait after a deployment before marking it healthy and continuing. Without bake time, rapid follow-on deployments stack unverified changes, so when something breaks you cannot tell which change caused it. Configuration parameters have the same risk. Templates use variables that differ between environments, and passing those variables on the command line invites human error. Store configuration in a repository, deploy it through a pipeline, and have deployments read only approved values. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Store code and configuration in a repository:** Use a hosted source control system based on a widely adopted technology such as Git to store application source and infrastructure as code (IaC) configuration securely. 

1.  **Configure a continuous integration service:** Compile source, run tests, and produce deployment artifacts automatically. To set up a build project, see [Getting started with AWS CodeBuild using the console](https://docs.aws.amazon.com/codebuild/latest/userguide/). 

1.  **Configure an automated deployment service:** Use [AWS CodeDeploy](https://docs.aws.amazon.com/codedeploy/latest/userguide/getting-started-codedeploy.html) to deploy to compute services such as Amazon EC2, [AWS Fargate](https://aws.amazon.com/fargate/), and [AWS Lambda](https://aws.amazon.com/lambda/), as well as on-premises servers, without relying on error-prone manual steps. 

1.  **Automate the release pipeline:** Use [AWS CodePipeline](https://docs.aws.amazon.com/codepipeline/latest/userguide/getting-started-codepipeline.html) to orchestrate build, test, and deployment stages for faster, more reliable updates. For examples, see the [CodePipeline tutorials](https://docs.aws.amazon.com/codepipeline/latest/userguide/tutorials.html). 

1.  **Lint your infrastructure as code:** Scan templates for common failure scenarios with a tool such as [cfn\_nag](https://github.com/stelligent/cfn_nag), and update the rules as new misconfigurations are discovered. Enforce availability and performance thresholds early in the pipeline. 

1.  **Manage environmental configuration through change control:** Store template variables in a repository and deploy them through a pipeline rather than passing them on the command line. Use a service such as [AWS AppConfig](https://docs.aws.amazon.com/appconfig/latest/userguide/what-is-appconfig.html) so deployments read only approved settings, and monitor changes to these parameters. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [REL08-BP04 Deploy using immutable infrastructure](rel08-bp04.md) 
+  [REL08-BP01 Use runbooks for standard activities such as deployment](rel08-bp01.md) 
+  [OPS03-BP04 Fully automate integration and deployment](ops03-bp04.md) 
+  [OPS04-BP02 Automate testing and rollback](ops04-bp02.md) 
+  [OPS04-BP01 Employ and test safe deployment strategies](ops04-bp01.md) 

 **Related documents:** 
+  [Blue/Green Deployments to Amazon ECS using AWS CloudFormation and AWS CodeDeploy](https://aws.amazon.com/blogs/devops/blue-green-deployments-to-amazon-ecs-using-aws-cloudformation-and-aws-codedeploy) 
+  [The Amazon Builders' Library: Ensuring rollback safety during deployments](https://builder.aws.com/content/3F04j2yRAAMBuPSPs50xwXZqg01/ensuring-rollback-safety-during-deployments) 
+  [The Amazon Builders' Library: Going faster with continuous delivery](https://builder.aws.com/content/3F08Mhh186qOa4VhG19egs06NJa/going-faster-with-continuous-delivery) 
+  [What is AWS CodePipeline?](https://docs.aws.amazon.com/codepipeline/latest/userguide/welcome.html) 
+  [What is CodeDeploy?](https://docs.aws.amazon.com/codedeploy/latest/userguide/welcome.html) 
+  [AWS Systems Manager Patch Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/patch-manager.html) 
+  [What is Amazon Q Developer in chat applications?](https://docs.aws.amazon.com/chatbot/latest/adminguide/what-is.html) 
+  [What is Amazon SES?](https://docs.aws.amazon.com/ses/latest/dg/Welcome.html) 
+  [What is Amazon SNS?](https://docs.aws.amazon.com/sns/latest/dg/welcome.html) 

 **Related videos:** 
+  [AWS re:Invent 2025 - Continuous integration and continuous delivery (CI/CD) for AWS (DVT202)](https://www.youtube.com/watch?v=rm9gPOlUxNY) 

 **Related tools:** 
+  [GitHub - stelligent/cfn\_nag: Linting tool for CloudFormation templates](https://github.com/stelligent/cfn_nag) 
+  [AWS Partner Network: partners that can help you create automated deployment solutions](https://partners.amazonaws.com/search/partners?keyword=devops) 
+  [AWS Marketplace: products that can be used to automate your deployments](https://aws.amazon.com/marketplace/search/results?searchTerms=DevOps) 