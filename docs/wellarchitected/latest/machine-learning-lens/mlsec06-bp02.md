# MLSEC06-BP02 Monitor human interactions with data for anomalous

activity

Implement comprehensive monitoring of data access events to detect
unauthorized or suspicious activities. By auditing user interactions
with data, you can identify potential security threats such as
unusual access patterns, abnormal locations, or activity that
exceeds normal baselines. Use specialized AWS services for anomaly
detection alongside data classification to assess risks and protect
your machine learning assets.

**Desired outcome:** You have
comprehensive visibility into human interactions with your data,
with logging enabled for create, read, update, and delete
operations. You can identify who accessed specific data elements,
what actions they took, and when those actions occurred. Your
monitoring system automatically flags anomalous activities based on
established baselines and alerts you to potential security threats.
Data classification is integrated with your monitoring approach to
prioritize security events based on data sensitivity.

**Common anti-patterns:**

- Implementing logging without monitoring or analysis
  capabilities.
- Focusing only on system-level access without tracking specific
  data interactions.
- Failing to establish user activity baselines for anomaly
  detection.
- Not classifying data to differentiate between access to
  sensitive and non-sensitive information.
- Monitoring access events without automated alerting mechanisms.

**Benefits of establishing this best
practice:**

- Early detection of potential data breaches or insider threats.
- Improved ability to investigate security incidents with
  comprehensive audit trails.
- Improves adherence to data protection regulations and
  requirements.
- Better visibility into how data is being used across your ML
  systems.
- Reduced risk of unauthorized data access or exfiltration.

**Level of risk exposed if this best practice
is not established:** High

## Implementation guidance

Protecting your machine learning data requires visibility into who
is accessing it and how it's being used. By monitoring human
interactions with your data, you can identify potential security
threats before they lead to data breaches or misuse. This involves
implementing comprehensive logging for data access events,
classifying your data based on sensitivity, and using automated
tools to detect anomalous behavior.

Start by enabling logging for data interactions, particularly
focusing on human access rather than just system-to-system
communications. Your logs should capture details about who
accessed the data, what specific elements they accessed, what
actions they took, and when those interactions occurred. This
creates an audit trail that serves as the foundation for your
monitoring strategy.

Next, classify your data based on sensitivity and importance. By
knowing which datasets contain personally identifiable information
(PII), intellectual property, or other sensitive information, you
can prioritize monitoring efforts and apply appropriate security
controls. This classification details the potential impact of
unauthorized access to different datasets.

Finally, implement anomaly detection to identify unusual patterns
that might indicate security threats. These anomalies could
include access from unusual locations, outside normal working
hours, excessive access volume, or access to data that's not
typically needed for an employee's role. When anomalies are
detected, your system should generate alerts to prompt
investigation.

### Implementation steps

