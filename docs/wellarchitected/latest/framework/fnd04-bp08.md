

# FND04-BP08 Establish resilience testing tooling

 Resilience testing (fault injection, chaos engineering, game days) validates that workloads handle the failures they are designed to handle. Without central tooling, workload teams either build their own testing infrastructure or, more often, skip testing entirely. A central resilience testing foundation gives workload teams ready-to-use experiment templates, safe execution environments, and the observability they need to learn from each experiment. 

 **Desired outcome:** 
+  Your foundation team provides a central resilience testing service based on AWS Fault Injection Service (FIS), with pre-built experiment templates for common failure modes. 
+  Your workload teams can run resilience experiments in non-production environments without building the testing infrastructure themselves. 
+  Your experiments are bounded by stop conditions, scope-of-impact controls, and approval gates so production experiments cannot cause uncontrolled impact. 
+  Your game days and resilience exercises are scheduled and tracked centrally, with findings flowing into workload improvement backlogs. 
+  Your observability system is integrated with the testing service so each experiment produces a clear before-and-after signal workload teams can learn from. 

 **Common anti-patterns:** 
+  Relying on the assumption that workloads are resilient because they were designed to be, without ever validating the assumption experimentally. 
+  Running chaos experiments in production without stop conditions or scope-of-impact controls, causing real customer impact rather than controlled learning. 
+  Each workload team building its own experiment tooling from scratch, so testing is rare, inconsistent, and limited by what each team has time to build. 
+  Treating resilience testing as a one-time certification instead of an ongoing practice, so drift between test runs goes unnoticed. 
+  Running experiments without observability integration, so the team cannot see what the experiment actually caused and cannot tell whether the workload handled it correctly. 
+  Running game days only in non-production, so the tested resilience patterns never prove themselves against the real dependencies, scale, and configurations of production. 

 **Benefits of establishing this best practice:** 
+  Validated resilience because experiments confirm that workloads actually handle the failures they are designed to handle, not just the failures their designers imagined. 
+  Faster learning because the foundation team's shared experiment templates help workload teams start testing immediately rather than building tooling for six months first. 
+  Safer production testing because the central service enforces stop conditions, scope-of-impact limits, and approval gates on experiments that touch production. 
+  Continuous improvement because exercises run on a regular schedule, with findings feeding back into workload improvement rather than sitting in a post-exercise report. 
+  Clearer incident response muscle memory because game days exercise the teams and runbooks that will be needed during real incidents. 

 **Level of risk exposed if this best practice is not established:** Medium 

