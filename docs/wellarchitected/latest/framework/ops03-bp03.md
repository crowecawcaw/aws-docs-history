

# OPS03-BP03 Implement practices to improve code quality

 Defects are cheapest to remove before a change is deployed. Practices such as test-driven development, code reviews, pair programming, and shared coding standards raise quality at the source, so fewer defects reach testing and production. A second reviewer catches errors, security flaws, and standards violations the author cannot see, and spreads knowledge across the team. 

 **Desired outcome:** 
+  Your teams use code reviews or pair programming, so no change reaches the main branch unreviewed. 
+  Your developers and operators treat quality practices as part of the normal development lifecycle, not an afterthought. 
+  Your team members build skills and share knowledge through the review process. 
+  Your automated tools handle the mechanical parts of review, so your reviewers focus on judgment. 

 **Common anti-patterns:** 
+  A developer commits to the main branch with no review, the change deploys automatically, and it causes an incident. 
+  Teams ask builders to review code for security without training them on what to look for. 
+  A new application ships with no unit, integration, or end-to-end tests, so nothing can be verified before deployment. 
+  Operators make manual fixes directly in production, bypassing review and leaving no record in the delivery process. 
+  A team runs automated code analysis only at the review gate, so developers see security, logic, and standards findings for the first time after they have already submitted the change for review. 

 **Benefits of establishing this best practice:** 
+  Fewer defects reach production because problems are caught at the source. 
+  Later-stage testing and penetration testing surface fewer issues. 
+  Reviews and pair programming spread knowledge and reduce single points of failure on the team. 
+  Shared coding standards make the codebase more consistent and easier to maintain. 

 **Level of risk exposed if this best practice is not established:** Medium 

## Implementation guidance
<a name="implementation-guidance"></a>

 In a code review, another engineer reads the change before it merges. It catches defects, distributes understanding of the codebase, and enforces standards that keep code consistent as teams grow. Authors miss gaps between intent and implementation because they know what they meant; a reviewer sees the code as written. 

 Test-driven development inverts the usual order: you write a failing test that describes the desired behavior, then write the code that makes it pass. It forces you to define "correct" before you build, and leaves behind a regression suite. The cost is up-front effort and a learning curve. Well-specified logic benefits most; exploratory or throwaway code benefits least. 

 In pair programming, review happens as the change is written. Two developers at one change catch problems and transfer knowledge immediately, which helps with complex features or onboarding. It also spends two people's time on one task, so most teams reserve it for high-risk or high-learning work. Where you draw that line depends on team size, seniority mix, and defect cost. 

 Reviews only catch what the reviewer knows to look for. A team that reviews for correctness but has no training in application security won't catch security flaws. Train reviewers in secure coding patterns, common vulnerability classes, and your organization's standards before you rely on the review as a quality gate. 

 Agentic assistants extend this by working from a specification. [Kiro](https://kiro.dev/) generates code, unit tests, and documentation from a spec, scans infrastructure as code, detects vulnerabilities and secrets, and can run an automated first-pass review through sub-agents. Because these tools work quickly, keep each change small enough for a reviewer to judge whether it is the right change. 

 Automated review and analysis tools catch mechanical issues such as security findings, logic bugs, and standards violations. If they run only at the review gate, developers see the findings after they submit the change, and review becomes a second round of development. Make the same analysis available as a local command or API so developers fix findings before review. Use the same rules locally as at the gate so the results match. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Adopt quality practices in your delivery process:** Choose the practices that fit your work, such as test-driven development, code reviews, pair programming, and shared coding standards, and make them part of continuous integration and delivery rather than optional extras. Require a review before any change merges to the main branch. 

1.  **Train reviewers before relying on reviews:** Give reviewers the secure coding knowledge and standards they need, so reviews catch security flaws and not just functional bugs. Document the standards a review must check against. 

1.  **Generate specs, tests, and documentation:** Use [Kiro](https://kiro.dev/) to implement features from [feature specs](https://kiro.dev/docs/specs/feature-specs/), verify behavior with [property-based tests](https://kiro.dev/docs/specs/correctness/), and generate documentation. Add [vulnerability inspection to your pipelines](https://docs.aws.amazon.com/inspector/latest/user/cicd-inspector-codepipeline-actions.html) so scanning runs on every change. 

1.  **Automate first-pass review with Kiro sub-agents:** Use [sub-agents in Kiro](https://kiro.dev/docs/custom-agents/subagents/#how-sub-agents-work) to automate code reviews, and extend them through the [Model Context Protocol (MCP)](https://kiro.dev/docs/mcp/) with specialist servers such as the [AWS Documentation server](https://kiro.dev/docs/mcp/usage/#aws-documentation-server) and the [AWS Well-Architected Security Assessment Tool MCP Server](https://awslabs.github.io/mcp/servers/well-architected-security-mcp-server). Route the findings into your review workflow. 

1.  **Make automated analysis callable locally:** Expose your automated code analysis as a local command, IDE integration, or API that developers and their coding agents can run before submitting a change. Use the same rules as the review gate, and reuse results for unchanged code. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [OPS03-BP02 Test and validate any and all changes](ops03-bp02.md) 
+  [OPS03-BP01 Adopt a configuration, build, and release pipeline](ops03-bp01.md) 
+  [OPS03-BP04 Fully automate integration and deployment](ops03-bp04.md) 

 **Related documents:** 
+  [DevOps Guidance: DL.CR.2 Perform peer review for code changes](https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/dl.cr.2-perform-peer-review-for-code-changes.html) 
+  [My CI/CD pipeline is my release captain](https://builder.aws.com/content/3Ev3XnnYuuBhlgnywbbVFzwibm1/my-cicd-pipeline-is-my-release-captain) 
+  [Shift-Left Workload, leveraging AI for test creation](https://builder.aws.com/content/2gBZtC94gPzaCQRnt4P0rIYWuBx/shift-left-workload-leveraging-ai-for-test-creation) 
+  [Agile software guide](https://martinfowler.com/agile.html) 
+  [On pair programming](https://martinfowler.com/articles/on-pair-programming.html) 
+  [Why code reviews matter (and actually save time)](https://www.atlassian.com/agile/software-development/code-reviews) 
+  [The Art of Agile Development: Test-driven development](https://www.jamesshore.com/v2/books/aoad1/test_driven_development) 
+  [Five ways to use Kiro and Amazon Q to strengthen your security posture](https://aws.amazon.com/blogs/security/five-ways-to-use-kiro-and-amazon-q-to-strengthen-your-security-posture/) 
+  [Automate your development workflow with Kiro's AI agent hooks](https://kiro.dev/blog/automate-your-development-workflow-with-agent-hooks/) 
+  [AWS Well-Architected Security Assessment Tool MCP Server](https://awslabs.github.io/mcp/servers/well-architected-security-mcp-server) 
+  [AWS Documentation server](https://kiro.dev/docs/mcp/usage/#aws-documentation-server) 

 **Related videos:** 
+  [Getting Started with Kiro for Non-Technicals](https://www.youtube.com/watch?v=PbgGC2n_Xu0) 
+  [Transform Your Development Workflow with Kiro](https://www.youtube.com/watch?v=JOqLp1adGO4) 
+  [Extending Kiro's Capabilities with MCP](https://www.youtube.com/watch?v=gFbCXnlWgW0) 

 **Related services:** 
+  [Kiro](https://kiro.dev/) 
+  [Amazon Inspector](https://aws.amazon.com/inspector/) 