1. **Enable data access
   logging**. Verify that you have data access logging
   for human CRUD (create, read, update, and delete)
   operations, including the details of who accessed what
   elements, what action they took, and at what time. Leverage
   [AWS CloudTrail](https://aws.amazon.com/cloudtrail/ "https://aws.amazon.com/cloudtrail/") to capture API calls and user activities
   across your AWS environment. Configure CloudTrail to log
   data events for
   [Amazon S3](https://aws.amazon.com/s3/ "https://aws.amazon.com/s3/") buckets containing your training and inference
   data. For SageMaker AI environments, use
   [Amazon SageMaker AI Logging and Monitoring](../../../sagemaker/latest/dg/logging-cloudwatch.md "../../../sagemaker/latest/dg/logging-cloudwatch.md") capabilities to
   track access to ML models and datasets.
2. **Classify your data**. Use
   [Amazon Macie](https://aws.amazon.com/macie/ "https://aws.amazon.com/macie/") for protecting and classifying training and
   inference data in
   [Amazon S3](https://aws.amazon.com/s3/ "https://aws.amazon.com/s3/"). Amazon Macie is a fully managed security service
   that uses ML to automatically discover, classify, and
   protect sensitive data in AWS. The service recognizes
   sensitive data, such as personally identifiable information
   (PII) or intellectual property. Configure Macie to perform
   regular automated scans of your S3 buckets to identify and
   tag sensitive data. Create custom data identifiers in Macie
   to recognize organization-specific sensitive data patterns
   beyond the standard patterns Macie detects.
3. **Monitor and protect**. Use
   [Amazon GuardDuty](https://aws.amazon.com/guardduty/ "https://aws.amazon.com/guardduty/") to monitor for malicious and unauthorized
   activities. This will enable protecting AWS accounts,
   workloads, and data stored in
   [Amazon S3](https://aws.amazon.com/s3/ "https://aws.amazon.com/s3/"). Configure GuardDuty to analyze CloudTrail logs,
   VPC flow logs, and DNS logs to detect suspicious activities.
   Pay special attention to the
   [GuardDuty
   S3 Finding Types](../../../guardduty/latest/ug/guardduty_finding-types-s3.md "../../../guardduty/latest/ug/guardduty_finding-types-s3.md") which can detect anomalous access
   patterns to your S3-stored data.
4. **Set up anomaly detection**.
   Implement automated anomaly detection for data access
   patterns using
   [Amazon CloudWatch Anomaly Detection](../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Anomaly_Detection.md "../../../AmazonCloudWatch/latest/monitoring/CloudWatch_Anomaly_Detection.md"). Create CloudWatch
   metrics for access frequency, data volume transferred,
   access times, and other relevant metrics. Configure
   CloudWatch alarms to alert when anomalies are detected based
   on these metrics.
5. **Establish data access
   baselines**. Create baseline profiles of normal
   user access patterns using
   [AWS CloudWatch](https://aws.amazon.com/cloudwatch/ "https://aws.amazon.com/cloudwatch/") to monitor access trends over time. Set up
   dashboards that visualize normal patterns of data access by
   team, role, or time period. Use these baselines to fine-tune
   anomaly detection thresholds and reduce false positives.
6. **Implement alerting
   mechanisms**. Configure
   [Amazon EventBridge](https://aws.amazon.com/eventbridge/ "https://aws.amazon.com/eventbridge/") to trigger automated responses when
   suspicious access events are detected. Route alerts to your
   security team through notification channels like
   [Amazon SNS](https://aws.amazon.com/sns/ "https://aws.amazon.com/sns/") for immediate response. Create different alerting
   thresholds based on data classification and sensitivity.
7. **Centralize logging and
   monitoring**. Use
   [Amazon OpenSearch Service](https://aws.amazon.com/opensearch-service/ "https://aws.amazon.com/opensearch-service/") (formerly Amazon OpenSearch Service) to create a centralized repository for log analysis
   and visualization. Build comprehensive dashboards to monitor
   data access patterns across your organization. Implement log
   retention policies that comply with your regulatory
   requirements.
8. **Control and audit data exploration
   activities**. Implement
   [AWS Lake Formation](https://aws.amazon.com/lake-formation/ "https://aws.amazon.com/lake-formation/") with
   [Amazon SageMaker AI Studio](https://aws.amazon.com/sagemaker/studio/ "https://aws.amazon.com/sagemaker/studio/") to provide fine-grained access
   controls for data exploration. Configure Lake Formation
   permissions to restrict data access based on user roles and
   data classification. Use
   [AWS IAM](https://aws.amazon.com/iam/ "https://aws.amazon.com/iam/") to enforce least-privilege access to sensitive
   data.
9. **Monitor access to AI training
   data**. Implement specialized monitoring for
   datasets used to train AI models, as these may contain
   particularly sensitive information or be subject to greater
   privacy concerns. Use
   [Amazon SageMaker AI Model Monitor](https://aws.amazon.com/sagemaker/model-monitor/ "https://aws.amazon.com/sagemaker/model-monitor/") to detect drift in model
   behavior that might indicate data access issues. Implement
   enterprise-ready security and privacy controls for
   foundation models.

## Resources

**Related documents:**

- [CloudWatch Logs for Amazon SageMaker AI](../../../sagemaker/latest/dg/logging-cloudwatch.md "../../../sagemaker/latest/dg/logging-cloudwatch.md")
- [GuardDuty
  S3 Protection finding types](../../../guardduty/latest/ug/guardduty_finding-types-s3.md "../../../guardduty/latest/ug/guardduty_finding-types-s3.md")
- [AWS CloudTrail Documentation](../../../cloudtrail.md "../../../cloudtrail.md")
- [Configure
  security in Amazon SageMaker AI](../../../sagemaker/latest/dg/security.md "../../../sagemaker/latest/dg/security.md")
- [Building
  a Self-Service, Secure, & Continually Compliant
  Environment on AWS](https://aws.amazon.com/blogs/architecture/building-a-self-service-secure-continually-compliant-environment-on-aws/ "https://aws.amazon.com/blogs/architecture/building-a-self-service-secure-continually-compliant-environment-on-aws/")
- [How
  to Use New Advanced Security Features for Amazon Cognito user pools](https://aws.amazon.com/blogs/security/how-to-use-new-advanced-security-features-for-amazon-cognito-user-pools/ "https://aws.amazon.com/blogs/security/how-to-use-new-advanced-security-features-for-amazon-cognito-user-pools/")
- [Best
  practices for setting up Amazon Macie with AWS Organizations](https://aws.amazon.com/blogs/security/best-practices-for-setting-up-amazon-macie-with-aws-organizations/ "https://aws.amazon.com/blogs/security/best-practices-for-setting-up-amazon-macie-with-aws-organizations/")

**Related videos:**

- [Protect
  Your Data in S3 with Amazon Macie and Amazon GuardDuty - AWS
  Online Tech Talks](https://www.youtube.com/watch?v=lvPT71jAIXk "https://www.youtube.com/watch?v=lvPT71jAIXk")
- [Protecting
  sensitive data with Amazon Macie and Amazon GuardDuty](https://www.youtube.com/watch?v=h7pq95RMuEQ "https://www.youtube.com/watch?v=h7pq95RMuEQ")

**Related examples:**

- [AWS Security Hub automated response and remediation](https://github.com/aws-solutions/aws-security-hub-automated-response-and-remediation "https://github.com/aws-solutions/aws-security-hub-automated-response-and-remediation")
