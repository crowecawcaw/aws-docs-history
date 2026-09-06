

# GxP Compliance Automation
<a name="gxp-compliance-automation"></a>

Publication date: **May 6, 2021 ([Diagram history](#gxp-history))**

With this architecture, you can build a secure and compliant Good Practice (GxP) workload on AWS. The solution uses [Service Catalog](https://docs.aws.amazon.com/servicecatalog/latest/adminguide/) to publish approved infrastructure templates, [AWS CloudFormation](https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/) to provision resources, and [AWS Config](https://docs.aws.amazon.com/config/latest/developerguide/) to monitor compliance continuously.

## GxP compliance automation diagram
<a name="gxp-diagram"></a>

![Reference architecture diagram showing how to build a secure and compliant GxP workload by using Service Catalog, CloudFormation, AWS Config, and CloudWatch.](http://docs.aws.amazon.com/reference-architecture-diagrams/latest/gxp-compliance-automation/images/gxp-compliance-automation.png)


The following steps describe the data flow and compliance automation for this architecture:

1. Use AWS Landing Zone to automate the setup of a secure and scalable environment. The security administrator defines an Service Catalog product (for example, a GxP application) by using CloudFormation templates.

1. Publish the template for developers in Service Catalog. Developers use this framework to further enhance the template based on application requirements.

1. Modify applications under source control by using AWS CodeCommit to manage the private code repository.

1. Deploy the modified code from AWS CodeCommit to your GxP infrastructure. Use Service Catalog Catalog to launch the product as a CloudFormation stack.

1. The stack provisions the necessary AWS resources based on what you committed to the code repository.

1. With Service Catalog at the center of this architecture, you can release source code without needing access to underlying resources or going through security administrators.

1. Automate the testing and installation qualification process by using [AWS Lambda](https://docs.aws.amazon.com/lambda/latest/dg/) or Python. Create a test summary and qualification report automatically in an Amazon S3 bucket.

1. Aggregate all individual AWS CloudTrail logs, Amazon VPC flow logs, and AWS Config changes into a centralized [Amazon Simple Storage Service](https://docs.aws.amazon.com/AmazonS3/latest/userguide/) bucket in a separate AWS account.

1. Configure, monitor, and set up automated alerts on changes and on the health of the stack by using [Amazon CloudWatch](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/).

1. Record and track change events through AWS Config when the stack changes. Display out-of-compliance events in a dashboard.

1. Initiate CloudWatch alarms based on rules you design to indicate when something might be out of compliance.

1. Use AWS CloudTrail to monitor API calls made against your AWS environment. CloudWatch Events alerts the administrator when something changes that could cause the system to be non-compliant.

1. Query log data and convert it into a human-readable format like CSV by using Amazon [Athena](https://docs.aws.amazon.com/athena/latest/ug/) for audit purposes.

1. Visualize AWS CloudTrail logs by using Amazon Quick Sight.

## Further reading
<a name="gxp-further-reading"></a>

For additional information, see the following resources:
+  [AWS Architecture Icons](https://aws.amazon.com/architecture/icons) 
+  [AWS Architecture Center](https://aws.amazon.com/architecture/) 
+  [AWS Well-Architected](https://aws.amazon.com/architecture/well-architected) 

## Diagram history
<a name="gxp-history"></a>

To receive updates about this reference architecture diagram, subscribe to the RSS feed.

| Change | Description | Date | 
| --- |--- |--- |
| [Initial publication](#gxp-history) | Reference architecture diagram first published. | May 6, 2021 | 

**RSS subscription requirement**  
To subscribe to RSS updates, you must have an RSS plugin enabled for the browser you are using.