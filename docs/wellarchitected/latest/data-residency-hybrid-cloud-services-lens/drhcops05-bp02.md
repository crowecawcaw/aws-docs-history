

# DRHCOPS05-BP02 Understand monitoring requirements in your Outposts
<a name="drhcops05-bp02"></a>

 Focus on similar observability and alerting as in an Availability Zone. In addition, add alerts for added responsibility such as security, networking, and capacity. 

 **Desired outcome:** Implement comprehensive monitoring for AWS Outposts workloads that aligns with the Availability Zone structure and accounts for the shared responsibility model. 

 **Benefits of establishing this best practice:** Enables end-to-end visibility, accurate issue detection, and targeted troubleshooting across cloud and on-premises components, improving operational efficiency. 

 **Level of risk exposed if this best practice is not established:** High 

## Implementation guidance
<a name="implementation-guidance-12"></a>

 Outposts have an updated shared responsibility model, as the hardware is not within an AWS-owned facility. As a result of this model, customers take on additional ownership of network, capacity, and security management, and they work with AWS in collaboration for any hardware maintenance. Set up specific metrics for Outposts at infrastructure and application layers, and provide visibility into AWS Health events. 

![Details the shared responsibility model for Outposts, which places software and hardware/global infrastructure responsibility with AWS.](http://docs.aws.amazon.com/wellarchitected/latest/data-residency-hybrid-cloud-services-lens/images/outposts-responsibility-model.png)


 Set up CloudWatch metrics, and enable cross-account observability where possible. Set up metrics to understand your connected status to the Region and traffic in and out. Implement capacity monitoring and follow [N\+1 capacity guidance](https://docs.aws.amazon.com/whitepapers/latest/aws-outposts-high-availability-design/capacity-planning.html) which means you provision additional capacity for each instance family for redundant hardware. to follow N\+1 guidance. Consider VPC Flow Logs and ELB access logs. If further detail is required, AWS X-Ray is an additional option for a complete view of requests across your applications. 

## Resources
<a name="resources-1"></a>
+  [CloudWatch metrics for Outposts racks](https://docs.aws.amazon.com/outposts/latest/userguide/outposts-cloudwatch-metrics.html) [Deploying an automated Amazon CloudWatch dashboard for AWS Outposts using AWS CDK](https://aws.amazon.com/blogs/compute/deploying-an-automated-amazon-cloudwatch-dashboard-for-aws-outposts-using-aws-cdk/) 
+  [Monitor your Outposts rack](https://docs.aws.amazon.com/outposts/latest/userguide/monitor-outposts.html) 
+  [Monitoring best practices for AWS Outposts](https://aws.amazon.com/blogs/mt/monitoring-best-practices-for-aws-outposts/) 
+  [CloudWatch metrics for Outposts racks](https://docs.aws.amazon.com/outposts/latest/userguide/outposts-cloudwatch-metrics.html) 