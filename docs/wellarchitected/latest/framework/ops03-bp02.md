

# OPS03-BP02 Test and validate any and all changes

 Test every change before it reaches production, including application code, infrastructure, configuration, security controls, and operational procedures. When you run tests immediately after each change, defects are cheap to fix and developers get fast feedback. 

 **Desired outcome:** 
+  Your changes are tested before they are delivered, and your pipeline blocks any change that fails. 
+  Your developers see test results quickly and act on them without leaving their workflow. 
+  Your testing covers application code, infrastructure, configuration, and security controls, not code alone. 
+  Every artifact meets your shared testing standard before it is promoted. 

 **Common anti-patterns:** 
+  Teams deploy a change with no tests, and it fails in production and causes an incident. 
+  Teams deploy new security group rules without testing them, and the change makes the application unreachable for customers. 
+  Developers modify a method that has no unit test, and the defect surfaces only after release. 
+  Testing happens manually at the end of the process, so feedback arrives too late to be cheap to act on. 

 **Benefits of establishing this best practice:** 
+  Change failure rate drops because defects are caught before release. 
+  Software quality improves as tests document expected behavior and guard against regression. 
+  Developers gain confidence in their changes through fast, automated feedback. 
+  Security and compliance controls roll out with evidence that they work as intended. 
+  Infrastructure changes such as scaling policy updates are validated before they affect live traffic. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 The earlier a test runs, the cheaper the defect is to fix, because less work has been built on top of it. 

 Unit tests check a single function in isolation and run in milliseconds. Integration and end-to-end tests exercise components together and take longer. Static analysis and software composition analysis (SCA) inspect code and dependencies for known vulnerabilities without running the software. Weight your test suite toward fast, narrow tests and use slower, broad tests sparingly. A suite that takes an hour to run gets skipped under deadline pressure. 

 Test infrastructure definitions, configuration, security controls, and operational procedures the same way you test code. Code tests never catch security group rules that block legitimate traffic, a scaling policy that fails under load, or a runbook that no longer matches reality. Treat every artifact that can change production behavior as something to test. 

 Automated tests remove manual effort and human error, and give developers fast feedback. Automate everything repetitive, and reserve human judgment for work such as exploratory testing, usability review, or security assessment of a novel design. Publish results to developers immediately. Agree on a testing standard with stakeholders that defines which tests every artifact must pass and who is notified when they complete. 

 Use [Kiro](https://kiro.dev/) to write code artifacts, find and resolve bugs, and develop unit tests across large codebases. [AWS CodeBuild](https://docs.aws.amazon.com/codebuild/latest/userguide/welcome.html) runs tests on each artifact, and [AWS CodePipeline](https://docs.aws.amazon.com/codepipeline/latest/userguide/welcome.html) sequences those tests into gates a change must clear before promotion. The [AWS Deployment Pipeline Reference Architecture](https://aws-samples.github.io/aws-deployment-pipeline-reference-architecture/) catalogs the test types you can place at each stage. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Define a testing standard with your stakeholders:** Agree on which tests every artifact must pass, the compliance and governance requirements to cover, and who is notified when tests complete. Use the [AWS Deployment Pipeline Reference Architecture](https://aws-samples.github.io/aws-deployment-pipeline-reference-architecture/) as an authoritative list of test types to include. 

1.  **Instrument artifacts with automated tests:** Add the tests your standard requires so they run as part of the integration pipeline, and keep each suite within a predictable duration, such as under ten minutes. Use [Kiro](https://kiro.dev/) to generate unit tests with boundary conditions and to find defects. 

1.  **Run tests automatically in the pipeline:** Configure [AWS CodeBuild](https://docs.aws.amazon.com/codebuild/latest/userguide/welcome.html) to run your tests on each change, and use [AWS CodePipeline](https://docs.aws.amazon.com/codepipeline/latest/userguide/welcome.html) to order them into gates that block promotion on failure. 

1.  **Test infrastructure and security changes the same way:** Validate infrastructure definitions, configuration, and security controls in a pre-production environment before they reach production. Apply the same automated gates to these artifacts that you apply to application code. 

1.  **Publish results and store validated artifacts:** Send test outcomes to developers as each gate passes, so feedback is immediate. Promote only artifacts that clear every gate, and store them in an artifact repository for deployment. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [OPS03-BP03 Implement practices to improve code quality](ops03-bp03.md) 
+  [OPS03-BP04 Fully automate integration and deployment](ops03-bp04.md) 
+  [OPS03-BP01 Adopt a configuration, build, and release pipeline](ops03-bp01.md) 
+  [OPS04-BP02 Automate testing and rollback](ops04-bp02.md) 

 **Related documents:** 
+  [Practicing continuous integration and continuous delivery on AWS](https://docs.aws.amazon.com/whitepapers/latest/practicing-continuous-integration-continuous-delivery/welcome.html) 
+  [My CI/CD pipeline is my release captain](https://builder.aws.com/content/3Ev3XnnYuuBhlgnywbbVFzwibm1/my-cicd-pipeline-is-my-release-captain) 
+  [Shift-Left Workload, leveraging AI for test creation](https://builder.aws.com/content/2gBZtC94gPzaCQRnt4P0rIYWuBx/shift-left-workload-leveraging-ai-for-test-creation) 

 **Related videos:** 
+  [AWS re:Invent 2025 - Spec-driven development with Kiro (DEV314)](https://www.youtube.com/watch?v=4qcWgPb-8Fk) 
+  [The Tale of Building with Kiro](https://www.youtube.com/watch?v=ht68gwyD4ZU) 

 **Related examples:** 
+  [AWS Deployment Pipeline Reference Architecture - Application](https://aws-samples.github.io/aws-deployment-pipeline-reference-architecture/application-pipeline/index.html) 
+  [AWS Kubernetes DevSecOps pipeline](https://github.com/aws-samples/devsecops-cicd-containers) 

 **Related services:** 
+  [Kiro](https://kiro.dev/) 
+  [AWS CodeBuild](https://docs.aws.amazon.com/codebuild/latest/userguide/welcome.html) 
+  [AWS CodePipeline](https://docs.aws.amazon.com/codepipeline/latest/userguide/welcome.html) 