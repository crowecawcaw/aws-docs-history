# Cost optimization

Amazon S3 offers a range of features and storage classes to help you optimize costs throughout your data lifecycle. Storage classes offer the flexibility to manage your costs, by providing different data-access levels at corresponding costs, with no upfront fees or commitment to how much content you store. Like other AWS services, you pay as you go and pay only for what you use. 

Amazon S3 storage classes are purpose-built to provide the lowest cost storage for different access patterns. These include: 


* S3 Standard for general-purpose storage of frequently accessed data.
* Amazon S3 Express One Zone for high-performance frequently accessed data in a single-Availability Zone.
* S3 Intelligent-Tiering to automatically optimize costs for data with unknown or changing access patterns.
* S3 Standard-IA (S3 Standard-IA) and S3 One Zone-IA (S3 One Zone-IA) for long-lived, but less frequently accessed data.
* S3 Glacier Instant Retrieval for archive data that needs immediate access.
* S3 Glacier Flexible Retrieval for archive data that doesn't require immediate access but needs the flexibility to
 retrieve large sets of data at no cost.
* S3 Glacier Deep Archive for long-term archive and digital preservation at the lowest storage costs in the cloud.

 You can move objects to the most cost-effective storage class at any time. Additionally, Amazon S3 provides features to manage your data lifecycle. For example, you can use S3 Lifecycle configuration to automate transitioning objects to more cost-effective storage classes, or to automatically delete expired objects based on the rules that you define.

Features such as S3 Storage Class Analysis, cost allocation tagging, and billing and usage reports help you analyze your cost and usage patterns.

###### Topics

* [Billing and usage reporting for Amazon S3](BucketBilling.md "BucketBilling.md")
* [Understanding and managing Amazon S3 storage classes](storage-class-intro.md "storage-class-intro.md")
* [Managing the lifecycle of objects](object-lifecycle-mgmt.md "object-lifecycle-mgmt.md")
