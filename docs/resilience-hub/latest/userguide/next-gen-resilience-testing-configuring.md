

# Configuring a test
<a name="next-gen-resilience-testing-configuring"></a>

When you create a test from a template, you configure the following settings. Settings are saved and reused for future runs – you can edit them at any time.

**Test duration**  
The length of time the test actions run. For recovery tests (**Availability Zone: recovery** and **Multi-Region: recovery**), the default duration is your RTO plus 30 minutes, giving your service time to recover and confirming that it sustains. For sustained tests, the default is 30 minutes for **Dependency validation** or 3 hours for **Multi-Region: isolation**. These defaults apply in the console; when using the API, you provide the duration explicitly.

**Fault scope**  
Defines where faults are injected – the Availability Zone or Regions to impair. Each test has its own parameters. For details, see [Available tests](next-gen-resilience-testing-available-tests.md).

**Test actions**  
Read-only. Defined by the test template. Shows the fault actions and their target resource types. If no resources match an action's target type, that action is skipped.

**Dependencies to block**  
Dependencies to block during the test. Select from discovered dependencies (if dependency discovery is enabled) or enter dependencies manually by DNS domain name. Required for some tests, optional for others. For defaults and requirements, see [Available tests](next-gen-resilience-testing-available-tests.md).

**Test alarms**  
**Success alarms** (required) – CloudWatch alarms that determine success criteria pass or fail. At least one is required. If you select multiple, all must pass for the test to pass. Choose alarms that measure your service's overall health.  
How the test passes:  
+ **Availability Zone: recovery** – all success alarms must return to `OK` state within your Multi-AZ RTO and remain there until the test actions end.
+ **Multi-Region: recovery** – all success alarms must return to `OK` state within your Multi-Region RTO and remain there until the test actions end.
+ **Dependency validation** – all success alarms remain in `OK` state until the test actions end.
+ **Multi-Region: isolation** – all success alarms remain in `OK` state until the test actions end.
**Additional alarms** (optional) – For observability only. Shown in the results and report but do not affect the pass or fail outcome.

**Region switch plan** (**Multi-Region: recovery** only, optional)  
Attaching an AWS Application Recovery Controller (ARC) Region Switch plan lets the next generation of Resilience Hub include the failover timeline in your test results and report. Optional; leave empty if you use manual failover or a custom automation.

**Additional settings** (optional)    
**Stop conditions**  
CloudWatch alarms that automatically stop the test if they breach their threshold. Use stop conditions as guardrails to protect your workloads during testing. For example, create a CloudWatch alarm on a critical business metric (such as latency or error rate) that stops the test if it exceeds an unacceptable threshold. Stop condition alarms must be in the account where the test runs and the Region where the faults are injected. For more information, see [Stop conditions for AWS FIS](https://docs.aws.amazon.com/fis/latest/userguide/stop-conditions.html).  
**Reports**  
A report is automatically generated after each test run when a report destination (Amazon S3 bucket) is configured on your service. Reports include the test configuration, alarm status, timeline, and pass or fail results. Test reports are included at no additional cost when you use the next generation of Resilience Hub resilience testing. To configure a report destination, see your service's reporting settings.  
**Logs**  
Send detailed test logs to Amazon S3, CloudWatch Logs, or both. Logs capture timestamped events, including action start and end, target resolution, and errors. Use logs to debug failed tests or to understand the sequence of fault injection. Logging requires additional permissions on your test execution role. For more information, see [Experiment logging for AWS FIS](https://docs.aws.amazon.com/fis/latest/userguide/monitoring-logging.html).

**Test permissions**  
An IAM execution role is required. Permissions vary based on the test type, fault actions, and options selected. For multi-account tests, use the same-named role in each account. For more information, see [IAM execution roles for resilience testing](next-gen-resilience-testing-iam.md).