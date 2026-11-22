

# SEC06-BP01 Perform vulnerability management

 Software accumulates known vulnerabilities as researchers find flaws in operating systems, libraries, and dependencies. Vulnerability management is the ongoing practice of finding these weaknesses, judging their risk to your workload, and remediating them before they can be used for unauthorized access. Prioritize fixes by data sensitivity and the business impact of the affected component. 

 **Desired outcome:** 
+  You scan for vulnerabilities across the development pipeline and running environments, not production alone. 
+  You prioritize remediation using workload context such as data sensitivity, exposure, and business impact, rather than treating every finding equally. 
+  You favor immutable infrastructure, replacing resources from updated images instead of patching in place, and you document any exceptions with approved compensating controls. 
+  You maintain a remediation backlog with defined timelines, and you review aging findings and approved exceptions on a regular cadence. 

 **Common anti-patterns:** 
+  Teams treat all vulnerabilities with equal priority, ignoring the workload context that determines real risk. 
+  Scanning runs only in production, so vulnerabilities reach live systems before detection. 
+  Workload teams bypass organizational vulnerability management tools and build parallel, unmanaged solutions. 
+  Teams delay patches without a risk assessment, or apply emergency patches with no testing in a non-production environment. 
+  Teams ignore application dependencies when assessing a finding, so the true scope of impact stays hidden. 

 **Benefits of establishing this best practice:** 
