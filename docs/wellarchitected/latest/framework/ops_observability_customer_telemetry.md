# OPS04-BP03 Implement user experience telemetry

Gaining deep insights into customer experiences and interactions with your application is crucial. Real user monitoring (RUM) and synthetic transactions serve as powerful tools for this purpose. RUM provides data about real user interactions granting an unfiltered perspective of user satisfaction, while synthetic transactions simulate user interactions, helping in detecting potential issues even before they impact real users.

**Desired outcome:** A holistic view of the customer experience, proactive detection of issues, and optimization of user interactions to deliver seamless digital experiences.

**Common anti-patterns:**

- Applications without real user monitoring (RUM):
  - Delayed issue detection: Without RUM, you might not become aware of performance bottlenecks or issues until users complain. This reactive approach can lead to customer dissatisfaction.
  - Lack of user experience insights: Not using RUM means you lose out on crucial data that shows how real users interact with your application, limiting your ability to optimize the user experience.

- Applications without synthetic transactions:
  - Missed edge cases: Synthetic transactions help you test paths and functions that might not be frequently used by typical users but are critical to certain business functions. Without them, these paths could malfunction and go unnoticed.
  - Checking for issues when the application is not being used: Regular synthetic testing can simulate times when real users aren't actively interacting with your application, ensuring the system always functions correctly.

**Benefits of establishing this best
practice:**

- Proactive issue detection: Identify and address potential issues before they impact real users.
- Optimized user experience: Continuous feedback from RUM aids in refining and enhancing the overall user experience.
- Insights on device and browser performance: Understand how your application performs across various devices and browsers, enabling further optimization.
- Validated business workflows: Regular synthetic transactions ensure that core functionalities and critical paths remain operational and efficient.
- Enhanced application performance: Leverage insights gathered from real user data to improve application responsiveness and reliability.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

To leverage RUM and synthetic transactions for user activity telemetry, AWS offers services like [Amazon CloudWatch RUM](../../../AmazonCloudWatch/latest/monitoring/CloudWatch-RUM.md "../../../AmazonCloudWatch/latest/monitoring/CloudWatch-RUM.md") and [Amazon CloudWatch Synthetics](../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries.md "../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries.md"). Metrics, logs, and traces, coupled with user activity data, provide a comprehensive view of both the application's operational state and the user experience.

### Implementation steps

1. **Deploy Amazon CloudWatch RUM:** Integrate your application with CloudWatch RUM to collect, analyze, and present real user data.
   1. Use the [CloudWatch RUM JavaScript library](../../../AmazonCloudWatch/latest/monitoring/CloudWatch-RUM.md "../../../AmazonCloudWatch/latest/monitoring/CloudWatch-RUM.md") to integrate RUM with your application.
   2. Set up dashboards to visualize and monitor real user data.

2. **Configure CloudWatch Synthetics:** Create canaries, or scripted routines, that simulate user interactions with your application.
   1. Define critical application workflows and paths.
   2. Design canaries using [CloudWatch Synthetics scripts](../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries.md "../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries.md") to simulate user interactions for these paths.
   3. Schedule and monitor canaries to run at specified intervals, ensuring consistent performance checks.

3. **Analyze and act on data:** Utilize data from RUM and synthetic transactions to gain insights and take corrective measures when anomalies are detected. Use CloudWatch dashboards and alarms to stay informed.

**Level of effort for the implementation plan:** Medium

## Resources

**Related best practices:**

- [OPS04-BP01 Identify key performance indicators](ops_observability_identify_kpis.md "ops_observability_identify_kpis.md")
- [OPS04-BP02 Implement application telemetry](ops_observability_application_telemetry.md "ops_observability_application_telemetry.md")
- [OPS04-BP04 Implement dependency telemetry](ops_observability_dependency_telemetry.md "ops_observability_dependency_telemetry.md")
- [OPS04-BP05 Implement distributed tracing](ops_observability_dist_trace.md "ops_observability_dist_trace.md")

**Related documents:**

- [Amazon CloudWatch RUM Guide](../../../AmazonCloudWatch/latest/monitoring/CloudWatch-RUM.md "../../../AmazonCloudWatch/latest/monitoring/CloudWatch-RUM.md")
- [Amazon CloudWatch Synthetics Guide](../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries.md "../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Synthetics_Canaries.md")

**Related videos:**

- [Optimize applications through end user insights with Amazon CloudWatch RUM](https://www.youtube.com/watch?v=NMaeujY9A9Y "https://www.youtube.com/watch?v=NMaeujY9A9Y")
- [AWS on Air ft. Real-User Monitoring for Amazon CloudWatch](https://www.youtube.com/watch?v=r6wFtozsiVE "https://www.youtube.com/watch?v=r6wFtozsiVE")

**Related examples:**

- [One Observability Workshop](https://catalog.workshops.aws/observability/en-US/intro "https://catalog.workshops.aws/observability/en-US/intro")
- [Git Repository for Amazon CloudWatch RUM Web Client](https://github.com/aws-observability/aws-rum-web "https://github.com/aws-observability/aws-rum-web")
- [Using Amazon CloudWatch Synthetics to measure page load time](https://github.com/aws-samples/amazon-cloudwatch-synthetics-page-performance "https://github.com/aws-samples/amazon-cloudwatch-synthetics-page-performance")
