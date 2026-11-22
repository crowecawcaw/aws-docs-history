

# FND04-BP03 Establish standard repositories of shared resources and patterns

 In environments with many collaborating teams, central repositories of shared resources, patterns, and hardened assets let central and security teams deliver reusable and secure components to engineering teams across the organization. This approach improves consistency, strengthens security, builds resilience, speeds up delivery, and spreads best practices across the cloud environment. 

 **Desired outcome:** 
+  You have pre-hardened, security-vetted resources and patterns available to all teams, so deployments start from a secure baseline. 
+  Your engineering teams speed up delivery by using a library of pre-approved, tested, and optimized resources. 
+  Your organization has fewer manual errors in resource provisioning and configuration, improving resilience. 
+  Your teams spend less time on repeated tasks such as setting up basic infrastructure or common security controls. 

 **Common anti-patterns:** 
+  Over-centralizing by trying to control every resource and decision, which creates bottlenecks that slow innovation. 
+  Building shared resources that are too rigid or that miss different use cases across teams or projects. 
+  Failing to version and document shared resources, leading to inconsistencies and making updates or rollbacks hard. 
+  Developing shared resources without input from consuming teams, so the resources do not meet real needs. 
+  Distributing shared resources through one-off processes instead of standard pipelines with shift-left code and artifact scanning and approvals. 
+  Leaving out metrics on the use and effectiveness of shared resources, making it hard to justify the effort or find areas to improve. 

 **Benefits of establishing this best practice:** 
+  Pre-hardened, security-vetted resources and patterns give all deployments a secure baseline. 
+  A library of pre-approved, tested, and optimized resources shortens time from idea to production. 
+  Standard provisioning and configuration cut the chance of manual error. 
+  Teams spend less time on undifferentiated setup such as base infrastructure or standard security controls. 
+  Common infrastructure patterns, security controls, and operational practices apply the same way across teams. 

 **Level of risk exposed if this best practice is not established:** Medium 

