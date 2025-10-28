# Monitoring AWS Elemental MediaConnect with Amazon CloudWatch

metrics

You can monitor AWS Elemental MediaConnect using CloudWatch, which collects raw data and processes it
into readable, near real-time metrics. These metrics are kept for 15 months, so that you
can access historical information and gain a better perspective on how your web
application or service is performing. Most MediaConnect metrics can be accessed in periods as
short as one second. You can also set alarms that watch for certain thresholds, and send
notifications or take actions when those thresholds are met. For more information, see
the [Amazon CloudWatch User Guide](../../../AmazonCloudWatch/latest/monitoring.md "../../../AmazonCloudWatch/latest/monitoring.md").

You can view CloudWatch metrics for your flows directly on the MediaConnect console. On the
console, you can view these metrics in periods as short as one second or as long as 30
minutes.

###### Note

MediaConnect Gateway metrics are not available in high resolution periods (one second). You must
select a period of at least one minute.
