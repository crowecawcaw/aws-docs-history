

# Best practice 6.3 – Notify stakeholders about analytics or ETL job failures
<a name="best-practice-6.3---notify-stakeholders-about-analytics-or-etl-job-failures."></a>

 Analytics and ETL job failures can impact the SLAs for delivering the data on time for downstream analytics workloads. Failures might cause data quality or data integrity issues as well. Notifying all stakeholders about the job failure as soon as possible is important for remediation actions needed. Stakeholders may include IT operations, help desk, data sources, analytics, and downstream workloads. 

 For more details, see AWS Well-Architected: [Design your Workload to Withstand Component Failures](https://docs.aws.amazon.com/wellarchitected/latest/reliability-pillar/design-your-workload-to-withstand-component-failures.html) 

## Suggestions 6.3.1 – Establish automated notifications to predefined recipients
<a name="suggestions-6.3.1---establish-automated-notifications-to-predefined-recipients."></a>

 Use services such Amazon Simple Notification Service (Amazon SNS) to send automated emails, SMS alerts, or both in the event of failure. Store the alert logs in an immutable data store for future reference. 

## Suggestions 6.3.2 – Do not include sensitive data in notifications
<a name="suggestions-6.3.2-do-not-include-sensitive-data-in-notifications."></a>

 Automated alerts often include indicators of useful information for troubleshooting the failure. Ensure PII and sensitive information, such as personal, medical, or ﬁnancial information is not shared in failure notiﬁcations. 

For more details, see AWS Glue: [Detect and process sensitive data](https://docs.aws.amazon.com/glue/latest/dg/detect-PII.html).

## Suggestions 6.3.3 – Integrate the analytics job failure notification solution with the enterprise operation management system
<a name="suggestions-6.3.3---integrate-the-analytics-job-failure-notification-solution-with-the-enterprise-operation-management-system."></a>

 Where possible, integrate automated notifications into existing operations management tools. For example, an operations support ticket can be automatically filed in the event of a failure. That same ticket can automatically be resolved if the analytics system recovers on retry. 

## Suggestions 6.3.4 – Notify IT operations and help desk teams of any ETL job failures
<a name="suggestions-6.3.4-notify-it-operations-and-help-desk-teams-of-any-etl-job-failures."></a>

 Normally, the IT operations team should be the first contact for production workload failures. The IT operations team troubleshoots and attempts to recover the failed job, if possible. It is also helpful to notify the IT help desk of system failures that have an end user impact. These can include issues with the data warehouse used by the business intelligence (BI) analysts. 

 

## Suggestions 6.3.5 – Notify downstream systems of data freshness
<a name="suggestion-6.3.5"></a>

 Monitor data updates as this gives process and application information when data becomes stale. Stale data can lead to misreporting due to the correct values being stale and not current. 