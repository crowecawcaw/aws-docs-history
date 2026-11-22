

# SEC11-BP02 Follow established secure coding guidelines

 Most software vulnerabilities come from a small set of recurring coding mistakes. Established secure coding standards capture how to avoid these mistakes so that each team does not have to rediscover them. Adopt a recognized standard, tailor it to your technology stack, and build it into how your teams write and review code. 

 **Desired outcome:** 
+  Your organization has a defined set of secure coding guidelines that teams apply consistently across projects and application types. 
+  Your guidelines are tailored to your technology stack and cloud services, not a generic checklist. 
+  Your guidelines are built into code reviews and automated scans, so adherence is checked rather than assumed. 
+  You update the guidelines as new threats and language features emerge, treating them as living documents. 

 **Common anti-patterns:** 
+  Teams rely on security tools alone and never establish written coding standards. 
+  Guidelines go stale and no longer address current threats or cloud-specific risks. 
+  Guidelines exist but are applied inconsistently across teams and application types. 
+  Developers receive no training in secure coding for the environments they build on. 
+  Guidelines are so generic or so complex that developers ignore them. 
+  Organizations treat secure coding as a one-time project rather than an ongoing practice. 

 **Benefits of establishing this best practice:** 
+  Applications carry fewer common vulnerabilities because known defect classes are prevented at the source. 
+  Code quality improves and security incidents in operations become less frequent. 
+  New team members write secure code sooner because the standard encodes the organization's collective experience. 
+  Reviews go faster because reviewers check against an agreed baseline instead of personal preference. 

 **Level of risk exposed if this best practice is not established:** Medium 

## Implementation guidance
<a name="implementation-guidance"></a>

 Several recognized standards serve different purposes. The [OWASP Top 10](https://owasp.org/projects/top-ten) and SANS Top 25 rank the most common and impactful weaknesses. The [NIST Secure Software Development Framework (SSDF)](https://csrc.nist.gov/Projects/ssdf) describes practices across the whole lifecycle. [Common Weakness Enumeration (CWE)](https://cwe.mitre.org/) provides a shared vocabulary for classifying flaws. Most organizations combine a ranked list for awareness with a lifecycle framework for process, then map findings to CWE identifiers. 

 A generic standard that ignores your stack flags issues that do not apply and misses actual issues. Tailor the guidelines to the languages, frameworks, and cloud services your teams use. Different application types also need different emphasis. Frontend code needs attention to cross-site scripting and safe communication with backend services. Backend code needs input validation, authentication, and authorization. Data science code needs data privacy and protection against manipulated inputs. Data engineering code needs data integrity and defense against injection in extract, transform, and load processes. 

 The other common failure is complexity. A standard that runs to hundreds of rules with no tooling to enforce them gets read once and forgotten. Keep the guidelines concise, back them with automated checks that give developers feedback where they work, and explain why each rule exists. [Amazon Inspector code security](https://docs.aws.amazon.com/inspector/latest/user/scanning-cicd.html) and tools such as [SonarQube](https://www.sonarsource.com/products/sonarqube/) can check code against many of these rules automatically inside the development environment and the pipeline. 

 As threats and languages change, the guidelines must change with them. Assign ownership, set a review cadence, and give developers a way to propose improvements from what they learn in reviews and incidents. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Select and tailor a standard:** Choose a recognized framework such as [OWASP](https://owasp.org/projects/top-ten), [NIST SSDF](https://csrc.nist.gov/Projects/ssdf), or [CWE](https://cwe.mitre.org/), then adapt it to your languages, frameworks, and cloud services. Involve both security and development teams so the result is practical and accepted. 

1.  **Document and communicate the guidelines:** Write clear, accessible documentation and include the reasoning behind each rule. Announce the guidelines to every team that writes code, and store them where developers already work. 

1.  **Integrate the guidelines into development:** Add them to code review checklists, configure automated analysis in the pipeline, and enable development-environment plugins that give real-time feedback. Use [Amazon Inspector code security](https://docs.aws.amazon.com/inspector/latest/user/scanning-cicd.html) or a comparable tool to check code as it is written and committed. 

1.  **Train developers:** Deliver secure coding training that covers your cloud environment, and maintain a repository of worked examples for each application type. Repeat training as the guidelines and threats evolve. 

1.  **Enforce and measure adherence:** Add automated checks to the pipeline, track metrics on how often teams meet the standard, and audit code for compliance. Use the metrics to find where the guidelines or tooling need work, not only to grade teams. 

1.  **Review and update on a cadence:** Assign an owner, set a regular review, and fold in feedback from developers and new threat information. Retire rules that no longer apply so the standard stays lean. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [SEC11-BP01 Embed security ownership in workload teams, and train for application security](sec11-bp01.md) 
+  [SEC11-BP03 Automate testing throughout the development and release lifecycle](sec11-bp03.md) 
+  [SEC11-BP05 Conduct code reviews](sec11-bp05.md) 

 **Related documents:** 
+  [OWASP Secure Coding Practices quick reference guide](https://owasp.org/projects/secure-coding-practices-quick-reference-guide) 
+  [NIST Secure Software Development Framework (SSDF)](https://csrc.nist.gov/Projects/ssdf) 
+  [Common Weakness Enumeration (CWE)](https://cwe.mitre.org/) 
+  [CWE Top 25 Most Dangerous Software Weaknesses](https://cwe.mitre.org/top25/) 

 **Related examples:** 
+  [Addressing OWASP Top 10 risks](https://builder.aws.com/content/2wCesCbqbOMKs3njdYPNVPDerKg/application-security-addressing-owasp-top-10-risks) 

 **Related tools:** 
+  [Amazon Inspector code security](https://docs.aws.amazon.com/inspector/latest/user/scanning-cicd.html) 
+  [SonarQube](https://www.sonarsource.com/products/sonarqube/) 