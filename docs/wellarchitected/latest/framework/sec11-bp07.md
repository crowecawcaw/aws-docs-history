

# SEC11-BP07 Deploy software programmatically

 Manual deployments introduce human error and make it hard to prove that what you tested is what you released. Programmatic deployment runs the same steps every time, removes people from the production path, and gives you a way to verify the integrity of each release. Externalize configuration so one artifact runs in any environment, and sign packages so you can prove they did not change. 

 **Desired outcome:** 
+  You deploy the exact version you tested, and deployment runs the same way every time. 
+  You externalize configuration, so the same artifact deploys to different environments without change. 
+  You cryptographically sign your packages and verify the signatures during deployment. 
+  You remove persistent human access to production environments in favor of automated pipelines. 

 **Common anti-patterns:** 
+  Teams deploy software to production manually. 
+  Teams modify software manually to suit different environments. 

 **Benefits of establishing this best practice:** 
+  Confidence in the release process increases because deployments are consistent and repeatable. 
+  The risk of a failed change affecting business functionality drops. 
+  Release cadence increases because each change carries less risk. 
+  Rollback becomes automatic when a deployment encounters an unexpected event. 
+  You can cryptographically prove that the software tested is the software deployed. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 Manual deployments fail through forgotten flags, steps that were run in the wrong order, or config values that were edited on the production host. Such mistakes are hard to reproduce and hard to audit, and they explain why a change that worked in testing fails in production. Encode the deployment once and run it identically every time. 

 Build one artifact and move that exact artifact through your environments. If you rebuild or hand-modify for each environment, production runs a different version of the artifact than the one you tested. Keep environment-specific settings out of the artifact and read them at deploy or run time from a store such as [AWS Systems Manager Parameter Store](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-parameter-store.html). Sign the artifact after testing with [AWS Signer](https://docs.aws.amazon.com/signer/latest/developerguide/Welcome.html) or [AWS Key Management Service (AWS KMS)](https://aws.amazon.com/kms/), and verify the signature before deployment. Signing algorithms will change as post-quantum algorithms replace traditional ones, and not every environment supports them. Choose signing mechanisms you can move to a new algorithm without re-architecting, and prefer managed ones. The more managed the mechanism, the more of the transition sits on AWS' side of the shared responsibility model. 

 Remove persistent human access from production so every change reaches it through the pipeline, where it is tested, reviewed, and recorded. Separate environments into distinct accounts so a mistake in development cannot reach production (for more detail, see [Organizing your AWS environment using multiple accounts](https://docs.aws.amazon.com/whitepapers/latest/organizing-your-aws-environment/organizing-your-aws-environment.html)). Run build, test, and deployment through continuous integration and delivery tools such as [AWS CodeBuild](https://aws.amazon.com/codebuild/) and [AWS CodePipeline](https://aws.amazon.com/codepipeline/). 

 Apply the same repeatability to infrastructure. Define infrastructure with [AWS CloudFormation](https://aws.amazon.com/cloudformation/) or the [AWS Cloud Development Kit (AWS CDK) (AWS CDK)](https://aws.amazon.com/cdk/) so environments are created the same way and drift is visible. Deploy progressively to limit the scope of impact. A canary releases the change to a small subset of instances or users first. Watch its effect and roll back before a bad change reaches your entire user base. [AWS CodeDeploy](https://aws.amazon.com/codedeploy/) supports canaries for Amazon EC2 and AWS Lambda. Amazon ECS provides [blue/green service deployments](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/deployment-type-blue-green.html), with bake time, hooks for automated validation, and rollback to the previous revision. [AWS CodePipeline](https://aws.amazon.com/codepipeline/) can also [roll back a stage](https://docs.aws.amazon.com/codepipeline/latest/userguide/stage-rollback.html) automatically when it fails. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Separate environments into accounts:** Follow [Organizing your AWS environment using multiple accounts](https://docs.aws.amazon.com/whitepapers/latest/organizing-your-aws-environment/organizing-your-aws-environment.html) to place development, staging, and production in distinct accounts. Configure access controls that remove direct human access to production. 

1.  **Build a CI/CD pipeline:** Use [AWS CodeBuild](https://aws.amazon.com/codebuild/) and [AWS CodePipeline](https://aws.amazon.com/codepipeline/) to build, test, and deploy automatically. Connect your code repositories to the pipeline for version control. 

1.  **Sign and verify packages:** Sign artifacts after testing with [AWS Signer](https://docs.aws.amazon.com/signer/latest/developerguide/Welcome.html) or [AWS KMS](https://aws.amazon.com/kms/), and verify the signature before deploying so only validated code reaches each environment. For container workloads, verify the signature again when the cluster admits the image. 

1.  **Externalize configuration:** Store environment-specific settings in [AWS Systems Manager Parameter Store](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-parameter-store.html), and read them at deploy or run time so one artifact serves every environment. 

1.  **Define infrastructure as code:** Provision resources with [AWS CloudFormation](https://aws.amazon.com/cloudformation/) or the [AWS CDK](https://aws.amazon.com/cdk/), and deploy infrastructure changes through the same pipeline as application changes. 

1.  **Deploy progressively with rollback:** Release changes to a subset first, monitor the effect, and roll back automatically when issues appear. Use [AWS CodeDeploy](https://aws.amazon.com/codedeploy/) for Amazon EC2 and AWS Lambda, and [Amazon ECS blue/green service deployments](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/deployment-type-blue-green.html) for containers. [Stage rollback in AWS CodePipeline](https://docs.aws.amazon.com/codepipeline/latest/userguide/stage-rollback.html) reverses a failed stage. 

1.  **Monitor and audit deployments:** Track deployments, performance, and infrastructure changes with [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) and [AWS CloudTrail](https://aws.amazon.com/cloudtrail/), and use the records to confirm adherence to your security and compliance requirements. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [SEC11-BP03 Automate testing throughout the development and release lifecycle](sec11-bp03.md) 
+  [SEC11-BP06 Centralize services for packages and dependencies](sec11-bp06.md) 
+  [SEC11-BP08 Regularly assess security properties of the pipelines](sec11-bp08.md) 

 **Related documents:** 
+  [Organizing your AWS environment using multiple accounts](https://docs.aws.amazon.com/whitepapers/latest/organizing-your-aws-environment/organizing-your-aws-environment.html) 
+  [DevOps Guidance: DL.CI.2 Trigger builds automatically upon source code modifications](https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/dl.ci.2-trigger-builds-automatically-upon-source-code-modifications.html) 
+  [Automating safe, hands-off deployments](https://builder.aws.com/content/3ErTKQOTKc5NIw031UePBPxTQ6I/automating-safe-hands-off-deployments) 
+  [Amazon ECS blue/green deployments](https://docs.aws.amazon.com/AmazonECS/latest/developerguide/deployment-type-blue-green.html) 
+  [Accelerate deployments on AWS with effective governance](https://aws.amazon.com/blogs/architecture/accelerate-deployments-on-aws-with-effective-governance/) 
+  [Code signing using AWS Certificate Manager Private CA and AWS KMS asymmetric keys](https://aws.amazon.com/blogs/security/code-signing-aws-certificate-manager-private-ca-aws-key-management-service-asymmetric-keys/) 
+  [Code signing, a trust and integrity control for AWS Lambda](https://aws.amazon.com/blogs/aws/new-code-signing-a-trust-and-integrity-control-for-aws-lambda/) 

 **Related videos:** 
+  [AWS re:Invent 2025 - Build safe and resilient deployment pipelines for Amazon ECS (CNS353)](https://www.youtube.com/watch?v=Z_21fo3BmEc) 
+  [AWS re:Invent 2025 - Large-scale software deployments: Inside Amazon S3's release pipeline (STG352)](https://www.youtube.com/watch?v=ve7vWTrfe40) 

 **Related services:** 
+  [AWS CodePipeline](https://aws.amazon.com/codepipeline/) 
+  [AWS Signer](https://docs.aws.amazon.com/signer/latest/developerguide/Welcome.html) 
+  [AWS Systems Manager Parameter Store](https://docs.aws.amazon.com/systems-manager/latest/userguide/systems-manager-parameter-store.html) 