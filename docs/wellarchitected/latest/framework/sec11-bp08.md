

# SEC11-BP08 Regularly assess security properties of the pipelines

 A pipeline holds the permissions to build and deploy your software, which makes it a high-value target. Apply the same security principles to the pipeline that you apply to any workload, with particular attention to separating permissions. Reassess the pipeline's security properties on a schedule. 

 **Desired outcome:** 
+  Your pipelines follow the same security practices as any other workload in your environment. 
+  You prevent the teams that use a pipeline from editing or bypassing the security tests it runs. 
+  Each of your pipelines holds only the permissions needed for its deployments, granted through temporary credentials. 
+  Your safeguards prevent a pipeline from deploying to the wrong environment. 
+  Your pipelines emit state so you can validate the integrity of your build environments. 

 **Common anti-patterns:** 
+  Builders can bypass the security tests in the pipeline. 
+  Deployment pipelines hold overly broad permissions. 
+  Pipelines are not configured to validate their inputs. 
+  No one reviews the permissions attached to the CI/CD infrastructure on a regular basis. 
+  Pipelines use long-lived or hardcoded credentials. 

 **Benefits of establishing this best practice:** 
+  Confidence in the integrity of the software built and deployed through the pipelines increases. 
+  You can stop a deployment when suspicious activity appears. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 Distinguish security *of* the pipeline from security *through* the pipeline. Security through a pipeline refers to the tests, scans, and gates a pipeline runs. If the pipeline itself is weakly secured, an unauthorized user who gains control of it can disable those controls and push whatever they want to production. Treat the pipeline as a workload and give it the same access controls, input validation, and permission review as the applications it deploys. 

 Separation of duties matters most in this aspect of pipeline security. If the team that writes the application can also edit the pipeline's security tests, then a person with that access operating under deadline pressure can weaken a failing check. Configure the pipeline so the people who use it cannot alter or bypass its security stages. 

 Permissions are the other major exposure. A pipeline needs enough access to deploy across environments, so an over-permissioned pipeline comprises a risk. Grant each pipeline only the permissions required by its deployments, and issue them through temporary credentials. Long-lived or hardcoded keys cannot be rotated quickly and are easily exposed. 

 [IAM Access Analyzer policy generation](https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-policy-generation.html) builds least privilege policies from observed activity. Use it for the pipeline's own permissions, and as a pipeline step that checks the permissions of the workload being deployed. Add controls that prevent a pipeline from targeting the wrong environment, and validate pipeline inputs so malformed or harmful input cannot redirect the build. 

 As permissions accumulate, tools change, and new stages get added, review the security properties of your CI/CD infrastructure on a schedule. An [unused access analyzer](https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-create-unused.html) reports which permissions your pipeline roles have not used in a period you set, so the review works from evidence. The [Deployment Pipeline Reference Architecture](https://aws-samples.github.io/aws-deployment-pipeline-reference-architecture/) is a secure, scalable starting point that already reflects these principles. Connect the pipeline to monitoring and alerting so unexpected activity reaches you quickly. [Amazon EventBridge](https://aws.amazon.com/eventbridge/) can route pipeline events to targets such as [AWS Lambda](https://aws.amazon.com/lambda/) or [Amazon Simple Notification Service (Amazon SNS)](https://aws.amazon.com/sns/) so you can investigate and, if needed, stop a deployment. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Start from a secure reference architecture:** Base your pipelines on the [Deployment Pipeline Reference Architecture](https://aws-samples.github.io/aws-deployment-pipeline-reference-architecture/) so security properties are built in rather than added later. 

1.  **Separate permissions so tests cannot be bypassed:** Configure the pipeline so the teams that use it cannot edit or skip its security stages. Keep ownership of the security checks with a function independent of the application teams. 

1.  **Grant least-privilege, temporary credentials:** Use [IAM Access Analyzer policy generation](https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-policy-generation.html) to build IAM policies with least privilege for the pipeline. Issue permissions through temporary credentials rather than long-lived keys. 

1.  **Add environment and input safeguards:** Configure controls that prevent deployment to the wrong environment, and validate pipeline inputs so malformed input cannot alter the build. 

1.  **Integrate monitoring and alerting:** Route pipeline events through [Amazon EventBridge](https://aws.amazon.com/eventbridge/) to targets such as [AWS Lambda](https://aws.amazon.com/lambda/) or [Amazon SNS](https://aws.amazon.com/sns/) so you are notified of abnormal activity and can stop a deployment. 

1.  **Review pipeline security on a cadence:** Reassess the permissions and configuration of your CI/CD infrastructure on a schedule. Use an [unused access analyzer](https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-create-unused.html) to find permissions the pipeline no longer needs, and follow the [security best practices for AWS CodePipeline](https://docs.aws.amazon.com/codepipeline/latest/userguide/security-best-practices.html). 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [SEC11-BP03 Automate testing throughout the development and release lifecycle](sec11-bp03.md) 
+  [SEC11-BP07 Deploy software programmatically](sec11-bp07.md) 
+  [SEC03-BP01 Grant least privilege access in workload components](sec03-bp01.md) 

 **Related documents:** 
+  [Deployment Pipeline Reference Architecture](https://aws-samples.github.io/aws-deployment-pipeline-reference-architecture/) 
+  [IAM Access Analyzer policy generation](https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-policy-generation.html) 
+  [Create an IAM Access Analyzer unused access analyzer](https://docs.aws.amazon.com/IAM/latest/UserGuide/access-analyzer-create-unused.html) 
+  [Monitoring AWS CodePipeline](https://docs.aws.amazon.com/codepipeline/latest/userguide/monitoring.html) 
+  [Security best practices for AWS CodePipeline](https://docs.aws.amazon.com/codepipeline/latest/userguide/security-best-practices.html) 

 **Related videos:** 
+  [AWS re:Invent 2025 - Automating IAM policy validation and analysis using GitHub Actions (SEC341)](https://www.youtube.com/watch?v=77jWcqzlDNM) 
+  [AWS re:Inforce 2025 - Getting to least privilege takes more than CIEM (IAM101)](https://www.youtube.com/watch?v=6wb4qI5tA84) 

 **Related examples:** 
+  [Deployment Pipeline Reference Architecture reference implementations](https://github.com/aws-samples/aws-deployment-pipeline-reference-architecture) 

 **Related services:** 
+  [AWS IAM Access Analyzer](https://docs.aws.amazon.com/IAM/latest/UserGuide/what-is-access-analyzer.html) 
+  [Amazon EventBridge](https://aws.amazon.com/eventbridge/) 