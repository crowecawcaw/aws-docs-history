

# OPS03-BP05 Design for efficient patch management

 Patching keeps systems secure, supported, and current with features, but patching manually does not scale and is error-prone. Treat patch management as a designed process: decide what to patch, when, and how it moves across environments, and then automate the mechanics. Rebuild systems from a known good image where you can, and use controlled in-place patching where you cannot. 

 **Desired outcome:** 
+  Your machine and container images are patched, updated, and ready to launch from a known good state. 
+  You can track the patch status of all deployed images and know your compliance position. 
+  You have a process to report current patch status against your compliance requirements. 
+  You know about planned lifecycle events in advance and plan patching around them. 

 **Common anti-patterns:** 
+  A team is told to apply every security patch within two hours, and the rushed patches cause incidentss from application incompatibility. 
+  An unpatched library carries a known vulnerability that an unauthorized user can use to reach the workload. 
+  A team patches developer environments automatically with no notice, and the changes break the developers' work. 
+  A team never patches commercial software on a long-lived instance, then finds the vendor will not support the outdated version during an incident. 
+  A team learns of a zero-day vulnerability and has to patch every environment manually because nothing is automated. 
+  A team ignores planned lifecycle events, loses the lead time to prepare, and faces emergency changes and unexpected downtime. 

 **Benefits of establishing this best practice:** 
+  A defined patch process lets you scale patching and report on patch levels across environments. 
+  You gain assurance and visibility that known fixes are in place. 
+  You adopt new features and capabilities and remove known issues quickly. 
+  Automation lowers the effort to deploy patches and reduces manual errors. 

 **Level of risk exposed if this best practice is not established:** Medium 

