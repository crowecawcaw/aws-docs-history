# Resilience in Amazon SNS

Resilience in Amazon SNS is ensured through leveraging the AWS global
infrastructure, which revolves around AWS Regions and Availability Zones. AWS Regions offer
physically separated and isolated Availability Zones connected by low-latency, high-throughput,
and highly redundant networking. This architecture allows for seamless failover between
Availability Zones without interruption, making applications and databases inherently more fault
tolerant and scalable compared to traditional data center infrastructures. By using Availability
Zones, Amazon SNS subscribers benefit from enhanced availability and reliability, guaranteeing
message delivery despite potential disruptions. For more information about AWS Regions and
Availability Zones, see [AWS
Global Infrastructure](https://aws.amazon.com/about-aws/global-infrastructure/ "https://aws.amazon.com/about-aws/global-infrastructure/").

Additionally, subscriptions to Amazon SNS topics can be configured with delivery retries and
dead-letter queues, enabling automatic handling of transient failures and ensuring messages
reliably reach their intended destinations.

Amazon SNS also supports message filtering and message attributes, which lets you tailor
resilience strategies to their specific use cases, enhancing the overall robustness of your
applications.
