

# Creating additional CloudWatch alarms for Accelerate
<a name="acc-mem-create-cw-alarms"></a>

You can create additional CloudWatch alarms for AMS Accelerate using custom CloudWatch metrics and alarms for Amazon EC2 instances.

Produce your application monitoring script and custom metric. For more information and access to example scripts, see [Monitoring Memory and Disk Metrics for Amazon EC2 Linux Instances](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/mon-scripts.html).

The CloudWatch monitoring scripts for Linux Amazon EC2 instances demonstrate how to produce and consume custom CloudWatch metrics. These sample Perl scripts comprise a fully functional example that reports memory, swap, and disk space utilization metrics for a Linux instance.

**Important**  
AMS Accelerate does not monitor CloudWatch alarms created by you.