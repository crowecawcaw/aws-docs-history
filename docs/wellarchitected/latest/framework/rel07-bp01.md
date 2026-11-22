

# REL07-BP01 Use automation when obtaining or scaling resources

 Manual provisioning produces environments that drift apart and fail in non-reproducible ways. When you define resources as code and automate provisioning and scaling, every environment is built the same way and every change is reviewable. This turns capacity into a property of your architecture. 

 **Desired outcome:** 
+  Your infrastructure is defined as code and stored in a version control system, so every change is reviewable, auditable, and repeatable. 
+  Automated pipelines apply infrastructure changes, and code commits initiate provisioning and updates without manual console work. 
+  Your resources scale out and scale in automatically in response to demand signals, within limits you have defined. 
+  Configuration drift is detected against the declared state, so divergence does not go unnoticed. 

 **Common anti-patterns:** 
+  Teams provision resources manually through the console or command line, a practice sometimes called click-ops. 
+  Teams tightly couple components, which produces rigid architectures that cannot scale a single tier independently. 
+  Scaling policies stay fixed and do not adapt to changing traffic patterns, business events, or new resource types. 
+  Teams estimate capacity manually and provision statically to cover an anticipated peak. 

 **Benefits of establishing this best practice:** 
+  Infrastructure changes move through the same review, testing, and release process as application code, which reduces error-prone manual work. 
+  Environments are consistent and reproducible, so a fault in one environment can be recreated and diagnosed in another. 
+  Capacity tracks demand automatically, which improves availability during traffic growth and reduces cost when demand falls. 
+  Recovery is faster because rebuilding a resource means re-applying its definition rather than reconstructing it from memory. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 Infrastructure as code (IaC) treats the definition of your environment as a versioned artifact. Instead of a person clicking through a console to create a load balancer or a database, you declare the desired state in a template and let a provisioning engine reconcile reality to match it. You can review a declared state before applying it, compare it against what is actually running, and re-apply it identically in another account or Region. 

 The most damaging failure mode in manual environments is *drift*, the divergence between what you believe is deployed and what is actually running. Someone adjusts a security group during an incident, or increases an instance size to handle a spike, and never records it. Months later a rebuild produces a subtly different environment that fails in production. IaC with drift detection makes the declared template the single source of truth and surfaces any manual change as a deviation to reconcile. 

 *Provisioning automation* creates and updates the resources through a delivery pipeline. The pipeline validates templates, deploys to a staging environment, runs tests, and promotes to production with approval gates where the blast radius warrants human judgment. *Scaling automation* adjusts the quantity of running resources after they exist. A pipeline governs change to your architecture, while auto scaling governs capacity within it. Conflating them, for example by editing instance counts directly in a pipeline instead of delegating to a scaler, produces conflicts between the two systems where each system undoes the other's work. 

 A pipeline adds latency to routine changes and requires investment in tests and approval logic before it pays off. Auto scaling depends on choosing a metric that correlates with demand and on setting minimum and maximum limits that leave headroom without wasting money. Treat these parameters as decisions and review them as you would any other part of your architecture. 

 Managed scaling and load-distribution services reduce the amount of automation you build yourself. [Amazon EC2 Auto Scaling](https://docs.aws.amazon.com/autoscaling/ec2/userguide/what-is-amazon-ec2-auto-scaling.html) maintains a target number of instances, and [AWS Auto Scaling](https://docs.aws.amazon.com/autoscaling/plans/userguide/migrate-scaling-plan.html) coordinates scaling across multiple resource types from a single plan. Load balancers distribute traffic across the resources a scaler manages, so capacity added during a scale-out event receives work immediately. Defining these services inside your IaC templates keeps the scaling behavior under version control alongside the resources it governs. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Store infrastructure definitions in version control:** Create a source repository for the templates and configuration that describe your infrastructure. Commit every change so that the repository history reflects the full evolution of your environment and changes can be reviewed before they apply. 

1.  **Choose an infrastructure as code tool:** Select an IaC solution such as [AWS CloudFormation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/Welcome.html) to declare your resources and detect drift from the intended state. Define your components, such as networks, compute groups, and databases, within these templates. 

1.  **Deploy infrastructure through a pipeline:** Integrate your IaC templates with a continuous integration and delivery pipeline using a service such as [AWS CodePipeline](https://docs.aws.amazon.com/codepipeline/latest/userguide/tutorials-four-stage-pipeline.html). Configure stages that lint and validate templates, deploy to staging, run automated tests, and promote to production, with approval gates where the change carries risk. 

1.  **Select scaling metrics that track demand:** Identify the metrics that rise and fall with your workload's demand, and collect them for the components you intend to scale. Avoid metrics that do not correlate with demand in both directions. 

1.  **Configure automatic scaling within defined limits:** Set scale-out and scale-in policies for each scalable component, and set minimum and maximum limits that leave headroom for bursts. Use scheduled scaling for demand that follows a known calendar pattern. 

1.  **Monitor deployments and enable rollback:** Watch pipeline deployments for failures and regressions, and configure rollback in your pipeline so a bad change reverts to the last known-good state without manual reconstruction. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [REL07-BP02 Obtain resources upon detection of impairment to a workload](rel07-bp02.md) 
+  [REL07-BP03 Obtain resources upon detection that more resources are needed for a workload](rel07-bp03.md) 
+  [REL08-BP05 Deploy changes with automation](rel08-bp05.md) 
+  [REL08-BP04 Deploy using immutable infrastructure](rel08-bp04.md) 

 **Related documents:** 
+  [Migrate your scaling plan](https://docs.aws.amazon.com/autoscaling/plans/userguide/migrate-scaling-plan.html) 
+  [How scaling plans work](https://docs.aws.amazon.com/autoscaling/plans/userguide/how-it-works.html) 
+  [What is Amazon EC2 Auto Scaling?](https://docs.aws.amazon.com/autoscaling/ec2/userguide/what-is-amazon-ec2-auto-scaling.html) 
+  [Managing throughput capacity automatically with DynamoDB auto scaling](https://docs.aws.amazon.com/amazondynamodb/latest/developerguide/AutoScaling.html) 
+  [Use Elastic Load Balancing to distribute incoming application traffic in your Auto Scaling group](https://docs.aws.amazon.com/autoscaling/ec2/userguide/autoscaling-load-balancer.html) 
+  [What is Elastic Load Balancing?](https://docs.aws.amazon.com/elasticloadbalancing/latest/userguide/what-is-load-balancing.html) 
+  [What is an Application Load Balancer?](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/introduction.html) 
+  [What is a Network Load Balancer?](https://docs.aws.amazon.com/elasticloadbalancing/latest/network/introduction.html) 
+  [Tutorial: Create a four-stage pipeline](https://docs.aws.amazon.com/codepipeline/latest/userguide/tutorials-four-stage-pipeline.html) 

 **Related videos:** 
+  [Enable Cross-Account Observability in Amazon CloudWatch \| Amazon Web Services](https://www.youtube.com/watch?v=lUaDO9dqISc) 

 **Related examples:** 
+  [Integrating with GitHub Actions – CI/CD pipeline to deploy a Web App to Amazon EC2](https://aws.amazon.com/blogs/devops/integrating-with-github-actions-ci-cd-pipeline-to-deploy-a-web-app-to-amazon-ec2) 
+  [AWS Marketplace: products that can be used with auto scaling](https://aws.amazon.com/marketplace/search/results?searchTerms=Auto+Scaling) 