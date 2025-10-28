# CloudWatch integration with X-Ray

AWS X-Ray integrates with [CloudWatch Application Signals](../../../AmazonCloudWatch/latest/monitoring/CloudWatch-Application-Monitoring-Sections.md "../../../AmazonCloudWatch/latest/monitoring/CloudWatch-Application-Monitoring-Sections.md"),
CloudWatch RUM, and CloudWatch Synthetics to make it easier to monitor the health of your applications. Enable your application
for Application Signals to monitor and troubleshoot the operational health of your services, client pages,
Synthetics canaries, and service dependencies.

By correlating CloudWatch metrics, logs, and X-Ray traces, the X-Ray trace map provides an end-to-end view of
your services to help you quickly pinpoint performance bottlenecks and identify impacted users.

With CloudWatch RUM, you can perform real user monitoring to collect and view client-side data about your web
application performance from actual user sessions in near-real time. With AWS X-Ray and CloudWatch RUM, you can analyze
and debug the request path starting from end users of your application through downstream AWS managed services.
This helps you identify latency trends and errors that impact your end users.

###### Topics

- [CloudWatch RUM and AWS X-Ray](xray-services-RUM.md "xray-services-RUM.md")
- [Debugging CloudWatch synthetics canaries using X-Ray](xray-services-cloudwatch-synthetics.md "xray-services-cloudwatch-synthetics.md")
