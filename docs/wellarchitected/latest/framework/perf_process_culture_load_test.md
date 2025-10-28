# PERF05-BP04 Load test your workload

Load test your workload to verify it can handle production load and
identify any performance bottleneck.

**Common anti-patterns:**

- You load test individual parts of your workload but not your
  entire workload.
- You load test on infrastructure that is not the same as your
  production environment.
- You only conduct load testing to your expected load and not
  beyond, to help foresee where you may have future problems.
- You perform load testing without consulting the [Amazon EC2 Testing Policy](https://aws.amazon.com/ec2/testing/ "https://aws.amazon.com/ec2/testing/") and submitting a Simulated Event Submissions Form. This results in your test failing to run, as it looks like a denial-of-service event.

**Benefits of establishing this best
practice:** Measuring your performance under a load test
will show you where you will be impacted as load increases. This can
provide you with the capability of anticipating needed changes
before they impact your workload.

**Level of risk exposed if this best practice
is not established:** Low

## Implementation guidance

Load testing in the cloud is a process to measure the performance
of cloud workload under realistic conditions with expected user
load. This process involves provisioning a production-like cloud
environment, using load testing tools to generate load, and
analyzing metrics to assess the ability of your workload handling
a realistic load. Load tests must be run using synthetic or
sanitized versions of production data (remove sensitive or
identifying information). Automatically carry out load tests as
part of your delivery pipeline, and compare the results against
pre-defined KPIs and thresholds. This process helps you continue
to achieve required performance.

### Implementation steps

- **Define your testing objectives:** Identify the performance aspects of your workload that you want to evaluate, such as throughput and response time.
- **Select a testing tool:** Choose and configure the load testing tool that suits your workload.
- **Set up your environment:**
  Set up the test environment based on your production
  environment. You can use AWS services to run
  production-scale environments to test your architecture.
- **Implement monitoring:** Use monitoring tools such as [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/ "https://aws.amazon.com/cloudwatch/") to collect metrics across the resources in your architecture. You can also collect and publish custom metrics.
- **Define scenarios:**
  Define the load testing scenarios and parameters (like test
  duration and number of users).
- **Conduct load testing:**
  Perform test scenarios at scale. Take advantage of the AWS Cloud to test your workload to discover where it fails to
  scale, or if it scales in a non-linear way. For example, use
  Spot Instances to generate loads at low cost and discover
  bottlenecks before they are experienced in production.
- **Analyze test results:**
  Analyze the results to identify performance bottlenecks and
  areas for improvements.
- **Document and share findings:**
  Document and report on findings and recommendations. Share this information with stakeholders to help them make informed decision regarding performance optimization strategies.
- **Continually iterate:** Load testing should be performed at regular cadence, especially after a system change of update.

## Resources

**Related documents:**

- [Amazon CloudWatch RUM](../../../AmazonCloudWatch/latest/monitoring/CloudWatch-RUM.md "../../../AmazonCloudWatch/latest/monitoring/CloudWatch-RUM.md")
- [Amazon CloudWatch Synthetics](../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries.md "../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries.md")
- [Distributed
  Load Testing on AWS](../../../solutions/latest/distributed-load-testing-on-aws/welcome.md "../../../solutions/latest/distributed-load-testing-on-aws/welcome.md")

**Related videos:**

- [AWS Summit ANZ 2023: Accelerate with confidence through AWS Distributed Load Testing](https://www.youtube.com/watch?v=4J6lVqa6Yh8 "https://www.youtube.com/watch?v=4J6lVqa6Yh8")
- [AWS re:Invent 2022 - Scaling on AWS for your first 10 million users](https://www.youtube.com/watch?v=yrP3M4_13QM "https://www.youtube.com/watch?v=yrP3M4_13QM")
- [Solving
  with AWS Solutions: Distributed Load Testing](https://www.youtube.com/watch?v=Y-2rk0sSyOM "https://www.youtube.com/watch?v=Y-2rk0sSyOM")

- [AWS re:Invent 2021 - Optimize applications through end user insights with Amazon CloudWatch RUM](https://www.youtube.com/watch?v=NMaeujY9A9Y "https://www.youtube.com/watch?v=NMaeujY9A9Y")
- [Demo
  of Amazon CloudWatch Synthetics](https://www.youtube.com/watch?v=hF3NM9j-u7I "https://www.youtube.com/watch?v=hF3NM9j-u7I")

**Related examples:**

- [Distributed
  Load Testing on AWS](https://aws.amazon.com/solutions/implementations/distributed-load-testing-on-aws/ "https://aws.amazon.com/solutions/implementations/distributed-load-testing-on-aws/")
