

# Security-rich API management using IBM API Connect on AWS

Publication date: **October 26, 2023 ([Diagram history](diagram-history.md))**

With this architecture, you can take advantage of agility, security, and elasticity to create, manage, secure, and socialize your APIs across the cloud, powering digital applications with a scalable API management solution.

## Security-rich API management using IBM API Connect on AWS diagram
<a name="security-rich-api-management-using-ibm-api-connect-diagram"></a>

![API developers publish APIs through IBM API Connect on AWS, and client apps discover and consume them.](https://docs.aws.amazon.com/reference-architecture-diagrams/latest/digital-marketing/images/security-rich-api-management-using-ibm-api-connect.png)


The following steps describe the architecture:

1.  The API developer creates API endpoints, specifies access controls, and publishes the APIs to the developer portal for external discovery by app developers using IBM API Connect. 

1.  An application developer can access the API Connect developer portal to search and discover APIs. 

1.  API calls can be authorized using different authentication and authorization mechanisms, such as OAuth providers or a user registry. 

1.  API Connect can be integrated with Stripe Billing to monetize APIs, generate monthly invoices, and charge customers automatically. 

1.  API implementation and integration can span across [Amazon Elastic Compute Cloud](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/) (Amazon EC2), [Amazon Elastic Kubernetes Service](https://docs.aws.amazon.com/eks/latest/userguide/) (Amazon EKS), [AWS Elastic Beanstalk](https://docs.aws.amazon.com/elasticbeanstalk/latest/dg/), [Red Hat OpenShift Service on AWS](https://docs.aws.amazon.com/rosa/latest/userguide/) (ROSA), and corporate data center applications. The API developer can also use an [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/) policy to initiate Lambda functions with AWS-native service integrations. 

1.  [AWS CodePipeline](https://docs.aws.amazon.com/codepipeline/latest/userguide/) can be integrated with an API Connect CI/CD pipeline to publish and test APIs and product changes. 

1.  Client applications (consuming applications) such as web apps, mobile apps, and IoT devices can invoke and consume the APIs. 

1.  The API analytics data can be offloaded to [Amazon Simple Storage Service](https://docs.aws.amazon.com/AmazonS3/latest/userguide/) (Amazon S3), which integrates with [AWS Quick](https://docs.aws.amazon.com/quick/latest/userguide/) to visualize using dashboards. You can review API traffic patterns, latency, consumption, and more, then make data-driven insights into your API initiatives. 

## Further reading
<a name="security-rich-api-management-using-ibm-api-connect-further-reading"></a>

For additional information, see the following resources:
+ [AWS Architecture Icons](https://aws.amazon.com/architecture/icons)
+ [AWS Architecture Center](https://aws.amazon.com/architecture)
+  [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected) 