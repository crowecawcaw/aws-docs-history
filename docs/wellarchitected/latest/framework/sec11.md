

# Application security

 Application security is the practice of building security properties into software as it is designed, written, and released, and then confirming those properties hold before the software reaches production. When security is a design input rather than a final inspection, teams find and fix risks early, when remediation costs the least. 

 The discipline spans people, process, and the mechanism that ships the code. Teams make sound security decisions about the software they build when they hold both the skills and the authority to do so. Consistent coding standards, peer review, and automated testing keep known defect classes out of the codebase. The third-party components a team depends on and the pipeline that assembles and deploys the result each carry their own risk, so both need deliberate control. 

 This capability covers embedding security throughout the software lifecycle: team ownership and skills, secure coding and code review, automated and manual testing, supply chain and dependency control, and secured programmatic deployment. It does not cover the identity, network, data protection, or detection controls that other capabilities address. 


|  SEC11: How do you incorporate and validate the security properties of applications throughout the design, development, and deployment lifecycle?  | 
| --- | 
|  [SEC11-BP01 Embed security ownership in workload teams, and train for application security](sec11-bp01.md)  | 
|  [SEC11-BP02 Follow established secure coding guidelines](sec11-bp02.md)  | 
|  [SEC11-BP03 Automate testing throughout the development and release lifecycle](sec11-bp03.md)  | 
|  [SEC11-BP04 Perform regular penetration testing](sec11-bp04.md)  | 
|  [SEC11-BP05 Conduct code reviews](sec11-bp05.md)  | 
|  [SEC11-BP06 Centralize services for packages and dependencies](sec11-bp06.md)  | 
|  [SEC11-BP07 Deploy software programmatically](sec11-bp07.md)  | 
|  [SEC11-BP08 Regularly assess security properties of the pipelines](sec11-bp08.md)  | 

## Capability intent
<a name="sec11-intent"></a>
+  The teams that build software own the security decisions for it, backed by training in threat modeling and secure coding and a clear line for escalating high-risk or novel cases. 
+  Recognized secure coding standards are tailored to the technology stack and enforced through code review and automated analysis, so common vulnerability classes are prevented at the source. 
+  Security testing runs automatically across the repository, build, and pipeline stages, and skilled penetration testing exercises the flaws that automation cannot reach, with findings tracked to remediation before release. 
+  Third-party dependencies flow through a controlled source that scans, approves, and caches them, so supply chain risk is visible and builds do not depend on public repositories. 
+  Software is deployed through automated pipelines that promote one signed artifact unchanged across environments and remove persistent human access to production. 
+  Pipelines are treated as high-value workloads whose security tests cannot be bypassed and whose permissions are least privilege and regularly reassessed. 

## Common issues to watch for
<a name="sec11-issues"></a>
+  Security is treated as a gate at the end of development, so findings arrive after the design is set and cost far more to fix than they would have earlier. 
+  Teams are told to own security but lack the training to recognize a flaw or the authority to delay a release, so they ship the flaw in good faith. 
+  Coding standards are too generic or too complex to apply, or they are never enforced by tooling, so they drift out of date and teams ignore them. 
+  Automated testing runs only right before release and reports findings with no remediation guidance, so the same issues recur across teams and go unactioned. 
+  Dependencies are pulled directly from public repositories with no review, tying build integrity and availability to infrastructure the organization does not control. 
+  Deployments are manual and pipelines are weakly secured, so the version tested cannot be proven to match the version released and the pipeline itself becomes a high-value target that can disable its own controls. 