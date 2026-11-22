

# SEC01-BP05 Automate deployment of standard security controls

 Manually-applied security controls can drift, vary between environments, and are hard to audit. Define controls as code, version them, test them, and deploy them through a pipeline to keep them consistent, reviewable, and repeatable. 

 **Desired outcome:** 
+  Your standard controls are defined as code and committed to a version control system. 
+  Your CI/CD pipelines detect changes and automate testing and deployment across your environments. 
+  Your guardrails catch template misconfigurations before deployment proceeds. 
+  Your workload teams deploy approved configurations through a self-service mechanism. 
+  You have secure backup and recovery for control definitions, scripts, and related data. 

 **Common anti-patterns:** 
+  Teams change standard security controls manually through a console or command line. 
+  A central team defines controls but relies on each workload team to implement them manually. 
+  Workload teams wait on a central security team to deploy workload-level controls on request. 
+  The same individuals develop, test, and deploy control automation with no separation of duties. 

 **Benefits of establishing this best practice:** 
+  Version control makes every change to a control trackable and comparable over time. 
+  Automated testing and deployment increase consistency and reduce repetitive manual work. 
+  Self-service deployment of approved configurations lowers the risk of misconfiguration and misuse. 
+  Teams incorporate security controls earlier in development, where issues cost less to fix. 

 **Level of risk exposed if this best practice is not established:** Medium 

## Implementation guidance
<a name="implementation-guidance"></a>

 Once you separate workloads into multiple accounts, you may encounter a scaling problem. Each environment requires a consistent set of security controls, and applying them manually across many accounts guarantees inconsistency. Many controls are standard across the organization, such as integrating a central identity provider, defining networks and firewalls, and configuring standard locations for storing and analyzing logs. *Infrastructure as code* (IaC) lets you define these standard controls declaratively and apply the same rigor to them that you apply to application code. 

 Declarative definitions provide three useful capabilities that do not exist when performing manual configuration. Storing templates in [AWS CloudFormation](https://aws.amazon.com/cloudformation/) under source control provides a reviewable history of every change. Automated testing with a tool such as [AWS CloudFormation Guard](https://docs.aws.amazon.com/cfn-guard/latest/ug/what-is-guard.html) validates a template against policy before it deploys. Drift detection tells you when a deployed control no longer matches its definition, which is often the first sign of an unauthorized or accidental change. *Static application security testing* (SAST) analyzes templates and code before deployment with tools such as [cfn-lint](https://github.com/aws-cloudformation/cfn-lint), *dynamic application security testing* (DAST) probes running systems for runtime-only flaws, and *software composition analysis* (SCA) finds known vulnerabilities in third-party dependencies. 

 A pipeline built from services such as [AWS CodePipeline](https://aws.amazon.com/codepipeline/), [AWS CodeBuild](https://aws.amazon.com/codebuild/), and [AWS CodeDeploy](https://aws.amazon.com/codedeploy/) automates deployment of these controls. The [Deployments OU guidance](https://docs.aws.amazon.com/whitepapers/latest/organizing-your-aws-environment/advanced-ous.html#deployments-ou) recommends housing your CI/CD capabilities in their own deployment accounts, separated from the workload environments they deploy to, so that unauthorized access in one does not reach the controls that govern the rest. Consider how to separate duties in this architecture. For example, when the same person authors, tests, and deploys a control without an independent check, the pipeline provides no assurance. 

 With [Service Catalog](https://aws.amazon.com/servicecatalog/), a central security team publishes approved templates as *products* that workload teams incorporate into their own deployments, so approved configurations spread without a central bottleneck. [AWS Control Tower](https://aws.amazon.com/controltower/) supplies a set of templates and controls as a starting point, and its [Account Factory](https://docs.aws.amazon.com/controltower/latest/userguide/account-factory.html) lets workload teams create new accounts without waiting on a central approval step. Self-service removes the dependency on a central team while keeping definitions under central governance. 

 Some services provide [declarative policies](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_declarative_policies.html) to control specific security configurations across all AWS accounts in an AWS Organization. After you attach the policy, the configuration persists as the service adds new features or APIs. For example, a declarative policy can be set to [force enabling Block Public Access on all S3 buckets](https://docs.aws.amazon.com/organizations/latest/userguide/orgs_manage_policies_s3_syntax.html) across the AWS Organization, without configuring it in each account. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Store control templates in version control:** Decide how you will store and maintain your control templates in a version control system, so that every change is tracked and reviewable. 

1.  **Build CI/CD pipelines for your templates:** Create pipelines that test and deploy your templates, with checks that catch misconfigurations and confirm templates meet your organization's standards. 

1.  **Integrate SAST and DAST:** Add static analysis of code and IaC templates and dynamic testing of deployed environments into the pipeline, so vulnerabilities are caught before and after deployment. 

1.  **Scan third-party dependencies:** Add software composition analysis to identify known vulnerabilities in external libraries and components your controls and workloads rely on. 

1.  **Publish a catalog of standardized templates:** Build a catalog of approved templates that workload teams use to deploy accounts and services according to your requirements through self-service. 

1.  **Implement secure backup and recovery:** Establish secure backup and recovery for your control configurations, scripts, and related data so you can restore them after loss or corruption. [SEC08-BP03 Automate data at rest protection](sec08-bp03.md) covers how to automate encrypted, recoverable backups. 

1.  **Use declarative policies when available:** Declarative policies allow you to centrally manage and configure select security-related features on AWS services across all accounts in an AWS Organization, without the need to configure that feature for every account. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [SEC01-BP01 Separate workloads using accounts](sec01-bp01.md) 
+  [SEC08-BP03 Automate data at rest protection](sec08-bp03.md) 
+  [OPS03-BP01 Adopt a configuration, build, and release pipeline](ops03-bp01.md) 
+  [REL08-BP05 Deploy changes with automation](rel08-bp05.md) 

 **Related documents:** 
+  [From clickops to governed IaC: CloudFormation drift detection in practice](https://aws.amazon.com/blogs/devops/from-clickops-to-governed-iac-cloudformation-drift-detection-in-practice/) 
+  [Ship infrastructure faster with CloudFormation and CDK pre-deployment validation on every stack operation](https://aws.amazon.com/blogs/devops/ship-infrastructure-faster-with-cloudformation-and-cdk-pre-deployment-validation-on-every-stack-operation/) 

 **Related videos:** 
+  [AWS Summit DC 2022 - Building and governing multi-accounts using AWS Control Tower](https://www.youtube.com/watch?v=agpyuvRv5oo) 

 **Related examples:** 
+  [Strengthen the DevOps pipeline and protect data with AWS Secrets Manager, AWS KMS, and AWS Certificate Manager](https://aws.amazon.com/blogs/security/strengthen-the-devops-pipeline-and-protect-data-with-aws-secrets-manager-aws-kms-and-aws-certificate-manager/) 
+  [Building end-to-end AWS DevSecOps CI/CD pipeline with open source SCA, SAST, and DAST tools](https://aws.amazon.com/blogs/devops/building-end-to-end-aws-devsecops-ci-cd-pipeline-with-open-source-sca-sast-and-dast-tools/) 

 **Related tools:** 
+  [Landing Zone Accelerator on AWS](https://github.com/awslabs/landing-zone-accelerator-on-aws) 