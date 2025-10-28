# Process and culture

When architecting workloads, there are principles and practices that
you can adopt to help you better run efficient high-performing cloud
workloads. To adopt a culture that fosters performance efficiency of
cloud workloads, consider these key principles and practices.

Consider these key principles to build this culture:

- **Infrastructure as code:**
  Define your infrastructure as code using approaches such as AWS CloudFormation templates. The use of templates allows you to
  place your infrastructure into source control alongside your
  application code and configurations. This allows you to apply
  the same practices you use to develop software in your
  infrastructure so you can iterate rapidly.
- **Deployment pipeline:** Use a
  continuous integration/continuous deployment (CI/CD) pipeline
  (for example, source code repository, build systems, deployment,
  and testing automation) to deploy your infrastructure. This
  allows you to deploy in a repeatable, consistent, and low-cost
  fashion as you iterate.
- **Well-defined metrics:** Set up
  and monitor metrics to capture key performance indicators
  (KPIs). We recommend that you use both technical and business
  metrics. For websites or mobile apps, key metrics are capturing
  time-to-first-byte or rendering. Other generally applicable
  metrics include thread count, garbage collection rate, and wait
  states. Business metrics, such as the aggregate cumulative cost
  per request, can alert you to ways to drive down costs.
  Carefully consider how you plan to interpret metrics. For
  example, you could choose the maximum or 99th percentile instead
  of the average.
- **Performance test
  automatically:** As part of your deployment process,
  automatically start performance tests after the quicker running
  tests have passed successfully. The automation should create a
  new environment, set up initial conditions such as test data,
  and then run a series of benchmarks and load tests. Results from
  these tests should be tied back to the build so you can track
  performance changes over time. For long-running tests, you can
  make this part of the pipeline asynchronous from the rest of the
  build. Alternatively, you could run performance tests overnight
  using Amazon EC2 Spot Instances.
- **Load generation:** You should
  create a series of test scripts that replicate synthetic or
  prerecorded user journeys. These scripts should be idempotent
  and not coupled, and you might need to include _pre-warming_
  scripts to yield valid results. As much as possible, your test
  scripts should replicate the behavior of usage in production.
  You can use software or software-as-a-service (SaaS) solutions
  to generate the load. Consider using [AWS Marketplace](https://aws.amazon.com/marketplace/ "https://aws.amazon.com/marketplace/") solutions
  and [Spot Instances](../../../AWSEC2/latest/UserGuide/using-spot-instances.md "../../../AWSEC2/latest/UserGuide/using-spot-instances.md") — they can be cost-effective ways to generate
  the load.
- **Performance visibility:** Key
  metrics should be visible to your team, especially metrics
  against each build version. This allows you to see any
  significant positive or negative trend over time. You should
  also display metrics on the number of errors or exceptions to
  make sure you are testing a working system.
- **Visualization:** Use visualization techniques that make it clear where performance issues, hot spots, wait states, or low utilization is occurring. Overlay performance metrics over architecture diagrams — call graphs or code can help identify issues quickly.
- **Regular review process:** Architectures performing poorly is usually the result of a non-existent or broken performance review process. If your architecture is performing poorly, implementing a performance review process allows you to drive iterative improvement.
- **Continual optimization:** Adopt a culture to continually optimize the performance efficiency of your cloud workload.
  The following question focuses on these considerations for performance efficiency.

| PERF 5:  What process do you use to support more performance efficiency for your workload?
|
| --- |
| When architecting workloads, there are principles and practices that you can adopt to help you better run efficient high-performing cloud workloads. To adopt a culture that fosters performance efficiency of cloud workloads, consider these key principles and practices. |
