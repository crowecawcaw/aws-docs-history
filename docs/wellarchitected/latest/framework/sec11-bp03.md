

# SEC11-BP03 Automate testing throughout the development and release lifecycle

 Manual security checks run late and inconsistently, and they depend on a reviewer being available. Automated tests run the same way every time and give builders feedback while the code is still new. Automate security testing across the development and release lifecycle so issues appear early and known flaws do not reach production. 

 **Desired outcome:** 
+  Your pipelines run security tests automatically at multiple stages, from the code repository through the build. 
+  Your builders receive security feedback during development without waiting for a manual review. 
+  Your tests cover both functional requirements and non-functional properties such as security and reliability. 
+  You track findings to remediation, and each finding links to guidance on how to fix it. 

 **Common anti-patterns:** 
+  Teams run automated security testing only right before a release. 
+  Test cases and results are not shared, so the same issues recur across teams. 
+  Teams automate tests for requirements that change constantly, producing noise instead of signal. 
+  Findings are reported without any guidance on how to remediate them. 

 **Benefits of establishing this best practice:** 
+  Fewer security issues reach production because tests catch them earlier in the lifecycle. 
+  The time between detecting an issue and fixing it shrinks. 
+  Reliance on individual reviewers to judge security properties drops. 
+  Recurring findings across teams become visible and can drive organization-wide fixes. 

 **Level of risk exposed if this best practice is not established:** Medium 

