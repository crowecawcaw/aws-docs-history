

# REL08-BP02 Integrate functional testing as part of your deployment

 Functional tests confirm that code behaves as the requirements specify before it reaches customers. When these tests run automatically inside the deployment pipeline and a failure stops the release, defects are caught in a controlled environment before they reach production. 

 **Desired outcome:** 
+  Your unit and integration tests run automatically on every change as part of the deployment pipeline. 
+  A test failure halts or rolls back the deployment, so unverified code cannot reach production. 
+  Your tests run in a pre-production environment that closely resembles production. 
+  Your test suite is maintainable and evolves with the application rather than decaying as the code changes. 

 **Common anti-patterns:** 
+  Teams ignore or bypass test failures during deployment to meet a timeline. 
+  Teams run tests manually outside the pipeline, so results depend on who remembers to run them. 
+  Teams skip testing steps through manual emergency workflows. 
+  Teams run automated tests in an environment that does not resemble production. 
+  Teams build a rigid test suite that is hard to maintain, update, or scale as the application evolves. 

 **Benefits of establishing this best practice:** 
+  Defects surface early, which lowers the risk of releasing bugs or unexpected behavior to production. 
+  Unit tests confirm that code behaves as intended and that API contracts hold. 
+  Integration tests confirm that components such as user interfaces, APIs, and databases work together as specified. 
+  Releases become more predictable because every change passes the same enforced checks. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 Unit tests and integration tests answer different questions: 
+  A *unit test* checks the smallest testable piece of code in isolation, confirming that one function behaves correctly for a given input. 
+  An *integration test* checks that features work together and accounts for side effects, such as the state change caused by a mutation operation. 

 Unit tests are fast and pinpoint the exact line that broke. Integration tests are slower but catch the failures that only appear when components interact. Relying on one type alone means that unit tests pass while the system is broken, or integration tests fail without telling you where the failure occurs. 

 In *test-driven development (TDD)*, you write the test case first, watch it fail, then write the code that makes it pass. This produces a test suite that grows with the code. Teams that add tests only after shipping tend to write tests that confirm current behavior, including its bugs, rather than the intended behavior. 

 If your pre-production environment differs from production, a passing test gives false confidence. Configuration differences, missing dependencies, and divergent data shapes cause production failures, so the staging environment must mirror production as closely as practical. Using the same deployment mechanism for every environment removes another class of difference, because the path to production is itself tested on the way there. 

 Automated tests protect reliability only when a failure stops the release. If the pipeline continues past a failed test or a manual override lets it through, the tests do not enforce anything. Wire the pipeline to halt or roll back when success criteria are not met, and treat emergency bypass paths as rare, audited exceptions rather than a routine escape hatch. For web and mobile applications, add cross-browser and real-device tests, where compatibility failures are common and hard to reproduce manually. 

 Test coverage shows how much of the code your tests exercise. Code coverage tools such as [JaCoCo](https://www.jacoco.org/jacoco/) for Java or [Istanbul](https://istanbul.js.org/) for JavaScript report which lines and branches execute during a test run. Integrate coverage reporting into the build stage so teams can track coverage over time, spot declining coverage on critical paths, and focus new tests where they add the most value. Coverage is a directional signal, not a target to game. High coverage does not guarantee correctness, but a sustained decline usually means new code is shipping without tests. 

 Progressive deployment strategies complement testing by limiting the blast radius of a defect that tests did not catch. When a deployment uses canary releases, linear rollouts, or blue/green swaps, the system runs verified code alongside the new change and promotes it only if health checks and alarms stay clean. This adds a live-traffic safety net but does not replace functional testing. See [REL08-BP05 Deploy changes with automation](rel08-bp05.md) for detailed guidance on progressive deployment. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Adopt test-driven development for unit tests:** Write unit tests before the functional code, and make passing unit tests a coding requirement enforced before commit. Establish code guidelines so that writing and running these tests is a standard part of development. 

1.  **Build an automated integration test suite:** Create integration tests that cover the testable functionality of your application. Design them to simulate user interactions and validate the expected outcomes, including the side effects that unit tests do not cover. 

1.  **Provision a production-like test environment:** Create the staging or pre-production environment where integration tests run, and make it resemble production in configuration, dependencies, and data shape as closely as practical. 

1.  **Configure pipeline stages:** Set up source, build, test, and deploy stages using the [AWS CodePipeline](https://docs.aws.amazon.com/codepipeline/latest/userguide/getting-started-codepipeline.html) console or AWS CLI. Run unit tests in the build stage and integration tests in the test stage. 

1.  **Deploy with a consistent mechanism:** Use [AWS CodeDeploy](https://docs.aws.amazon.com/codedeploy/latest/userguide/getting-started-codedeploy.html) to deploy the built and tested code to staging and then production. Use the same deployment mechanism across all environments, whether the targets are Amazon EC2 instances, AWS Lambda functions, or on-premises servers. 

1.  **Gate the pipeline on test results:** Configure [quality checks](https://docs.aws.amazon.com/codepipeline/latest/userguide/monitoring.html) that block progression when tests fail, and configure notifications for stage failures and pipeline completion. Integrate code coverage reporting into the build stage so the team can track coverage trends over time. For web and mobile applications, add cross-browser and real-device testing with [AWS Device Farm](https://docs.aws.amazon.com/codepipeline/latest/userguide/action-reference-DeviceFarm.html) as an additional pipeline action. 

1.  **Review test results and refine the suite:** Track results over time and look for regressions and areas that need more coverage. Use what you learn to strengthen the suite and remove tests that no longer apply, such as tests that validate deprecated behavior or duplicate coverage provided by other tests. Be cautious about removing tests without justification - tests that catch real bugs are worth fixing rather than deleting. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [REL08-BP03 Integrate resilience testing as part of your deployment](rel08-bp03.md) 
+  [REL08-BP05 Deploy changes with automation](rel08-bp05.md) 
+  [REL07-BP04 Load test your workload](rel07-bp04.md) 
+  [REL12-BP04 Test resilience using chaos engineering](rel12-bp04.md) 

 **Related documents:** 
+  [Test automation](https://docs.aws.amazon.com/prescriptive-guidance/latest/performance-engineering-aws/test-automation.html) 
+  [Continuous delivery and continuous integration](https://docs.aws.amazon.com/codepipeline/latest/userguide/concepts-continuous-delivery-integration.html) 
+  [Indicators for functional testing](https://docs.aws.amazon.com/wellarchitected/latest/devops-guidance/indicators-for-functional-testing.html) 
+  [Monitoring pipelines](https://docs.aws.amazon.com/codepipeline/latest/userguide/monitoring.html) 
+  [Use AWS CodeBuild with AWS CodePipeline to test code and run builds](https://docs.aws.amazon.com/codebuild/latest/userguide/how-to-create-pipeline.html) 
+  [Create code coverage reports](https://docs.aws.amazon.com/codebuild/latest/userguide/code-coverage-report.html) 