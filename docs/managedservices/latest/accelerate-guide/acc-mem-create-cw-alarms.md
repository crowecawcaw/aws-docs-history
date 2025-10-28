# Creating additional CloudWatch alarms for Accelerate

You can create additional CloudWatch alarms for AMS Accelerate using custom CloudWatch metrics and alarms for Amazon EC2 instances.

Produce your application monitoring script and custom metric. For more information and access to example scripts, see
[Monitoring Memory and Disk Metrics for Amazon EC2 Linux Instances](../../../AWSEC2/latest/UserGuide/mon-scripts.md "../../../AWSEC2/latest/UserGuide/mon-scripts.md").

The CloudWatch monitoring scripts for Linux Amazon EC2 instances demonstrate how to produce and consume custom CloudWatch metrics. These sample Perl scripts comprise a
fully functional example that reports memory, swap, and disk space utilization metrics for a Linux instance.

###### Important

AMS Accelerate does not monitor CloudWatch alarms created by you.
