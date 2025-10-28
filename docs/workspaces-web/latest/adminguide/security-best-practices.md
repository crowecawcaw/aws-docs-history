# Security best practices for Amazon WorkSpaces Secure Browser

Amazon WorkSpaces Secure Browser provides a number of security features you can use as you develop and implement
your own security policies. The following best practices are general guidelines and don’t
represent a complete security solution. Because these best practices might not be appropriate
or sufficient for your environment, treat them as helpful considerations rather than
prescriptions.

Best practices for Amazon WorkSpaces Secure Browser include the following:

- To detect potential security events associated with your use of WorkSpaces Secure Browser, use AWS CloudTrail
  or Amazon CloudWatch to detect and track access history and process logs. For more information,
  see [Monitoring Amazon WorkSpaces Secure Browser with Amazon CloudWatch](monitoring-cloudwatch.md "monitoring-cloudwatch.md") and
  [Logging WorkSpaces Secure Browser API calls using AWS CloudTrail](logging-using-cloudtrail.md "logging-using-cloudtrail.md").
- To implement detective controls and identify anomalies, use CloudTrail logs and CloudWatch
  metrics. For more information, see [Monitoring Amazon WorkSpaces Secure Browser with Amazon CloudWatch](monitoring-cloudwatch.md "monitoring-cloudwatch.md") and [Logging WorkSpaces Secure Browser API calls using AWS CloudTrail](logging-using-cloudtrail.md "logging-using-cloudtrail.md").
- You can set up user access logging to record user events. For more information, see
  [Setting up user activity logging in Amazon WorkSpaces Secure Browser](user-logging.md "user-logging.md").
  To prevent potential security events associated with your use of WorkSpaces Secure Browser, follow these best
  practices:

- Implement least privilege access and create specific roles to be used for WorkSpaces Secure Browser
  actions. Use IAM templates to create a Full Access or Read Only role. For more
  information, see [AWS managed policies for WorkSpaces Secure Browser](security-iam-awsmanpol.md "security-iam-awsmanpol.md").
- Be careful with sharing portal domains and user credentials. Anyone on the internet
  can access the web portal, but they can't start a session unless they have a valid user
  credential to the portal. Be cautious about how, when, and to whom you share web portal
  credentials.