## Implementation guidance
<a name="implementation-guidance"></a>

 Without shared standard resources, engineering teams build their own versions of common infrastructure, each with different security settings, patching schedules, and compliance postures. This duplication wastes effort, creates inconsistency, and leaves security gaps where hardened configurations are not applied consistently. A central repository of shared resources and patterns gives teams a pre-approved starting point that carries your organization's security and compliance standards. 

 A single hardened AMI or container image, maintained centrally and published to multiple Regions, removes the need for each team to track vulnerabilities and apply patches on its own. Standard IaC templates for common resource stacks cut the time from project start to deployment and keep security controls consistent. A self-service catalog of approved solutions, driven from reference architectures, lets teams deploy well-understood patterns without waiting for central team approvals. A curated pattern library is itself a preventive compliance control. A team that deploys a vetted pattern cannot produce a non-compliant variant, so the pattern replaces a dedicated pipeline check and saves the team from building the resource from scratch. 

 Central teams build, harden, and maintain a library of approved resources. Engineering teams keep the autonomy to use those resources when they need them. At minimum, set up a shared services account that hosts your central code repository connections, CI/CD automation, and resource sharing infrastructure. Your AWS Organizations structure sets the scope and boundaries of resource sharing, whether across the entire organization, specific organizational units, or individual accounts. 

 Your central code repository is the single source of truth for all shared resources, with changes tracked, reviewed, and approved before deployment. CI/CD pipelines connected to this repository automate testing, scanning, and deployment of resources to target accounts. These pipelines run shift-left security scans, check compliance requirements, and run automated tests before any resource reaches production. Dedicated non-production accounts support realistic testing of shared resources before broad release. Consider canary deployments where new versions go to a subset of accounts first, catching issues before they reach many teams. 

 Reusable networking patterns (standard VPC designs and security group configurations) are high-value because networking misconfigurations are a common source of security incidents. Sharing these patterns across accounts lowers the chance of misconfiguration and keeps deployments consistent. Changes to a widely-used AMI or template can affect the entire organization without thorough testing. Let engineering team feedback guide which resources to centralize first, and run regular audits of shared resource use to identify low adoption and potential security risks. 

 Over-centralization is the opposite failure mode. Trying to control every part of resource provisioning creates bottlenecks that defeat the goal. Teams drop overly rigid or poorly documented resources and build their own alternatives. Make the secure, compliant path the path of least resistance. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Set up AWS Organizations and a multi-account environment:** Consider using [AWS Control Tower](https://docs.aws.amazon.com/controltower/latest/userguide/planning-your-deployment.html) to set up controls and a standard account creation process. With AWS Control Tower, you can deploy a full landing zone or use the Controls-Only experience to adopt managed controls without a full deployment. 

1.  **Create a centralized code repository:** Set up a central code repository using your approved version control system to share reusable assets and patterns with engineering teams. Consider using [AWS CodeConnections](https://docs.aws.amazon.com/dtconsole/latest/userguide/welcome-connections-how-it-works.html) to connect AWS resources to the central repository. 

1.  **Create CI/CD deployment automation pipelines:** Set up CI/CD pipelines in a shared services AWS account connected to your central code repository using [AWS CodePipeline](https://docs.aws.amazon.com/codepipeline/latest/userguide/welcome-what-can-I-do.html). Configure pipeline stages for source retrieval, security scanning, testing, approval, and deployment. 

1.  **Establish a secure artifact repository for third-party dependencies:** Deploy [AWS CodeArtifact](https://docs.aws.amazon.com/codeartifact/latest/ug/getting-started.html) early in your implementation to provide a private repository for approved third-party libraries. Configure CodeArtifact to pull from public repositories such as npm, Maven Central, or PyPI, and require security scanning and approval before packages are available to teams. This repository supports the steps that follow, because third-party dependencies are needed when you build hardened AMIs, container images, and IaC templates. 

1.  **Build a self-service catalog:** Use [Service Catalog](https://docs.aws.amazon.com/servicecatalog/latest/adminguide/getstarted.html) to create portfolios and products for common shared resources. Start with common application stacks such as serverless architectures, n-tier applications, and containerized environments. 

1.  **Develop standardized IaC templates:** Develop standard CloudFormation templates (or other IaC frameworks) for common resources following [CloudFormation best practices](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/best-practices.html). Validate templates against [CloudFormation Guard](https://docs.aws.amazon.com/cfn-guard/latest/ug/what-is-guard.html) policy rules. 

1.  **Create hardened AMIs and container images:** Create hardened AMIs using [EC2 Image Builder](https://docs.aws.amazon.com/imagebuilder/latest/userguide/what-is-image-builder.html) and [share them](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/share-amis-with-organizations-and-OUs.html) with your organizational units. Configure private [Amazon ECR](https://aws.amazon.com/ecr/) repositories for container images and [apply repository policies](https://docs.aws.amazon.com/AmazonECR/latest/userguide/repository-policies.html) with [cross-Region replication](https://docs.aws.amazon.com/AmazonECR/latest/userguide/replication.html). For serverless components, consider creating shared [Lambda layers](https://docs.aws.amazon.com/lambda/latest/dg/chapter-layers.html) with common dependencies. 

1.  **Configure cross-account resource sharing:** [Set up AWS Resource Access Manager (RAM)](https://docs.aws.amazon.com/ram/latest/userguide/getting-started-sharing.html) and configure resource sharing across accounts. Review the list of [shareable AWS resources](https://docs.aws.amazon.com/ram/latest/userguide/shareable.html) and prioritize based on feedback from engineering teams. Consider using [AWS CloudFormation StackSets](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/what-is-cfnstacksets.html) to deploy shared resources consistently across multiple accounts. 

1.  **Create standardized networking patterns:** Create [standard VPC designs](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-examples-intro.html) and security group configurations so teams inherit consistent network baselines across accounts. 

1.  **Share operational runbooks:** Use [AWS Systems Manager](https://aws.amazon.com/systems-manager/) to [create automations and runbooks](https://docs.aws.amazon.com/systems-manager/latest/userguide/automation-documents.html) and share them across accounts so teams inherit a consistent operational baseline. 

1.  **Establish a feedback and contribution process:** Create a process for teams to give input on shared resources and contribute improvements. Use source control features to support issue creation and accept contributions where it fits. Hold regular review sessions with engineering teams (at minimum quarterly) to discuss adoption metrics, pain points, and priorities for new resources. \#\# Resources 

 **Related best practices:** 
+  [FND01-BP01 Establish management account and organizational structure](fnd01-bp01.md) 
+  [FND01-BP03 Establish boundaries and scopes for your environments](fnd01-bp03.md) 

 **Related documents:** 
+  [Managing Catalogs](https://docs.aws.amazon.com/servicecatalog/latest/adminguide/catalogs.html) 
+  [EC2 Image Builder](https://aws.amazon.com/image-builder/) 
+  [CloudFormation best practices](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/best-practices.html) 
+  [Amazon ECR private repositories](https://docs.aws.amazon.com/AmazonECR/latest/userguide/Repositories.html) 
+  [Creating your own runbooks](https://docs.aws.amazon.com/systems-manager/latest/userguide/automation-documents.html) 
+  [Getting started with CodeArtifact](https://docs.aws.amazon.com/codeartifact/latest/ug/getting-started.html) 
+  [AWS Resource Access Manager User Guide](https://docs.aws.amazon.com/ram/latest/userguide/what-is.html) 

 **Related videos:** 
+  [AWS re:Invent 2023 - Building a multi-account, multi-runtime service-oriented architecture (DOP316)](https://www.youtube.com/watch?v=nSFHlcWj8TY) 
+  [AWS re:Invent 2023 - Centralizing automation to drive business value: A real-world story (COP102)](https://www.youtube.com/watch?v=nII-I7XS-sA) 
+  [AWS re:Invent 2023 - Scale organizational cloud knowledge & improve builder productivity (ARC207)](https://www.youtube.com/watch?v=rcRz6BOyTZY) 