

# REL07-BP04 Load test your workload

 A load test drives representative traffic at a workload until something breaks, which reveals where capacity runs out and which metric warns you first. Without this evidence, you discover your limits during a real peak. 

 **Desired outcome:** 
+  You know which component fails first under load and at what level of demand it fails. 
+  You have identified the metrics that signal an approaching limit in time to act on them. 
+  Load tests run against an environment that matches production in configuration and scale. 
+  You re-test as demand grows, so the workload is validated against current and projected traffic, not only its launch profile. 

 **Common anti-patterns:** 
+  Teams load test against an environment that does not match the production configuration. 
+  Teams test individual components in isolation and never test the workload as a whole. 
+  Test traffic uses a narrow set of requests rather than a representative mix of real ones. 
+  Tests stop at a small margin above expected load and never find the breaking point. 
+  Load testing happens once at project start and is never repeated as demand grows. 
+  Teams never check whether throughput degrades gradually or collapses once load passes the workload's limit. 

 **Benefits of establishing this best practice:** 
+  You learn the failure points of your architecture before customers do, and you know which metrics warn of them. 
+  Scaling decisions become proactive because you can see a limit approaching rather than reacting after it is reached. 
+  Confidence in capacity plans is grounded in measured behavior rather than estimates. 
+  Recurring tests confirm the workload can meet future growth targets as demand increases. 

 **Level of risk exposed if this best practice is not established:** Medium 

## Implementation guidance
<a name="implementation-guidance"></a>

 A load test finds the breaking point and characterizes behavior on the way to it. Sustained load, held long enough to expose resource leaks and queue buildup, matters more than a brief spike that a warm system absorbs. In the cloud, you can create a production-scale test environment on demand, run the test, and decommission it, paying only for the hours it runs. 

 A test against an environment that differs from production, in instance types, configuration, or scale, measures a system you do not run. Testing a single component in isolation misses interactions that fail under load. A shared database or downstream dependency may saturate before the component under test does. Representative traffic matters. A workload rarely receives one kind of request, and the mix shifts across the day. A test built from one request type can pass while production fails on a mix it never exercised. Sample the request mix across several time windows to capture that variation. 

 You can also load test in production as a game day. During a period of low customer usage, stress the live system, with the responsible people present to interpret results and address problems as they surface. This tests the real environment with no fidelity gap, but risks live traffic, so plan and staff carefully. 

 Watch how the workload fails once it passes its limit. Throughput that falls toward zero while compute sits idle often indicates a retry feedback loop. Client timeouts trigger retries, and the retries occupy the worker threads or connections that should serve live requests. Set connection and worker limits with your client timeout in mind, and confirm that excess requests are rejected quickly instead of queued. For mitigations, see [REL05-BP03 Control and limit retry calls](rel05-bp03.md), [REL05-BP04 Fail fast and limit queues](rel05-bp04.md), and [REL05-BP05 Set client timeouts](rel05-bp05.md). 

 Demand grows, architectures change, and a limit that had headroom above traffic at launch can move into range as usage climbs. Re-test on a cadence and against projected growth targets, not only current load. 

### Implementation steps
<a name="implementation-steps"></a>

1.  **Identify the request mix:** Analyze production traffic across several time windows to build a representative mix of requests, because the mix shifts over time and a single snapshot misrepresents real load. Use this mix as the basis for the test traffic. 

1.  **Implement a load driver:** Choose custom code, open-source, or commercial tooling to generate the load. A managed option such as [Distributed Load Testing on AWS](https://docs.aws.amazon.com/solutions/distributed-load-testing-on-aws/) can simulate thousands of connected users without you operating the test fleet. 

1.  **Test at small capacity first:** Drive load against a small footprint, possibly a single instance or container, to observe immediate effects and confirm the test harness and instrumentation behave as expected. 

1.  **Test at production scale:** Run the test against an environment that matches production in configuration and scale, because a distributed system behaves differently under distributed load than a single node does. Test the entire workload, not isolated components. 

1.  **Increase load until the breaking point:** Raise demand while watching your instrumented metrics, and continue past expected peak until a component fails. Record which component fails first and which metric signaled the limit ahead of the failure. Keep increasing load after the first degradation to see whether throughput falls gradually or collapses. For a structured approach, see [AWS Prescriptive Guidance: load testing applications](https://docs.aws.amazon.com/prescriptive-guidance/latest/load-testing/). 

1.  **Re-test as demand grows:** Repeat the tests on a cadence and against projected growth targets, so the workload is validated for future demand rather than only the load it saw at launch. 

## Resources
<a name="resources"></a>

 **Related best practices:** 
+  [REL07-BP03 Obtain resources upon detection that more resources are needed for a workload](rel07-bp03.md) 
+  [REL12-BP03 Test scalability and performance requirements](rel12-bp03.md) 
+  [REL07-BP01 Use automation when obtaining or scaling resources](rel07-bp01.md) 
+  [REL05-BP03 Control and limit retry calls](rel05-bp03.md) 
+  [REL05-BP04 Fail fast and limit queues](rel05-bp04.md) 
+  [REL05-BP05 Set client timeouts](rel05-bp05.md) 

 **Related documents:** 
+  [Distributed Load Testing on AWS: simulate thousands of connected users](https://docs.aws.amazon.com/solutions/distributed-load-testing-on-aws/) 
+  [AWS Prescriptive Guidance: load testing applications](https://docs.aws.amazon.com/prescriptive-guidance/latest/load-testing/introduction.html) 

 **Related videos:** 
+  [AWS re:Invent 2024 - How Netflix handles sudden load spikes in the cloud (NFX301)](https://www.youtube.com/watch?v=TkFyZyxFRBM) 