+  Remediation effort goes to the vulnerabilities that matter most to your workload, because priority reflects data sensitivity and exposure. 
+  Vulnerabilities are caught earlier, because scanning happens across the pipeline rather than only in production. 
+  Replacing resources from updated images reduces configuration drift and shrinks the window available for unauthorized use. 
+  Regular exception reviews keep the number of unpatched, long-lived components shrinking over time. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 Vulnerability management in the cloud splits into two models depending on whether a resource is immutable. With immutable infrastructure, you never patch a running system. You build a new image with the fix, deploy fresh resources, and retire the old ones. This removes a whole class of problems, including configuration drift, failed in-place patches, and malware that survives a patch, because every deployment starts from a known, clean state. Stateless components such as web servers, application servers, and API layers fit this model well. 

 Not every component can be immutable. Stateful systems, licensed appliances, and long-lived instances often need in-place patching. For these, continuous scanning and a disciplined patch process matter more, because the resource carries whatever state and drift it has accumulated. [Amazon Inspector](https://docs.aws.amazon.com/inspector/latest/user/what-is-inspector.html) gives continuous visibility into known CVEs across instances, container images, and functions, and [AWS Systems Manager Patch Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/patch-manager.html) applies patches against a defined baseline. In-place patching preserves state. Drift also returns, and a patch can break the application. Test patches in a non-production environment before they reach production. 

 A severity score describes a vulnerability in isolation. The actual risk to your workload depends on data classification, exposure, and the dependency graph. A critical CVE in a component with no network exposure and no sensitive data can matter less than a medium finding on an internet-facing service that processes regulated data. Your workload team is best placed to make this call. [AWS Security Hub CSPM](https://docs.aws.amazon.com/securityhub/latest/userguide/) automates part of it by correlating vulnerability findings with network reachability and resource relationships to produce exposure findings that show which vulnerabilities are reachable in your environment. 

 To catch issues before they ship, scan infrastructure code, container images, and application dependencies inside the deployment pipeline. At the same time, automated gates can stop a build when a critical finding appears. [Amazon Inspector code security](https://docs.aws.amazon.com/inspector/latest/user/code-security-assessments.html) extends this coverage into source code repositories with SAST, SCA, and IaC scanning through integrations with GitHub and GitLab, so you discover vulnerabilities in application code and infrastructure templates alongside runtime findings. Most organizations run shared vulnerability management services and baselines, so integrate with those services and feed findings from services such as [Amazon ECR image scanning](https://docs.aws.amazon.com/AmazonECR/latest/userguide/image-scanning.html) and Amazon Inspector into a shared view such as [AWS Security Hub CSPM](https://docs.aws.amazon.com/securityhub/latest/userguide/). 

 A component that cannot yet move to an immutable pattern gets an approved exception with a compensating control. Unreviewed exceptions become long-lived paths available for unauthorized access. Document exceptions, review them on a schedule, and eliminate them over time through architectural improvements. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Document your workload's vulnerability context:** Identify critical components, data classification levels, exposure, and regulatory requirements. Use this record to set remediation priorities and to justify any exceptions to organizational standards. Note the components that handle sensitive data or fall under compliance requirements, because these often need additional controls or more frequent assessment. 

1.  **Adopt immutable patterns for stateless components:** Configure your CI/CD pipeline to build new AMIs or container images with [EC2 Image Builder](https://docs.aws.amazon.com/imagebuilder/latest/userguide/what-is-image-builder.html) when updates are needed, and deploy fresh resources rather than modifying running ones. Test new images in a staging environment before you promote them to production. 

1.  **Scan continuously across environments:** Configure [Amazon Inspector](https://docs.aws.amazon.com/inspector/latest/user/what-is-inspector.html) to match your workload's architecture, and aggregate findings in [AWS Security Hub CSPM](https://docs.aws.amazon.com/securityhub/latest/userguide/). Create insights that focus on your workload's components, and set severity thresholds from your risk assessment. 

1.  **Add scanning gates to the pipeline:** Run pre-deployment scans of infrastructure code, container images with [Amazon ECR image scanning](https://docs.aws.amazon.com/AmazonECR/latest/userguide/image-scanning.html), and application dependencies. Use [Amazon Inspector code security](https://docs.aws.amazon.com/inspector/latest/user/code-security-assessments.html) to scan application source code and IaC templates directly in your source repository. Block deployment on critical findings and allow warnings for lower-severity issues, according to your risk tolerance. 

1.  **Patch non-immutable components:** Configure [AWS Systems Manager Patch Manager](https://docs.aws.amazon.com/systems-manager/latest/userguide/patch-manager.html) to apply patches against your organizational and workload baselines. Test emergency patches in a non-production environment before they reach production. 

1.  **Manage a remediation backlog and review exceptions:** Prioritize fixes by risk level and operational impact, and track aging findings against your remediation timelines. Review the exception inventory at least quarterly, and remove exceptions through architectural improvements where you can. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [SEC06-BP05 Automate compute protection](sec06-bp05.md) 
+  [SEC06-BP02 Provision compute from hardened images](sec06-bp02.md) 
+  [SEC06-BP03 Reduce manual management and interactive access](sec06-bp03.md) 
+  [SEC06-BP04 Validate software integrity](sec06-bp04.md) 

 **Related documents:** 
+  [What is Vulnerability Management?](https://aws.amazon.com/what-is/vulnerability-management/) 

 **Related videos:** 
+  [AWS re:Invent 2025 - Staying Ahead: Smart Strategies for Effective Vulnerability Management (SEC316)](https://www.youtube.com/watch?v=XnwrWIzSW8I) 
+  [Agentless Scanning for EC2 Instances with Amazon Inspector](https://www.youtube.com/watch?v=Aedp1LIjL6w) 

 **Related examples:** 
+  [Shifting vulnerability detection left with Amazon Inspector code security capabilities](https://aws.amazon.com/blogs/security/shifting-vulnerability-detection-left-with-amazon-inspector-code-security-capabilities/) 
+  [Transition to using Instance Metadata Service Version 2](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/instance-metadata-transition-to-version-2.html) 
+  [AWS Compliance Programs](https://aws.amazon.com/compliance/programs/) 

 **Related services:** 
+  [Amazon Inspector](https://aws.amazon.com/inspector/) 
+  [EC2 Image Builder](https://aws.amazon.com/image-builder/) 
+  [AWS Systems Manager](https://aws.amazon.com/systems-manager/) 
+  [Amazon ECR](https://aws.amazon.com/ecr/) 