

# SEC11-BP04 Perform regular penetration testing

 Automated scans and code reviews find known patterns but miss flaws that appear only when someone chains steps together or abuses business logic. Penetration testing places a skilled tester in the role of an unauthorized user to find those gaps and check whether your detective controls work. Run these tests on a regular schedule and after major changes. 

 **Desired outcome:** 
+  You run penetration tests on a regular schedule and after major changes, as part of the software development lifecycle. 
+  Your testers address findings before the software is released. 
+  You analyze findings to identify issues that automation could have caught, and you feed that back into your automated tests. 
+  Your penetration testing process includes a feedback loop that improves guidance to builders and raises software quality. 

 **Common anti-patterns:** 
+  Testers check only for known or prevalent security issues. 
+  Testing excludes the third-party tools and libraries the application depends on. 
+  Testing covers package vulnerabilities but never exercises the application's business logic. 

 **Benefits of establishing this best practice:** 
+  Confidence in the software's security properties increases before release. 
+  Testers identify preferred application patterns, which raises overall software quality. 
+  A feedback loop shows where automation or training could catch issues earlier in the cycle. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 A penetration test runs planned attack scenarios against your software to detect, remediate, and validate security controls. The tester starts with reconnaissance by gathering the current design of the application and its dependencies. From that picture, they build scenarios that aim at unintended access to the environment or protected data. Test when you launch new features and whenever the application changes significantly in function or implementation. 

 Automated scanners recognize known signatures and common misconfigurations, and code reviews catch issues a reader can spot. A skilled tester finds flaws that combine several small weaknesses into one usable weakness. They also find authorization gaps that appear only on unexpected paths through the business logic. A test that only checks package vulnerabilities duplicates what your scanners already do. 

 Scope each test from your [threat model](https://aws.amazon.com/blogs/security/how-to-approach-threat-modeling/) so scenarios are tied to real assets and risks and cover more than the easy-to-reach parts of the application. Include the third-party tools and libraries the application depends on, as attackers do not respect the boundary between your code and imported code. Decide whether internal staff, an external specialist, or both should run the test. External testers bring impartiality and a fresh perspective, while internal testers bring context that speeds up reconnaissance. 

 Test when the application is close to its release state but with time remaining to remediate findings. On AWS, review the [penetration testing policy](https://aws.amazon.com/security/penetration-testing/) first — it defines which activities require prior approval. 

 A manual penetration test takes weeks, so most teams test only their most important applications and everything else waits months between tests. [AWS Continuum penetration tests](https://docs.aws.amazon.com/securityagent/latest/userguide/perform-penetration-test.html) remove testing limits, so you can start a test whenever you need one. The agent reads your source code, infrastructure as code, API definitions, and any threat models, then writes tests that match how the application was built. It takes advantage of each weakness it finds and reports only the ones it can confirm. It also shows how a minor weakness can lead to a serious one and can raise a pull request with a suggested fix. You still choose what to test and when it runs tests. Use the agent to test more applications more often, and keep human-run engagements where compliance requires them. 

 Analyze findings for patterns that reveal a systemic weakness, then add automated tests for recurring issues and update builder training. AWS Continuum penetration tests can enable [automated remediation](https://docs.aws.amazon.com/securityagent/latest/userguide/remediate-finding.html), which proposes a code fix for each finding. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Define a structured scoping process:** Base the scope of each test on your [threat model](https://aws.amazon.com/blogs/security/how-to-approach-threat-modeling/) so scenarios stay tied to real assets and risks. Include third-party dependencies and the application's business logic, not only package vulnerabilities. 

1.  **Choose the point in the lifecycle to test:** Select a stage where the application is close to its release state but enough time remains to remediate findings. Repeat testing after major functional or technical changes. 

1.  **Prepare builders for the findings:** Train your teams on what penetration test findings look like and where to get remediation guidance, so results lead to fixes rather than confusion. 

1.  **Automate repeatable tests:** Use tools to speed up common or repeatable scenarios, which frees testers to focus on business logic and chained weaknesses that need human judgment. To use [AWS Continuum](https://aws.amazon.com/continuum/), create an agent space for each application, prove that you own the domain you want to test, then connect the repository and documents for the agent to read. 

1.  **Analyze findings and close the loop:** Review findings for systemic issues, then add automated tests for recurring problems and update builder training based on what the tests reveal. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [SEC11-BP01 Embed security ownership in workload teams, and train for application security](sec11-bp01.md) 
+  [SEC11-BP03 Automate testing throughout the development and release lifecycle](sec11-bp03.md) 
+  [SEC11-BP05 Conduct code reviews](sec11-bp05.md) 

 **Related documents:** 
+  [AWS penetration testing policy](https://aws.amazon.com/security/penetration-testing/) 
+  [Accelerate deployments on AWS with effective governance](https://aws.amazon.com/blogs/architecture/accelerate-deployments-on-aws-with-effective-governance/) 
+  [Modernize your penetration testing architecture on AWS Fargate](https://aws.amazon.com/blogs/architecture/modernize-your-penetration-testing-architecture-on-aws-fargate/) 
+  [AWS Security Competency Partners](https://aws.amazon.com/security/partner-solutions/) 
+  [AWS Security Agent (now AWS Continuum) on-demand penetration testing now generally available](https://aws.amazon.com/blogs/security/aws-security-agent-on-demand-penetration-testing-now-generally-available/) 
+  [AWS Well-Architected Agentic AI Lens: Agent vulnerability scanning and penetration testing](https://docs.aws.amazon.com/wellarchitected/latest/agentic-ai-lens/agentsec09.html) 

 **Related examples:** 
+  [Automate API testing with AWS CodePipeline](https://github.com/aws-samples/aws-codepipeline-codebuild-with-postman) 
+  [Automated Security Helper](https://github.com/awslabs/automated-security-helper) 