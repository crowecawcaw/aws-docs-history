

# REL12-BP03 Test scalability and performance requirements

 Scalability and performance testing validates that your workload meets its throughput, latency, and scaling targets under realistic load before customers reach the limits. 

 **Desired outcome:** 
+  Your workload holds its expected behavior under peak load, including sudden spikes and sustained high demand. 
+  You have clear, measurable performance requirements for response time, throughput, and scaling. 
+  Your test environment closely mirrors production, so results predict real behavior. 
+  Load tests run as part of your delivery pipeline, catching performance regressions before release. 

 **Common anti-patterns:** 
+  Teams test against environments that do not match production in size or configuration. 
+  Load testing is a one-time activity rather than part of the delivery pipeline. 
+  Performance requirements are undefined, so tests have no pass or fail criteria. 
+  Test scenarios use unrealistic load and never exercise peak, spike, or sustained conditions. 
+  Teams never exceed expected load, so they never find the breaking point. 
+  Monitoring and alerting are too thin to track performance metrics or detect anomalies. 

 **Benefits of establishing this best practice:** 
+  Bottlenecks surface before production, where they are cheaper to fix. 
+  Measured resource requirements prevent both over-provisioning and under-provisioning. 
+  Observed behavior under stress reveals failure points and informs fault-tolerance design. 
+  Detailed performance data speeds incident diagnosis when issues do reach production. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance"></a>

 Start from service-level objectives (SLOs). An SLO states a target for a measurable output such as throughput, a latency percentile, or an error rate. Derive each target from business need and user expectation. SLOs give every load test a clear pass or fail outcome and set the target that scaling and performance work must satisfy. 

 A test environment one-tenth the size of production predicts production behavior poorly, because contention, connection limits, and scaling thresholds do not scale linearly. Provision a production-scale environment on demand and tear it down after the test to get accurate results without permanent cost. Infrastructure as code and container-based deployment make these environments reproducible, so each test run exercises the same configuration. 

 Cover average usage, sudden spikes, and sustained peaks, then add stress testing that deliberately exceeds expected load. Stress testing is where you find the breaking point: the load at which response time degrades, resources exhaust, or components fail. Once you know the breaking point, you can set scaling policies and capacity plans against real limits. This is also where scaling settings, service quotas, and resilience mechanisms prove they work together under pressure. 

 Workloads change, traffic patterns shift, and a configuration that scaled last quarter can regress after a release. Add load tests to your delivery pipeline to catch regressions early. Continuous production monitoring feeds real usage data back into the test suite. Analyze that data regularly to refine scenarios, validate new scaling strategies, and keep the tests representative of how the workload is used. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Define measurable performance requirements:** Set targets for response time, throughput, and scalability based on usage patterns, user expectations, and business need. Express them as SLOs so every test has a clear pass or fail result. 

1.  **Select and configure a load testing tool:** Choose a tool that reproduces the load patterns and user behavior of your production environment. Configure it to generate realistic traffic across the scenarios you plan to test. 

1.  **Build a production-like test environment:** Provision an environment that matches production in infrastructure and configuration. Use [infrastructure as code](https://docs.aws.amazon.com/prescriptive-guidance/latest/agentic-ai-serverless/infrastructure-as-code.html) and container-based deployment to make the environment reproducible and to scale it to production levels on demand. 

1.  **Create a test suite and integrate it into the pipeline:** Cover average usage, peak loads, rapid spikes, and sustained high load. Add the suite to your continuous integration and deployment pipeline so performance regressions are caught early rather than in production. 

1.  **Run load and stress tests:** Simulate real-world traffic to observe behavior under normal conditions, then exceed expected load to find the breaking point. Increase load incrementally to measure scaling limits and inform capacity plans. Watch for response-time degradation, resource exhaustion, and component failures. 

1.  **Monitor performance and alert on anomalies:** Track key performance metrics during every test and in production. Configure alerts that fire when thresholds are exceeded and that can initiate scaling actions or notify responders. 

1.  **Analyze results and iterate:** Review performance data to find emerging issues and areas to optimize. Refine test scenarios and scaling strategies with each cycle so the workload adapts to changing demand. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [REL07-BP04 Load test your workload](rel07-bp04.md) 
+  [REL06-BP01 Monitor all components for the workload (Generation)](rel06-bp01.md) 
+  [REL06-BP03 Send notifications with real-time processing and alarming](rel06-bp03.md) 
+  [REL01-BP04 Monitor and manage quotas](rel01-bp04.md) 

 **Related documents:** 
+  [Load testing applications](https://docs.aws.amazon.com/prescriptive-guidance/latest/load-testing/introduction.html) 
+  [Distributed Load Testing on AWS](https://docs.aws.amazon.com/solutions/distributed-load-testing-on-aws/) 
+  [What is APM? - Application Performance Monitoring Explained](https://aws.amazon.com/what-is/application-performance-monitoring/) 
+  [Amazon EC2 Testing Policy](https://aws.amazon.com/ec2/testing/) 

 **Related examples:** 
+  [GitHub - aws-solutions/distributed-load-testing-on-aws: Distributed Load Testing on AWS automates performance testing at scale, demonstrating how systems behave under different load conditions and helping identify potential performance issues throughout their lifecycle.](https://github.com/aws-solutions/distributed-load-testing-on-aws) 

 **Related tools:** 
+  [Application Signals](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-Application-Monitoring-Sections.html) 
+  [CloudWatch RUM](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-RUM.html) 
+  [Apache JMeter - Apache JMeter™](https://jmeter.apache.org/) 
+  [k6](https://k6.io/) 
+  [GitHub - tsenart/vegeta: HTTP load testing tool and library. It's over 9000\!](https://github.com/tsenart/vegeta) 
+  [GitHub - rakyll/hey: HTTP load generator, ApacheBench (ab) replacement](https://github.com/rakyll/hey) 
+  [ab - Apache HTTP server benchmarking tool - Apache HTTP Server Version 2.4](https://httpd.apache.org/docs/2.4/programs/ab.html) 
+  [GitHub - wg/wrk: Modern HTTP benchmarking tool](https://github.com/wg/wrk) 