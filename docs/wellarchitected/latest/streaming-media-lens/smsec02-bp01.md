

# SMSEC02-BP01 Monitor for fraudulent access attempts
<a name="smsec02-bp01"></a>

Even when you have implemented access controls to the content you want to serve, continue to monitor for unauthorized access and perform regular checks to verify that access groups are up to date and that no unauthorized users have found their way in.

**Desired outcome:**
+ By monitoring access requests and user access, you will have the ability to know how your content is being accessed and can confirm that content isn't being delivered to unauthorized users. This data can also be used to create risk scoring or warnings that can help teams take proactive actions.

**Common anti-patterns:**
+ Organizations deploy streaming infrastructure without configuring access logging or monitoring for anomalous viewing patterns, leaving credential sharing and account compromise undetected.
+ Teams rely solely on authentication without monitoring post-authentication behavior, missing indicators such as simultaneous streams from geographically distant locations.
+ Organizations don't aggregate or analyze Amazon CloudFront access logs, failing to detect patterns like automated content scraping or bot-driven access from data center IP ranges.
+ Teams lack automated alerting for abnormal request volumes or geographic anomalies, discovering unauthorized access only after content has been widely redistributed.
+ Organizations fail to implement risk scoring for viewer sessions, treating all authenticated requests equally regardless of suspicious device fingerprints, VPN usage, or unusual viewing cadence.

**Benefits of establishing this best practice:**
+ Automated monitoring identifies credential sharing, account compromise, and unauthorized access attempts before they result in widespread content theft or service abuse.
+ Risk-based authentication detects credential stuffing attacks and password reuse, prompting additional verification before granting access to premium content.
+ Visibility into viewing patterns enables detection of stream redistribution services that use legitimate accounts to capture and rebroadcast content.
+ Aggregated access data reveals trends in unauthorized usage, informing decisions about where to strengthen access controls or adjust content protection strategies.
+ Full access logs provide auditable records demonstrating that content access is monitored and controlled, satisfying content licensor security requirements.

**Level of risk exposed if this best practice is not established:** High

## Implementation guidance
<a name="implementation-guidance"></a>

Implement a multi-layered approach combining Amazon CloudFront access logs, Amazon Cognito security features, and custom analytics using Amazon Kinesis and Amazon OpenSearch to detect and investigate anomalies. Configure automated response mechanisms that can prompt for additional verification or block suspicious access attempts.

For example, content requests through Amazon CloudFront can be logged and aggregated into Amazon S3. Amazon Athena can then [query this access data](https://docs.aws.amazon.com/athena/latest/ug/create-cloudfront-table-manual-json.html) for abnormalities like:
+ **Request location** — Are requests only coming from geographic Regions where you would expect? Is the user location obfuscated by a downstream provider?
+ **Request IP** — Is a specific IP address requesting content in a pattern that reflects normal viewing habits?
+ **User Agent** — Is the user-agent string from the device one that is known and valid?

Amazon CloudFront logs can also be delivered to [OpenSearch which allows for creation of dashboards](https://docs.aws.amazon.com/solutions/latest/centralized-logging-with-opensearch/amazon-cloudfront-logs.html) that can visualize data and trends. When data is aggregated and presented in metrics or a dashboard, teams can use the data to help detect trends such as high requests from outside your geo-location settings.

Monitor activities such as sign-in attempts from new locations and devices, assign a risk score based on the activity, and decide to either prompt users for additional verification or block the sign-in request. You can notify users of suspicious sign-in attempts and prompt them to secure their accounts. You can also view a history of sign-in attempts and their risk scores. The advanced security features in Amazon Cognito can also help you identify password sharing, reuse, or theft.

### Implementation steps
<a name="implementation-steps"></a>

1. **Configure access logging:** Configure full access logging with Amazon CloudWatch.

1. **Set up log aggregation:** Set up Amazon Kinesis or Amazon OpenSearch for log aggregation and pattern analysis.

1. **Enable advanced security features:** Set up Amazon Cognito advanced security features for user risk assessment.

1. **Configure security alerting:** Implement Amazon EventBridge rules or Amazon Simple Notification Service (SNS) for security alerting and user notification.

1. **Deploy monitoring dashboards:** Deploy Amazon CloudWatch and OpenSearch dashboards for security operation visibility.

1. **Query access logs:** [Use Amazon Athena to query logs from CloudFront with JSON](https://docs.aws.amazon.com/athena/latest/ug/create-cloudfront-table-manual-json.html).

## Resources
<a name="resources"></a>

**Related best practices**
+ [SMSEC01-BP01 Use an identity provider to authenticate viewers and access policies to implement least privilege access to protected content](smsec01-bp01.html)

**Related documents**
+ [Amazon CloudFront Usage Charts](https://docs.aws.amazon.com/AmazonCloudFront/latest/DeveloperGuide/usage-charts.html)
+ [Querying CloudFront Logs with Amazon Athena](https://docs.aws.amazon.com/athena/latest/ug/cloudfront-logs.html)
+ [Getting Started with CloudWatch Internet Monitor](https://docs.aws.amazon.com/AmazonCloudWatch/latest/monitoring/CloudWatch-IM-get-started.cf-monitor.html)
+ [Centralized Logging with OpenSearch for CloudFront](https://docs.aws.amazon.com/solutions/latest/centralized-logging-with-opensearch/amazon-cloudfront-logs.html)

**Related services**
+ [Amazon CloudFront](https://aws.amazon.com/cloudfront/)
+ [Amazon Athena](https://aws.amazon.com/athena/)