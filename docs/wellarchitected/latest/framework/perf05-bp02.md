

# PERF05-BP02 Evaluate your workload performance

 Everyday performance does not predict how a workload behaves at peak traffic. Test the workload against your KPIs under realistic and stressful conditions to find where it slows or stops scaling before customers notice. 

 **Desired outcome:** 
+  You test the whole workload against defined KPIs, not individual components in isolation. 
+  Your test environment reproduces the production factors that affect performance, including configuration, scale, data distribution, quotas, and dependencies. 
+  You test at normal load, peak load, and beyond expected load to find limits and time-dependent degradation early. 
+  Your performance tests run automatically as part of the delivery pipeline and compare results against thresholds and previous baselines. 
+  For AI workloads, your pass criteria cover response quality or task success together with latency, throughput, and resource efficiency. 
+  You adjust resource configurations using test evidence instead of guesswork. 

 **Common anti-patterns:** 
+  Teams run load tests without defining the KPIs the test is meant to validate. 
+  Teams test individual parts of the workload but never exercise the whole system together. 
+  Teams test on infrastructure that does not reproduce the production factors affecting performance, so the results do not transfer. 
+  Teams test only to expected load and never beyond it, so they never see the breaking point. 
+  Teams test the workload once and do not repeat the test as the environment changes. 
+  Teams do not distinguish legitimate network stress tests from prohibited volumetric DDoS simulations or review the applicable provider testing policy. 
+  Teams test AI workloads with a fixed prompt size and score only latency, missing token-distribution, throughput, and quality regressions. 

 **Benefits of establishing this best practice:** 
+  You discover scaling limits and bottlenecks before they affect customers. 
+  You prepare realistic test data and reuse it to make results comparable over time. 
+  You anticipate the changes a growing workload will need instead of reacting to a disruption. 
+  You right-size resources from evidence and avoid both over- and under-provisioning. 
+  You gain confidence that each release still meets its performance requirements. 

 **Level of risk exposed if this best practice is not established:** Medium 

