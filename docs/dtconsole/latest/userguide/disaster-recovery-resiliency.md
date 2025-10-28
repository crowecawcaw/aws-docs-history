# Resilience in AWS CodeStar Notifications and AWS CodeConnections

The AWS global infrastructure is built around AWS Regions and Availability Zones.
AWS Regions provide multiple physically separated and isolated Availability Zones, which
are connected with low-latency, high-throughput, and highly redundant networking. With
Availability Zones, you can design and operate applications and databases that automatically
fail over between Availability Zones without interruption. Availability Zones are more
highly available, fault tolerant, and scalable than traditional single or multiple data
center infrastructures.

For more information about AWS Regions and Availability Zones, see [AWS global
infrastructure](https://aws.amazon.com/about-aws/global-infrastructure/ "https://aws.amazon.com/about-aws/global-infrastructure/").

- Notification rules are specific to the AWS Region where they are created. If you
  have notification rules in more than one AWS Region, use the Region selector to
  review notification rules in each AWS Region.
- AWS CodeStar Notifications relies on Amazon Simple Notification Service (Amazon SNS) topics as notification rule targets. Information
  about your Amazon SNS topics and notification rule targets might be stored in an AWS
  Region different from the Region in which you configured the notification
  rule.
