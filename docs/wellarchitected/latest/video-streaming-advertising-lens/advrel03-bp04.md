

# ADVREL03-BP04 Reserve appropriate capacity of services in the supported Regions
<a name="advrel03-bp04"></a>

 Manage service capacity across multiple Regions. Perform regular load testing at five times your baseline RTB traffic levels to validate capacity requirements. Validate that appropriate reservations are made to handle normal operations, peak loads, and potential disruptions. 

## Implementation guidance
<a name="implementation-guidance-25"></a>

 If your application is designed to scale out over multiple Regions, service could be disrupted by temporary resource constraints or other issues impacting a single Availability Zone or Region. Regularly perform load tests with at least five times the baseline of RTB traffic expectations to validate that allocated capacity meets low water mark, mean, and peak capacity projections. Based on the results of your load tests, make capacity reservation. 

## Key AWS services
<a name="key-aws-services-11"></a>
+  [Amazon Route 53](https://aws.amazon.com/route53/) 
+ [Amazon DynamoDB global tables](https://aws.amazon.com/dynamodb/)
+  [Amazon S3](https://aws.amazon.com/s3/) 

## Resources
<a name="resources-20"></a>
+  [AWS service quotas](https://docs.aws.amazon.com/general/latest/gr/aws_service_limits.html) 
+  [Quotas and constraints for Amazon RDS](https://docs.aws.amazon.com/AmazonRDS/latest/UserGuide/CHAP_Limits.html) 
+  [What to Consider when Selecting a Region for your Workloads](https://aws.amazon.com/blogs/architecture/what-to-consider-when-selecting-a-region-for-your-workloads/) 
+  [Creating a Multi-Region Application with AWS Services – Part 1, Compute, Networking, and Security](https://aws.amazon.com/blogs/architecture/creating-a-multi-region-application-with-aws-services-part-1-compute-and-security/index.html) 