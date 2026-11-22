

# SEC11-BP06 Centralize services for packages and dependencies

 Every third-party package brings its own vulnerabilities, sub-dependencies, and risk of disappearing or being tampered with. Route dependencies through a central, controlled source so you can scan them, approve them, and keep building when public repositories are unavailable. 

 **Desired outcome:** 
+  Your organization has visibility into every third-party dependency across its applications. 
+  Your teams add new dependencies deliberately, weighing security and maintenance before adopting them. 
+  Your applications keep building and deploying even when an upstream public repository is unavailable. 
+  You have an approval process for new dependencies that matches your organization's risk tolerance. 

 **Common anti-patterns:** 
+  Developers pull dependencies straight from public repositories, tying their ability to build to the availability and integrity of those repositories. 
+  Teams stand up a central repository without deciding which security controls it needs or how to configure them. 
+  Developers add dependencies with no review of security, stability, size, sub-dependencies, or license. 
+  The approval process is so slow or strict that developers bypass the central repository to get what they need. 
+  No one reviews dependencies over time to update outdated ones or remove those no longer used. 

 **Benefits of establishing this best practice:** 
+  Your software supply chain is protected from harmful or tampered packages, and package usage is visible. 
+  Package distribution stays efficient while security controls remain in place. 
+  A newly disclosed vulnerability can be traced to every application that uses the affected component. 

 **Level of risk exposed if this best practice is not established:** Medium 

## Implementation guidance
<a name="implementation-guidance"></a>

 A dependency can carry a known vulnerability, pull in sub-dependencies you never chose, or ship under a license that conflicts with your obligations. It can also be replaced by a harmful version through a typosquatting or account-takeover attack. Pulling packages directly from public repositories ties your build to infrastructure you do not control. An upstream service disruption or a withdrawn package can stop your delivery. 

 A central package repository fetches, scans, and caches packages, so your builds pull from it instead of public ones. This acts a central place to apply vulnerability scanning, enforce license policy, and control which upstream sources you trust. On AWS, [Amazon CodeArtifact](https://aws.amazon.com/codeartifact/) provides this managed repository. Its package origin control helps prevent dependency substitution attacks, where someone publishes a harmful package under a name your internal code looks for. 

 If approval is too slow or too strict, developers bypass the repository and the uncontrolled sourcing returns. If it is too loose, the repository does not add enough protection. Set a clear, fast policy by defining acceptance criteria (security history, maintenance status, code size, sub-dependencies, license) and providing a quick path for common cases. 

 A package that was safe at adoption can have a vulnerability disclosed against it later. Monitor dependencies continuously for newly disclosed vulnerabilities, use of unapproved sources, and prohibited licenses. [Amazon Inspector](https://aws.amazon.com/inspector/) integrates with your pipeline to detect affected versions as advisories are published, and open-source tools such as [OWASP Dependency-Check](https://owasp.org/projects/dependency-check) can supplement it. [Amazon Inspector Code Security](https://docs.aws.amazon.com/inspector/latest/user/code-security-assessments.html) scans your source repositories for vulnerable dependencies, first-party code, and infrastructure as code, so you catch issues before a build starts. Amazon Inspector can also [export a software bill of materials](https://docs.aws.amazon.com/inspector/latest/user/sbom-export.html), which is the inventory that tells you which applications use an affected package. Pair monitoring with a standing review that updates outdated dependencies and removes unused ones, and consider frameworks such as [Supply chain Levels for Software Artifacts (SLSA)](https://slsa.dev/) to set a target maturity for supply chain integrity. 

 Plan for a [compromised third-party package](https://aws-samples.github.io/threat-technique-catalog-for-aws/Techniques/T1648.A002.html) already in your applications. The code runs with the permissions of the workload that imported it, so removing the package is only the first step. Rotate every credential and secret that code could reach. This includes the role credentials the workload runs with, values in environment variables, and secrets in AWS Secrets Manager or AWS Systems Manager Parameter Store. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Define a dependency policy:** Set the criteria for accepting a package, including security history, maintenance status, size, sub-dependencies, and license. Document the approval path and keep it fast enough that teams do not bypass it. 

1.  **Stand up a central package repository:** Configure [Amazon CodeArtifact](https://aws.amazon.com/codeartifact/) or your organization's approved repository as the single source for dependencies. Apply access controls, enable package origin control, and point developer machines and pipelines at it. 

1.  **Scan incoming packages:** Enable vulnerability scanning on packages entering the repository, and enforce license and policy checks before a package becomes available to teams. 

1.  **Add automated checks to the pipeline:** [Integrate Amazon Inspector scans into your CI/CD pipeline](https://docs.aws.amazon.com/inspector/latest/user/scanning-cicd.html), and fail or flag builds that pull affected versions or violate policy. Apply a [Code Security](https://docs.aws.amazon.com/inspector/latest/user/code-security-assessments.html) scan configuration to the repositories themselves, so you catch a vulnerable dependency before a build starts. 

1.  **Monitor existing dependencies continuously:** Configure alerts for newly disclosed vulnerabilities in dependencies already in use, and establish a regular cadence to update outdated packages and remove unused ones. Decide in advance which credentials and secrets you rotate when a package already in use is found to be harmful. 

1.  **Train developers on dependency risk:** Educate teams on supply chain threats and on how to evaluate and select packages responsibly, so the policy is applied with understanding rather than resistance. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [SEC11-BP03 Automate testing throughout the development and release lifecycle](sec11-bp03.md) 
+  [SEC11-BP07 Deploy software programmatically](sec11-bp07.md) 
+  [SEC11-BP08 Regularly assess security properties of the pipelines](sec11-bp08.md) 

 **Related documents:** 
+  [Amazon Inspector Code Security](https://docs.aws.amazon.com/inspector/latest/user/code-security-assessments.html) 
+  [Integrating Amazon Inspector scans into your CI/CD pipeline](https://docs.aws.amazon.com/inspector/latest/user/scanning-cicd.html) 
+  [Exporting SBOMs with Amazon Inspector](https://docs.aws.amazon.com/inspector/latest/user/sbom-export.html) 
+  [DevOps Guidance: DL.CS.2 Sign code artifacts after each build](https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/dl.cs.2-sign-code-artifacts-after-each-build.html) 
+  [Supply chain Levels for Software Artifacts (SLSA)](https://slsa.dev/) 

 **Related videos:** 
+  [AWS re:Inforce 2025 - From compute to code: Expanding vulnerability scanning across the SDLC (APS203)](https://www.youtube.com/watch?v=2SSWyuWivIs) 
+  [AWS re:Inforce 2025 - Scale vulnerability management using Amazon Inspector (TDR305)](https://www.youtube.com/watch?v=ju5Uyb8ve6g) 

 **Related examples:** 
+  [Tighten your package security with the CodeArtifact package origin control toolkit](https://aws.amazon.com/blogs/devops/tighten-your-package-security-with-codeartifact-package-origin-control-toolkit/) 
+  [Multi-Region package publishing pipeline](https://github.com/aws-samples/multi-region-python-package-publishing-pipeline) 

 **Related tools:** 
+  [Amazon CodeArtifact](https://aws.amazon.com/codeartifact/) 
+  [Amazon Inspector](https://aws.amazon.com/inspector/) 
+  [OWASP Dependency-Check](https://owasp.org/projects/dependency-check) 