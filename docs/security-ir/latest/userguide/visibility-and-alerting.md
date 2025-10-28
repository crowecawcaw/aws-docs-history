# Visibility and alerting

[**AWS Security Incident Response**](https://aws.amazon.com/security-incident-response/ "https://aws.amazon.com/security-incident-response/") – AWS Security Incident Response is a comprehensive service that
helps organizations handle security events throughout their lifecycle by combining automated capabilities with expert human support. The service leverages
automated monitoring and investigation features to free up organizational resources while maintaining vigilant security oversight, and when security events
occur, it facilitates accelerated communication and coordination among stakeholders for swift response times. The service supports multiple use cases, including
preparation and simulation of security events, response to active incidents, and streamlined post-incident reporting and analysis, ensuring organizations are
well-equipped to handle security challenges at every stage.

[**AWS Security Hub**](https://aws.amazon.com/security-hub/ "https://aws.amazon.com/security-hub/") – AWS Security Hub provides customers with a comprehensive view of high-priority
security alerts and compliance statuses across AWS accounts. Security Hub aggregates, organizes, and prioritizes findings
from AWS services such as Amazon GuardDuty, Amazon Inspector, Amazon Macie, and AWS Partner solutions. Findings are visually summarized on
integrated dashboards with actionable graphs and tables. You can also continuously monitor your environment using
automated compliance checks based on the AWS best practices and industry standards your organization follows.

[**Amazon GuardDuty**](https://aws.amazon.com/guardduty/ "https://aws.amazon.com/guardduty/") – Amazon GuardDuty is a managed threat detection service continuously
monitoring malicious or unauthorized behavior to help customers protect AWS accounts and workloads. It
monitors activity such as unusual API calls or potentially unauthorized deployments indicating possible
account or resource compromise of Amazon EC2 instances, Amazon S3 buckets, or reconnaissance by bad actors.

GuardDuty identifies suspected bad actors through integrated threat intelligence feeds using machine learning
to detect anomalies in account and workload activity. When a potential threat is detected, the
service delivers a detailed security alert to the GuardDuty console and CloudWatch Events. This makes alerts
actionable and simple to integrate into existing event management and workflow systems.

GuardDuty also offers two add-ons to monitor for threats with specific services: Amazon GuardDuty for Amazon S3 protection and Amazon GuardDuty for Amazon EKS protection.
Amazon S3 protection enables GuardDuty to monitor object-level API operations to identify potential security risks for data within Amazon S3 buckets.
Kubernetes protection enables GuardDuty to detect suspicious activities and potential compromises of
Kubernetes clusters within Amazon EKS.

[**Amazon Macie**](https://aws.amazon.com/macie/ "https://aws.amazon.com/macie/") – Amazon Macie is an AI-powered security service that helps prevent
data loss by automatically discovering, classifying, and protecting sensitive data stored in AWS. Macie
uses machine learning (ML) to recognize sensitive data such as personally identifiable information
(PII) or intellectual property, assign a business value, and provide visibility into where this data
is stored and how it is being used in your organization. Amazon Macie continuously monitors data access
activity for anomalies, and delivers alerts when it detects a risk of unauthorized access or inadvertent
data leaks.

[**AWS Config Rules**](https://aws.amazon.com/config/ "https://aws.amazon.com/config/") – An AWS Config rule represents the preferred configurations for a
resource and is evaluated against configuration changes on the relevant resources, as recorded by AWS Config.
You can see the results of evaluating a rule against the configuration of a resource on a dashboard.
Using AWS Config rules, you can assess your overall compliance and risk status from a configuration perspective,
view compliance trends over time, and find which configuration change caused a resource to be out
of compliance with a rule.

[**AWS Trusted Advisor**](https://aws.amazon.com/premiumsupport/technology/trusted-advisor/ "https://aws.amazon.com/premiumsupport/technology/trusted-advisor/") – AWS Trusted Advisor is an online resource to help you reduce cost,
increase performance, and improve security by optimizing your AWS environment. Trusted Advisor provides
real time guidance to help you provision your resources by following AWS best practices. The full set of Trusted Advisor checks,
including CloudWatch Events integration, is available to Business and Enterprise Support plan customers.

[**Amazon CloudWatch**](https://aws.amazon.com/cloudwatch/ "https://aws.amazon.com/cloudwatch/") – Amazon CloudWatch is a monitoring service for AWS Cloud
resources and the applications you run on AWS. You can use CloudWatch to collect and track metrics,
collect and monitor log files, set alarms, and automatically react to changes in your AWS resources.
CloudWatch can monitor AWS resources, such as Amazon EC2 instances, Amazon DynamoDB tables, and Amazon RDS DB instances, as
well as custom metrics generated by your applications and services, and any log files your
applications generate. You can use Amazon CloudWatch to get system-wide visibility into resource
utilization, application performance, and operational health. You can use these insights
to react accordingly and keep your application running smoothly.

[**Amazon Inspector**](https://aws.amazon.com/inspector/ "https://aws.amazon.com/inspector/") – Amazon Inspector is an automated security assessment
service that helps improve the security and compliance of applications deployed on AWS.
Amazon Inspector automatically assesses applications for vulnerabilities or deviations from best
practices. After performing an assessment, Amazon Inspector produces a detailed list of security
findings prioritized by level of severity. These findings can be reviewed directly or as
part of detailed assessment reports which are available through the Amazon Inspector console or API.

[**Amazon Detective**](https://aws.amazon.com/detective/ "https://aws.amazon.com/detective/") – Amazon Detective is a security service that
automatically collects log data from your AWS resources and uses machine learning,
statistical analysis, and graph theory to build a linked set of data that enables you
to conduct faster and more efficient security investigations. Detective can
analyze trillions of events from multiple data sources such as VPC Flow Logs, CloudTrail, and GuardDuty,
and automatically creates a unified, interactive view of your resources, users, and the
interactions between them over time. With this unified view, you can visualize all the details
and context in one place to identify the underlying reasons for the findings, drill down into
relevant historical activities, and quickly determine the root cause.