## Implementation guidance
<a name="implementation-guidance"></a>

 To trust load-test results, exercise the complete workload. Testing components in isolation does not prove that shared dependencies handle combined load. Reproduce the production factors that affect performance: compute characteristics, scaling configuration, quotas, network paths, data volume, and dependencies. Match production closely enough that differences do not invalidate conclusions about bottlenecks or capacity. Every test also needs KPIs. Without targets, results cannot show whether the workload meets its performance requirement. 

 Use more than one test type, because each reveals a different failure mode. Load tests validate expected and peak traffic. Stress tests push beyond expected capacity to identify saturation and the breaking point. Spike tests apply a sudden traffic surge to check burst scaling and recovery. Endurance tests hold load over time to expose memory leaks, connection-pool exhaustion, queue growth, and other time-dependent degradation. These tests show whether the workload degrades gracefully, fails abruptly, or scales non-linearly. 

 Run tests on synthetic or sanitized data, with sensitive and identifying fields removed, to protect customers and keep results repeatable. Data volume and distribution also shape performance: a test against a few thousand uniform records does not predict behavior on a production-sized, skewed data set. For generative AI and agentic workloads, cover the expected distribution of input and output tokens, prompt categories, retrieval sizes, tool calls, model configurations, and concurrent sessions. Evaluate response quality or task success alongside time to first token, output token throughput, end-to-end latency, throttling, errors, and cost or resource consumption per task. 

 Every deployment, dependency upgrade, and traffic-pattern shift changes the performance profile. Include evaluation in the delivery pipeline so it runs on a schedule and compares each result against previous baselines. With cloud infrastructure, you can create a representative test environment and remove it afterward. [Distributed Load Testing on AWS](https://docs.aws.amazon.com/solutions/distributed-load-testing-on-aws/) runs distributed test workers on Amazon ECS and AWS Fargate. It supports JMeter, k6, Locust, and simple HTTP tests, distributes load across Regions, and records baseline comparisons. Its optional MCP server supports AI-assisted result analysis, and its native [AWS DevOps Agent integration](https://docs.aws.amazon.com/solutions/latest/distributed-load-testing-on-aws/devops-agent-integration.html) investigates completed test runs for bottlenecks and root-cause hypotheses. 

 Review the [Amazon EC2 testing policy](https://aws.amazon.com/ec2/testing/) before high-volume network tests originating from EC2. The policy distinguishes legitimate network stress tests from volumetric DDoS simulations, which are prohibited from EC2 and governed separately. At high aggregate traffic volumes, AWS reserves the right to apply traffic engineering or shaping. Follow the current policy and DDoS Simulation Testing Policy. Not every load test requires advance notification. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Prepare representative test data:** Produce synthetic or sanitized data at production-representative volume and distribution, and remove sensitive and identifying information before the data leaves its source system. For AI workloads, include representative token lengths, prompt categories, retrieval inputs, tool paths, and expected output-quality cases. 

1.  **Define objectives and KPIs:** State which performance aspects the test evaluates and attach a target to each. Include latency percentiles, throughput, error rate, saturation point, and resource efficiency. For generative AI or agentic workloads, add time to first token, output token throughput, throttling, end-to-end task time, and response quality or task-success criteria. These targets are the pass or fail conditions the pipeline checks. 

1.  **Build a representative environment:** Reproduce the production characteristics that affect results, including compute types, autoscaling, service quotas, network paths, configuration, data size, and dependencies. Document every material difference from production and how it affects interpretation. Use on-demand infrastructure to create the environment for the test and remove it afterward. 

1.  **Configure tooling and monitoring:** Use a load testing tool matched to the workload. [Distributed Load Testing on AWS](https://docs.aws.amazon.com/solutions/distributed-load-testing-on-aws/) supports simple HTTP, JMeter, k6, and Locust tests with distributed Fargate workers, multi-Region traffic, scheduling, and baseline comparison. Instrument the workload and the test generators with [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) so a load-generator limit is not mistaken for a workload limit. 

1.  **Run scenarios across the performance envelope:** Run load tests at normal and expected peak traffic, stress tests beyond expected capacity, spike tests for sudden surges, and endurance tests for sustained behavior. Review the [Amazon EC2 testing policy](https://aws.amazon.com/ec2/testing/) for high-volume tests originating from EC2, and do not use a load test to perform a prohibited volumetric DDoS simulation. 

1.  **Analyze results, validate findings, and adjust resources:** Compare p50, p95, and p99 latency, throughput, error rate, saturation, and resource use against KPIs and previous baselines. Use DLT baseline comparison and, where configured, [AWS DevOps Agent](https://docs.aws.amazon.com/solutions/latest/distributed-load-testing-on-aws/devops-agent-integration.html) to accelerate investigation of regressions. Treat agent findings as hypotheses, verify them against telemetry, change one factor at a time, and rerun the test before accepting a remediation. 

1.  **Document, share, and iterate:** Record findings and recommendations and share them with stakeholders to support optimization decisions. Repeat the evaluation on a regular cadence and after any significant change to the workload. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [PERF05-BP01 Use monitoring solutions to understand the areas where performance is most critical](perf05-bp01.md) 
+  [PERF05-BP03 Use automation to proactively remediate performance-related issues](perf05-bp03.md) 
+  [PERF01-BP03 Derive and establish KPIs that validate adherence to your performance requirements](perf01-bp03.md) 
+  [PERF02-BP03 Configure and right-size compute resources](perf02-bp03.md) 
+  [PERF02-BP04 Scale your compute resources dynamically](perf02-bp04.md) 

 **Related documents:** 
+  [Performance Testing on AWS](https://docs.aws.amazon.com/solutions/latest/performance-testing/overview.html) 
+  [Distributed Load Testing on AWS features](https://docs.aws.amazon.com/solutions/latest/distributed-load-testing-on-aws/features.html) 
+  [Distributed Load Testing on AWS security](https://docs.aws.amazon.com/solutions/latest/distributed-load-testing-on-aws/security-1.html) 
+  [Interpreting results and taking action](https://docs.aws.amazon.com/solutions/latest/performance-testing/interpreting-results.html) 
+  [AWS DevOps Agent integration](https://docs.aws.amazon.com/solutions/latest/distributed-load-testing-on-aws/devops-agent-integration.html) 
+  [Amazon EC2 testing policy](https://aws.amazon.com/ec2/testing/) 
+  [Benchmarking customized models on Amazon Bedrock using LLMPerf and LiteLLM](https://aws.amazon.com/blogs/machine-learning/benchmarking-customized-models-on-amazon-bedrock-using-llmperf-and-litellm/) 
+  [Generative AI Lens: Performance efficiency](https://docs.aws.amazon.com/wellarchitected/latest/generative-ai-lens/performance-efficiency.html) 

 **Related videos:** 
+  [AWS re:Invent 2025 - Building for Efficiency & Reliability with Performance Testing on AWS](https://www.youtube.com/watch?v=tyjc6Mknacc) 
+  [AWS re:Invent 2025 - Maximizing EC2 Performance: A Hands-on Guide to Instance Optimization](https://www.youtube.com/watch?v=mSrDZuxWFtw&t=1102s) 
+  [AWS Summit ANZ 2023 - Accelerate with confidence through AWS Distributed Load Testing](https://www.youtube.com/watch?v=4J6lVqa6Yh8) 

 **Related examples:** 
+  [Distributed Load Testing on AWS source](https://github.com/aws-solutions/distributed-load-testing-on-aws) 
+  [Testing big projects using Distributed Load Testing on AWS with Sony Music Solutions](https://aws.amazon.com/solutions/case-studies/sony-music-solutions-inc-case-study/) 
+  [Performance Testing on AWS journey](https://docs.aws.amazon.com/solutions/latest/performance-testing/overview.html) 
+  [Benchmarking customized models on Amazon Bedrock using LLMPerf and LiteLLM](https://aws.amazon.com/blogs/machine-learning/benchmarking-customized-models-on-amazon-bedrock-using-llmperf-and-litellm/) 

 **Related services:** 
+  [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/) 
+  [Amazon EC2](https://aws.amazon.com/ec2/) 
+  [Amazon ECS](https://aws.amazon.com/ecs/) 
+  [AWS Fargate](https://aws.amazon.com/fargate/) 
+  [AWS DevOps Agent](https://aws.amazon.com/devops-agent/) 
+  [Amazon Bedrock](https://aws.amazon.com/bedrock/) 