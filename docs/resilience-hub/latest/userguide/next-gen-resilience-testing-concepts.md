# How resilience testing works

Resilience testing uses three core concepts:

- **Test template** – A pre-configured, recommended
  test that defines which resilience capability to validate. A test template specifies the
  actions to perform, and declares the parameters it accepts.
- **Test** – A test you create by configuring a
  recommended test template for your service, including your success criteria, stop conditions,
  and other settings. Each service has one test per template. For example, an Availability Zone:
  recovery test configured for your checkout service with a 30-minute RTO (Recovery Time
  Objective).
- **Test run** – A single execution of a test. Each
  test run scopes to the current resources in your service and produces a pass or fail outcome,
  along with results and a report. You can have multiple runs of the same test. For example,
  running your Availability Zone: recovery test monthly to test recovery within your 30-minute RTO.
  When you run a resilience test, the next generation of Resilience Hub performs the following:

1. **Scopes the test** –
   Automatically includes all resources discovered in your service that apply to the test.
2. **Configures the test** – Sets up the test
   with the configuration you provide, including success alarms, stop conditions, and
   log destinations.
3. **Injects faults** – Runs AWS FIS experiments to
   inject the faults defined by the test for the period of time specified.
4. **Evaluates results** – Determines a pass or
   fail outcome based on whether your service met your success criteria during the test.
   You can review test results in the console or programmatically. A test report is generated
   for each run.
   Resilience tests are charged based on AWS FIS action-minute pricing. For details, see [AWS Fault Injection Service pricing](https://aws.amazon.com/fis/pricing/ "https://aws.amazon.com/fis/pricing/").
