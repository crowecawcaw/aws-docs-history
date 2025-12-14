**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console.
For more details, see [Working with the console](working-with-console.md "working-with-console.md").

# Monitoring AWS WAF, AWS Firewall Manager, and AWS Shield Advanced

Monitoring is an important part of maintaining the reliability, availability, and
performance of your services.

###### Note

For information about monitoring your Shield Advanced resources and identifying possible DDoS events
using Shield Advanced, see [AWS Shield](shield-chapter.md "shield-chapter.md").

As you start monitoring these services, you should create a monitoring plan
that includes answers to the following questions:

- What are your monitoring goals?
- What resources will you monitor?
- How often will you monitor these resources?
- What monitoring tools will you use?
- Who will perform the monitoring tasks?
- Who should be notified when something goes wrong?
  The next step is to establish a baseline for normal performance in your environment, by measuring performance at various times and under
  different load conditions. As you monitor AWS WAF, Firewall Manager, Shield Advanced and related services, store
  historical monitoring data so that you can compare it with current performance data,
  identify normal performance patterns and performance anomalies, and devise methods to
  address issues.

For AWS WAF, you should monitor the following items at a minimum to establish a
baseline:

- The number of allowed web requests
- The number of blocked web requests

###### Topics

- [Monitoring tools](monitoring_automated_manual.md "monitoring_automated_manual.md")
- [Monitoring with Amazon CloudWatch](monitoring-cloudwatch.md "monitoring-cloudwatch.md")
- [Logging API calls with AWS CloudTrail](logging-using-cloudtrail.md "logging-using-cloudtrail.md")
