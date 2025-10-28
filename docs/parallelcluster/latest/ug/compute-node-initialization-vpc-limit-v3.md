# Seeing `An error occurred (VcpuLimitExceeded)` in `slurm_resume.log`

when I fail to run a job, or in `clustermgtd.log`, when I fail to create a cluster

Check the vCPU limits on your account for the specific Amazon EC2 instance type that you are using. If you see zero or fewer vCPUs than you are
requesting, request an increase for your limits. For information about how to view current limits and request new limits, see [Amazon EC2 service quotas](../../../AWSEC2/latest/UserGuide/ec2-resource-limits.md "../../../AWSEC2/latest/UserGuide/ec2-resource-limits.md") in the
_Amazon EC2 User Guide_.
