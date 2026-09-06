

# Best practice 6.2 – Monitor analytics systems to detect analytics or extract, transform and load (ETL) job failures
<a name="best-practice-6.2---monitor-analytics-systems-to-detect-analytics-or-etl-job-failures."></a>

 Detect extract, transform, and load (ETL) and analytics job failures as soon as possible. Pinpointing where and how the error occurred is critical for notiﬁcations and corrective actions. 

## Suggestion 6.2.1– Monitor and track job errors from different levels, including infrastructure, ETL workﬂow, and ETL application code
<a name="suggestion-6.2.1---monitor-and-track-job-errors-from-different-levels"></a>

 Failures can occur at all levels of the analytics system. Each task in the analytics workload should be instrumented to provide metrics indicating the health of the task. Monitor the emitted metrics and raise alarms if any components fail. Create dashboards to visualize metrics and govern access to them. 

 For more details, refer to the following: 
+ [ Visualize data warehouse metrics: Query and visualize Amazon Redshift operational metrics using the Amazon Redshift plugin for Grafana ](https://aws.amazon.com/blogs/big-data/query-and-visualize-amazon-redshift-operational-metrics-using-the-amazon-redshift-plugin-for-grafana/)
+ [ Visualize Amazon EMR metrics: Monitor Amazon EMR on Amazon EKS with Amazon Managed Prometheus and Amazon Managed Grafana ](https://aws.amazon.com/blogs/mt/monitoring-amazon-emr-on-eks-with-amazon-managed-prometheus-and-amazon-managed-grafana/)

## Suggestion 6.2.2 – Establish end-to-end monitoring for the complete analytics and ETL pipeline
<a name="suggestion-6.2.2---establish-end-to-end-monitoring-for-the-complete-analytics-and-etl-pipeline."></a>

 End-to-end monitoring allows tracking the ﬂow of data as it passes through the analytics system. In many cases, data processing might be dependent on application logic, such as sampling a subset of data from a data stream to check accuracy. Properly identifying and monitoring the end-to-end ﬂow of data allows detecting at which step the analytics and ETL job fails. 

## Suggestions 6.2.3 – Determine what data was processed when the job failed
<a name="suggestions-6.2.3---determine-what-data-was-processed-when-the-job-failed."></a>

 Failures in data processing systems can cause data integrity or data quality issues. Determine what data was being processed at the time of failure and perform quality checks of both the input and output data. If possible, roll-back the committed data and restart your job. 

 For more details, see AWS Glue: [Overview of Data Quality in AWS Glue](https://docs.aws.amazon.com/glue/latest/dg/workflows_overview.html). 

## Suggestions 6.2.4 – Classify the severity of the job failures based on the type of failure and the business impact
<a name="suggestions-6.2.4---classify-the-severity-of-the-job-failures-based-on-the-type-of-failure-and-the-business-impact."></a>

 Classifying the severity of different job failures helps you prioritize remediation and guide the notiﬁcation requirements to key stakeholders. Classification of jobs can be agreed upon based on importance and the impact the failure has on meeting internal and external SLAs. 