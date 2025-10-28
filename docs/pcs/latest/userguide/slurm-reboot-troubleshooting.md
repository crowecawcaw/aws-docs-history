# Troubleshooting Slurm reboot issues in

AWS PCS

When you encounter node reboot problems, first check the node status using `scontrol
 show node `nodename``. Then examine CloudWatch logs for both Slurm
(slurmctld and slurmd) and system logs to identify potential errors.

For basic troubleshooting, verify network connectivity, check security group settings, and
ensure all required services are running after the reboot. If problems persist after basic
troubleshooting steps, contact AWS Support. When reaching out to support, provide relevant log
excerpts, node status information, and a timeline of the reboot attempt to help expedite the
resolution process.

## Additional resources

- For monitoring AWS PCS instances using CloudWatch, see [Monitoring AWS PCS instances using Amazon CloudWatch](monitoring-cloudwatch_instances.md "monitoring-cloudwatch_instances.md").
- For general troubleshooting, see [Troubleshooting problems in AWS Parallel Computing Service](troubleshooting.md "troubleshooting.md").
- For Slurm documentation, see [Slurm Troubleshooting Guide](https://slurm.schedmd.com/troubleshoot.html "https://slurm.schedmd.com/troubleshoot.html").