## Implementation guidance
<a name="implementation-guidance"></a>

 Immutable infrastructure replaces a running system with a freshly built, patched image, so the fleet never diverges from a known good state. In-place patching modifies systems where they run. With immutable patching, you roll back by redeploying the previous image. Your systems must be rebuildable with externalized state. We recommend immutable patching wherever the workload supports it, and in-place patching when a system cannot be rebuilt. 

 Apply a patch only when it supports an operational or business outcome, and test it in a safe environment before production. Define your patch criteria and distribution method up front: which patches qualify, how they move across environments, and how quickly. Urgent patches then have a fast path without bypassing testing. 

 Planned lifecycle events also require patching: mandatory version updates, runtime deprecations, and end-of-support dates. Missing these events turns a scheduled update into an emergency change. [AWS Health](https://aws.amazon.com/premiumsupport/technology/aws-health/) reports planned lifecycle events and other action-required events for your resources; major events are announced at least six months ahead. Review these notifications as part of your patch planning. 

 Image pipelines make immutable patching repeatable. [Amazon EC2 Image Builder](https://aws.amazon.com/image-builder/) builds and updates [Amazon Machine Images](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AMIs.html) through an image pipeline and container images through a container image pipeline. For containers, [Amazon Elastic Container Registry](https://docs.aws.amazon.com/AmazonECR/latest/userguide/what-is-ecr.html) stores updated images for use with your existing deployment pipeline. For serverless code, [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/configuration-versions.html) supports function versioning and [custom runtimes and additional libraries](https://docs.aws.amazon.com/lambda/latest/dg/runtimes-custom.html), so you can remove vulnerable dependencies. 

 [Amazon Inspector](https://aws.amazon.com/inspector/) tells you what needs patching. It continuously scans your Amazon EC2 instances, container images, and Lambda functions for known [Common Vulnerabilities and Exposures (CVEs)](https://docs.aws.amazon.com/inspector/latest/user/vulnerability-search.html). You can [integrate it into your pipelines and source repositories](https://docs.aws.amazon.com/inspector/latest/user/code-security-assessments-create-integration.html) — such as AWS CodePipeline, GitHub, or GitLab — so vulnerabilities surface before an image ships. 

 When you must patch in place, automate it. [AWS Systems Manager Patch Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/patch-manager.html) patches managed instances against a patch baseline, and [Systems Manager Maintenance Windows](https://docs.aws.amazon.com/systems-manager/latest/userguide/maintenance-windows.html) schedule that work for times that limit disruption. You can then respond to previously-unknown issues across every environment without patching each system manually. 

 When a patch or platform upgrade changes behavior in several subsystems, release it in stages and hold each stage long enough to observe sustained production load. Some defects take days to appear. See [OPS04-BP01 Employ and test safe deployment strategies](ops04-bp01.md) for staged rollout and bake time. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Choose immutable or in-place patching per workload:** For workloads you can rebuild, patch by producing a new image and redeploying. Reserve in-place patching for systems that cannot be rebuilt. Document which model each workload uses so the patch process is predictable. 

1.  **Build image pipelines for immutable patching:** Use [Amazon EC2 Image Builder](https://docs.aws.amazon.com/imagebuilder/latest/userguide/what-is-image-builder.html) to create an [image pipeline](https://docs.aws.amazon.com/imagebuilder/latest/userguide/start-build-image-pipeline.html) for machine images and a [container image pipeline](https://docs.aws.amazon.com/imagebuilder/latest/userguide/start-build-container-pipeline.html) for containers. Define the pipeline schedule, choose a recipe with a base image and build components, set the target registry, and review the configuration before you run it. Revisit recipes regularly so base images and components stay current. 

1.  **Automate in-place patching where rebuilds are not possible:** Create a patch baseline in [AWS Systems Manager Patch Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/patch-manager.html), select a patching method, and schedule it with [Maintenance Windows](https://docs.aws.amazon.com/systems-manager/latest/userguide/maintenance-windows.html). Enable compliance scanning so you can report on patch levels. 

1.  **Test patches before production:** Apply patches in a safe environment and verify application compatibility before you promote them. Notify the owners of shared or developer environments before patching, so changes do not disrupt their work. 

1.  **Track compliance and monitor lifecycle events:** Use Patch Manager [compliance reports](https://docs.aws.amazon.com/systems-manager/latest/userguide/patch-manager-compliance-reports.html) to report patch status against your requirements, and review [AWS Health](https://aws.amazon.com/premiumsupport/technology/aws-health/) for planned lifecycle events that require action. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [OPS03-BP01 Adopt a configuration, build, and release pipeline](ops03-bp01.md) 
+  [OPS03-BP04 Fully automate integration and deployment](ops03-bp04.md) 
+  [OPS04-BP01 Employ and test safe deployment strategies](ops04-bp01.md) 
+  [OPS04-BP02 Automate testing and rollback](ops04-bp02.md) 

 **Related documents:** 
+  [What is EC2 Image Builder?](https://docs.aws.amazon.com/imagebuilder/latest/userguide/what-is-image-builder.html) 
+  [Create an image pipeline using the EC2 Image Builder console](https://docs.aws.amazon.com/imagebuilder/latest/userguide/start-build-image-pipeline.html) 
+  [Create a container image pipeline](https://docs.aws.amazon.com/imagebuilder/latest/userguide/start-build-container-pipeline.html) 
+  [AWS Systems Manager Patch Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/patch-manager.html) 
+  [Working with Patch Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/patch-manager-console.html) 
+  [Working with patch compliance reports](https://docs.aws.amazon.com/systems-manager/latest/userguide/patch-manager-compliance-reports.html) 
+  [Amazon Machine Images (AMIs)](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/AMIs.html) 
+  [What is Amazon Elastic Container Registry?](https://docs.aws.amazon.com/AmazonECR/latest/userguide/what-is-ecr.html) 
+  [AWS Lambda runtimes: custom runtimes and additional libraries](https://docs.aws.amazon.com/lambda/latest/dg/runtimes-custom.html) 
+  [AWS Lambda function versions](https://docs.aws.amazon.com/lambda/latest/dg/configuration-versions.html) 
+  [AWS Developer Tools](https://aws.amazon.com/products/developer-tools) 

 **Related examples:** 
+  [AWS Systems Manager Patch Manager tutorials](https://docs.aws.amazon.com/systems-manager/latest/userguide/patch-manager-tutorials.html) 

 **Related services:** 
+  [Amazon EC2 Image Builder](https://aws.amazon.com/image-builder/) 
+  [AWS Systems Manager](https://aws.amazon.com/systems-manager/) 
+  [AWS Health](https://aws.amazon.com/premiumsupport/technology/aws-health/) 
+  [Amazon Elastic Container Registry](https://aws.amazon.com/ecr/) 
+  [AWS Serverless Application Repository](https://aws.amazon.com/serverless/serverlessrepo) 
+  [Amazon Inspector](https://aws.amazon.com/inspector/) 