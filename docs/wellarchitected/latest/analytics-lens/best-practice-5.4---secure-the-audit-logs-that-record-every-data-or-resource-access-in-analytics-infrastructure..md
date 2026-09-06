

# Best practice 5.4 – Secure the audit logs that record every data or resource access in analytics infrastructure
<a name="best-practice-5.4---secure-the-audit-logs-that-record-every-data-or-resource-access-in-analytics-infrastructure."></a>

 Logs are an audit trail of events and should be stored in an immutable format for compliance purposes. These logs provide proof of actions and help in identifying misuse. The logs provide a baseline for analysis or for an audit when initiating an investigation. By using a fault-tolerant storage for these logs, it is possible to recover them even when there is a failure in the auditing systems. Access permissions to these logs must be restricted to privileged users. Also log audit log access to help in identifying unintended access to audit data. 

## Suggestion 5.4.1 – Ensure that auditing is active in analytics services and are delivered to fault-tolerant persistent storage
<a name="suggestion-5.4.1---ensure-that-auditing-is-active-in-analytics-services-and-are-delivered-to-fault-tolerant-persistent-storage."></a>

 Review the available audit log features of your analytics solutions, and configure the solutions to store the audit logs to fault-tolerant persistent storage. This helps ensure that you have complete audit logs for security and compliance purposes. 

 For more details, refer to the following information: 
+  AWS Management and Governance Blog: [AWS CloudTrail Best Practices](https://aws.amazon.com/blogs/mt/aws-cloudtrail-best-practices/) 
+  Amazon Redshift Cluster Management Guide: [Database audit logging](https://docs.aws.amazon.com/redshift/latest/mgmt/db-auditing.html) 
+  Amazon OpenSearch Service (successor to Amazon OpenSearch Service) Developer Guide: [Monitoring](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/audit-logs.html) [audit logs in Amazon OpenSearch Service](https://docs.aws.amazon.com/opensearch-service/latest/developerguide/audit-logs.html) 
+  AWS Technical Guide – Build a Secure Enterprise Machine Learning Platform on AWS: [Audit trail](https://docs.aws.amazon.com/whitepapers/latest/build-secure-enterprise-ml-platform/audit-trail-management.html) [management](https://docs.aws.amazon.com/whitepapers/latest/build-secure-enterprise-ml-platform/audit-trail-management.html) 
+  AWS Big Data Blog: [Build, secure, and manage data lakes with AWS Lake Formation](https://aws.amazon.com/blogs/big-data/building-securing-and-managing-data-lakes-with-aws-lake-formation/) 