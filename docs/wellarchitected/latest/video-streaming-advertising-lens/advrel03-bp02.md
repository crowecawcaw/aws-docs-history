

# ADVREL03-BP02 Choose AWS Regions that meet your legal and disaster recovery requirements
<a name="advrel03-bp02"></a>

 Select AWS Regions based on compliance and disaster recovery needs. It emphasizes the importance of understanding data jurisdiction requirements, particularly for advertising systems, and explains how regional choices impact both regulatory compliance (like GDPR) and system redundancy. 

## Implementation guidance
<a name="implementation-guidance-23"></a>

 Depending on the resiliency design of your advertising system, some components may reside in a different Region for redundancy purposes. Consider compliance needs for your in-transit and at-rest data. 

## Key AWS services
<a name="key-aws-services-9"></a>
+  [AWS Control Tower](https://aws.amazon.com/controltower/) provides Region-deny capabilities 
+  [AWS Managed Microsoft AD](https://aws.amazon.com/directoryservice/) supports multi-Region deployment, allowing AD-aware applications and AWS services to connect to the local instances of the global directory 
+  [AWS KMS](https://aws.amazon.com/kms/) allows you to replicate multi-Region keys into other Regions 
+  AWS services like [Amazon S3](https://aws.amazon.com/s3/) and [Amazon RDS](https://aws.amazon.com/rds/) are designed to be resilient by spreading requests and data across multiple [Availability Zones within a Region](https://aws.amazon.com/about-aws/global-infrastructure/regions_az/). However, for additional redundancy, you can deploy these services across multiple Regions to achieve isolation and avoid correlated failures 

## Resources
<a name="resources-18"></a>
+  [Accelerate your multi-region strategy with Amazon DynamoDB: Part 1](https://aws.amazon.com/blogs/database/part-1-accelerate-your-multi-region-strategy-with-amazon-dynamodb/) 
+  [AWS Global Infrastructure](https://aws.amazon.com/about-aws/global-infrastructure/) 
+  [Understand resiliency patterns and trade-offs to architect efficiently in the cloud](https://aws.amazon.com/blogs/architecture/understand-resiliency-patterns-and-trade-offs-to-architect-efficiently-in-the-cloud/) 
+  [Deny services and operations for AWS Regions of your choice with AWS Control Tower](https://aws.amazon.com/about-aws/whats-new/2021/11/deny-services-operations-aws-regions-control-tower/index.html) 
+  [Design consideration for AWS Managed Microsoft Active Directory - Active Directory Domain Services on AWS](https://docs.aws.amazon.com/whitepapers/latest/active-directory-domain-services/design-consideration-for-aws-managed-microsoft-active-directory.html) 
+  [Creating multi-Region replica keys - AWS Key Management Service](https://docs.aws.amazon.com/kms/latest/developerguide/multi-region-keys-replicate.html) 
+  [Regional services - AWS Fault Isolation Boundaries](https://docs.aws.amazon.com/whitepapers/latest/aws-fault-isolation-boundaries/regional-services.html) 
+  [Navigating GDPR Compliance on AWS](https://docs.aws.amazon.com/whitepapers/latest/navigating-gdpr-compliance/welcome.html) 