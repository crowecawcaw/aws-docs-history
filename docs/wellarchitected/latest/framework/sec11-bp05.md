

# SEC11-BP05 Conduct code reviews

 In a code review, a team member other than the author reads the code delta to find defects, vulnerabilities, and departures from your standards. Reviews spread knowledge across the team and help less experienced developers learn. Automated tools handle mechanical checks so reviewers concentrate on logic and design. 

 **Desired outcome:** 
+  A reviewer other than the author approves every change before it merges or deploys. 
+  Your reviews raise the security and quality of the code, not only its correctness. 
+  Your less experienced team members learn from the feedback they receive during reviews. 
+  Your automated tools handle repetitive checks so human reviewers concentrate on design and business logic. 

 **Common anti-patterns:** 
+  Teams deploy code without any review. 
+  The same person writes and approves the change. 
+  Reviews are entirely manual, with no tooling to assist or orchestrate them. 
+  Reviewers have no training in application security and cannot spot security flaws. 

 **Benefits of establishing this best practice:** 
+  Code quality improves because a second reviewer catches issues the author missed. 
+  Teams reuse common, proven approaches, which makes the codebase more consistent. 
+  Fewer issues reach penetration testing and later stages, where they cost more to fix. 
+  Knowledge spreads across the team as reviewers and authors exchange context. 

 **Level of risk exposed if this best practice is not established:** Medium 

## Implementation guidance
<a name="implementation-guidance"></a>

 The author of a change is the person least able to see its flaws, because they already believe it is correct. A reviewer who did not write the code questions choices the author took for granted. The author must not review their own work. 

 Manual review and automated analysis complement each other. Tools handle mechanical checks, such as style violations, known-insecure functions, missing null checks, and common vulnerability signatures. Humans judge what tools cannot, such as design soundness, authorization gaps in business logic, and subtle race conditions. Automate the mechanical checks so your reviewers can spot problems only a human can catch. 

 The most common failure mode is the review that exists on paper but not in practice. For example, a reviewer who approves without reading, a required-reviewer rule filled by a colleague who rubber-stamps, or a queue so slow that authors pressure reviewers to hurry. An untrained reviewer who cannot recognize a security flaw could approve one in good faith. Train your reviewers in application security, and treat review as real work with time allocated for it. 

 When feedback attacks the person, authors become defensive and reviewers soften their comments until the review means nothing. Make reviews a shared responsibility for quality. Keep feedback specific and about the code. Approach findings as a chance to learn. [Amazon Inspector code security](https://docs.aws.amazon.com/inspector/latest/user/scanning-cicd.html) scans application code, third-party dependencies, and infrastructure as code to flag security vulnerabilities, secrets, and code quality issues. It connects to GitHub and GitLab, runs on every change, and gives authors feedback before a human reviewer sees the code. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Establish a review process:** Decide when reviews happen, such as before a merge to the main branch or before a production deployment, and who takes part. Document the methodology so every team applies it the same way. 

1.  **Set up and configure review tools:** Select tools that fit your workflow, such as [GitHub pull requests](https://docs.github.com/en/pull-requests/get-started/about-pull-requests) or [Amazon Inspector code security](https://docs.aws.amazon.com/inspector/latest/user/scanning-cicd.html). Integrate them with your repositories and pipelines, and configure rules such as a minimum number of reviewers and required approvals. 

1.  **Define a review checklist:** Write down what reviewers check, covering code quality, security vulnerabilities, adherence to coding standards, and performance. Share it so all reviewers hold the same expectations. 

1.  **Train reviewers in application security:** Teach your team how to conduct effective reviews and which common vulnerabilities to look for. Use pair programming and knowledge sharing to bring less experienced members up to speed. 

1.  **Integrate review into the workflow:** Make review a required step, such as opening a pull request and assigning reviewers, and block merges or deployments until it completes. Encourage direct, constructive feedback. 

1.  **Monitor and improve the process:** Review how well the process works, gather feedback from the team, and look for steps to automate. Update the checklist as you learn and as practices change. 

1.  **Foster a supportive review culture:** Reinforce why reviews matter, keep feedback about the code rather than the person, and create an environment where developers give and receive feedback comfortably. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [SEC11-BP02 Follow established secure coding guidelines](sec11-bp02.md) 
+  [SEC11-BP03 Automate testing throughout the development and release lifecycle](sec11-bp03.md) 
+  [SEC11-BP04 Perform regular penetration testing](sec11-bp04.md) 

 **Related documents:** 
+  [DevOps Guidance: DL.CR.2 Perform peer review for code changes](https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/dl.cr.2-perform-peer-review-for-code-changes.html) 
+  [About pull requests in GitHub](https://docs.github.com/en/pull-requests/reference/pull-requests) 
+  [Amazon Inspector Code Security](https://docs.aws.amazon.com/inspector/latest/user/code-security-assessments.html) 

 **Related tools:** 
+  [Amazon Inspector code security](https://docs.aws.amazon.com/inspector/latest/user/scanning-cicd.html) 