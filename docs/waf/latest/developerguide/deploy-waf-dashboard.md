**Introducing a new console experience for AWS WAF**

You can now use the updated experience to access AWS WAF functionality anywhere in the console.
For more details, see [Working with the console](working-with-console.md "working-with-console.md").

# Creating a DDoS dashboard in CloudWatch and setting CloudWatch alarms

This page provides instructions for creating a DDoS dashboard in CloudWatch and setting CloudWatch alarms.

You can monitor potential DDoS activity using Amazon CloudWatch, which collects raw data from
Shield Advanced and processes it into readable, near real-time metrics. You can use statistics
in CloudWatch to gain a perspective on how your web application or service is performing. For
more information about using CloudWatch, see [What is CloudWatch](../../../AmazonCloudWatch/latest/DeveloperGuide/WhatIsCloudWatch.md "../../../AmazonCloudWatch/latest/DeveloperGuide/WhatIsCloudWatch.md") in the _Amazon CloudWatch User Guide_.

- For instructions for creating a CloudWatch dashboard, see [Monitoring with Amazon CloudWatch](monitoring-cloudwatch.md "monitoring-cloudwatch.md").
- For descriptions of the Shield Advanced metrics that you can add to your dashboard, see [AWS Shield Advanced metrics](shield-metrics.md "shield-metrics.md").
  Shield Advanced reports resource metrics to CloudWatch more frequently during DDoS events than
  while no events are underway. Shield Advanced reports metrics once a minute during an event,
  and then once right after the event ends. While no events are underway, Shield Advanced reports
  metrics once a day, at a time assigned to the resource. This periodic report keeps the
  metrics active and available for use in your custom CloudWatch alarms.

This completes the tutorial for getting started with Shield Advanced. To take full advantage
of the protections you've chosen, continue exploring the features and options of
Shield Advanced. To start, familiarize yourself with your options for viewing and responding to
events at [Visibility into DDoS events with Shield Advanced](ddos-viewing-events.md "ddos-viewing-events.md") and
[Responding to DDoS events in AWS](ddos-responding.md "ddos-responding.md").
