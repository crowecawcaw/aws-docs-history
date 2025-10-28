# Resilience in Macie

The AWS global infrastructure is built around AWS Regions and Availability Zones.
Regions provide multiple physically separated and isolated Availability Zones, which are
connected through low-latency, high-throughput, and highly redundant networking. With
Availability Zones, you can design and operate applications and databases that automatically
fail over between zones without interruption. Availability Zones are more highly available,
fault tolerant, and scalable than traditional single or multiple data center
infrastructures. For more information about AWS Regions and Availability Zones, see [AWS Global
Infrastructure](https://aws.amazon.com/about-aws/global-infrastructure/ "https://aws.amazon.com/about-aws/global-infrastructure/").

In addition to the AWS global infrastructure, Amazon Macie offers several features to help
support your data resiliency and backup needs. For example, when you run a sensitive data discovery job or
Macie performs automated sensitive data discovery, Macie automatically creates an analysis record for each Amazon Simple Storage Service
(Amazon S3) object that's included in the scope of the analysis. These records, referred to as a
_sensitive data discovery results_, log details about the analysis that
Macie performs on individual S3 objects. This includes objects that Macie doesn't detect
sensitive data in, and objects that Macie can't analyze due to errors or issues. Macie
stores these results in an S3 bucket that you specify. For more information, see [Storing and retaining sensitive data
discovery results](discovery-results-repository-s3.md "discovery-results-repository-s3.md").

Macie also publishes policy and sensitive data findings to Amazon EventBridge as events. This
includes new findings and updates to existing policy findings. (It doesn't include findings
that you archive automatically using suppression rules.) By using EventBridge, you can send
findings data to your preferred storage platform and store the data for as long as you like.
Depending on publication settings that you choose, Macie can also publish policy and
sensitive data findings to AWS Security Hub. For more information, see [Monitoring and processing Macie findings](findings-monitor.md "findings-monitor.md").

You also have the option of using Macie API operations to retrieve findings and other
types of data programmatically. You can then process and send the data to your preferred
storage platform, or another service, application, or system. For information about API
operations that you might use to do this, see the [Amazon Macie API Reference](../APIReference/welcome.md "../APIReference/welcome.md").
