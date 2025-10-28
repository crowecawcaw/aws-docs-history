# Chatting about your telemetry and operations

Amazon Q analyzes your CloudWatch telemetry and operational data to help manage your AWS environment. It
retrieves resource health information, monitors alarms, and provides troubleshooting guidance. When
you ask questions, Amazon Q may prompt you for specific details like resource names and time ranges to
ensure accurate assistance.

**AWS service health check:** Evaluate the health of resources of
specified AWS services, assisting customers in troubleshooting and resolving issues or errors they
encounter with these resources.

- Is my Lambda function X healthy?
- Is anything wrong with my Amazon ECS clusters?
- Help me troubleshoot my DynamoDB tables between time X and Y.
- Investigate anomalies related to Amazon S3 between time X and Y.
  **Alarm troubleshooting:** Identifies alarms in Alarm state and the
  underlying telemetry that triggered the alarm, helping customers diagnose the reasons behind the
  alarm/alert/pages.

- Why is my alarm with name X firing?
  **Application Signals specific troubleshooting:** Analyzes
  CloudWatch Application Signals service-level objectives and indicators to determine the overall health of a service,
  enabling you to assess and maintain application performance.

- Is my Service X in environment Y healthy?
  For more information about how Amazon Q analyzes your CloudWatch telemetry and operational data, see
  _CloudWatch investigations_ in the [Amazon CloudWatch User Guide](../../../AmazonCloudWatch/latest/monitoring/Investigations.md "../../../AmazonCloudWatch/latest/monitoring/Investigations.md").