## Implementation guidance
<a name="implementation-guidance"></a>

 Software must satisfy functional requirements (what the application does for the business) and non-functional requirements (how well it does it in terms of reliability, performance, and security). Automated testing checks both of these elements and is the only approach that scales with continuous delivery. 

 Static application security testing (SAST) analyzes source code without running it. It scans large codebases quickly and points to the exact line of a suspected flaw. SAST cannot see issues that only appear at runtime, and it tends to produce false positives that erode trust if left unmanaged. 

 Dynamic application security testing (DAST) exercises the running application and catches behavior static analysis misses, such as configuration flaws or how components interact. It runs later and gives less precise locations. 

 Use both, and place tests at the repository, build, and pipeline stages so you catch each issue where it is cheapest to fix. The [NIST software quality group](https://www.nist.gov/itl/ai/ai-standards-and-guidelines-group) maintains a list of [source code security analyzers](https://www.nist.gov/itl/csd/secure-systems-and-applications/source-code-security-analyzers) if you are evaluating options. 

 A *software bill of materials (SBOM)* is a formal record of the components and dependencies that make up your software. Most applications are mostly third-party code, and you cannot respond to a newly disclosed vulnerability without knowing where the affected component runs. Generating an SBOM during the build feeds vulnerability management and makes supply chain risk visible. 

 Blocking a pipeline on every finding stops delivery and trains teams to disable the check. Notifying without ever blocking lets known-critical issues into your shipped code. Decide per stage and per severity: block on high-confidence critical findings, notify and track the rest. Whatever the policy, route findings into a ticketing system and attach remediation guidance so builders can act on each finding. 

 [Kiro](https://kiro.dev/) offers code recommendations inside the development environment, and its hooks can run a linter or scanner automatically whenever the agent changes a file. [Amazon Inspector code security](https://docs.aws.amazon.com/inspector/latest/user/scanning-cicd.html) integrates with GitHub and GitLab. It performs SAST, SCA, and IaC scanning against source repositories, so vulnerability findings appear in the same workflow where code is written. [Amazon Inspector](https://docs.aws.amazon.com/inspector/latest/user/scanning-resources.html) also scans deployed function code and container images for software vulnerabilities and unintended network exposure. The [Amazon Inspector SBOM generator](https://docs.aws.amazon.com/inspector/latest/user/sbom-generator.html) produces SBOMs in a standard format. A scanner reports what looks wrong. [AWS Continuum](https://docs.aws.amazon.com/securityagent/latest/userguide/what-is.html) goes further and tries to take advantage of what it finds, so you can be more confident about which findings should stop a build. 

 Review the findings your tools produce and look for patterns. Use them to decide what to automate next, what training to run, and which awareness campaign to prioritize. Pair automated testing with periodic reviews by your security team and address their feedback as part of release readiness. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Standardize tooling across the lifecycle:** Adopt consistent development-environment, code review, and pipeline tools that include security testing. This gives every team the same checks and makes findings comparable across workstreams. 

1.  **Add static analysis at commit:** Run SAST as code is written and committed. [Kiro](https://kiro.dev/) hooks can trigger these checks on file save in the developer's environment. For repository-level coverage across application code, dependencies, and IaC templates, connect your source repositories to [Amazon Inspector code security](https://docs.aws.amazon.com/inspector/latest/user/scanning-cicd.html). The open-source [Automated Security Helper](https://github.com/awslabs/automated-security-helper) is one example of a scanning tool you can integrate. 

1.  **Add dynamic and runtime testing:** Complement static analysis with DAST against the running application, and scan deployed artifacts. When you build on serverless functions, use [Amazon Inspector](https://docs.aws.amazon.com/inspector/latest/user/scanning-lambda.html) to scan the function code. 

1.  **Decide where to block and where to notify:** For each stage, choose whether a finding blocks the pipeline or notifies the builder, based on severity and confidence. Document the policy so teams understand why a build stops. 

1.  **Generate an SBOM in the pipeline:** Produce an SBOM during the build with the [Amazon Inspector SBOM generator](https://docs.aws.amazon.com/inspector/latest/user/sbom-generator.html) to feed vulnerability management and expose dependency risk. 

1.  **Track findings and link remediation:** Route findings into a ticketing system, and attach guidance on how to fix each class of issue so builders can act without waiting for a review. 

1.  **Analyze findings to prioritize:** Review results on a cadence to spot systemic issues, then use them to decide the next automation, training topic, or awareness effort. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [SEC11-BP02 Follow established secure coding guidelines](sec11-bp02.md) 
+  [SEC11-BP04 Perform regular penetration testing](sec11-bp04.md) 
+  [SEC11-BP05 Conduct code reviews](sec11-bp05.md) 
+  [SEC11-BP08 Regularly assess security properties of the pipelines](sec11-bp08.md) 

 **Related documents:** 
+  [DevOps Guidance: DL.CR.3 Establish clear completion criteria for code tasks](https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/dl.cr.3-establish-clear-completion-criteria-for-code-tasks.html) 
+  [Source code security analyzers (NIST)](https://www.nist.gov/itl/ai/ai-standards-and-guidelines-group/source-code-security-analyzers) 
+  [Continuous delivery and continuous integration](https://aws.amazon.com/devops/continuous-delivery/) 
+  [Choosing a Well-Architected CI/CD approach](https://aws.amazon.com/blogs/devops/choosing-well-architected-ci-cd-open-source-software-aws-services/) 
+  [Building an end-to-end AWS DevSecOps CI/CD pipeline with open source SCA, SAST, and DAST tools](https://aws.amazon.com/blogs/devops/building-end-to-end-aws-devsecops-ci-cd-pipeline-with-open-source-sca-sast-and-dast-tools/) 
+  [How AWS approaches automating safe, hands-off deployments](https://builder.aws.com/content/3ErTKQOTKc5NIw031UePBPxTQ6I/automating-safe-hands-off-deployments) 

 **Related videos:** 
+  [AWS DevOps Best Practices Well-Architected Framework (re:Invent 2025)](https://aws.amazon.com/video/watch/fe720103fd9/) 

 **Related examples:** 
+  [Automated Security Helper](https://github.com/awslabs/automated-security-helper) 
+  [AWS CodePipeline governance](https://github.com/awslabs/aws-codepipeline-governance) 
+  [OWASP Top 10 – industry awareness for developers](https://owasp.org/projects/top-ten) 

 **Related tools:** 
+  [Kiro](https://kiro.dev/) 
+  [AWS Continuum](https://aws.amazon.com/continuum/) 
+  [Amazon Inspector](https://docs.aws.amazon.com/inspector/latest/user/what-is-inspector.html) 