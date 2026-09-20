

# Resilience in Amazon SNS
<a name="disaster-recovery-resiliency"></a>

Resilience in Amazon SNS is ensured through the AWS global infrastructure. AWS Regions contain physically separated and isolated Availability Zones connected by low-latency, high-throughput, and highly redundant networking. This architecture supports seamless failover between Availability Zones without interruption. As a result, applications and databases are more fault tolerant and scalable than traditional data center infrastructures. Amazon SNS subscribers benefit from this design through enhanced availability and reliable message delivery, even during disruptions. For more information about AWS Regions and Availability Zones, see [AWS Global Infrastructure](https://aws.amazon.com/about-aws/global-infrastructure/).

You can also configure subscriptions with delivery retries and dead-letter queues. These features handle transient failures automatically and help ensure messages reach their intended destinations. 

Amazon SNS supports message filtering and message attributes. You can use these features to tailor resilience strategies to your specific use case and enhance the robustness of your applications.