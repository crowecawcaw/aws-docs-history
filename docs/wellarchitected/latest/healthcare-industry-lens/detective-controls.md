# Detective controls

| HCL_SEC3. How are you logging access<br>to health data? |
| ------------------------------------------------------- |
|                                                         |

**Log access to systems,
resources, and data in accordance with your policies and
procedures**

If your workload hosts health data, then under the
[Architecting
for HIPAA Security and Compliance on Amazon Web Services
whitepaper](../../../whitepapers/latest/architecting-hipaa-security-and-compliance-on-aws/auditing-back-ups-and-disaster-recovery.md "../../../whitepapers/latest/architecting-hipaa-security-and-compliance-on-aws/auditing-back-ups-and-disaster-recovery.md") you must implement and maintain logging of
access to that data in accordance with the regulatory
frameworks applicable to your workload. AWS makes it easy to
log access to health data stored in many services with AWS
CloudWatch and AWS CloudTrail. AWS also provides
service-specific mechanism to audit access to health data and
health data systems. For audit logging details, see the [Architecting
for HIPAA Security and Compliance on Amazon Web Services
whitepaper](../../../whitepapers/latest/architecting-hipaa-security-and-compliance-on-aws/auditing-back-ups-and-disaster-recovery.md "../../../whitepapers/latest/architecting-hipaa-security-and-compliance-on-aws/auditing-back-ups-and-disaster-recovery.md").

**Configure audit logs to
be centralized and immutable**

Environments that host and process health data should record
and audit any person or system that accesses the data. Such
logging provides evidence that the proper people and systems
are accessing health data, and can be helpful in investigating
a security incident. Configure logging to save to a
centralized location and the logs made immutable to verify
their integrity in the event of a forensic requirement.
Prevent modification of log data by creating an AWS account in
your organization that is designated to host audit logs and
implement strict authorization rules. AWS audit and logging
services, such as CloudWatch and CloudTrail, can save logs to
a central location, yielding one set of logs that encompass an
entire IT environment.

Use CloudTrail to log actions taken by users, roles, and AWS
services across your AWS infrastructure. Enable CloudTrail log
file integrity validation to prevent modification, deletion,
or forgery of CloudTrail log files without detection.

Enable AWS Config in all AWS accounts to assess, audit, and
evaluate resources within your AWS environment. AWS Config
maintains a database of resources, and their associated
configurations. This provides an audit record of AWS resource
configurations over time.

Capture network layer logs to track the transport layer
activity going to and from network interfaces in your VPC
using VPC Flow Logs. When using ELB, enable
access logs to capture detailed information about the requests
received and processed by one or more load balancers,
including client IP addresses, request paths, and server
responses. Similar approaches should be employed for other AWS
services, such as Amazon API Gateway, which offer similar
functionality.

Configure operating system and application logs, including
managed compute services like AWS Lambda, Amazon Elastic Container Service, and Amazon Elastic Kubernetes Service,
to send logs to CloudWatch log groups.  CloudWatch log
groups can be configured to forward logs to a centralized
account for long-term retention. Develop processes and coding
standards to avoid putting sensitive information into logs.
Additionally, use AWS encryption services to encrypt log data.
When using managed database services to store health data,
such as Amazon RDS and Amazon Redshift, enable database level
audit logging to collect information about connections and
user activity within the database.  You can use service
features to publish database logs to CloudWatch, simplifying
centralized log management.

Enable and configure Amazon S3 access logging for any Amazon S3 buckets that
may contain sensitive health data. Amazon S3 Access Logs record every
upload, download, and modification to stored objects.

Refer to the AWS documentation for each AWS service to find
the supported service-specific logging options.

| HCL_SEC4. How often do you review<br>audit logs? |
| ------------------------------------------------ |
|                                                  |

**Create, document, and
follow a policy and procedure to regularly review audit
logs**

In addition to the creation and documentation of an audit log
review policy and procedure, organizations who are auditing
access to health data should also have systems and procedures
in place to review the audit logs on a regular basis.
Facilitate audits by collecting all logs in a centralized
location. For example, AWS CloudTrail can be configured to
deliver logs from multiple accounts to a single Amazon S3 bucket.
This provides both an easier location allowing regular review
of the logs, while limiting the scope of access required for the
reviewer by limiting them to a single location rather than
multiple accounts.

Enable
[CloudTrail
Insights](../../../awscloudtrail/latest/userguide/logging-insights-events-with-cloudtrail.md "../../../awscloudtrail/latest/userguide/logging-insights-events-with-cloudtrail.md") to identify unusual activity in CloudTrail
logs in order to help improve the audit log review process.

**Automate alerts for
potential anomalies detected in logs**

Additionally, use automated systems that will generate
alerts if anomalies are detected in logs.  For example, create
[CloudWatch
alarms based on anomaly detection](../../../AmazonCloudWatch/latest/monitoring/Create_Anomaly_Detection_Alarm.md "../../../AmazonCloudWatch/latest/monitoring/Create_Anomaly_Detection_Alarm.md") that uses previously
recorded metrics to create a model of expected results.  You
can also use [the
Amazon OpenSearch Service to detect anomalies in logs](https://aws.amazon.com/blogs/big-data/preprocess-logs-for-anomaly-detection-in-amazon-opensearch/ "https://aws.amazon.com/blogs/big-data/preprocess-logs-for-anomaly-detection-in-amazon-opensearch/").
Enable CloudTrail Insights to detect unusual operational
activity that is recorded in your CloudTrail audit logs.
Review all applicable regulatory frameworks and standards and
ensuring the specific requirements are being met.  Configure
all alarms to be received by an identified owner, ensuring
that the alarm is acknowledged, triaged, and actioned.
Finally, create and follow a procedure that outlines a
regular cadence to review all automation configurations for
continued accuracy, sufficiency, and relevance of the alerts.