## Implementation guidance
<a name="implementation-guidance"></a>

 A workload's resilience design might determine that a workload will tolerate an Availability Zone failure, a dependency failure, or a scaling event, but that design is rarely tested until the failure actually happens. Testing infrastructure is expensive to build, production testing can be intimidating, your test environments might not closely resemble production, and the teams that would benefit most from testing may also lack resources. Resilience that works in practice is a result of testing that resilience in reality. 

 A central foundation lowers the cost of resilience testing. The foundation team provides the service (AWS Fault Injection Service), a library of experiment templates for common failure modes, safety controls, and observability integration. Workload teams consume these experiments instead of building their own. 

 [AWS Fault Injection Service (FIS)](https://aws.amazon.com/fis/) is the native AWS service for this. It supports experiments against [Amazon EC2](https://docs.aws.amazon.com/fis/latest/userguide/fis-actions-reference.html#fis-actions-reference-ec2), [Amazon ECS](https://docs.aws.amazon.com/fis/latest/userguide/fis-actions-reference.html#fis-actions-reference-ecs), [Amazon EKS](https://docs.aws.amazon.com/fis/latest/userguide/fis-actions-reference.html#fis-actions-reference-eks), [Amazon RDS](https://docs.aws.amazon.com/fis/latest/userguide/fis-actions-reference.html#fis-actions-reference-rds), and [network paths](https://docs.aws.amazon.com/fis/latest/userguide/fis-actions-reference.html#fis-actions-reference-network), with [experiment templates](https://docs.aws.amazon.com/fis/latest/userguide/experiment-templates.html) defining actions, targets, and stop conditions. [Pre-defined scenarios](https://docs.aws.amazon.com/fis/latest/userguide/) cover common failure patterns: Availability Zone impairment, Region-scale impact, EC2 instance interruption, and network packet loss. The foundation team curates these templates, adapts them to the organization's common architecture patterns, and publishes them for reuse. 

 **Safety controls** limit every experiment's impact. [Stop conditions](https://docs.aws.amazon.com/fis/latest/userguide/stop-conditions.html) tied to CloudWatch alarms halt an experiment automatically when customer-impacting metrics cross a threshold. Scope-of-impact limits confine experiments to tagged resources, specific accounts, or non-production environments. Approval gates require explicit sign-off before experiments run in production, routed through the foundation team or the workload team's own change management. 

 *Production testing* exposes failure modes that non-production cannot, and it has the highest risk of customer impact. Run the same experiment in staging first, then in production during a quiet period with a small scope of impact. Expand the scope of impact only after the workload handles the small experiments. Stop conditions and rollback keep production experiments from causing uncontrolled customer impact. 

 *Game days* complement fault injection by exercising the human and procedural side of resilience: the on-call rotation, runbooks, escalation paths, and communication channels. [SEC10-BP04 Run simulations](sec10-bp04.md) provides a starting framework. The foundation team owns the game day tooling (scheduling, scenario design, and run patterns) and rotates workload teams through exercises. Findings from game days feed into runbook improvements, monitoring gaps, and training needs. 

 *Observability integration* places each experiment's results in the same dashboards and telemetry the workload team already uses. Each experiment produces a before-and-after signal in [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) dashboards, X-Ray traces, and Security Hub CSPM findings, so the workload team can see what the experiment did and how the workload responded. 

**Important**  
 Start every resilience testing program in non-production with non-disruptive experiments, then progress to disruptive experiments as teams build confidence. Production fault injection without stop conditions and scope-of-impact limits can cause a customer-facing incident. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Define the resilience testing program scope and approval model:** Document which teams own the central testing service, which experiments require foundation-team approval, which can be self-service by workload teams in non-production, and which require change-management review before running in production. The approval model is the guardrail that makes the service safe to use without friction that discourages use. 

1.  **Deploy AWS Fault Injection Service as the central testing service:** Enable [AWS Fault Injection Service](https://docs.aws.amazon.com/fis/latest/userguide/getting-started.html) in the accounts that will run experiments. Create IAM roles with least-privilege permissions for the resources experiments will target, scoped by tag so experiments cannot affect untagged or untested resources. Document how workload teams request access and how their resources are tagged in. 

1.  **Publish a library of experiment templates for common failure modes:** Build and publish [FIS experiment templates](https://docs.aws.amazon.com/fis/latest/userguide/experiment-templates.html) covering the failure modes most relevant to your organization: single-instance failure, Availability Zone impairment, dependency latency and failure, database failover, network partition, and certificate expiry. Start with the [pre-defined scenarios](https://docs.aws.amazon.com/fis/latest/userguide/) and adapt them to your common architecture patterns. Publish the templates as reusable modules with documentation on what each experiment tests and how to interpret the results. 

1.  **Configure stop conditions and scope-of-impact limits:** For each template, define [stop conditions](https://docs.aws.amazon.com/fis/latest/userguide/stop-conditions.html) tied to CloudWatch alarms on customer-impacting metrics (error rate, latency, availability). Scope target selection using tags so experiments only run against resources that have been explicitly marked as in scope. Document the stop conditions in the template so workload teams understand what helps protect them. 

1.  **Integrate with the observability system:** Configure experiments to emit CloudWatch events at start, completion, and stop, and publish the events to a shared dashboard. Tag all experiment-related telemetry so it can be correlated with workload metrics. Provide a standard Before/During/After dashboard template that workload teams use to evaluate each experiment. 

1.  **Run experiments in non-production first:** Establish the practice of running every new experiment template in non-production before it is used in production. This validates the experiment itself (does it do what it says it does) and the stop conditions (do they fire when expected) without putting real users at risk. Non-production experimentation also gives workload teams time to build their interpretation muscle before the stakes are higher. 

1.  **Expand to production experiments with progressive impact radius:** When a workload's non-production experiments produce consistent, well-understood results, graduate to production testing. Start with the smallest possible impact radius (a single instance, a single shard), a quiet traffic window, and an approved change window. Expand the impact radius over successive experiments as the workload handles the small ones cleanly. Do not run a larger impact radius in production than has been tested in non-production. 

1.  **Schedule and run game days:** Run regular game days with rotating workload teams. Each game day has a defined scenario (a particular failure or combination of failures), a lead from the foundation team, and clear roles for the workload team: incident commander, communications lead, and investigators. Capture findings in a practical format: what worked, what did not, what runbook changes are needed, and what monitoring gaps surfaced. Track completion of the follow-up actions so that game days produce improvement, not just insight. 

1.  **Report program effectiveness and evolve the template library:** Maintain metrics on program health: number of experiments run per quarter, coverage of common failure modes, number of findings closed, and mean time from game-day finding to remediation. Use the metrics to guide where the template library needs to grow (a new failure mode common enough to warrant a template) and where workload teams need more support (a team whose experiments keep producing unexpected results). 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [FND04-BP06 Establish centralized backup standards and mechanisms](fnd04-bp06.md) 
+  [FND04-BP07 Establish cross-Region replication and failover capabilities](fnd04-bp07.md) 
+  [FND05-BP10 Prepare forensic capabilities](fnd05-bp10.md) 
+  [REL12-BP05 Conduct game days regularly](rel12-bp05.md) 
+  [REL12-BP04 Test resilience using chaos engineering](rel12-bp04.md) 

 **Related documents:** 
+  [AWS Fault Injection Service User Guide](https://docs.aws.amazon.com/fis/latest/userguide/what-is.html) 
+  [FIS pre-defined scenarios](https://docs.aws.amazon.com/fis/latest/userguide/) 
+  [Stop conditions for FIS experiments](https://docs.aws.amazon.com/fis/latest/userguide/stop-conditions.html) 
+  [SEC10-BP04 Run simulations](sec10-bp04.md) 
+  [Chaos engineering on AWS](https://aws.amazon.com/blogs/architecture/chaos-engineering-in-the-cloud/) 
+  [Operational readiness reviews](https://docs.aws.amazon.com/wellarchitected/latest/operational-readiness-reviews/wa-operational-readiness-reviews.html) 

 **Related examples:** 
+  [Use AWS Fault Injection Service to test your application resiliency](https://aws.amazon.com/blogs/architecture/verify-the-resilience-of-your-workloads-using-chaos-engineering/) 
+  [Running chaos experiments on Amazon EKS](https://aws.amazon.com/blogs/devops/chaos-engineering-on-amazon-eks-using-aws-fault-injection-simulator/) 

 **Related services:** 
+  [AWS Fault Injection Service](https://aws.amazon.com/fis/) 
+  [AWS Resilience Hub](https://aws.amazon.com/resilience-hub/) 
+  [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) 