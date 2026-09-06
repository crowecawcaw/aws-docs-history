

# GAMESEC06-BP03 Use insights from system-level logs to continuously improve your infrastructure protection strategy
<a name="gamesec06-bp03"></a>

 Capture and store system-level logs from relevant services, such as [S3 server access logs](https://docs.aws.amazon.com/AmazonS3/latest/userguide/ServerLogs.html), [CloudFront access logs](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/AccessLogs.html), and [ALB access](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/load-balancer-access-logs.html) [logs](https://docs.aws.amazon.com/elasticloadbalancing/latest/application/load-balancer-access-logs.html). These logs can be stored in an S3 bucket in your account and are useful for associating your player usage information from within the game with system-level information including connection details such as IP addresses, request headers, and relevant request manipulation and filtering that you may have configured within your game backend. You can send these logs to the same logging solutions mentioned earlier, and you can [analyze them using SQL queries with Amazon Athena](https://docs.aws.amazon.com/athena/latest/ug/application-load-balancer-logs.html) without requiring the logs to be moved out of Amazon S3. 

 **Level of risk exposed if this best practice is not established:** Medium 

## Implementation guidance
<a name="implementation-guidance-32"></a>

 [Access Analyzer for S3](https://docs.aws.amazon.com/AmazonS3/latest/userguide/access-analyzer.html) is a feature that monitors your bucket access policies, making sure that the policies provide only the intended access to your Amazon S3 resources. Access Analyzer for S3 evaluates your bucket access policies and allows you to discover and swiftly remediate buckets with potentially unintended access. 

### Implementation steps
<a name="implementation-steps-32"></a>
+  Use AWS services for threat detection and incident response to automate aspects of your infrastructure protection strategy. 
+  Gain insights into your infrastructure protection through system-level logs and AWS services for artificial intelligence and machine learning. 

## Data protection
<a name="data-protection"></a>

 When developing and architecting your game, consider what type of data your studio is gathering and how you have decided to approach protecting it. Topics to explore within this aspect of security include: 
+  How you have chosen to identify and classify your data 
+  How you are protecting data at rest 
+  How you are protecting data in transit 

 There are no data protection best practices specific to the Games Lens. Refer to the Well-Architected Framework whitepaper for best practices in [data protection](https://docs.aws.amazon.com/wellarchitected/latest/security-pillar/data-protection.html) for security. 